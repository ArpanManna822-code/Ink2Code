def generate_html(components):

    html = """
<!DOCTYPE html>
<html>

<head>

<title>Generated UI</title>

<script src="https://cdn.tailwindcss.com"></script>

</head>

<body class="bg-gradient-to-br from-slate-900 via-slate-800 to-slate-700 flex items-center justify-center h-screen">

<div class="bg-white/90 backdrop-blur-lg shadow-2xl rounded-xl p-10 w-96">

<h2 class="text-2xl font-bold text-center mb-6 text-gray-800">
Generated UI
</h2>
"""

    components = sorted(components, key=lambda x: x[1])

    for x, y, w, h in components:

        if w > 250:

            html += """
<input 
type="text"
placeholder="Input Field"
class="w-full p-3 mb-4 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500">
"""

        elif w > 170:

            html += """
<button
class="w-full p-3 bg-gradient-to-r from-indigo-600 to-purple-600 text-white rounded-lg hover:opacity-90 transition">
Submit
</button>
"""

    html += """

</div>

</body>
</html>
"""

    return html



def generate_react(components):

    code = """
import React from "react";

function App() {

return (

<div style={{
display:"flex",
justifyContent:"center",
alignItems:"center",
height:"100vh",
background:"#0f172a"
}}>

<div style={{
background:"white",
padding:"40px",
borderRadius:"12px",
width:"320px"
}}>

<h2 style={{textAlign:"center"}}>Login</h2>
"""

    for x,y,w,h in components:

        if w > 250:
            code += '<input placeholder="Input Field" style={{width:"100%",padding:"10px",marginBottom:"10px"}} />\n'

        elif w > 170:
            code += '<button style={{width:"100%",padding:"10px"}}>Button</button>\n'

    code += """

</div>

</div>

);

}

export default App;
"""

    return code



def generate_flutter(components):

    code = """
import 'package:flutter/material.dart';

class GeneratedUI extends StatelessWidget {

@override
Widget build(BuildContext context){

return Scaffold(

backgroundColor: Color(0xFF0f172a),

body: Center(

child: Container(

padding: EdgeInsets.all(30),

width:300,

decoration: BoxDecoration(
color: Colors.white,
borderRadius: BorderRadius.circular(12)
),

child: Column(
mainAxisSize: MainAxisSize.min,
children: [

Text("Login",style:TextStyle(fontSize:22)),

SizedBox(height:20),
"""

    for x,y,w,h in components:

        if w > 250:
            code += """
TextField(
decoration: InputDecoration(
border: OutlineInputBorder(),
hintText: "Input Field"
),
),
SizedBox(height:10),
"""

        elif w > 170:
            code += """
ElevatedButton(
onPressed:(){},
child:Text("Button"),
),
"""

    code += """

]

)

)

)

);

}

}
"""

    return code