---
article_id: 9345133921175
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 676d05ef219c9641181e3889a4322f8f0d2d5e8533751c080a9b782c16d00ba1
fetched_at: '2026-06-28T22:37:21.413310+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Campos de Retenção
  de ISS de Pedidos de Vendas gerados pela Medição não são preenchidos
type: support-article
updated_at: '2024-08-20T11:35:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9345133921175-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Campos-de-Reten%C3%A7%C3%A3o-de-ISS-de-Pedidos-de-Vendas-gerados-pela-Medi%C3%A7%C3%A3o-n%C3%A3o-s%C3%A3o-preenchidos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Campos de Retenção de ISS de Pedidos de Vendas gerados pela Medição não são preenchidos.

Ao gerar uma Pedido de Venda pela rotina de Medição, os campos C5\_ESTPRES, C5\_MUNPRES e C5\_RECISS utilizados para geração de título de retenção de ISS não são preenchidos.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões  
  
**Solução**Por padrão do módulo de Gestão de Contratos, ele não possui campos relacionados a Impostos para serem preenchidos e posteriormente levada a informação para os documentos gerados na medição neste caso os Pedidos de Vendas.

Estes campos informados relacionados a retenção de ISS de fato não são preenchidos quando o pedido é gerado pelo módulo de Gestão de Contratos.

Pelo padrão do sistema, os pedidos gerados pelo SIGAGCT possuem abertura para alteração de alguns campos, e a forma de preenchimento destes campos é, após serem gerado pelo SIGAGCT, através da rotina de Pedido de Vendas (MATA410) alterar o Pedido e realizar o preenchimento manualmente do campos, conforme imagem abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9344910446743)

Caso se deseje realizar o preenchimento dessas informações ou outras nos pedidos de venda de forma automática na medição, pode-se avaliar a possibilidade através de uma customização conforme a necessidade.  
Abaixo artigo disponível com pontos de entrada da rotina:  
  
[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Pontos de entrada para rotinas de Medição](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022685112-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Pontos-de-entrada-para-rotinas-de-Medi%C3%A7%C3%A3o?source=search)  
  
  
*Se precisar de apoio no desenvolvimento do Ponto de Entrada, sugerimos a verificação e apoio junto a um analista especialista desenvolvedor em loco, através de seu ESN Totvs.*  
  
Dúvidas e dicas referente a como realizar desenvolvimento de customizações, sugerimos a que seja reportado ao nosso portal oficial de desenvolvedores.([https://devforum.totvs.com.br](https://devforum.totvs.com.br/))  
  
Caso sua dúvida seja referente a utilização de alguma função AdvPL, deverá ser aberto um ticket para a equipe de AdvPL.

***Saiba Mais:***

* [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Alteração de Pedidos de Vendas / Compras gerados pelo Gestão de Contratos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000675988-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Altera%C3%A7%C3%A3o-de-Pedidos-de-Vendas-Compras-gerados-pelo-Gest%C3%A3o-de-Contratos?source=search)
* [Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
