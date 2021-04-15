import React from "react";
import styled from 'styled-components';
import slugify from "./slugify";
import countries from "i18n-iso-countries"

countries.registerLocale(require("i18n-iso-countries/langs/en.json"));

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

    const requestImageFile = require.context('../assets', true);

    const slug_sport = slugify(props.sport);
    let win_image = ""
    let lose_image = ""

    if(slug_sport === "cricket"){
        win_image = `./cricket/teams/${slugify(props.winning_team)}.png`
        lose_image = `./cricket/teams/${slugify(props.losing_team)}.png`
    }
    else if(slug_sport === "hockey"){
        const win = slugify(countries.getAlpha2Code(props.winning_team, "en"));
        const lose = slugify(countries.getAlpha2Code(props.losing_team, "en"));
        win_image = `./flags/${win}.png`
        lose_image = `./flags/${lose}.png`
    }
    else if(slug_sport === "tennis"){
        win_image = `./tennis/players/${slugify(props.winning_team)}.jpg`
        lose_image = `./tennis/players/${slugify(props.losing_team)}.jpg`
    }

    return(
        <SportsIngograhics1wrapper backgroundImage={requestImageFile(`./${slug_sport}/index.jpg`).default}>
            <div className="layout">
                <div className="blur"/>
                <div className="match">
                    {
                        props.match ? (
                            <>
                                <span>{props.match}</span> <br/>
                                <img src={requestImageFile(`./${slug_sport}/matches/${slugify(props.match)}.png`).default} alt={props.match}/>
                            </>
                        ) : (
                            <>
                                <span>{props.sport} Match</span> <br/>
                                <img src={requestImageFile(`./${slug_sport}/matches/index.png`).default} alt="match"/>
                            </>
                        )
                    }
                </div>
                <div className="teams">
                    <div className="team winner">
                        <img src={requestImageFile(win_image).default} alt="Winner"/>
                        <span>{props.winning_team}</span>
                    </div>
                    <div className="team loser">
                        <img src={requestImageFile(lose_image).default} alt="Loser"/>
                        <span>{props.losing_team}</span>
                    </div>
                </div>
                <div className="score">
                    <span>Defeats</span><br/>
                    {
                        props.score && (
                            <>
                                By {props.score}
                            </>
                        )
                    }
                </div>
            </div>
        </SportsIngograhics1wrapper>
    )
}

export default SportsIngograhics1;
