# Comics publisher

<a href='README.md'>RU</a>

Automated upload to public VK of a randomly downloaded comic.
The script publishes random comics to VK by downloading them from this [site](https://xkcd.com/).

### How to install

1. Python3 should already be installed.

2. Clone this repository and change to the project directory

```
    git clone https://github.com/wezbicka/Comics-publisher.git
```
    
3. Create and activate the virtual environment

```Bash
    python -m venv venv
    source ./venv/Scripts/activate #for Windows
    source ./venv/bin/activate #for Linux and macOS
```

4. Install required dependencies
```
    pip install -r requirements.txt
```

5. Create an application in VK ([link](https://vk.com/apps?act=manage)) and get its ID. Then get [access_token](https://vk.com/dev/implicit_flow_user) with the following permissions: `photos, groups, wall, offline`. Also create your community in VK and [find out its ID](https://regvk.com/id/).

6. Create a file called .env and add everything you got above. Here is an example:

```
    CLIENT_ID=0000000
    GROUP_ID=0000001
    VK_TOKEN=vk1.a.vk_access_token
```

7. Run the script

```
    python main.py
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
