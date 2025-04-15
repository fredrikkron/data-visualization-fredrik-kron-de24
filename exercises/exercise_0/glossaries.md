## Glossary

terminology	| explanation
------------|------------
artist | The base class for all elements that can be drawn (lines, text, patches, etc.). Almost everything you see in a plot is an artist.
containers | Groupings of multiple artists (e.g., a bar chart’s bars and labels) to treat them as a single object. 
spine	| The borders of the plot area; typically the four lines (top, bottom, left, right) that frame the axes
axes| The individual plot area — one figure can have multiple axes (not to be confused with x/y axes).
figure | The entire drawing area or canvas, which can contain multiple subplots or axes.
subplot | A specific kind of axes positioned within a grid inside a figure (e.g., part of a multi-panel layout).
patch	| A shape (rectangle, circle, polygon, etc.) used to create graphics like bars, pies, or custom shapes.
annotation | Text or labels added to highlight or explain specific parts of the plot.
arrowprops | A dictionary of properties to style arrows in annotations (like color, width, headstyle, etc.).
marker | A symbol used to denote individual data points on a line or scatter plot (e.g., ‘o’, ‘x’, ‘^’).
ticks | The small marks along axes that indicate scale or values.
ticklabels | The text labels associated with ticks, showing the actual values or categories.
layout | The arrangement or spacing of subplots and elements within a figure
grid | A visual aid made of horizontal and/or vertical lines to align elements to data points.
legend | A guide that explains the symbols, colors, or lines used in the plot to differentiate data series.