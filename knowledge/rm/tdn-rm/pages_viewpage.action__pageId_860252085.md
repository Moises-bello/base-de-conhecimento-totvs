---
content_hash: 6d853dabd07f5017d9e7b826e9621bf403fac141444022e87f617baddbb9e397
fetched_at: '2026-06-29T00:11:55.059675+00:00'
page_id: '860252085'
product: rm
source: tdn-rm
title: DT - Salário Família - Declaração de frequência escolar a partir de 4 anos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=860252085
version: 3
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Cálculo Salário Família |
| País: | Brasil |
| Ticket: | 18250581 |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHCALCRM-5625](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-5625) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2410
* 12.1.2406.122
* 12.1.2402.193
* 12.1.2310.237

## **03.****SITUAÇÃO/REQUISITO**

A partir do entendimento com a consultoria, entendemos a necessidade de ajuste nos dependentes passíveis de recebimento do salário família. Antes, a regra era aplicada da seguinte forma. Os dependentes válidos para o pagamento de Salário Família são verificados, dentre outras regras, os que tiverem entre 7 e 14 anos e estejam marcados no cadastro de dependente a flag de comprovante de frequência escolar.

Porém, foi houve a alteração através do Art. 363 conforme imagem abaixo:

## **04. SOLUÇÃO**

Aplicamos a regra solicitada, então agora no cálculo de Salário Família, quando o dependente for:

* Dependentes válidos com idade entre 4 e 14 anos devem ter comprovado a frequência escolar;

O comprovante de vacina continua valendo até os 6 anos. Logo, se o dependente for menor que 7 anos e foi entregue a caderneta de vacina e não está marcada a frequência escolar, não deve pagar salário família. O Contrário também deve ser observado: O dependente tem mais de 4 anos, entregou o comprovante escolar, mas não entregou a caderneta de vacina, não deve pagar o Salário Família.

## **05. DOCUMENTAÇÃO**

[Link consultoria](https://tdn.totvs.com.br/pages/releaseview.action?pageId=804048743)  
[Doc. Referencia Dependentes](https://tdn.totvs.com/display/LRM/Dependentes)
