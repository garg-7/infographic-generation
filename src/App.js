import React from "react";
import Container from "@material-ui/core/Container";
import styled from 'styled-components';
import Infograpgic1 from "./Components/infographics1";

const AppWrapper = styled.div`
  font-family: 'Roboto', sans-serif;
`;

const App = () => {
    let backgroundColor = "#4ade43";
    let textColor = "#baf7b7";
    let value = "15%";
    let text = "of the forest in India are evergreen";
    let countryCode = "in";
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
            </AppWrapper>
        </Container>
    );
};

export default App;
