---
article_id: 9649411006743
category: MDT - Atendimento Médico
content_hash: 02e25f422ce33c4c77018288eecc6f6ef42f96daa805e2825fedcd30ca8f4f3e
fetched_at: '2026-06-28T22:44:20.530777+00:00'
product: protheus
section_id: 360010945694
source: central-protheus
title: RH - Linha Protheus - MDT - Ao realizar atendimento Médico e informar o horário
  da consulta, porque é apresentado a mensagem horário Inválido. "Favor informar um
  horário válido sendo necessário terminar em 0 ou 5."
type: support-article
updated_at: '2025-03-12T20:53:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9649411006743-RH-Linha-Protheus-MDT-Ao-realizar-atendimento-M%C3%A9dico-e-informar-o-hor%C3%A1rio-da-consulta-porque-%C3%A9-apresentado-a-mensagem-hor%C3%A1rio-Inv%C3%A1lido-Favor-informar-um-hor%C3%A1rio-v%C3%A1lido-sendo-necess%C3%A1rio-terminar-em-0-ou-5
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25588771487127) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Ao realizar atendimento Médico e informar o horário da consulta, porque é apresentado a mensagem horário Inválido. "**Favor informar um horário válido sendo necessário terminar em 0 ou 5**."  
Existe a possibilidade de configurar para não realizar esta validação?  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9649413622935)  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**Não temos como alterar esta validação, pois o sistema valida algumas informações do atendimento Médico em si, relacionado a quantidade mínima de atendimento, horários subdivididos de 5 em 5 minutos, são horários validos e disponíveis, ainda que esteja utilizado a rotina ficha Médica ou prontuário médico o sistema fará referencia a agenda médica para a definição.   
Referencias sistêmicas, **Calendário** (*TMK\_Calend*) e a **Quant. Horas** (*TMK\_QTDHRS*) padrão na inclusão de um médico.  
  
Representação do agendamento no sistema para horário de consulta. Exemplo consulta de 15 minutos, cada 5 minutos corresponde a 1 célula da imagem abaixo.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9649335920151)  
  
Maiores informações consulte: [Agenda Médica Modelo 2](https://tdn.totvs.com/display/public/PROT/197739+MNG-897+DT+Agenda+Medica+Mod+2)  
  
**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
