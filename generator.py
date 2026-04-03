def generate_html(components):

    html = """
<div style="position:relative;width:900px;height:700px;border:1px solid #ccc;transform:scale(0.8);transform-origin:top left;">
"""

    for x,y,w,h in components:

        if w > 250:

            html += f"""
<input type="text" placeholder="Input Field"
style="
position:absolute;
left:{x}px;
top:{y}px;
width:{w}px;
height:{h}px;
"/>
"""

        elif w > 170:

            html += f"""
<button
style="
position:absolute;
left:{x}px;
top:{y}px;
width:{w}px;
height:{h}px;
">
Button
</button>
"""

        else:

            html += f"""
<div
style="
position:absolute;
left:{x}px;
top:{y}px;
width:{w}px;
height:{h}px;
border:1px solid black;
">
</div>
"""

    html += "</div>"

    return html


def generate_react(components):

    react="function App(){\nreturn(\n<div>\n"

    for x,y,w,h in components:

        if w>250:
            react+="<input placeholder='Input Field'/>\n"

        elif w>120:
            react+="<button>Button</button>\n"

        else:
            react+="<div>Container</div>\n"

    react+="</div>\n)\n}"

    return react


def generate_flutter(components):

    flutter="Column(\nchildren:[\n"

    for x,y,w,h in components:

        if w>250:
            flutter+="TextField(),\n"

        elif w>120:
            flutter+="ElevatedButton(onPressed:(){},child:Text('Button')),\n"

        else:
            flutter+="Container(height:50,width:100),\n"

    flutter+="]\n)"

    return flutter