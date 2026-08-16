from flask import Flask, render_template, request, jsonify, send_file
import zipfile
import os
import io

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 200 * 1024 * 1024  # 200MB

# Try importing rarfile
try:
    import rarfile
    RAR_SUPPORTED = True
except ImportError:
    RAR_SUPPORTED = False


@app.route('/')
def index():
    return render_template('index.html', rar_supported=RAR_SUPPORTED)


@app.route('/compress', methods=['POST'])
def compress_single_file():
    try:
        uploaded = request.files.get('file_a') or request.files.get('file')
        if not uploaded or not uploaded.filename:
            return jsonify({'error': 'Please upload one file to compress'}), 400

        target_size_raw = request.form.get('target_size', '').strip()
        if not target_size_raw:
            target_size_raw = request.form.get('target_kb', '100000').strip()

        try:
            target_bytes = max(1, int(target_size_raw))
        except ValueError:
            target_bytes = 100000

        file_bytes = uploaded.read()
        source_name = uploaded.filename
        base_name = os.path.splitext(source_name)[0] or 'compressed'

        out_buffer = io.BytesIO()
        with zipfile.ZipFile(out_buffer, mode='w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
            zf.writestr(source_name, file_bytes)

        out_buffer.seek(0)
        response = send_file(
            out_buffer,
            mimetype='application/zip',
            as_attachment=True,
            download_name=f"{base_name}.zip"
        )

        response.headers['X-Compressed-Bytes'] = str(len(out_buffer.getvalue()))
        response.headers['X-Target-Bytes'] = str(target_bytes)
        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True,port=5002)