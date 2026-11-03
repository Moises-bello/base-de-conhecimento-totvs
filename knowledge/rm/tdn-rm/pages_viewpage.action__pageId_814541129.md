---
content_hash: 149c583d0719c24d3f1a346ce1a6d0c568927a3595c61d32d6b23dfb179b739b
fetched_at: '2026-06-29T00:11:44.319377+00:00'
page_id: '814541129'
product: rm
source: tdn-rm
title: DT - Retificação Folha - Parecer SEI Nº16120/2020
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=814541129
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Retificação da Folha de Pagamento |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHCALCRM-5398](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-5398)  [DRHCALCRM-5436](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-5436) |

## **02. SITUAÇÃO/REQUISITO**

Como faço para corrigir um desconto informado a maior no eSocial? Por exemplo: Enviei a remuneração de um empregado com quinze dias de afastamento, e no mês seguinte o afastamento foi transformado em Benefício Previdenciário. Como devo fazer para retificar os valores informados no eSocial?

## **03. SOLUÇÃO**

No processo de Retificação da Folha de Pagamento ter o parâmetro ‘Retificar eventos de afastamento (CC’s 145 e 445) pelo processo automático’ para retificar eventos de afastamento (CC145 - ATESTADO MÉDICO e CC445 - ATESTADO MÉDICO SEM INCIDÊNCIA EM INSS) automaticamente. 

Quando o usuário marcar o parâmetro não será necessário preencher o grid com eventos a serem retificados, mas caso o usuário queira informar mais algum evento, deverá calcular o mesmo na retificação.

Caso opte por lançar manualmente os valores de atestado para retificação, o usuário deve acessar o processo em Lançamento / Retificação da Folha de Pagamento sem marcar o parâmetro "Retificar eventos de afastamento (CC's 145 e 445) pelo processo automático" e informar os eventos de provento e desconto que serão lançados no "Período lancto. de Retificação".

Caso não informe um desses eventos corretamente o cálculo ficará inconsistente.

**Atenção:** Não deve  marcar o parâmetro  "Retificar eventos de afastamento (CC's 145 e 445) pelo processo automático" e informar os eventos de CC's 145 e 445 para cálculo manual para um cálculo não interferir um no outro.

## **04. ASSUNTOS RELACIONADOS**

* [Retificação da Folha de Pagamento](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719911)
* [Como gerar a retificação da folha de pagamento de meses anteriores?](https://tdn.totvs.com/pages/releaseview.action?pageId=438289252#1-1)
* [DT - S-1200 e S-1210 - Unificação de períodos mediante retificação](https://tdn.totvs.com/pages/releaseview.action?pageId=811714715)
