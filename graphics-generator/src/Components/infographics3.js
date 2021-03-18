import React from "react";
import SvgLoader from "./svg-loader";
import styled from 'styled-components';

const Infographics3Wrapper = styled.div`
    margin: 20px auto;
  .layout{
    background-color: ${props=> props.backgroundColor};
    color: ${props=> props.textColor};
    width: 580px;
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
          height: 350px;
          width: 350px;
          g{
            fill: ${props=> props.textColor};
          }
        }
        .element{
          position: absolute;
          top: 20px;
          left: 330px;
          height: 150px;
          width: 150px;
          fill: ${props=> props.backgroundColor};
          stroke: ${props=> props.textColor};
        }
        
        .arrow{
          position: absolute;
          fill: ${props=> props.backgroundColor};
          stroke: ${props=> props.textColor};
          height: 400px;
          //width: 350px;
          top: -30px;
          left: 70px;
        }
        .increase-text{
           position: absolute;
           font-weight: 700;
           font-size: 60px;
           top: -25px;
           left: 420px;
        }
        .decrease-text{
           position: absolute;
           font-weight: 700;
           font-size: 60px;
           left: 420px;
           bottom: -12px;
        }
      }
    }
  }
`;


const Infograpgic3 = (props) => {
    return(
        <Infographics3Wrapper backgroundColor={props.backgroundColor} textColor={props.textColor}>
            <div className="layout">
                <div className="inner-layout">
                    <div className="text-section">
                        {/*<span>{props.value}</span>*/}
                        {props.text}
                    </div>
                    <div className="info-section">
                        <SvgLoader className="map" name={props.code} type="map"/>
                        <SvgLoader className="element" name={props.element}/>
                        {props.decrease ? (
                            <>
                                <SvgLoader className="arrow" name="decrease-arrow"/>
                                <span className="decrease-text">{props.value}</span>
                            </>
                        ):(
                            <>
                            <SvgLoader className="arrow" name="increase-arrow"/>
                            <span className="increase-text">{props.value}</span>
                            </>
                        )}

                    </div>
                </div>
            </div>
        </Infographics3Wrapper>
    )
};

export default Infograpgic3;
