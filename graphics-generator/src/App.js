import React, {useState} from "react";
import Container from "@material-ui/core/Container";
import styled from 'styled-components';
import TextField from '@material-ui/core/TextField';
import Infograpgic1 from "./Components/infographics1";
import Infograpgic2 from "./Components/infographics2";
import Infograpgic3 from "./Components/infographics3";
import {Button} from "@material-ui/core";
import axios from "axios";

const AppWrapper = styled.div`
  font-family: 'Roboto', sans-serif;
  .textfield{
        margin-top: 100px;
        width: 100%;
        display: flex;
        #outlined-basic{
          width: 700px;
        }
    }
`;

const colors = {
    "lightning" : { backgroundColor : "#fcba03", textColor : "#fce49f"},
    "tree" : { backgroundColor : "#2d960e", textColor : "#afeb9d"},
    "money" : { backgroundColor : "#85bf4b", textColor : "#d2edb7"},
    "internet" : { backgroundColor : "#4287f5", textColor : "#b0ceff"},
    "family" : { backgroundColor : "#38d9f2", textColor : "#afe5ed"},
}



const App = () => {
    let backgroundColor = "#4287f5";  // #e31b47
    let textColor = "#b0ceff";  // #e0abb6
    let value = "15%";
    let text = "Decrease in forest cover of Australia in 12 years";
    let countryCode = "au";
    let element = "internet";

    const [input, setInput] = useState('');
    const [tokens, setTokens] = useState({})
    const handleSubmit = evt => {
        evt.preventDefault();
        console.log(input)
        axios.post("/tokenize", {text: input})
            .then((res) => {
                setTokens(res.data);
            })
    }

    return (
        <Container>
            <AppWrapper >
                <form className="textfield" noValidate autoComplete="off" onSubmit={handleSubmit}>
                    <TextField
                        id="outlined-basic"
                        label="text"
                        variant="outlined"
                        value={input}
                        onInput={ e=>setInput(e.target.value)}
                    />
                    <Button
                        type="submit"
                        variant="contained"
                        color="primary"
                    >
                        Submit
                    </Button>
                </form>
                <Infograpgic1
                    backgroundColor={backgroundColor}
                    textColor={textColor}
                    value={value}
                    text={text}
                    code={countryCode}
                    element={element}
                />
                <Infograpgic2
                    backgroundColor={backgroundColor}
                    textColor={textColor}
                    value={value}
                    text={text}
                    code={countryCode}
                    element={element}
                    decrease={true}
                />
                <Infograpgic3
                    backgroundColor={backgroundColor}
                    textColor={textColor}
                    value={value}
                    text={text}
                    code={countryCode}
                    element={element}
                    decrease={true}
                />
            </AppWrapper>
        </Container>
    );
};

export default App;
