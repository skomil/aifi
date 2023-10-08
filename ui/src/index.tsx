import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Rig from './pages/Rig';
import Racks from './pages/Racks';
import Rack from './pages/Rack';
import reportWebVitals from './reportWebVitals';
import {
  createBrowserRouter,
  RouterProvider,
  useParams
} from "react-router-dom";

const RackPage = () => {
  const { rackId } = useParams<{ rackId: string }>();
  return <Rack identifier={rackId} />;
};

const router = createBrowserRouter([
  {
    path: "/rig",
    element: <Rig />,
  },
  {
    path: "/racks",
    element: <Racks />,
  },
  {
    path: "/rack/:rackId",
    element: <RackPage />,
  },
]);

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
