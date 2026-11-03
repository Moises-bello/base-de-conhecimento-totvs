---
article_id: 35801736878231
category: Materiais - Compras (SIGACOM)
content_hash: 8df31e91f986e91b224171565cabb67ebc05b11fd4c8e5b4c5deba72c28de230
fetched_at: '2026-06-28T22:41:21.810954+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - Help Grupos de
  Produtos Diferentes ao selecionar Solicitações de Compras
type: support-article
updated_at: '2025-10-22T11:53:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35801736878231-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-Help-Grupos-de-Produtos-Diferentes-ao-selecionar-Solicita%C3%A7%C3%B5es-de-Compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35801736870807) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**

Na tela de Necessidade de Compra do Novo Fluxo de Compra, ao selecionar Solicitações de Compras que possuem produtos de grupos de produto diferentes, é gerado help e não permite prosseguir com a geração da cotação. Como proceder?

Grupos de produto diferentes

Só é permitido selecionar itens do grupo de produto "XPTO"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35801758867735)

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras - Protheus Release 12.1.2310

**Solução**

Na tela de Necessidade de Compra do Novo Fluxo de Compras, temos um botão chamado "**Validar Grupo de Produto?"**

A funcionalidade "**Validar Grupo de Produto?"** tem como objetivo garantir que o usuário não selecione um **produto que não pertença ao mesmo grupo de produto**. Essa validação é ativada quando o **interruptor**é acionado e sempre verifica o grupo de produto do **primeiro item selecionado**. Se o produto não possuir um grupo de produto definido, será exibida uma mensagem informando que apenas é possível selecionar itens sem grupo de produtos.  
   
![](https://tdn.totvs.com.br/download/attachments/680260500/grupo%20de%20produtos.gif?version=1&modificationDate=1712875668370&api=v2)

Sendo assim, caso deseje que essa validação não seja realizada e que o help não apareça, basta desligar o interruptor deste botão para que a validação fique desabilitada.

***Saiba Mais:***

[Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Como configurar o WorkFlow no Novo Fluxo de Compras - NFC (PGCA010)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19823527070871-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Como-configurar-o-WorkFlow-no-Novo-Fluxo-de-Compras-NFC-PGCA010)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Novo Fluxo de Compras - NFC (PGCA010)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19838751317655-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Novo-Fluxo-de-Compras-NFC-PGCA010)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
