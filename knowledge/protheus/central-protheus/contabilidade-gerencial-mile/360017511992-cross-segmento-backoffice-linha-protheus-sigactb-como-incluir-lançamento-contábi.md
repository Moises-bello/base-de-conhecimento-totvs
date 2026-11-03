---
article_id: 360017511992
category: Contabilidade Gerencial - Mile
content_hash: 2c47451e986625d7aaf8cf36677bc31b0659a39e810eb8c062a7307a69b87b53
fetched_at: '2026-06-28T22:40:59.381555+00:00'
product: protheus
section_id: 1500001548482
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB: COMO INCLUIR LANÇAMENTO
  CONTÁBIL VIA MILE UTILIZANDO ROTINA AUTOMÁTICA'
type: support-article
updated_at: '2025-01-24T00:22:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017511992-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-COMO-INCLUIR-LAN%C3%87AMENTO-CONT%C3%81BIL-VIA-MILE-UTILIZANDO-ROTINA-AUTOM%C3%81TICA
---

**Dúvida**Como incluir lançamentos contábeis via mile, utilizando rotina automática.

**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial - A partir da versão 12  
  
**Solução**

Para inclusão de lançamentos contábeis via MILE utilizando a rotina automática seguir os passos abaixo:

-Via configurador em Aceleradores / Mile / Layout - criar layout de importação para rotina CTBA102.

Exemplo de XML que pode ser importado na rotina:

<?xml version="1.0" encoding="UTF-8"?>  
<CFGA600 Operation="4" version="1.01">  
<XZ1MASTER modeltype="FIELDS" >  
<XZ1\_LAYOUT order="1">  
<value>RMCT2</value>  
</XZ1\_LAYOUT>  
<XZ1\_TYPE order="2">  
<value>1</value>  
</XZ1\_TYPE>  
<XZ1\_DESC order="3">  
<value>MIGRACAO RM LANCAMENTOS CONTABEIS</value>  
</XZ1\_DESC>  
<XZ1\_ADAPT order="4">  
<value>CTBA102</value>  
</XZ1\_ADAPT>  
<XZ1\_STRUC order="5">  
<value>2</value>  
</XZ1\_STRUC>  
<XZ1\_SEPARA order="6">  
<value>|</value>  
</XZ1\_SEPARA>  
<XZ1\_SEPINASP order="7">  
<value>2</value>  
</XZ1\_SEPINASP>  
<XZ1\_TYPEXA order="8">  
<value>2</value>  
</XZ1\_TYPEXA>  
<XZ1\_SEPINI order="9">  
<value>1</value>  
</XZ1\_SEPINI>  
<XZ1\_SEPFIN order="10">  
<value>1</value>  
</XZ1\_SEPFIN>  
<XZ1\_TABLE order="11">  
<value>CT2</value>  
</XZ1\_TABLE>  
<XZ1\_DESTAB order="12">  
<value>Lançamentos Contábeis</value>  
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
<item id="1" deleted="0" >  
<XZ2\_SEQ>01</XZ2\_SEQ>  
<XZ2\_CHANEL>MASTER</XZ2\_CHANEL>  
<XZ3DETAIL modeltype="FIELDS" >  
<XZ3\_CHANEL order="2">  
<value>MASTER</value>  
</XZ3\_CHANEL>  
<XZ3\_DESC order="3">  
<value>CANAL MASTER</value>  
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
<item id="1" deleted="0" >  
<XZ4\_SEQ>001</XZ4\_SEQ>  
<XZ4\_FIELD>DDATALANC</XZ4\_FIELD>  
<XZ4\_TYPFLD>D</XZ4\_TYPFLD>  
<XZ4\_NOVAL>2</XZ4\_NOVAL>  
<XZ4\_SOURCE>0002</XZ4\_SOURCE>  
</item>  
<item id="2" deleted="0" >  
<XZ4\_SEQ>006</XZ4\_SEQ>  
<XZ4\_FIELD>CLOTE</XZ4\_FIELD>  
<XZ4\_TYPFLD>C</XZ4\_TYPFLD>  
<XZ4\_NOVAL>2</XZ4\_NOVAL>  
<XZ4\_SOURCE>0003</XZ4\_SOURCE>  
</item>  
<item id="3" deleted="0" >  
<XZ4\_SEQ>007</XZ4\_SEQ>  
<XZ4\_FIELD>CSUBLOTE</XZ4\_FIELD>  
<XZ4\_TYPFLD>C</XZ4\_TYPFLD>  
<XZ4\_NOVAL>2</XZ4\_NOVAL>  
<XZ4\_SOURCE>0004</XZ4\_SOURCE>  
</item>  
<item id="4" deleted="0" >  
<XZ4\_SEQ>008</XZ4\_SEQ>  
<XZ4\_FIELD>CDOC</XZ4\_FIELD>  
<XZ4\_TYPFLD>C</XZ4\_TYPFLD>  
<XZ4\_NOVAL>2</XZ4\_NOVAL>  
<XZ4\_SOURCE>0005</XZ4\_SOURCE>  
</item>  
<item id="6" deleted="0" >  
<XZ4\_SEQ>010</XZ4\_SEQ>  
<XZ4\_FIELD>NTOTINF</XZ4\_FIELD>  
<XZ4\_TYPFLD>N</XZ4\_TYPFLD>  
<XZ4\_NOVAL>2</XZ4\_NOVAL>  
<XZ4\_SOURCE>0007</XZ4\_SOURCE>  
</item>  
<item id="7" deleted="0" >  
<XZ4\_SEQ>011</XZ4\_SEQ>  
<XZ4\_FIELD>NTOTINFLOT</XZ4\_FIELD>  
<XZ4\_TYPFLD>N</XZ4\_TYPFLD>  
<XZ4\_NOVAL>2</XZ4\_NOVAL>  
<XZ4\_SOURCE>0008</XZ4\_SOURCE>  
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
<item id="2" deleted="0" >  
<XZ2\_SEQ>02</XZ2\_SEQ>  
<XZ2\_CHANEL>DETAIL</XZ2\_CHANEL>  
<XZ2\_SUPER>MASTER</XZ2\_SUPER>  
<XZ3DETAIL modeltype="FIELDS" >  
<XZ3\_CHANEL order="2">  
<value>DETAIL</value>  
</XZ3\_CHANEL>  
<XZ3\_DESC order="3">  
<value>CANAL DETAIL</value>  
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
<item id="1" deleted="0" >  
<XZ4\_SEQ>002</XZ4\_SEQ>  
<XZ4\_FIELD>CT2\_FILIAL</XZ4\_FIELD>  
<XZ4\_NOVAL>2</XZ4\_NOVAL>  
<XZ4\_DESC>Filial do Sistema</XZ4\_DESC>  
<XZ4\_OBS>FILIAL DO SISTEMA</XZ4\_OBS>  
<XZ4\_SOURCE>0002</XZ4\_SOURCE>  
</item>  
<item id="2" deleted="0" >  
<XZ4\_SEQ>003</XZ4\_SEQ>  
<XZ4\_FIELD>CT2\_LINHA</XZ4\_FIELD>  
<XZ4\_NOVAL>2</XZ4\_NOVAL>  
<XZ4\_DESC>Numero da Linha</XZ4\_DESC>  
<XZ4\_OBS>Numero da Linha</XZ4\_OBS>  
<XZ4\_SOURCE>0003</XZ4\_SOURCE>  
</item>  
<item id="3" deleted="0" >  
<XZ4\_SEQ>004</XZ4\_SEQ>  
<XZ4\_FIELD>CT2\_MOEDLC</XZ4\_FIELD>  
<XZ4\_NOVAL>2</XZ4\_NOVAL>  
<XZ4\_DESC>Moeda do Lancamento</XZ4\_DESC>  
<XZ4\_OBS>Moeda do Lancamento</XZ4\_OBS>  
<XZ4\_SOURCE>0004</XZ4\_SOURCE>  
</item>  
<item id="4" deleted="0" >  
<XZ4\_SEQ>005</XZ4\_SEQ>  
<XZ4\_FIELD>CT2\_DC</XZ4\_FIELD>  
<XZ4\_NOVAL>2</XZ4\_NOVAL>  
<XZ4\_DESC>Tipo do Lancamento</XZ4\_DESC>  
<XZ4\_OBS>Tipo do Lancamento</XZ4\_OBS>  
<XZ4\_SOURCE>0005</XZ4\_SOURCE>  
</item>  
<item id="5" deleted="0" >  
<XZ4\_SEQ>006</XZ4\_SEQ>  
<XZ4\_FIELD>CT2\_DEBITO</XZ4\_FIELD>  
<XZ4\_NOVAL>2</XZ4\_NOVAL>  
<XZ4\_DESC>Conta Debito</XZ4\_DESC>  
<XZ4\_OBS>Conta Debito</XZ4\_OBS>  
<XZ4\_SOURCE>0006</XZ4\_SOURCE>  
</item>  
<item id="6" deleted="0" >  
<XZ4\_SEQ>007</XZ4\_SEQ>  
<XZ4\_FIELD>CT2\_CREDIT</XZ4\_FIELD>  
<XZ4\_NOVAL>2</XZ4\_NOVAL>  
<XZ4\_DESC>Conta Credito</XZ4\_DESC>  
<XZ4\_OBS>Conta Credito</XZ4\_OBS>  
<XZ4\_SOURCE>0007</XZ4\_SOURCE>  
</item>  
<item id="7" deleted="0" >  
<XZ4\_SEQ>008</XZ4\_SEQ>  
<XZ4\_FIELD>CT2\_VALOR</XZ4\_FIELD>  
<XZ4\_NOVAL>2</XZ4\_NOVAL>  
<XZ4\_DESC>Valor do Lancamento</XZ4\_DESC>  
<XZ4\_OBS>Valor do Lancamento</XZ4\_OBS>  
<XZ4\_SOURCE>0008</XZ4\_SOURCE>  
</item>  
<item id="8" deleted="0" >  
<XZ4\_SEQ>009</XZ4\_SEQ>  
<XZ4\_FIELD>CT2\_ORIGEM</XZ4\_FIELD>  
<XZ4\_NOVAL>2</XZ4\_NOVAL>  
<XZ4\_DESC>Origem do Lancamento</XZ4\_DESC>  
<XZ4\_SOURCE>0009</XZ4\_SOURCE>  
</item>  
<item id="9" deleted="0" >  
<XZ4\_SEQ>010</XZ4\_SEQ>  
<XZ4\_FIELD>CT2\_HP</XZ4\_FIELD>  
<XZ4\_NOVAL>2</XZ4\_NOVAL>  
<XZ4\_DESC>Historico Padrao</XZ4\_DESC>  
<XZ4\_SOURCE>0010</XZ4\_SOURCE>  
</item>  
<item id="10" deleted="0" >  
<XZ4\_SEQ>011</XZ4\_SEQ>  
<XZ4\_FIELD>CT2\_CONVER</XZ4\_FIELD>  
<XZ4\_NOVAL>2</XZ4\_NOVAL>  
<XZ4\_DESC>Criterio de Conversao</XZ4\_DESC>  
<XZ4\_OBS>CRITERIO DE CONVERSAO</XZ4\_OBS>  
<XZ4\_SOURCE>0011</XZ4\_SOURCE>  
</item>  
<item id="11" deleted="0" >  
<XZ4\_SEQ>012</XZ4\_SEQ>  
<XZ4\_FIELD>CT2\_HIST</XZ4\_FIELD>  
<XZ4\_NOVAL>2</XZ4\_NOVAL>  
<XZ4\_DESC>Historico Lcto</XZ4\_DESC>  
<XZ4\_OBS>Historico Lcto</XZ4\_OBS>  
<XZ4\_SOURCE>0012</XZ4\_SOURCE>  
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

-Criar Arquivo Texto com as seguintes características:

-Canal Master - Incluir data de lançamento, numero do lote, numero do sublote, numero do documento, valor informado e valor informado do lote

|MASTER|12/05/16|333333|333|333333|2450.50|2450.50|

-Canal Detail - Incluir dados do lançamento como filial, linha, moeda, tipo do lançamento, conta a debito, conta a credito, valor, origem do lançamento, critério de conversão e histórico,

|DETAIL|D MG 01 |001|01|3|101010101|101010102|2450.50|TESTEPC||11|HISTORICO TESTE|

Exemplo de Arquivo Texto a ser Importado:

|MASTER|12/05/16|333333|333|333333|2450.50|2450.50|  
|DETAIL|D MG 01 |001|01|3|101010101|101010102|2450.50|TESTEPC||11|HISTORICO TESTE|

-Na própria rotina do MILE executar Processamento de TXT informando o layout e o nome do arquivo a ser importado.

-Entrar em Contabilidade Gerencial e verificar se lançamento foi incluído na data informada no arquivo texto em lançamentos contábeis automáticos (CTBA102)

Este exemplo é para inclusão de novos lançamentos, portanto se necessitar rodar a rotina novamente tem que previamente excluir o lançamento ja processado. Caso copie este exemplo para testes deverá ser acertados os campos filiais e conta contábil de acordo com seus próprios cadastros.

**Importante:**

Diferente da chamada da rotina automática diretamente as variáveis vazias não são carregadas no MILE. Exemplo TDN a variável CPADRAO é passada vazia no MILE mesmo que tiver no leiaute e no arquivo texto estiver vazio esta não é carregada.

**Para mais detalhe Veja** :

<https://tdn.totvs.com/display/framework/MILE+-+Model+Integrator+Layout+Engine>

[Manual MILE Model Integrator Layout Engine.pdf](http://tdn.totvs.com/download/attachments/63865874/Manual%20MILE%20Model%20Integrator%20Layout%20Engine.pdf?version=1&modificationDate=1372449207000&api=v2)

[MILE - Model Integrator Layout Engine](http://tdn.totvs.com/display/framework/MILE+-+Model+Integrator+Layout+Engine)
