---
article_id: 360046030993
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 14cff20cd9e348c461ff387fb6e91654b3789da8bebb896d297cc4dc61df2e33
fetched_at: '2026-06-28T22:38:41.038835+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT)
  - HELP FWFORMCANCEL ao excluir controle de reservas
type: support-article
updated_at: '2022-12-30T18:50:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046030993-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-HELP-FWFORMCANCEL-ao-excluir-controle-de-reservas
---

**Dúvida**Ao tentar excluir um registro de reserva no cadastro de reservas (MATA430), o sistema gera a mensagem FWFORMCANCEL, como resolver?

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063546874/mceclip2.png)

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) -

**Solução**

A mensagem informa que esta reserva encontra-se associado em um pedido da  base, portanto não poderá ser excluído, para não gerar falha de integridade com o banco.  
  
Se for reserva manual, esta que inclui no cadastro de reserva e depois associa ao pedido via campo **C6\_RESERVA**, basta buscar em seus pedidos, qual que possui o número de reserva apresentado no cadastro, depois altere o pedido e exclua a informação do campo de reserva, assim poderá excluir o registro da reserva no cadastro.  
  
Se for automática, via parâmetro **MV\_RESEST**, habilite o parâmetro **MV\_DELRES** e estorne a liberação do pedido, deixando-o em aberto, assim a reserva será estornada.  
  
Se o campo **C6\_RESERVA** não estiver no browse do pedido, via configurador, habilite para usado e no browse, atualize a tabela e o dicionário de dados, depois reinicie o Smartclient para que fique visível na alteração do pedido de venda (**MATA410**).

**Saiba mais:** <https://tdn.totvs.com/display/public/PROT/FAT0131_Rotina_MATA430_Controle_de_Reservas_B2_RESERVA>
