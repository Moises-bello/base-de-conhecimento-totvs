---
article_id: 14338035084055
category: GPE - eSocial - Não Periódicos
content_hash: ba45daf185b39581ae0c9cc232960b1b44a5e828d772ab71cfcd43ba8e35b872
fetched_at: '2026-06-28T22:45:05.800597+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-2299 - Código de ocorrência 181: vinculo
  trabalhista ja se encontra encerrado na dato do evento'
type: support-article
updated_at: '2026-06-16T11:28:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14338035084055-RH-Linha-Protheus-GPE-eSocial-S-2299-C%C3%B3digo-de-ocorr%C3%AAncia-181-vinculo-trabalhista-ja-se-encontra-encerrado-na-dato-do-evento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24317301627543) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Ao enviar o evento S-2299, retorna código de **ocorrência 181**: vinculo trabalhista já se encontra encerrado na dato do evento.   
  
**Ambiente**  
TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Este erro é validação do RET (Governo), ele esta informando que existe **algum registro com data posterior ao desligamento**, por isso não esta aceitando o evento S-2299  
   
No **portal eSocial,** verifique as **Movimentações Trabalhistas** desse funcionário. Normalmente são eventos de Medicina e Segurança. Mas também pode ser o evento de Pagamento e Rendimentos (S-1210).  
   
Identificado o evento, sugiro que exclua este evento ou retifique a data, pois o Governo não aceita eventos com data posterior ao desligamento.   
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
