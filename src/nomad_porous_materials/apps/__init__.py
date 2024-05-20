from nomad.config.models.plugins import AppEntryPoint
from nomad.config.models.ui import (
    App,
    Column,
    Columns,
    Dashboard,
    FilterMenu,
    FilterMenus,
    Filters,
    Layout,
    SearchSyntaxes,
    WidgetHistogram,
    WidgetPeriodicTable,
    WidgetTerms,
)

mofapp = AppEntryPoint(
    name='MOF',
    description='App defined using the new plugin mechanism.',
    app=App(
        label='Metal-Organic Frameworks',
        path='mofs',
        description='Search metal-organic frameworks (MOFs)',
        readme="""
            This page allows you to search **metal-organic framework
            (MOF) data** within NOMAD. The filter menu on the left
            and the shown default columns are specifically designed
            for MOF exploration. The dashboard directly shows useful
            interactive statistics about the data.""",
        category='Use Cases',
        filters=Filters(exclude=['mainfile', 'entry_name', 'combine']),
        filters_locked={'results.material.topology.label': 'MOF'},
        search_syntaxes=SearchSyntaxes(exclude=['free_text']),
        columns=Columns(
            selected=['results.material.chemical_formula_iupac', 'mainfile', 'authors'],
            options={
                'results.material.chemical_formula_iupac': Column(label='Formula'),
                'mainfile': Column(),
                'upload_create_time': Column(label='Upload time'),
                'authors': Column(),
                'comment': Column(),
                'datasets': Column(),
                'published': Column(label='Access'),
            },
        ),
        filter_menus=FilterMenus(
            options={
                'material': FilterMenu(label='Material'),
                'elements': FilterMenu(
                    label='Elements / Formula',
                    level=1,
                    size='xl',
                ),
                'structure': FilterMenu(
                    label='Structure',
                    level=1,
                ),
                'electronic': FilterMenu(
                    label='Electronic Properties',
                ),
                'author': FilterMenu(
                    label='Author / Origin / Dataset',
                    size='m',
                ),
                'metadata': FilterMenu(
                    label='Visibility / IDs / Schema',
                ),
                'optimade': FilterMenu(
                    label='Optimade',
                    size='m',
                ),
            }
        ),
        dashboard=Dashboard(
            widgets=[
                WidgetPeriodicTable(
                    type='periodictable',
                    layout={
                        'lg': Layout(h=9, w=15, x=0, y=0),
                        'md': Layout(h=8, w=11, x=0, y=0),
                        'sm': Layout(h=6, w=9, x=0, y=0),
                        'xl': Layout(h=9, w=19, x=0, y=0),
                        'xxl': Layout(h=10, w=25, x=0, y=0),
                    },
                    quantity='results.material.elements',
                    scale='linear',
                ),
                WidgetTerms(
                    type='terms',
                    layout={
                        'lg': Layout(h=9, w=9, x=15, y=0),
                        'md': Layout(h=8, w=7, x=11, y=0),
                        'sm': Layout(h=6, w=3, x=9, y=0),
                        'xl': Layout(h=9, w=11, x=19, y=0),
                        'xxl': Layout(h=10, w=11, x=25, y=0),
                    },
                    quantity='results.material.topology.sbu_type',
                    scale='linear',
                    title='SBU type',
                    showinput=True,
                ),
                WidgetHistogram(
                    type='histogram',
                    layout={
                        'lg': Layout(h=5, w=12, x=0, y=9),
                        'md': Layout(h=4, w=9, x=0, y=8),
                        'sm': Layout(h=3, w=6, x=0, y=6),
                        'xl': Layout(h=5, w=15, x=0, y=9),
                        'xxl': Layout(h=6, w=19, x=0, y=10),
                    },
                    quantity='results.material.topology.pore_limiting_diameter',
                    scale='linear',
                    nbins=30,
                    showinput=True,
                ),
                WidgetHistogram(
                    type='histogram',
                    layout={
                        'lg': Layout(h=5, w=12, x=0, y=14),
                        'md': Layout(h=4, w=9, x=9, y=8),
                        'sm': Layout(h=3, w=6, x=6, y=6),
                        'xl': Layout(h=5, w=15, x=0, y=14),
                        'xxl': Layout(h=6, w=17, x=19, y=10),
                    },
                    quantity='results.material.topology.largest_cavity_diameter',
                    scale='linear',
                    nbins=30,
                    showinput=True,
                ),
                WidgetHistogram(
                    type='histogram',
                    layout={
                        'lg': Layout(h=5, w=12, x=11, y=9),
                        'md': Layout(h=4, w=9, x=0, y=12),
                        'sm': Layout(h=3, w=6, x=0, y=9),
                        'xl': Layout(h=5, w=15, x=15, y=9),
                        'xxl': Layout(h=6, w=19, x=0, y=16),
                    },
                    quantity='results.material.topology.accessible_surface_area',
                    scale='linear',
                    nbins=30,
                    showinput=True,
                ),
                WidgetHistogram(
                    type='histogram',
                    layout={
                        'lg': Layout(h=5, w=12, x=11, y=14),
                        'md': Layout(h=4, w=9, x=9, y=12),
                        'sm': Layout(h=3, w=6, x=6, y=9),
                        'xl': Layout(h=5, w=15, x=15, y=14),
                        'xxl': Layout(h=6, w=17, x=19, y=16),
                    },
                    quantity='results.material.topology.void_fraction',
                    scale='linear',
                    nbins=30,
                    showinput=True,
                ),
            ]
        ),
    ),
)
