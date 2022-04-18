function getData()
{
    var user_email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    console.log(user_email + "\n" + password);
}
function WriteData()
{
    const fsLibrary  = require('fs')
    let user_name = document.getElementById('email').value;
    let password = document.getElementById('password').value;
    fsLibrary.writeFile('db.txt', user_name, (error) => {
    if (error) 
        throw err;
    })
    fsLibrary.writeFile('db.txt', password, (error) =>
    {
        if(error)
            throw err;
    })
} 
