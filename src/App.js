import React from "react";
import Container from "@material-ui/core/Container";
import styled from 'styled-components';
import Infograpgic from "./Components/infographics";

const AppWrapper = styled.div`
  
`;

const App = () => {
    let backgroundColor = "#f45454";
    let textColor = "#f4eac7";
    let value = "36%";
    let text = "of the great lakes lie within Canadian territory";
    let countryCode = "ca";
    return (
        <Container>
            <AppWrapper >
                <Infograpgic
                    backgroundColor={backgroundColor}
                    textColor={textColor}
                    value={value}
                    text={text}
                    code={countryCode}
                />
            </AppWrapper>
        </Container>
    );
};

export default App;
