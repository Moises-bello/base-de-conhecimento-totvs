---
article_id: 7952402785943
category: PCO - Cadastros
content_hash: 198b3104f39612f17f21df0ea46136c59a339960b3f6c698271764e5eddb1638
fetched_at: '2026-06-28T22:37:12.864070+00:00'
product: protheus
section_id: 1500001550802
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAPCO - PCOA010 - Incluir dados
  na AK5 via MILE
type: support-article
updated_at: '2022-08-04T20:06:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7952402785943-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-PCOA010-Incluir-dados-na-AK5-via-MILE
---

**Dúvida**Como incluir Contas Orçamentarias via MILE ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Planejamento e Controle Orçamentário - A partir da versão 12  
  
**Solução**

Para incluir as Contas Orçamentarias via MILE, siga os passos abaixo:

1- Via configurador em **Aceleradores / Mile / Layout** - criar layout de importação para rotina PCOA010, caso deseje importar um layout, pode-se utilizar o modelo abaixo:

<?xml version="1.0" encoding="UTF-8"?>  
<CFGA600 Operation="4" version="1.01">  
<XZ1MASTER modeltype="FIELDS">  
<XZ1\_LAYOUT order="1">  
<value>IMPAK5</value>  
</XZ1\_LAYOUT>  
<XZ1\_TYPE order="2">  
<value>2</value>  
</XZ1\_TYPE>  
<XZ1\_DESC order="3">  
<value>Contas Orcamentarias</value>  
</XZ1\_DESC>  
<XZ1\_ADAPT order="4">  
<value>PCOA010</value>  
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
<value>1</value>  
</XZ1\_TYPEXA>  
<XZ1\_SEPINI order="9">  
<value>2</value>  
</XZ1\_SEPINI>  
<XZ1\_SEPFIN order="10">  
<value>2</value>  
</XZ1\_SEPFIN>  
<XZ1\_TABLE order="11">  
<value>AK5</value>  
</XZ1\_TABLE>  
<XZ1\_DESTAB order="12">  
<value>Contas Orçamentárias</value>  
</XZ1\_DESTAB>  
<XZ1\_ORDER order="13">  
<value>1</value>  
</XZ1\_ORDER>  
<XZ1\_TIPDAT order="18">  
<value>1</value>  
</XZ1\_TIPDAT>  
<XZ1\_DECSEP order="19">  
<value>1</value>  
</XZ1\_DECSEP>  
<XZ1\_EMULTC order="20">  
<value>2</value>  
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
<XZ2\_LAYOUT order="1"></XZ2\_LAYOUT>  
<XZ2\_SEQ order="2"></XZ2\_SEQ>  
<XZ2\_CHANEL order="3"></XZ2\_CHANEL>  
<XZ2\_SUPER order="4"></XZ2\_SUPER>  
</struct>  
<items>  
<item id="1" deleted="0" >  
<XZ2\_SEQ>01</XZ2\_SEQ>  
<XZ2\_CHANEL>AK5MASTER</XZ2\_CHANEL>  
<XZ3DETAIL modeltype="FIELDS">  
<XZ3\_CHANEL order="2">  
<value>AK5MASTER</value>  
</XZ3\_CHANEL>  
<XZ3\_DESC order="3">  
<value>Cadastro de Contas Orcamentarias</value>  
</XZ3\_DESC>  
<XZ3\_IDOUT order="4">  
<value>AK5MASTER</value>  
</XZ3\_IDOUT>  
<XZ3\_OCCURS order="5">  
<value>1</value>  
</XZ3\_OCCURS>  
</XZ3DETAIL>  
<XZ4DETAIL modeltype="GRID" optional="1">  
<struct>  
<XZ4\_LAYOUT order="1"></XZ4\_LAYOUT>  
<XZ4\_CHANEL order="2"></XZ4\_CHANEL>  
<XZ4\_SEQ order="3"></XZ4\_SEQ>  
<XZ4\_FIELD order="4"></XZ4\_FIELD>  
<XZ4\_TYPFLD order="5"></XZ4\_TYPFLD>  
<XZ4\_EXEC order="6"></XZ4\_EXEC>  
<XZ4\_COND order="7"></XZ4\_COND>  
<XZ4\_NOVAL order="8"></XZ4\_NOVAL>  
<XZ4\_DESC order="9"></XZ4\_DESC>  
<XZ4\_OBS order="10"></XZ4\_OBS>  
<XZ4\_SOURCE order="11"></XZ4\_SOURCE>  
</struct>  
<items>  
<item id="1" deleted="0" >  
<XZ4\_SEQ>001</XZ4\_SEQ>  
<XZ4\_FIELD>AK5\_FILIAL</XZ4\_FIELD>  
<XZ4\_NOVAL>2</XZ4\_NOVAL>  
<XZ4\_DESC>Filial do Sistema</XZ4\_DESC>  
<XZ4\_SOURCE>0001</XZ4\_SOURCE>  
</item>  
<item id="2" deleted="0" >  
<XZ4\_SEQ>002</XZ4\_SEQ>  
<XZ4\_FIELD>AK5\_CODIGO</XZ4\_FIELD>  
<XZ4\_NOVAL>2</XZ4\_NOVAL>  
<XZ4\_DESC>Cod. Conta Orcamentaria</XZ4\_DESC>  
<XZ4\_SOURCE>0002</XZ4\_SOURCE>  
</item>  
<item id="3" deleted="0" >  
<XZ4\_SEQ>003</XZ4\_SEQ>  
<XZ4\_FIELD>AK5\_DESCRI</XZ4\_FIELD>  
<XZ4\_NOVAL>2</XZ4\_NOVAL>  
<XZ4\_DESC>Descricao do C.O.</XZ4\_DESC>  
<XZ4\_SOURCE>0003</XZ4\_SOURCE>  
</item>  
<item id="4" deleted="0" >  
<XZ4\_SEQ>004</XZ4\_SEQ>  
<XZ4\_FIELD>AK5\_TIPO</XZ4\_FIELD>  
<XZ4\_NOVAL>2</XZ4\_NOVAL>  
<XZ4\_DESC>Tipo de Conta Orcament.</XZ4\_DESC>  
<XZ4\_SOURCE>0004</XZ4\_SOURCE>  
</item>  
<item id="5" deleted="0" >  
<XZ4\_SEQ>005</XZ4\_SEQ>  
<XZ4\_FIELD>AK5\_DEBCRE</XZ4\_FIELD>  
<XZ4\_NOVAL>2</XZ4\_NOVAL>  
<XZ4\_DESC>Condicäo Normal da Conta</XZ4\_DESC>  
<XZ4\_SOURCE>0005</XZ4\_SOURCE>  
</item>  
<item id="6" deleted="0" >  
<XZ4\_SEQ>006</XZ4\_SEQ>  
<XZ4\_FIELD>AK5\_MASC</XZ4\_FIELD>  
<XZ4\_NOVAL>2</XZ4\_NOVAL>  
<XZ4\_DESC>Codigo da Mascara</XZ4\_DESC>  
<XZ4\_SOURCE>0006</XZ4\_SOURCE>  
</item>  
<item id="7" deleted="0" >  
<XZ4\_SEQ>007</XZ4\_SEQ>  
<XZ4\_FIELD>AK5\_DTINC</XZ4\_FIELD>  
<XZ4\_NOVAL>2</XZ4\_NOVAL>  
<XZ4\_DESC>Data de Inclusao do CO</XZ4\_DESC>  
<XZ4\_SOURCE>0007</XZ4\_SOURCE>  
</item>  
<item id="8" deleted="0" >  
<XZ4\_SEQ>008</XZ4\_SEQ>  
<XZ4\_FIELD>AK5\_DTINI</XZ4\_FIELD>  
<XZ4\_NOVAL>2</XZ4\_NOVAL>  
<XZ4\_DESC>Inicio da Vigencia</XZ4\_DESC>  
<XZ4\_SOURCE>0008</XZ4\_SOURCE>  
</item>  
<item id="9" deleted="0" >  
<XZ4\_SEQ>009</XZ4\_SEQ>  
<XZ4\_FIELD>AK5\_COSUP</XZ4\_FIELD>  
<XZ4\_NOVAL>2</XZ4\_NOVAL>  
<XZ4\_DESC>Conta Orcament. Superior.</XZ4\_DESC>  
<XZ4\_SOURCE>0009</XZ4\_SOURCE>  
</item>  
<item id="10" deleted="0" >  
<XZ4\_SEQ>010</XZ4\_SEQ>  
<XZ4\_FIELD>AK5\_MSBLQL</XZ4\_FIELD>  
<XZ4\_NOVAL>2</XZ4\_NOVAL>  
<XZ4\_DESC>Registro bloqueado</XZ4\_DESC>  
<XZ4\_SOURCE>0010</XZ4\_SOURCE>  
</item>  
<item id="11" deleted="0" >  
<XZ4\_SEQ>011</XZ4\_SEQ>  
<XZ4\_FIELD>AK5\_CTACTB</XZ4\_FIELD>  
<XZ4\_NOVAL>2</XZ4\_NOVAL>  
<XZ4\_DESC>Conta Contabil CTB</XZ4\_DESC>  
<XZ4\_SOURCE>0011</XZ4\_SOURCE>  
</item>  
</items>  
</XZ4DETAIL>  
<XZ5DETAIL modeltype="GRID" optional="1">  
<struct>  
<XZ5\_LAYOUT order="1"></XZ5\_LAYOUT>  
<XZ5\_CHANEL order="2"></XZ5\_CHANEL>  
<XZ5\_SEQ order="3"></XZ5\_SEQ>  
<XZ5\_FIELD order="4"></XZ5\_FIELD>  
<XZ5\_TYPFLD order="5"></XZ5\_TYPFLD>  
<XZ5\_EXEC order="6"></XZ5\_EXEC>  
<XZ5\_COND order="7"></XZ5\_COND>  
<XZ5\_OBS order="8"></XZ5\_OBS>  
<XZ5\_SOURCE order="9"></XZ5\_SOURCE>  
</struct>  
</XZ5DETAIL>  
</item>  
</items>  
</XZ2DETAIL>  
</XZ1MASTER>  
</CFGA600>

OBS: Deverá salvar o arquivo do modelo em XML.

2-Criar o arquivo texto conforme o layout utilizado, no modelo acima podemos usar o seguinte TXT:

01;11101002;Conta Orçamentaria;2;2;;01/07/2022;01/07/2022;11101;2;;

Segue a relação de qual campo cada valor do exemplo se refere:

01(AK5\_FILIAL);

11101002(AK5\_CODIGO);

Conta Orçamentaria(AK5\_DESCRI);

2(AK5\_TIPO);

2(AK5\_DEBCRE);

(AK5\_MASC-Esta vazio pois não possui mascara);

01/07/2022(AK5\_DTINC);

01/07/2022(AK5\_DTINI);

11101(AK5\_COSUP);

2(AK5\_\_MSBLQL);

(AK5\_CTACTB, Esta vazio pois não possui amarração com conta contábil.);

3- Garanta que o parâmetro MV\_PCOSINC esteja com "1", que não esteja vinculado o plano de contas contábil.

4- Na própria rotina do**MILE** executar Processamento de TXT informando o layout e o nome do arquivo a ser importado.

5- Entrar na rotina PCOA010e verificar se a conta foi importada corretamente.

**OBS: Os exemplos acima podem ser utilizados para testes, porém o cliente deve ajustar o layout e arquivo conforme a sua necessidade e lembrando de preencher todos os campos considerados obrigatórios em sua base.**

**Saiba Mais:**

[MILE - Model Integrator Layout Engine](http://tdn.totvs.com/display/framework/MILE+-+Model+Integrator+Layout+Engine)
