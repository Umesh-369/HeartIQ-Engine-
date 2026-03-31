document.addEventListener('DOMContentLoaded', () => {
    
    // 1. 3D Tilt Effect Setup
    const tiltElement = document.getElementById('tilt-element');
    
    document.addEventListener('mousemove', (e) => {
        const xAxis = (window.innerWidth / 2 - e.pageX) / 40;
        const yAxis = (window.innerHeight / 2 - e.pageY) / 40;
        tiltElement.style.transform = `rotateY(${xAxis}deg) rotateX(${yAxis}deg)`;
    });
    
    document.addEventListener('mouseleave', () => {
        tiltElement.style.transform = `rotateY(0deg) rotateX(0deg)`;
        tiltElement.style.transition = 'transform 0.5s ease';
    });
    
    document.addEventListener('mouseenter', () => {
        tiltElement.style.transition = 'transform 0.1s ease';
    });

    // 2. Form Submission connected to Flask API
    const form = document.getElementById('prediction-form');
    const submitBtn = document.getElementById('submit-btn');
    const spinner = document.getElementById('loading-spinner');
    const resultOverlay = document.getElementById('result-overlay');
    const closeResultBtn = document.getElementById('close-result');
    
    const resultIcon = document.getElementById('result-icon');
    const resultTitle = document.getElementById('result-title');
    const resultMessage = document.getElementById('result-message');
    const scoreFill = document.getElementById('score-fill');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        // Convert to loading state
        submitBtn.style.display = 'none';
        spinner.style.display = 'flex';
        
        // Assemble payload mapping exactly to the Flask API
        const payload = {
            age: document.getElementById('age').value,
            sex: document.getElementById('sex').value,
            cp: document.getElementById('cp').value,
            trestbps: document.getElementById('trestbps').value,
            chol: document.getElementById('chol').value,
            fbs: document.getElementById('fbs').value,
            restecg: document.getElementById('restecg').value,
            thalach: document.getElementById('thalach').value,
            exang: document.getElementById('exang').value,
            oldpeak: document.getElementById('oldpeak').value,
            slope: document.getElementById('slope').value,
            ca: document.getElementById('ca').value,
            thal: document.getElementById('thal').value
        };

        try {
            // POST request to local Flask server
            const response = await fetch('http://127.0.0.1:5000/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(payload)
            });

            if (!response.ok) {
                throw new Error("Server Error - Ensure the Python Flask server is running");
            }

            const data = await response.json();
            
            // Revert loading state
            spinner.style.display = 'none';
            submitBtn.style.display = 'block';
            
            // Show result passing the model's authentic prediction and confidence
            showResult(data.prediction === 1, data.confidence);

        } catch (error) {
            console.error(error);
            spinner.style.display = 'none';
            submitBtn.style.display = 'block';
            alert("Connection Error: " + error.message + "\n\nMake sure your Flask python server is running!");
        }
    });

    function showResult(hasDisease, confidence) {
        resultOverlay.classList.remove('hidden');
        
        setTimeout(() => {
            resultOverlay.classList.add('active');
            
            const confFormatted = confidence.toFixed(1);

            if(hasDisease) {
                resultIcon.innerHTML = '<i class="fa-solid fa-heart-crack"></i>';
                resultIcon.className = 'result-icon icon-presence pulse';
                resultTitle.innerText = "High Risk Detected";
                resultTitle.style.color = "var(--accent)";
                resultMessage.innerText = `Machine Learning Model predicts the PRESENCE of heart disease. (Confidence: ${confFormatted}%)`;
                
                scoreFill.style.background = 'linear-gradient(to right, #f43f5e, #be123c)';
                scoreFill.style.width = `${confFormatted}%`;
            } else {
                resultIcon.innerHTML = '<i class="fa-solid fa-heart"></i>';
                resultIcon.className = 'result-icon icon-absence pulse';
                resultTitle.innerText = "Low Risk / Normal";
                resultTitle.style.color = "#10b981";
                resultMessage.innerText = `Machine Learning Model predicts the ABSENCE of heart disease. (Confidence: ${confFormatted}%)`;
                
                scoreFill.style.background = 'linear-gradient(to right, #10b981, #059669)';
                scoreFill.style.width = `${confFormatted}%`;
            }
        }, 50);
    }

    closeResultBtn.addEventListener('click', () => {
        resultOverlay.classList.remove('active');
        setTimeout(() => {
            resultOverlay.classList.add('hidden');
            scoreFill.style.width = '0%';
        }, 400);
    });

});
