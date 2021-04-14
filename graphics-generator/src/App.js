import React, {useState} from "react";
import Container from "@material-ui/core/Container";
import styled from 'styled-components';
import TextField from '@material-ui/core/TextField';
import Infograpgic1 from "./Components/infographics1";
import Infograpgic2 from "./Components/infographics2";
import Infograpgic3 from "./Components/infographics3";
import {Button} from "@material-ui/core";
import CircularProgress from '@material-ui/core/CircularProgress';
import axios from "axios";
import countries from "i18n-iso-countries"

countries.registerLocale(require("i18n-iso-countries/langs/en.json"));


// India saw a 63 . 1 % hike in the per capita power consumption over the course of the past 12 months .

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

const elements = {
    "per capita power consumption": "lightning",
    "forest-cover": "tree",
    "gdp": "money",
    "internet": "internet",
    "population": "family"
}



const App = () => {
    const [input, setInput] = useState('');
    const [countryCode, setCountryCode] = useState("")
    const [value, setValue] = useState("")
    const [element, setElement] = useState("")
    const [quantify, setQuantify] = useState(false)
    const [backgroundColor, setBackgroundColor] = useState("")
    const [textColor, setTextColor] = useState("")
    const [text, setText] = useState("")
    const [click, setClick] = useState(false)

    const handleSubmit = evt => {
        evt.preventDefault();
        setClick(true)
        console.log(click)
        console.log(input)
        axios.post("/tokenize", {text: input})
            .then((res) => {
                const data = res.data
                setCountryCode(countries.getAlpha2Code(data.country, "en").toLowerCase())
                setValue(data.value)
                setQuantify(data.quantify)
                const para = data.parameter.toLowerCase()
                setElement(elements[para])
                setBackgroundColor(colors[elements[para]].backgroundColor)
                setTextColor(colors[elements[para]].textColor)
                setText(`${data.quantify ? "Increase": "Decrease"} in ${data.parameter} of ${data.country} in ${data.time} `)
            })
        setClick(false)
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
                {
                    click && (
                        <CircularProgress size={30}/>
                    )
                }
                {
                    text && (
                        <>
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
                                decrease={!quantify}
                            />
                            <Infograpgic3
                                backgroundColor={backgroundColor}
                                textColor={textColor}
                                value={value}
                                text={text}
                                code={countryCode}
                                element={element}
                                decrease={!quantify}
                            />
                        </>
                    )
                }
            </AppWrapper>
        </Container>
    );
};

export default App;
