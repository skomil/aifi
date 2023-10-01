import React from 'react';
import { render, screen } from '@testing-library/react';
import Rig from './Rig';

test('renders learn react link', () => {
  render(<Rig />);
  const linkElement = screen.getByText(/Rig/i);
  expect(linkElement).toBeInTheDocument();
});
