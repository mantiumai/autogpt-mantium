# Auto-GPT Mantium Plugin: Conquering Step One in the AI pipeline

[Mantium](https://mantiumai.com/) is your pathway for accelerating your AI journey by easily connecting internal data to Large Language Models (LLMs), enabling seamless AI integration across industries. 

## 🌟 Key Features

- Fetches user-created applications from Mantium and retrieves relevant info based on user queries.

## 🔧 Installation

Follow these steps to configure the Auto-GPT Mantium Plugin:

### 1. Follow Auto-GPT-Plugins Installation Instructions

Follow the instructions as per the [Auto-GPT-Plugins/README.md](https://github.com/Significant-Gravitas/Auto-GPT-Plugins/blob/master/README.md)

### 2. Locate the `.env.template` file

Find the file named `.env.template` in the main `/Auto-GPT` folder.

### 3. Create and rename a copy of the file

Duplicate the `.env.template` file and rename the copy to `.env` inside the `/Auto-GPT` folder.

### 4. Edit the `.env` file

Open the `.env` file in a text editor. Note: Files starting with a dot might be hidden by your operating system.

In your `.env` search for `ALLOWLISTED_PLUGINS` and add this Plugin:

```ini
################################################################################
### ALLOWLISTED PLUGINS
################################################################################

#ALLOWLISTED_PLUGINS - Sets the listed plugins that are allowed (Example: plugin1,plugin2,plugin3)
ALLOWLISTED_PLUGINS=AutoGPTMantium
```

### 5. Add API configuration settings

Append the following configuration settings to the end of the file:

```ini
################################################################################
### Mantium API
################################################################################

MANTIUM_CLIENT_ID=
MANTIUM_CLIENT_SECRET=
```


You can obtain `MANTIUM_CLIENT_ID` and `MANTIUM_CLIENT_SECRET` by following the steps below.
  - Sign up for an account at [Mantium](https://mantiumai.com/).
  - In the platform, navigate to your User Profile, and copy your `Client ID` and `Secret`.
  
