import uvicorn
import random
from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse

app = FastAPI()

# List of possible damaged systems
systems = {
    "navigation": "NAV-01",
    "communications": "COM-02",
    "life_support": "LIFE-03",
    "engines": "ENG-04",
    "deflector_shield": "SHLD-05"
}

# Randomly select a damaged system at startup
damaged_system = random.choice(list(systems.keys()))

@app.get("/status")
def get_status():
    """Returns a randomly selected damaged system."""
    return {"damaged_system": damaged_system}

@app.get("/repair-bay", response_class=HTMLResponse)
def get_repair_bay():
    """Returns an HTML page with the repair code in a div with class 'anchor-point'."""
    repair_code = systems[damaged_system]
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Repair</title>
    </head>
    <body>
        <div class="anchor-point">{repair_code}</div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.post("/teapot")
def teapot():
    """Returns HTTP 418 - I'm a teapot."""
    return Response(status_code=418)

# Run the FastAPI server when executed directly
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
