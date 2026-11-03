---
article_id: 1500004348661
category: SIGAACD - Automação e Coleta de Dados
content_hash: 5c18c04df7b522f32ca37243dd8e22f934599411e01984b5b4f0fb76fafb21ae
fetched_at: '2026-06-28T22:39:11.140062+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD -  Erro ao Alterar Pedido
  de Venda com Ordem de Separação
type: support-article
updated_at: '2025-03-12T12:45:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004348661-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Erro-ao-Alterar-Pedido-de-Venda-com-Ordem-de-Separa%C3%A7%C3%A3o
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24763527152279) Tempo aproximado para leitura: **00:02:00 min***

**Dúvida**

Ao alterar um Pedido de Venda oriundo de uma Ordem de Separação ocorre o erro "A liberação do Pedido não pode ser alterada pois o mesmo encontra-se amarrado à Ordem de Separação. Consulte o pedido na opção Visualizar". Como alterar um Pedido de Venda amarrado à Ordem de Separação?

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005572141)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da versão 12.1.17  
  
**Solução**Dentro do Protheus padrão, realmente não possível efetuar uma alteração de um Pedido de Vendas que já tenha uma Ordem de Separação atrelada. Desta forma, uma alternativa seria por meio do Ponto de Entrada **[AC100VLA](https://tdn.totvs.com/pages/releaseview.action?pageId=6091031)**, criando regras que permita, dentro da amarração entre as tabelas SC6, CB8 e CB9, a possibilidade de alterar direto no Pedido de Venda.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Automação e Coleta de Dados (ACD)*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360002469152-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
