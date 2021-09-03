var creddefID;
var creddefMessage;

$(document).ready(() => {
    $(document).on("click", "#btnCreddefCreated", () => {
        $.ajax({
            type: "GET",
            url: "http://localhost:8021/credential-definitions/created",
            dataType: "json"
        })
            .done((response) => {
                creddefID = response["credential_definition_ids"][0];
                console.log("cred def ID: " + creddefID);

                const appendedTag = `
                    <br>
                    <input type="button" id="btnCreddefGet" value="cred_def 받기">
                `;
                $("#credContainer").append(appendedTag);
            })
    });

    $(document).on("click", "#btnCreddefGet", () => {
        $.ajax({
            type: "GET",
            url: `http://localhost:8021/credential-definitions/${creddefID}`
        })
            .done((response) => {
                console.log(JSON.stringify(response));
            })
    })
})