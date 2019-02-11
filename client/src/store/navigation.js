export default{
    state:{
        loading:true,
        errored:false,
        root_group:'test1', 
        items: [
            {
            name: 'group102',
            children:[{
                name:'object11'
                }]
            },
            {
            name: 'group202',
            children: [
                {
                name: 'group21',
                children: [{
                    name: 'object211',
              
                    }]
                },
                {
                name: 'object22',
           
                },
                {
                name: 'object23',
            
                }
            ]
            },
            {
            name: 'object01',
        
            },
            {
            name: 'object02',
        
            }
            ]
    },
    mutations:{
        set_root_group(state,payload){
            state.root_group=payload
        }
        
    
    },
    actions:{
//        isGroups(){
//           axios
//            .get('')
//            .then(response =>{
//                  this.items=respone.data
//                  })
//            .catch(error =>{
//                  console.log(error);
//                  this.errored =true;
//                  })
//            .finally(() => (this.loading = false));
//        },
        isClass(){
            console.log("isClass action")
        },
        isGroup(){
            console.log("isGroup action")
        },
        isRootGroup(context, payload){
            context.commit('set_root_group', payload);
            console.log("New root group: "+context.state.root_group)
        }
        
        
    },
    getters:{
        getItems: (state) => state.items,
        
        
    }
}