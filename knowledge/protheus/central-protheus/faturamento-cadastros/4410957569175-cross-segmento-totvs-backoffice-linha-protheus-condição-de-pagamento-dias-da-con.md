---
article_id: 4410957569175
category: Faturamento - Cadastros
content_hash: 92f316381d1d2aa8c9f164aee9aa25b7d339402e265ed1291a4bd2f3887907b9
fetched_at: '2026-06-28T22:38:35.231319+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Condição de Pagamento
  "Dias da Cond E4_DDD - Fora o Dia"
type: support-article
updated_at: '2023-12-05T15:02:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410957569175-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Condi%C3%A7%C3%A3o-de-Pagamento-Dias-da-Cond-E4-DDD-Fora-o-Dia
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19576051137943) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Qual o conceito do funcionamento do campo "Dias da Cond" (E4\_DDD) - Fora o Dia" na Condição de Pagamento?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.  
  
**Solução**

Fora o dia (pula esse dia); e assim por diante.  
Exemplo, a Data base é dia 18/10 com condição de 10 dias. Irá cair no dia 27 de acordo com o prazo estipulado. Se configurar para "Fora o dia" então, o dia em questão (27) fica "Fora" e será contado para o dia 28.

O sistema irá contar a data do Pedido de Venda com o campo Fora a Data a partir do dia 19/10, com a condição 10 dias, sendo a data final 28/10;

Exemplo:

Pedido de Venda criado 18/10;

Condição de Pagamento 10 dias;  
Duplicata com data 28/10;

![fora_dia.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4410957413655)

Saiba Mais:

[MP - FAT - Qual o parâmetro que define o preenchimento da Data de Entrega na Cópia do Pedido de Venda](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050372634-MP-FAT-Qual-o-par%C3%A2metro-que-define-o-preenchimento-da-Data-de-Entrega-na-C%C3%B3pia-do-Pedido-de-Venda)

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Condições de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017468312-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Condi%C3%A7%C3%B5es-de-Pagamento?source=search)
