---
content_hash: 95d387efc7f91acc0c24e687adb4eecf6353ebf598fe8c53cb77701a31bed22e
fetched_at: '2026-06-28T21:44:18.546446+00:00'
product: fluig
source: style-guide
title: TOTVS Fluig Developer
type: documentation
url: https://style.fluig.com/chart.html
---

# About

Style Guide includes a component for creating charts based on chartjs and gauge.js

#### Charts should only be used for low online data volume. For large volumes of data and complex graphics, must compulsorily use [Analytics](http://tdn.totvs.com/display/fluig/Analytics).

The Chart components of the Fluig Style Guide are based on the **Chart.js** and **gauge.js** plugins.

#### While it is possible to use these two plugins directly, it is not recommended as you may be impacted by a future update. Always use the FLUIGC.chart component to create your charts.

| Plugin | Version | Description | Documentation |
| --- | --- | --- | --- |
| Chart.js | 2.9.4 | Chart.js is a free JavaScript library for making HTML-based charts. It is one of the simplest visualization libraries for JavaScript, and comes with the following built-in chart types: Scatter Plot. Line Chart. | <https://www.chartjs.org/docs/2.9.4/getting-started/> |
| gauge.js | 1.3.7 | The Gauge.js library is a lightweight JavaScript tool for creating interactive and visually appealing circular gauges, commonly used to represent a single metric on dashboards. It allows easy customization and integration into web pages. | <https://github.com/bernii/gauge.js> |

### Creating charts with Developer Studio using the Style Guide

If you want to create forms using the style guide and add charts,
you'll need to import the minified CSS and JavaScript files.
To import them, follow the example below, not forgetting
to import the `fluig-style-guide-chart.min.js` file:

```
	<head>
	<link rel="stylesheet" type="text/css" href="/style-guide/css/fluig-style-guide-flat.min.css">
	<script src="/portal/resources/js/jquery/jquery.js"></script>
	<script src="/portal/resources/js/jquery/jquery-ui.min.js"></script>
	<script src="/style-guide/js/fluig-style-guide.min.js"></script>
	<script src="/style-guide/js/fluig-style-guide-chart.min.js"></script>
	</head>
	<body>
		<div class="fluig-style-guide">
			<!--Some code here-->
		</div>
	</body>
```

### Using charts in widgets

To use charts in widgets, you must inform the following line in the `application.info` file of your widget:

```
	application.resource.component.1=fluigchart
```

# Configurations

## Animations

Chart.js animates charts out of the box. A number of options are provided to configure how the animation looks and how long it takes.

### Animation Configuration

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `duration` | `number` | `1000` | The number of milliseconds an animation takes. |
| `easing` | `string` | `'easeOutQuart'` | Easing function to use. more... |
| `onProgress` | `function` | `null` | Callback called on each step of an animation. more... |
| `onComplete` | `function` | `null` | Callback called at the end of an animation. more... |

### Easing

Available options are:

* `'linear'`
* `'easeInQuad'`
* `'easeOutQuad'`
* `'easeInOutQuad'`
* `'easeInCubic'`
* `'easeOutCubic'`
* `'easeInOutCubic'`
* `'easeInQuart'`
* `'easeOutQuart'`
* `'easeInOutQuart'`
* `'easeInQuint'`
* `'easeOutQuint'`
* `'easeInOutQuint'`
* `'easeInSine'`
* `'easeOutSine'`
* `'easeInOutSine'`
* `'easeInExpo'`
* `'easeOutExpo'`
* `'easeInOutExpo'`
* `'easeInCirc'`
* `'easeOutCirc'`
* `'easeInOutCirc'`
* `'easeInElastic'`
* `'easeOutElastic'`
* `'easeInOutElastic'`
* `'easeInBack'`
* `'easeOutBack'`
* `'easeInOutBack'`
* `'easeInBounce'`
* `'easeOutBounce'`
* `'easeInOutBounce'`

See Robert Penner's easing equations.

### Animation Callbacks

The `onProgress` and `onComplete` callbacks are useful for synchronizing an external draw to the chart animation. The callback is passed a `Chart.Animation` instance:

```
    {
        // Chart object
        chart: Chart,

        // Current Animation frame number
        currentStep: number,

        // Number of animation frames
        numSteps: number,

        // Animation easing to use
        easing: string,

        // Function that renders the chart
        render: function,

        // User callback
        onAnimationProgress: function,

        // User callback
        onAnimationComplete: function
    }
```

The following example fills a progress bar during the chart animation.

```
    var chart = FLUIGC.chart('#MY_SELECTOR', {
        id: 'set_an_id_for_my_chart',
        width: '700',
        height: '200',
    });
    // call the bar function
    var barChart = chart.bar(data, {
        animation: {
            onProgress: function(animation) {
                progress.value = animation.animationObject.currentStep / animation.animationObject.numSteps;
            }
        }
    });
```

Another example usage of these callbacks can be found on Github: this sample displays a progress bar showing how far along the animation is.

## Layout Configuration

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `padding` | `number|object` | `0` | The padding to add inside the chart. more... |

### Padding

If this value is a number, it is applied to all sides of the chart (left, top, right, bottom). If this value is an object, the `left` property defines the left padding. Similarly the `right`, `top` and `bottom` properties can also be specified.

Lets say you wanted to add 50px of padding to the left side of the chart canvas, you would do:

```
    var chart = FLUIGC.chart('#MY_SELECTOR', {
        id: 'set_an_id_for_my_chart',
        width: '700',
        height: '200',
    });
    // call the line function
    var lineChart = chart.line(data, {
        layout: {
            padding: {
                left: 50,
                right: 0,
                top: 0,
                bottom: 0
            }
        }
    });
```

## Legend Configuration

The chart legend displays data about the datasets that are appearing on the chart.

### Configuration options

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `display` | `boolean` | `true` | Is the legend shown? |
| `position` | `string` | `'top'` | Position of the legend. more... |
| `align` | `string` | `'center'` | Alignment of the legend. more... |
| `fullWidth` | `boolean` | `true` | Marks that this box should take the full width of the canvas (pushing down other boxes). This is unlikely to need to be changed in day-to-day use. |
| `onClick` | `function` |  | A callback that is called when a click event is registered on a label item. |
| `onHover` | `function` |  | A callback that is called when a 'mousemove' event is registered on top of a label item. |
| `onLeave` | `function` |  | A callback that is called when a 'mousemove' event is registered outside of a previously hovered label item. |
| `reverse` | `boolean` | `false` | Legend will show datasets in reverse order. |
| `labels` | `object` |  | See the Legend Label Configuration section below. |
| `rtl` | `boolean` |  | `true` for rendering the legends from right to left. |
| `textDirection` | `string` | canvas' default | This will force the text direction `'rtl' | 'ltr` on the canvas for rendering the legend, regardless of the css specified on the canvas |

### Position

Position of the legend. Options are:

* `'top'`
* `'left'`
* `'bottom'`
* `'right'`

### Align

Alignment of the legend. Options are:

* `'start'`
* `'center'`
* `'end'`

Defaults to `'center'` for unrecognized values.

### Legend Label Configuration

The legend label configuration is nested below the legend configuration using the `labels` key.

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `boxWidth` | `number` | `40` | Width of coloured box. |
| `fontSize` | `number` | `12` | Font size of text. |
| `fontStyle` | `string` | `'normal'` | Font style of text. |
| `fontColor` | `Color` | `'#666'` | Color of text. |
| `fontFamily` | `string` | `"'Lato', Arial, sans-serif"` | Font family of legend text. |
| `padding` | `number` | `10` | Padding between rows of colored boxes. |
| `generateLabels` | `function` |  | Generates legend items for each thing in the legend. Default implementation returns the text + styling for the color box. See Legend Item for details. |
| `filter` | `function` | `null` | Filters legend items out of the legend. Receives 2 parameters, a Legend Item and the chart data. |
| `usePointStyle` | `boolean` | `false` | Label style will match corresponding point style (size is based on the mimimum value between boxWidth and fontSize). |

### Legend Item Interface

Items passed to the legend `onClick` function are the ones returned from `labels.generateLabels`. These items must implement the following interface.

```
    {
        // Label that will be displayed
        text: string,

        // Fill style of the legend box
        fillStyle: Color,

        // If true, this item represents a hidden dataset. Label will be rendered with a strike-through effect
        hidden: boolean,

        // For box border. See https://developer.mozilla.org/en/docs/Web/API/CanvasRenderingContext2D/lineCap
        lineCap: string,

        // For box border. See https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/setLineDash
        lineDash: number[],

        // For box border. See https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/lineDashOffset
        lineDashOffset: number,

        // For box border. See https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/lineJoin
        lineJoin: string,

        // Width of box border
        lineWidth: number,

        // Stroke style of the legend box
        strokeStyle: Color,

        // Point style of the legend box (only used if usePointStyle is true)
        pointStyle: string | Image,

        // Rotation of the point in degrees (only used if usePointStyle is true)
        rotation: number
    }
```

### Example

The following example will create a chart with the legend enabled and turn all of the text red in color.

```
    var chart = FLUIGC.chart('#MY_SELECTOR', {
        id: 'set_an_id_for_my_chart',
        width: '700',
        height: '200',
    });
    // call the bar function
    var barChart = chart.bar(data, {
        legend: {
            display: true,
            labels: {
                fontColor: 'rgb(255, 99, 132)'
            }
        }
    });
```

### Custom On Click Actions

It can be common to want to trigger different behaviour when clicking an item in the legend. This can be easily achieved using a callback in the config object.

The default legend click handler is:

```
    function(e, legendItem) {
        var index = legendItem.datasetIndex;
        var ci = this.chart;
        var meta = ci.getDatasetMeta(index);

        // See controller.isDatasetVisible comment
        meta.hidden = meta.hidden === null ? !ci.data.datasets[index].hidden : null;

        // We hid a dataset ... rerender the chart
        ci.update();
    }
```

Lets say we wanted instead to link the display of the first two datasets. We could change the click handler accordingly.

```
    var defaultLegendClickHandler = Chart.defaults.global.legend.onClick;
    var newLegendClickHandler = function (e, legendItem) {
        var index = legendItem.datasetIndex;

        if (index > 1) {
            // Do the original logic
            defaultLegendClickHandler(e, legendItem);
        } else {
            let ci = this.chart;
            [
                ci.getDatasetMeta(0),
                ci.getDatasetMeta(1)
            ].forEach(function(meta) {
                meta.hidden = meta.hidden === null ? !ci.data.datasets[index].hidden : null;
            });
            ci.update();
        }
    };

    var chart = FLUIGC.chart('#MY_SELECTOR', {
        id: 'set_an_id_for_my_chart',
        width: '700',
        height: '200',
    });
    // call the line function
    var lineChart = chart.line(data, {
        legend: {
            onClick: newLegendClickHandler
        }
    });
```

Now when you click the legend in this chart, the visibility of the first two datasets will be linked together.

### HTML Legends

Sometimes you need a very complex legend. In these cases, it makes sense to generate an HTML legend. Charts provide a `generateLegend()` method on their prototype that returns an HTML string for the legend.

To configure how this legend is generated, you can change the `legendCallback` config property.

```
    var chart = FLUIGC.chart('#MY_SELECTOR', {
        id: 'set_an_id_for_my_chart',
        width: '700',
        height: '200',
    });
    // call the line function
    var lineChart = chart.line(data, {
        legendCallback: function(chart) {
            // Return the HTML string here.
        }
    });
```

Note that legendCallback is not called automatically and you must call `generateLegend()` yourself in code when creating a legend using this method.

## Title

The chart title defines text to draw at the top of the chart.

### Title Configuration

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `display` | `boolean` | `false` | Is the title shown? |
| `position` | `string` | `'top'` | Position of title. more... |
| `fontSize` | `number` | `12` | Font size. |
| `fontFamily` | `string` | `"'Lato', Arial, sans-serif"` | Font family for the title text. |
| `fontColor` | `Color` | `'#666'` | Font color. |
| `fontStyle` | `string` | `'bold'` | Font style. |
| `padding` | `number` | `10` | Number of pixels to add above and below the title text. |
| `lineHeight` | `number|string` | `1.2` | Height of an individual line of text. See MDN. |
| `text` | `string|string[]` | `''` | Title text to display. If specified as an array, text is rendered on multiple lines. |

### Position

Possible title position values are:

* `'top'`
* `'left'`
* `'bottom'`
* `'right'`

### Example Usage

The example below would enable a title of 'Custom Chart Title' on the chart that is created.

```
    var chart = FLUIGC.chart('#MY_SELECTOR', {
        id: 'set_an_id_for_my_chart',
        width: '700',
        height: '200',
    });
    // call the line function
    var lineChart = chart.line(data, {
        title: {
            display: true,
            text: 'Custom Chart Title'
        }
    });
```

## Tooltips

### Tooltip Configuration

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `enabled` | `boolean` | `true` | Are on-canvas tooltips enabled? |
| `custom` | `function` | `null` | See custom tooltip section. |
| `mode` | `string` | `'nearest'` | Sets which elements appear in the tooltip. more.... |
| `intersect` | `boolean` | `true` | If true, the tooltip mode applies only when the mouse position intersects with an element. If false, the mode will be applied at all times. |
| `position` | `string` | `'average'` | The mode for positioning the tooltip. more... |
| `callbacks` | `object` |  | See the callbacks section. |
| `itemSort` | `function` |  | Sort tooltip items. more... |
| `filter` | `function` |  | Filter tooltip items. more... |
| `backgroundColor` | `Color` | `'rgba(0, 0, 0, 0.8)'` | Background color of the tooltip. |
| `titleFontFamily` | `string` | `"'Lato', Arial, sans-serif"` | Title font. |
| `titleFontSize` | `number` | `12` | Title font size. |
| `titleFontStyle` | `string` | `'bold'` | Title font style. |
| `titleFontColor` | `Color` | `'#fff'` | Title font color. |
| `titleAlign` | `string` | `'left'` | Horizontal alignment of the title text lines. more... |
| `titleSpacing` | `number` | `2` | Spacing to add to top and bottom of each title line. |
| `titleMarginBottom` | `number` | `6` | Margin to add on bottom of title section. |
| `bodyFontFamily` | `string` | `"'Lato', Arial, sans-serif"` | Body line font. |
| `bodyFontSize` | `number` | `12` | Body font size. |
| `bodyFontStyle` | `string` | `'normal'` | Body font style. |
| `bodyFontColor` | `Color` | `'#fff'` | Body font color. |
| `bodyAlign` | `string` | `'left'` | Horizontal alignment of the body text lines. more... |
| `bodySpacing` | `number` | `2` | Spacing to add to top and bottom of each tooltip item. |
| `footerFontFamily` | `string` | `"'Lato', Arial, sans-serif"` | Footer font. |
| `footerFontSize` | `number` | `12` | Footer font size. |
| `footerFontStyle` | `string` | `'bold'` | Footer font style. |
| `footerFontColor` | `Color` | `'#fff'` | Footer font color. |
| `footerAlign` | `string` | `'left'` | Horizontal alignment of the footer text lines. more... |
| `footerSpacing` | `number` | `2` | Spacing to add to top and bottom of each footer line. |
| `footerMarginTop` | `number` | `6` | Margin to add before drawing the footer. |
| `xPadding` | `number` | `6` | Padding to add on left and right of tooltip. |
| `yPadding` | `number` | `6` | Padding to add on top and bottom of tooltip. |
| `caretPadding` | `number` | `2` | Extra distance to move the end of the tooltip arrow away from the tooltip point. |
| `caretSize` | `number` | `5` | Size, in px, of the tooltip arrow. |
| `cornerRadius` | `number` | `6` | Radius of tooltip corner curves. |
| `multiKeyBackground` | `Color` | `'#fff'` | Color to draw behind the colored boxes when multiple items are in the tooltip. |
| `displayColors` | `boolean` | `true` | If true, color boxes are shown in the tooltip. |
| `borderColor` | `Color` | `'rgba(0, 0, 0, 0)'` | Color of the border. |
| `borderWidth` | `number` | `0` | Size of the border. |
| `rtl` | `boolean` |  | `true` for rendering the legends from right to left. |
| `textDirection` | `string` | canvas' default | This will force the text direction `'rtl' | 'ltr` on the canvas for rendering the tooltips, regardless of the css specified on the canvas |

### Alignment

The `titleAlign`, `bodyAlign` and `footerAlign` options define the horizontal position of the text lines with respect to the tooltip box. The following values are supported.

* `'left'` (default)
* `'right'`
* `'center'`

These options are only applied to text lines. Color boxes are always aligned to the left edge.

### Sort Callback

Allows sorting of tooltip items. Must implement at minimum a function that can be passed to Array.prototype.sort. This function can also accept a third parameter that is the data object passed to the chart.

### Filter Callback

Allows filtering of tooltip items. Must implement at minimum a function that can be passed to Array.prototype.filter. This function can also accept a second parameter that is the data object passed to the chart.

### Tooltip Callbacks

The tooltip label configuration is nested below the tooltip configuration using the `callbacks` key. The tooltip has the following callbacks for providing text. For all functions, `this` will be the tooltip object created from the `Chart.Tooltip` constructor.

All functions are called with the same arguments: a tooltip item and the `data` object passed to the chart. All functions must return either a string or an array of strings. Arrays of strings are treated as multiple lines of text.

| Name | Arguments | Description |
| --- | --- | --- |
| `beforeTitle` | `TooltipItem[], object` | Returns the text to render before the title. |
| `title` | `TooltipItem[], object` | Returns text to render as the title of the tooltip. |
| `afterTitle` | `TooltipItem[], object` | Returns text to render after the title. |
| `beforeBody` | `TooltipItem[], object` | Returns text to render before the body section. |
| `beforeLabel` | `TooltipItem, object` | Returns text to render before an individual label. This will be called for each item in the tooltip. |
| `label` | `TooltipItem, object` | Returns text to render for an individual item in the tooltip. more... |
| `labelColor` | `TooltipItem, Chart` | Returns the colors to render for the tooltip item. more... |
| `labelTextColor` | `TooltipItem, Chart` | Returns the colors for the text of the label for the tooltip item. |
| `afterLabel` | `TooltipItem, object` | Returns text to render after an individual label. |
| `afterBody` | `TooltipItem[], object` | Returns text to render after the body section. |
| `beforeFooter` | `TooltipItem[], object` | Returns text to render before the footer section. |
| `footer` | `TooltipItem[], object` | Returns text to render as the footer of the tooltip. |
| `afterFooter` | `TooltipItem[], object` | Text to render after the footer section. |

### Label Callback

The `label` callback can change the text that displays for a given data point. A common example to round data values; the following example rounds the data to two decimal places.

```
    var chart = FLUIGC.chart('#MY_SELECTOR', {
        id: 'set_an_id_for_my_chart',
        width: '700',
        height: '200',
    });
    // call the line function
    var lineChart = chart.line(data, {
        tooltips: {
            callbacks: {
                label: function(tooltipItem, data) {
                    var label = data.datasets[tooltipItem.datasetIndex].label || '';

                    if (label) {
                        label += ': ';
                    }
                    label += Math.round(tooltipItem.yLabel * 100) / 100;
                    return label;
                }
            }
        }
    });
```

### Label Color Callback

For example, to return a red box for each item in the tooltip you could do:

```
    var chart = FLUIGC.chart('#MY_SELECTOR', {
        id: 'set_an_id_for_my_chart',
        width: '700',
        height: '200',
    });
    // call the line function
    var lineChart = chart.line(data, {
        tooltips: {
            callbacks: {
                labelColor: function(tooltipItem, chart) {
                    return {
                        borderColor: 'rgb(255, 0, 0)',
                        backgroundColor: 'rgb(255, 0, 0)'
                    };
                },
                labelTextColor: function(tooltipItem, chart) {
                    return '#543453';
                }
            }
        }
    });
```

### Tooltip Item Interface

The tooltip items passed to the tooltip callbacks implement the following interface.

```
    {
        // Label for the tooltip
        label: string,

        // Value for the tooltip
        value: string,

        // X Value of the tooltip
        // (deprecated) use `value` or `label` instead
        xLabel: number | string,

        // Y value of the tooltip
        // (deprecated) use `value` or `label` instead
        yLabel: number | string,

        // Index of the dataset the item comes from
        datasetIndex: number,

        // Index of this data item in the dataset
        index: number,

        // X position of matching point
        x: number,

        // Y position of matching point
        y: number
    }
```

### External (Custom) Tooltips

Custom tooltips allow you to hook into the tooltip rendering process so that you can render the tooltip in your own custom way. Generally this is used to create an HTML tooltip instead of an oncanvas one. You can enable custom tooltips in the global or chart configuration like so:

```
    var chart = FLUIGC.chart('#MY_SELECTOR', {
        id: 'set_an_id_for_my_chart',
        width: '700',
        height: '200',
    });
    // call the line function
    var lineChart = chart.line(data, {
        tooltips: {
            // Disable the on-canvas tooltip
            enabled: false,

            custom: function(tooltipModel) {
                // Tooltip Element
                var tooltipEl = document.getElementById('chartjs-tooltip');

                // Create element on first render
                if (!tooltipEl) {
                    tooltipEl = document.createElement('div');
                    tooltipEl.id = 'chartjs-tooltip';
                    tooltipEl.innerHTML = '
```

';
document.body.appendChild(tooltipEl);
}
// Hide if no tooltip
if (tooltipModel.opacity === 0) {
tooltipEl.style.opacity = 0;
return;
}
// Set caret Position
tooltipEl.classList.remove('above', 'below', 'no-transform');
if (tooltipModel.yAlign) {
tooltipEl.classList.add(tooltipModel.yAlign);
} else {
tooltipEl.classList.add('no-transform');
}
function getBody(bodyItem) {
return bodyItem.lines;
}
// Set Text
if (tooltipModel.body) {
var titleLines = tooltipModel.title || [];
var bodyLines = tooltipModel.body.map(getBody);
var innerHtml = '';
titleLines.forEach(function(title) {
innerHtml += '| ' + title + ' |
| --- |
';
});
innerHtml += '';
bodyLines.forEach(function(body, i) {
var colors = tooltipModel.labelColors[i];
var style = 'background:' + colors.backgroundColor;
style += '; border-color:' + colors.borderColor;
style += '; border-width: 2px';
var span = '';
innerHtml += '| ' + span + body + ' |
';
});
innerHtml += '';
var tableRoot = tooltipEl.querySelector('table');
tableRoot.innerHTML = innerHtml;
}
// `this` will be the overall tooltip
var position = this.\_chart.canvas.getBoundingClientRect();
// Display, position, and set styles for font
tooltipEl.style.opacity = 1;
tooltipEl.style.position = 'absolute';
tooltipEl.style.left = position.left + window.pageXOffset + tooltipModel.caretX + 'px';
tooltipEl.style.top = position.top + window.pageYOffset + tooltipModel.caretY + 'px';
tooltipEl.style.fontFamily = tooltipModel.\_bodyFontFamily;
tooltipEl.style.fontSize = tooltipModel.bodyFontSize + 'px';
tooltipEl.style.fontStyle = tooltipModel.\_bodyFontStyle;
tooltipEl.style.padding = tooltipModel.yPadding + 'px ' + tooltipModel.xPadding + 'px';
tooltipEl.style.pointerEvents = 'none';
}
}
});

See samples for examples on how to get started with custom tooltips.

### Tooltip Model

The tooltip model contains parameters that can be used to render the tooltip.

```
    {
        // The items that we are rendering in the tooltip. See Tooltip Item Interface section
        dataPoints: TooltipItem[],

        // Positioning
        xPadding: number,
        yPadding: number,
        xAlign: string,
        yAlign: string,

        // X and Y properties are the top left of the tooltip
        x: number,
        y: number,
        width: number,
        height: number,
        // Where the tooltip points to
        caretX: number,
        caretY: number,

        // Body
        // The body lines that need to be rendered
        // Each object contains 3 parameters
        // before: string[] // lines of text before the line with the color square
        // lines: string[], // lines of text to render as the main item with color square
        // after: string[], // lines of text to render after the main lines
        body: object[],
        // lines of text that appear after the title but before the body
        beforeBody: string[],
        // line of text that appear after the body and before the footer
        afterBody: string[],
        bodyFontColor: Color,
        _bodyFontFamily: string,
        _bodyFontStyle: string,
        _bodyAlign: string,
        bodyFontSize: number,
        bodySpacing: number,

        // Title
        // lines of text that form the title
        title: string[],
        titleFontColor: Color,
        _titleFontFamily: string,
        _titleFontStyle: string,
        titleFontSize: number,
        _titleAlign: string,
        titleSpacing: number,
        titleMarginBottom: number,

        // Footer
        // lines of text that form the footer
        footer: string[],
        footerFontColor: Color,
        _footerFontFamily: string,
        _footerFontStyle: string,
        footerFontSize: number,
        _footerAlign: string,
        footerSpacing: number,
        footerMarginTop: number,

        // Appearance
        caretSize: number,
        caretPadding: number,
        cornerRadius: number,
        backgroundColor: Color,

        // colors to render for each item in body[]. This is the color of the squares in the tooltip
        labelColors: Color[],
        labelTextColors: Color[],

        // 0 opacity is a hidden tooltip
        opacity: number,
        legendColorBackground: Color,
        displayColors: boolean,
        borderColor: Color,
        borderWidth: number
    }
```

## Elements

While chart types provide settings to configure the styling of each dataset, you sometimes want to style **all datasets the same way**. A common example would be to stroke all of the bars in a bar chart with the same colour but change the fill per dataset. Options can be configured for four different types of elements: **arc**, **lines**, **points**, and **rectangles**. When set, these options apply to all objects of that type unless specifically overridden by the configuration attached to a dataset.

### Point Configuration

Point elements are used to represent the points in a line, radar or bubble chart.

Global point options: `Chart.defaults.global.elements.point`.

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `radius` | `number` | `3` | Point radius. |
| `pointStyle` | `string|Image` | `'circle'` | Point style. |
| `rotation` | `number` | `0` | Point rotation (in degrees). |
| `backgroundColor` | `Color` | `'rgba(0, 0, 0, 0.1)'` | Point fill color. |
| `borderWidth` | `number` | `1` | Point stroke width. |
| `borderColor` | `Color` | `'rgba(0, 0, 0, 0.1)'` | Point stroke color. |
| `hitRadius` | `number` | `1` | Extra radius added to point radius for hit detection. |
| `hoverRadius` | `number` | `4` | Point radius when hovered. |
| `hoverBorderWidth` | `number` | `1` | Stroke width when hovered. |

### Point Styles

The following values are supported:

* `'circle'`
* `'cross'`
* `'crossRot'`
* `'dash'`
* `'line'`
* `'rect'`
* `'rectRounded'`
* `'rectRot'`
* `'star'`
* `'triangle'`

If the value is an image, that image is drawn on the canvas using drawImage.

### Line Configuration

Line elements are used to represent the line in a line chart.

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `tension` | `number` | `0.4` | Bézier curve tension ( `0` for no Bézier curves). |
| `backgroundColor` | `Color` | `'rgba(0, 0, 0, 0.1)'` | Line fill color. |
| `borderWidth` | `number` | `3` | Line stroke width. |
| `borderColor` | `Color` | `'rgba(0, 0, 0, 0.1)'` | Line stroke color. |
| `borderCapStyle` | `string` | `'butt'` | Line cap style. See MDN. |
| `borderDash` | `number[]` | `[]` | Line dash. See MDN. |
| `borderDashOffset` | `number` | `0.0` | Line dash offset. See MDN. |
| `borderJoinStyle` | `string` | `'miter'` | Line join style. See MDN. |
| `capBezierPoints` | `boolean` | `true` | `true` to keep Bézier control inside the chart, `false` for no restriction. |
| `cubicInterpolationMode` | `string` | `'default'` | Interpolation mode to apply. See more... |
| `fill` | `boolean|string` | `true` | How to fill the area under the line. See area charts. |
| `stepped` | `boolean` | `false` | `true` to show the line as a stepped line ( `tension` will be ignored). |

### Rectangle Configuration

Rectangle elements are used to represent the bars in a bar chart.

Global rectangle options: `Chart.defaults.global.elements.rectangle`.

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `backgroundColor` | `Color` | `'rgba(0, 0, 0, 0.1)'` | Bar fill color. |
| `borderWidth` | `number` | `0` | Bar stroke width. |
| `borderColor` | `Color` | `'rgba(0, 0, 0, 0.1)'` | Bar stroke color. |
| `borderSkipped` | `string` | `'bottom'` | Skipped (excluded) border: `'bottom'`, `'left'`, `'top'` or `'right'`. |

### Arc Configuration

Arcs are used in the polar area, doughnut and pie charts.

Global arc options: `Chart.defaults.global.elements.arc`.

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `angle` - for polar only | `number` | `circumference / (arc count)` | Arc angle to cover. |
| `backgroundColor` | `Color` | `'rgba(0, 0, 0, 0.1)'` | Arc fill color. |
| `borderAlign` | `string` | `'center'` | Arc stroke alignment. |
| `borderColor` | `Color` | `'#fff'` | Arc stroke color. |
| `borderWidth` | `number` | `2` | Arc stroke width. |

# Chart Line

## Examples

A line chart is a way of plotting data points on a line.

### Live demo

Below an example of line chart

Add
Update
Remove

### HTML

```
<div id="MY_SELECTOR"></div>
```

### Javascript

Below is the basic configuration to use the line chart.

```
var chart = FLUIGC.chart('#MY_SELECTOR');
// call the line function
var lineChart = chart.line(data, options);
```

### Javascript

Below is the configuration, with the id, width and height of the canvas.

```
var chart = FLUIGC.chart('#MY_SELECTOR', {
	id: 'set_an_id_for_my_chart',
	width: '700',
	height: '200',
	/* See the list of options */
});
// call the line function
var lineChart = chart.line(data, options);
```

### Data structure

The line chart requires an array of labels for each of the data points.
Each dataset has a colour for the fill, a colour for the line and colours for the points and strokes of the points.

```
var data = {
    labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
    datasets: [
        {
            label: 'My First dataset',
            data: [65, 59, 80, 81, 56, 55, 40],
            backgroundColor: 'rgba(170, 194, 77, 0.5)',
            hoverBackgroundColor: 'rgba(170, 194, 77, 0.5)',
            borderColor: '#b0cc49',
            hoverBorderColor: '#b0cc49'
        },
        {
            label: 'My Second dataset',
            data: [28, 48, 40, 19, 86, 27, 90],
            backgroundColor: 'rgba(190, 49, 88, 0.5)',
            hoverBackgroundColor: 'rgba(190, 49, 88, 0.5)',
            borderColor: '#ed145b',
            hoverBorderColor: '#ed145b'
        }
    ]
};
```

### Dataset Properties

The line chart allows a number of properties to be specified for each dataset. These are used to set display properties for a specific dataset. For example, the colour of a line is generally set this way.

| Name | Type | Scriptable | Indexable | Default |
| --- | --- | --- | --- | --- |
| `backgroundColor` | `Color` | Yes | - | `'rgba(0, 0, 0, 0.1)'` |
| `borderCapStyle` | `string` | Yes | - | `'butt'` |
| `borderColor` | `Color` | Yes | - | `'rgba(0, 0, 0, 0.1)'` |
| `borderDash` | `number[]` | Yes | - | `[]` |
| `borderDashOffset` | `number` | Yes | - | `0.0` |
| `borderJoinStyle` | `string` | Yes | - | `'miter'` |
| `borderWidth` | `number` | Yes | - | `3` |
| `cubicInterpolationMode` | `string` | Yes | - | `'default'` |
| `clip` | `number|object` | - | - | `borderWidth / 2` |
| `fill` | `boolean|string` | Yes | - | `true` |
| `hoverBackgroundColor` | `Color` | Yes | - | `undefined` |
| `hoverBorderCapStyle` | `string` | Yes | - | `undefined` |
| `hoverBorderColor` | `Color` | Yes | - | `undefined` |
| `hoverBorderDash` | `number[]` | Yes | - | `undefined` |
| `hoverBorderDashOffset` | `number` | Yes | - | `undefined` |
| `hoverBorderJoinStyle` | `string` | Yes | - | `undefined` |
| `hoverBorderWidth` | `number` | Yes | - | `undefined` |
| `label` | `string` | - | - | `''` |
| `lineTension` | `number` | - | - | `0.4` |
| `order` | `number` | - | - | `0` |
| `pointBackgroundColor` | `Color` | Yes | Yes | `'rgba(0, 0, 0, 0.1)'` |
| `pointBorderColor` | `Color` | Yes | Yes | `'rgba(0, 0, 0, 0.1)'` |
| `pointBorderWidth` | `number` | Yes | Yes | `1` |
| `pointHitRadius` | `number` | Yes | Yes | `1` |
| `pointHoverBackgroundColor` | `Color` | Yes | Yes | `undefined` |
| `pointHoverBorderColor` | `Color` | Yes | Yes | `undefined` |
| `pointHoverBorderWidth` | `number` | Yes | Yes | `1` |
| `pointHoverRadius` | `number` | Yes | Yes | `4` |
| `pointRadius` | `number` | Yes | Yes | `3` |
| `pointRotation` | `number` | Yes | Yes | `0` |
| `pointStyle` | `string|Image` | Yes | Yes | `'circle'` |
| `showLine` | `boolean` | - | - | `undefined` |
| `spanGaps` | `boolean` | - | - | `undefined` |
| `steppedLine` | `boolean|string` | - | - | `false` |
| `xAxisID` | `string` | - | - | first x axis |
| `yAxisID` | `string` | - | - | first y axis |

### General

| Name | Description |
| --- | --- |
| `label` | The label for the dataset which appears in the legend and tooltips. |
| `order` | The drawing order of dataset. Also affects order for stacking, tooltip, and legend. |
| `xAxisID` | The ID of the x axis to plot this dataset on. |
| `yAxisID` | The ID of the y axis to plot this dataset on. |

### Point Styling

The style of each point can be controlled with the following properties:

| Name | Description |
| --- | --- |
| `pointBackgroundColor` | The fill color for points. |
| `pointBorderColor` | The border color for points. |
| `pointBorderWidth` | The width of the point border in pixels. |
| `pointHitRadius` | The pixel size of the non-displayed point that reacts to mouse events. |
| `pointRadius` | The radius of the point shape. If set to 0, the point is not rendered. |
| `pointRotation` | The rotation of the point in degrees. |
| `pointStyle` | Style of the point. more... |

All these values, if `undefined`, fallback first to the dataset options then to the associated `elements.point.*` options.

### Line Styling

The style of the line can be controlled with the following properties:

| Name | Description |
| --- | --- |
| `backgroundColor` | The line fill color. |
| `borderCapStyle` | Cap style of the line. See MDN. |
| `borderColor` | The line color. |
| `borderDash` | Length and spacing of dashes. See MDN. |
| `borderDashOffset` | Offset for line dashes. See MDN. |
| `borderJoinStyle` | Line joint style. See MDN. |
| `borderWidth` | The line width (in pixels). |
| `clip` | How to clip relative to chartArea. Positive value allows overflow, negative value clips that many pixels inside chartArea. `0` = clip at chartArea. Clipping can also be configured per side: `clip: {left: 5, top: false, right: -2, bottom: 0}` |
| `fill` | How to fill the area under the line. See area charts. |
| `lineTension` | Bezier curve tension of the line. Set to 0 to draw straightlines. This option is ignored if monotone cubic interpolation is used. |
| `showLine` | If false, the line is not drawn for this dataset. |
| `spanGaps` | If true, lines will be drawn between points with no or null data. If false, points with `NaN` data will create a break in the line. |

If the value is `undefined`, `showLine` and `spanGaps` fallback to the associated chart configuration options. The rest of the values fallback to the associated `elements.line.*` options.

### Interactions

The interaction with each point can be controlled with the following properties:

| Name | Description |
| --- | --- |
| `pointHoverBackgroundColor` | Point background color when hovered. |
| `pointHoverBorderColor` | Point border color when hovered. |
| `pointHoverBorderWidth` | Border width of point when hovered. |
| `pointHoverRadius` | The radius of the point when hovered. |

### cubicInterpolationMode

The following interpolation modes are supported.

* `'default'`
* `'monotone'`

The `'default'` algorithm uses a custom weighted cubic interpolation, which produces pleasant curves for all types of datasets.

The `'monotone'` algorithm is more suited to `y = f(x)` datasets : it preserves monotonicity (or piecewise monotonicity) of the dataset being interpolated, and ensures local extremums (if any) stay at input data points.

If left untouched ( `undefined`), the global `options.elements.line.cubicInterpolationMode` property is used.

### Stepped Line

The following values are supported for `steppedLine`.

* `false`: No Step Interpolation (default)
* `true`: Step-before Interpolation (eq. `'before'`)
* `'before'`: Step-before Interpolation
* `'after'`: Step-after Interpolation
* `'middle'`: Step-middle Interpolation

If the `steppedLine` value is set to anything other than false, `lineTension` will be ignored.

### Configuration Options

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `showLines` | `boolean` | `true` | If false, the lines between points are not drawn. |
| `spanGaps` | `boolean` | `false` | If false, NaN data causes a break in the line. |

### Data Structure

The `data` property of a dataset for a line chart can be passed in two formats.

### number[]

```
	data: [20, 10]
```

When the `data` array is an array of numbers, the x axis is generally a category. The points are placed onto the axis using their position in the array. When a line chart is created with a category axis, the `labels` property of the data object must be specified.

### Point[]

```
	data: [{
		x: 10,
		y: 20
	}, {
		x: 15,
		y: 10
	}]
```

This alternate is used for sparse datasets, such as those in scatter charts. Each data point is specified using an object containing `x` and `y` properties.

### Stacked Area Chart

Line charts can be configured into stacked area charts by changing the settings on the y axis to enable stacking. Stacked area charts can be used to show how one data trend is made up of a number of smaller pieces.

```
	var chart = FLUIGC.chart('#MY_SELECTOR', {
		id: 'set_an_id_for_my_chart',
		width: '700',
		height: '200'
	});
	var lineChart = chart.line(data, {
		scales: {
			yAxes: [{
				stacked: true
			}]
		}
	});
```

### Methods.addData(valuesArray, label)

Adds a new data to chart.

```
	lineChart.addData([40, 60], 'August');
```

#### .update()

Update the dataset's value.

```
	// Would update the first dataset's value of 'March' to be 50
	lineChart.data.datasets[0].data[2] = 50;
	// Calling update now animates the position of March from 90 to 50.
	lineChart.update();
```

#### .removeData()

Remove the first value for all datasets on the chart.

```
	lineChart.removeData();
```

## Events

| Name | Description |
| --- | --- |
| fluig.chart.click | Triggered when the click ocurrs on a line chart area. |

### Events triggered by element selector

#### fluig.chart.click

This event is fired when the click ocurrs on a line chart area. The returned object has the label attributes and the value of the chart area.

```
	$('YOUR_SELECTOR').on('fluig.chart.click', function(data) {
		// Do something
	});
```

# Chart Bar

## Examples

A bar chart is a way of showing data as bars

### Live demo

Below an example of bar chart

Add
Update
Remove

### HTML

```
<div id="MY_SELECTOR"></div>
```

### Javascript

Below is the basic configuration to use the bar chart.

```
var chart = FLUIGC.chart('#MY_SELECTOR');
// call the bar function
var barChart = chart.bar(data, options);
```

### Javascript

Below is the configuration, with the id, width and height of the canvas.

```
var chart = FLUIGC.chart('#MY_SELECTOR', {
	id: 'set_an_id_for_my_chart',
	width: '700',
	height: '200',
	/* See the list of options */
});
// call the bar function
var barChart = chart.bar(data, options);
```

### Data structure

The bar chart has the a very similar data structure to the line chart, and has an array of datasets,
each with colours and an array of data.

```
var data = {
    labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
    datasets: [
        {
            label: 'My First dataset',
            data: [65, 59, 80, 81, 56, 55, 40],
            backgroundColor: 'rgba(170, 194, 77, 0.5)',
            hoverBackgroundColor: 'rgba(170, 194, 77, 0.5)',
            borderColor: '#b0cc49',
            hoverBorderColor: '#b0cc49'
        },
        {
            label: 'My Second dataset',
            data: [28, 48, 40, 19, 86, 27, 90],
            backgroundColor: 'rgba(190, 49, 88, 0.5)',
            hoverBackgroundColor: 'rgba(190, 49, 88, 0.5)',
            borderColor: '#ed145b',
            hoverBorderColor: '#ed145b'
        }
    ]
};
```

A bar chart provides a way of showing data values represented as vertical bars. It is sometimes used to show trend data, and the comparison of multiple data sets side by side.

### Dataset Properties

The bar chart allows a number of properties to be specified for each dataset. These are used to set display properties for a specific dataset. For example, the color of the bars is generally set this way.

| Name | Type | Scriptable | Indexable | Default |
| --- | --- | --- | --- | --- |
| `backgroundColor` | `Color` | Yes | Yes | `'rgba(0, 0, 0, 0.1)'` |
| `borderColor` | `Color` | Yes | Yes | `'rgba(0, 0, 0, 0.1)'` |
| `borderSkipped` | `string` | Yes | Yes | `'bottom'` |
| `borderWidth` | `number|object` | Yes | Yes | `0` |
| `data` | `object[]` | - | - | **required** |
| `hoverBackgroundColor` | `Color` | - | Yes | `undefined` |
| `hoverBorderColor` | `Color` | - | Yes | `undefined` |
| `hoverBorderWidth` | `number` | - | Yes | `1` |
| `label` | `string` | - | - | `''` |
| `order` | `number` | - | - | `0` |
| `xAxisID` | `string` | - | - | first x axis |
| `yAxisID` | `string` | - | - | first y axis |

### General

| Name | Description |
| --- | --- |
| `label` | The label for the dataset which appears in the legend and tooltips. |
| `order` | The drawing order of dataset. Also affects order for stacking, tooltip, and legend. |
| `xAxisID` | The ID of the x axis to plot this dataset on. |
| `yAxisID` | The ID of the y axis to plot this dataset on. |

### Styling

The style of each bar can be controlled with the following properties:

| Name | Description |
| --- | --- |
| `backgroundColor` | The bar background color. |
| `borderColor` | The bar border color. |
| `borderSkipped` | The edge to skip when drawing bar. |
| `borderWidth` | The bar border width (in pixels). |

All these values, if `undefined`, fallback to the associated `elements.rectangle.*` options.

#### borderSkipped

This setting is used to avoid drawing the bar stroke at the base of the fill. In general, this does not need to be changed except when creating chart types that derive from a bar chart.

**Note:** for negative bars in vertical chart, `top` and `bottom` are flipped. Same goes for `left` and `right` in horizontal chart.

Options are:

* `'bottom'`
* `'left'`
* `'top'`
* `'right'`
* `false`

#### borderWidth

If this value is a number, it is applied to all sides of the rectangle (left, top, right, bottom), except `borderSkipped`. If this value is an object, the `left` property defines the left border width. Similarly the `right`, `top` and `bottom` properties can also be specified. Omitted borders and `borderSkipped` are skipped.

### Interactions

The interaction with each bar can be controlled with the following properties:

| Name | Description |
| --- | --- |
| `hoverBackgroundColor` | The bar background color when hovered. |
| `hoverBorderColor` | The bar border color when hovered. |
| `hoverBorderWidth` | The bar border width when hovered (in pixels). |

All these values, if `undefined`, fallback to the associated `elements.rectangle.*` options.

### Dataset Configuration

The bar chart accepts the following configuration from the associated dataset options:

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `barPercentage` | `number` | `0.9` | Percent (0-1) of the available width each bar should be within the category width. 1.0 will take the whole category width and put the bars right next to each other. more... |
| `categoryPercentage` | `number` | `0.8` | Percent (0-1) of the available width each category should be within the sample width. more... |
| `barThickness` | `number|string` |  | Manually set width of each bar in pixels. If set to `'flex'`, it computes "optimal" sample widths that globally arrange bars side by side. If not set (default), bars are equally sized based on the smallest interval. more... |
| `maxBarThickness` | `number` |  | Set this to ensure that bars are not sized thicker than this. |
| `minBarLength` | `number` |  | Set this to ensure that bars have a minimum length in pixels. |

### Example Usage

```
		data: {
			datasets: [{
				barPercentage: 0.5,
				barThickness: 6,
				maxBarThickness: 8,
				minBarLength: 2,
				data: [10, 20, 30, 40, 50, 60, 70]
			}]
		};
```

### barThickness

If this value is a number, it is applied to the width of each bar, in pixels. When this is enforced, `barPercentage` and `categoryPercentage` are ignored.

If set to `'flex'`, the base sample widths are calculated automatically based on the previous and following samples so that they take the full available widths without overlap. Then, bars are sized using `barPercentage` and `categoryPercentage`. There is no gap when the percentage options are 1. This mode generates bars with different widths when data are not evenly spaced.

If not set (default), the base sample widths are calculated using the smallest interval that prevents bar overlapping, and bars are sized using `barPercentage` and `categoryPercentage`. This mode always generates bars equally sized.

### Scale Configuration

The bar chart sets unique default values for the following configuration from the associated `scale` options:

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `offset` | `boolean` | `true` | If true, extra space is added to the both edges and the axis is scaled to fit into the chart area. |
| `gridLines.offsetGridLines` | `boolean` | `true` | If true, the bars for a particular data point fall between the grid lines. The grid line will move to the left by one half of the tick interval. If false, the grid line will go right down the middle of the bars. more... |

### Example Usage

```
		options = {
			scales: {
				xAxes: [{
					gridLines: {
						offsetGridLines: true
					}
				}]
			}
		};
```

### offsetGridLines

If true, the bars for a particular data point fall between the grid lines. The grid line will move to the left by one half of the tick interval, which is the space between the grid lines. If false, the grid line will go right down the middle of the bars. This is set to true for a category scale in a bar chart while false for other scales or chart types by default.

### barPercentage vs categoryPercentage

The following shows the relationship between the bar percentage option and the category percentage option.

```
		// categoryPercentage: 1.0
		// barPercentage: 1.0
		Bar:        | 1.0 | 1.0 |
		Category:   |    1.0    |
		Sample:     |===========|

		// categoryPercentage: 1.0
		// barPercentage: 0.5
		Bar:          |.5|  |.5|
		Category:  |      1.0     |
		Sample:    |==============|

		// categoryPercentage: 0.5
		// barPercentage: 1.0
		Bar:            |1.||1.|
		Category:       |  .5  |
		Sample:     |==============|
```

### Data Structure

The `data` property of a dataset for a bar chart is specified as an array of numbers. Each point in the data array corresponds to the label at the same index on the x axis.

```
		data: [20, 10]
```

You can also specify the dataset as x/y coordinates when using the time scale.

```
		data: [{x:'2016-12-25', y:20}, {x:'2016-12-26', y:10}]
```

You can also specify the dataset for a bar chart as arrays of two numbers. This will force rendering of bars with gaps between them (floating-bars). First and second numbers in array will correspond the start and the end point of a bar respectively.

```
		data: [[5,6], [-3,-6]]
```

### Stacked Bar Chart

Bar charts can be configured into stacked bar charts by changing the settings on the X and Y axes to enable stacking. Stacked bar charts can be used to show how one data series is made up of a number of smaller pieces.

```
		var chart = FLUIGC.chart('#MY_SELECTOR', {
			id: 'set_an_id_for_my_chart',
			width: '700',
			height: '200'
		});
		var lineChart = chart.bar(data, {
			scales: {
				xAxes: [{
					stacked: true
				}],
				yAxes: [{
					stacked: true
				}]
			}
		});
```

The following dataset properties are specific to stacked bar charts.

| Name | Type | Description |
| --- | --- | --- |
| `stack` | `string` | The ID of the group to which this dataset belongs to (when stacked, each group will be a separate stack). |

# Chart Horizontal Bar

A horizontal bar chart is a variation on a vertical bar chart. It is sometimes used to show trend data, and the comparison of multiple data sets side by side.

Add
Update
Remove

### Example

### HTML

```
	<div id="MY_SELECTOR"></div>
```

### Javascript

Below is the basic configuration to use the horizontal bar chart.

```
	var chart = FLUIGC.chart('#MY_SELECTOR');
	// call the horizontal bar function
	var barChart = chart.horizontalBar(data, options);
```

### Javascript

Below is the configuration, with the id, width and height of the canvas.

```
	var chart = FLUIGC.chart('#MY_SELECTOR', {
		id: 'set_an_id_for_my_chart',
		width: '700',
		height: '200',
		/* See the list of options */
	});
	// call the horizontal bar function
	var horizontalBarChart = chart.horizontalBar(data, options);
```

### Config Options

The configuration options for the horizontal bar chart are the same as for the bar chart. However, any options specified on the x axis in a bar chart, are applied to the y axis in a horizontal bar chart.

### Methods.addData(valuesArray, label)

Adds a new data to chart.

```
	horizontalBarChart.addData([40, 60], 'August');
```

#### .update()

Update the dataset's value.

```
	// Would update the first dataset's value of 'March' to be 50
	horizontalBarChart.data.datasets[0].data[2] = 50;
	// Calling update now animates the position of March from 90 to 50.
	horizontalBarChart.update();
```

#### .removeData()

Remove the first value for all datasets on the chart.

```
	horizontalBarChart.removeData();
```

## Events

| Name | Description |
| --- | --- |
| fluig.chart.click | Triggered when the click ocurrs on a bar chart area. |

### Events triggered by element selector

#### fluig.chart.click

This event is fired when the click ocurrs on a bar chart area. The returned object has the label attributes and the value of the chart area.

```
	$('YOUR_SELECTOR').on('fluig.chart.click', function(data) {
		// Do something
	});
```

# Chart Radar

## Examples

A radar chart is a way of showing multiple data points and the variation between them.

### Live demo

Below an example of radar chart

Add
Update
Remove

### HTML

```
<div id="MY_SELECTOR"></div>
```

### Javascript

Below is the basic configuration to use the radar chart.

```
var chart = FLUIGC.chart('#MY_SELECTOR');
// call the radar function
var radarChart = chart.radar(data, options);
```

### Javascript

Below is the configuration, with the id, width and height of the canvas.

```
var chart = FLUIGC.chart('#MY_SELECTOR', {
	id: 'set_an_id_for_my_chart',
	width: '700',
	height: '200',
	/* See the list of options */
});
// call the radar function
var radarChart = chart.radar(data, options);
```

### Data structure

For a radar chart, to provide context of what each point means, we include an array of strings
that show around each point in the chart. For the radar chart data, we have an array of datasets.
Each of these is an object, with a fill colour, a stroke colour, a colour for the fill of each point,
and a colour for the stroke of each point. We also have an array of data values.

```
var data = {
    labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
    datasets: [
        {
            label: 'My First dataset',
            data: [65, 59, 80, 81, 56, 55, 40],
            backgroundColor: 'rgba(170, 194, 77, 0.5)',
            hoverBackgroundColor: 'rgba(170, 194, 77, 0.5)',
            borderColor: '#b0cc49',
            hoverBorderColor: '#b0cc49'
        },
        {
            label: 'My Second dataset',
            data: [28, 48, 40, 19, 86, 27, 90],
            backgroundColor: 'rgba(190, 49, 88, 0.5)',
            hoverBackgroundColor: 'rgba(190, 49, 88, 0.5)',
            borderColor: '#ed145b',
            hoverBorderColor: '#ed145b'
        }
    ]
};
```

### Dataset Properties

The radar chart allows a number of properties to be specified for each dataset. These are used to set display properties for a specific dataset. For example, the colour of a line is generally set this way.

| Name | Type | Scriptable | Indexable | Default |
| --- | --- | --- | --- | --- |
| `backgroundColor` | `Color` | Yes | - | `'rgba(0, 0, 0, 0.1)'` |
| `borderCapStyle` | `string` | Yes | - | `'butt'` |
| `borderColor` | `Color` | Yes | - | `'rgba(0, 0, 0, 0.1)'` |
| `borderDash` | `number[]` | Yes | - | `[]` |
| `borderDashOffset` | `number` | Yes | - | `0.0` |
| `borderJoinStyle` | `string` | Yes | - | `'miter'` |
| `borderWidth` | `number` | Yes | - | `3` |
| `hoverBackgroundColor` | `Color` | Yes | - | `undefined` |
| `hoverBorderCapStyle` | `string` | Yes | - | `undefined` |
| `hoverBorderColor` | `Color` | Yes | - | `undefined` |
| `hoverBorderDash` | `number[]` | Yes | - | `undefined` |
| `hoverBorderDashOffset` | `number` | Yes | - | `undefined` |
| `hoverBorderJoinStyle` | `string` | Yes | - | `undefined` |
| `hoverBorderWidth` | `number` | Yes | - | `undefined` |
| `fill` | `boolean|string` | Yes | - | `true` |
| `label` | `string` | - | - | `''` |
| `order` | `number` | - | - | `0` |
| `lineTension` | `number` | - | - | `0` |
| `pointBackgroundColor` | `Color` | Yes | Yes | `'rgba(0, 0, 0, 0.1)'` |
| `pointBorderColor` | `Color` | Yes | Yes | `'rgba(0, 0, 0, 0.1)'` |
| `pointBorderWidth` | `number` | Yes | Yes | `1` |
| `pointHitRadius` | `number` | Yes | Yes | `1` |
| `pointHoverBackgroundColor` | `Color` | Yes | Yes | `undefined` |
| `pointHoverBorderColor` | `Color` | Yes | Yes | `undefined` |
| `pointHoverBorderWidth` | `number` | Yes | Yes | `1` |
| `pointHoverRadius` | `number` | Yes | Yes | `4` |
| `pointRadius` | `number` | Yes | Yes | `3` |
| `pointRotation` | `number` | Yes | Yes | `0` |
| `pointStyle` | `string|Image` | Yes | Yes | `'circle'` |
| `spanGaps` | `boolean` | - | - | `undefined` |

### General

| Name | Description |
| --- | --- |
| `label` | The label for the dataset which appears in the legend and tooltips. |
| `order` | The drawing order of dataset. |

### Point Styling

The style of each point can be controlled with the following properties:

| Name | Description |
| --- | --- |
| `pointBackgroundColor` | The fill color for points. |
| `pointBorderColor` | The border color for points. |
| `pointBorderWidth` | The width of the point border in pixels. |
| `pointHitRadius` | The pixel size of the non-displayed point that reacts to mouse events. |
| `pointRadius` | The radius of the point shape. If set to 0, the point is not rendered. |
| `pointRotation` | The rotation of the point in degrees. |
| `pointStyle` | Style of the point. more... |

All these values, if `undefined`, fallback first to the dataset options then to the associated `elements.point.*` options.

### Line Styling

The style of the line can be controlled with the following properties:

| Name | Description |
| --- | --- |
| `backgroundColor` | The line fill color. |
| `borderCapStyle` | Cap style of the line. See MDN. |
| `borderColor` | The line color. |
| `borderDash` | Length and spacing of dashes. See MDN. |
| `borderDashOffset` | Offset for line dashes. See MDN. |
| `borderJoinStyle` | Line joint style. See MDN. |
| `borderWidth` | The line width (in pixels). |
| `fill` | How to fill the area under the line. See area charts. |
| `lineTension` | Bezier curve tension of the line. Set to 0 to draw straightlines. |
| `spanGaps` | If true, lines will be drawn between points with no or null data. If false, points with `NaN` data will create a break in the line. |

If the value is `undefined`, `spanGaps` fallback to the associated chart configuration options. The rest of the values fallback to the associated `elements.line.*` options.

### Interactions

The interaction with each point can be controlled with the following properties:

| Name | Description |
| --- | --- |
| `pointHoverBackgroundColor` | Point background color when hovered. |
| `pointHoverBorderColor` | Point border color when hovered. |
| `pointHoverBorderWidth` | Border width of point when hovered. |
| `pointHoverRadius` | The radius of the point when hovered. |

### Configuration Options

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `spanGaps` | `boolean` | `false` | If false, NaN data causes a break in the line. |

### Scale Options

The radar chart supports only a single scale. The options for this scale are defined in the `scale` property. The options for this scale are defined in the `scale` property, which can be referenced from the Linear Radial Axis page.

```
		options = {
			scale: {
				angleLines: {
					display: false
				},
				ticks: {
					suggestedMin: 50,
					suggestedMax: 100
				}
			}
		};
```

### Data Structure

The `data` property of a dataset for a radar chart is specified as an array of numbers. Each point in the data array corresponds to the label at the same index.

```
		data: [20, 10]
```

For a radar chart, to provide context of what each point means, we include an array of strings that show around each point in the chart.

```
		data: {
			labels: ['Running', 'Swimming', 'Eating', 'Cycling'],
			datasets: [{
				data: [20, 10, 4, 2]
			}]
		}
```

### Methods.addData(valuesArray, label)

Adds a new data to chart.

```
	radarChart.addData([40, 60], 'Working');
```

#### .update()

Update the dataset's value.

```
	// Would update the first dataset's value of 'March' to be 50
	radarChart.data.datasets[0].data[2] = 50;
	// Calling update now animates the position of March from 90 to 50.
	radarChart.update();
```

#### .removeData()

Remove the first value for all datasets on the chart.

```
	radarChart.removeData();
```

## Events

| Name | Description |
| --- | --- |
| fluig.chart.click | Triggered when the click ocurrs on a radar chart area. |

### Events triggered by element selector

#### fluig.chart.click

This event is fired when the click ocurrs on a radar chart area. The returned object has the label attributes and the value of the chart area.

```
	$('YOUR_SELECTOR').on('fluig.chart.click', function(data) {
		// Do something
	});
```

# Chart Polar

## Examples

Polar area charts are similar to pie charts, but each segment has the same
angle - the radius of the segment differs depending on the value.

### Live demo

Below an example of polar chart

Add
Update
Remove

### HTML

```
<div id="MY_SELECTOR"></div>
```

### Javascript

Below is the basic configuration to use the polar chart.

```
var chart = FLUIGC.chart('#MY_SELECTOR');
// call the polar function
var polarChart = chart.polar(data, options);
```

### Javascript

Below is the configuration, with the id, width and height of the canvas.

```
var chart = FLUIGC.chart('#MY_SELECTOR', {
	id: 'set_an_id_for_my_chart',
	width: '700',
	height: '200',
	/* See the list of options */
});
// call the polar function
var polarChart = chart.polar(data, options);
```

### Data structure

The chart data you pass in an array of objects, with a value and a colour.

```
var data = {
    labels: ['bpm', 'ecm', 'social', 'mall', 'wcm'],
    datasets: [
        {
            label: 'My First Dataset',
            data: [300, 50, 100, 40, 120],
            backgroundColor: ['#b0cc49', '#ed145b', '#c67926', '#d3a82f', '#303030'],
            hoverBackgroundColor: ['#b0cc49', '#ed145b', '#c67926', '#d3a82f', '#303030'],
            borderColor: ['rgba(170, 194, 77, 0.5)', 'rgba(190, 49, 88, 0.5)', 'rgba(198, 121, 38, 0.5)', 'rgba(211, 168, 47, 0.5)', 'rgba(43, 43, 42, 0.5)'],
            hoverBorderColor: ['rgba(170, 194, 77, 0.5)', 'rgba(190, 49, 88, 0.5)', 'rgba(198, 121, 38, 0.5)', 'rgba(211, 168, 47, 0.5)', 'rgba(43, 43, 42, 0.5)']
        }
    ]
};
```

### Dataset Properties

The following options can be included in a polar area chart dataset to configure options for that specific dataset.

| Name | Type | Scriptable | Indexable | Default |
| --- | --- | --- | --- | --- |
| `backgroundColor` | `Color` | Yes | Yes | `'rgba(0, 0, 0, 0.1)'` |
| `borderAlign` | `string` | Yes | Yes | `'center'` |
| `borderColor` | `Color` | Yes | Yes | `'#fff'` |
| `borderWidth` | `number` | Yes | Yes | `2` |
| `data` | `number[]` | - | - | **required** |
| `hoverBackgroundColor` | `Color` | Yes | Yes | `undefined` |
| `hoverBorderColor` | `Color` | Yes | Yes | `undefined` |
| `hoverBorderWidth` | `number` | Yes | Yes | `undefined` |

### Styling

The style of each arc can be controlled with the following properties:

| Name | Description |
| --- | --- |
| `backgroundColor` | arc background color. |
| `borderColor` | arc border color. |
| `borderWidth` | arc border width (in pixels). |

All these values, if `undefined`, fallback to the associated `elements.arc.*` options.

### Border Alignment

The following values are supported for `borderAlign`.

* `'center'` (default)
* `'inner'`

When `'center'` is set, the borders of arcs next to each other will overlap. When `'inner'` is set, it is guaranteed that all the borders are not overlap.

### Interactions

The interaction with each arc can be controlled with the following properties:

| Name | Description |
| --- | --- |
| `hoverBackgroundColor` | arc background color when hovered. |
| `hoverBorderColor` | arc border color when hovered. |
| `hoverBorderWidth` | arc border width when hovered (in pixels). |

All these values, if `undefined`, fallback to the associated `elements.arc.*` options.

### Config Options

These are the customisation options specific to Polar Area charts. These options are merged with the global chart default options, and form the options of the chart.

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `startAngle` | `number` | `-0.5 * Math.PI` | Starting angle to draw arcs for the first item in a dataset. |
| `animation.animateRotate` | `boolean` | `true` | If true, the chart will animate in with a rotation animation. This property is in the `options.animation` object. |
| `animation.animateScale` | `boolean` | `true` | If true, will animate scaling the chart from the center outwards. |

### Data Structure

For a polar area chart, datasets need to contain an array of data points. The data points should be a number, Chart.js will total all of the numbers and calculate the relative proportion of each.

You also need to specify an array of labels so that tooltips appear correctly for each slice.

```
		data = {
			datasets: [{
				data: [10, 20, 30]
			}],

			// These labels appear in the legend and in the tooltips when hovering different arcs
			labels: [
				'Red',
				'Yellow',
				'Blue'
			]
		};
```

### Methods.addData(valuesArray, label)

Adds a new data to chart.

```
	polarChart.addData([40], 'Purple');
```

#### .update()

Update the dataset's value.

```
	polarChart.data.datasets[0].data[3] = 50;
	polarChart.update();
```

#### .removeData()

Remove the first value for all datasets on the chart.

```
	polarChart.removeData();
```

## Events

| Name | Description |
| --- | --- |
| fluig.chart.click | Triggered when the click ocurrs on a polar chart area. |

### Events triggered by element selector

#### fluig.chart.click

This event is fired when the click ocurrs on a polar chart area. The returned object has the label attributes and the value of the chart area.

```
	$('YOUR_SELECTOR').on('fluig.chart.click', function(data) {
		// Do something
	});
```

# Chart Doughnut and Pie

Pie and doughnut charts are probably the most commonly used charts. They are divided into segments, the arc of each segment shows the proportional value of each piece of data.

They are excellent at showing the relational proportions between data.

Pie and doughnut charts are effectively the same class in Chart.js, but have one different default value - their `cutoutPercentage`. This equates what percentage of the inner should be cut out. This defaults to `0` for pie charts, and `50` for doughnuts.

They are also registered under two aliases in the `Chart` core. Other than their different default value, and different alias, they are exactly the same.

## Doughnut examples

Doughnut chart is divided into segments, the arc of each segment shows the proportional value of each piece of data.

### Live demo

Below an example of doughnut chart

Add
Update
Remove

### HTML

```
<div id="MY_SELECTOR"></div>
```

### Javascript

Below is the basic configuration to use the doughnut chart.

```
var chart = FLUIGC.chart('#MY_SELECTOR');
// call the doughnut function
var doughnutChart = chart.doughnut(data, options);
```

### Javascript

Below is the configuration, with the id, width and height of the canvas.

```
var chart = FLUIGC.chart('#MY_SELECTOR', {
	id: 'set_an_id_for_my_chart',
	width: '700',
	height: '200',
	/* See the list of options */
});
// call the doughnut function
var doughnutChart = chart.doughnut(data, options);
```

### Data structure

For a doughnut chart, you must pass in an array of objects with a value and a color property.

```
var data = {
    labels: ['bpm', 'ecm', 'social', 'mall', 'wcm'],
    datasets: [
        {
            label: 'My First Dataset',
            data: [300, 50, 100, 40, 120],
            backgroundColor: ['#b0cc49', '#ed145b', '#c67926', '#d3a82f', '#303030'],
            hoverBackgroundColor: ['#b0cc49', '#ed145b', '#c67926', '#d3a82f', '#303030'],
            borderColor: ['rgba(170, 194, 77, 0.5)', 'rgba(190, 49, 88, 0.5)', 'rgba(198, 121, 38, 0.5)', 'rgba(211, 168, 47, 0.5)', 'rgba(43, 43, 42, 0.5)'],
            hoverBorderColor: ['rgba(170, 194, 77, 0.5)', 'rgba(190, 49, 88, 0.5)', 'rgba(198, 121, 38, 0.5)', 'rgba(211, 168, 47, 0.5)', 'rgba(43, 43, 42, 0.5)']
        }
    ]
};
```



## Pie example

Pie chart is divided into segments, the arc of each segment shows the proportional value of each piece of data.

### Live demo

Below an example of pie chart

Add
Update
Remove

### HTML

```
<div id="MY_SELECTOR"></div>
```

### Javascript

Below is the basic configuration to use the pie chart.

```
var chart = FLUIGC.chart('#MY_SELECTOR');
// call the pie function
var pieChart = chart.pie(data, options);
```

### Javascript

Below is the configuration, with the id, width and height of the canvas.

```
var chart = FLUIGC.chart('#MY_SELECTOR', {
	id: 'set_an_id_for_my_chart',
	width: '700',
	height: '200',
	/* See the list of options */
});
// call the pie function
var pieChart = chart.pie(data, options);
```

### Data structure

For a pie chart, you must pass in an array of objects with a value and a color property.

```
var data = {
	labels: ['bpm', 'ecm', 'social', 'mall', 'wcm'],
	datasets: [
		{
			label: 'My First Dataset',
			data: [300, 50, 100, 40, 120],
			backgroundColor: ['#b0cc49', '#ed145b', '#c67926', '#d3a82f', '#303030'],
			hoverBackgroundColor: ['#b0cc49', '#ed145b', '#c67926', '#d3a82f', '#303030'],
			borderColor: ['rgba(170, 194, 77, 0.5)', 'rgba(190, 49, 88, 0.5)', 'rgba(198, 121, 38, 0.5)', 'rgba(211, 168, 47, 0.5)', 'rgba(43, 43, 42, 0.5)'],
			hoverBorderColor: ['rgba(170, 194, 77, 0.5)', 'rgba(190, 49, 88, 0.5)', 'rgba(198, 121, 38, 0.5)', 'rgba(211, 168, 47, 0.5)', 'rgba(43, 43, 42, 0.5)']
		}
	]
};
```

### Dataset Properties

The doughnut/pie chart allows a number of properties to be specified for each dataset. These are used to set display properties for a specific dataset. For example, the colours of the dataset's arcs are generally set this way.

| Name | Type | Scriptable | Indexable | Default |
| --- | --- | --- | --- | --- |
| `backgroundColor` | `Color` | Yes | Yes | `'rgba(0, 0, 0, 0.1)'` |
| `borderAlign` | `string` | Yes | Yes | `'center'` |
| `borderColor` | `Color` | Yes | Yes | `'#fff'` |
| `borderWidth` | `number` | Yes | Yes | `2` |
| `data` | `number[]` | - | - | **required** |
| `hoverBackgroundColor` | `Color` | Yes | Yes | `undefined` |
| `hoverBorderColor` | `Color` | Yes | Yes | `undefined` |
| `hoverBorderWidth` | `number` | Yes | Yes | `undefined` |
| `weight` | `number` | - | - | `1` |

### Styling

The style of each arc can be controlled with the following properties:

| Name | Description |
| --- | --- |
| `backgroundColor` | arc background color. |
| `borderColor` | arc border color. |
| `borderWidth` | arc border width (in pixels). |
| `weight` | The relative thickness of the dataset. Providing a value for weight will cause the pie or doughnut dataset to be drawn with a thickness relative to the sum of all the dataset weight values. |

All these values, if `undefined`, fallback to the associated `elements.arc.*` options.

### Border Alignment

The following values are supported for `borderAlign`.

* `'center'` (default)
* `'inner'`

When `'center'` is set, the borders of arcs next to each other will overlap. When `'inner'` is set, it is guaranteed that all borders will not overlap.

### Interactions

The interaction with each arc can be controlled with the following properties:

| Name | Description |
| --- | --- |
| `hoverBackgroundColor` | arc background color when hovered. |
| `hoverBorderColor` | arc border color when hovered. |
| `hoverBorderWidth` | arc border width when hovered (in pixels). |

All these values, if `undefined`, fallback to the associated `elements.arc.*` options.

### Config Options

These are the customisation options specific to Pie & Doughnut charts. These options are merged with the global chart configuration options, and form the options of the chart.

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `cutoutPercentage` | `number` | `50` - for doughnut, `0` - for pie | The percentage of the chart that is cut out of the middle. |
| `rotation` | `number` | `-0.5 * Math.PI` | Starting angle to draw arcs from. |
| `circumference` | `number` | `2 * Math.PI` | Sweep to allow arcs to cover. |
| `animation.animateRotate` | `boolean` | `true` | If true, the chart will animate in with a rotation animation. This property is in the `options.animation` object. |
| `animation.animateScale` | `boolean` | `false` | If true, will animate scaling the chart from the center outwards. |

### Default Options

We can also change these default values for each Doughnut type that is created, this object is available at `Chart.defaults.doughnut`. Pie charts also have a clone of these defaults available to change at `Chart.defaults.pie`, with the only difference being `cutoutPercentage` being set to 0.

### Data Structure

For a pie chart, datasets need to contain an array of data points. The data points should be a number, Chart.js will total all of the numbers and calculate the relative proportion of each.

You also need to specify an array of labels so that tooltips appear correctly.

```
data = {
    datasets: [{
        data: [10, 20, 30]
    }],

    // These labels appear in the legend and in the tooltips when hovering different arcs
    labels: [
        'Red',
        'Yellow',
        'Blue'
    ]
};
```

### Methods.addData(valuesArray, label)

Adds a new data to chart.

```
	// doughnut
	doughnutChart.addData([40], 'Purple');
	
	// pie
	pieChart.addData([40], 'Purple');
```

#### .update()

Update the dataset's value.

```
	// doughnut
	doughnutChart.data.datasets[0].data[3] = 50;
	doughnutChart.update();

	// pie
	pieChart.data.datasets[0].data[3] = 50;
	pieChart.update();
```

#### .removeData()

Remove the first value for all datasets on the chart.

```
	// doughnut
	doughnutChart.removeData();

	// pie
	pieChart.removeData();
```

## Events

| Name | Description |
| --- | --- |
| fluig.chart.click | Triggered when the click ocurrs on a doughnut/pie chart area. |

### Events triggered by element selector

#### fluig.chart.click

This event is fired when the click ocurrs on a doughnut/pie chart area. The returned object has the label attributes and the value of the chart area.

```
	$('YOUR_SELECTOR').on('fluig.chart.click', function(data) {
		// Do something
	});
```

# Chart Gauge

## Examples

Allows the creation of a chart style of a manometer

### Live demo

Below an example of gauge chart

Set to 10
Set to 2500

### HTML

```
<div id="MY_SELECTOR"></div>
```

### Javascript

Below is the basic configuration to use the gauge chart.

```
var chart = FLUIGC.chart('#MY_SELECTOR');
// call the gauge function
var chartGauge = chart.gauge();
```

### Javascript

Below is the configuration, with the id, width and height of the canvas.

```
var chart = FLUIGC.chart('#MY_SELECTOR', {
	id: 'set_an_id_for_my_chart',
	width: '700',
	height: '200'
});
// call the gauge function
var chartGauge = chart.gauge({
	lines: 12,
	angle: 0.15,
	lineWidth: 0.44,
	pointer: {
		length: 0.9,
		strokeWidth: 0.035,
		color: '#000000'
	},
	limitMax: 'false',
	colorStart: '#6FADCF',
	colorStop: '#8FC0DA',
	borderColor: '#E0E0E0',
	generateGradient: true
});
```

### Gauge Chart options

The options object has the following attributes:

| Name | type | default | description |
| --- | --- | --- | --- |
| lines | number | 12 | The number of lines to draw |
| angle | number | 0.15 | The length of each line |
| lineWidth | number | 0.44 | The line thickness |
| pointer | object | '' | Settings pointer |
| limitMax | string | 'false' | If true, the pointer will not go past the end of the gauge |
| colorStart | string | '#faa61a' | Colors |
| colorStop | string | '#ed145b' | Colors |
| borderColor | string | '#ed145b' | To see which ones work best for you |
| generateGradient | boolean | true | Generate Gradient |

### Settings to Object pointer

The options object has the following attributes:

| Name | type | default | description |
| --- | --- | --- | --- |
| length | number | 0.9 | The radius of the inner circle |
| strokeWidth | number | 0.035 | The rotation offset |
| color | string | '#000000' | Fill color |

### You can change the following attributesmaxValue

Set max gauge value.

```
	gaugeChart.maxValue = 3000;	
```

#### animationSpeed

Set animation speed (32 is default value).

```
	gaugeChart.animationSpeed = 74;	
```

### Methods.set(newValue)

Set actual value.

```
	gaugeChart.set(925);
```

# Chart Donut

## Examples

Allows the creation of a chart style of a donut

### Live demo

Below an example of donut chart

Set to 10
Set to 2500

### HTML

```
<div id="MY_SELECTOR"></div>
```

### Javascript

Below is the basic configuration to use the donut chart.

```
var chart = FLUIGC.chart('#MY_SELECTOR');
// call the donut function
var chartDonut = chart.donut();
```

### Javascript

Below is the configuration, with the id, width and height of the canvas.

```
var chart = FLUIGC.chart('#MY_SELECTOR', {
	id: 'set_an_id_for_my_chart',
	width: '700',
	height: '200'
});
// call the donut function
var chartDonut = chart.donut({
	lines: 12,
	angle: 0.15,
	lineWidth: 0.44,
	pointer: {
		length: 0.9,
		strokeWidth: 0.035,
		color: '#000000'
	},
	limitMax: 'false',
	colorStart: '#6FADCF',
	colorStop: '#8FC0DA',
	strokeColor: '#E0E0E0',
	generateGradient: true
});
```

### Donut Chart options

The options object has the following attributes:

| Name | type | default | description |
| --- | --- | --- | --- |
| lines | number | 12 | The number of lines to draw |
| angle | number | 0.15 | The length of each line |
| lineWidth | number | 0.44 | The line thickness |
| pointer | object | '' | Settings pointer |
| limitMax | string | 'false' | If true, the pointer will not go past the end of the donut |
| colorStart | string | '#faa61a' | Colors |
| colorStop | string | '#ed145b' | Colors |
| strokeColor | string | '#303030' | To see which ones work best for you |
| generateGradient | boolean | true | Generate Gradient |

### Settings to Object pointer

The options object has the following attributes:

| Name | type | default | description |
| --- | --- | --- | --- |
| length | number | 0.9 | The radius of the inner circle |
| strokeWidth | number | 0.035 | The rotation offset |
| color | string | '#000000' | Fill color |

### You can change the following attributesmaxValue

Set max gauge value.

```
	donutChart.maxValue = 3000;	
```

#### animationSpeed

Set animation speed (32 is default value).

```
	donutChart.animationSpeed = 74;	
```

### Methods.set(newValue)

Set actual value.

```
	donutChart.set(925);
```

# Chart Mixed

## Examples

A mixed chart is a mix of line chart and bar chart.

### Live demo

Below an example of mixed chart

Add
Update
Remove

### HTML

```
<div id="MY_SELECTOR"></div>
```

### Javascript

Below is the basic configuration to use the line chart.

```
var chart = FLUIGC.chart('#MY_SELECTOR');
// call the mixed function
var mixedChart = chart.mixed(data, options);
```

### Javascript

Below is the configuration, with the id, width and height of the canvas.

```
var chart = FLUIGC.chart('#MY_SELECTOR', {
	id: 'set_an_id_for_my_chart',
	width: '700',
	height: '200',
	/* See the list of options */
});
// call the mixed function
var mixedChart = chart.mixed(data, options);
```

### Data structure

The mixed chart requires an array of labels and an array of datasets.

```
var data = {
    labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
    datasets: [
        {
            label: 'My First dataset',
			type: 'line',
            data: [65, 59, 80, 81, 56, 55, 40],
            backgroundColor: 'rgba(170, 194, 77, 0.5)',
            hoverBackgroundColor: 'rgba(170, 194, 77, 0.5)',
            borderColor: '#b0cc49',
            hoverBorderColor: '#b0cc49'
        },
        {
            label: 'My Second dataset',
			type: 'bar',
            data: [28, 48, 40, 19, 86, 27, 90],
            backgroundColor: 'rgba(190, 49, 88, 0.5)',
            hoverBackgroundColor: 'rgba(190, 49, 88, 0.5)',
            borderColor: '#ed145b',
            hoverBorderColor: '#ed145b'
        }
    ]
};
```

### Drawing order

By default, datasets are drawn so that first one is top-most. This can be altered by specifying `order` option to datasets. `order` defaults to `0`.

```
var data = {
	labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
	datasets: [
		{
			label: 'My First dataset',
			type: 'line',
			data: [65, 59, 80, 81, 56, 55, 40]
			// this dataset is drawn below
			order: 1
		},
		{
			label: 'My Second dataset',
			type: 'bar',
			data: [28, 48, 40, 19, 86, 27, 90],
			// this dataset is drawn on top
			order: 2
		}
	]
};
```

### Mixed Chart options and methods

You can use the same attributes and methods used to line charts and bar.

## Events

| Name | Description |
| --- | --- |
| fluig.chart.click | Triggered when the click ocurrs on a mixed chart area. |

### Events triggered by element selector

#### fluig.chart.click

This event is fired when the click ocurrs on a mixed chart area. The returned object has the label attributes and the value of the chart area.

```
	$('YOUR_SELECTOR').on('fluig.chart.click', function(data) {
		// Do something
	});
```
