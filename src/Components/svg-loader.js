import React from "react";


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

export default Icon;
