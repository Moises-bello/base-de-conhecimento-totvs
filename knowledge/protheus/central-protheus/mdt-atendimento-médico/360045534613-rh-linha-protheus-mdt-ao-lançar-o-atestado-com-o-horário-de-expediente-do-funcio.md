---
article_id: 360045534613
category: MDT - Atendimento Médico
content_hash: 427dbe3104a11b3c99db96e5d9f9d9607adbba88f3f69005d4f841ee674eee9b
fetched_at: '2026-06-28T22:44:20.527388+00:00'
product: protheus
section_id: 360010945694
source: central-protheus
title: RH - Linha Protheus - MDT - Ao lançar o atestado com o horário de expediente
  do funcionário, não é apresentado a quantidade de dias de afastamento corretamente
  no campo Dias Afast (TNY_QTDIAS)
type: support-article
updated_at: '2025-03-03T18:19:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045534613-RH-Linha-Protheus-MDT-Ao-lan%C3%A7ar-o-atestado-com-o-hor%C3%A1rio-de-expediente-do-funcion%C3%A1rio-n%C3%A3o-%C3%A9-apresentado-a-quantidade-de-dias-de-afastamento-corretamente-no-campo-Dias-Afast-TNY-QTDIAS
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23283060652055)**Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Ao lançar o atestado com o horário de expediente do funcionário, não é apresentado a quantidade de dias de afastamento corretamente no campo Dias Afast (**TNY\_QTDIAS**).  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as Versões  
  
**Causa**O sistema efetua o cálculo das horas lançadas e gera o resultado para o campo "Dias Afast" (**TNY\_QTDIAS**):

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8496531644183)  
  
**Solução**No menu Atualizações > Atendimento Médico > Atendimento Médico (MDTA685), deve ser lançado no campo Hora Inic (**TNY\_HRINIC)** a hora 00:00 e Hora Fim (**TNY\_HRFIM**) 23:59.  
Dessa forma o Sistema irá calcular 24 horas horas e lançar 01 dia para cada dia de afastamento.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8496531644183)  
  
Veja que na aba "Afastamento" foi calculado 15 dias de acordo com o preenchimento dos campos "Inic.Afast" e "Data Fim".  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8496569571223)  
  
**Saiba Mais**  
[Artigos Atendimento Médico](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945694-MDT-Atendimento-M%C3%A9dico)  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206971487-RH-Medicina-e-Seguran%C3%A7a-do-Trabalho%20)  
[ChatBot Carol](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
