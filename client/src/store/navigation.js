export default{
    state:{
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
    mutation:{
        
        
    
    },
    actions:{
        
    },
    getters:{
        getItems: (state) => state.items,
        
    }
}