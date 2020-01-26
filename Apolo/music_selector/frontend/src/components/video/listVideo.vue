<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <br>
                <br>
                <br>
                <h1 align="center">Listado con todos los video musicales almacenados en la DB</h1>
                <br>
                <br>
                <br>
                <div class="col-md-12">
                    <b-table striped hover :items="videos" :fields="fields" >
                    </b-table>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data () {
        return {
            fields: [
                { key: 'video_id', label: 'Id' },
                { key: 'video_title', label:'Título' },
                { key: 'video_type', label: 'Género' },
                { key: 'moods', label: 'Emoción Etiquetada' },
                { key: 'predicted_moods', label: 'Emoción Recomendada' },
                { key: 'labeled', label: 'Etiqueta' },
            ],
        
            videos: []
        }
    },
    methods: {

        /**
         * Permite obtener un json con todos los datos que existen en a DB
         */
        getVideos () {
            const path = 'http://localhost:8000/api/v2/new-videos/'
            axios.get(path).then((response) => {
                this.videos = response.data
            })
            .catch((error) => {
                console.log(error)
            })
        }
    },

    /**
     * Ejecuta el metodo getVideos() de inmiediato
     */
    created(){
        this.getVideos()
    }
}
</script>