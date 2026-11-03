---
article_id: 360023247291
category: Ativo Fixo - Mile
content_hash: d0efb998ea99f570068c8bda82125b93156bbbc5b564b4eb90e0df85ec4de9a0
fetched_at: '2026-06-28T22:41:36.891442+00:00'
product: protheus
section_id: 1500001536661
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA012 incluir ativo
  via txt MILE '
type: support-article
updated_at: '2025-01-02T10:45:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023247291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA012-incluir-ativo-via-txt-MILE
---

**Dúvida**Como incluir um ativo via **Mile** através da rotina automática **ATFA012**?

**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial - A partir da versão 12  
  
**Solução**Siga os passos abaixo:

1- Via configurador em **Aceleradores / Mile / Layout** - criar layout de importação para rotina ATFA012, caso deseje importar um layout, pode-se utilizar o modelo:

<?xml version="1.0" encoding="UTF-8"?>

<CFGA600 version="1.01" Operation="4">

<XZ1MASTER modeltype="FIELDS">

<XZ1\_LAYOUT order="1">

<value>SN1MIR\_E</value>

</XZ1\_LAYOUT>

<XZ1\_TYPE order="2">

<value>1</value>

</XZ1\_TYPE>

<XZ1\_DESC order="3">

<value>ATIVO IMOBILIZADO (ERP)</value>

</XZ1\_DESC>

<XZ1\_ADAPT order="4">

<value>ATFA012</value>

</XZ1\_ADAPT>

<XZ1\_STRUC order="5">

<value>2</value>

</XZ1\_STRUC>

<XZ1\_SEPARA order="6">

<value>;</value>

</XZ1\_SEPARA>

<XZ1\_SEPINASP order="7">

<value>2</value>

</XZ1\_SEPINASP>

<XZ1\_TYPEXA order="8">

<value>3</value>

</XZ1\_TYPEXA>

<XZ1\_SEPINI order="9">

<value>2</value>

</XZ1\_SEPINI>

<XZ1\_SEPFIN order="10">

<value>2</value>

</XZ1\_SEPFIN>

<XZ1\_TABLE order="11">

<value>SN1</value>

</XZ1\_TABLE>

<XZ1\_DESTAB order="12">

<value>Ativo Imobilizado</value>

</XZ1\_DESTAB>

<XZ1\_ORDER order="13">

<value>1</value>

</XZ1\_ORDER>

<XZ1\_SOURCE order="14">

<value>0001</value>

</XZ1\_SOURCE>

<XZ1\_TIPDAT order="18">

<value>1</value>

</XZ1\_TIPDAT>

<XZ1\_DECSEP order="19">

<value>1</value>

</XZ1\_DECSEP>

<XZ1\_EMULTC order="20">

<value>1</value>

</XZ1\_EMULTC>

<XZ1\_DETOPC order="21">

<value>2</value>

</XZ1\_DETOPC>

<XZ1\_IMPEXP order="23">

<value>1</value>

</XZ1\_IMPEXP>

<XZ1\_VERSIO order="24">

<value>1.0</value>

</XZ1\_VERSIO>

<XZ1\_MVCOPT order="25">

<value>1</value>

</XZ1\_MVCOPT>

<XZ1\_MVCMET order="26">

<value>1</value>

</XZ1\_MVCMET>

<XZ1\_NOCACHEMOD order="27">

<value>2</value>

</XZ1\_NOCACHEMOD>

<XZ2DETAIL modeltype="GRID">

<struct>

<XZ2\_LAYOUT order="1"/>

<XZ2\_SEQ order="2"/>

<XZ2\_CHANEL order="3"/>

<XZ2\_SUPER order="4"/>

</struct>

<items>

<item deleted="0" id="1">

<XZ2\_LAYOUT>SN1BRA</XZ2\_LAYOUT>

<XZ2\_SEQ>01</XZ2\_SEQ>

<XZ2\_CHANEL>SN1</XZ2\_CHANEL>

<XZ3DETAIL modeltype="FIELDS">

<XZ3\_CHANEL order="2">

<value>SN1</value>

</XZ3\_CHANEL>

<XZ3\_DESC order="3">

<value>SN1</value>

</XZ3\_DESC>

<XZ3\_IDOUT order="4">

<value>MASTER</value>

</XZ3\_IDOUT>

<XZ3\_OCCURS order="5">

<value>1</value>

</XZ3\_OCCURS>

</XZ3DETAIL>

<XZ4DETAIL modeltype="GRID" optional="1">

<struct>

<XZ4\_LAYOUT order="1"/>

<XZ4\_CHANEL order="2"/>

<XZ4\_SEQ order="3"/>

<XZ4\_FIELD order="4"/>

<XZ4\_TYPFLD order="5"/>

<XZ4\_EXEC order="6"/>

<XZ4\_COND order="7"/>

<XZ4\_NOVAL order="8"/>

<XZ4\_DESC order="9"/>

<XZ4\_OBS order="10"/>

<XZ4\_SOURCE order="11"/>

</struct>

<items>

<item deleted="0" id="1">

<XZ4\_SEQ>001</XZ4\_SEQ>

<XZ4\_FIELD>N1\_GRUPO</XZ4\_FIELD>

<XZ4\_TYPFLD>C</XZ4\_TYPFLD>

<XZ4\_NOVAL>2</XZ4\_NOVAL>

<XZ4\_DESC>Grupo do Bem</XZ4\_DESC>

<XZ4\_SOURCE>0002</XZ4\_SOURCE>

</item>

<item deleted="0" id="2">

<XZ4\_SEQ>002</XZ4\_SEQ>

<XZ4\_FIELD>N1\_CBASE</XZ4\_FIELD>

<XZ4\_TYPFLD>C</XZ4\_TYPFLD>

<XZ4\_NOVAL>2</XZ4\_NOVAL>

<XZ4\_DESC>(\*)Codigo Base do Bem</XZ4\_DESC>

<XZ4\_SOURCE>0003</XZ4\_SOURCE>

</item>

<item deleted="0" id="3">

<XZ4\_SEQ>003</XZ4\_SEQ>

<XZ4\_FIELD>N1\_ITEM</XZ4\_FIELD>

<XZ4\_TYPFLD>C</XZ4\_TYPFLD>

<XZ4\_NOVAL>2</XZ4\_NOVAL>

<XZ4\_DESC>(\*)Numero do Item</XZ4\_DESC>

<XZ4\_SOURCE>0004</XZ4\_SOURCE>

</item>

<item deleted="0" id="4">

<XZ4\_SEQ>004</XZ4\_SEQ>

<XZ4\_FIELD>N1\_AQUISIC</XZ4\_FIELD>

<XZ4\_TYPFLD>D</XZ4\_TYPFLD>

<XZ4\_NOVAL>2</XZ4\_NOVAL>

<XZ4\_DESC>(\*)Data de Aquisicao</XZ4\_DESC>

<XZ4\_SOURCE>0005</XZ4\_SOURCE>

</item>

<item deleted="0" id="5">

<XZ4\_SEQ>005</XZ4\_SEQ>

<XZ4\_FIELD>N1\_QUANTD</XZ4\_FIELD>

<XZ4\_TYPFLD>N</XZ4\_TYPFLD>

<XZ4\_NOVAL>2</XZ4\_NOVAL>

<XZ4\_DESC>Quantidade do Bem</XZ4\_DESC>

<XZ4\_SOURCE>0006</XZ4\_SOURCE>

</item>

<item deleted="0" id="6">

<XZ4\_SEQ>006</XZ4\_SEQ>

<XZ4\_FIELD>N1\_DESCRIC</XZ4\_FIELD>

<XZ4\_TYPFLD>C</XZ4\_TYPFLD>

<XZ4\_NOVAL>2</XZ4\_NOVAL>

<XZ4\_DESC>(\*)Descricao Sintetica</XZ4\_DESC>

<XZ4\_SOURCE>0007</XZ4\_SOURCE>

</item>

<item deleted="0" id="7">

<XZ4\_SEQ>007</XZ4\_SEQ>

<XZ4\_FIELD>N1\_CHAPA</XZ4\_FIELD>

<XZ4\_TYPFLD>C</XZ4\_TYPFLD>

<XZ4\_NOVAL>2</XZ4\_NOVAL>

<XZ4\_DESC>Numero da Plaqueta</XZ4\_DESC>

<XZ4\_SOURCE>0008</XZ4\_SOURCE>

</item>

<item deleted="0" id="8">

<XZ4\_SEQ>008</XZ4\_SEQ>

<XZ4\_FIELD>N1\_FORNEC</XZ4\_FIELD>

<XZ4\_TYPFLD>C</XZ4\_TYPFLD>

<XZ4\_NOVAL>2</XZ4\_NOVAL>

<XZ4\_DESC>Codigo do Fornecedor</XZ4\_DESC>

<XZ4\_SOURCE>0009</XZ4\_SOURCE>

</item>

<item deleted="0" id="9">

<XZ4\_SEQ>013</XZ4\_SEQ>

<XZ4\_FIELD>N1\_LOJA</XZ4\_FIELD>

<XZ4\_TYPFLD>C</XZ4\_TYPFLD>

<XZ4\_NOVAL>2</XZ4\_NOVAL>

<XZ4\_DESC>Loja do Fornecedor</XZ4\_DESC>

<XZ4\_SOURCE>0010</XZ4\_SOURCE>

</item>

<item deleted="0" id="10">

<XZ4\_SEQ>014</XZ4\_SEQ>

<XZ4\_FIELD>N1\_NSERIE</XZ4\_FIELD>

<XZ4\_TYPFLD>C</XZ4\_TYPFLD>

<XZ4\_NOVAL>2</XZ4\_NOVAL>

<XZ4\_DESC>Serie da Nota Fiscal</XZ4\_DESC>

<XZ4\_SOURCE>0011</XZ4\_SOURCE>

</item>

<item deleted="0" id="11">

<XZ4\_SEQ>015</XZ4\_SEQ>

<XZ4\_FIELD>N1\_NFISCAL</XZ4\_FIELD>

<XZ4\_TYPFLD>C</XZ4\_TYPFLD>

<XZ4\_NOVAL>2</XZ4\_NOVAL>

<XZ4\_DESC>Numero da Nota Fiscal</XZ4\_DESC>

<XZ4\_SOURCE>0012</XZ4\_SOURCE>

</item>

-<item deleted="0" id="12">

<XZ4\_SEQ>016</XZ4\_SEQ>

<XZ4\_FIELD>N1\_DTBLOQ</XZ4\_FIELD>

<XZ4\_TYPFLD>D</XZ4\_TYPFLD>

<XZ4\_NOVAL>2</XZ4\_NOVAL>

<XZ4\_DESC>Data para bloqueio</XZ4\_DESC>

<XZ4\_SOURCE>0013</XZ4\_SOURCE>

</item>

</items>

</XZ4DETAIL>

<XZ5DETAIL modeltype="GRID" optional="1">

<struct>

<XZ5\_LAYOUT order="1"/>

<XZ5\_CHANEL order="2"/>

<XZ5\_SEQ order="3"/>

<XZ5\_FIELD order="4"/>

<XZ5\_TYPFLD order="5"/>

<XZ5\_EXEC order="6"/>

<XZ5\_COND order="7"/>

<XZ5\_OBS order="8"/>

<XZ5\_SOURCE order="9"/>

</struct>

</XZ5DETAIL>

</item>

<item deleted="0" id="2">

<XZ2\_SEQ>02</XZ2\_SEQ>

<XZ2\_CHANEL>SN3</XZ2\_CHANEL>

<XZ2\_SUPER>SN1</XZ2\_SUPER>

<XZ3DETAIL modeltype="FIELDS">

<XZ3\_CHANEL order="2">

<value>SN3</value>

</XZ3\_CHANEL>

<XZ3\_DESC order="3">

<value>CANAL SN3</value>

</XZ3\_DESC>

<XZ3\_IDOUT order="4">

<value>DETAIL</value>

</XZ3\_IDOUT>

<XZ3\_OCCURS order="5">

<value>N</value>

</XZ3\_OCCURS>

</XZ3DETAIL>

<XZ4DETAIL modeltype="GRID" optional="1">

<struct>

<XZ4\_LAYOUT order="1"/>

<XZ4\_CHANEL order="2"/>

<XZ4\_SEQ order="3"/>

<XZ4\_FIELD order="4"/>

<XZ4\_TYPFLD order="5"/>

<XZ4\_EXEC order="6"/>

<XZ4\_COND order="7"/>

<XZ4\_NOVAL order="8"/>

<XZ4\_DESC order="9"/>

<XZ4\_OBS order="10"/>

<XZ4\_SOURCE order="11"/>

</struct>

<items>

<item deleted="0" id="1">

<XZ4\_SEQ>001</XZ4\_SEQ>

<XZ4\_FIELD>N3\_TIPO</XZ4\_FIELD>

<XZ4\_TYPFLD>C</XZ4\_TYPFLD>

<XZ4\_NOVAL>2</XZ4\_NOVAL>

<XZ4\_DESC>(\*)Tipo do Ativo</XZ4\_DESC>

<XZ4\_SOURCE>0002</XZ4\_SOURCE>

</item>

<item deleted="0" id="2">

<XZ4\_SEQ>002</XZ4\_SEQ>

<XZ4\_FIELD>N3\_HISTOR</XZ4\_FIELD>

<XZ4\_TYPFLD>C</XZ4\_TYPFLD>

<XZ4\_NOVAL>2</XZ4\_NOVAL>

<XZ4\_DESC>(\*)Historico do Valor</XZ4\_DESC>

<XZ4\_SOURCE>0003</XZ4\_SOURCE>

</item>

<item deleted="0" id="3">

<XZ4\_SEQ>003</XZ4\_SEQ>

<XZ4\_FIELD>N3\_TPDEPR</XZ4\_FIELD>

<XZ4\_TYPFLD>C</XZ4\_TYPFLD>

<XZ4\_NOVAL>2</XZ4\_NOVAL>

<XZ4\_DESC>Tipo de depreciacao</XZ4\_DESC>

<XZ4\_SOURCE>0004</XZ4\_SOURCE>

</item>

<item deleted="0" id="4">

<XZ4\_SEQ>004</XZ4\_SEQ>

<XZ4\_FIELD>N3\_CUSTBEM</XZ4\_FIELD>

<XZ4\_TYPFLD>C</XZ4\_TYPFLD>

<XZ4\_NOVAL>2</XZ4\_NOVAL>

<XZ4\_DESC>C Custo da Conta do Bem</XZ4\_DESC>

<XZ4\_SOURCE>0005</XZ4\_SOURCE>

</item>

<item deleted="0" id="5">

<XZ4\_SEQ>006</XZ4\_SEQ>

<XZ4\_FIELD>N3\_CCONTAB</XZ4\_FIELD>

<XZ4\_TYPFLD>C</XZ4\_TYPFLD>

<XZ4\_NOVAL>2</XZ4\_NOVAL>

<XZ4\_DESC>(\*)Conta Contabil</XZ4\_DESC>

<XZ4\_SOURCE>0006</XZ4\_SOURCE>

</item>

<item deleted="0" id="6">

<XZ4\_SEQ>007</XZ4\_SEQ>

<XZ4\_FIELD>N3\_CDEPREC</XZ4\_FIELD>

<XZ4\_TYPFLD>C</XZ4\_TYPFLD>

<XZ4\_NOVAL>2</XZ4\_NOVAL>

<XZ4\_DESC>Conta Despesa Depreciacao</XZ4\_DESC>

<XZ4\_SOURCE>0007</XZ4\_SOURCE>

</item>

<item deleted="0" id="7">

<XZ4\_SEQ>008</XZ4\_SEQ>

<XZ4\_FIELD>N3\_CCUSTO</XZ4\_FIELD>

<XZ4\_TYPFLD>C</XZ4\_TYPFLD>

<XZ4\_NOVAL>2</XZ4\_NOVAL>

<XZ4\_DESC>Centro de Custo Despesa</XZ4\_DESC>

<XZ4\_SOURCE>0008</XZ4\_SOURCE>

</item>

<item deleted="0" id="8">

<XZ4\_SEQ>009</XZ4\_SEQ>

<XZ4\_FIELD>N3\_CCDEPR</XZ4\_FIELD>

<XZ4\_TYPFLD>C</XZ4\_TYPFLD>

<XZ4\_NOVAL>2</XZ4\_NOVAL>

<XZ4\_DESC>Conta Deprec. Acumulada</XZ4\_DESC>

<XZ4\_SOURCE>0009</XZ4\_SOURCE>

</item>

<item deleted="0" id="9">

<XZ4\_SEQ>010</XZ4\_SEQ>

<XZ4\_FIELD>N3\_DINDEPR</XZ4\_FIELD>

<XZ4\_TYPFLD>D</XZ4\_TYPFLD>

<XZ4\_NOVAL>2</XZ4\_NOVAL>

<XZ4\_DESC>(\*)Data Inicio depreciaca</XZ4\_DESC>

<XZ4\_SOURCE>0010</XZ4\_SOURCE>

</item>

<item deleted="0" id="10">

<XZ4\_SEQ>013</XZ4\_SEQ>

<XZ4\_FIELD>N3\_VORIG1</XZ4\_FIELD>

<XZ4\_TYPFLD>N</XZ4\_TYPFLD>

<XZ4\_NOVAL>2</XZ4\_NOVAL>

<XZ4\_DESC>Valor Original Moeda 1</XZ4\_DESC>

<XZ4\_SOURCE>0011</XZ4\_SOURCE>

</item>

<item deleted="0" id="11">

<XZ4\_SEQ>014</XZ4\_SEQ>

<XZ4\_FIELD>N3\_TXDEPR1</XZ4\_FIELD>

<XZ4\_TYPFLD>N</XZ4\_TYPFLD>

<XZ4\_NOVAL>2</XZ4\_NOVAL>

<XZ4\_DESC>Taxa Anual Depreciacao 1</XZ4\_DESC>

<XZ4\_SOURCE>0012</XZ4\_SOURCE>

</item>

<item deleted="0" id="12">

<XZ4\_SEQ>027</XZ4\_SEQ>

<XZ4\_FIELD>N3\_VRDACM1</XZ4\_FIELD>

<XZ4\_TYPFLD>N</XZ4\_TYPFLD>

<XZ4\_NOVAL>2</XZ4\_NOVAL>

<XZ4\_DESC>Deprecia Acumulada Moeda1</XZ4\_DESC>

<XZ4\_SOURCE>0013</XZ4\_SOURCE>

</item>

<item deleted="0" id="13">

<XZ4\_SEQ>040</XZ4\_SEQ>

<XZ4\_FIELD>N3\_AQUISIC</XZ4\_FIELD>

<XZ4\_TYPFLD>D</XZ4\_TYPFLD>

<XZ4\_NOVAL>2</XZ4\_NOVAL>

<XZ4\_DESC>Data Aquisicao Original</XZ4\_DESC>

<XZ4\_SOURCE>0014</XZ4\_SOURCE>

</item>

</items>

</XZ4DETAIL>

<XZ5DETAIL modeltype="GRID" optional="1">

<struct>

<XZ5\_LAYOUT order="1"/>

<XZ5\_CHANEL order="2"/>

<XZ5\_SEQ order="3"/>

<XZ5\_FIELD order="4"/>

<XZ5\_TYPFLD order="5"/>

<XZ5\_EXEC order="6"/>

<XZ5\_COND order="7"/>

<XZ5\_OBS order="8"/>

<XZ5\_SOURCE order="9"/>

</struct>

</XZ5DETAIL>

</item>

</items>

</XZ2DETAIL>

</XZ1MASTER>

</CFGA600>

2-Criar o arquivo texto conforme o layout utilizado, ex:

-Para o layout acima, criamos o **canal SN1 e SN3**, pertencendo as saídas **MASTER e DETAIL respectivamente**,  sendo assim, o seu arquivo texto poderia ser da seguinte forma:

SN1;0001;V000000037;0001;02/01/15;1;FOCUSTITANIUM2.0;V0000000000000000037;;;;;  
SN3;01;FOCUSTITANIUM2.0;1;;1120201003;4110103001;;1120201010;02/01/15;65990;20;;02/01/15

3-Na própria rotina do **MILE** executar Processamento de TXT informando o layout e o nome do arquivo a ser importado.

4-Entrar na rotina **ATFA012** e verificar se o Bem foi cadastrado.

**OBS: Os exemplos acima podem ser utilizados para testes, porém o cliente deve ajustar o layout e arquivo conforme a sua necessidade e lembrando de preencher todos os campos considerados obrigatórios em sua base.**

SAIBA MAIS: <http://tdn.totvs.com/display/public/PROT/CTB0075_COMO_INCLUIR_LCTO_CONTABIL_VIA_MILE_ROT_AUT_CTBA102>

[Manual MILE Model Integrator Layout Engine](https://tdn.totvs.com/display/public/framework/MILE+-+Model+Integrator+Layout+Engine)

[MILE - Model Integrator Layout Engine](http://tdn.totvs.com/display/framework/MILE+-+Model+Integrator+Layout+Engine)
