import React, { useState } from 'react';

// import { TextField, MaskedTextField } from '@fluentui/react/lib/TextField';
// import { Stack, IStackProps, IStackStyles } from '@fluentui/react/lib/Stack';

// const stackTokens = { childrenGap: 50 };
// const iconProps = { iconName: 'Calendar' };
// const stackStyles = { root: { width: 650 } };
// const columnProps = {
//   tokens: { childrenGap: 15 },
//   styles: { root: { width: 300 } },
// };

const Login = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const handleSubmit = (e) => {

    }

    const handleUsernameChange = (e) => {
        setUsername(e.target.value)
    }

    const handlePasswordChange = (e) => {
        setPassword(e.target.value)
        console.log(password)
    }

    return (
        <div>
            <h1>Enter Agora Portal login details</h1>
            {/* <Stack {...columnProps}>
                <TextField label="Standard" />
            </Stack> */}
            <form onSubmit={handleSubmit}>
                <label>
                    Username:
                    <input type="text" name="name" onChange={handleUsernameChange}/>
                </label>
                <br></br>
                <br></br>
                <label>
                    Password:
                    <input type="text" name="name" onChange={handlePasswordChange}/>
                </label>
            <input type="submit" value="Login" />
            </form>
        </div>
    )
}

export default Login;