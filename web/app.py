from flask import Flask, render_template, request, redirect, url_for
from core.device_management import DeviceManager
from core.registration import RegistrationManager
from config.config import config

app = Flask(__name__)
device_manager = DeviceManager()
registration_manager = RegistrationManager(config.SECRET_KEY)


@app.route('/')
def index():
    devices = device_manager.list_devices()
    return render_template('index.html', devices=devices)


@app.route('/register', methods=['POST'])
def register():
    device_id = request.form['device_id']
    device_info = request.form['device_info']
    token = registration_manager.register_device(device_id, device_info)
    return redirect(url_for('index'))


@app.route('/devices')
def devices():
    devices = device_manager.list_devices()
    return render_template('devices.html', devices=devices)


if __name__ == '__main__':
    app.run(debug=True)
