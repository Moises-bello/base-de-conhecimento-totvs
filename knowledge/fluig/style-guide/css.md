---
content_hash: b8da2a689f514b709c85f38b3e7372e48fe286f0c825a861fcbc3b530048904d
fetched_at: '2026-06-28T21:44:19.037779+00:00'
product: fluig
source: style-guide
title: TOTVS Fluig Developer
type: documentation
url: https://style.fluig.com/css.html
---

# Themes

## Check color

Use this tool to check which variable should be used instead of a color in hexadecimal or RGB.

**Important**: Works only for neutral colors (grayscale).

Enter the color in Hex or RGB

Search

## CSS Variables

CSS variables to be used in development on Fluig.

### Brand color variables

Brand colors are inverted from Light mode to Dark mode.

**Important**: Brand colors are the foundation for the entire theme structure and can be overridden by Fluig's theme functionality. Therefore, never use the hexadecimal value directly, always use the CSS variable.

| Variable | Description | Light Value | Dark Value |
| --- | --- | --- | --- |
| --fs-color-brand-01-lightest | 01-lightest | #e3eefb | #051f31 |
| --fs-color-brand-01-lighter | 01-lighter | #afd3fa | #004064 |
| --fs-color-brand-01-light | 01-light | #3dadfa | #00659a |
| --fs-color-brand-01-base | 01-base | #0079b8 | #0079b8 |
| --fs-color-brand-01-dark | 01-dark | #00659a | #3dadfa |
| --fs-color-brand-01-darker | 01-darker | #004064 | #afd3fa |
| --fs-color-brand-01-darkest | 01-darkest | #051f31 | #e3eefb |

### Action color variables

Action colors point to brand colors, inheriting their values.

| Variable | Description | Light Value | Dark Value |
| --- | --- | --- | --- |
| --fs-color-action-default | default | var(--fs-color-brand-01-base) | var(--fs-color-brand-01-dark) |
| --fs-color-action-hover | hover | var(--fs-color-brand-01-dark) | var(--fs-color-brand-01-darker) |
| --fs-color-action-pressed | pressed | var(--fs-color-brand-01-darker) | var(--fs-color-brand-01-darkest) |
| --fs-color-action-disabled | disabled | var(--fs-color-neutral-mid-40) | var(--fs-color-neutral-mid-40) |
| --fs-color-action-focus | focus | var(--fs-color-brand-01-darkest) | var(--fs-color-brand-01-darkest) |

### Variables for Neutral Colors

Neutral color variables are important for all contexts. They change values in both Light mode and Dark mode.

| Variable | Description | Light Value | Dark Value |
| --- | --- | --- | --- |
| --fs-color-neutral-light-00 | light-00 | #ffffff | #1c1c1c |
| --fs-color-neutral-light-05 | light-05 | #eeeeee | #202020 |
| --fs-color-neutral-light-10 | light-10 | #d9d9d9 | #2b2b2b |
| --fs-color-neutral-light-20 | light-20 | #c1c1c1 | #3b3b3b |
| --fs-color-neutral-light-30 | light-30 | #a1a1a1 | #5a5a5a |
| --fs-color-neutral-mid-40 | mid-40 | #7c7c7c | #7c7c7c |
| --fs-color-neutral-mid-60 | mid-60 | #5a5a5a | #a1a1a1 |
| --fs-color-neutral-dark-70 | dark-70 | #3b3b3b | #c1c1c1 |
| --fs-color-neutral-dark-80 | dark-80 | #2b2b2b | #d9d9d9 |
| --fs-color-neutral-dark-90 | dark-90 | #202020 | #eeeeee |
| --fs-color-neutral-dark-95 | dark-95 | #1c1c1c | #fbfbfb |

### Feedback Color Variables

The feedback color variables are used to represent a message with a contextual color based on the result.

| Variable | Description | Light Value | Dark Value |
| --- | --- | --- | --- |
| --fs-color-positive-lightest | positive-lightest | #def7ed | #002415 |
| --fs-color-positive-lighter | positive-lighter | #7ecead | #083a25 |
| --fs-color-positive-light | positive-light | #41b483 | #0f5236 |
| --fs-color-positive-base | positive-base | #107048 | #107048 |
| --fs-color-positive-dark | positive-dark | #0f5236 | #41b483 |
| --fs-color-positive-darker | positive-darker | #083a25 | #7ecead |
| --fs-color-positive-darkest | positive-darkest | #002415 | #def7ed |
| --fs-color-negative-lightest | negative-lightest | #f6e6e5 | #4a1512 |
| --fs-color-negative-lighter | negative-lighter | #e3aeab | #72211d |
| --fs-color-negative-light | negative-light | #d58581 | #9b2d27 |
| --fs-color-negative-base | negative-base | #be3e37 | #be3e37 |
| --fs-color-negative-dark | negative-dark | #9b2d27 | #d58581 |
| --fs-color-negative-darker | negative-darker | #72211d | #e3aeab |
| --fs-color-negative-darkest | negative-darkest | #4a1512 | #f6e6e5 |
| --fs-color-warning-lightest | warning-lightest | #fcf6e3 | #473400 |
| --fs-color-warning-lighter | warning-lighter | #f7dd97 | #705200 |
| --fs-color-warning-light | warning-light | #f1cd6a | #d8a20e |
| --fs-color-warning-base | warning-base | #efba2a | #efba2a |
| --fs-color-warning-dark | warning-dark | #d8a20e | #f1cd6a |
| --fs-color-warning-darker | warning-darker | #705200 | #f7dd97 |
| --fs-color-warning-darkest | warning-darkest | #473400 | #fcf6e3 |
| --fs-color-info-lightest | info-lightest | #e3e9f7 | #081536 |
| --fs-color-info-lighter | info-lighter | #b0c1e8 | #0f2557 |
| --fs-color-info-light | info-light | #7996d7 | #173782 |
| --fs-color-info-base | info-base | #23489f | #23489f |
| --fs-color-info-dark | info-dark | #173782 | #7996d7 |
| --fs-color-info-darker | info-darker | #0f2557 | #b0c1e8 |
| --fs-color-info-darkest | info-darkest | #081536 | #e3e9f7 |

### Shadow variables

Below are the variables to be used as shadow..

| Variable | Description | Light Value | Dark Value |
| --- | --- | --- | --- |
| --fs-shadow-none | No shadow | 0 0 0 var(--color-neutral-light-00) | 0 0 0 var(--color-neutral-light-00) |
| --fs-shadow-sm | Light shadow | 0 1px 4px 0 color-mix(in srgb, var(--color-neutral-dark-95) 10%, rgba(0, 0, 0, 0)), 0 0 3px 0 color-mix(in srgb, var(--color-neutral-dark-95) 10%, rgba(0, 0, 0, 0)) | 0 1px 4px 0 color-mix(in srgb, var(--color-neutral-dark-95) 10%, rgba(0, 0, 0, 0)), 0 0 3px 0 color-mix(in srgb, var(--color-neutral-dark-95) 10%, rgba(0, 0, 0, 0)) |
| --fs-shadow-md | Standard shadow | 0 4px 8px 0 color-mix(in srgb, var(--color-neutral-dark-95) 10%, rgba(0, 0, 0, 0)), 0 0 3px 0 color-mix(in srgb, var(--color-neutral-dark-95) 10%, rgba(0, 0, 0, 0)) | 0 4px 8px 0 color-mix(in srgb, var(--color-neutral-dark-95) 10%, rgba(0, 0, 0, 0)), 0 0 3px 0 color-mix(in srgb, var(--color-neutral-dark-95) 10%, rgba(0, 0, 0, 0)) |
| --fs-shadow-lg | More intense shadow | 0 6px 12px 0 color-mix(in srgb, var(--color-neutral-dark-95) 10%, rgba(0, 0, 0, 0)), 0 0 3px 0 color-mix(in srgb, var(--color-neutral-dark-95) 10%, rgba(0, 0, 0, 0)) | 0 6px 12px 0 color-mix(in srgb, var(--color-neutral-dark-95) 10%, rgba(0, 0, 0, 0)), 0 0 3px 0 color-mix(in srgb, var(--color-neutral-dark-95) 10%, rgba(0, 0, 0, 0)) |
| --fs-shadow-xl | Very pronounced shadow | 0 16px 24px 0 color-mix(in srgb, var(--color-neutral-dark-95) 10%, rgba(0, 0, 0, 0)), 0 0 3px 0 color-mix(in srgb, var(--color-neutral-dark-95) 10%, rgba(0, 0, 0, 0)) | 0 16px 24px 0 color-mix(in srgb, var(--color-neutral-dark-95) 10%, rgba(0, 0, 0, 0)), 0 0 3px 0 color-mix(in srgb, var(--color-neutral-dark-95) 10%, rgba(0, 0, 0, 0)) |

# Grid system

Style Guide includes a responsive, mobile first fluid grid system that appropriately scales up to 12 columns as the device or viewport size increases. It includes predefined classes for easy layout options, as well as powerful mixins for generating more semantic layouts.

### Introduction

Grid systems are used for creating page layouts through a series of rows and columns that house your content. Here's how the Style Guide grid system works:

* Rows must be placed within a `.container` (fixed-width) or `.container-fluid` (full-width) for proper alignment and padding.
* Use rows to create horizontal groups of columns.
* Content should be placed within columns, and only columns may be immediate children of rows.
* Predefined grid classes like `.row` and `.col-xs-4` are available for quickly making grid layouts. Less mixins can also be used for more semantic layouts.
* Columns create gutters (gaps between column content) via `padding`. That padding is offset in rows for the first and last column via negative margin on `.row`s.
* The negative margin is why the examples below are outdented. It's so that content within grid columns is lined up with non-grid content.
* Grid columns are created by specifying the number of twelve available columns you wish to span. For example, three equal columns would use three `.col-xs-4`.
* If more than 12 columns are placed within a single row, each group of extra columns will, as one unit, wrap onto a new line.
* Grid classes apply to devices with screen widths greater than or equal to the breakpoint sizes, and override grid classes targeted at smaller devices. Therefore, applying any `.col-md-` class to an element will not only affect its styling on medium devices but also on large devices if a `.col-lg-` class is not present.

Look to the examples for applying these principles to your code.

### Media queries

We use the following media queries in our Less files to create the key breakpoints in our grid system.

```
/* Extra small devices (phones, less than 768px) */
/* No media query since this is the default in Style Guide */

/* Small devices (tablets, 768px and up) */
@media (min-width: @screen-sm-min) { ... }

/* Medium devices (desktops, 992px and up) */
@media (min-width: @screen-md-min) { ... }

/* Large devices (large desktops, 1200px and up) */
@media (min-width: @screen-lg-min) { ... }
```

We occasionally expand on these media queries to include a `max-width` to limit CSS to a narrower set of devices.

```
@media (max-width: @screen-xs-max) { ... }
@media (min-width: @screen-sm-min) and (max-width: @screen-sm-max) { ... }
@media (min-width: @screen-md-min) and (max-width: @screen-md-max) { ... }
@media (min-width: @screen-lg-min) { ... }
```

### Grid options

See how aspects of the Style Guide grid system work across multiple devices with a handy table.

|  | Extra small devices Phones (<768px) | Small devices Tablets (≥768px) | Medium devices Desktops (≥992px) | Large devices Desktops (≥1200px) |
| --- | --- | --- | --- | --- |
| Grid behavior | Horizontal at all times | Collapsed to start, horizontal above breakpoints | | |
| Container width | None (auto) | 750px | 970px | 1170px |
| Class prefix | `.col-xs-` | `.col-sm-` | `.col-md-` | `.col-lg-` |
| # of columns | 12 | | | |
| Column width | Auto | ~62px | ~81px | ~97px |
| Gutter width | 32px (16px on each side of a column) | | | |
| Nestable | Yes | | | |
| Offsets | Yes | | | |
| Column ordering | Yes | | | |

### Example: Stacked-to-horizontal

Using a single set of `.col-md-*` grid classes, you can create a basic grid system that starts out stacked on mobile devices and tablet devices (the extra small to small range) before becoming horizontal on desktop (medium) devices. Place grid columns in any `.row`.

.col-md-1

.col-md-1

.col-md-1

.col-md-1

.col-md-1

.col-md-1

.col-md-1

.col-md-1

.col-md-1

.col-md-1

.col-md-1

.col-md-1

.col-md-8

.col-md-4

.col-md-4

.col-md-4

.col-md-4

.col-md-6

.col-md-6

```
<div class="row">
	<div class="col-md-1">.col-md-1</div>
	<div class="col-md-1">.col-md-1</div>
	<div class="col-md-1">.col-md-1</div>
	<div class="col-md-1">.col-md-1</div>
	<div class="col-md-1">.col-md-1</div>
	<div class="col-md-1">.col-md-1</div>
	<div class="col-md-1">.col-md-1</div>
	<div class="col-md-1">.col-md-1</div>
	<div class="col-md-1">.col-md-1</div>
	<div class="col-md-1">.col-md-1</div>
	<div class="col-md-1">.col-md-1</div>
	<div class="col-md-1">.col-md-1</div>
</div>
<div class="row">
	<div class="col-md-8">.col-md-8</div>
	<div class="col-md-4">.col-md-4</div>
</div>
<div class="row">
	<div class="col-md-4">.col-md-4</div>
	<div class="col-md-4">.col-md-4</div>
	<div class="col-md-4">.col-md-4</div>
</div>
<div class="row">
	<div class="col-md-6">.col-md-6</div>
	<div class="col-md-6">.col-md-6</div>
</div>
```

### Example: Fluid container

Turn any fixed-width grid layout into a full-width layout by changing your outermost `.container` to `.container-fluid`.

```
<div class="container-fluid">
	<div class="row">
		...
	</div>
</div>
```

### Example: Mobile and desktop

Don't want your columns to simply stack in smaller devices? Use the extra small and medium device grid classes by adding `.col-xs-*` `.col-md-*` to your columns. See the example below for a better idea of how it all works.

.col-xs-12 .col-md-8

.col-xs-6 .col-md-4

.col-xs-6 .col-md-4

.col-xs-6 .col-md-4

.col-xs-6 .col-md-4

.col-xs-6

.col-xs-6

```
<!-- Stack the columns on mobile by making one full-width and the other half-width -->
<div class="row">
	<div class="col-xs-12 col-md-8">.col-xs-12 .col-md-8</div>
	<div class="col-xs-6 col-md-4">.col-xs-6 .col-md-4</div>
</div>

<!-- Columns start at 50% wide on mobile and bump up to 33.3% wide on desktop -->
<div class="row">
	<div class="col-xs-6 col-md-4">.col-xs-6 .col-md-4</div>
	<div class="col-xs-6 col-md-4">.col-xs-6 .col-md-4</div>
	<div class="col-xs-6 col-md-4">.col-xs-6 .col-md-4</div>
</div>

<!-- Columns are always 50% wide, on mobile and desktop -->
<div class="row">
	<div class="col-xs-6">.col-xs-6</div>
	<div class="col-xs-6">.col-xs-6</div>
</div>
```

### Example: Mobile, tablet, desktops

Build on the previous example by creating even more dynamic and powerful layouts with tablet `.col-sm-*` classes.

.col-xs-12 .col-sm-6 .col-md-8

.col-xs-6 .col-md-4

.col-xs-6 .col-sm-4

.col-xs-6 .col-sm-4

.col-xs-6 .col-sm-4

```
<div class="row">
	<div class="col-xs-12 col-sm-6 col-md-8">.col-xs-12 .col-sm-6 .col-md-8</div>
	<div class="col-xs-6 col-md-4">.col-xs-6 .col-md-4</div>
</div>
<div class="row">
	<div class="col-xs-6 col-sm-4">.col-xs-6 .col-sm-4</div>
	<div class="col-xs-6 col-sm-4">.col-xs-6 .col-sm-4</div>
	<!-- Optional: clear the XS cols if their content doesn't match in height -->
	<div class="clearfix visible-xs-block"></div>
	<div class="col-xs-6 col-sm-4">.col-xs-6 .col-sm-4</div>
</div>
```

### Example: Column wrapping

If more than 12 columns are placed within a single row, each group of extra columns will, as one unit, wrap onto a new line.

.col-xs-9

.col-xs-4  
Since 9 + 4 = 13 > 12, this 4-column-wide div gets wrapped onto a new line as one contiguous unit.

.col-xs-6  
Subsequent columns continue along the new line.

```
<div class="row">
	<div class="col-xs-9">.col-xs-9</div>
	<div class="col-xs-4">.col-xs-4<br>Since 9 + 4 = 13 &gt; 12, this 4-column-wide div gets wrapped onto a new line as one contiguous unit.</div>
	<div class="col-xs-6">.col-xs-6<br>Subsequent columns continue along the new line.</div>
</div>
```

### Responsive column resets

With the four tiers of grids available you're bound to run into issues where, at certain breakpoints, your columns don't clear quite right as one is taller than the other. To fix that, use a combination of a `.clearfix` and our responsive utility classes.

.col-xs-6 .col-sm-3
  
Resize your viewport or check it out on your phone for an example.

.col-xs-6 .col-sm-3

.col-xs-6 .col-sm-3

.col-xs-6 .col-sm-3

```
<div class="row">
	<div class="col-xs-6 col-sm-3">.col-xs-6 .col-sm-3</div>
	<div class="col-xs-6 col-sm-3">.col-xs-6 .col-sm-3</div>

	<!-- Add the extra clearfix for only the required viewport -->
	<div class="clearfix visible-xs-block"></div>

	<div class="col-xs-6 col-sm-3">.col-xs-6 .col-sm-3</div>
	<div class="col-xs-6 col-sm-3">.col-xs-6 .col-sm-3</div>
</div>
```

In addition to column clearing at responsive breakpoints, you may need to **reset offsets, pushes, or pulls**. See this in action in the grid example.

```
<div class="row">
	<div class="col-sm-5 col-md-6">.col-sm-5 .col-md-6</div>
	<div class="col-sm-5 col-sm-offset-2 col-md-6 col-md-offset-0">.col-sm-5 .col-sm-offset-2 .col-md-6 .col-md-offset-0</div>
</div>

<div class="row">
	<div class="col-sm-6 col-md-5 col-lg-6">.col-sm-6 .col-md-5 .col-lg-6</div>
	<div class="col-sm-6 col-md-5 col-md-offset-2 col-lg-6 col-lg-offset-0">.col-sm-6 .col-md-5 .col-md-offset-2 .col-lg-6 .col-lg-offset-0</div>
</div>
```

### Offsetting columns

Move columns to the right using `.col-md-offset-*` classes. These classes increase the left margin of a column by `*` columns. For example, `.col-md-offset-4` moves `.col-md-4` over four columns.

.col-md-4

.col-md-4 .col-md-offset-4

.col-md-3 .col-md-offset-3

.col-md-3 .col-md-offset-3

.col-md-6 .col-md-offset-3

```
<div class="row">
	<div class="col-md-4">.col-md-4</div>
	<div class="col-md-4 col-md-offset-4">.col-md-4 .col-md-offset-4</div>
</div>
<div class="row">
	<div class="col-md-3 col-md-offset-3">.col-md-3 .col-md-offset-3</div>
	<div class="col-md-3 col-md-offset-3">.col-md-3 .col-md-offset-3</div>
</div>
<div class="row">
	<div class="col-md-6 col-md-offset-3">.col-md-6 .col-md-offset-3</div>
</div>
```

### Nesting columns

To nest your content with the default grid, add a new `.row` and set of `.col-sm-*` columns within an existing `.col-sm-*` column. Nested rows should include a set of columns that add up to 12 or less (it is not required that you use all 12 available columns).

Level 1: .col-sm-9

Level 2: .col-xs-8 .col-sm-6

Level 2: .col-xs-4 .col-sm-6

```
<div class="row">
	<div class="col-sm-9">
	Level 1: .col-sm-9
		<div class="row">
			<div class="col-xs-8 col-sm-6">
				Level 2: .col-xs-8 .col-sm-6
			</div>
			<div class="col-xs-4 col-sm-6">
				Level 2: .col-xs-4 .col-sm-6
			</div>
		</div>
	</div>
</div>
```

### Column ordering

Easily change the order of our built-in grid columns with `.col-md-push-*` and `.col-md-pull-*` modifier classes.

.col-md-9 .col-md-push-3

.col-md-3 .col-md-pull-9

```
<div class="row">
	<div class="col-md-9 col-md-push-3">.col-md-9 .col-md-push-3</div>
	<div class="col-md-3 col-md-pull-9">.col-md-3 .col-md-pull-9</div>
</div>
```

### Less mixins and variables

In addition to prebuilt grid classes for fast layouts, Style Guide includes Less variables and mixins for quickly generating your own simple, semantic layouts.

#### Variables

Variables determine the number of columns, the gutter width, and the media query point at which to begin floating columns. We use these to generate the predefined grid classes documented above, as well as for the custom mixins listed below.

```
@grid-columns:              12;
@grid-gutter-width:         32px;
@grid-float-breakpoint:     768px;
```

#### Mixins

Mixins are used in conjunction with the grid variables to generate semantic CSS for individual grid columns.

```
// Creates a wrapper for a series of columns
.make-row(@gutter: @grid-gutter-width) {
	// Then clear the floated columns
	.clearfix();

	@media (min-width: @screen-sm-min) {
		margin-left:  (@gutter / -2);
		margin-right: (@gutter / -2);
	}

	// Negative margin nested rows out to align the content of columns
	.row {
		margin-left:  (@gutter / -2);
		margin-right: (@gutter / -2);
	}
}

// Generate the extra small columns
.make-xs-column(@columns; @gutter: @grid-gutter-width) {
	position: relative;
	// Prevent columns from collapsing when empty
	min-height: 1px;
	// Inner gutter via padding
	padding-left:  (@gutter / 2);
	padding-right: (@gutter / 2);

	// Calculate width based on number of columns available
	@media (min-width: @grid-float-breakpoint) {
		float: left;
		width: percentage((@columns / @grid-columns));
	}
}

// Generate the small columns
.make-sm-column(@columns; @gutter: @grid-gutter-width) {
	position: relative;
	// Prevent columns from collapsing when empty
	min-height: 1px;
	// Inner gutter via padding
	padding-left:  (@gutter / 2);
	padding-right: (@gutter / 2);

	// Calculate width based on number of columns available
	@media (min-width: @screen-sm-min) {
		float: left;
		width: percentage((@columns / @grid-columns));
	}
}

// Generate the small column offsets
.make-sm-column-offset(@columns) {
	@media (min-width: @screen-sm-min) {
		margin-left: percentage((@columns / @grid-columns));
	}
}
.make-sm-column-push(@columns) {
	@media (min-width: @screen-sm-min) {
		left: percentage((@columns / @grid-columns));
	}
}
.make-sm-column-pull(@columns) {
	@media (min-width: @screen-sm-min) {
		right: percentage((@columns / @grid-columns));
	}
}

// Generate the medium columns
.make-md-column(@columns; @gutter: @grid-gutter-width) {
	position: relative;
	// Prevent columns from collapsing when empty
	min-height: 1px;
	// Inner gutter via padding
	padding-left:  (@gutter / 2);
	padding-right: (@gutter / 2);

	// Calculate width based on number of columns available
	@media (min-width: @screen-md-min) {
		float: left;
		width: percentage((@columns / @grid-columns));
	}
}

// Generate the medium column offsets
.make-md-column-offset(@columns) {
	@media (min-width: @screen-md-min) {
		margin-left: percentage((@columns / @grid-columns));
	}
}
.make-md-column-push(@columns) {
	@media (min-width: @screen-md-min) {
		left: percentage((@columns / @grid-columns));
	}
}
.make-md-column-pull(@columns) {
	@media (min-width: @screen-md-min) {
		right: percentage((@columns / @grid-columns));
	}
}

// Generate the large columns
.make-lg-column(@columns; @gutter: @grid-gutter-width) {
	position: relative;
	// Prevent columns from collapsing when empty
	min-height: 1px;
	// Inner gutter via padding
	padding-left:  (@gutter / 2);
	padding-right: (@gutter / 2);

	// Calculate width based on number of columns available
	@media (min-width: @screen-lg-min) {
		float: left;
		width: percentage((@columns / @grid-columns));
	}
}

// Generate the large column offsets
.make-lg-column-offset(@columns) {
	@media (min-width: @screen-lg-min) {
		margin-left: percentage((@columns / @grid-columns));
	}
}
.make-lg-column-push(@columns) {
	@media (min-width: @screen-lg-min) {
		left: percentage((@columns / @grid-columns));
	}
}
.make-lg-column-pull(@columns) {
	@media (min-width: @screen-lg-min) {
		right: percentage((@columns / @grid-columns));
	}
}
```

#### Example usage

You can modify the variables to your own custom values, or just use the mixins with their default values. Here's an example of using the default settings to create a two-column layout with a gap between.

```
.wrapper {
	.make-row();
}
.content-main {
	.make-lg-column(8);
}
.content-secondary {
	.make-lg-column(3);
	.make-lg-column-offset(1);
}
```

```
<div class="wrapper">
	<div class="content-main">...</div>
	<div class="content-secondary">...</div>
</div>
```

# Responsive utilities

For faster mobile-friendly development, use these utility classes for showing and hiding content by device via media query. Also included are utility classes for toggling content when printed.

Try to use these on a limited basis and avoid creating entirely different versions of the same site. Instead, use them to complement each device's presentation.

## Available classes

Use a single or combination of the available classes for toggling content across viewport breakpoints.

|  | Extra small devices Phones (<768px) | Small devices Tablets (≥768px) | Medium devices Desktops (≥992px) | Large devices Desktops (≥1200px) |
| --- | --- | --- | --- | --- |
| `.visible-xs-*` | Visible | Hidden | Hidden | Hidden |
| `.visible-sm-*` | Hidden | Visible | Hidden | Hidden |
| `.visible-md-*` | Hidden | Hidden | Visible | Hidden |
| `.visible-lg-*` | Hidden | Hidden | Hidden | Visible |
| `.hidden-xs` | Hidden | Visible | Visible | Visible |
| `.hidden-sm` | Visible | Hidden | Visible | Visible |
| `.hidden-md` | Visible | Visible | Hidden | Visible |
| `.hidden-lg` | Visible | Visible | Visible | Hidden |

| Group of classes | CSS `display` |
| --- | --- |
| `.visible-*-block` | `display: block;` |
| `.visible-*-inline` | `display: inline;` |
| `.visible-*-inline-block` | `display: inline-block;` |

So, for extra small (`xs`) screens for example, the available `.visible-*-*` classes are: `.visible-xs-block`, `.visible-xs-inline`, and `.visible-xs-inline-block`.

## Print classes

Similar to the regular responsive classes, use these for toggling content for print.

| Classes | Browser | Print |
| --- | --- | --- |
| `.visible-print-block`  `.visible-print-inline`  `.visible-print-inline-block` | Hidden | Visible |
| `.hidden-print` | Visible | Hidden |

## Test cases

Resize your browser or load on different devices to test the responsive utility classes.

### Visible on...

Green checkmarks indicate the element **is visible** in your current viewport.

Extra small
✔ Visible on x-small

Small
✔ Visible on small

Medium
✔ Visible on medium

Large
✔ Visible on large

Extra small and small
✔ Visible on x-small and small

Medium and large
✔ Visible on medium and large

Extra small and medium
✔ Visible on x-small and medium

Small and large
✔ Visible on small and large

Extra small and large
✔ Visible on x-small and large

Small and medium
✔ Visible on small and medium

### Hidden on...

Here, green checkmarks also indicate the element **is hidden** in your current viewport.

Extra small
✔ Hidden on x-small

Small
✔ Hidden on small

Medium
✔ Hidden on medium

Large
✔ Hidden on large

Extra small and small
✔ Hidden on x-small and small

Medium and large
✔ Hidden on medium and large

Extra small and medium
✔ Hidden on x-small and medium

Small and large
✔ Hidden on small and large

Extra small and large
✔ Hidden on x-small and large

Small and medium
✔ Hidden on small and medium

# Typography

## Headings

All HTML headings, `<h1>` through `<h6>`, are available. `.h1` through `.h6` classes are also available, for when you want to match the font styling of a heading but still want your text to be displayed inline.

|  |  |
| --- | --- |
| h1. Style Guide heading | Bold 30px |
| h2. Style Guide heading | Bold 24px |
| h3. Style Guide heading | Bold 18px |
| h4. Style Guide heading | Bold 16px |
| h5. Style Guide heading | Bold 14px |
| h6. Style Guide heading | Bold 12px |

```
<h1>h1. Style Guide heading</h1>
<h2>h2. Style Guide heading</h2>
<h3>h3. Style Guide heading</h3>
<h4>h4. Style Guide heading</h4>
<h5>h5. Style Guide heading</h5>
<h6>h6. Style Guide heading</h6>
```

Create lighter, secondary text in any heading with a generic `<small>` tag or the `.small` class.

|  |
| --- |
| h1. Style Guide heading Secondary text |
| h2. Style Guide heading Secondary text |
| h3. Style Guide heading Secondary text |
| h4. Style Guide heading Secondary text |
| h5. Style Guide heading Secondary text |
| h6. Style Guide heading Secondary text |

```
<h1>h1. Style Guide heading <small>Secondary text</small></h1>
<h2>h2. Style Guide heading <small>Secondary text</small></h2>
<h3>h3. Style Guide heading <small>Secondary text</small></h3>
<h4>h4. Style Guide heading <small>Secondary text</small></h4>
<h5>h5. Style Guide heading <small>Secondary text</small></h5>
<h6>h6. Style Guide heading <small>Secondary text</small></h6>
```

## Horizontal rules

This is applied to the `<hr>`.

---

```
	<hr>
```

## Body copy

Style Guide's global default `font-size` is **14px**, with a `line-height` of **24px**. This is applied to the `<body>` and all paragraphs. In addition, `<p>` (paragraphs) receive a bottom margin of half their computed line-height (10px by default).

Nullam quis risus eget urna mollis ornare vel eu leo. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nullam id dolor id nibh ultricies vehicula.

Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec ullamcorper nulla non metus auctor fringilla. Duis mollis, est non commodo luctus, nisi erat porttitor ligula, eget lacinia odio sem nec elit. Donec ullamcorper nulla non metus auctor fringilla.

Maecenas sed diam eget risus varius blandit sit amet non magna. Donec id elit non mi porta gravida at eget metus. Duis mollis, est non commodo luctus, nisi erat porttitor ligula, eget lacinia odio sem nec elit.

```
<p>...</p>
```

## Note or reference data

This is applied to the `<body>` and all paragraphs. In addition, `<p>` (paragraphs) receive a low tone color.

Nullam quis risus eget urna mollis ornare vel eu leo. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nullam id dolor id nibh ultricies vehicula.

```
<p class="text-muted">...</p>
```

## Emphasis classes

Assign a visual meaning to the text through the use of auxiliary color.

Fusce dapibus, tellus ac cursus commodo, tortor mauris nibh.

Etiam porta sem malesuada magna mollis euismod.

Donec ullamcorper nulla non metus auctor fringilla.

Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis.

Duis mollis, est non commodo luctus, nisi erat porttitor ligula.

```
<p class="text-primary">Fusce dapibus, tellus ac cursus commodo, tortor mauris nibh.</p>
<p class="text-warning">Etiam porta sem malesuada magna mollis euismod.</p>
<p class="text-danger">Donec ullamcorper nulla non metus auctor fringilla.</p>
<p class="text-info">Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis.</p>
<p class="text-success">Duis mollis, est non commodo luctus, nisi erat porttitor ligula.</p>
```

### Lead body copy

Make a paragraph stand out by adding `.lead`.

Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor. Duis mollis, est non commodo luctus.

```
<p class="lead">...</p>
```

### Built with Less

The typographic scale is based on two Less variables in **variables.less**: `@font-size-base` and `@line-height-base`. The first is the base font-size used throughout and the second is the base line-height. We use those variables and some simple math to create the margins, paddings, and line-heights of all our type and more. Customize them and Style Guide adapts.

## Inline text elements

### Marked text

For highlighting a run of text due to its relevance in another context, use the `<mark>` tag.

You can use the mark tag to highlight text.

```
You can use the mark tag to <mark>highlight</mark> text.
```

### Deleted text

For indicating blocks of text that have been deleted use the `<del>` tag.

~~This line of text is meant to be treated as deleted text.~~

```
<del>This line of text is meant to be treated as deleted text.</del>
```

### Strikethrough text

For indicating blocks of text that are no longer relevant use the `<s>` tag.

~~This line of text is meant to be treated as no longer accurate.~~

```
<s>This line of text is meant to be treated as no longer accurate.</s>
```

### Inserted text

For indicating additions to the document use the `<ins>` tag.

This line of text is meant to be treated as an addition to the document.

```
<ins>This line of text is meant to be treated as an addition to the document.</ins>
```

### Underlined text

To underline text use the `<u>` tag.

This line of text will render as underlined

```
<u>This line of text will render as underlined</u>
```

Make use of HTML's default emphasis tags with lightweight styles.

### Small text

For de-emphasizing inline or blocks of text, use the `<small>` tag to set text at 85% the size of the parent. Heading elements receive their own `font-size` for nested `<small>` elements.

You may alternatively use an inline element with `.small` in place of any `<small>`.

This line of text is meant to be treated as fine print.

```
<small>This line of text is meant to be treated as fine print.</small>
```

### Bold

For emphasizing a snippet of text with a heavier font-weight.

The following snippet of text is **rendered as bold text**.

```
<strong>rendered as bold text</strong>
```

### Italics

For emphasizing a snippet of text with italics.

The following snippet of text is *rendered as italicized text*.

```
<em>rendered as italicized text</em>
```

#### Alternate elements

Feel free to use `<b>` and `<i>` in HTML5. `<b>` is meant to highlight words or phrases without conveying additional importance while `<i>` is mostly for voice, technical terms, etc.

## Alignment classes

Easily realign text to components with text alignment classes.

Left aligned text.

Center aligned text.

Right aligned text.

Justified text.

No wrap text.

```
<p class="text-left">Left aligned text.</p>
<p class="text-center">Center aligned text.</p>
<p class="text-right">Right aligned text.</p>
<p class="text-justify">Justified text.</p>
<p class="text-nowrap">No wrap text.</p>
```

## Transformation classes

Transform text in components with text capitalization classes.

Lowercased text.

Uppercased text.

Capitalized text.

```
<p class="text-lowercase">Lowercased text.</p>
<p class="text-uppercase">Uppercased text.</p>
<p class="text-capitalize">Capitalized text.</p>
```

## Abbreviations

Stylized implementation of HTML's `<abbr>` element for abbreviations and acronyms to show the expanded version on hover. Abbreviations with a `title` attribute have a light dotted bottom border and a help cursor on hover, providing additional context on hover.

### Basic abbreviation

For expanded text on long hover of an abbreviation, include the `title` attribute with the `<abbr>` element.

An abbreviation of the word attribute is attr.

```
<abbr title="attribute">attr</abbr>
```

### Initialism

Add `.initialism` to an abbreviation for a slightly smaller font-size.

HTML is the best thing since sliced bread.

```
<abbr title="HyperText Markup Language" class="initialism">HTML</abbr>
```

## Addresses

Present contact information for the nearest ancestor or the entire body of work. Preserve formatting by ending all lines with `<br>`.

**Twitter, Inc.**  
795 Folsom Ave, Suite 600  
San Francisco, CA 94107  
P: (123) 456-7890

**Full Name**  
[first.last@example.com](mailto:#)

```
<address>
	<strong>Twitter, Inc.</strong><br>
	795 Folsom Ave, Suite 600<br>
	San Francisco, CA 94107<br>
	<abbr title="Phone">P:</abbr> (123) 456-7890
</address>
<address>
	<strong>Full Name</strong><br>
	<a href="mailto:#">first.last@example.com</a>
</address>
```

## Blockquotes

For quoting blocks of content from another source within your document.

### Default blockquote

Wrap `<blockquote>` around any HTML as the quote. For straight quotes, we recommend a `<p>`.

> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.

```
<blockquote>
	<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
</blockquote>
```

### Blockquote options

Style and content changes for simple variations on a standard `<blockquote>`.

#### Naming a source

Add a `<footer>` for identifying the source. Wrap the name of the source work in `<cite>`.

> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.

```
<blockquote>
	<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
	<footer>Someone famous in <cite title="Source Title">Source Title</cite></footer>
</blockquote>
```

#### Alternate displays

Add `.blockquote-reverse` for a blockquote with right-aligned content.

> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.

```
<blockquote class="blockquote-reverse">
	...
</blockquote>
```

## Lists

### Unordered

A list of items in which the order does *not* explicitly matter.

* Lorem ipsum dolor sit amet
* Consectetur adipiscing elit
* Integer molestie lorem at massa
* Facilisis in pretium nisl aliquet
* Nulla volutpat aliquam velit
  + Phasellus iaculis neque
  + Purus sodales ultricies
  + Vestibulum laoreet porttitor sem
  + Ac tristique libero volutpat at
* Faucibus porta lacus fringilla vel
* Aenean sit amet erat nunc
* Eget porttitor lorem

```
<ul>
	<li>...</li>
</ul>
```

### Ordered

A list of items in which the order *does* explicitly matter.

1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa
4. Facilisis in pretium nisl aliquet
5. Nulla volutpat aliquam velit
6. Faucibus porta lacus fringilla vel
7. Aenean sit amet erat nunc
8. Eget porttitor lorem

```
<ol>
	<li>...</li>
</ol>
```

### Unstyled

Remove the default `list-style` and left margin on list items (immediate children only). **This only applies to immediate children list items**, meaning you will need to add the class for any nested lists as well.

* Lorem ipsum dolor sit amet
* Consectetur adipiscing elit
* Integer molestie lorem at massa
* Facilisis in pretium nisl aliquet
* Nulla volutpat aliquam velit
  + Phasellus iaculis neque
  + Purus sodales ultricies
  + Vestibulum laoreet porttitor sem
  + Ac tristique libero volutpat at
* Faucibus porta lacus fringilla vel
* Aenean sit amet erat nunc
* Eget porttitor lorem

```
<ul class="list-unstyled">
	<li>...</li>
</ul>
```

### Inline

Place all list items on a single line with `display: inline-block;` and some light padding.

* Lorem ipsum
* Phasellus iaculis
* Nulla volutpat

```
<ul class="list-inline">
	<li>...</li>
</ul>
```

### Description

A list of terms with their associated descriptions.

Description lists
:   A description list is perfect for defining terms.

Euismod
:   Vestibulum id ligula porta felis euismod semper eget lacinia odio sem nec elit.
:   Donec id elit non mi porta gravida at eget metus.

Malesuada porta
:   Etiam porta sem malesuada magna mollis euismod.

```
<dl>
	<dt>...</dt>
	<dd>...</dd>
</dl>
```

#### Horizontal description

Make terms and descriptions in `<dl>` line up side-by-side. Starts off stacked like default `<dl>`s, but when the navbar expands, so do these.

Description lists
:   A description list is perfect for defining terms.

Euismod
:   Vestibulum id ligula porta felis euismod semper eget lacinia odio sem nec elit.
:   Donec id elit non mi porta gravida at eget metus.

Malesuada porta
:   Etiam porta sem malesuada magna mollis euismod.

Felis euismod semper eget lacinia
:   Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.

```
<dl class="dl-horizontal">
	<dt>...</dt>
	<dd>...</dd>
</dl>
```

#### Auto-truncating

Horizontal description lists will truncate terms that are too long to fit in the left column with `text-overflow`. In narrower viewports, they will change to the default stacked layout.

## Links

### Apply custom styles to create greater navigation interest. Know the available style links.

A link standard applied in the name of the logged user.

[![Marcos Campos](images/user_picture.png)](#)

Hello [Juan Pablo de Maria](#) and [Margareth Ashley](#) Proin ut nulla vitae sem tristique lacinia. Cras vel commodo dui. Maecenas vitae elit eget nibh porta mollis. Etiam et ex a mi pretium porta. Proin vel mauris dictum mi ultrices iaculis sit amet in sapien. Cras sit amet consectetur eros, ut facilisis lacus. Maecenas facilisis, mauris vel maximus sagittis, lacus odio pellentesque massa, facilisis dapibus sapien nisl a nunc. Cras accumsan congue mi. Ut ligula erat, pellentesque ut ante vitae, efficitur rutrum libero.

```
	<div class="panel panel-default fs-no-margin">
		<div class="panel-body fs-sm-space media clearfix">
			<a class="pull-left" href="#">
				<div>
					<img src="images/user_picture.png" alt="Marcos Campos" class="fluig-style-guide thumb-profile img-rounded thumb-profile-sm thumb-profile-sm-legacy">
				</div>
			</a>
			<div class="media-body">
				<header>
					<h5 class="media-heading">
						<span class="wrap-element-popover"><a href="#" class="link-default">Marcos Campos</a></span>
						<span class="timeline-header-no-link"> shared </span>
						<a href="#" class="link-default">an post</a>
						<span class="timeline-header-no-link"> in </span>
						<span class="wrap-element-popover"><a href="#" class="link-default">usabilistas</a></span>
						<span class="timeline-header-no-link fs-no-bold"> - </span>
						<a href="#" class="link-reference-time fs-no-bold" title="15/5/2015 - 17:51:29">4 days ago</a>
					</h5>
				</header>
				<p>Hello <a href="#" class="link-default">Juan Pablo de Maria</a> and <a href="#" class="link-default">Margareth Ashley</a> Proin ut nulla vitae sem tristique lacinia. Cras vel commodo dui. Maecenas vitae elit eget nibh porta mollis. Etiam et ex a mi pretium porta. Proin vel mauris dictum mi ultrices iaculis sit amet in sapien. Cras sit amet consectetur eros, ut facilisis lacus. Maecenas facilisis, mauris vel maximus sagittis, lacus odio pellentesque massa, facilisis dapibus sapien nisl a nunc. Cras accumsan congue mi. Ut ligula erat, pellentesque ut ante vitae, efficitur rutrum libero.</p>
				
			</div>
		</div>
		<div class="panel-footer">
			
		</div>
	</div>
```

A link reference applied at the time ocurred post.

[![Adalberto Lima](images/user_picture.png)](#)

Hello [Juan Pablo de Maria](#) and [Margareth Ashley](#) Proin ut nulla vitae sem tristique lacinia. Cras vel commodo dui. Maecenas vitae elit eget nibh porta mollis. Etiam et ex a mi pretium porta. Proin vel mauris dictum mi ultrices iaculis sit amet in sapien. Cras sit amet consectetur eros, ut facilisis lacus. Maecenas facilisis, mauris vel maximus sagittis, lacus odio pellentesque massa, facilisis dapibus sapien nisl a nunc. Cras accumsan congue mi. Ut ligula erat, pellentesque ut ante vitae, efficitur rutrum libero.

```
	<div class="panel panel-default fs-no-margin">
		<div class="panel-body fs-sm-space media clearfix">
			<a class="pull-left" href="#">
				<div>
					<img src="images/user_picture.png" alt="Marcos Campos" class="fluig-style-guide thumb-profile img-rounded thumb-profile-sm thumb-profile-sm-legacy">
				</div>
			</a>
			<div class="media-body">
				<header>
					<h5 class="media-heading">
						<span class="wrap-element-popover"><a href="#">Marcos Campos</a></span>
						<span class="timeline-header-no-link"> shared </span>
						<a href="#" class="link-default">an post</a>
						<span class="timeline-header-no-link"> in </span>
						<span class="wrap-element-popover"><a href="#">usabilistas</a></span>
						<span class="timeline-header-no-link fs-no-bold"> - </span>
						<a href="#" class="link-reference-time fs-no-bold" title="15/5/2015 - 17:51:29">4 days ago</a>
					</h5>
				</header>
				<p>Hello <a href="#" class="link-default">Juan Pablo de Maria</a> and <a href="#" class="link-default">Margareth Ashley</a> Proin ut nulla vitae sem tristique lacinia. Cras vel commodo dui. Maecenas vitae elit eget nibh porta mollis. Etiam et ex a mi pretium porta. Proin vel mauris dictum mi ultrices iaculis sit amet in sapien. Cras sit amet consectetur eros, ut facilisis lacus. Maecenas facilisis, mauris vel maximus sagittis, lacus odio pellentesque massa, facilisis dapibus sapien nisl a nunc. Cras accumsan congue mi. Ut ligula erat, pellentesque ut ante vitae, efficitur rutrum libero.</p>
				
			</div>
		</div>
		<div class="panel-footer">
			
		</div>
	</div>
```

A style external link applied to url.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante. 
 [see more](#).

```
	<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante. <a href="#" class="fluigicon fluigicon-export fs-no-text-underline" target="_blank"></a>
	<a href="#" class="link-default"> see more</a>.</p>
```

A Pin applied in the link body text.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante. 
 [see note](#)

```
	<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante. <a href="#" class="fluigicon fluigicon-notes fs-no-text-underline"></a>
	<a href="#" class="link-default"> see note</a></p>
```

# Tables

## Basic example

For basic styling—light padding and only horizontal dividers—add the base class `.table` to any `<table>`. It may seem super redundant, but given the widespread use of tables for other plugins like calendars and date pickers, we've opted to isolate our custom table styles.

| # | First Name | Last Name | Username |
| --- | --- | --- | --- |
| 1 | Mark | Otto | @mdo |
| 2 | Jacob | Thornton | @fat |
| 3 | Larry | the Bird | @twitter |

```
<table class="table">
	...
</table>
```

## Striped rows

Use `.table-striped` to add zebra-striping to any table row within the `<tbody>`.

#### Cross-browser compatibility

Striped tables are styled via the `:nth-child` CSS selector, which is not available in Internet Explorer 8.

| # | First Name | Last Name | Username |
| --- | --- | --- | --- |
| 1 | Mark | Otto | @mdo |
| 2 | Jacob | Thornton | @fat |
| 3 | Larry | the Bird | @twitter |

```
<table class="table table-striped">
	...
</table>
```

## Bordered table

Add `.table-bordered` for borders on all sides of the table and cells.

| # | First Name | Last Name | Username |
| --- | --- | --- | --- |
| 1 | Mark | Otto | @mdo |
| Mark | Otto | @Style Guide |
| 2 | Jacob | Thornton | @fat |
| 3 | Larry the Bird | | @twitter |

```
<table class="table table-bordered">
	...
</table>
```

## Hover rows

Add `.table-hover` to enable a hover state on table rows within a `<tbody>`.

| # | First Name | Last Name | Username |
| --- | --- | --- | --- |
| 1 | Mark | Otto | @mdo |
| 2 | Jacob | Thornton | @fat |
| 3 | Larry the Bird | | @twitter |

```
<table class="table table-hover">
	...
</table>
```

## Condensed table

Add `.table-condensed` to make tables more compact by cutting cell padding in half.

| # | First Name | Last Name | Username |
| --- | --- | --- | --- |
| 1 | Mark | Otto | @mdo |
| 2 | Jacob | Thornton | @fat |
| 3 | Larry the Bird | | @twitter |

```
<table class="table table-condensed">
	...
</table>
```

## Contextual classes

Use contextual classes to color table rows or individual cells.

| Class | Description |
| --- | --- |
| `.active` | Applies the hover color to a particular row or cell |
| `.success` | Indicates a successful or positive action |
| `.info` | Indicates a neutral informative change or action |
| `.warning` | Indicates a warning that might need attention |
| `.danger` | Indicates a dangerous or potentially negative action |

| # | Column heading | Column heading | Column heading |
| --- | --- | --- | --- |
| 1 | Column content | Column content | Column content |
| 2 | Column content | Column content | Column content |
| 3 | Column content | Column content | Column content |
| 4 | Column content | Column content | Column content |
| 5 | Column content | Column content | Column content |
| 6 | Column content | Column content | Column content |
| 7 | Column content | Column content | Column content |
| 8 | Column content | Column content | Column content |
| 9 | Column content | Column content | Column content |

```
<!-- On rows -->
<tr class="active">...</tr>
<tr class="success">...</tr>
<tr class="warning">...</tr>
<tr class="danger">...</tr>
<tr class="info">...</tr>

<!-- On cells (`td` or `th`) -->
<tr>
	<td class="active">...</td>
	<td class="success">...</td>
	<td class="warning">...</td>
	<td class="danger">...</td>
	<td class="info">...</td>
</tr>
```

## Responsive tables

Create responsive tables by wrapping any `.table` in `.table-responsive` to make them scroll horizontally on small devices (under 768px). When viewing on anything larger than 768px wide, you will not see any difference in these tables.

#### Firefox and fieldsets

Firefox has some awkward fieldset styling involving `width` that interferes with the responsive table. This cannot be overriden without a Firefox-specific hack that we **don't** provide in Style Guide:

```
@-moz-document url-prefix() {
	fieldset { display: table-cell; }
}
```

For more information, read this Stack Overflow answer.

| # | Table heading | Table heading | Table heading | Table heading | Table heading | Table heading |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Table cell | Table cell | Table cell | Table cell | Table cell | Table cell |
| 2 | Table cell | Table cell | Table cell | Table cell | Table cell | Table cell |
| 3 | Table cell | Table cell | Table cell | Table cell | Table cell | Table cell |

| # | Table heading | Table heading | Table heading | Table heading | Table heading | Table heading |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Table cell | Table cell | Table cell | Table cell | Table cell | Table cell |
| 2 | Table cell | Table cell | Table cell | Table cell | Table cell | Table cell |
| 3 | Table cell | Table cell | Table cell | Table cell | Table cell | Table cell |

```
<div class="table-responsive">
	<table class="table">
		...
	</table>
</div>
```

## Layout-fixed tables

Sets the CSS attribute "table-layout" to the value "fixed".

```
<div class="table-responsive">
	<table class="table table-layout-fixed">
		...
	</table>
</div>
```

## Ellipsis cells

Gives the "ellipsis" property to the `td` and the `p` elements of the table, when it's contents are longer than the width of the cell.

In the first examble below, all of the table cells have the "ellipsis" attribute.

In the second one, just the cell with the class "cell-ellipsis" has the attribute. In this case, the table must have the class "table-layout-fixed", otherwise it will not work properly.

```
<div class="table-responsive">
	<table class="table table-ellipsis">
		<tr>
			<td></td>
			<td></td>
			<td></td>
			<td></td>
		</tr>
	</table>
</div>
```

```
<div class="table-responsive">
	<table class="table table-layout-fixed">
		<tr>
			<td class="cell-ellipsis"></td>
			<td></td>
			<td></td>
			<td></td>
		</tr>
	</table>
</div>
```

## Datatable markup

Datatable html markup for example.

### Datatable default title

First action


Toggle Dropdown

* [Action](#)
* [Another action](#)
* [Something else here](#)
* [Separated link](#)

|  | Code | Name | City | Actions |
| --- | --- | --- | --- | --- |
|  | 28472 | Bradley Abbott | North Halle |  |
|  | 61121 | Frances Snyder | Mathewview |  |
|  | 418 | Polly Wright | Clydeberg |  |
|  | 477 | Herbert Johnson | Schillerberg |  |
|  | 180 | Eula Patton | Schillerberg |  |

```
<div class="table-datatable">
	<div class="panel panel-default">
		<div class="panel-heading">
			<h3 class="panel-title">Datatable default title</h3>
		</div>
		<div class="panel-body">
			<div class="row">
				<div class="col-md-10">
					<div class="form-group">
						<input type="text" class="form-control" id="table-header-search" placeholder="Search...">
					</div>
				</div>
				<div class="col-md-2">
					<div class="btn-group">
						<button type="button" class="btn btn-primary">First action</button>
						<button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown">
						<span class="caret"></span>
						<span class="sr-only">Toggle Dropdown</span>
						</button>
						<ul class="dropdown-menu dropdown-menu-right" role="menu">
							<li><a href="#">Action</a></li>
							<li><a href="#">Another action</a></li>
							<li><a href="#">Something else here</a></li>
							<li class="divider"></li>
							<li><a href="#">Separated link</a></li>
						</ul>
					</div>
				</div>
			</div>
		</div>
		<!-- Table -->
		<table id="myTableHeader" class="table">
			<thead>
				<tr>
					<th>
						<input type="checkbox" name="selected-itens" value="all">
					</th>
					<th>Code</th>
					<th>Name</th>
					<th>City</th>
					<th>Actions</th>
				</tr>
			</thead>
			<tbody>
				<tr>
					<td>
						<input type="checkbox" name="selected-itens" value="item-1">
					</td>
					<td>28472</td>
					<td>Bradley Abbott</td>
					<td>North Halle</td>
					<td></td>
				</tr>
				<tr>
					<td>
						<input type="checkbox" name="selected-itens" value="item-2">
					</td>
					<td>61121</td>
					<td>Frances Snyder</td>
					<td>Mathewview</td>
					<td></td>
				</tr>
				<tr>
					<td>
						<input type="checkbox" name="selected-itens" value="item-3">
					</td>
					<td>418</td>
					<td>Polly Wright</td>
					<td>Clydeberg</td>
					<td></td>
				</tr>
				<tr>
					<td>
						<input type="checkbox" name="selected-itens" value="item-4">
					</td>
					<td>477</td>
					<td>Herbert Johnson</td>
					<td>Schillerberg</td>
					<td></td>
				</tr>
				<tr>
					<td>
						<input type="checkbox" name="selected-itens" value="item-5">
					</td>
					<td>180</td>
					<td>Eula Patton</td>
					<td>Schillerberg</td>
					<td></td>
				</tr>
			</tbody>
		</table>
	</div>
</div>
```

# Forms

## Basic example

Individual form controls automatically receive some global styling. All textual `<input>`, `<textarea>`, and `<select>` elements with `.form-control` are set to `width: 100%;` by default. Wrap labels and controls in `.form-group` for optimum spacing.

Email address

Password

File input


Example block-level help text here.

Check me out

Submit

```
<form role="form">
	<div class="form-group">
		<label for="exampleInputEmail1">Email address</label>
		<input type="email" class="form-control" id="exampleInputEmail1" placeholder="Enter email">
	</div>
	<div class="form-group">
		<label for="exampleInputPassword1">Password</label>
		<input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
	</div>
	<div class="form-group">
		<label for="exampleInputFile">File input</label>
		<input type="file" id="exampleInputFile">
		<p class="help-block">Example block-level help text here.</p>
	</div>
	<div class="checkbox">
		<label>
		<input type="checkbox"> Check me out
		</label>
	</div>
	<button type="submit" class="btn btn-default">Submit</button>
</form>
```

#### Don't mix form groups with input groups

Do not mix form groups directly with input groups. Instead, nest the input group inside of the form group.

## Search form

Example form with search icon.

```
<form role="form" autocomplete="off">
	<div class="form-group has-feedback">
		<input name="search-form-example" class="form-control" type="text" placeholder="Search...">
		<i class="flaticon flaticon-search icon-sm form-control-feedback" aria-hidden="true"></i>
	</div>
</form>
```

## Inline form

Add `.form-inline` to your `<form>` for left-aligned and inline-block controls. **This only applies to forms within viewports that are at least 768px wide.**

#### Requires custom widths

Inputs, selects, and textareas are 100% wide by default in Style Guide. To use the inline form, you'll have to set a width on the form controls used within.

#### Always add labels

Screen readers will have trouble with your forms if you don't include a label for every input. For these inline forms, you can hide the labels using the `.sr-only` class.

Email address

@

Password

Remember me

Sign in

```
<form class="form-inline" role="form">
	<div class="form-group">
		<label class="sr-only" for="exampleInputEmail2">Email address</label>
		<input type="email" class="form-control" id="exampleInputEmail2" placeholder="Enter email">
	</div>
	<div class="form-group">
		<div class="input-group">
			<div class="input-group-addon">@</div>
			<input class="form-control" type="email" placeholder="Enter email">
		</div>
	</div>
	<div class="form-group">
		<label class="sr-only" for="exampleInputPassword2">Password</label>
		<input type="password" class="form-control" id="exampleInputPassword2" placeholder="Password">
	</div>
	<div class="checkbox">
		<label>
		<input type="checkbox"> Remember me
		</label>
	</div>
	<button type="submit" class="btn btn-default">Sign in</button>
</form>
```

## Horizontal form

Use Style Guide's predefined grid classes to align labels and groups of form controls in a horizontal layout by adding `.form-horizontal` to the form. Doing so changes `.form-group`s to behave as grid rows, so no need for `.row`.

Email

Password

Remember me

Sign in

```
<form class="form-horizontal" role="form">
	<div class="form-group">
		<label for="inputEmail3" class="col-sm-2 control-label">Email</label>
		<div class="col-sm-10">
			<input type="email" class="form-control" id="inputEmail3" placeholder="Email">
		</div>
	</div>
	<div class="form-group">
		<label for="inputPassword3" class="col-sm-2 control-label">Password</label>
		<div class="col-sm-10">
			<input type="password" class="form-control" id="inputPassword3" placeholder="Password">
		</div>
	</div>
	<div class="form-group">
		<div class="col-sm-offset-2 col-sm-10">
			<div class="checkbox">
				<label>
				<input type="checkbox"> Remember me
				</label>
			</div>
		</div>
	</div>
	<div class="form-group">
		<div class="col-sm-offset-2 col-sm-10">
			<button type="submit" class="btn btn-default">Sign in</button>
		</div>
	</div>
</form>
```

## Supported controls

Examples of standard form controls supported in an example form layout.

### Inputs

Most common form control, text-based input fields. Includes support for all HTML5 types: `text`, `password`, `datetime`, `datetime-local`, `date`, `month`, `time`, `week`, `number`, `email`, `url`, `search`, `tel`, and `color`.

#### Type declaration required

Inputs will only be fully styled if their `type` is properly declared.

```
<input type="text" class="form-control" placeholder="Text input">
```

#### Input groups

To add integrated text or buttons before and/or after any text-based `<input>`, check out the input group component.

### Textarea

Form control which supports multiple lines of text. Change `rows` attribute as necessary.

```
<textarea class="form-control" rows="3"></textarea>
```

### Checkboxes and radios

Checkboxes are for selecting one or several options in a list, while radios are for selecting one option from many.

A checkbox or radio with the `disabled` attribute will be styled appropriately. To have the `<label>` for the checkbox or radio also display a "not-allowed" cursor when the user hovers over the label, add the `.disabled` class to your `.radio`, `.radio-inline`, `.checkbox`, `.checkbox-inline`, or `<fieldset>`.

#### Default (stacked)

Option one is this and that—be sure to include why it's great

Option two is disabled

  

Option one is this and that—be sure to include why it's great

Option two can be something else and selecting it will deselect option one

Option three is disabled

```
<div class="checkbox">
	<label>
	<input type="checkbox" value="">
	Option one is this and that—be sure to include why it's great
	</label>
</div>
<div class="checkbox disabled">
	<label>
	<input type="checkbox" value="" disabled>
	Option two is disabled
	</label>
</div>
<div class="radio">
	<label>
	<input type="radio" name="optionsRadios" id="optionsRadios1" value="option1" checked>
	Option one is this and that—be sure to include why it's great
	</label>
</div>
<div class="radio">
	<label>
	<input type="radio" name="optionsRadios" id="optionsRadios2" value="option2">
	Option two can be something else and selecting it will deselect option one
	</label>
</div>
<div class="radio disabled">
	<label>
	<input type="radio" name="optionsRadios" id="optionsRadios3" value="option3" disabled>
	Option three is disabled
	</label>
</div>
```

#### Inline checkboxes and radios

Use the `.checkbox-inline` or `.radio-inline` classes on a series of checkboxes or radios for controls that appear on the same line.

1

 2

 3
  


 1

 2

 3

```
<label class="checkbox-inline">
	<input type="checkbox" id="inlineCheckbox1" value="option1"> 1
</label>
<label class="checkbox-inline">
	<input type="checkbox" id="inlineCheckbox2" value="option2"> 2
</label>
<label class="checkbox-inline">
	<input type="checkbox" id="inlineCheckbox3" value="option3"> 3
</label>
<label class="radio-inline">
	<input type="radio" name="inlineRadioOptions" id="inlineRadio1" value="option1"> 1
</label>
<label class="radio-inline">
	<input type="radio" name="inlineRadioOptions" id="inlineRadio2" value="option2"> 2
</label>
<label class="radio-inline">
	<input type="radio" name="inlineRadioOptions" id="inlineRadio3" value="option3"> 3
</label>
```

### Selects

Use the default option, or add `multiple` to show multiple options at once.

1
2
3
4
5
  

1
2
3
4
5
  

1
2
3
4
5

```
<select class="form-control">
	<option>1</option>
	<option>2</option>
	<option>3</option>
	<option>4</option>
	<option>5</option>
</select>
<select multiple class="form-control">
	<option>1</option>
	<option>2</option>
	<option>3</option>
	<option>4</option>
	<option>5</option>
</select>
```

## Static control

When you need to place plain text next to a form label within a horizontal form, use the `.form-control-static` class on a `<p>`.

Email

email@example.com

Password

```
<form class="form-horizontal" role="form">
	<div class="form-group">
		<label class="col-sm-2 control-label">Email</label>
		<div class="col-sm-10">
			<p class="form-control-static">email@example.com</p>
		</div>
	</div>
	<div class="form-group">
		<label for="inputPassword" class="col-sm-2 control-label">Password</label>
		<div class="col-sm-10">
			<input type="password" class="form-control" id="inputPassword" placeholder="Password">
		</div>
	</div>
</form>
```

## Input focus

We remove the default `outline` styles on some form controls and apply a `box-shadow` in its place for `:focus`.

#### Demo `:focus` state

The above example input uses custom styles in our documentation to demonstrate the `:focus` state on a `.form-control`.

## Disabled inputs

Add the `disabled` boolean attribute on an input to prevent user input and trigger a slightly different look.

```
<input class="form-control" id="disabledInput" type="text" placeholder="Disabled input here..." disabled>
```

### Disabled fieldsets

Add the `disabled` attribute to a `<fieldset>` to disable all the controls within the `<fieldset>` at once.

#### Caveat about link functionality of `<a>`

Our styles use `pointer-events: none` to try to disable the link functionality of `<a class="btn btn-*">` buttons in this case, but that CSS property is not yet standardized and isn't fully supported in Opera 18 and below, or in Internet Explorer 11. So to be safe, use custom JavaScript to disable such links.

#### Cross-browser compatibility

While Style Guide will apply these styles in all browsers, Internet Explorer 9 and below don't actually support the `disabled` attribute on a `<fieldset>`. Use custom JavaScript to disable the fieldset in these browsers.

Disabled input

Disabled select menu

Disabled select

Can't check this

Submit

```
<form role="form">
	<fieldset disabled>
		<div class="form-group">
			<label for="disabledTextInput">Disabled input</label>
			<input type="text" id="disabledTextInput" class="form-control" placeholder="Disabled input">
		</div>
		<div class="form-group">
			<label for="disabledSelect">Disabled select menu</label>
			<select id="disabledSelect" class="form-control">
				<option>Disabled select</option>
			</select>
		</div>
		<div class="checkbox">
			<label>
			<input type="checkbox"> Can't check this
			</label>
		</div>
		<button type="submit" class="btn btn-primary">Submit</button>
	</fieldset>
</form>
```

## Readonly inputs

Add the `readonly` boolean attribute on an input to prevent user input and style the input as disabled.

```
<input class="form-control" type="text" placeholder="Readonly input here…" readonly>
```

## Validation states

Style Guide includes validation styles for error, warning, and success states on form controls. To use, add `.has-warning`, `.has-error`, or `.has-success` to the parent element. Any `.control-label`, `.form-control`, and `.help-block` within that element will receive the validation styles.

Input with success


Example block-level help text here.

Input with warning


Example block-level help text here.

Input with error


Example block-level help text here.

Input with info


Example block-level help text here.

```
<div class="form-group has-success">
	<label class="control-label" for="inputSuccess1">Input with success</label>
	<input type="text" class="form-control" id="inputSuccess1">
	<p class="help-block">Example block-level help text here.</p>
</div>
<div class="form-group has-warning">
	<label class="control-label" for="inputWarning1">Input with warning</label>
	<input type="text" class="form-control" id="inputWarning1">
	<p class="help-block">Example block-level help text here.</p>
</div>
<div class="form-group has-error">
	<label class="control-label" for="inputError1">Input with error</label>
	<input type="text" class="form-control" id="inputError1">
	<p class="help-block">Example block-level help text here.</p>
</div>
<div class="form-group has-info">
	<label class="control-label" for="inputInfo1">Input with info</label>
	<input type="text" class="form-control" id="inputInfo1">
	<p class="help-block">Example block-level help text here.</p>
</div>
```

### With optional icons

You can also add optional feedback icons with the addition of `.has-feedback` and the right icon.

#### Icons, labels, and input groups

Manual positioning of feedback icons is required for inputs without a label and for input groups with an add-on on the right. You are strongly encouraged to provide labels for all inputs for accessibility reasons. If you wish to prevent labels from being displayed, hide them with the `sr-only` class. If you must do without labels, adjust the `top` value of the feedback icon. For input groups, adjust the `right` value to an appropriate pixel value depending on the width of your addon.

Input with success

Input with warning

Input with error

Input with info

Input group with success

@

```
<div class="form-group has-success has-feedback">
	<label class="control-label" for="inputSuccess2">Input with success</label>
	<input type="text" class="form-control" id="inputSuccess2">
	<i class="flaticon flaticon-check-circle icon-sm form-control-feedback" aria-hidden="true"></i>
</div>
<div class="form-group has-warning has-feedback">
	<label class="control-label" for="inputWarning2">Input with warning</label>
	<input type="text" class="form-control" id="inputWarning2">
	<i class="flaticon flaticon-alert icon-sm form-control-feedback" aria-hidden="true"></i>
</div>
<div class="form-group has-error has-feedback">
	<label class="control-label" for="inputError2">Input with error</label>
	<input type="text" class="form-control" id="inputError2">
	<i class="flaticon flaticon-info icon-sm form-control-feedback" aria-hidden="true"></i>
</div>
<div class="form-group has-info has-feedback">
	<label class="control-label" for="inputInfo2">Input with info</label>
	<input type="text" class="form-control" id="inputInfo2">
	<i class="flaticon flaticon-info icon-sm form-control-feedback" aria-hidden="true"></i>
</div>
```

#### Optional icons in horizontal and inline forms

Input with success

```
<form class="form-horizontal" role="form">
	<div class="form-group has-success has-feedback">
		<label class="control-label col-sm-3" for="inputSuccess3">Input with success</label>
		<div class="col-sm-9">
			<input type="text" class="form-control" id="inputSuccess3">
			<i class="flaticon flaticon-check-circle icon-sm form-control-feedback" aria-hidden="true"></i>
		</div>
	</div>
</form>
```

Input with success

```
<form class="form-inline" role="form">
	<div class="form-group has-success has-feedback">
		<label class="control-label" for="inputSuccess4">Input with success</label>
		<input type="text" class="form-control" id="inputSuccess4">
		<i class="flaticon flaticon-check-circle icon-sm form-control-feedback" aria-hidden="true"></i>
	</div>
</form>
```

#### Optional icons with hidden `.sr-only` labels

For form controls with no visible label, add the `.sr-only` class on the label. Style Guide will automatically adjust the position of the icon once it's been added.

Hidden label

```
<div class="form-group has-success has-feedback">
	<label class="control-label sr-only" for="inputSuccess5">Hidden label</label>
	<input type="text" class="form-control" id="inputSuccess5">
	<i class="flaticon flaticon-check-circle icon-sm form-control-feedback" aria-hidden="true"></i>
</div>
```

## Control sizing

Set heights using classes like `.input-lg`, and set widths using grid column classes like `.col-lg-*`.

### Height sizing

Create taller or shorter form controls that match button sizes.

.input-lg

Default select

.input-sm

```
<input class="form-control input-lg" type="text" placeholder=".input-lg">
<input class="form-control" type="text" placeholder="Default input">
<input class="form-control input-sm" type="text" placeholder=".input-sm">
<select class="form-control input-lg">...</select>
<select class="form-control">...</select>
<select class="form-control input-sm">...</select>
```

### Horizontal form group sizes

Quickly size labels and form controls within `.form-horizontal` by adding `.form-group-lg` or `.form-group-sm`.

Large label

Small label

```
<form class="form-horizontal" role="form">
	<div class="form-group form-group-lg clearfix">
		<label class="col-sm-2 control-label" for="formGroupInputLarge">Large label</label>
		<div class="col-sm-10">
			<input class="form-control" type="text" id="formGroupInputLarge" placeholder="Large input">
		</div>
	</div>
	<div class="form-group form-group-sm">
		<label class="col-sm-2 control-label" for="formGroupInputSmall">Small label</label>
		<div class="col-sm-10">
			<input class="form-control" type="text" id="formGroupInputSmall" placeholder="Small input">
		</div>
	</div>
</form>
```

### Column sizing

Wrap inputs in grid columns, or any custom parent element, to easily enforce desired widths.

```
<div class="row">
	<div class="col-xs-2">
		<input type="text" class="form-control" placeholder=".col-xs-2">
	</div>
	<div class="col-xs-3">
		<input type="text" class="form-control" placeholder=".col-xs-3">
	</div>
	<div class="col-xs-4">
		<input type="text" class="form-control" placeholder=".col-xs-4">
	</div>
</div>
```

## Help text

Block level help text for form controls.

A block of help text that breaks onto a new line and may extend beyond one line.

```
<span class="help-block">A block of help text that breaks onto a new line and may extend beyond one line.</span>
```

# Skeleton Loader

This class adds the skeleton-loader style to an element, this is used when it is necessary to show for the user that
certain content is in its loading state, providing feedback to the user of this state.

## Content rendered

##### Requests

### Vacation Request

###### Request

Some quick example text to build on the card title and make up the bulk of the card's
content.

[Create](#)
[View records](#)

### Customer service

###### Request

Some quick example text to build on the card title and make up the bulk of the card's
content.

[Create](#)
[View records](#)

### Payment Closing

###### Request

Some quick example text to build on the card title and make up the bulk of the card's
content.

[Create](#)
[View records](#)

### Create Maintenance

###### Request

Some quick example text to build on the card title and make up the bulk of the card's
content.

[Create](#)
[View records](#)

##### Create User

Email address

Password

File input


Example block-level help text here.

Check me out

Submit


## Content in loading state.

##### Requests

### 

######

### 

######

### 

######

### 

######

##### Create User

Email address

Password

File input

Check me out

HTML code from the example above:

```
    <div class="row col-md-12">
      <h5>
        Requests
      </h5>
    </div>
    <div class="row">
      <div class="col-md-3">
        <div class="card">
          <div class="card-body">
            <h3 class="card-title"><span class="fs-skeleton-loader size-40"></span></h3>
            <h6 class="card-subtitle mb-2 text-muted"><span class="fs-skeleton-loader size-20"></span></h6>
            <p class="card-text">
            <div class="fs-skeleton-loader"></div>
            <div class="fs-skeleton-loader"></div>
            </p>
            <a href="#" class="card-link fs-skeleton-loader size-20"></a>
            <a href="#" class="card-link fs-skeleton-loader size-20"></a>
          </div>
        </div>
      </div>

      <div class="col-md-3">
        <div class="card">
          <div class="card-body">
            <h3 class="card-title"><span class="fs-skeleton-loader size-40"><span></h3>
            <h6 class="card-subtitle mb-2 text-muted"><span class="fs-skeleton-loader size-20"></span></h6>
            <p class="card-text">
            <div class="fs-skeleton-loader"></div>
            <div class="fs-skeleton-loader"></div>
            </p>
            <a href="#" class="card-link fs-skeleton-loader size-20"></a>
            <a href="#" class="card-link fs-skeleton-loader size-20"></a>
          </div>
        </div>
      </div>


      <div class="col-md-3">
        <div class="card">
          <div class="card-body">
            <h3 class="card-title"><span class="fs-skeleton-loader size-40"></span></h3>
            <h6 class="card-subtitle mb-2 text-muted"><span class="fs-skeleton-loader size-20"></span></h6>
            <p class="card-text">
            <div class="fs-skeleton-loader"></div>
            <div class="fs-skeleton-loader"></div>
            </p>
            <a href="#" class="card-link fs-skeleton-loader size-20"></a>
            <a href="#" class="card-link fs-skeleton-loader size-20"></a>
          </div>
        </div>
      </div>

      <div class="col-md-3">
        <div class="card">
          <div class="card-body">
            <h3 class="card-title"><span class="fs-skeleton-loader size-40"></span></h3>
            <h6 class="card-subtitle mb-2 text-muted"><span class="fs-skeleton-loader size-20"></span></h6>
            <p class="card-text">
            <div class="fs-skeleton-loader"></div>
            <div class="fs-skeleton-loader"></div>
            </p>
            <a href="#" class="card-link fs-skeleton-loader size-20"></a>
            <a href="#" class="card-link fs-skeleton-loader size-20"></a>
          </div>
        </div>
      </div>
    </div>
    <div class="row col-md-12">
      <h3>
        Create User
      </h3>
    </div>
    <form role="form">
      <div class="form-group">
        <label for="exampleInputEmail1">Email address</label>
        <div class="fs-skeleton-loader fs-skeleton-loader-input"></div>
      </div>
      <div class="form-group">
        <label for="exampleInputPassword1">Password</label>
        <div class="fs-skeleton-loader fs-skeleton-loader-input"></div>
      </div>
      <div class="form-group">
        <label for="exampleInputFile" class="exampleInputFile" style="display: block">File input</label>
        <div class="fs-skeleton-loader size-20 fs-skeleton-loader-input"></div>
      </div>
      <div class="checkbox">
        <label>
          <input type="checkbox"> Check me out
        </label>
      </div>
      <div class="fs-skeleton-loader fs-skeleton-loader-button"></div>
    </form>
```

# Helpers

## Scrollbar

Classes that change *Scrollbar* of elements

| Name | Description |
| --- | --- |
| .fs-scrollbar | Add style in scrollbar |
| .fs-scrollbar-thin | Add thin style in scrollbar |

## Positioning

Classes that change *positioning* of elements

| Name | Description |
| --- | --- |
| .fs-clearfix | Fix problems when there children with float |
| .fs-float-none | Insert float: none |
| .fs-float-right | Insert float: right |
| .fs-float-left | Insert float: left |
| .fs-clear-both | Insert clear: both |
| .fs-clear-right | Insert clear: right |
| .fs-clear-left | Insert clear: left |
| .fs-overflow-hidden | Insert overflow: hidden |
| .fs-overflow-visible | Insert overflow: visible |
| .fs-overflow-auto | Insert overflow: auto |
| .fs-overflow-x-auto | Insert overflow-x: auto |
| .fs-overflow-y-auto | Insert overflow-y: auto |
| .fs-position-relative | Insert position: relative |
| .fs-position-absolute | Insert position: absolute |
| .fs-position-fixed | Insert position: fixed |
| .fs-position-static | Insert position: static |
| .fs-position-sticky | Insert position: sticky |
| .fs-position-top-left | Insert top: 0 and left: 0 |
| .fs-position-top-right | Insert top: 0 and right: 0 |
| .fs-position-bottom-left | Insert bottom: 0 and left: 0 |
| .fs-position-bottom-right | Insert bottom: 0 and right: 0 |

## Block and inline

Classes that change the *display* of elements

| Name | Description |
| --- | --- |
| .fs-display-block | Insert display: block |
| .fs-display-inline | Insert display: inline |
| .fs-display-inline-block | Insert display: inline-block |
| .fs-display-none | Insert display: none (hide element) |
| .fs-display-flex | Insert display: flex |
| .fs-display-inline-flex | Insert display: inline-flex |
| .fs-display-grid | Insert display: grid |

## Flex helpers

Classes to assist with *flex display*

| Name | Description |
| --- | --- |
| .fs-align-items-center | Insert align-items: center |
| .fs-align-items-start | Insert align-items: start |
| .fs-align-items-end | Insert align-items: end |
| .fs-align-items-flex-start | Insert align-items: flex-start |
| .fs-align-items-flex-end | Insert align-items: flex-end |
| .fs-align-items-stretch | Insert align-items: stretch |
| .fs-align-items-baseline | Insert align-items: baseline |
| .fs-align-self-flex-end | Insert align-self: flex-end |
| .fs-align-self-center | Insert align-self: center |
| .fs-justify-content-center | Insert justify-content: center |
| .fs-justify-content-left | Insert justify-content: left |
| .fs-justify-content-right | Insert justify-content: right |
| .fs-justify-content-space-between | Insert justify-content: space-between |
| .fs-justify-content-space-around | Insert justify-content: space-around |
| .fs-justify-content-flex-start | Insert justify-content: flex-start |
| .fs-justify-content-flex-end | Insert justify-content: flex-end |
| .fs-flex-wrap-nowrap | Insert flex-wrap: nowrap |
| .fs-flex-wrap-wrap | Insert flex-wrap: flex-wrap-wrap |
| .fs-flex-wrap-wrap-reverse | Insert flex-wrap: wrap-reverse |
| .fs-flex-direction-row | Insert flex-direction: row |
| .fs-flex-direction-row-reverse | Insert flex-direction: row-reverse |
| .fs-flex-direction-column | Insert flex-direction: column |
| .fs-flex-direction-column-reverse | Insert flex-direction: column-reverse |
| .fs-flex-1 | Insert flex: 1 |
| .fs-**(xs, sm, md, lg, xl)**-gap | Insert gap **(4px, 8px, 16px, 24px, 32px)** between the contents in display |
| .fs-**(xs, sm, md, lg, xl)**-gap-horizontal | Insert gap **(4px, 8px, 16px, 24px, 32px)** in the horizontal between the contents in display |
| .fs-**(xs, sm, md, lg, xl)**-gap-vertical | Insert gap **(4px, 8px, 16px, 24px, 32px)** in the vertical between the contents in display |

## Size

Classes that changes the *size* of elements

| Name | Description |
| --- | --- |
| .fs-width-auto | Insert width: auto |
| .fs-width-50 a .fs-width-500 | Change *width* of 50px in 50px |
| .fs-min-width-50 a .fs-min-width-500 | Change *min-width* of 50px in 50px |
| .fs-max-width-50 a .fs-max-width-500 | Change *max-width* of 50px in 50px |
| .fs-width-inherit | Insert width: inherit |
| .fs-full-width | Insert width: 100% |
| .fs-half-width | Insert width: 50% |
| .fs-one-third-width | Insert width: 33.333333% |
| .fs-one-fourth-width | Insert width: 25% |
| .fs-one-fifth-width | Insert width: 20% |
| .fs-one-sixth-width | Insert width: 16.666667% |
| .fs-max-full-width | Insert max-width: 100% |
| .fs-height-inherit | Insert height: inherit |
| .fs-height-auto | Insert height: auto |
| .fs-height-50 a .fs-height-500 | Change *height* of 50px in 50px |
| .fs-min-height-50 a .fs-min-height-500 | Change *min-height* of 50px in 50px |
| .fs-max-height-50 a .fs-max-height-500 | Change *max-height* of 50px in 50px |
| .fs-no-resize | Blocks resizing (resize: none) |

## Margin and Padding

Classes that changes the *size* of elements

### Structure of Helper Class Naming

Helper classes are named following a logical structure that facilitates the identification and proper use of each class. Below is the explanation of the naming structure:

#### General Class Format

```
.{breakpoint}:fs-{type and direction}-{value}
```

#### Explanation of the parts of the class name

**{breakpoint}**: Is optional. Defines at which breakpoint the class will be applied.

* xs: Extra small (devices less than 768px)
* sm: Small (devices from 768px)
* md: Medium (devices from 992px)
* lg: Large (devices from 1200px)

**{type and direction}**: Indicates the type and the direction of the spacing. The values can be:

* m: For all directions of margin (top, bottom, left, and right)
* mt: Margin Top
* mb: Margin Bottom
* ml: Margin Left
* mr: Margin Right
* mx: Margin Horizontal (left and right)
* my: Margin Vertical (top and bottom)
* p: For all directions of padding (top, bottom, left, and right)
* pt: Padding Top
* pb: Padding Bottom
* pl: Padding Left
* pr: Padding Right
* px: Padding Horizontal (left and right)
* py: Padding Vertical (top and bottom)

**{value}**: Represents the value of the spacing, which can be one of the following:

* 0, 4, 8, 16, 24, 32, 40, 48, 56, 64 (values in pixels)
* auto

### Examples of use

#### Using Margins

```
<!-- Margin applied to all breakpoints -->
<div class="fs-m-8">This element has a margin of 8px.</div>

<!-- Top Margin applied only at the xs breakpoint -->
<div class="xs:fs-mt-16">This element has a top margin of 16px (applied in xs).</div>

<!-- Bottom Margin applied only at the sm breakpoint -->
<div class="sm:fs-mb-8">This element has a bottom margin of 8px (applied in sm).</div>

<!-- Horizontal Margin applied only at the md breakpoint -->
<div class="md:fs-mx-24">This element has a margin of 24px on the sides (applied in md).</div>

<!-- Vertical Margin applied only at the lg breakpoint -->
<div class="lg:fs-my-32">This element has a margin of 32px on the top and bottom (applied in lg).</div>
```

#### Using Paddings

```
<!-- Padding applied to all breakpoints -->
<div class="fs-m-24">This element has a padding of 24px.</div>

<!-- Top Padding applied only at the xs breakpoint -->
<div class="xs:fs-pt-4">This element has a top padding of 4px (applied in xs).</div>

<!-- Bottom Padding applied only at the sm breakpoint -->
<div class="sm:fs-pb-16">This element has a bottom padding of 16px (applied in sm).</div>

<!-- Horizontal Padding applied only at the md breakpoint -->
<div class="md:fs-px-40">This element has a padding of 40px on the sides (applied in md).</div>

<!-- Vertical Padding applied only at the lg breakpoint -->
<div class="lg:fs-py-8">This element has a padding of 8px on the top and bottom (applied in lg).</div>
```

#### Combining Classes

```
<!-- Top Margin and Bottom Padding applied at the sm breakpoint -->
<div class="fs-mt-24 sm:fs-mt-16 xs:fs-mt-8 sm:fs-pb-8">
	This element has a top margin of 24px (applied globally), 16px (applied in sm), and 8px (applied in xs), along with a bottom padding of 8px (applied in sm).
</div>

<!-- Horizontal Margin and Vertical Padding applied at the md breakpoint -->
<div class="md:fs-mx-24 md:fs-py-16">This element has a margin of 24px on the sides and a padding of 16px on the top and bottom (applied in md).</div>
```

## Text and alignment

Classes that changes *size* elements and aligment

| Name | Description |
| --- | --- |
| .fs-text-left **(-xs, -sm)** | Align left |
| .fs-text-right **(-xs, -sm)** | Align right |
| .fs-text-justify | Text justify |
| .fs-text-center | Align center |
| .fs-text-center-all | Set vertical align and horizontal align to text |
| .fs-v-align-top | Align the element on top |
| .fs-v-align-middle | Align the element on middle |
| .fs-v-align-bottom | Align the element on base |
| .fs-ellipsis | Insert (...) |
| .fs-nowrap | Insert white-space: nowrap |
| .fs-white-space-normal | Insert white-space: normal |
| .fs-no-bold | Insert font-weight: none |
| .fs-font-bold | Insert font-weight: bold |
| .fs-font-italic | Insert font-style: italic |
| .fs-word-break-all | Insert word-break: break-all |
| .fs-word-break | Insere word-break: break-word |
| .fs-no-word-break | Insert word-break: normal |
| .fs-list-style-disc | Add the standard style on lists |
| .fs-no-list-style | Remove the standard style on lists |
| .fs-text-underline | Insert underline |
| .fs-no-text-underline | Remove underline link and hover |
| .fs-small-letter-spacing | Decreases the spacing of the letters |
| .fs-text-uppercase | Transform all caracters to uppercase. |
| .fs-text-lowercase | Transform all caracters to lowercase. |
| .fs-text-capitalize | Transform the first caracter to uppercase. |
| .fs-text-xs | Set font size element to 10px. |
| .fs-text-sm | Set font size element to 12px. |
| .fs-text-md | Set font size element to 14px. |
| .fs-text-lg | Set font size element to 16px. |
| .fs-text-xl | Set font size element to 18px. |
| .fs-text-xxl | Set font size element to 24px. |
| .fs-text-xxxl | Set font size element to 30px. |
| .fs-style-list | Apply the standard type `ul` and `ol`. |

## Background, border and transparency

Classes that changes the background colors, border and transparency

| Name | Description |
| --- | --- |
| .fs-no-bg | Remove background |
| .fs-no-bghover | Remove background when the element recebe hover |
| .fs-no-shadow | Remove box-shadow |
| .fs-shadow-light | Add box-shadow light |
| .fs-shadow-medium | Add box-shadow medium |
| .fs-shadow-dark | Add box-shadow dark |
| .fs-shadow-ultra-dark | Add box-shadow ultra-dark |
| .fs-border | Add border |
| .fs-no-border | Remove border |
| .fs-no-border-right | Remove border right |
| .fs-no-border-left | Remove border left |
| .fs-no-border-bottom | Remove border bottom |
| .fs-no-border-top | Remove border top |
| .fs-border-dashed | Add border dashed |
| .fs-border-radius | Add border radius |
| .fs-border-rounded-full | Add full border radius |
| .fs-no-border-radius | Remove border radius |
| .fs-no-border-left-radius | Remove border radius left |
| .fs-no-border-right-radius | Remove border radius right |
| .fs-no-border-top-radius | Remove border radius top |
| .fs-no-border-bottom-radius | Remove border radius bottom |
| .fs-no-border-top-right-radius | Remove border radius top right |
| .fs-no-border-bottom-right-radius | Remove border radius bottom right |
| .fs-no-border-bottom-left-radius | Remove border radius bottom left |
| .fs-no-border-top-left-radius | Remove border radius top left |
| .fs-no-outline | Remove outline |
| .fs-transparent-25 | Apply opacity 25% |
| .fs-transparent-50 | Apply opacity 50% |
| .fs-transparent-75 | Apply opacity 75% |

## Cursor and mouse

Classes that changes appearance cursor and mouse

| Name | Description |
| --- | --- |
| .fs-cursor-pointer | Insert cursor: pointer |
| .fs-cursor-default | Insert cursor: default |
| .fs-cursor-crosshair | Insert cursor: crosshair |
| .fs-cursor-move | Insert cursor: move |
| .fs-cursor-help | Insert cursor: help |
| .fs-cursor-wait | Insert cursor: wait |
| .fs-cursor-inherit | Insert cursor: inherit |
| .fs-cursor-text | Insert cursor: text |
| .fs-cursor-progress | Insert cursor: progress |
| .fs-cursor-grab | Insert cursor: grag |
| .fs-cursor-grabbing | Insert cursor: grabbing |
| .fs-cursor-not-allowed | Insert cursor: not-allowed |

## Colors

Classes that changes background colors and text colors

| Name | Description |
| --- | --- |
| .fs-bg-white | Insert white background color |
| .fs-bg-black | Insert black background color |
| .fs-bg-gray | Insert gray background color |
| .fs-bg-danger | Insert danger background color |
| .fs-bg-info | Insert info background color |
| .fs-bg-warning | Insert warning background color |
| .fs-bg-success | Insert success background color |
| .fs-color-white | Insert white color to text |
| .fs-color-black | Insert black color to text |
| .fs-color-gray | Insert gray color to text |
| .fs-color-danger | Insert danger color to text |
| .fs-color-info | Insert info color to text |
| .fs-color-warning | Insert warning color to text |
| .fs-color-success | Insert success color to text |

## Forms and inputs

Classes that changes form elements

| Name | Description |
| --- | --- |
| .fs-no-style-input | Remove all styles of input |
| .fs-no-spin | Remove the arrows to input at type number |

## General

General classes

| Name | Description |
| --- | --- |
| .fs-break-text | Force text wrap, even when there is no spacing between words. |
| .fs-text-access | Class that hides text, but it is accessible to screen readers. |
| .fs-pointer-events-none | Insert pointer-events: none |

## Responsive classes

|  | Extra small devices Phones (<768px) | Small devices Tablets (≥768px) | Medium devices Desktops (≥992px) | Large devices Desktops (≥1200px) |
| --- | --- | --- | --- | --- |
| `.fs-xs-*` | Apply classes at the breakpoint | Default behavior | Default behavior | Default behavior |
| `.fs-sm-*` | Default behavior | Apply classes at the breakpoint | Default behavior | Default behavior |
| `.fs-md-*` | Default behavior | Default behavior | Apply classes at the breakpoint | Default behavior |
| `.fs-lg-*` | Default behavior | Default behavior | Default behavior | Apply classes at the breakpoint |

| Group of responsive classes | CSS |
| --- | --- |
| `.fs-*-no-float` | `float: none;` |
| `.fs-*-float-right` | `float: right;` |
| `.fs-*-float-left` | `float: left;` |
| `.fs-*-clear-both` | `clear: both;` |
| `.fs-*-clear-right` | `clear: right;` |
| `.fs-*-clear-left` | `clear: left;` |
| `.fs-*-display-flex` | `display: flex;` |
| `.fs-*-display-inline-flex` | `display: inline-flex;` |
| `.fs-*-display-grid` | `display: grid;` |
| `.fs-*-full-width` | `width: 100%;` |
| `.fs-*-width-auto` | `width: auto;` |
| `.fs-*-max-full-width` | `max-width: 100%;` |
| `.fs-*-half-width` | `width: 50%;` |
| `.fs-*-one-third-width` | `width: 33.333333%;` |
| `.fs-*-one-fourth-width` | `width: 25%;` |
| `.fs-*-one-fifth-width` | `width: 20%;` |
| `.fs-*-one-sixth-width` | `width: 16.666667%;` |
| `.fs-*-text-left` | `text-align: left;` |
| `.fs-*-text-right` | `text-align: right;` |
| `.fs-*-text-justify` | `text-align: justify;` |
| `.fs-*-text-center` | `text-align: center;` |
| `.fs-*-text-middle` | `vertical-align: middle;` |
| `.fs-*-no-border` | `border: none;` |
| `.fs-*-no-border-right` | `border-right: none;` |
| `.fs-*-no-border-left` | `border-left: none;` |
| `.fs-*-no-border-bottom` | `border-bottom: none;` |
| `.fs-*-no-border-top` | `border-top: none;` |
| `.fs-*-font-10` | `font-size: 10px;` |
| `.fs-*-font-12` | `font-size: 12px;` |
| `.fs-*-font-14` | `font-size: 14px;` |
| `.fs-*-font-16` | `font-size: 16px;` |
| `.fs-*-font-18` | `font-size: 18px;` |
| `.fs-*-no-margin` | `margin: 0;` |
| `.fs-*-no-margin-left` | `margin-left: 0;` |
| `.fs-*-no-margin-right` | `margin-right: 0;` |
| `.fs-*-no-margin-top` | `margin-top: 0;` |
| `.fs-*-no-margin-bottom` | `margin-bottom: 0;` |
| `.fs-*-no-padding` | `padding: 0;` |
| `.fs-*-no-padding-left` | `padding-left: 0;` |
| `.fs-*-no-padding-right` | `padding-right: 0;` |
| `.fs-*-no-padding-top` | `padding-top: 0;` |
| `.fs-*-no-padding-bottom` | `padding-bottom: 0;` |
| `.fs-*-align-items-center` | `align-items: center;` |
| `.fs-*-align-items-start` | `align-items: start;` |
| `.fs-*-align-items-end` | `align-items: end;` |
| `.fs-*-justify-content-center` | `justify-content: center;` |
| `.fs-*-justify-content-left` | `justify-content: left;` |
| `.fs-*-justify-content-right` | `justify-content: right;` |
| `.fs-*-justify-content-space-between` | `justify-content: space-between;` |
| `.fs-*-justify-content-space-around` | `justify-content: space-around;` |
| `.fs-*-justify-content-flex-start` | `justify-content: flex-start;` |
| `.fs-*-justify-content-flex-end` | `justify-content: flex-end;` |
| `.fs-*-flex-wrap-nowrap` | `flex-wrap: nowrap;` |
| `.fs-*-flex-wrap-wrap` | `flex-wrap: wrap;` |
| `.fs-*-flex-direction-column` | `flex-direction: column;` |
