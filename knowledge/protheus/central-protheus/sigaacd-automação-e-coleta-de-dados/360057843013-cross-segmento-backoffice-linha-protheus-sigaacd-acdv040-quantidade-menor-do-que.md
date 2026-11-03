---
article_id: 360057843013
category: SIGAACD - Automação e Coleta de Dados
content_hash: 9e26a6403f81c78b439dd5b342502e1328478bcc8995d8645e6bad451582db6a
fetched_at: '2026-06-28T22:39:11.238267+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - ACDV040 - Quantidade
  menor do que a quantidade da etiqueta
type: support-article
updated_at: '2025-03-12T12:45:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057843013-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-ACDV040-Quantidade-menor-do-que-a-quantidade-da-etiqueta
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24763814432919) Tempo aproximado para leitura: **00:01:20 min***  
**Dúvida**

Na rotina ACDV040 ao realizar a requisição via ACD é gerado o alerta "Quantidade menor do que a quantidade da etiqueta".  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da versão 12.1.25  
  
**Solução**Esse tipo de validão é padrão do sistema, pois é acionada após a validação da quantidade da etiqueta para esse tratamento pode ser utilizado esse ponto de entrada ACD040QE segue a documentação no link abaixo do ponto.

<https://tdn.totvs.com/display/public/mp/ACD040QE+-+Valida+quantidade+a+ser+requisitada+na+Req.+de+materias+por+OPCentro+de+Custo+--+110503> 

Sobre a validação,  não se trata de erro, ela existe exatamente para impedir que seja informada uma quantidade menor do que foi configurado na etiqueta, caso necessite de quantidade variável, defina através do SB5 no campo B5\_QTDVARou ainda utilize o ponto de entrada *CBQTDVAR :*  
*<https://tdn.totvs.com/pages/releaseview.action?pageId=6091003>*

***Saiba Mais:**  
[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23970894011799-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Configurar-Local-de-impress%C3%A3o-ACDA060-para-utilizar-na-impress%C3%A3o-de-Etiquetas#:~:text=Saiba%20Mais%3A,Coleta%20de%20Dados)*
