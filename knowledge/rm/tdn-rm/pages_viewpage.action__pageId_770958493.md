---
content_hash: b11dc39dc59b1556ab5102c060ef3fb0d390170a63a59446712d92840c667d27
fetched_at: '2026-06-29T00:11:36.057970+00:00'
page_id: '770958493'
product: rm
source: tdn-rm
title: DT - Rescisão Complementar (Tipo F) - Campo dissídio para eventos de IRRF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=770958493
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Rescisão Complementar e Gerar XML Periódicos |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue: | [DRHCALCRM-4782](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-4782) |

## **02. SITUAÇÃO/REQUISITO**

Ao gerar uma rescisão complementar do tipo F com pagamento de PLR. No XML do evento S-1200 o evento de IRRF não é gerado.    
   
De acordo com o MOS página 129, item 4.1  
   
Indicativo de apuração de imposto de renda 4.1.  
Como regra, o campo

{indApurIR}

deve ser preenchido com [0]: com esse indicativo a rubrica é  
considerada para apuração do IR a partir dos dados informados no eSocial (S-1200, S-1202, S-1207, S  
2299 ou S-2399).  
Indicativo de tipo de apuração de IR:  
0 - Normal (apuração sob a folha de pagamento declarada no eSocial);  
1 - Situação especial de apuração de IR.

## **03. SOLUÇÃO**

Ao calcular a rescisão complementar selecionando:

* + Parâmetro "Dissídio/ Convenção / Acordo coletivo" marcado como "Não"
  + Parâmetro "Calcular somente eventos informados" marcado
  + Parâmetro "Pagamento de verbas de natureza salarial ou não salarial devidas após o desligamento" marcado
  + Selecionar "Dados do dissidio / convenção / acordo coletivo" com tipo de acordo "F - Outras verbas de natureza salarial ou não salarial devidas após o desligamento"

Serão inseridos os eventos de IRRF com flag marcada como "Não" para o parâmetro "Dissidio" dentro da edição do evento na ficha financeira e na geração do XML periódico serão informados os eventos no XML S1200 do e-Social.

Realizado alteração para todos os códigos de cálculo de IRRFs:

* Código de cálculo 4  - IRRF
* Código de cálculo 49 - IRRF 13º SALARIO
* Código de cálculo 61 - IRRF FÉRIAS ENVELOPE
* Código de cálculo 127 - IRRF PARTICIPACAO NOS LUCROS

## **04. ASSUNTOS RELACIONADOS**

* [Rescisão Complementar](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718921)
* [Gerar XML Periódicos](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719232)
