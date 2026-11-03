---
article_id: 360057045994
category: SIGAACD - Automação e Coleta de Dados
content_hash: 9058eba88e4312eca407bb6ce5a63ebc64bb9f4ec8b58e51c065ae69b894116e
fetched_at: '2026-06-28T22:39:11.424120+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - B1_CODBAR (Código
  de Barras) com tamanho 15 caracteres.
type: support-article
updated_at: '2025-03-12T12:42:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057045994-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-B1-CODBAR-C%C3%B3digo-de-Barras-com-tamanho-15-caracteres
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24763877035543) Tempo aproximado para leitura: **00:01:10 min***

**Dúvida**

Quando informa 15 caracteres no campo B1\_CODBAR aparece a mensagem abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096836514)  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da versão 12.1.25

**Solução**

Para solucionar a mensagem acima temos um parâmetro **MV\_ACDVLBA**que permite o sistema informar 15 caracteres normalmente, segue uma documentação do parâmetro.

<https://tdn.totvs.com/pages/releaseview.action?pageId=273988711>

OBS: Além de desativar o parâmetro, pode ter casos de seja necessário excluir também o gatilho do campo B1\_CODBAR .

**Saiba Mais:**  
[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23970894011799-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Configurar-Local-de-impress%C3%A3o-ACDA060-para-utilizar-na-impress%C3%A3o-de-Etiquetas#:~:text=Saiba%20Mais%3A,Coleta%20de%20Dados)
