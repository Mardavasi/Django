<template>
  <div>

     <!--navbar-->
    <NavbarComponent  @getSearchText="search"/>

    <!-- integramos el NavigationComponent para poder lograr filtrar los categorias -->
    <NavigationComponent @getCategoryID="categoryID" />
    <div class="mb-3" v-if="searchTextRule">
      <h3>productos <strong>{{ searchTextRule }}</strong></h3>
      <button class="btn btn-lg btn-success" @click="resetFilter">Mostrar todos los productos</button>
      <div class=" alert alert-warning mt-3" v-if="filteredProducts.length === 0">No existen productos para <strong>{{
        searchTextRule }}</strong></div>
    </div>
    <div class="mb-3" v-if="categoryReceived">
      <h3>productos <strong>{{ categoryReceived }}</strong></h3>
      <button class="btn btn-lg btn-success" @click="resetFilter">Mostrar todos los productos</button>
      <div class=" alert alert-warning mt-3" v-if="filteredProducts.length === 0">No existen productos para <strong>{{
        categoryReceived }}</strong></div>
    </div>
    <div>
      <div class="row row-cols-1 row-cols-md-3 g-4">
        <div class="col" v-for="product in filteredProducts" :key="product.id">
          <div class=" card text-center">
            <img :src="product.image" class="card-img-top" alt="imagen de {{ product.name }}">
            <div class="card-body">
              <h5 class="card-tittle">{{ product.name }}</h5>
              <h6 class="card-subtitle mb-2 text-body-secondary">{{ product.category_name }}</h6>
              <p class=" card-text">{{ product.description }}</p>
            </div>
            <div class="card-footer text-danger">
              {{ product.price }} - Por {{ product.price_type_description }}
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import NavigationComponent from '@/components/NavigationComponent.vue';
import NavbarComponent from '@/components/NavbarComponent.vue';
import { ref, onMounted } from 'vue';

const products = ref([])
const filteredProducts = ref([])
const categoryReceived = ref(null)
const searchTextRule = ref(null)

// Función para realizar una búsqueda en los productos según el texto proporcionado
const search = (searchText) => {
  // Reiniciar la categoría recibida a null al realizar una búsqueda
  categoryReceived.value = null;
  // Establecer el texto de búsqueda actual
  searchTextRule.value = searchText;

  if (searchText) {
    // Filtrar productos según el nombre o descripción que coincida con el texto de búsqueda
    filteredProducts.value = products.value.filter(product => {
      const productName = product.name.toLowerCase();
      const productDescription = product.description.toLowerCase();
      const searchTerm = searchText.toLowerCase();

      return productName.includes(searchTerm) || productDescription.includes(searchTerm);
    });
  } else {
    // Si no hay texto de búsqueda, mostrar todos los productos sin filtrar
    filteredProducts.value = products.value;
  }
}

// Función para filtrar productos por categoría
const categoryID = (categoryID, categoryName) => {
  // Reiniciar el texto de búsqueda al seleccionar una categoría
  searchTextRule.value = null;
  // Establecer la categoría recibida actual
  categoryReceived.value = categoryName;

  if (categoryID) {
    // Filtrar productos según la categoría seleccionada
    filteredProducts.value = products.value.filter((product) => product.category === categoryID);
  } else {
    // Si no hay categoría seleccionada, mostrar todos los productos sin filtrar
    filteredProducts.value = products;
  }
}

// Función para restablecer todos los filtros y mostrar todos los productos
const resetFilter = () => {
  categoryReceived.value = null;
  filteredProducts.value = products.value;
  searchTextRule.value = null;
}

// Cargar productos desde la API al montar el componente
onMounted(() => {
  axios.get('http://127.0.0.1:8000/api/products/')
    .then(response => {
      // Almacenar productos en la referencia reactiva y mostrar todos los productos inicialmente
      products.value = response.data;
      filteredProducts.value = products.value;
    })
    .catch(error => {
      console.log(error);
    });
});





</script>
<style>
.card {
  border: 2px solid grey !important;
}
</style>
