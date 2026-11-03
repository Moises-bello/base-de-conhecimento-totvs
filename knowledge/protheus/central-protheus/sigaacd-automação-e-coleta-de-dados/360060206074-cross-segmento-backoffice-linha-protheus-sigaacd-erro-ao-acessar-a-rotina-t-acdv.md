---
article_id: 360060206074
category: SIGAACD - Automação e Coleta de Dados
content_hash: ec99c5c7edabdd03a8ee0a3e71f199d3adc71161167c5286a8c839c198ee61a7
fetched_at: '2026-06-28T22:39:12.703583+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Erro ao acessar a
  rotina T_ACDV130 (Movimentação interna)
type: support-article
updated_at: '2025-03-12T12:42:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060206074-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Erro-ao-acessar-a-rotina-T-ACDV130-Movimenta%C3%A7%C3%A3o-interna
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24763468215063) Tempo aproximado para leitura: **00:01:00 min***  
**Dúvida**Erro ao acessar a rotina ACDV130(Movimentação interna): 

Erro /0 InterFunctionCall: cannot find function T\_ACDV130 in AppMap: T\_ACDV130:![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100450234)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da versão 12.1.25   
  
**Solução**

Identificado no ambiente do cliente através da pasta System dele o arquivo SIGAACD.XNU

estava dessa forma conforme a imagem  abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001559242)

Ao retirar essa validação informado na função e deixado dessa forma Function ACDV130 o error.log parou de ocorrer.

**Saiba Mais:**  
[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23970894011799-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Configurar-Local-de-impress%C3%A3o-ACDA060-para-utilizar-na-impress%C3%A3o-de-Etiquetas#:~:text=Saiba%20Mais%3A,Coleta%20de%20Dados)
