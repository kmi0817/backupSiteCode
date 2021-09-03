var num = 1;

$(window).scroll(() => {
    if ($(window).scrollTop() >= $(document).height() - $(window).height()) {
        $.ajax({
            type: 'GET',
            url: '../static/repo_list.json',
            datatype: 'json'
        })
            .done(function (data) {
                for (var i = 0; i < 10; i++) {
                    let index = `repo_${num}`;
                    const appendHTML = appendHTMLTemplate(index, data[index].name, data[index].create_time, data[index].language);
                    $('#containers').append(appendHTML);
                    num = num + 1;
                }
            })
    }
});

$(document).ready(() => {
    $.ajax({
        type: "GET",
        url: "../static/repo_list.json",
        dataType: "json"
    })
        .done((data) => {
            for (var i = 0; i < 10; i++) {
                let index = `repo_${num}`;
                const appendHTML = appendHTMLTemplate(index, data[index].name, data[index].create_time, data[index].language);
                $('#containers').append(appendHTML);
                num = num + 1;
            }
        })
});

function appendHTMLTemplate(index, name, created, lang) {
    return `
        <div class="repoContainer">
            <table>
                <tr>
                    <td class="repoName"><a>${index}: ${name}</a></td>
                </tr>
                <tr>
                    <td class="repoCreated">${created}</td>
                </tr>
                <tr>
                    <td class="repoLang">${lang}</td>
                </tr>
            </table>
        </div>
    `;
}