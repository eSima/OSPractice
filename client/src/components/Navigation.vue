<template>
   <v-container>
        <v-layout wrap class="nav" >
           <v-treeview  :items="items" item-key="name" open-on-click>
            </v-treeview>
        </v-layout>
    </v-container> 
</template>

<script >
  export default{
        data: () => ({
    
  }),
        computed:{
            items(){
                return this.$store.getters.getItems
            },          
            
        }
       
       
  }
</script>

<style scoped>


</style>

        
