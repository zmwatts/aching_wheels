axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

let app = new Vue({
    el: '#app',
    delimiters: ["[[","]]"],
    data: {
        mapdiv: "",
        message: 'Hello!',
        id: 0,
        person: {},
        newCommentText: "",
        newCommentusername: "",
        comments: [],
    },
    mounted: function (){
           let url = window.location.pathname;
           this.id = url.substring(url.lastIndexOf('/') + 1);
            axios.get(`http://127.0.0.1:8000/apis/v1/${this.id}/`)
        .then((response) => {
            console.log(response.data)
            app.person = response.data
            console.log("anystring")
        })
        .then(()=>{
            this.mapdiv =  `<iframe
            width="550em"
            height="600em"
            frameborder="0" style="border:0"
            src="https://www.google.com/maps/embed/v1/view?key=${token}&center=${this.person.last_seen_latitude},${this.person.last_seen_longitude}&zoom=18&maptype=satellite" 
            allowfullscreen>
            </iframe>`
            // <iframe 
            // src="https://www.google.com/maps/d/embed?mid=12C7RhA4kv2E2ogjukUtLctLIwGRcxDHy" 
            //width="550em" height="600em"></iframe>
        });
    },
});

let comment = new Vue({
    el: '#comments',
    delimiters: ["[[","]]"],
    data: {
        comments: [],
        newCommentText: "",
        newCommentusername: "",
        id: 0,
        edittedcontent: "",
    },
    mounted: function(){
        let url = window.location.pathname;
        this.id = url.substring(url.lastIndexOf('/') + 1);
        axios.get(`http://127.0.0.1:8000/apis/v1/${this.id}/`).then((response)=>
        {
            this.comments = response.data.comments
        })
        },
    methods: {
    addNewComment: function (user) {
        axios.post(`http://127.0.0.1:8000/apis/v1/comment/`,
        {
            "username": user,
            "content": this.newCommentText,
            "missing_person": this.id,
        }
        ).then(axios.get(`http://127.0.0.1:8000/apis/v1/${this.id}/`).then((response)=>
        {
        this.comments = response.data.comments
        this.newCommentText = ""})
        
        )},
    
    
    deleteComment: function (index, id) {
        axios.delete(`http://127.0.0.1:8000/apis/v1/comment/${id}/`)
        this.comments.splice(index, 1)
    },  
    editComment: function (index, id) {
        mycontainer = document.getElementById("editcontainer"+index)
        mycontainer.style.display = "flex"

    },
    formcontainer: function (index){
        return "editcontainer" + index
    },
    submitedit: function(index, id){
        axios.put(`http://127.0.0.1:8000/apis/v1/comment/${id}/`, 
        {"content":comment.comments[index].content}
        ).finally(()=>{
        mycontainer = document.getElementById("editcontainer"+index)
        mycontainer.style.display = "none"
        })
    }
    },
})