<template>
  <div id="app">
    <div>
      <nav class="nav">
        <div class="container">
          <div class="logo">
            <a href="./">
              <b-icon icon="music-player-fill" variant="ligth"></b-icon>
              <strong>APOLO</strong>
            </a>
          </div>
          <div id="mainListDiv" class="main_list">
            <ul class="navlinks">
              <li>
                <a class="nav-link nav-social" href="#">
                  <i class="fa fa-facebook" aria-hidden="true"></i>
                </a>
              </li>
              <li>
                <a href>
                  <b-icon icon="info" variant="ligth"></b-icon>
                  <strong>Info</strong>
                </a>
              </li>
              <li>
                <a href="./video">
                  <b-icon icon="documents" variant="ligth"></b-icon>
                  <strong>List DB</strong>
                </a>
              </li>
            </ul>
          </div>
          <span class="navTrigger">
            <i></i>
            <i></i>
            <i></i>
          </span>
        </div>
      </nav>

      <section class="home">
        <br>
        <div clas="mt-4">
          <div class="inner cover">
            <h1 class="cover-heading" font-scale="7">La aventura musical Inicia</h1>
            <p class="lead cover-copy">
            El Prototipo del Sistema de Recomendación Musical <strong>APOLO</strong> te recomienda música basada en tus emociones
            Apolo se preocupa por cómo te sientes.
            <br>
            Más de 1000 videos musicales libres de derechos de autor de YouTube. 
            <br>
            Disfrútalo :3
            </p>
            <br>
            <p class="lead">
              <a href="#contenido">                   
              <button type="button" class="btn btn-lg btn-default btn-notify">Adelante!</button>
              </a>
            </p>
          </div>
          <div>
            <div class="mastfoot">
              <div class="inner">
                <p>
                  &copy; Prototipo SR-Musical Apolo. Diseñado por:<br>
                  <a href="" target="_blank" style="color:#fff">Jhon Sebastian Cano Ruiz & Johan Steeven Sanchez Sepúlveda</a>.
                  <br>
                  2020
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <div id="contenido" name="contenido" style="height: 1000px">
        <br>
        <br>
        <br>
        <br>
        <br>

        <div>
          <router-view />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
//Se inporta JQuery
const $ = require("jquery");

$('nav a').click(function(e){				
		e.preventDefault();		//evitar el eventos del enlace normal
		var strAncla=$(this).attr('href'); //id del ancla
			$('body,html').stop(true,true).animate({				
				scrollTop: $(strAncla).offset().top
			},1000);
	});

//controla el scroll
$(window).scroll(function() {
  if ($(document).scrollTop() > 50) {
    $(".nav").addClass("affix");
  } else {
    $(".nav").removeClass("affix");
  }
});

//para el caso del menú de dispositivos móviles
$(".navTrigger").click(function() {
  $(this).toggleClass("active");
  //console.log("Clicked menu");
  $("#mainListDiv").toggleClass("show_list");
  $("#mainListDiv").fadeIn();
});

export default {
  name: "App"
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}

#contenido {
  margin-top: 4em;
}

/* Seccion intemedia */
.inner {
  padding: 30px;
}

.cover {
  padding: 0 20px;
  margin-top: 16em;
}

.cover-heading {
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 10px;
  font-size: 7rem;
  color: #fff;
  margin-bottom: 7rem;
  /**Sombras */
  text-shadow: 0px 0px 15px #f2f;
}

.cover-copy {
  font-size: 2rem;
  color: white;

  max-width: 900px;
  margin: 0 auto 2rem;
  /**Sombras */
text-shadow: 4px 3px 2px #000;
}

.mastfoot {
  color: #999;
  /* IE8 proofing */
  color: rgba(255, 255, 255, 0.5);
  margin-top: 3em;
}
.nav-masthead .nav-link {
  display: inline-block;
}

/* Custom default button */
.btn-default {
  color: #fff;
    font-size: 3rem;
  text-shadow: none;
  background-color: transparent;
  border: 2px solid #fff;
  border-radius: 20px;
  padding: 0.5rem 2rem;
}

.btn-default:hover,
.btn-default:focus {
  background-color: rgba(255, 255, 255, 0.3);
}
/** End seccion intermedia */

@import url("assets/fondo.jpg");
html,
body {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Quicksand", sans-serif;
  font-size: 62.5%;
  font-size: 10px;
}

/* Navbar section */

.nav {
  width: 100%;
  height: 70px;
  position: fixed;
  line-height: 65px;
  text-align: center;
  z-index: 1;
}

.nav div.logo {
  float: left;
  width: auto;
  height: auto;
  padding-left: 3rem;
}

.nav div.logo a {
  text-decoration: none;
  color: #fff;
  font-size: 2.5rem;
}

.nav div.logo a:hover {
  color: #e7ae18;
}

.nav div.main_list {
  height: 65px;
  float: right;
}

.nav div.main_list ul {
  width: 100%;
  height: 65px;
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav div.main_list ul li {
  width: auto;
  height: 65px;
  padding: 0;
  padding-right: 3rem;
}

.nav div.main_list ul li a {
  text-decoration: none;
  color: #fff;
  line-height: 65px;
  font-size: 2.4rem;
}

.nav div.main_list ul li a:hover {
  color: #00e676;
}

/* Home section */

.home {
  width: 100%;
  height: 100vh;
  background-image: url("assets/fondo1.jpg");
  background-position: center top;
  background-size: cover;
}

.navTrigger {
  display: none;
}

.nav {
  padding-top: 20px;
  padding-bottom: 20px;
  -webkit-transition: all 0.4s ease;
  transition: all 0.4s ease;
}

/* Media qurey section */

@media screen and (min-width: 768px) and (max-width: 1024px) {
  .container {
    margin: 0;
  }
}

@media screen and (max-width: 768px) {
  .navTrigger {
    display: block;
  }
  .nav div.logo {
    margin-left: 15px;
  }
  .nav div.main_list {
    width: 100%;
    height: 0;
    overflow: hidden;
  }
  .nav div.show_list {
    height: auto;
    display: none;
  }
  .nav div.main_list ul {
    flex-direction: column;
    width: 100%;
    height: 100vh;
    right: 0;
    left: 0;
    bottom: 0;
    background-color: #111;
    /*same background color of navbar*/
    background-position: center top;
  }
  .nav div.main_list ul li {
    width: 100%;
    text-align: right;
  }
  .nav div.main_list ul li a {
    text-align: center;
    width: 100%;
    font-size: 3rem;
    padding: 20px;
  }
  .nav div.media_button {
    display: block;
  }
}

/* Animation */

.navTrigger {
  cursor: pointer;
  width: 30px;
  height: 25px;
  margin: auto;
  position: absolute;
  right: 30px;
  top: 0;
  bottom: 0;
}

.navTrigger i {
  background-color: #fff;
  border-radius: 2px;
  content: "";
  display: block;
  width: 100%;
  height: 4px;
}

.navTrigger i:nth-child(1) {
  -webkit-animation: outT 0.8s backwards;
  animation: outT 0.8s backwards;
  -webkit-animation-direction: reverse;
  animation-direction: reverse;
}

.navTrigger i:nth-child(2) {
  margin: 5px 0;
  -webkit-animation: outM 0.8s backwards;
  animation: outM 0.8s backwards;
  -webkit-animation-direction: reverse;
  animation-direction: reverse;
}

.navTrigger i:nth-child(3) {
  -webkit-animation: outBtm 0.8s backwards;
  animation: outBtm 0.8s backwards;
  -webkit-animation-direction: reverse;
  animation-direction: reverse;
}

.navTrigger.active i:nth-child(1) {
  -webkit-animation: inT 0.8s forwards;
  animation: inT 0.8s forwards;
}

.navTrigger.active i:nth-child(2) {
  -webkit-animation: inM 0.8s forwards;
  animation: inM 0.8s forwards;
}

.navTrigger.active i:nth-child(3) {
  -webkit-animation: inBtm 0.8s forwards;
  animation: inBtm 0.8s forwards;
}

@-webkit-keyframes inM {
  50% {
    -webkit-transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(45deg);
  }
}

@keyframes inM {
  50% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(45deg);
  }
}

@-webkit-keyframes outM {
  50% {
    -webkit-transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(45deg);
  }
}

@keyframes outM {
  50% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(45deg);
  }
}

@-webkit-keyframes inT {
  0% {
    -webkit-transform: translateY(0px) rotate(0deg);
  }
  50% {
    -webkit-transform: translateY(9px) rotate(0deg);
  }
  100% {
    -webkit-transform: translateY(9px) rotate(135deg);
  }
}

@keyframes inT {
  0% {
    transform: translateY(0px) rotate(0deg);
  }
  50% {
    transform: translateY(9px) rotate(0deg);
  }
  100% {
    transform: translateY(9px) rotate(135deg);
  }
}

@-webkit-keyframes outT {
  0% {
    -webkit-transform: translateY(0px) rotate(0deg);
  }
  50% {
    -webkit-transform: translateY(9px) rotate(0deg);
  }
  100% {
    -webkit-transform: translateY(9px) rotate(135deg);
  }
}

@keyframes outT {
  0% {
    transform: translateY(0px) rotate(0deg);
  }
  50% {
    transform: translateY(9px) rotate(0deg);
  }
  100% {
    transform: translateY(9px) rotate(135deg);
  }
}

@-webkit-keyframes inBtm {
  0% {
    -webkit-transform: translateY(0px) rotate(0deg);
  }
  50% {
    -webkit-transform: translateY(-9px) rotate(0deg);
  }
  100% {
    -webkit-transform: translateY(-9px) rotate(135deg);
  }
}

@keyframes inBtm {
  0% {
    transform: translateY(0px) rotate(0deg);
  }
  50% {
    transform: translateY(-9px) rotate(0deg);
  }
  100% {
    transform: translateY(-9px) rotate(135deg);
  }
}

@-webkit-keyframes outBtm {
  0% {
    -webkit-transform: translateY(0px) rotate(0deg);
  }
  50% {
    -webkit-transform: translateY(-9px) rotate(0deg);
  }
  100% {
    -webkit-transform: translateY(-9px) rotate(135deg);
  }
}

@keyframes outBtm {
  0% {
    transform: translateY(0px) rotate(0deg);
  }
  50% {
    transform: translateY(-9px) rotate(0deg);
  }
  100% {
    transform: translateY(-9px) rotate(135deg);
  }
}

.affix {
  padding: 0;
  background-color: #111;
}

.myH2 {
  text-align: center;
  font-size: 4rem;
}
.myP {
  text-align: justify;
  padding-left: 15%;
  padding-right: 15%;
  font-size: 20px;
}
@media all and (max-width: 700px) {
  .myP {
    padding: 2%;
  }
}
</style>