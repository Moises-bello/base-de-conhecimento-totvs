---
article_id: 23309085166359
category: Evento S-2240
content_hash: 98c9de1f95a25129cf276c3c286f55a290dc065cafa9496ec8b53bb79e4cd740
fetched_at: '2026-06-28T22:45:23.546794+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2240 - Ao informar data Fim da Tarefa
  é gerando novo S-2240 com a data início igual a data fim
type: support-article
updated_at: '2024-05-10T21:15:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23309085166359-RH-Linha-Protheus-MDT-eSocial-S-2240-Ao-informar-data-Fim-da-Tarefa-%C3%A9-gerando-novo-S-2240-com-a-data-in%C3%ADcio-igual-a-data-fim
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23309115926807) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Ao informar data Fim da Tarefa é gerando novo S-2240 com a data início igual a data fim.  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**O Protheus se comporta conforme o MOS indica, gerando novo evento a cada alteração na exposição do funcionário.  
De acordo com o MOS, nos itens 9.1 e 13.1 ([MOS eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-2.pdf)) contém as informações:  
  
9.1- "Caso ocorra alteração das informações entre o início da obrigação do envio das informações de SST ou da data de admissão, se posterior, e antes do envio do evento S-2240, deve ser enviado um evento com as informações iniciais e, em seguida, enviadas as alterações por meio de outro evento S-2240, para formação do histórico laboral das exposições".  
  
13.1- "O histórico laboral do trabalhador e sua divisão em períodos ocorre a partir de cada novo evento S-2240 enviado com uma nova data de início de condição. Cada evento deve descrever de forma completa todas as informações do trabalhador naquele momento. O evento enviado com nova data de início da condição marca o início de um novo período no histórico do trabalhador".  
  
Na rotina Tarefas por Funcionário (Atualização - PPRA - Tarefas por Func.), ao incluir Data Término, será enviado o registro S-2240 para o TAF:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23309085159063)  
  
Ao acessar o módulo TAF (84), na rotina Monitor. Saúde do Trabalhador (Atualizações - Eventos eSocial - Não periódico - Monitor. Saúde do Trabalhador), será apresentado o registro com o campo "Dt. Ini. Con" com a mesma data término informada na rotina de Tarefas (MDT):  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23309085159575)  
  
O procedimento está correto, conforme orientações do eSocial. Para mais informações, entre em contato com Suporte do Governo.  
  
**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
