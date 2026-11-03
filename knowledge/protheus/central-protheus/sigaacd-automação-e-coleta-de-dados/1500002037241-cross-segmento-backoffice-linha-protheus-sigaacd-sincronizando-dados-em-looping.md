---
article_id: 1500002037241
category: SIGAACD - Automação e Coleta de Dados
content_hash: 264bb42c29ca750f32b8e6c48d81789b5cd161cd6c05a0d11d2aea43d5f2e9d6
fetched_at: '2026-06-28T22:39:13.824716+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Sincronizando Dados
  em Looping
type: support-article
updated_at: '2025-03-12T12:45:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002037241-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Sincronizando-Dados-em-Looping
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24763619957271) Tempo aproximado para leitura: **00:01:00 min***

**Dúvida** No Meu Coletor, ao clicar na opção "Sincronizar Dados" o processo fica executando por muito tempo e entra em Looping.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001951822)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da versão 12.1.23  
  
**Solução**

Normalmente este tipo de lentidão ocorre quando existe uma grande quantidade de produtos cadastrados. Para melhora na performance, crie os seguintes parâmetros:  
**MV\_MCDPRSL** : .T.

**MV\_MCDTPPR:** PA

Para melhoria de performance, no parâmetro MV\_MCDTPPR, basta selecionar apenas um tipo de produto.

**Saiba mais:**

*[Validação dos parâmetros MV\_MCDPRSL e MV\_MCDTPPR](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=546686576)*

*[Clique aqui e veja mais artigos sobre Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360002469152-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)*
