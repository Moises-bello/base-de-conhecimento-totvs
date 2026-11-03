---
article_id: 1500000620561
category: Portal de Gestão de Capital Humano
content_hash: e35056893148d14942d8795cf29686e0f4d88239f34f841e54dd0742b553ed7e
fetched_at: '2026-06-28T22:43:00.038500+00:00'
product: protheus
section_id: 206960887
source: central-protheus
title: RH - Linha Protheus - PORTAL GCH - É possível solicitar férias com 2 dias que
  antecede ao feriado
type: support-article
updated_at: '2021-04-07T12:16:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000620561-RH-Linha-Protheus-PORTAL-GCH-%C3%89-poss%C3%ADvel-solicitar-f%C3%A9rias-com-2-dias-que-antecede-ao-feriado
---

**Dúvida**Ao solicitar férias com dois dias que antecede ao feriado é apresentado mensagem "A data inicial do período de gozo deve anteceder pelo menos 2 dias ao feriado. Deseja continuar?"  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) -  Portal Gestão do Capital Humano – Todas as versões  
  
**Solução**A mensagem é demonstrada de forma opcional conforme configuração a seguir, para avisar que o gozo das férias será iniciado dois dias antes de um feriado. Ao incluir as informações de férias e a data for menor que 2 dias que antecede a um feriado, é apresentado mensagem informativa:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001122081/mceclip0.png)  
  
**Observação:** O ambiente deve estar atualizado com Binário e pacote Acumulado RH nos RPO Portal e Protheus.   
  
O parâmetro **MV\_REFTRAB** deve estar configurado (F= Férias, S= Contrib. Sindical, R= Regime Parcial, I= Insal.Gest).  
  
No módulo Configurador, acesse o menu *Ambientes > Cadastros > Parâmetros*e filtre o parâmetro:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099634294/mceclip0.png)  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o Portal GCH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano)  
[MP - GPE - Pacote de acumulado do RH no Portal de Cliente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115015741848-MP-GPE-Pacote-de-acumulado-do-RH-no-Portal-de-Cliente)
