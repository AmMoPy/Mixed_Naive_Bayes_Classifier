from IPython.core.display import display, HTML
button = '''
<form action="javascript:code_toggle()"><input type="submit" id="toggleButton" value="Show Code"></form>
'''

toggle = '''
    <script>
    function code_toggle() {
        if ($('div.cell.code_cell.rendered.selected div.input').css('display')!='none'){
            $('div.cell.code_cell.rendered.selected div.input').hide();
        } else {
            $('div.cell.code_cell.rendered.selected div.input').show();
        }
    }
    </script>
'''

display(HTML(toggle + button))

def hide_code():
    display(HTML(button))