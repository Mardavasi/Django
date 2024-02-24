<template>
    <section class="mt-5 text-center mx-auto">
        <h1 class="text-success">Panaderia y Pasteleria Peter Pan</h1>
        <img class="img-fluid" :src="require('@/assets/img/logo.png')" alt="">
        <div class="mt-3" v-if="$route.path !== '/about'">
            <button type="button" class="btn btn-success" v-for="category in categories" :key="category.id"
                @click="getCategory(category.id, category.name)">{{ category.name
                }}</button>

        </div>
        <hr>
    </section>
</template>

<script setup>
//Instalamos axios para permitir la conexion con el backend de django y vue
import axios from 'axios';
import { ref, defineEmits, onMounted } from 'vue';

// Crear una referencia reactiva para almacenar las categorías
const categories = ref([]);

// Definir eventos emitidos usando defineEmits
const emits = defineEmits(['getCategoryID']);

// Función para obtener la categoría seleccionada y emitir un evento
const getCategory = (id, name) => {
    // Emitir el evento 'getCategoryID' con la id y el nombre de la categoría
    emits('getCategoryID', id, name);
}

// Cargar las categorías desde la API al montar el componente
onMounted(() => {
    axios.get('http://127.0.0.1:8000/api/categories/')
        .then(response => {
            // Almacenar las categorías en la referencia reactiva
            categories.value = response.data;
        })
        .catch(error => {
            console.log(error);
        });
});


</script>

<style>
button {
    margin-right: 5px;
}

button+button,
button:first-child {
    margin-left: 5px;
}

@media (max-width:768px) {
    button {
        width: 100%;
        margin: 0 0 5px !important;
        box-sizing: border-box;
    }
}
</style>