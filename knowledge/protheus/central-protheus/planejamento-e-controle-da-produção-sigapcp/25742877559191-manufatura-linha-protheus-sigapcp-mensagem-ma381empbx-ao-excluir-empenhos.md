---
article_id: 25742877559191
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 3bb7fb0fd77f9d74bfa5a2ed4265e7bd0e8d1bcf0caac6c374a02e9484b556b4
fetched_at: '2026-06-28T22:42:44.502453+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem MA381EMPBX ao excluir empenhos
type: support-article
updated_at: '2024-08-19T17:58:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25742877559191-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-MA381EMPBX-ao-excluir-empenhos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25742907030679) Tempo aproximado para leitura: **00:01:14 min****Ocorrência**Ao tentar excluir os empenhos de uma **OP - Ordem de produção** através da rotina **MATA381 - Ajuste de Empenhos Modelo 2** é apresentada a mensagem **MA381EMPBX - Esta Ordem de produção possui empenhos parcialmente baixados e que não podem ser excluído**s.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**Essa mensagem é apresentada quando existem produtos empenhados que já foram totalmente ou parcialmente requisitados. Isto é, quando a quantidade do campo **D4\_QUANT  - Saldo da quantidade** **empenhada** é menor do que o conteúdo do campo **D4\_QTDEORI - Quantidade empenhada.**Empenhos nesta situação não podem ser excluídos.  
  
**Solução**Se houver necessidade de zerar o saldo empenhado de todos os produtos da **OP**, no **MATA381** clique em **Alterar** e na sequência clique em **Zerar Emp**.  
Ou então, através do **MATA381** clique em Alterar e na sequência exclua os componentes que tem o campo **D4\_QUANT** com o mesmo conteúdo do campo **D4\_QTDEORI.**
