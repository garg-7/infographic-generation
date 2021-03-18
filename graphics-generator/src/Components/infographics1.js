import React from "react";
import SvgLoader from "./svg-loader";
import styled from 'styled-components';

const Infographics1Wrapper = styled.div`
    margin: 20px auto;
  .layout{
    background-color: ${props=> props.backgroundColor};
    color: ${props=> props.textColor};
    width: 500px;
    height: 500px;
    padding: 15px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    
    .inner-layout{
      margin: 0 auto;
      height: 96%;
      width: 96%;
      border: ${props=> props.textColor} solid 4px;
      border-radius: 10px;
      text-align: center;
      .text-section{
        span{
          display: block;
          font-weight: 700;
          font-size: 100px;
        }
        font-weight: 600;
        font-size: 30px;
        margin: 0 auto 20px auto;
        width: 70%;
      }
      
      .info-section{
        position: relative;
        .map{
          height: 250px;
          width: 250px;
          g{
            fill: ${props=> props.textColor};
          }
        }
        .element{
          position: absolute;
          top: 20px;
          left: 300px;
          height: 100px;
          width: 100px;
          fill: ${props=> props.backgroundColor};
          stroke: ${props=> props.textColor};
        }
      }
    }
  }
`;


const Infograpgic1 = (props) => {
    return(
        <Infographics1Wrapper backgroundColor={props.backgroundColor} textColor={props.textColor}>
            <div className="layout">
                <div className="inner-layout">
                    <div className="text-section">
                        <span>{props.value}</span>
                        {props.text}
                    </div>
                    <div className="info-section">
                        <SvgLoader className="map" name={props.code} type="map"/>
                        <SvgLoader className="element" name={props.element}/>
                    </div>
                </div>
            </div>
        </Infographics1Wrapper>
    )
};

export default Infograpgic1;
