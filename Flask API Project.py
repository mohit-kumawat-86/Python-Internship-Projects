from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome</h1>
    <p>Go to <a href="/resume">/resume</a> to see my resume.</p>
    """

@app.route("/resume")
def resume():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Resume</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }
            .container {
                width: 80%;
                max-width: 900px;
                margin: 20px auto;
                background: #fff;
                padding: 20px 30px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
                border-radius: 8px;
            }
            h1, h2, h3 {
                margin-bottom: 5px;
            }
            .name {
                text-align: center;
                border-bottom: 2px solid #ddd;
                padding-bottom: 10px;
            }
            .section {
                margin-top: 20px;
            }
            .section-title {
                font-size: 20px;
                font-weight: bold;
                border-bottom: 1px solid #ddd;
                margin-bottom: 10px;
                padding-bottom: 5px;
            }
            .item {
                margin-bottom: 10px;
            }
            .item-title {
                font-weight: bold;
            }
            .item-subtitle {
                font-style: italic;
                font-size: 14px;
            }
            .skills span {
                display: inline-block;
                margin: 4px 6px 4px 0;
                padding: 4px 8px;
                border-radius: 4px;
                border: 1px solid #ccc;
                font-size: 14px;
            }
            .contact {
                font-size: 14px;
                text-align: center;
                margin-top: 5px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <!-- Name / Header -->
            <div class="name">
                <h1>Mohit Kumawat</h1>
                <div class="contact">
                    <span>Email: mohitkumawar10gmail.com</span> |
                    <span>Phone: +91-8619016802</span> |
                    <span>City: Jaipur, Rajsthan, India</span>
                </div>
            </div>

            <!-- Career Objective -->
            <div class="section">
                <div class="section-title">Career Objective</div>
                <p>
                    To obtain an internship/entry-level position where I can apply my skills in Python, web development,
                    and problem solving, while continuously learning new technologies.
                </p>
            </div>

            <!-- Education -->
            <div class="section">
                <div class="section-title">Education</div>
                <div class="item">
                    <div class="item-title">B.Tech in Computer Science & Engineering</div>
                    <div class="item-subtitle"> Vivekananda Global University | 2024 - 2028</div>
                    <div>CGPA / Percentage: 8.0+</div>
                </div>
                <div class="item">
                    <div class="item-title">Class 12th</div>
                    <div class="item-subtitle">SRK Jobner | 2023</div>
                </div>
            </div>

            <!-- Skills -->
            <div class="section">
                <div class="section-title">Skills</div>
                <div class="skills">
                    <span>Python (if, else, loops)</span>
                    <span>Flask (Basics)</span>
                    <span>HTML</span>
                    <span>CSS (Basic)</span>
                    <span>Problem Solving</span>
                    <span>Git (Basic)</span>
                </div>
            </div>

            <!-- Projects -->
            <div class="section">
                <div class="section-title">Projects</div>

                <div class="item">
                    <div class="item-title">1. Simple ATM Simulator (Python)</div>
                    <div class="item-subtitle">Python | if-else, loops</div>
                    <ul>
                        <li>Implemented basic ATM features like balance check, cash withdrawal, and PIN verification.</li>
                        <li>Used loops and conditional statements for user input and validation.</li>
                    </ul>
                </div>

                <div class="item">
                    <div class="item-title">2. Mini Console-Based Student Management</div>
                    <div class="item-subtitle">Python | list, dictionary</div>
                    <ul>
                        <li>Stored student records (name, roll number, marks) using dictionaries.</li>
                        <li>Implemented features to add, search, and delete student data.</li>
                    </ul>
                </div>
            </div>

            <!-- Achievements -->
            <div class="section">
                <div class="section-title">Achievements / Activities</div>
                <ul>
                    <li>Participated in coding contests and online challenges.</li>
                    <li>Actively learning Python and web development.</li>
                </ul>
            </div>

            <!-- Personal Details -->
            <div class="section">
                <div class="section-title">Personal Details</div>
                <ul>
                    <li>Date of Birth: 19/09/2006</li>
                    <li>Languages: Hindi, English</li>
                    <li>Hobbies: Coding, YouTube, Anime, Learning new tech</li>
                </ul>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run()