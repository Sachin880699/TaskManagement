
/**
 *  renders the dropdown message and
 *  handles the user selection
 * @param {Array} drop_down_data json array
 */


function renderForm(form_data) {
    let form_inputs = "";
    for (let i = 0; i < form_data.length; i += 1) {
       form_inputs += `<div class="inputs"><input type="${form_data[i].type}" id="${form_data[i].id}"  name="name_${i+1}" placeholder="${form_data[i].value}" required></div>`;
       // console.log(form_inputs)
    }
    const form_obj = `<center><div class="formMsg"><form id="frm1" action="" method="post" onsubmit="return false">${form_inputs}<br><br>
                      <input type="submit" value="Submit" id="bt" onClick="login()"></form></div></center>`;
     
    // console.log(form_obj)
    $(".chats").append(form_obj);
    scrollToBottomOfResults();
     // event.preventDefault();

}
   function login()
    {
        
        var uname = document.getElementById("txtname").value;
        console.log(uname)
        var pwd = document.getElementById("txtpassword").value;
        console.log(pwd)



        
        writeTofile(uname,pwd)
        if(uname =='')
        {
            console.log("please enter user name.")
        }
        else if(pwd=='')
        {
            console.log("please enter the password")
        }
    
        else
        {
          console.log('Thank You for Login')
            }
         
}

     function writeTofile(a,b)

     {
      

    var fso = new ActiveXObject("Microsoft.XMLDOM");
    var fh = fso.OpenTextFile("data.txt", 8, false, 0);
    fh.WriteLine(d1 + ',' + d2);
    fh.Close();
      

     }
 
