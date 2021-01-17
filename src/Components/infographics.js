import React from "react";
import styled from 'styled-components';

const InfographicsWrapper = styled.div`
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



const Icon = ({ name, type, ...rest }) => {
    const ImportedIconRef = React.useRef(null);
    const [loading, setLoading] = React.useState(false);

    React.useEffect(() => {
        setLoading(true);
        const importIcon = async () => {
            try {
                ImportedIconRef.current =  type === "map" ?  (await import(`!!@svgr/webpack?-svgo,+titleProp,+ref!../assets/maps/${name}/vector.svg`)).default
                    : (await import(`!!@svgr/webpack?-svgo,+titleProp,+ref!../assets/elements/${name}.svg`)).default ;
            } catch (err) {
                // Your own error handling logic, throwing error for the sake of
                // simplicity
                throw err;
            } finally {
                setLoading(false);
            }
        };
        importIcon();
    }, [name]);

    if (!loading && ImportedIconRef.current) {
        const { current: ImportedIcon } = ImportedIconRef;
        return <ImportedIcon {...rest} />;
    }

    return null;
};

const Infograpgic = (props) => {
    return(
        <InfographicsWrapper backgroundColor={props.backgroundColor} textColor={props.textColor}>
            <div className="layout">
                <div className="inner-layout">
                    <div className="text-section">
                        <span>{props.value}</span>
                        {props.text}
                    </div>
                    <div className="info-section">
                        <Icon className="map" name={props.code} type="map"/>
                        <Icon className="element" name={props.element}/>
                    </div>
                </div>
            </div>
        </InfographicsWrapper>
    )
};

export default Infograpgic;
