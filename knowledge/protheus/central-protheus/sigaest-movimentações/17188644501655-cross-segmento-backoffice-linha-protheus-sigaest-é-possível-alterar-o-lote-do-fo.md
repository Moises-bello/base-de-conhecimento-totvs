---
article_id: 17188644501655
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 2078c8535ae19faafe95cae6bc7534aa863a6a22f1bac2b9358bb1a435be4806
fetched_at: '2026-06-28T22:38:55.458963+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - É possível alterar
  o Lote do Fornecedor (B8_LOTEFOR)?
type: support-article
updated_at: '2023-08-31T21:07:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17188644501655-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-%C3%89-poss%C3%ADvel-alterar-o-Lote-do-Fornecedor-B8-LOTEFOR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17188628226071) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**

É possível alterar o ***Lote do Fornecedor (B8\_LOTEFOR)***? Foi digitado errado o Lote do Fornecedor, o documento de entrada não pode ser estornado, existe alguma rotina, ***como por exemplo*** a Manutenção de Lote (MATA390) que permita alterar essa informação?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

No padrão, atualmente não tem uma rotina ou um processo para ajuste desse campo, somente seria possível estornado a movimentação e incluindo novamente com o conteúdo correto. 

***Importante:*** revisando a funcionalidade do campo ***B8\_LOTEFOR***, o mesmo somente é preenchido quando pelo Documento de Entrada informar o ***Lote do Fornecedor (D1\_LOTEFOR)*** que também atualiza a tabela de movimentos por lote (SD5) o campo ***D5\_LOTEFOR***. a finalidade de utilização desse campo é aumentar o controle de rastreabilidade. Algumas empresas utilizam apenas um Lote específico, outras também utilizam a informação do Lote do Fornecedor, com a finalidade de rastrear as entradas dos lotes.

***Saiba Mais:***

*[SIGAEST - Conceito e tabelas de controle de Lote e Endereço no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018454332-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-tabelas-de-controle-de-Lote-e-Endere%C3%A7o-no-Protheus)*

*[Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
