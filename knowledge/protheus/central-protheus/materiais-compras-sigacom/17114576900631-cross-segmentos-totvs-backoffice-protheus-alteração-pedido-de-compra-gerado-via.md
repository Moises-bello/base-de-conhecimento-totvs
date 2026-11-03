---
article_id: 17114576900631
category: Materiais - Compras (SIGACOM)
content_hash: 859de88e4fda34ec6bb2a3113bdd9528eb19a502972946cf2baa8c291b0acf86
fetched_at: '2026-06-28T22:41:12.848230+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - Alteração pedido de compra gerado
  via Cotação
type: support-article
updated_at: '2023-08-29T13:46:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17114576900631-Cross-Segmentos-Totvs-Backoffice-Protheus-Altera%C3%A7%C3%A3o-pedido-de-compra-gerado-via-Cota%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17114569393303) Tempo aproximado para leitura: **00:02 min** **Dúvida**

O sistema permite alterar um PC ainda "pendente" que foi gerado através da Análise de Cotação, sem que o processo de cotação seja obrigatoriamente revisado, não emite um alerta informando da integridade com a Cotação.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - A partir da Versão 12  
  
**Solução**Foi realizada manutenção na rotina de pedidos de compra (MATA120), por meio da criação do parâmetro MV\_APEDCOT, para que verifique a integridade do pedido com a cotação que o gerou.  
Ao configurar o parâmetro MV\_APEDCOT com .F. o sistema não irá permitir alterar um pedido de compra que foi gerado via cotação.  
O pedido poderá ser excluído normalmente.

Nome da Variável: MV\_APEDCOT

Tipo: Lógico

Descrição: Permite alterar os pedidos de compra gerados via cotação. (.T.) Permite (.F.) Não permite. 

 Valor Padrão: .T.

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como Gerar Cotação ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417420194455-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-Gerar-Cota%C3%A7%C3%A3o-?source=search)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
