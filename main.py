from flask import Flask, render_template

jobs = [{
  "id": 1,
  "job name": "Data Scientist",
  "location": "Zagreb Croatia",
  "salary": 5000
}, {
  "id": 2,
  "job name": "Front End Developer",
  "location": "Zagreb Croatia",
  "salary": 2000
}, {
  "id": 3,
  "job name": "Backend Developer",
  "location": "Split Croatia",
  "salary": 15000
}, {
  "id": 4,
  "job name": "ML Scientist",
  "location": "Zagreb Croatia",
  "salary": 5000
}]
app = Flask(__name__)


@app.route("/")
def helloWorld():
  return render_template("home.html", jobs=jobs)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
