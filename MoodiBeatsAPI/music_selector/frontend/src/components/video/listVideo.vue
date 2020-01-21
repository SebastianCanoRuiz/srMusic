<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Listado de Videos</h2>

                <div class="col-md-12">
                    <b-table striped hover :items="videos" :fields="fields">
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
                { key: 'video_title', label:'Título' },
                { key: 'video_id', label: 'ID' },
                { key: 'moods', label: 'Emoción Etiquetada' },
                { key: 'predicted_moods', label: 'Emoción Recomendada' },
            ],
        
            videos: []
        }
    },
    methods: {
        getVideos () {

            const path = 'http://localhost:8000/api/v1.0/new-videos/'
            axios.get(path).then((response) => {
                this.videos = response.data
            })
            .catch((error) => {
                console.log(error)
            })
        }
    },

    created(){
        this.getVideos()
    }
}
</script>