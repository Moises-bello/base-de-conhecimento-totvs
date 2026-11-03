---
content_hash: add54ad0f6d54833a58bc08ab0b45cd3ed65f74491eb2d3de883ebd8d9d14327
fetched_at: '2026-06-29T00:05:53.192055+00:00'
page_id: '1068186521'
product: rm
source: tdn-rm
title: DT - Cadastro de Dependente - Alteração na inclusão do Valor Dedução do Rendimento
  Tributável
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1068186521
version: 7
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Cadastro de Dependente - Valor Dedução do Rendimento Tributável |
| País: | Brasil |
| Issue: | [DRHCALCRM-12018](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-12018) |

## **02.****VERSÕES**

**A partir das Versões:**

* 12.1.2506.308
* 12.1.2510.234
* 12.1.2602.149
* 12.1.2606 e superiores

## **03.****SITUAÇÃO/REQUISITO**

Conforme informado pela consultoria: 

"Ainda que as deduções legais não sejam utilizadas no cálculo do IRRF em razão da aplicação do desconto simplificado mensal, tais informações permanecem existentes no contexto fiscal do trabalhador e devem ser devidamente declaradas. A própria orientação oficial do eSocial, constante no FAQ 10.39 (atualizado em 17/12/2025), estabelece expressamente que, mesmo quando aplicado o desconto simplificado mensal, é obrigatório o envio dos dados de deduções legais aplicáveis ao trabalhador no evento de pagamento. Assim, a não utilização das deduções no cálculo não afasta a obrigatoriedade de sua informação no evento S-1210." 

Link consultoria:

## **04.****SOLUÇÃO**

Desta forma devemos considerar a dedução do dependente quando for aplicável, mesmo se não existir o desconto do IRRF ou quando for utilizado o desconto simplificado.

Deverá ser preenchido o histórico dos dependentes sempre que aplicável e não somente quando houver o desconto de IRRF.

## **05. ASSUNTOS RELACIONADOS**

* [Valor Dedução do Rendimento Tributável](https://tdn.totvs.com/pages/releaseview.action?pageId=784779468)
* [Valor Dedução do Rendimento Tributável no Cadastro de Dependentes - Alterações no cálculo para atender ao leiaute S-1.2 que irá substituir a DIRF](https://tdn.totvs.com/pages/releaseview.action?pageId=786553670#tabs-passo3)
* [Passo a Passo para atualizar o "Valor Dedução do Rendimento Tributável" do Dependente](https://tdn.totvs.com/pages/viewpage.action?pageId=1070064028)
