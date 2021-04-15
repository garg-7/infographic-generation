import React from "react";
import styled from 'styled-components';
import cricket_image from "../assets/cricket/index.jpg"


const SportsIngograhics1wrapper = styled.div`
  margin: 20px auto;
  .layout{
    width: 1200px;
    height: 700px;
    background: url(${props=> props.backgroundImage}) no-repeat;
    background-size: cover;
    position: absolute;
    
    .blur{
      background: rgba(255, 255, 255, 0.2);
      backdrop-filter: blur(3px);
      width: 1200px;
      height: 700px;
      position: absolute;
    }
    
    .match{
      text-align: center;
      position: relative;
      margin-top: 26px;
      
      
      span{
        font-size: 45px;
        font-family: 'Dela Gothic One', cursive;
        color: #36454f;
      }
      
      img{
        width: 120px;
      }
    }
    
    .teams{
      position: relative;
      display: flex;
      align-items: center;
      justify-content: space-between;
      .team{
        display: flex;
        flex-direction: column;
        align-items: center;
        
        span{
          font-size: 30px;
          font-family: 'Dela Gothic One', cursive;
          color: white;
        }
      }
      .winner{
        margin-left: 70px;
      }
      .loser{
        margin-right: 70px;
      }
      img{
        height: 250px;
      }
    }

    .score{
      position: relative;
      text-align: center;
      font-size: 25px;
      font-family: 'Dela Gothic One', cursive;
      color: white;
      
      span{
        font-size: 40px;
      }
    }
  }
`;



const SportsIngograhics1 = (props) =>{

    // const im = require("../assets/cricket/matches/icc-mens-cricket-world-cup.png")
    const requestImageFile = require.context('../assets', true);


    return(
        <SportsIngograhics1wrapper backgroundImage={requestImageFile("./cricket/index.jpg").default}>
            <div className="layout">
                <div className="blur"/>
                <div className="match">
                    <span>ICC Men's Cricket World Cup</span> <br/>
                    <img src={requestImageFile("./cricket/matches/icc-mens-cricket-world-cup.png").default} alt="ICC Men's Cricket World Cup"/>
                </div>
                <div className="teams">
                    <div className="team winner">
                        <img src={requestImageFile("./cricket/teams/india.png").default} alt="Winner"/>
                        <span>India</span>
                    </div>
                    <div className="team loser">
                        <img src={requestImageFile("./cricket/teams/england.png").default} alt="Loser"/>
                        <span>England</span>
                    </div>
                </div>
                <div className="score">
                    <span>Defeats</span><br/>
                    By 5 runs
                </div>
            </div>
        </SportsIngograhics1wrapper>
    )
}

export default SportsIngograhics1;
