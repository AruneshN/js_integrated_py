import execjs

# =================================== test 2 ======================================== work well
js_code="""
    function message(){
        return "hello";
    }
"""
# Compile the JavaScript code
context=execjs.compile(js_code)

# Execute the JavaScript code and capture the result
result=context.call("message")
print("Result of executing JavaScript:", result)  # Output: Result of executing JavaScript: 7





















# ===================================== DEMO ==============================================
js_code="""
    function add(a,b){
        return a+b;
    }
"""
# create an execjs context
ctx=execjs.compile(js_code)

# call the javascript function
result=ctx.call("add",10,15)
print(result)


# ====================================== TEST ==============================================
js="""
    console.log(6+8);
"""

context=execjs.compile(js)

#result
result=context.eval('6+8')
print(result)

# =================================== test 2 ======================================== work well
js_code = """
function add() {
    return 5 + 50;
}
"""

# Compile the JavaScript code
context = execjs.compile(js_code)

# Execute the JavaScript code and capture the result
result = context.call("add")

print("Result of executing JavaScript:", result)  # Output: Result of executing JavaScript: 7