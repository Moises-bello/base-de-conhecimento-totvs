---
article_id: 23080786481687
category: GPE - eSocial - Não Periódicos
content_hash: f03b11d36bd1f6fa7e8701d9b2579915ab95324de551043867c29da817237f40
fetched_at: '2026-06-28T22:45:04.710742+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2206 - O evento S-2206 não é gerado
  após realizar uma alterações salarial por dissidio ou através da rotina Reajuste
  Salarial
type: support-article
updated_at: '2026-06-16T11:47:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23080786481687-RH-Linha-Protheus-GPE-eSocial-S-2206-O-evento-S-2206-n%C3%A3o-%C3%A9-gerado-ap%C3%B3s-realizar-uma-altera%C3%A7%C3%B5es-salarial-por-dissidio-ou-atrav%C3%A9s-da-rotina-Reajuste-Salarial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23080768262167) Tempo aproximado para leitura: **00:02:00min** **Dúvida**O evento S-2206 não é gerado após realizar uma alterações salarial por dissidio ou através da rotina Reajuste Salarial.  
S-2206 não integra após reajuste salarial.  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Quando ocorre uma alteração salarial por dissidio ou através da rotina Reajuste Salarial, o evento S-2206 não é gerado de forma automática.  
  
O sistema realiza a alteração salarial no GPE e grava a linha na rotina Histórico Salário (Atualizações > Funcionários > Histórico Salário > Visualizar), porém o campo **Integ TAF (R3\_\_INTGTAF)** fica vazio  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23080768266135)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23080786431511)  
  
Para a geração e integração do S-2206, é necessário configurar e executar o schedule/job:  
[RH - Linha Protheus - GPE - eSocial - S-2206/S-2230 - Como configurar o job schedule GPEM026B na tela PO UI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21979795766167-RH-Linha-Protheus-GPE-eSocial-S-2206-S-2230-Como-configurar-o-job-schedule-GPEM026B-na-tela-PO-UI)  
  
Após executar o job, o evento S-2206 será gerado e o campo **Integ TAF (R3\_\_INTGTAF)** no Histórico Salarial preenchido:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23080786436503)  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:  
[RH - Linha Protheus - GPE - eSocial - S-2206 - Como utilizar o parâmetro MV\_DTALTSA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9295167803287-RH-Linha-Protheus-GPE-eSocial-S-2206-Como-utilizar-o-par%C3%A2metro-MV-DTALTSA)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
