axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

let app = new Vue({
    el: '#app1',
    delimiters: ["[[","]]"],
    data: {
        message: 'Hello!',
        searchCriteria: "",
        searchResults: [],
    },
    methods: {
       search: function (){
        axios.get(`http://127.0.0.1:8000/apis/v1/search/custom/?search=${this.searchCriteria}`)
        .then((response) => {
            console.log(response.data)
            for (let i = 0; i < response.data.length; ++i) {
                this.searchResults.push(response.data[i])
            }
            console.log(this.searchResults)
        })
    },
    bulletin: function(id){
        window.location.href=`http://127.0.0.1:8000/bulletin/${id}`
    },  
},

})