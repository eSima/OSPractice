<template>
   <v-container>
        <v-layout column wrap class="nav">
            <ul>                     
               <v-flex v-for="group in groups" :key="group.id">
                    <li>
                        <v-card flat   class="gray--text">
                            {{group.name}}
                            <ul v-if="true">
                                <v-card flat v-for="element in group.elements" :key="element.id">
                                    <li>{{element.name}}</li>
<!--                                    <li>{{isShow(group)}}</li>-->
                                </v-card>
                            </ul>
                        </v-card> 
                    </li>
                </v-flex> 
                
            </ul>
        </v-layout>
    </v-container> 
</template>

<script >
  export default{
        computed:{
            groups(){
                return this.$store.getters.getGroups
            },
            isShow(group){
                return group.$store.getters.getIsShow
            }
           
            
        },
        compmnent:{
            
        },
        methods:{
            show:function(group){
            group.$store.commit('change_show')
            }
        }
  }
</script>

<style scoped>


</style>
