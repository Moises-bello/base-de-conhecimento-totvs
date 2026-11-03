---
content_hash: e405206730409ea26dd47281a76763758abc0083b9594581d083ce1e5f7f4d59
fetched_at: '2026-06-29T00:10:31.707857+00:00'
page_id: '521995713'
product: rm
source: tdn-rm
title: 6850440 FISCAL01-11071 DT Retido na Fonte - INSS \ FUNRURAL
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=521995713
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | Nota Fiscal |
| Ticket: | 6850440 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11071 |

## **02. SITUAÇÃO/REQUISITO**

Cliente informa que possui os tributos INSS\ FunRural, Girat, Senar destacado no item do movimento de saída. Segundo ele, esses valores não devem ser destacados no campo Retenção da NF (TAG e ), pois o responsável pelo pagamento é o Emissor (nosso cliente).

Porém, os tributos devem ser destacados no movimento\lançamento fiscal para geração da REINF - R2050.

Documento onde orientamos os clientes a informar Tipos de Recolhimento específicos para o INSS/FUNRURAL de forma a atender a Reinf: <https://tdn.totvs.com/pages/viewpage.action?pageId=347445276>

Existência de INSS/FUNRURAL nos movimentos de entrada sempre será indício de que o tributo é retido.

Já nas saídas o que diferenciava se o tributos seria retido pelo cliente era o Tipo de Recolhimento (Retido na Fonte) e isso não gerava impacto no Fiscal uma vez que o sistema não apura INSS/FUNRURAL na saída.

**PROPOSTA DE SOLUÇÃO:**

Na NF-e

Se houver retenção do INSS/FUNRURAL pelo tomador, o cliente deverá colocar no Tipo de Recolhimento do tributo INSS/FUNRURAL a opção "**Retido na Fonte**". Os demais tributos INSS15, INSS20, INSS25, GILRAT e SENAR devem continuar com seus respectivos Tipos de Recolhimento.

A geração da respectiva tag na NF-e deve considerar a soma de todos os tributos que estiverem informados no Item do Movimento:

* INSS = INSS + INSS15 + INSS20 + INSS25
* FUNRURAL = Funrural + GILRAT + SENAR

Escrituração

A escrituração deve continuar funcionando tendo os tributos INSS e FUNRURAL parametrizados com o Tipo de Recolhimento INSS/FUNRURAL ou Retido na Fonte.

## **03. SOLUÇÃO**

Foi alterado a geração das tags vBCRetPrev e vRetPrev, referente ao imposto retido do Funrural e INSS. Passa a ser considerado a seguinte regra, para geração das tags:  
   
● Existir tributo principal (deve existir tributo Funrural ou INSS com tipo de recolhimento “Retido na Fonte”)  
   
Será seguido a seguinte regra para totalizar as tags:  
● Os outros tributos devem ser do mesmo tipo do tributo principal( exemplo, para o INSS15, INSS20 e INSS25 o  
tipo de tributo deve ser INSS)  
   
Quando o tipo de recolhimento for “Retido na fonte” as tags **serão** geradas no XML da nota fiscal, quando o tipo de recolhimento for diferente as tags **não serão** geradas.
