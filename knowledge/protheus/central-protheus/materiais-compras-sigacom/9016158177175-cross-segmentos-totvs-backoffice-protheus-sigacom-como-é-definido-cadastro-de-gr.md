---
article_id: 9016158177175
category: Materiais - Compras (SIGACOM)
content_hash: bd39a8e00dde7c8307535c7ea34a3a4060ff9e932adc32c4af30d102da325ca6
fetched_at: '2026-06-28T22:41:15.772826+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como é definido cadastro
  de Grupo de Compras ( COMA086 ) no Módulo de Compras ?
type: support-article
updated_at: '2026-06-22T19:57:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9016158177175-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-%C3%A9-definido-cadastro-de-Grupo-de-Compras-COMA086-no-M%C3%B3dulo-de-Compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32434085450263) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como é definido cadastro de Grupo de Compras ( MATA086 ) no Módulo de Compras ?

**Ambiente**  
  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus compras - Todas as versões  
  
**Solução**  
A funcionalidade do Cadastro de Grupo de Compras (MATA086) e para poder incluir usuários dentro de um determinado Grupo e outros usuários que não pertecerem a esse Grupo **Não** poderão excluir ou alterar Solicitação de Compras ou Pedido de compras.

**Configuração  para Solicitação de Compras.**

1. Para realizar o processo em Solicitação de Compras habilite o parâmetro **MV\_RESTCOM**.
2. É necessários que os usuários que forem vinculados ao Grupo de Compra estejam cadastrados como Compradores acesse Adminstração de Compras>Compradores (COMA087) >incluir para incluir os compradores.
3. Após Cadastrar os Compradores acesse a Rotina Grupo de Compras (COMA086) para que possa incluir os usuário Compradores que poderão realizar as alterações e exclusões de Solicitações.

Vídeo Youtube com a Configuração.

How To| MP-SIGACOM Grupo de Compras COMA086 #TOTVS Backoffice (linha Protheus) <https://www.youtube.com/watch?v=H4d-uXQRJ6k>

**Configuração para Pedido de Compras.**

1. Para Pedido de Compras ative o parâmetro **MV\_RESTPED.**
2. É necessários que os usuários que forem vinculados ao Grupo de Compra estejam cadastrados como Compradores acesse Adminstração de Compras>Compradores (COMA087) >incluir para incluir os compradores.
3. Após Cadastrar os Compradores acesse a Rotina Grupo de Compras (COMA086) para que possa incluir os usuário Compradores que poderão realizar as alterações e exclusões de Pedido de compras.
4. Acesse a Rotina Compradores (COMA087)>Vincule o Código do Grupo de Compras(COMA086).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33686538512023)

**Obs:**

Após incluir o Pedido de compras pelo usuário Comprador conforme as configurações acima, será preenchido o campo **C7\_GRUPCOM**, usuários que não pertecerem ao Grupo vinculado no pedido, não conseguirão alterar ou excluir o pedido, somente os usuário do Grupo de compras que terão acesso ao pedido.

**Configuração de Gera Cotação x Solicitante x Grupo de Compras**

Para garantir que apenas usuários pertencentes ao Grupo de Compras vinculado ao cadastro de Solicitante possam realizar cotações, é necessário configurar a seguinte restrição:

1. Habilite o parâmetro **MV\_RESTCOM = S**
2. Incluir o comprador na Rotina de cadastro de compradores (**COMA087)**
3. Vincular o Comprador na Rotina de Grupo de Compras **(COMA086)**
4. Vincular o Grupo de compras no Cadastro do Solicitante **(MATA084)**

Dessa forma só poderá fazer cotações os usuários que tiverem dentro do Grupo de compras.

***Saiba Mais :***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - O que é o Cadastro de Compradores MATA087 / COMA087 ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024650292-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-O-que-%C3%A9-o-Cadastro-de-Compradores-MATA087-COMA087-?source=search)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Help A120RSPED ao Incluir/Alterar um Pedido de Compras e/ou alterar/excluir uma Solicitação de Compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005050031-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Help-A120RSPED-ao-Incluir-Alterar-um-Pedido-de-Compras-e-ou-alterar-excluir-uma-Solicita%C3%A7%C3%A3o-de-Compras)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
