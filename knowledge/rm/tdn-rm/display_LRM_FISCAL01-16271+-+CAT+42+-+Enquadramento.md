---
content_hash: 9016bd48a0ba98ecc41135093608a317eac7c2bae4736abe13dd7bd8e173af60
fetched_at: '2026-06-29T00:11:09.540025+00:00'
page_id: '640203492'
product: rm
source: tdn-rm
title: FISCAL01-16271 - CAT 42 - Enquadramento
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-16271+-+CAT+42+-+Enquadramento
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | CAT 42 |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-16271 |

## **02. SITUAÇÃO/REQUISITO**

No período de apuração do tributo icmsst | ressarcimento/complemento de icms st |coluna valor unitário realiza o calculo  com base no campo ICMS Próprio dentro dos itens. Porém a nota de saída com cfop iniciado com 5.xxx.xxx esta atrelado o tipo de tributação isento ou não incidência com isso impactando no calculo do valor a ressarcir.

Conforme nossa consultoria e o manual da CAT 42 o campo Confronto deve ser preenchido anexo o trecho da cat 42.

Foi inserido a nota de entrada (28072021) e saída  (2280721) no nucleus e realizado processo conforme a documentação: [https://tdn.totvs.com/pages/releaseview.action?pageId=403048724#FISCAL01-6374ERPortariaCAT42/2018SP-5](https://tdn.totvs.com/pages/releaseview.action?pageId=403048724#FISCAL01-6374ERPortariaCAT42/2018SP-5 "Follow link"). A geração da CAT 42 com base no calculo **((Preço unit \* quant) \* alíquota interna) quando o tipo de tributação do icms for isento ou imune.**

## **03. SOLUÇÃO**

**Foi implementado a regra abaixo para o Enquadramento Legal:**

**Se** Operação com Ressarcimento/Complemento de ST desmarcado

**Então** 0

**Senão Se** Regra ICMS Isento OU Não incidência  
**Então** 3

**Senão Se** Venda Interestadual  
**Então** 4

**Senão** **Se** Consumidor Final  
**Então** 1

**Senão**  
**Então** 2

As Operações de Vendas (Internas ou Interestadual) com o Tipo de Tributação igual a: **Isenta** ou **Não Incidência**, agora estão sendo geradas com Código de Enquadramento igual a 3.

Segundo a consultoria o **Código 4** – Deve ser considerado todas as Venda Interestadual – **Tributada, Outras, Suspensas**. Foi alterado na **Rotina CAT 42** que as Operações de Vendas (Internas ou Interestadual) com o Tipo de Tributação igual a: **Isenta, Não Incidência,** seja gerada com Código de Enquadramento **igual a 3,** mesmo sendo interestadual.
