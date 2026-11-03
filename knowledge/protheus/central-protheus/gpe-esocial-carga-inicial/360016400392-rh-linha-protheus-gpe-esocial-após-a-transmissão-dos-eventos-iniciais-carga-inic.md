---
article_id: 360016400392
category: GPE - eSocial - Carga Inicial
content_hash: 5f1988da8f3693782667049e472959896be21ee89a9ad6d0bd6870df7c9fc7d5
fetched_at: '2026-06-28T22:45:03.101760+00:00'
product: protheus
section_id: 360005445833
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - Após a transmissão dos eventos iniciais
  (carga inicial), como enviar um único registro de Horários/Turnos de trabalho para
  o TAF
type: support-article
updated_at: '2023-11-30T18:34:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016400392-RH-Linha-Protheus-GPE-eSocial-Ap%C3%B3s-a-transmiss%C3%A3o-dos-eventos-iniciais-carga-inicial-como-enviar-um-%C3%BAnico-registro-de-Hor%C3%A1rios-Turnos-de-trabalho-para-o-TAF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19457706420375) Tempo aproximado para leitura: 01:00 min****Dúvida**Após a transmissão dos eventos iniciais (carga inicial), como enviar Horários/Turnos de trabalho para o TAF  de forma individual?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**Desde o leiaute S-1.0, vigente em 19/07/2021 o evento S-1050 (Tabela de Horários/Turnos de Trabalho) foi descontinuado.  
  
As informações do Horários/Turnos de Trabalho devem ser enviados no cadastro do trabalhador (enviado pelo S-2200) e nas alterações contratuais (enviado pelo S-2206).  
  
Em ambos os eventos, as informações são enviadas no grupo de informações [horContratual](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s1.1-nt-01-2023/index.html#r_2200_vinculo_infoContrato_horContratual):  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19457706432663)

**Observação**:  
Quando alterado informações no cadastro do horário ou turno em algum dos campos que tem impacto com o eSocial, será enviado a alteração do contrato de trabalho dos trabalhadores que estão ativos no turno alterado.   
  
A alteração só será integrada com o TAF se o Job Schedule estiver parametrizado para a (**lAltTurno**- Informa se deve ou não executar a rotina de troca de turno).  
  
Para mais informações do Job Schedule, acesse os links abaixo:

* [RH - Linha Protheus - GPE - eSocial - S-2206/S-2230 - Como configurar o job schedule GPEM026B](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5220215589527-RH-Linha-Protheus-GPE-eSocial-S-2206-S-2230-Como-configurar-o-job-schedule-GPEM026B?source=search)
* [RH - Linha Protheus - GPE - eSocial - S-2206/S-2230 - Como executar o Job/Schedule manualmente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035161473-RH-Linha-Protheus-GPE-eSocial-S-2206-S-2230-Como-executar-o-Job-Schedule-manualmente?source=search)

**Saiba Mais**Para saber mais consulte os links abaixo:   
[Artigos S-1050](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052497253)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
