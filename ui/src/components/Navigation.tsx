import { Button, Heading, Link, Pane, defaultTheme, majorScale } from "evergreen-ui";
import { FC } from "react";

interface NavigationProps { 
    path: string[];
}
const Navigation: FC<NavigationProps> = () => {
    return (
        <Pane 
            backgroundColor={defaultTheme.colors.gray400} 
            height={majorScale(5)} display="flex" alignItems="center"
            paddingLeft={majorScale(2)} paddingRight={majorScale(2)}
            >
            <Heading size={800}>AIFI</Heading>
            <Button marginLeft={majorScale(2)} appearance="minimal" onClick={()=>{window.location.href = '/racks'}}>
                Racks
            </Button>
            <Pane width="100%" textAlign="right">
                <Button marginLeft={majorScale(2)} appearance="minimal" onClick={()=>{window.location.href = '/rig'}}>
                    Rig
                </Button>
            </Pane>
            
            
        </Pane>
    )
}
export default Navigation;