<template>
   <v-container>
        <v-layout wrap class="nav" >
           <v-treeview  :active.sync="active" :items="items" item-key="id" open-on-click activatable transition
            active-class="primary--text" >
            </v-treeview>
        </v-layout>
    </v-container> 
</template>

<script >
  export default{
        data: () => ({
           active:[],
           
  }),
        computed:{
            items(){
                return this.$store.getters.getItems
            },
            
        },
        watch: {
            active: function(){
                if (this.active.length) this.$store.dispatch('showOnMap',this.active[0]) 
            }
        },
        methods:{
 
        }
       
       
  }
</script>

<style scoped>


</style>

        
