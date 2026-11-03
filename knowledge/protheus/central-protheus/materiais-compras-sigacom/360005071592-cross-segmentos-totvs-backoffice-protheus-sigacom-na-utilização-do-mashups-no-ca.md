---
article_id: 360005071592
category: Materiais - Compras (SIGACOM)
content_hash: 624548a75e70e6671a6151b1ffde689e88f0841b5e6f31bcf650b2e107d86d97
fetched_at: '2026-06-28T22:41:09.046872+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Na utilização do mashups
  no cadastro do fornecedor ocorre erro "Failed to create OpenGL context for format
  QFlags()... "
type: support-article
updated_at: '2022-05-13T11:40:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005071592-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Na-utiliza%C3%A7%C3%A3o-do-mashups-no-cadastro-do-fornecedor-ocorre-erro-Failed-to-create-OpenGL-context-for-format-QFlags
---

**Dúvida**Como resolver o erro "Failed to create OpenGL context for format QFlags()... " quando utiliza o recaptcha do mashups no cadastro do fornecedor?

**Ambiente**  
Protheus – Compras – A partir da versão 12.1.17  
  
**Solução**

Conforme instruções passada pela equipe de Framework seguir com o procedimento abaixo:

Nas maquinas que ocorre o erro "Failed to create OpenGL context for format QSurfaceFormat(version 2.0, options QFlags()... " é pelo fato que o drive de vídeo e o SO estão desatualizados.  
  
A Ferramenta Recaptcha.exe foi criada para solucionar a necessidade do Mashup e essa ferramenta utiliza recursos da OpenGL2.0 e necessita de recursos não disponíveis no drive de vídeo do Usuário.   
  
Atualize o sistema operacional e Drive de vídeo das maquinas que ocorre o erro.

Persistindo, Favor abrir um ticket para equipe de Framework vincular a melhoria aberta do ticket [MTEC-1751](http://jiraproducao.totvs.com.br/browse/MTEC-1751) referente ao recaptcha do Mashups para versões de placas de vídeo sem suporte a OpenGL2.0.

Abaixo a tela do erro e a consulta Mashups:

![Capturar9.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360006724931/Capturar9.JPG)

![Capturar7.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360006688372/Capturar7.JPG)

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
