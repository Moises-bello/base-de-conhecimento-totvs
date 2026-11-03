---
article_id: 16700548157207
category: Gestão de Distribuição (SIGAOMS)
content_hash: 3af6d0189683397b0b0936ac0e493770412c97476121f5013c70f5398cbc584d
fetched_at: '2026-06-28T22:45:49.791073+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Determinar o tipo do peso que será utilizado
  na Montagem de Carga
type: support-article
updated_at: '2023-08-14T14:25:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16700548157207-Log%C3%ADstica-Linha-Protheus-OMS-Determinar-o-tipo-do-peso-que-ser%C3%A1-utilizado-na-Montagem-de-Carga
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16700523709591) Tempo aproximado para leitura: **00:01:36 min** **Dúvida**Como determinar o **tipo do peso** que será utilizado na **Montagem de Carga - OMSA200**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**O **tipo do peso** a ser considerado na **Montagem de Carga - OMSA200** pode ser **Liquido** ou **Bruto**. Para determinar isso, o Sistema verificará o conteúdo informado no parâmetro **MV\_PESOCAR - Indica o tipo do peso a ser usado na montagem de cargas e relatórios de cargas**.

1. Quando o parâmetro **MV\_PESOCAR** estiver com **L**, será considerado o **Peso Liquido - B1\_PESO** informado no **Produto - MATA010**.
2. Quando o parâmetro **MV\_PESOCAR** estiver com **B**, será considerado o **Peso Bruto - B1\_PESBRU** informado no **Produto - MATA010**.

O **tipo do peso** informado no parâmetro **MV\_PESOCAR** será utilizado na **Montagem de Carga** e também nos **relatórios** do módulo **TOTVS OMS.  
  
Importante**Se desejado alterar o tratamento descrito acima, poderá ser utilizado o ponto de entrada **OM200PES**, que permite informar o peso variável do item do pedido de venda utilizado na **Montagem de Carga**.   
No tópico **Saiba mais**, segue artigo com a documentação desse ponto de entrada, bem como dos demais pontos de entradas disponíveis na Montagem de Carga.  
  
**Saiba mais**Abaixo destacamos o *link* com todos os pontos de entrada disponíveis na Montagem de Carga:  
[Logística - Linha Protheus - OMS - Pontos de Entrada disponíveis na rotina Montagem de Carga - OMSA200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000900021-Log%C3%ADstica-Linha-Protheus-OMS-Pontos-de-Entrada-dispon%C3%ADveis-na-rotina-Montagem-de-Carga-OMSA200)
