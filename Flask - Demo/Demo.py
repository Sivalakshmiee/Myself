from flask import Flask, render_template

app = Flask( __name__ )

posts = [
    {
        'author': 'Siva',
        'title': 'Blog Post 1',
        'content': 'Lorem ipsum dolor',
        'date_posted': 'jan 20'
    },
    {
        'author':'John Doe',
        'title':'Blog Post 2',
        'content': 'aaabbbaa',
        'date_posted': 'april 16'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = posts)

@app.route('/about')
def about():
    return render_template('about.html', title = "About")

if __name__ == '__main__':
    app.run(debug=True)