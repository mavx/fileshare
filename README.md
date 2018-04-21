# fileshare
Simple endpoint to accept file uploads and returns a URL for sharing.

## Requirements
* Python3.5+
* pipenv

## Running the app
```
git clone https://github.com/mavx/fileshare
cd fileshare
pipenv install --python python3 # Select python version
pipenv run python main.py
# pipenv run gunicorn -b :PORT_NUMBER main:app # Alternatively if hosting on server
```

## Usage
Just visit the `HOSTNAME:PORT/upload` using your browser for the GUI. Otherwise, see below:

Uploading a file via CLI
```
$ curl -F "file=@filename.txt" localhost:5000/upload
{
  "key": "figQPi",
  "success": true,
  "url": "localhost:5000/uploads/figQPi"
}
```

Accessing the file via CLI
```
$ curl -L localhost:5000/uploads/figQPi
```
