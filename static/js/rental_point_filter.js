function set_models_by_manufacture() {
    manufacture = $('#manufactures').find(":selected").text()
    $.ajax({
        url: 'get_manufacture_models',
        type: "POST",
        data: {manufacture: manufacture},
        success: (response) => {
            $('#models').html('')
            if(response.length > 0) {
                response.forEach(element => {
                    var option = document.createElement('option')
                    option.value = response
                    option.innerHTML = `${response}`
                    $('#models').append(option)
                    option.disabled = true
                })
            }
            else {
                var option = document.createElement('option')
                option.value = ""
                option.innerHTML = `Nav modeļu`
                $('#models').append(option)
            }
        }
    })
}

$("#PrecesPoga").click(() => {
    console.log($("#no").val())
    $.ajax({
        url: "filter_cars",
        type: "POST",
        data: {
            rental_point: $("#rental_points").find(":selected").val(),
            manufacture: $("#manufactures").find(":selected").val(),
            model: $("#models").find(":selected").val(),
            from_date: $("#from_date").val(),
            to_date: $("#to_date").val(),
            from_time: $("#no").val(),
            to_time: $("#lidz").val()
        },
        success: (response) =>{
            $(".list-container").html("")
            if(response.length > 0) {
                response.forEach((element) => {
                    var car = `
                        <div class="list-element">
                            <a href="/admin/rental_point/{{ rental_point.id }}"><h2>Nomas punkts: ${ element.rental_point }</h2></a>
                            <h3>Marka: ${ element.manufacture }</h3>
                            <h3>Modelis:  ${ element.model }</h3>
                            <h3>Klase:  ${ element.classifications }</h3>
                            <h3>Gads:  ${ element.year }</h3>
                            <h3>Valsts numurs: ${ element.number_plate }</h3>
                            <h3>Pieejams no: ${ element.from_date }</h3>
                            <h3>Pieejams līdz: ${ element.to_date }</h3>
                            <h2>Stundas likme: ${ element.hourly_rate }euro</h2>
                            <a><button>Rezervēt</button></a>
                        </div>
                    `
                    $(".list-container").append(car)
                })
            } else {
                $(".list-container").html("<h2>Nav rezultātu</h2>")
            }
        }
    })
})

// function set_cars() {
//     $.ajax({
//         url: `cars`,
//         success: (response) => {
//             var option = document.createElement('option')
//             option.value = -1
//             option.innerHTML = `Izvēlieties automašīnu`
//             document.getElementById('cars').appendChild(option)
//             response.forEach(element => {
//                 var option = document.createElement('option')
//                 option.value = element.rental_point_id
//                 option.innerHTML = `${element.manufacture} - ${element.model}`
//                 document.getElementById('cars').appendChild(option)
//             })
//         },
//     });
// }

// function set_rental_points() {
//     $.ajax({
//         url: `rental_points`,
//         success: (response) => {
//             var option = document.createElement('option')
//             option.value = -1
//             option.innerHTML = `Izvēlieties nomas punktu`
//             document.getElementById('rental_point').appendChild(option)
//             response.forEach(element => {
//                 var option = document.createElement('option')
//                 option.value = element.id
//                 option.innerHTML = `${element.title}`
//                 document.getElementById('rental_point').appendChild(option)
//             })
//         },
//     });
// }

// function filter_cars() {
//     document.getElementById('cars').innerHTML = ""
//     let id = document.getElementById('rental_point').value
//     if (id === "-1") {
//         set_cars()
//     } 
//     else {
//         $.ajax({
//             url: `rental_point_cars/${id}`,
//             success: (response) => {
//                 response.forEach(element => {
//                     var option = document.createElement('option')
//                     option.value = element.rental_point_id
//                     option.innerHTML = `${element.manufacture} - ${element.model}`
//                     document.getElementById('cars').appendChild(option)
//                 });
//             },
//         });
//     }
// }


// function filter_rental_points() {
//     document.getElementById('rental_point').innerHTML = ""
//     let id = document.getElementById('cars').value
//     if (id === "-1") {
//         set_rental_points()
//     } else {
//         $.ajax({
//             url: `rental_point/${id}`,
//             success: (response) => {
//                 var option = document.createElement('option')
//                 option.value = response.id
//                 option.innerHTML = `${response.title}`
//                 document.getElementById('rental_point').appendChild(option)
//                 option.disabled = true
//             }
//         });
//     }
// }


