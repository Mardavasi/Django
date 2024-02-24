<template>
    <section class="mt-5 text-center mx-auto">
        <h1 class="text-success">Panaderia y Pasteleria Peter Pan</h1>
        <img class="img-fluid" :src="require('@/assets/img/logo.png')" alt="">
        <div class="mt-3" v-if="$route.path !== '/about'">
            <button type="button" class="btn btn-success" v-for="category in categories" :key="category.id" @click ="getCategoryID(category.id,category.name)" >{{ category.name
            }}</button>

        </div>
        <hr>
    </section>
</template>

<script>
//Instalamos axios para permitir la conexion con el backend de django y vue
import axios from 'axios';
export default {
    name: 'NavigationComponent',

    data() {
        return {
            categories: [],
            categoryID: null,
            categoryName: null
        }
    },
    methods: {
        getCategoryID(categoryID, categoryName) {
            this.$emit('getCategoryID', categoryID,categoryName);
        }
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/api/categories/')
            .then(response => {
                this.categories = response.data;
            })
            .catch(error => {
                console.log(error);
            });
    },
}
</script>

<style>
button {
    margin-right: 5px;
}
button + button, button:first-child {
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