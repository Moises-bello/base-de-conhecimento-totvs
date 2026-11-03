---
article_id: 24034740362903
category: RH - Fechamento Período
content_hash: 63720a4b44a08f9abb6db10ef1747dea425aa32d46c4c927dd2498b1fb9a4ec1
fetched_at: '2026-06-28T22:43:24.442282+00:00'
product: protheus
section_id: 360011909793
source: central-protheus
title: RH - Linha Protheus - GPE - Como validar usuário no Fechamento do Período
type: support-article
updated_at: '2025-04-16T12:34:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24034740362903-RH-Linha-Protheus-GPE-Como-validar-usu%C3%A1rio-no-Fechamento-do-Per%C3%ADodo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24034740344471) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como validar usuário no Fechamento do Período?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões]  
  
**Solução**

Visando minimizar a ocorrência de fechamentos acidentais do roteiro ordinário, FOL e AUT, iremos implementar algumas validações que poderão auxiliar na operação do cliente no momento do fechamento do período. Para isso basta ajustar o parâmetro MV\_FECFOL para .T.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24034740346263)

- Criação do parâmetro MV\_FECFOL, que por padrão estará desativado. Ao ser ativado o sistema não permitirá o fechamento do roteiro FOL ou AUT junto com outro roteiro, devendo o usuário fechar todos os roteiros para em seguida fechar o roteiro FOL/AUT individualmente.  
- Criação de campo na RCH (RCH\_USERFE) para gravar o código e nome do usuário que efetuou o fechamento do roteiro. Essa gravação será feita sempre, independente da configuração do parâmetro MV\_FECFOL e dos campos USERLGI e USERLGA.

Parâmetro na SX6   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24034753275927)

 

Campo RCH\_USERFE no dicionário SX3 conforme estrutura abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24034753278359)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24035158098583)

Observação

Essa melhoria estará disponível no pacote da expedição contínua do RH igual ou superior a data de **29/03/2024  
  
Saiba Mais**<https://tdn.totvs.com/pages/releaseview.action?pageId=831826045>  
[RH - Linha Protheus - GPE - Funcionalidades da rotina de Fechamento de Período - GPEM120](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057827774-RH-Linha-Protheus-GPE-Funcionalidades-da-rotina-de-Fechamento-de-Per%C3%ADodo-GPEM120?source=search)  
[RH - Linha Protheus - GPE - Quais os parâmetros utilizados para o fechamento do período](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9070502632343-RH-Linha-Protheus-GPE-Quais-os-par%C3%A2metros-utilizados-para-o-fechamento-do-per%C3%ADodo?source=search)  
[RH - Linha Protheus - GPE - Como realizar o fechamento mensal de determinado período da folha](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027259971-RH-Linha-Protheus-GPE-Como-realizar-o-fechamento-mensal-de-determinado-per%C3%ADodo-da-folha?source=search)
