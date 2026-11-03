---
article_id: 360017838211
category: Financeiro - Contas a Pagar
content_hash: 4a158c7b1f204320ffa21bc2e538cda7df2e94276a4d6da465903a165b307643
fetched_at: '2026-06-28T22:38:07.199071+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - FINA340 - HELP: FA340PALIQ /
  FA340PABRU'
type: support-article
updated_at: '2022-03-23T01:30:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017838211-Cross-Segmento-Backoffice-Linha-Protheus-FINA340-HELP-FA340PALIQ-FA340PABRU
---

**Ocorrência**No módulo **Financeiro**, ao tentar realizar uma **compensação** na rotina **FINA340** é apresentado  a mensagem **HELP: FA340PALIQ**.  
  
**Ambiente**Microsiga Protheus – Financeiro – A partir da versão 11.80  
  
**Causa**Após atualização da rotina **FINA340**, a mesma passou a realizar a validação correta dos parâmetros abaixo:

**MV\_PABRUTO**   
**MV\_COMPCP**  
**MV\_BP10925**  
**MV\_PAPRIME**

**Solução**Para correção do **HELP**, é necessário realizar o ajuste na **parametrização** para seu correto funcionamento, segue abaixo duas opções:

1. **PRIMEIRA OPÇÃO**O parâmetro **MV\_PABRUTO** caso esteja com o valor **2** (**Líquido**), ao gerar títulos do tipo **PA** é mantida a geração com o valor líquido, em que são descontados os valores de impostos que podem ser retidos na inclusão.  
Ao realizar a compensação de um título, por exemplo, do tipo **NF** com uma **PA**, sendo que ambas retêm impostos na baixa, é aconselhável os parâmetros abaixo sejam configurados da seguinte maneira, para que haja coerência de valores:  
**MV\_COMPCP** = **.T.** - Indica se na compensação de uma **NF** com um **PA** os impostos serão proporcionalizados.  
**MV\_BP10925** = **2** - Considera valor Líquido na baixa Parcial descontados os impostos.  
**MV\_PAPRIME** = **1** - Considera provisionamento de impostos para **PA** Líquido.

2. **SEGUNDA OPÇÃO**O parâmetro **MV\_PABRUTO** estiver igual a **1** (**Bruto**) ao gerar títulos do tipo **PA** (Pagamentos Antecipados), é gerado com o valor **bruto**, não descontando os valores de impostos que podem ser retidos na inclusão. Então a compensação de uma **NF** com uma **PA**, deveria ser pelo valor bruto configurando os parâmetros conforme abaixo:  
**MV\_PABRUTO** = **1** - **Bruto** e **MV\_BX10925** = **1** Imposto na baixa ou **MV\_BX10925**=**2** Imposto na emissão  
**MV\_BP10925** = **1** - Considera valor Bruto na baixa Parcial sem descontar os impostos.  
**MV\_PAPRIME** = **2** - Não considera provisionamento de impostos para PA Líquido.  
Observação:  
O parâmetro **MV\_COMPCP** não influencia caso o parâmetro **MV\_PABRUTO** esteja com o valor em **1**. Independente dos títulos terem impostos, ou não, é necessário a parametrização.  
A compensação entre **NF** x **PA**, partindo tanto da **NF** como do **PA**, não é permitida caso o parâmetro **MV\_PABRUTO** esteja com o valor **2** (**Líquido**).

**Importante**O parâmetro **MV\_BX10925**não deve ser alterado, uma vez que no momento da implantação do ***Protheus***, foi definido como a empresa irá tratar o imposto.
