---
article_id: 1500000673121
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: fd71cc455584e35df0f1c4a537ac1bb44c7a975c350fb5a9054420650f0abb2e
fetched_at: '2026-06-28T22:42:47.287370+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: 'MP - SIGAPCP - Mensagem: Não existem registros para importação com os filtros
  selecionados'
type: support-article
updated_at: '2021-03-01T13:07:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000673121-MP-SIGAPCP-Mensagem-N%C3%A3o-existem-registros-para-importa%C3%A7%C3%A3o-com-os-filtros-selecionados
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:50 min**  
**Ocorrência**No módulo do **PCP - Planejamento e Controle da****Produção** ao tentar realizar a importação de **Pedidos de Venda** no **PCPA136 - Demandas do MRP** é apresentada o *help*:**Help Problema: Não existem registros para importação com os filtros selecionados.**  
 **Ambiente**Microsiga Protheus - Planejamento e Controle da Produção - Versão 12  
  
**Causa**A mensagem pode ser apresentada por causa da **TES -Tipo de Entrada e Saída** ou do filtro utilizado.  
  
**Solução**Para solucionar essa ocorrência, verifique os seguintes itens:

1. Se o filtro utilizado na importação está contemplando o item do pedido;
2. Se a **TES** está configurada para **Atualizar Estoque - F4\_ESTOQUE** igual a **S - Sim**.
