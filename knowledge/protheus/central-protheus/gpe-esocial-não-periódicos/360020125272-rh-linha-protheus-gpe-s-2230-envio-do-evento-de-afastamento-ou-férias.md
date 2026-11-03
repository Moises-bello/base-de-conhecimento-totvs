---
article_id: 360020125272
category: GPE - eSocial - Não Periódicos
content_hash: e22c0cb300f30197b5781c07ecd0c6dfbc37116b7f36f1a6ea4f63dc07281457
fetched_at: '2026-06-28T22:45:06.000520+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - S-2230- Envio do evento de afastamento ou Férias
type: support-article
updated_at: '2026-06-16T10:39:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020125272-RH-Linha-Protheus-GPE-S-2230-Envio-do-evento-de-afastamento-ou-F%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17962095604503) Tempo aproximado para leitura: **00:02:30 min**  
  
**Dúvida**  
Como realizar o envio do evento S-2230 afastamento ou férias?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Acesse a rotina **Tipos de Ausências**, e verifique se o motivo de afastamento eSocial está de acordo com a [Tabela 18 do Leiaute Vigente](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica).  
  
**Obs.:** O evento de afastamento poderá ser informado apenas com a data de início do afastamento.   
A data de término também poderá ser incluída no mesmo evento, desde que não seja superior à data atual acrescida de 15 dias corridos, caso contrário informar um novo evento de afastamento somente com data fim. Para o motivo de afastamento “15 - Férias”, o eSocial permitirá o registro do término desde que não seja superior à data atual acrescida de até 60 dias.  
Também pode ser feito o evento afastamento com a data inicio e fim já preenchida, onde é necessário deixar o parâmetro **MV\_DTFIMA** com **.T.** (SIGACFG > Configurador > Ambiente > Cadastros > Parâmetros). E para que o sistema envie a data fim automaticamente é preciso que o schedule esteja configurado:  
[RH - Linha Protheus - GPE - eSocial - S-2206/S-2230 - Como configurar o job schedule GPEM026B](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5220215589527-RH-Linha-Protheus-GPE-eSocial-S-2206-S-2230-Como-configurar-o-job-schedule-GPEM026B?source=search)  
[RH - Linha Protheus - GPE - eSocial - S-2206/S-2230 - Como executar o Job/Schedule manualmente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035161473-RH-Linha-Protheus-GPE-eSocial-S-2206-S-2230-Como-executar-o-Job-Schedule-manualmente?source=search)

**1.** Para enviar um afastamentos a partir do **GPE**, deve acessar a rotina **Cadastro de Ausências**.  
Caminho: Atualizações > Lançamentos > Ausências > Selecione o Funcionário > Manutenção*:*  
*![](https://centraldeatendimento.totvs.com/hc/article_attachments/17960757055383)*  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/17960760322583)**  
  
**1.1.** Preencher os campos os campos necessários e confirme:  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/17961134862615)**  
  
**1.2.** O afastamento será integrado com o TAF e depois deverá ser transmitido para o Governo:  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/17961091072535)**  
  
**2.**Para enviar afastamentos temporários relacionados a férias a partir do GPE, deve acessar a rotina **Calculo de Férias**.  
Caminho: Miscelânia > Calculo > Férias > Selecione o Funcionário > Calculo:  
*![](https://centraldeatendimento.totvs.com/hc/article_attachments/17961341441815)*  
*![](https://centraldeatendimento.totvs.com/hc/article_attachments/17961364047895)*  
  
**2.1.** Preencher os campos necessários, vá em outras ações e aperte **Calcular**, após realizar o cálculo, confirme:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17961619944215)  
  
**2.2.** As férias serão integradas com o TAF e depois deverá ser transmitido para o Governo:  
*![](https://centraldeatendimento.totvs.com/hc/article_attachments/17961711287959)*  
  
**3.** Para consultar os afastamentos no TAF (Módulo 84), acesse a rotina **Afastamento Temporário**:  
Caminho: Atualizações > Eventos eSocial > Não Periódicos > Afastamento Temp.:  
*![](https://centraldeatendimento.totvs.com/hc/article_attachments/17961939482135)*  
*![](https://centraldeatendimento.totvs.com/hc/article_attachments/17961947579287)*

**Importante**  
Referente a afastamento/atestado ou envio de férias deve se consultar [Leiaute vigente](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s1-1-nt-02-2023/index.html/index.html#evtAfastTemp) sobre as regras.  
  
**Saiba Mais**  
Para saber mais consulte os links abaixo:   
[Artigos S-2230](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058248413-RH-Linha-Protheus-GPE-eSocial-S-2230-Quais-s%C3%A3o-os-artigos-e-documenta%C3%A7%C3%B5es-relacionados-ao-evento-S-2230-Afastamento-Tempor%C3%A1rio-)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
