---
article_id: 28002527404695
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 997e01417a691868c137e40073cff1b0eeaee9b54ed73d711343abe516a11503
fetched_at: '2026-06-28T22:38:33.011372+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Acessos no configurador do
  Faturamento
type: support-article
updated_at: '2024-11-22T22:20:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28002527404695-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Acessos-no-configurador-do-Faturamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28002541554199) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Quais são os acessos no configurador do módulo Faturamento?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**Acessos de usuários (tópico 4: [Permissões, acessos e privilégios no Protheus](https://tdn.totvs.com/x/tEZpMg)) no configurador correspondentes ao módulo faturamento (SIGAFAT):

|  |  |  |  |
| --- | --- | --- | --- |
| ACESSO | DESCRIÇÃO | EXPLICAÇÃO | ROTINAS |
| 20 e 21 | Alterar pedidos de venda (20) e Excluir pedidos de venda (21) | Define se o usuário possui acesso para alterar (20) ou excluir (21) pedido de vendas | Sugestão Orçamento - MATA405  Pedidos de Venda - MATA410 |
| 51 | Emitir NF retroativa | Define se o usuário tem permissão para emitir NF retroativas (anteriores a DATABASE) | Documento de Saída - MATA460A |
| 107 | Formação de preço | Indica se é permitido acesso à planilha de formação de preços | Pedidos de Venda - MATA410  Tabela de preços - OMSA010 |
| 136 | Lib. ped. venda (crédito) | Define se o usuário tem permissão para liberação de crédito. | Liberação de Estoque - MATA450 |
| 137 | Lib. ped. venda (estoque) | Define se o usuário tem permissão para liberação de estoque. | Liberação de Estoque - MATA455 |
| 166 | Geração de Forecast | Define se o usuário tem permissão para gerar a proposta e definir o forecast. | Oportunidades - FATA300 |
