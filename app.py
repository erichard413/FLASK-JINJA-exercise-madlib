from flask import Flask, request, render_template
from stories import *
app = Flask(__name__)

@app.route('/')
def home_page():
    prompts = story.prompts
    return render_template("home.html", prompts=prompts)
@app.route('/story')
def story_page():
    place = request.args["place"]
    noun = request.args["noun"]
    verb = request.args["verb"]
    adjective = request.args["adjective"]
    plural_noun = request.args["plural_noun"]
    generated_story = story.generate({"place": place, "noun": noun, "verb": verb, "adjective": adjective, "plural_noun": plural_noun})
    return render_template("story.html", generated_story=generated_story)