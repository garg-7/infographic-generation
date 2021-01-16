import React from "react";
import Container from "@material-ui/core/Container";
import styled from 'styled-components';

const AppWrapper = styled.div`
  .layout{
    background-color: ${props=> props.backgroundColor};
    color: ${props=> props.textColor};
  }
`;

const App = () => {
    let backgroundColor = "#f45454";
    let textColor = "#f4eac7";
    return (
        <AppWrapper backgroundColor={backgroundColor} textColor={textColor}>
            <Container>
                <div className="layout">

                </div>
            </Container>
        </AppWrapper>
    );
};

export default App;
