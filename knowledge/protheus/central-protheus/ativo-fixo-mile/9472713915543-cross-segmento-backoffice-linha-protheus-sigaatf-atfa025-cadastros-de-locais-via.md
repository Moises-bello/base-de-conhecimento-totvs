---
article_id: 9472713915543
category: Ativo Fixo - Mile
content_hash: 03d02f623ba7e03f8440e8894fac05262c3a575961adf5132331f0827fe44f6e
fetched_at: '2026-06-28T22:41:36.949976+00:00'
product: protheus
section_id: 1500001536661
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA025 - Cadastros
  de locais via Mile
type: support-article
updated_at: '2025-01-03T17:38:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9472713915543-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA025-Cadastros-de-locais-via-Mile
---

**Dúvida**Como incluir Locais via MILE ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Ativo Fixo - A partir da versão 12  
  
**Solução**

Para incluir os Locais via MILE, siga os passos abaixo:

**1-** Via configurador em **Aceleradores / Mile / Layout** - criar layout de importação para rotina ATFA025, caso deseje importar um layout, pode-se utilizar o modelo abaixo:

<CFGA600Operation="4"version="1.01">

<XZ1MASTERmodeltype="FIELDS">

<XZ1\_LAYOUTorder="1">

<value>ATFA025\_</value>

</XZ1\_LAYOUT>

<XZ1\_TYPEorder="2">

<value>2</value>

</XZ1\_TYPE>

<XZ1\_DESCorder="3">

<value>INCLUSÃO DE LOCAIS MILE ATFA025</value>

</XZ1\_DESC>

<XZ1\_ADAPTorder="4">

<value>ATFA025</value>

</XZ1\_ADAPT>

<XZ1\_STRUCorder="5">

<value>2</value>

</XZ1\_STRUC>

<XZ1\_SEPARAorder="6">

<value>;</value>

</XZ1\_SEPARA>

<XZ1\_SEPINASPorder="7">

<value>2</value>

</XZ1\_SEPINASP>

<XZ1\_TYPEXAorder="8">

<value>1</value>

</XZ1\_TYPEXA>

<XZ1\_SEPINIorder="9">

<value>2</value>

</XZ1\_SEPINI>

<XZ1\_SEPFINorder="10">

<value>2</value>

</XZ1\_SEPFIN>

<XZ1\_TABLEorder="11">

<value>SNL</value>

</XZ1\_TABLE>

<XZ1\_DESTABorder="12">

<value>Cadastro de Locais</value>

</XZ1\_DESTAB>

<XZ1\_ORDERorder="13">

<value>1</value>

</XZ1\_ORDER>

<XZ1\_TIPDATorder="18">

<value>1</value>

</XZ1\_TIPDAT>

<XZ1\_DECSEPorder="19">

<value>1</value>

</XZ1\_DECSEP>

<XZ1\_EMULTCorder="20">

<value>2</value>

</XZ1\_EMULTC>

<XZ1\_DETOPCorder="21">

<value>2</value>

</XZ1\_DETOPC>

<XZ1\_IMPEXPorder="23">

<value>1</value>

</XZ1\_IMPEXP>

<XZ1\_VERSIOorder="24">

<value>1.0</value>

</XZ1\_VERSIO>

<XZ1\_MVCOPTorder="25">

<value>1</value>

</XZ1\_MVCOPT>

<XZ1\_MVCMETorder="26">

<value>1</value>

</XZ1\_MVCMET>

<XZ1\_NOCACHEMODorder="27">

<value>2</value>

</XZ1\_NOCACHEMOD>

<XZ2DETAILmodeltype="GRID">

<struct>

<XZ2\_LAYOUTorder="1"/>

<XZ2\_SEQorder="2"/>

<XZ2\_CHANELorder="3"/>

<XZ2\_SUPERorder="4"/>

</struct>

<items>

<itemid="1"deleted="0">

<XZ2\_SEQ>01</XZ2\_SEQ>

<XZ2\_CHANEL>SNLMASTER</XZ2\_CHANEL>

<XZ3DETAILmodeltype="FIELDS">

<XZ3\_CHANELorder="2">

<value>SNLMASTER</value>

</XZ3\_CHANEL>

<XZ3\_DESCorder="3">

<value>CANAL SNLMASTER</value>

</XZ3\_DESC>

<XZ3\_IDOUTorder="4">

<value>SNLMASTER</value>

</XZ3\_IDOUT>

<XZ3\_OCCURSorder="5">

<value>1</value>

</XZ3\_OCCURS>

</XZ3DETAIL>

<XZ4DETAILmodeltype="GRID"optional="1">

<struct>

<XZ4\_LAYOUTorder="1"/>

<XZ4\_CHANELorder="2"/>

<XZ4\_SEQorder="3"/>

<XZ4\_FIELDorder="4"/>

<XZ4\_TYPFLDorder="5"/>

<XZ4\_EXECorder="6"/>

<XZ4\_CONDorder="7"/>

<XZ4\_NOVALorder="8"/>

<XZ4\_DESCorder="9"/>

<XZ4\_OBSorder="10"/>

<XZ4\_SOURCEorder="11"/>

</struct>

<items>

<itemid="1"deleted="0">

<XZ4\_SEQ>001</XZ4\_SEQ>

<XZ4\_FIELD>NL\_CODIGO</XZ4\_FIELD>

<XZ4\_TYPFLD>N</XZ4\_TYPFLD>

<XZ4\_NOVAL>2</XZ4\_NOVAL>

<XZ4\_DESC>Codigo do Local</XZ4\_DESC>

<XZ4\_SOURCE>0001</XZ4\_SOURCE>

</item>

<itemid="2"deleted="0">

<XZ4\_SEQ>002</XZ4\_SEQ>

<XZ4\_FIELD>NL\_FILIAL</XZ4\_FIELD>

<XZ4\_NOVAL>2</XZ4\_NOVAL>

<XZ4\_DESC>Filial do Sistema</XZ4\_DESC>

<XZ4\_SOURCE>0002</XZ4\_SOURCE>

</item>

<itemid="3"deleted="0">

<XZ4\_SEQ>003</XZ4\_SEQ>

<XZ4\_FIELD>NL\_DESCRIC</XZ4\_FIELD>

<XZ4\_NOVAL>2</XZ4\_NOVAL>

<XZ4\_DESC>Descricao do local</XZ4\_DESC>

<XZ4\_SOURCE>0003</XZ4\_SOURCE>

</item>

<itemid="4"deleted="0">

<XZ4\_SEQ>004</XZ4\_SEQ>

<XZ4\_FIELD>NL\_TIPOLOC</XZ4\_FIELD>

<XZ4\_NOVAL>2</XZ4\_NOVAL>

<XZ4\_DESC>Tipo do local</XZ4\_DESC>

<XZ4\_SOURCE>0004</XZ4\_SOURCE>

</item>

<itemid="5"deleted="0">

<XZ4\_SEQ>005</XZ4\_SEQ>

<XZ4\_FIELD>NL\_BLOQ</XZ4\_FIELD>

<XZ4\_NOVAL>2</XZ4\_NOVAL>

<XZ4\_DESC>Bloqueio</XZ4\_DESC>

<XZ4\_SOURCE>0005</XZ4\_SOURCE>

</item>

</items>

</XZ4DETAIL>

<XZ5DETAILmodeltype="GRID"optional="1">

<struct>

<XZ5\_LAYOUTorder="1"/>

<XZ5\_CHANELorder="2"/>

<XZ5\_SEQorder="3"/>

<XZ5\_FIELDorder="4"/>

<XZ5\_TYPFLDorder="5"/>

<XZ5\_EXECorder="6"/>

<XZ5\_CONDorder="7"/>

<XZ5\_OBSorder="8"/>

<XZ5\_SOURCEorder="9"/>

</struct>

</XZ5DETAIL>

</item>

</items>

</XZ2DETAIL>

</XZ1MASTER>

</CFGA600>

**OBS:** Deverá salvar o arquivo do modelo em XML.

**2-**Criar o arquivo texto conforme o layout utilizado, no modelo acima podemos usar o seguinte TXT:

0001;01;Descricao;1;2;

Segue a relação de qual campo cada valor do exemplo se refere:

0001(NL\_CODIGO);

01(NL\_FILIAL);

Descricao(NL\_DESCRI);

1(NL\_TIPOLOC);

2(NL\_BLOC);

**3-** Na própria rotina do **MILE** executar Processamento de TXT informando o layout e o nome do arquivo a ser importado.

**4-** Entrar na rotina ATFA025 e verificar se a conta foi importada corretamente.

**OBS: Os exemplos acima podem ser utilizados para testes, porém o cliente deve ajustar o layout e arquivo conforme a sua necessidade e lembrando de preencher todos os campos considerados obrigatórios em sua base.**

**Saiba Mais:**

[MILE - Model Integrator Layout Engine](http://tdn.totvs.com/display/framework/MILE+-+Model+Integrator+Layout+Engine)
