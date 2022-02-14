$("#submit-button").click(() => {
    var from = $("#from").find(":selected").val()
    var to = $("#to").find(":selected").val()
    var from_date = $("#from_date").val()
    var to_date = $("#to_date").val()
    $.ajax({
        type: "POST",
        url: "catalogue_filter",
        data: {
            "from": from,
            "to":  to,
            "from_date": from_date,
            "to_date": to_date
        }
    })
})