---
article_id: 6983309563031
category: Materiais - Compras (SIGACOM)
content_hash: bc093330567512211cfbd18e8bd0c0ba56019242149e8770a9e479ae2d9ebbaa
fetched_at: '2026-06-28T22:41:11.504726+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Ponto de Pedido -
  Envio de E-mail
type: support-article
updated_at: '2025-03-08T17:09:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6983309563031-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Ponto-de-Pedido-Envio-de-E-mail
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30503014546327) Tempo aproximado para leitura: **00:03 min** **Dúvida**Como configuarar Envio de E-mail por Ponto de Pedido ?   
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - Versão 12  
  
**Solução**

Para envio de E-mail, configure o ambiente conforme o Artigo :

**[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Configuração de envio Messenger para ID de eventos do Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003963562-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Configura%C3%A7%C3%A3o-de-envio-Messenger-para-ID-de-eventos-do-Estoque?source=search)**

**Ponto de Pedido ->**Ponto de Pedido é a quantidade em estoque que uma vez atingida, pode iniciar o processo de compra a partir da **Geração de Solicitações de Compras por ponto de pedido.**

Toda vez que o Sistema detectar a falta de um material, somando saldo em estoque, pedidos e solicitações de compras em aberto e esta for menor que o Ponto de Pedido definido em seu cadastro de Produto é gerado uma **Solicitação de Compras**.

**Para Cadastrar Ponto de Pedido, seguir os procedimentos :**

**1. Event Viewer;**

![Event_v.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6983189815959)

**2.   Cadastros → Produtos> Incluir Produto e Acesse a Aba MRP / Suprimentos;**

![MRP.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6982834922007)

**Ponto de Pedido**: É neste campo que informamos a quantidade Mínima para o estoque, que uma vez atingida, pode iniciar o processo de compras a partir da Geração de Solicitação de Compras por ponto de pedido.

**3. Solicitação ao Armazém;**

A *Solicitação ao Armazém* representa a requisição de um ou mais produtos por um setor ou indivíduo específico da empresa, podendo ou não estar vinculada a uma Ordem de Produção. Podemos considerar, como exemplo, a requisição de materiais de escritório ao almoxarifado.

![mata105.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6982947270295)

**4. Gerar Pré-Requisição**

Todas as Solicitações ao Armazém (SA) podem tornar-se pré-requisições, mediante seleção dos itens pelo responsável por esta geração.

Esta pré-requisição tem como base os dados constantes da SA gerada, enviada ao Armazém e, dependendo do estoque atual disponível dos produtos solicitados, o Sistema gera automaticamente as Solicitações de Compra (SC) destes produtos.

De acordo com a parametrização da rotina, o material pode ser disponibilizado pela data imposta no campo Necessidade da SA, ou pela sua data de emissão;

**5. Baixa Pré-Requisão;**

![baixa_pre.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6982957610519)

![20220623_134901.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/6983193845143)

**OBS :** Em caso de dúvidas no processo do Messenger Ponto de Pedido, Evento 001, entrar em contato com o Suporte ao Modulo Estoque e Custos.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033382-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
