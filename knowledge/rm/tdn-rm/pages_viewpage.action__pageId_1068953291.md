---
content_hash: 937885ae9cba1da993e4fd2dcf400aba1e8189ff5eaf76bddf68d7352a5a6955
fetched_at: '2026-06-29T00:05:53.298661+00:00'
page_id: '1068953291'
product: rm
source: tdn-rm
title: DT - S-1210 - Valor Dedução do Rendimento Tributável
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1068953291
version: 8
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | **RM** |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | eSocial - Valor Dedução do Rendimento Tributável |
| País: | Brasil |
| Issue: | [DRHROTRM-18196](https://jiraproducao.totvs.com.br/browse/DRHROTRM-18196 "View this issue") |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2506.313
* 12.1.2510.238
* 12.1.2602.152 e Superiores

## **03.****SITUAÇÃO/REQUISITO**

Adaptar o produto TOTVS Folha de Pagamento à legislação referente ao valor de dedução de dependentes para IRRF, conforme orientação da consultoria tributária TOTVS:

> “Ainda que as deduções legais não sejam utilizadas no cálculo do IRRF em razão da aplicação do desconto simplificado mensal, tais informações permanecem existentes no contexto fiscal do trabalhador e devem ser devidamente declaradas. A própria orientação oficial do eSocial, constante no FAQ 10.39 (atualizado em 17/12/2025), estabelece expressamente que, mesmo quando aplicado o desconto simplificado mensal, é obrigatório o envio dos dados de deduções legais aplicáveis ao trabalhador no evento de pagamento. Assim, a não utilização das deduções no cálculo não afasta a obrigatoriedade de sua informação no evento S-1210.”

## **04. SOLUÇÃO**

Implementamos para que na geração do evento S-1210 a tag < dedDepen> passe a considerar o valor existente em Administração de Pessoal | Funcionário | Anexos | Folha de Pagamento | Dependentes | Anexos | Valor Dedução de Rendimento Tributável.

## **05. DEMAIS INFORMAÇÕES**

* [Consultoria - Envio de dedução de dependentes no S-1210](https://tdn.totvs.com/pages/releaseview.action?pageId=1056129814)
* [DT - Processo para atualizar Dedução por Dependente](https://tdn.totvs.com.br/pages/viewpage.action?pageId=1070066693)
* [Valor Dedução do Rendimento Tributável](https://tdn.totvs.com/pages/releaseview.action?pageId=784779468)
* [Valor Dedução do Rendimento Tributável no Cadastro de Dependentes - Alterações no cálculo para atender ao leiaute S-1.2 que irá substituir a DIRF](https://tdn.totvs.com/pages/releaseview.action?pageId=786553670#tabs-passo3)
