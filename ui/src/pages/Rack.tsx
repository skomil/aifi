import { Pane } from "evergreen-ui";
import { FC } from "react";
import Navigation from "../components/Navigation";

interface RackProps {
    identifier: string;
}

const Rack: FC<RackProps> = ({ identifier }) => {
    return (
        <Pane>
            <Navigation path={["Racks", identifier]} />
            <h1>Rack {identifier}</h1>
        </Pane>
    );
};
export default Rack;