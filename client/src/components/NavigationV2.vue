<template>
   <v-container>
        <v-layout wrap class="nav" >
            <v-navigation-drawer floating stateless value="true">
                <v-list subheader dense >  
                    <v-list-group lazy="true" value="true">
                        <v-list-tile slot="activator">
                            <v-list-tile-title>Test1</v-list-tile-title>
                        </v-list-tile>
                        <v-list-group no-action sub-group value="true">
                            <v-list-tile slot="activator">
                                <v-list-tile-title>Class1</v-list-tile-title>
                            </v-list-tile> 
                            <v-list-tile v-for="(el, i) in class1" :key="i" @click="">
                                <v-list-tile-title v-text="el"></v-list-tile-title>
                            </v-list-tile>
                        </v-list-group>
                        <v-list-group sub-group no-action >
                            <v-list-tile slot="activator">
                                <v-list-tile-title>Class2</v-list-tile-title>
                            </v-list-tile>
                            <v-list-tile v-for="(el, i) in class2" :key="i" @click="">
                                <v-list-tile-title v-text="el"></v-list-tile-title>
                            </v-list-tile>
                        </v-list-group>
                    </v-list-group>
                </v-list>
            </v-navigation-drawer>
        </v-layout>
    </v-container> 
</template>

<script >
  export default{
        data: () => ({
    class1: [
      'object1',
      'object2'
      
    ],
    class2: [
      'object1',
      'object2',
      'object3',
      'object4'
    ]
  }),
        computed:{
            groups(){
                return this.$store.getters.getGroups
            },
            isShow(group){
                return group.$store.getters.getIsShow
            }
           
            
        }
       
       
  }
</script>

<style scoped>


</style>

        
