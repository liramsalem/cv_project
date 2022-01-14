console.log('inside fetch example');

function getUsers(){
    console.log('clicked');
    let userID = document.getElementById('userID').value;
    fetch('https://reqres.in/api/users/'+userID).then(
        response => response.json()
    ).then(
        response_obj => put_users_inside_html(response_obj.data)
    ).catch(
        err => console.log(err)
    )
}

function put_users_inside_html(response_obj_data) {
    console.log('response_obj_data');  //הדפסה של גייסון לקונסול
    const curr_main = document.querySelector("main");
    curr_main.innerHTML = ` 
    <div>
        <br>
        <img src="${response_obj_data.avatar}" alt="Profile Picture"/>
        <br>
        <span> <b> ID: </b> ${response_obj_data.id} </span>
        <br>
        <span> <b> Full Name:</b>  ${response_obj_data.first_name} ${response_obj_data.last_name}</span>
        <br>
        <span> <b> Email:</b>  ${response_obj_data.email}    </span>
        <a href="mailto:${response_obj_data.email}">Send Email</a>   
     </div>
     `;
    }

