import React from "react";
import SvgLoader from "./svg-loader";
import Grid from '@material-ui/core/Grid';
import styled from 'styled-components';

const Infographics2Wrapper = styled.div`
    margin: 20px auto;
  .layout{
    background-color: ${props=> props.backgroundColor};
    color: ${props=> props.textColor};
    width: 900px;
    height: 500px;
    padding: 15px;
    
    .inner-layout{
      margin: 0 auto;
      height: 96%;
      width: 96%;
      border: ${props=> props.textColor} solid 4px;
      border-radius: 10px;
      display: flex;
      flex-direction: row;
      align-items: center;
      .text-section{
        font-weight: 600;
        font-size: 30px;
        margin: 0 auto 20px auto;
        width: 70%;
      }
      .map{
          height: 430px;
          width: 430px;
          g{
            fill: ${props=> props.textColor};
          }
        }
      
      .info-section{
        position: relative;
        margin-left: 30px;
        .element{
          position: absolute;
          top: 20px;
          left: 300px;
          height: 200px;
          width: 200px;
          fill: ${props=> props.backgroundColor};
          stroke: ${props=> props.textColor};
        }
      }
      .bar-wrapper{
        position: relative;
        margin-top: 20px;
        margin-left: 50px;
         span{
          position: absolute;
          font-weight: 700;
          font-size: 60px;
          left: 140px;
          top: -25px;
        }
        .bar-graph{
         height: 200px;
         width: 200px;
         fill: ${props=> props.textColor};
         stroke: ${props=> props.textColor};
        }
      }
      .right{
        margin-left: 50px;
      }
    }
  }
`;


const Infograpgic2 = (props) => {
    return(
        <Infographics2Wrapper backgroundColor={props.backgroundColor} textColor={props.textColor}>
            <div className="layout">
                <div className="inner-layout">
                    <Grid container spacing={3}>
                        <Grid item xs={6}>
                            <div className="info-section">
                                <SvgLoader className="map" name={props.code} type="map"/>
                                <SvgLoader className="element" name={props.element}/>
                            </div>
                        </Grid>
                        <Grid item xs={6}>
                            <Grid className="right" container spacing={3}>
                                <Grid item xs={12}>
                                    <div className="bar-wrapper">
                                        <span>{props.value}</span>
                                        { props.decrease ? (
                                            <SvgLoader className="bar-graph" name="bar-decrease"/>
                                        ) : ( <SvgLoader className="bar-graph" name="bar-increase"/>) }
                                    </div>
                                </Grid>
                                <Grid item xs={12}>
                                    <div className="text-section">
                                        {props.text}
                                    </div>
                                </Grid>
                            </Grid>
                        </Grid>
                    </Grid>
                </div>
            </div>
        </Infographics2Wrapper>
    )
};

export default Infograpgic2;
