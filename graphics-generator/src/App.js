import React, {useState} from "react";
import Container from "@material-ui/core/Container";
import styled from 'styled-components';
import TextField from '@material-ui/core/TextField';
import Infograpgic1 from "./Components/infographics1";
import Infograpgic2 from "./Components/infographics2";
import Infograpgic3 from "./Components/infographics3";
import SportsIngograhics1 from "./Components/sports-ingograhics1";
import {Button} from "@material-ui/core";
import axios from "axios";
import countries from "i18n-iso-countries"
import slugify from "./Components/slugify";

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

const elements = {
    "per-capita-power-consumption": {name : "lightning", backgroundColor : "#fcba03", textColor : "#fce49f"},
    "forest-cover": {name : "tree", backgroundColor : "#2d960e", textColor : "#afeb9d"},
    "gdp": {name : "money", backgroundColor : "#85bf4b", textColor : "#d2edb7"},
    "internet": {name : "internet", backgroundColor : "#4287f5", textColor : "#b0ceff"},
    "population": {name : "family", backgroundColor : "#38d9f2", textColor : "#afe5ed"},
}



const App = () => {
    const [input, setInput] = useState('');
    const [click, setClick] = useState(false)
    const [infoData, setInfoData] = useState({})

    const handleSubmit = evt => {
        evt.preventDefault();
        setClick(true)
        console.log(click)
        console.log(input)
        axios.post("/tokenize", {text: input})
            .then((res) => {
                setInfoData(res.data)
            })
        setClick(false)
    }



    let geographicData = {}

    if(infoData.country){
        Object.assign(geographicData, {countryCode: countries.getAlpha2Code(infoData.country, "en").toLowerCase()});
        Object.assign(geographicData, {value: infoData.value});
        Object.assign(geographicData, {quantify: infoData.quantify});
        const parameter = elements[infoData.parameter];
        Object.assign(geographicData, {element: parameter.name});
        Object.assign(geographicData, {backgroundColor: parameter.backgroundColor});
        Object.assign(geographicData, {textColor: parameter.textColor});
        const text = `${infoData.quantify ? "Increase": "Decrease"} in ${infoData.parameter} of ${infoData.country} in ${infoData.time} `
        Object.assign(geographicData, {text: text});
    }

    let sportsData = {}

    if(true){
        Object.assign(sportsData, {sport : "Hockey"})
        Object.assign(sportsData, {winning_team : "India"})
        Object.assign(sportsData, {losing_team : "France"})
        Object.assign(sportsData, {match : "Practice Match"})
        Object.assign(sportsData, {score : "5 runs"})
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
                    geographicData.text && (
                        <>
                            <Infograpgic1
                                backgroundColor={geographicData.backgroundColor}
                                textColor={geographicData.textColor}
                                value={geographicData.value}
                                text={geographicData.text}
                                code={geographicData.countryCode}
                                element={geographicData.element}
                            />
                            <Infograpgic2
                                backgroundColor={geographicData.backgroundColor}
                                textColor={geographicData.textColor}
                                value={geographicData.value}
                                text={geographicData.text}
                                code={geographicData.countryCode}
                                element={geographicData.element}
                                decrease={!geographicData.quantify}
                            />
                            <Infograpgic3
                                backgroundColor={geographicData.backgroundColor}
                                textColor={geographicData.textColor}
                                value={geographicData.value}
                                text={geographicData.text}
                                code={geographicData.countryCode}
                                element={geographicData.element}
                                decrease={!geographicData.quantify}
                            />
                        </>
                    )
                }
                {
                    sportsData.sport && (
                        <SportsIngograhics1
                            sport={sportsData.sport}
                            winning_team={sportsData.winning_team}
                            losing_team={sportsData.losing_team}
                            match={sportsData.match}
                            score={sportsData.score}
                        />
                    )
                }
            </AppWrapper>
        </Container>
    );
};

export default App;
