---
content_hash: f4706f7f45cca2c3365c5771530d006f7aff43be3e492778a8d5e60d5b377492
fetched_at: '2026-06-29T00:11:36.747753+00:00'
page_id: '773514122'
product: rm
source: tdn-rm
title: 'DT - S-2240: Gerar o agente nocivo verificando o código e a descrição'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=773514122
version: 13
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | S-2240: Gerar o agente nocivo conforme a chave do leiaute |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-6476](https://jiraproducao.totvs.com.br/browse/DRHROTRM-6476) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2209.242
* 12.1.2302.166
* 12.1.2306.109

## **03. SITUAÇÃO/REQUISITO**

No momento, ao gerar o evento S-2240, apenas um campo (tag <codAgNoc>) é considerado na chave do grupo agente nocivo do trabalhador. No entanto, em algumas situações, são necessárias avaliações de risco adicionais para o mesmo agente nocivo. Portanto, é necessário considerar não apenas o código, mas também a descrição do agente nocivo para atender a essas situações.

## **04. SOLUÇÃO**

Adequamos o produto, de modo que, ao gerar o evento S-2240, o grupo de agente nocivo seja gerado de acordo com a chave fornecida no leiaute do eSocial, onde as chaves atualmente utilizadas são codAgNoc e dscAgNoc.

Se um dos códigos definidos pelo layout (S-2240) for utilizado, o código do agente nocivo poderá se repetir com descrições diferentes. Porém, caso contrário, apenas um registro do grupo deverá ser gerado.

Importante lembrar que, de acordo com o leiaute S-1.1 do eSocial para o evento S-2240, o campo <dscAgNoc> só deve ser preenchido com uma descrição quando o código corresponder a um dos seguintes valores: [01.01.001, 01.02.001, 01.03.001, 01.04.001, 01.05.001, 01.06.001, 01.07.001, 01.08.001, 01.09.001, 01.10.001, 01.12.001, 01.13.001, 01.14.001, 01.15.001, 01.16.001, 01.17.001, 01.18.001, 05.01.001].
