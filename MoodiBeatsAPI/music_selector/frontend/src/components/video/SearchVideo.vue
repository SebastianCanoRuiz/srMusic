<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Buscar Canción</h2>
            </div>
        </div>

        <div class="row">
            <div class="col">
                <div class="card">
                    <div class="card-body">

                        <form @onSubmit="onSubmit">


                            <div class="form-group row">
                                <label for="title" class="col-sm-2 col-form-la">Título</label>
                                <div class="col-sm-6">
                                    <input type="text" placeholder="Canción" name="title" class="form-control">
                                </div>
                            </div>

                            <div class="rows">
                                <div class="col text-md-center">
                                    <b-button type="submit" variant="primary">Buscar</b-button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
</template>

<script>
export default {
     
}
</script>

<style lang="css" scoped>

</style>