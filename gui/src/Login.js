import React, { useState } from 'react';

const Login = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const handleSubmit = () => {
        
    }

    const handleUsernameChange = (e) => {
        setUsername(e.target.value)
    }

    const handlePasswordChange = (e) => {
        setPassword(e.target.value)
    }

    return (
        <div>
            <h1>Enter Agora Portal login details</h1>
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
            <input type="submit" value="Login"/>
            </form>
        </div>
    )
}

export default Login;