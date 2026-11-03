---
article_id: 7301225955607
category: TAF - eSocial - Eventos Periódicos
content_hash: 906bd651c645a1314337a61e082f2ddb753b3d1f9fb43c9e0f6cbf57a0344092
fetched_at: '2026-06-28T22:45:19.071945+00:00'
product: protheus
section_id: 1500001536901
source: central-protheus
title: 'RH - Linha Protheus - TAF - eSocial - Eventos Periódicos - S-1210 - Ocorrência:
  861 - Descrição: A data de pagamento deve ser maior ou igual ao mês anterior de
  rescisão do contrato de trabalho'
type: support-article
updated_at: '2026-06-25T12:31:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7301225955607-RH-Linha-Protheus-TAF-eSocial-Eventos-Peri%C3%B3dicos-S-1210-Ocorr%C3%AAncia-861-Descri%C3%A7%C3%A3o-A-data-de-pagamento-deve-ser-maior-ou-igual-ao-m%C3%AAs-anterior-de-rescis%C3%A3o-do-contrato-de-trabalho
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23699907701271) Tempo aproximado para leitura: **05:00:00 min**  
  
**Ocorrência**  
Erro ao tentar transmitir/integrar o evento S-1210:

*"Sequência: 000 - Tipo: Erro - Codigo da Ocorrência: 861 - Descrição : A data de pagamento deve ser maior ou igual ao mes anterior de rescisao do contrato de trabalho. - Localização : /eSocial/evtPgtos/ideBenef/infoPgto[2]/dtPgto"*  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Eventos Periódicos - S-1210 - Todas as versões

**Causa**  
A inconsistência é retornada quando não foi enviado o evento **S-2299 (Desligamento)** anterior ao envio do evento **S-1210 (Pagamento da Remuneração).**  
  
**Solução**  
Para correção desta inconsistência, indicamos a leitura dos artigos abaixo:

[RH - RM - FOP - eSocial - Erro código 861 na integração: A data de pagamento deve ser maior ou igual ao mês anterior de rescisão do contrato de trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6038379043863)

[RH - Linha Protheus - GPE - eSocial - S-1210 - Código da Ocorrência: 861 - A data de pagamento deve ser maior ou igual ao mês anterior de rescisão do contrato de trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19452617838103-RH-Linha-Protheus-GPE-eSocial-S-1210-C%C3%B3digo-da-Ocorr%C3%AAncia-861-A-data-de-pagamento-deve-ser-maior-ou-igual-ao-m%C3%AAs-anterior-de-rescis%C3%A3o-do-contrato-de-trabalho?source=search)
