import streamlit as st
import json
import pandas as pd
#%%
st.set_page_config(
    layout="wide",
)
#%%
st.write( '# Injecteur de Sort (FR) Prototype' )


#%%
dfSpell = pd.read_csv('spell.csv')
dfSpell = dfSpell.fillna('')
# dfSpell = dfSpell.replace('cantrip','0')
def ajoutSpellDf( df, spellName ):
    
    row = dfSpell[dfSpell['name'] == spellName].iloc[0]


    globalIndicator=''.join(spellName.split())
    
    roll_content = '@{wtype}&{template:spell} {{level=@{spellschool} ?{Cast at what level? @{spelllevel}}}} {{name=@{spellname}}} {{castingtime=@{spellcastingtime}}} {{range=@{spellrange}}} {{target=@{spelltarget}}} @{spellcomp_v} @{spellcomp_s} @{spellcomp_m} {{material=@{spellcomp_materials}}} {{duration=@{spellduration}}} {{description=@{spelldescription}}} {{athigherlevels=@{spellathigherlevels}}} @{spellritual} {{innate=@{innate}}} {{savedc=@{spell_save_dc}}} @{spellconcentration} @{charname_output}'

    textTemplate = [
        {'name':'repeating_spell-'+row['level']+'_-'+globalIndicator+'_spellname',          'current':row['namesFR'],    'max':'','id':'-'+globalIndicator+'SpellName'}, # spell name
        {'name':'repeating_spell-'+row['level']+'_-'+globalIndicator+'_spellschool',        'current':row['school'],   'max':'','id':'-'+globalIndicator+'spellschool'}, # source ~ Race / Feat / Class ...
        {'name':'repeating_spell-'+row['level']+'_-'+globalIndicator+'_spellcastingtime',   'current':row['casting_time'],   'max':'','id':'-'+globalIndicator+'spellcastingtime'}, # source text
        {'name':'repeating_spell-'+row['level']+'_-'+globalIndicator+'_spellrange',         'current':row['range'],'max':'','id':'-'+globalIndicator+'range'}, # flag > let it to 0
        {'name':'repeating_spell-'+row['level']+'_-'+globalIndicator+'_spelltarget',        'current':"",'max':'','id':'-'+globalIndicator+'target'}, # flag > let it to 0
        
        # {'name':'repeating_spell-'+row['level']+'_-'+globalIndicator+'_spellcomp_materials','current':descri,   'max':'','id':'-'+globalIndicator+'Descri'}, # text
        {'name':'repeating_spell-'+row['level']+'_-'+globalIndicator+'_spellconcentration', 'current':'{{concentration='+str(1*('concentration' in row['duration'].lower()))+'}}',  'max':'','id':'-'+globalIndicator+'concentration'}, # spell name
        {'name':'repeating_spell-'+row['level']+'_-'+globalIndicator+'_spellduration',      'current':row['duration'],   'max':'','id':'-'+globalIndicator+'duration'}, # source ~ Race / Feat / Class ...
        # {'name':'repeating_spell-'+row['level']+'_-'+globalIndicator+'_spell_ability',      'current':SPELL ABILITY,   'max':'','id':'-'+globalIndicator+'SourceType'}, # source text
        # {'name':'repeating_spell-'+row['level']+'_-'+globalIndicator+'_roll_output_dc',     'current':str(flag),'max':'','id':'-'+globalIndicator+'Flag'}, # flag > let it to 0
        
        {'name':'repeating_spell-'+row['level']+'_-'+globalIndicator+'_innate',             'current':'',   'max':'','id':'-'+globalIndicator+'innate'}, # text
        {'name':'repeating_spell-'+row['level']+'_-'+globalIndicator+'_spelldescription',   'current':row['descrisFR'],    'max':'','id':'-'+globalIndicator+'SpellDescri'}, # spell name
        {'name':'repeating_spell-'+row['level']+'_-'+globalIndicator+'_spellathigherlevels','current':row['descrisHLFR'],   'max':'','id':'-'+globalIndicator+'SpellDescriHL'}, # source ~ Race / Feat / Class ...
        # {'name':'repeating_spell-'+row['level']+'_-'+globalIndicator+'_spellclass',         'current':row['classes'],   'max':'','id':'-'+globalIndicator+'spellClass'}, # source text
        # {'name':'repeating_spell-'+row['level']+'_-'+globalIndicator+'_spellsource',        'current':str(flag),'max':'','id':'-'+globalIndicator+'Flag'}, # flag > let it to 0
        # options-flag
        {'name':'repeating_spell-'+row['level']+'_-'+globalIndicator+'_spellcomp_materials','current':row['components.materials_needed'],   'max':'','id':'-'+globalIndicator+'materialTxr'}, # text
        {'name':'repeating_spell-'+row['level']+'_-'+globalIndicator+'_spellcomp_m',        'current':'{{m='+str(row['components.material']*1)+'}}',  'max':'','id':'-'+globalIndicator+'M'}, # spell name
        {'name':'repeating_spell-'+row['level']+'_-'+globalIndicator+'_spellcomp_s',        'current':'{{m='+str(row['components.somatic']*1)+'}}',   'max':'','id':'-'+globalIndicator+'S'}, # source ~ Race / Feat / Class ...
        {'name':'repeating_spell-'+row['level']+'_-'+globalIndicator+'_spellcomp_v',        'current':'{{m='+str(row['components.verbal']*1)+'}}',   'max':'','id':'-'+globalIndicator+'V'}, # source text
        # 1{'name':'repeating_spell-'+row['level']+'_-'+globalIndicator+'_spellsource', 'current':str(flag),'max':'','id':'-'+globalIndicator+'Flag'}, # flag > let it to 0
       
        {'name':'repeating_spell-'+row['level']+'_-'+globalIndicator+'_rollcontent',        'current':roll_content,   'max':'','id':'-'+globalIndicator+'roll_content'}, # source text
        
        {'name':'repeating_spell-'+row['level']+'_-'+globalIndicator+'_option-flag',        'current':'0',   'max':'','id':'-'+globalIndicator+'option-flag'}, # source text
       
        ]

    tmpDf = pd.DataFrame( textTemplate )   
    df = pd.concat([df,tmpDf]).reset_index(drop=True)
    
    return df

#%%
st.write( '### Fiche de personnage (il faut bien mettre les sorts quelque part)' )

fiche = st.file_uploader(label='Mettez ici le fichier .json de votre Personnage', type='json',)

if(fiche):
    st.write('yeaah une fiche')
    
    data = json.load(fiche)
        
    listOfDict = data['character']['attribs']

    st.session_state['dfJson'] = pd.DataFrame( listOfDict )
    st.session_state['dfJson']['current'] = st.session_state['dfJson']['current'].astype('str') 
    st.session_state['dfJson'] = st.session_state['dfJson'].fillna('')


#%%

# st.write( '### Filtres')

# spell levels
# st.write( '##### niveau(x) des sorts')
# c0,c1,c2,c3,c4,c5,c6,c7,c8,c9=st.columns(10)
# with c0:st.checkbox(label='Cantrips',value=True,key='Niveau Cantrips')
# with c1:st.checkbox(label='Niveau 1',value=True,key='Niveau 1')
# with c2:st.checkbox(label='Niveau 2',value=True,key='Niveau 2')
# with c3:st.checkbox(label='Niveau 3',value=True,key='Niveau 3')
# with c4:st.checkbox(label='Niveau 4',value=True,key='Niveau 4')
# with c5:st.checkbox(label='Niveau 5',value=True,key='Niveau 5')
# with c6:st.checkbox(label='Niveau 6',value=True,key='Niveau 6')
# with c7:st.checkbox(label='Niveau 7',value=True,key='Niveau 7')
# with c8:st.checkbox(label='Niveau 8',value=True,key='Niveau 8')
# with c9:st.checkbox(label='Niveau 9',value=True,key='Niveau 9')

# if 'filterLvl' not in st.session_state:
#     st.session_state['filterLvl'] = [  ]
# st.write( [ key for key in st.session_state if st.session_state[key] is True and 'Niveau' in key  ] )
#%%

# st.write( '##### classe(s) des sorts')
# c0,c1,c2,c3=st.columns(4)

# with c0:st.checkbox(label='Druide | Druid',value=True)
# with c0:st.checkbox(label='Ensorceleur/euse | Sorcerer',value=True)
# with c1:st.checkbox(label='Clerc(esse)| Cleric',value=True)
# with c1:st.checkbox(label='Rodeur/euse | Ranger',value=True)
# with c2:st.checkbox(label='Soricer(e) | Warlock',value=True)
# with c2:st.checkbox(label='Barde | Bard',value=True)
# with c3:st.checkbox(label='Paladin',value=True)
# with c3:st.checkbox(label='Magicien(ne) | Wizard',value=True)

# st.write( '##### Ecole(s) des sorts')
# c0,c1,c2,c3=st.columns(4)

# with c0:st.checkbox(label='Conjuration',value=True)
# with c0:st.checkbox(label='Abjuration',value=True)
# with c1:st.checkbox(label='Enchantment',value=True)
# with c1:st.checkbox(label='Evocation',value=True)
# with c2:st.checkbox(label='Necromancy',value=True)
# with c2:st.checkbox(label='Illusion',value=True)
# with c3:st.checkbox(label='Divination',value=True)
# with c3:st.checkbox(label='Transmutation',value=True)

# # Concentraion + V / S / M
# st.write( '##### Concentraion / Vocal / Somatique / Materiel')
# c0,c1,c2,c3=st.columns(4)
# with c0:st.checkbox(label='Concentraion',value=True)
# with c1:st.checkbox(label='Vocal',value=True)
# with c2:st.checkbox(label='Somatique',value=True)
# with c3:st.checkbox(label='Materiel',value=True)

# ['conjuration', 'abjuration', 'enchantment', 'evocation',
#        'necromancy', 'illusion', 'divination', 'transmutation']
#%%
if 'spellList' not in st.session_state:
    st.session_state['spellList'] = []

# st.session_state['spellList'] = [f"{s1} | {s2}" for s1, s2 in zip( list(dfSpell['namesFR']), list(dfSpell['name']))]

st.session_state['spellList'] = [f"{s1} | {s2} | niv. {s3} | classes : "+','.join(eval(s4)) + ' | ecole : ' + s5 + ' | comp. : '+ s6 + ' | dur. : ' + s7  for s1, s2, s3, s4, s5, s6, s7  in zip( list(dfSpell['namesFR']), list(dfSpell['name']), list(dfSpell['level']), list(dfSpell['classes']), list(dfSpell['school']), list(dfSpell['components.raw']), list(dfSpell['duration']),   )]


# st.write('### Selectionnez vos sorts ici !')
# st.write( st.session_state['spellList'])

st.multiselect( label = '### Selectionnez vos sorts ici !' , options = st.session_state['spellList'], key = 'spellSelection' )


#%%
if 'validation' not in st.session_state:
    st.session_state['validation'] = False
# if(  ):
    
st.session_state['validation'] = st.button('Faire la fiche', disabled= not ( fiche and len(st.session_state['spellSelection']) > 0 ))

#%% insertion et telechargemnt ici

if(st.session_state['validation']):
    # st.write('cest validé')

    spellEng = [ i.split('|')[1][1:-1] for i in st.session_state['spellSelection'] ]
    
    # st.write(spellEng)
    
    for s in spellEng:
        st.session_state['dfJson'] = ajoutSpellDf( st.session_state['dfJson'], s )
    
    
    
    st.session_state['dfJson'] = st.session_state['dfJson'].fillna('')
    data['character']['attribs'] = st.session_state['dfJson'].to_dict('records')
    json_string = json.dumps(data)
    
    st.download_button(
        label="Téléchargez votre personnage avec ses nouveau sorts !",
        file_name=fiche.name,
        mime="application/json",
        data=json_string,
    )

    st.write('finito')
#%% affichage des sort selectionner

def displaySpell( spellName ):
    row = dfSpell[dfSpell['name'] == spellName].iloc[0]
    
    st.write( '### '+ row['namesFR'] +' | ' + spellName )
    st.write( row['school'] + ' de niveau ' + row['level'] )
    st.write( '**Casting Time** : ' + row['casting_time']  )
    st.write( '**Range** : ' + row['range']  )
    st.write( '**Components** : ' + row['components.raw']  )
    st.write( '**Duration** : ' + row['duration']  )
    
    st.write( row['descrisFR'] )
    st.write( 'A plus haut niveau : ' + row['descrisHLFR'] )
    
    st.write( '**classes** : ' + ','.join(eval(row['classes'])) )
    
    
    
spellEng = [ i.split('|')[1][1:-1] for i in st.session_state['spellSelection'] ]

for s in spellEng:
    
    displaySpell(s)











