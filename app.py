from flask import Flask, render_template, request, jsonify
from analyzer import analyze_resume_vs_job
import os

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5MB max upload

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        resume_text = request.form.get('resume_text', '').strip()
        job_description = request.form.get('job_description', '').strip()

        if not resume_text or not job_description:
            return jsonify({'error': 'Both resume and job description are required.'}), 400

        result = analyze_resume_vs_job(resume_text, job_description)
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True,use_reloader=True)
