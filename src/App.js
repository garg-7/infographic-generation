import React from "react";
import Container from "@material-ui/core/Container";
import styled from 'styled-components';
import Infograpgic from "./Components/infographics";

const AppWrapper = styled.div`
  font-family: 'Roboto', sans-serif;
`;

const App = () => {
    let backgroundColor = "#f45454";
    let textColor = "#f4eac7";
    let value = "10%";
    let text = "of the land in Australia is on fire";
    let countryCode = "au";
    let element = "fire";
    return (
        <Container>
            <AppWrapper >
                <Infograpgic
                    backgroundColor={backgroundColor}
                    textColor={textColor}
                    value={value}
                    text={text}
                    code={countryCode}
                    element={element}
                />
            </AppWrapper>
        </Container>
    );
};

export default App;
