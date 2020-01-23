<template lang="html">  

	<div class="container">

        <br>
		<div class="row">
			<div class="col-md-12">
				<div id="yt" align="center">

					<iframe v-bind:class="responsive" v-bind:width="ancho" v-bind:height="alto" v-bind:src="url + video"
						v-bind:frameborder="borde" v-bind:allowfullscreen="pcompleta">
					</iframe>
                    <hr>
                    <!-- ************************************************************************************ -->
                    <div >
                        <b-form inline @submit="onSubmit" > 

                                    <label class="mr-sm-2" for="inline-form-custom-select-pref">Género</label>
                                    <!-- Este es el select con las opciones de genero -->
                                    <b-form-select
                                        class="mb-2 mr-sm-2 mb-sm-0"
                                        v-model="selectGenero"
                                        :options="generos"
                                        id="inline-form-custom-select-pref">
                                    </b-form-select>

                                    <hr>
                                    <label class="mr-sm-2" for="inline-form-custom-select-pref">Emoción</label>
                                    <!-- Este es el select con las opciones de emoción -->
                                    <b-form-select
                                        class="mb-2 mr-sm-2 mb-sm-0"
                                        v-model="selectEmocion"
                                        :value="null"
                                        :options="emociones"
                                        id="inline-form-custom-select-pref">
                                    </b-form-select>
                                    <hr>
                                    <b-form-input v-model="inputVariable" type="text" class="form-control input-lg w-25" placeholder="Canción"></b-form-input> 
                                    <hr>             
                                    <b-button class="form-control my-2 w-25" type="submit"> Buscar </b-button>
                        </b-form>
                        </div>
                    <!-- ************************************************************************************ -->
					<p style="text-align: center; margin-top: 20px; margin-bottom: 20px;">
						<strong>El ID del video actual es: </strong> {{ video }}
                        <br>
                        <strong> La emoción es: </strong> {{ selectEmocion }}
                        <br>
                        <strong> El género es: </strong> {{ selectGenero }}
                        <br>
                        <strong> La prueba generó: </strong> {{ respuesta }}
                        <br>
                        <strong> La prueba 2 generó: </strong> {{ inputVariable }}
					</p>

				</div>
			</div>
		</div>

		<hr style="border: 1px dashed #999;" />

		<h3>Basado en tu búsqueda y video musical actual te recomendamos los siguientes: </h3>
        <hr>
		<div class="row">

			<div class="col-md-3">
				<strong>ID:</strong> 3f83zCFYV9Y
				<br>
				<strong>Título:</strong> Marketing Digital: Segmentar campaña por Departamentos en Perú con Google
				Adwords.
			</div>

			<div class="col-md-3">
				<strong>ID:</strong> v25gR7PKp3U
				<br>
				<strong>Título:</strong> Facebook: Como publicar contenido en varios idiomas.
			</div>

			<div class="col-md-3">
				<strong>ID:</strong> W2g3LkPBPjc
				<br>
				<strong>Título:</strong> Programar una publicación en WordPress.
			</div>

			<div class="col-md-3">
				<strong>ID:</strong> FkQruRGpgGk
				<br>
				<strong>Título:</strong> Videojuegos: Transmisión en vivo, impresiones de God of War Remastered en PS4.
			</div>
		</div>

		<br>

		<footer align="center">
			Desarrollado por <a href="#" target="_blank">Jhon Sebastian Cano Ruiz - Johan Steeven Sanchez Sepúlveda</a>
		</footer>

	</div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      selectGenero: null,
      selectEmocion: null,
      generos: [
        { value: null, text: "Elige..." },
        { value: "SALSA", text: "Salsa" },
        { value: "MERENGUE", text: "Merengue" },
        { value: "CUMBIA", text: "Cumbia" }
      ],
      emociones: [
        { value: null, text: "Elige..." },
        { value: "HAPPY", text: "Feliz..." },
        { value: "IN-LOVE", text: "Enamorado..." },
        { value: "SAD", text: "Triste..." },
        { value: "ANGRY", text: "Enojado..." }
      ],
      responsive: "embed-responsive-item",
      ancho: "100%",
      alto: "400",
      url: "https://www.youtube.com/embed/",
      video: "fBI4-eTBMqo",
      borde: "1",
      pcompleta: null,

      inputVariable: null,
      respuesta: []
    };
  },

  methods: {

    onSubmit(evt) {
      evt.preventDefault();
      
      const path = `http://localhost:8000/api/v2/songs-name/${this.inputVariable}`;
      axios.get(path, {responseType: 'json'}).then(response => {
          this.respuesta = response.data
          this.video = this.respuesta[0].video_id  
        })
        .catch(error => {
          console.log("*************************** -->" + error)
        }); 
    }
  }
};
</script>
    <style lang="css" scoped>
</style>