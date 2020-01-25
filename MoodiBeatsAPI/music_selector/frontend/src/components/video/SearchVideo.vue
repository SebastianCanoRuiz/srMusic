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
                    <b-alert
                        :show="dismissCountDown"
                        dismissible
                        v-bind:variant="tipoAlerta"
                        @dismissed="dismissCountDown=0"
                        @dismiss-count-down="countDownChanged">
                        {{ mensaje }}
                    </b-alert>
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
                                    <b-button class="form-control my-2 w-25" type="submit" > Buscar </b-button>
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

		<br>
<!-- ************************************** RECOMENDACIONES ******************************************************** -->
		<h4>Basado en tu búsqueda y video musical actual te recomendamos los siguientes: </h4>
        <hr>
		<div class="row">

			<div class="col-md-6" style="padding-left: 5px;padding-right: 5px;">
          <strong>ID:</strong> {{ recomendacion1.video_id }}
          <br>
          <strong>Título:</strong> {{ recomendacion1.video_title  }}
          <br>
        	<iframe v-bind:class="responsive" v-bind:width="ancho" v-bind:height="200" v-bind:src="url + recomendacion1.video_id"
						v-bind:frameborder="borde" v-bind:allowfullscreen="pcompleta">
					</iframe>
			</div>

			<div class="col-md-6" style="padding-left: 5px;padding-right: 5px;">
          <strong>ID:</strong> {{ recomendacion2.video_id }}
          <br>
          <strong>Título:</strong> {{ recomendacion2.video_title  }}
        <br>
        <iframe v-bind:class="responsive" v-bind:width="ancho" v-bind:height="200" v-bind:src="url + recomendacion2.video_id"
						v-bind:frameborder="borde" v-bind:allowfullscreen="pcompleta">
				</iframe>
			</div>
      <hr>
			<div class="col-md-6" style="padding-left: 5px;padding-right: 5px;">
          <strong>ID:</strong> {{ recomendacion3.video_id }}
          <br>
          <strong>Título:</strong> {{ recomendacion3.video_title  }}
        <br>
        <iframe v-bind:class="responsive" v-bind:width="ancho" v-bind:height="200" v-bind:src="url + recomendacion3.video_id"
						v-bind:frameborder="borde" v-bind:allowfullscreen="pcompleta">
				</iframe>
			</div>

			<div class="col-md-6" style="padding-left: 5px;padding-right: 5px;">
          <strong>ID:</strong> {{ recomendacion4.video_id }}
          <br>
          <strong>Título:</strong> {{ recomendacion4.video_title  }}
        <br>
        <iframe v-bind:class="responsive" v-bind:width="ancho" v-bind:height="200" v-bind:src="url + recomendacion4.video_id"
						v-bind:frameborder="borde" v-bind:allowfullscreen="pcompleta">
				</iframe>
			</div>
      <hr>
      <div class="col-md-6" style="padding-left: 5px;padding-right: 5px;">
          <strong>ID:</strong> {{ recomendacion5.video_id }}
          <br>
          <strong>Título:</strong> {{ recomendacion5.video_title  }}
        <br>
        <iframe v-bind:class="responsive" v-bind:width="ancho" v-bind:height="200" v-bind:src="url + recomendacion5.video_id"
						v-bind:frameborder="borde" v-bind:allowfullscreen="pcompleta">
				</iframe>
			</div>

      <div class="col-md-6" style="padding-left: 5px;padding-right: 5px;">
          <strong>ID:</strong> {{ recomendacion6.video_id }}
          <br>
          <strong>Título:</strong> {{ recomendacion6.video_title  }}
        <br>
        <iframe v-bind:class="responsive" v-bind:width="ancho" v-bind:height="200" v-bind:src="url + recomendacion6.video_id"
						v-bind:frameborder="borde" v-bind:allowfullscreen="pcompleta">
				</iframe>
			</div>
		</div>

		<hr style="border: 1px dashed #999;">

		<footer align="center">
			<p>Desarrollado por <a href="#" target="_blank">Jhon Sebastian Cano Ruiz - Johan Steeven Sanchez Sepúlveda</a></p>
      <p align="center">2020</p>
      
		</footer>

	</div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      //Variables para las alertas
      dismissSecs: 5,
      dismissCountDown: 0,
      mensaje: "",
      tipoAlerta: "warning",

      //Variables para los selct y el input de búsqueda
      selectEmocion: null,
      selectGenero: null,
      inputVariable: null,

      //Variable para guardar el reponse de la peticion get http
      respuesta: [],
      //Variable con todos los generos que se tiene, usado por el select de genero
      generos: [
        { value: null, text: "Elige..." },
        { value: "ROCK", text: "Rock" },
        { value: "BACHATA", text: "Bachata" },
        { value: "RANCHERA", text: "Ranchera" },
        { value: "CUMBIA", text: "Cumbia" },
        { value: "BALADAS", text: "Balada" },
        { value: "SALSA", text: "Salsa" },
        { value: "POP", text: "Pop" },
        { value: "VALLENATO", text: "Vallenato" },
        { value: "REGGAE", text: "Reggae" },
        { value: "RAP", text: "Rap" },
        { value: "METAL", text: "Metal" },
      ],
      //Variable con todos las emociones que se tienen, usado por el select de emoción
      emociones: [
        { value: null, text: "Elige..." },
        { value: 'HAPPY', text: "Feliz" },
        { value: 'IN-LOVE', text: "Enamorado" },
        { value: 'SAD', text: "Triste" },
        { value: 'ANGRY', text: "Enojado" }
      ],
      
      //Variables usadas por el reproductor
      responsive: "embed-responsive-item",
      ancho: "100%",
      alto: "400",
      url: "https://www.youtube.com/embed/",
      video: "fBI4-eTBMqo",
      borde: "1",
      pcompleta: null,

      //VARIABLES CON LOS DATOS DE LAS RECOMENDACIONES
      recomendacion1: [],
      recomendacion2: [],
      recomendacion3: [],
      recomendacion4: [],
      recomendacion5: [],
      recomendacion6: [],
    };
  },

methods: {

    //Disminuye una variable hasta 0 - Metodo recuperado de la Api de Bootstrap-Vue
    countDownChanged(dismissCountDown) {
        this.dismissCountDown = dismissCountDown
      },
    
    //Muestra una Alerta que desaparece en determinado tiempo - Metodo recuperado de la Api de Bootstrap-Vue
    showAlert() {
        this.dismissCountDown = this.dismissSecs
      },
    //end 

    generarRecomedaciones(response){
              let aleatorio = Math.round(Math.random()* (response.data.length - 1))
              //console.log("Numero Aleatorio-->" + aleatorio)
              
              this.recomendacion1 = {
                video_id:response.data[aleatorio].video_id, 
                video_title:response.data[aleatorio].video_title, 
                video_type:response.data[aleatorio].video_type,
                predicted_moods: response.data[aleatorio].predicted_moods,}
              
              aleatorio = Math.round(Math.random()* (response.data.length - 1))
              //console.log("Numero Aleatorio-->" + aleatorio)
              
              this.recomendacion2 = {
                video_id:response.data[aleatorio].video_id, 
                video_title:response.data[aleatorio].video_title, 
                video_type:response.data[aleatorio].video_type,
                predicted_moods: response.data[aleatorio].predicted_moods,}

              aleatorio = Math.round(Math.random()* (response.data.length - 1))
              //console.log("Numero Aleatorio-->" + aleatorio)

              this.recomendacion3 = {
                video_id:response.data[aleatorio].video_id, 
                video_title:response.data[aleatorio].video_title, 
                video_type:response.data[aleatorio].video_type,
                predicted_moods: response.data[aleatorio].predicted_moods,}

              aleatorio = Math.round(Math.random()* (response.data.length - 1))
              //console.log("Numero Aleatorio-->" + aleatorio)

              this.recomendacion4 = {
                video_id:response.data[aleatorio].video_id, 
                video_title:response.data[aleatorio].video_title, 
                video_type:response.data[aleatorio].video_type,
                predicted_moods: response.data[aleatorio].predicted_moods,}

              aleatorio = Math.round(Math.random()* (response.data.length - 1))
              //console.log("Numero Aleatorio-->" + aleatorio)

              this.recomendacion5 = {
                video_id:response.data[aleatorio].video_id, 
                video_title:response.data[aleatorio].video_title, 
                video_type:response.data[aleatorio].video_type,
                predicted_moods: response.data[aleatorio].predicted_moods,}

              aleatorio = Math.round(Math.random()* (response.data.length - 1))
              //console.log("Numero Aleatorio-->" + aleatorio)

              this.recomendacion6 = {
                video_id:response.data[aleatorio].video_id, 
                video_title:response.data[aleatorio].video_title, 
                video_type:response.data[aleatorio].video_type,
                predicted_moods: response.data[aleatorio].predicted_moods,}
    },

    //Genera una alerta, tipo 1 = success, tipo 2 = warning. Cambia el mensaje entre tipos
    generarAlerta(tipo) {
      if(tipo == 1 ){
        this.mensaje = "Las recomendaciones se generaron con exito.",
        this.tipoAlerta = "success"
      } else if(tipo == 2){
        this.mensaje = "No se han encontrado datos que coincidan con su búsqueda.",
        this.tipoAlerta = "warning"
      } else {
        this.mensaje = "Ingrese algún parametro para poder generar recomendaciones.",
        this.tipoAlerta = "info"
      }
      this.showAlert()
    },
    
    onSubmit(evt) {
      evt.preventDefault();
      var path = ``;

      if (this.selectGenero == null && this.selectEmocion == null && this.inputVariable != null) {
        //Consulta para recomendaciones
        path = `http://localhost:8000/api/v2/songs-name/${this.inputVariable}`;
        axios
          .get(path, { responseType: "json" })
          .then(response => {
            this.respuesta = response.data;
            this.video = this.respuesta[0].video_id;

          //Consulta para recomendaciones
          path = `http://localhost:8000/api/v2/songs-mood/${this.respuesta[0].predicted_moods}/`;
          axios
            .get(path, { responseType: "json" })
            .then(response => {
              this.generarRecomedaciones(response)
              this.generarAlerta(1)
              })
            .catch(error => {
              console.log("001R-->" + error);

            });
          })
          .catch(error => {
            this.generarAlerta(2)
            console.log("001B-->" + error);
          });
      } else if (this.selectGenero == null && this.selectEmocion != null && this.inputVariable == null) {
          //Consulta para recomendaciones
          path = `http://localhost:8000/api/v2/songs-mood/${this.selectEmocion}/`;
          axios
            .get(path, { responseType: "json" })
            .then(response => {
              this.generarRecomedaciones(response)
              this.generarAlerta(1)
              })
            .catch(error => {
              this.generarAlerta(2)
              console.log("010R-->" + error);
            });
      } else if (this.selectGenero == null && this.selectEmocion != null && this.inputVariable != null) {
          path = `http://localhost:8000/api/v2/songs-name-mood/${this.inputVariable}/${this.selectEmocion}/`;
          axios
            .get(path, { responseType: "json" })
            .then(response => {
              this.respuesta = response.data;
              this.video = this.respuesta[0].video_id;

            //Consulta para recomendaciones
            path = `http://localhost:8000/api/v2/songs-mood/${this.respuesta[0].predicted_moods}/`;
            axios
              .get(path, { responseType: "json" })
              .then(response => {
                this.generarRecomedaciones(response)
                this.generarAlerta(1)
                })
              .catch(error => {
                console.log("011R-->" + error);
              });
            })
            .catch(error => {
              this.generarAlerta(2)
              console.log("011B-->" + error);
            });

      } else if (this.selectGenero != null && this.selectEmocion == null && this.inputVariable == null) {
        //Consulta para recomendaciones
          path = `http://localhost:8000/api/v2/songs-genre/${this.selectGenero}/`;
          axios
            .get(path, { responseType: "json" })
            .then(response => {
              this.generarRecomedaciones(response)
              this.generarAlerta(1)
              })
            .catch(error => {
              this.generarAlerta(2)
              console.log("100R-->" + error);
            });
      } else if (this.selectGenero != null && this.selectEmocion == null && this.inputVariable != null) {
        path = `http://localhost:8000/api/v2/songs-name-genre/${this.inputVariable}/${this.selectGenero}/`;
          axios
            .get(path, { responseType: "json" })
            .then(response => {
              this.respuesta = response.data;
              this.video = this.respuesta[0].video_id;

            //Consulta para recomendaciones
            path = `http://localhost:8000/api/v2/songs-mood/${this.respuesta[0].predicted_moods}/`;
            axios
              .get(path, { responseType: "json" })
              .then(response => {
                this.generarRecomedaciones(response)
                this.generarAlerta(1)
                })
              .catch(error => {
                console.log("011R-->" + error);
              });
            })
            .catch(error => {
              this.generarAlerta(2)
              console.log("011B-->" + error);
            });

      } else if (this.selectGenero != null && this.selectEmocion != null && this.inputVariable == null) {
            //Consulta para recomendaciones
            path = `http://localhost:8000/api/v2/songs-genre-mood/${this.selectGenero}/${this.selectEmocion}/`;
            axios
              .get(path, { responseType: "json" })
              .then(response => {
                this.generarRecomedaciones(response)
                this.generarAlerta(1)
                })
            .catch(error => {
              this.generarAlerta(2)
              console.log("110R-->" + error);
            });

      } else if (this.selectGenero != null && this.selectEmocion != null && this.inputVariable != null) {
          path = `http://localhost:8000/api/v2/songs-name-mood-genre/${this.inputVariable}/${this.selectEmocion}/${this.selectGenero}/`;
          axios
            .get(path, { responseType: "json" })
            .then(response => {
              this.respuesta = response.data;
              this.video = this.respuesta[0].video_id;

            //Consulta para recomendaciones
            path = `http://localhost:8000/api/v2/songs-mood/${this.respuesta[0].predicted_moods}/`;
            axios
              .get(path, { responseType: "json" })
              .then(response => {
                this.generarRecomedaciones(response)
                this.generarAlerta(1)
                })
              .catch(error => {
                console.log("111R-->" + error);
              });
            })
            .catch(error => {
              this.generarAlerta(2)
              console.log("111B-->" + error);
            });

      } else {
        this.generarAlerta(3)
       };
    }
  }
}
</script>

<style lang="css" scoped>
</style>