---
article_id: 37340274516119
category: SIGAACD - Automação e Coleta de Dados
content_hash: 7d1798146e0ace5e634b51f2c24ee0bf7228afa583de15a3424bb9af5cdc1cdc
fetched_at: '2026-06-28T22:39:10.966575+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Como inventariar quantidade
  zero no Mestre de Inventário pelo coletor de dados?
type: support-article
updated_at: '2025-12-30T13:56:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37340274516119-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Como-inventariar-quantidade-zero-no-Mestre-de-Invent%C3%A1rio-pelo-coletor-de-dados
---

Para informar quantidade zero ao digitar um Mestre pelo Coletor de Dados no Protheus, é necessário posicionar manualmente o cursor no campo quantidade, alterar para 0 e retornar à tela anterior com ESC. O sistema exibirá uma mensagem para confirmar com "S". Atenção: se o Mestre não for guiado e possuir vários produtos no endereço, todos serão zerados. Mais detalhes em https://tdn.totvs.com/x/Zu6JLg.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37340274507671) Tempo aproximado para leitura: **01:30 min**

**Dúvida**  
Como informar a quantidade **zero** na digitação, ao inventariar um Mestre pelo Coletor de Dados?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.

**Solução**  
Para que o sistema considere a quantidade **0** no momento da digitação de um Mestre de inventário pelo Coletor de Dados, após informar os dados do mestre e o seletor cai direto para o campo do produto e automaticamente com a quantidade 1.

Dessa forma, é necessário posicionar manualmente no campo quantidade e informar a quantidade **0**, e retornar para a tela anterior (comando **ESC** pelo emulador).

Será apresentado a mensagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37340299575703)

Confirmar apertando **S.**

**OBS:** Caso o Mestre não seja guiado e tenha mais de um produto no endereço, todos os produtos serão zerados.

Veja maiores detalhes: <https://tdn.totvs.com/x/Zu6JLg>

**Saiba Mais:**

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
