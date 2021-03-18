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
    let backgroundColor = "#07ed42";  // #e31b47
    let textColor = "#92f0aa";  // #e0abb6
    let value = "15%";
    let text = "Decrease in forest cover of Australia in 12 years";
    let countryCode = "au";
    let element = "tree";
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
