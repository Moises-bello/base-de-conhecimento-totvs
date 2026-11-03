---
article_id: 38836592258711
category: SIGAEST - MOVIMENTAÇÕES
content_hash: f165d86ec172dd0922b3353a76a6ed5224ad049c7a61d1f35a66145cb68084b3
fetched_at: '2026-06-28T22:38:57.087004+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA270 - Campo "Código"
  está vindo preenchido automaticamente. Como corrigir?
type: support-article
updated_at: '2026-03-05T21:55:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38836592258711-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA270-Campo-C%C3%B3digo-est%C3%A1-vindo-preenchido-automaticamente-Como-corrigir
---

No TOTVS Protheus, para evitar que o campo Código (B7\_COD) seja preenchido automaticamente na inclusão de um novo produto no inventário, deve-se pressionar F12 na rotina de Digitação do Inventário (MATA270) e definir a opção "Sugere inform. inventário?" como "Não Sugere". Assim, o campo ficará vazio ao adicionar um produto.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38836592248599) Tempo aproximado para leitura: **00:01:17min**  
  
**Dúvida**  
Na inclusão de um novo produto a ser inventariado, o campo Código (B7\_COD) vem preenchido automaticamente com um código de produto. Como fazer com que não venha preenchido?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Para que o campo Código não venha preenchido, basta pressionar o F12 na tela da rotina de Digitação do Inventário (MATA270) e parametrizar a pergunta "**Sugere inform. inventário?**" = **Não Sugere**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38836592250135)

Assim, ao incluir uma digitação, o campo reservado ao código do produto virá vazio:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38836585944471)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/38836592258711/live_preview/01KJZVY3MM53BWP8CJJPDH5YD5)
