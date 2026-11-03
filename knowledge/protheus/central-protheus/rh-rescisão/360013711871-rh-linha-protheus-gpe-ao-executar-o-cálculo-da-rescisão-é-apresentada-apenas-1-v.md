---
article_id: 360013711871
category: RH - Rescisão
content_hash: 33f88bc68a7694cd6f0362b9a3de6b73cac16ff6fdaec08a8913029756cf9290
fetched_at: '2026-06-28T22:43:48.476737+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Ao executar o cálculo da rescisão, é apresentada
  apenas 1 verba no cálculo ou nenhuma verba
type: support-article
updated_at: '2026-06-25T12:37:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013711871-RH-Linha-Protheus-GPE-Ao-executar-o-c%C3%A1lculo-da-rescis%C3%A3o-%C3%A9-apresentada-apenas-1-verba-no-c%C3%A1lculo-ou-nenhuma-verba
---

**Ocorrência**Ao executar o cálculo da rescisão, é apresentada apenas 1 verba no cálculo ou nenhuma verba.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da versão 12.  
  
**Causa**Campo **RR\_NUMID**possui um tamanho diferente de 26.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Confirme o cálculo da rescisão mesmo que exista somente 1 verba. A confirmação não será efetivada e será mostrado em qual campo está o erro como no exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360009411171)  
  
2. Geralmente o erro ocorre em ambientes migrados devido ao campo **RR\_NUMID** que na versão 11 possuia 20 posições ter sido migrado para a versão 12, com o mesmo tamanho, **sendo que o correto são 26 posições na versão 12**.

Para realizar a alteração, é necessário abrir o campo **RR\_NUMID** pelo configurador e alterar o conteúdo do tamanho deste campo de 20 para 26 posições.

Para isso, acesso no Configurador a rotina Base de Dados pelo caminho **>Base de Dados >Dicionários >Base de dados**, pesquise pela tabela SRR e altere o tamanho do campo RR\_NUMID

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360009411191)

3. Ao confirmar, é necessário lembrar de clicar no ícone de confirmação verde e depois no ícone do disquete para que a alteração seja efetivada.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360009389492)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360009389532)**

Saiba mais:

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
