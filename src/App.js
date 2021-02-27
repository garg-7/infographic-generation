import React from "react";
import Container from "@material-ui/core/Container";
import styled from 'styled-components';
import Infograpgic1 from "./Components/infographics1";
import Infograpgic2 from "./Components/infographics2";
import Infograpgic3 from "./Components/infographics3";

const AppWrapper = styled.div`
  font-family: 'Roboto', sans-serif;
`;

const App = () => {
    let backgroundColor = "#e31b47";
    let textColor = "#e0abb6";
    let value = "15%";
    let text = "of the forest in India are evergreen";
    let countryCode = "au";
    let element = "fire";
    return (
        <Container>
            <AppWrapper >
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
