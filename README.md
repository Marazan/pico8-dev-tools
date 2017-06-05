# pico8-dev-tools
My dev work flow to make pico-8 dev more sane.  Saner.  A little less retro.  You know what I mean.

When I write game I base them around states.  I have a global state variable that holds a table with a update and draw function so my _update and _draw methods look like

```lua
function _update()
 g_state.update()
end

function _draw()
 g_state.draw()
end
```

Each state tries to stay as self cotnained as possible, using only the barest minimum number of shared variables between them - the have optional enter() and exit() functions to setup and teardown the state as appropriate.  As a result each state is an excellent candidate for going in it's own file.

The tool combines all these states into the final cartriage as well as setting up the global table of states

I also have a library of useful functions (screen shake, screen transitions etc) thta I may or may not want to include.  Including them is controlled by the config file in the cart directory.

```

.
├── .weaver_global.json
├── carts
│   └── loa
│       └── config.json
│       └── state_menu.json
│       └── state_game.json
│       └── state_death.json
└── library
    ├── better_random.lua
    └── screendissolve.lua
```


