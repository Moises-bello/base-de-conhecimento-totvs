---
article_id: 360028891972
category: Portal de Gestão de Capital Humano
content_hash: 868b92d930a735346ab71d577b86ea1c33f21c6f242b128e50cf00ce66f48f96
fetched_at: '2026-06-28T22:42:59.129660+00:00'
product: protheus
section_id: 206960887
source: central-protheus
title: RH - Linha Protheus - PORTAL GCH - Avaliação disponível no portal apenas dentro
  da data definida na avaliação
type: support-article
updated_at: '2021-04-07T13:20:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028891972-RH-Linha-Protheus-PORTAL-GCH-Avalia%C3%A7%C3%A3o-dispon%C3%ADvel-no-portal-apenas-dentro-da-data-definida-na-avalia%C3%A7%C3%A3o
---

**Dúvida**Como configurar uma avaliação, para que no portal seja apresentada apenas dentro do período de inicio?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Portal Gestão Capital Humano - Todas as versões  
  
**Solução**Utilize o parâmetro **MV\_APDVDAT,**que controla a apresentação das Avaliações que estão dentro do Prazo determinado para responder.  
  
Lembre-se que os campos da Montagem de Avaliação na Aba **Agenda** são de extrema importância para apresentação da Avaliação, eles determinam e somam-se junto ao Prazo de Avaliação para dispor alguns dias além do prazo inicial.  
  
Campo de Referência: **RD6\_RSP\_DOR** (Informe em quantos dias, em relação a data inicial da resposta da avaliação, será a data limite de resposta do avaliador.)  
  
Exemplo: Determinamos uma avaliação do período do dia **01/06/2019 à 30/06/2019.**  
Se o parâmetro **MV\_APDVDAT** estiver **habilitado,**o sistema considera o dia 01/06/2019 + XX Dias, informados no campo **RD6\_RSP\_DOR** formando assim o prazo estipulado para responder a avaliação.  
  
**Saiba Mais**  
[Artigos Portal Gestão Capital Humano](%C2%A0https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano)
