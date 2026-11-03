---
content_hash: 98594b2008d00bc687e942e7f9be7108ab1a41851377760fc7740196a3b5b3bc
fetched_at: '2026-06-29T00:05:52.181503+00:00'
page_id: '1058197181'
product: rm
source: tdn-rm
title: DT - Informe de Rendimentos 2026 - Tratativa na dedução de dependentes de IRRF
  no 13º salário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1058197181
version: 8
---

## **01. DADOS GERAIS**

| Produto: | TOTVS - Folha de Pagamento |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Informe de Rendimentos 2026 - Tratativa na dedução de dependentes de IRRF no 13º salário |
| País: | Brasil |
| Ticket: |  |
| Issue: | [DRHROTRM-18107](https://jiraproducao.totvs.com.br/browse/DRHROTRM-18107) |

## **02. VERSÕES**

A partir dos patches:

* 12.1.2506.288
* 12.1.2510.209
* 12.1.2602.129 e superiores

## **03. SITUAÇÃO/REQUISITO**

Ao gerar o Informe de Rendimentos pelo menu Anual | DIRF/Informe de Rendimentos, o valor apresentado no campo **“5. Rendimentos sujeitos à tributação exclusiva (rendimento líquido)”**, na linha **“1. 13º (Décimo terceiro) salário”**, está sendo calculado deduzindo o valor de dedução por dependente, mesmo quando não há desconto de IRRF no cálculo do 13º salário.

## **04. SOLUÇÃO**

Foi realizada uma tratativa na apuração do valor apresentado no campo **“5. Rendimentos sujeitos à tributação exclusiva (rendimento líquido)”**, especificamente na linha **“1. 13º (Décimo terceiro) salário”** do Informe de Rendimentos.

A geração doInforme de Rendimentos passa a utilizar o valor dedutível, existente no anexo **“Valor Dedução do Rendimento Tributável”**, disponível em: Administração de Pessoal | Funcionários | Anexos | Folha de Pagamento | Dependentes.

Com essa tratativa a dedução de dependentes será considerada apenas quando aplicável.

## **05.****ASSUNTOS RELACIONADOS**

+ - Consultoria
