---
article_id: 37664596026263
category: SIGAACD - Automação e Coleta de Dados
content_hash: 72772c0809d0909e88de1368275c6623179eee39901c54adad97ebfe9394c837
fetched_at: '2026-06-28T22:39:10.936075+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - ACDA100 Regras de
  Aglutinação de Pedidos de Venda na Ordem de Separação
type: support-article
updated_at: '2026-01-14T12:09:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37664596026263-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-ACDA100-Regras-de-Aglutina%C3%A7%C3%A3o-de-Pedidos-de-Venda-na-Ordem-de-Separa%C3%A7%C3%A3o
---

O artigo explica as possibilidades de aglutinação de itens nas Ordens de Separação do ACDA100, detalhando quatro configurações: sem aglutinação de pedidos nem armazéns, aglutinação apenas de armazéns, aglutinação apenas de pedidos e aglutinação de ambos, condicionando a geração das ordens conforme cliente/loja e armazém dos itens.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37664596019735) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Quais as possibilidades de aglutinação itens nas Ordens de Separação do ACDA100  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**  
Os pedidos de venda serão aglutinados na Ordem de Separação da seguinte forma de acordo com as configurações das perguntas abaixo:  
  
**Aglutina Pedidos = Não / Aglutina Armazém = Não**  
Será gerada uma Ordem de Separação para cada pedido de vendas.  
Caso um pedido de venda possua itens com armazéns diferentes, será gerada uma Ordem de Separação diferente para cada item/armazém.  
  
**Aglutina Pedidos = Não / Aglutina Armazém = Sim**  
Será gerada uma Ordem de Separação para cada pedido de vendas.  
Mesmo que o pedido de venda possua itens com armazéns diferentes, todos os itens do pedido serão considerados na mesma Ordem de Separação.  
  
**Aglutina Pedidos = Sim / Aglutina Armazém = Não**  
Pedidos de venda serão aglutinados em uma mesma Ordem de Separação desde que sejam do mesmo cliente/loja.  
Caso um pedido de venda possua itens com armazéns diferentes, será gerada uma Ordem de Separação diferente para cada item/armazém.  
  
**Aglutina Pedidos = Sim / Aglutina Armazém = Sim**  
Pedidos de venda serão aglutinados em uma mesma Ordem de Separação desde que sejam do mesmo cliente/loja.  
Mesmo que o pedido de venda possua itens com armazéns diferentes, todos os itens do pedido serão considerados na mesma Ordem de Separação.  
  
**Saiba mais:**  
[ACDA100 - Regras de Aglutinação de Pedidos de Venda na Ordem de Separação](https://tdn-homolog.totvs.com/pages/releaseview.action?pageId=619129430)  
[*Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
