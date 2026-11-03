---
article_id: 41143819145751
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: ca454fac72ef2ca81ee10798694fa9d43b4ab530d51653618ddac59a6bda2ee8
fetched_at: '2026-06-28T22:37:21.718156+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Contratos cadastrados
  em Outras Moedas no Gestão de Contratos
type: support-article
updated_at: '2026-06-12T20:48:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41143819145751-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Contratos-cadastrados-em-Outras-Moedas-no-Gest%C3%A3o-de-Contratos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41143819136535) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**

Contratos cadastrados em Outras Moedas

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos Fiscal - Todas as versões

**Solução**

Abaixo informações sobre o comportamento do padrão do módulo no contrato cadastrado com outras moedas:

Um contrato quando cadastrado com outra moeda (dólar, por exemplo), pelo conceito do módulo, significa que os valores inseridos em seu cadastro são na moeda que foi informada no cabeçalho do contrato.

O modulo não possui funcionalidade de converter, por exemplo, os valores do cronograma financeiro para a moeda corrente, onde como informado acima, no contrato cadastro em dólar significa que as informações inseridas no cronograma financeiro são em dólar.

Quanto aos títulos Provisórios (PR) referente às parcelas do Cronograma Financeiro, estes títulos, quanto a sua moeda, serão gerados conforme a configuração do parâmetro ***MV\_CNMOEDA***, onde:

* Quando ele estiver como "S" será gerado com a moeda do contrato,
* e se estiver como "N" será gerado com a moeda corrente, convertido conforme a taxa do dia que o contrato se torno vigente que os títulos foram criados.

Este parâmetro tem seu funcionamento apenas referente aos títulos PR do cronograma, conforme sua descrição.

No encerramento da medição, os Pedidos ou Títulos gerados nesse encerramento, por padrão, serão sempre gerados conforme a moeda do contrato (outra moeda).

E no caso da NF feita com o Pedido na outra moeda, o processo já é no módulo de Compras conforme o seu comportamento, onde com o vínculo de Pedidos de outras moedas, o valor na NF é convertido para a moeda corrente.

***Saiba Mais:***

[GCT0146\_Como utilizar o parâmetro MV\_CNMOEDA](https://tdn.totvs.com/x/Mr07Jg)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
