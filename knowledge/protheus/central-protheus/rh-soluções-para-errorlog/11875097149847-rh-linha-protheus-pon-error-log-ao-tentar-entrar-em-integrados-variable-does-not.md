---
article_id: 11875097149847
category: RH - Soluções para error.log
content_hash: b0a09cfa5e71c8bcf342eabe6fad8bf136a74fd94a88e794f8645a482c4afbc6
fetched_at: '2026-06-28T22:44:08.996683+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: 'RH - Linha Protheus - PON - Error log ao tentar entrar em integrados: variable
  does not exist P8_FUSO on P280MARCCOLS(PONA280.PRX)'
type: support-article
updated_at: '2025-08-04T20:30:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11875097149847-RH-Linha-Protheus-PON-Error-log-ao-tentar-entrar-em-integrados-variable-does-not-exist-P8-FUSO-on-P280MARCCOLS-PONA280-PRX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33941803896471) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao tentar entrar na rotina de integrados, PONA280, gera *error log*: ***v**ariable does not exist* P8\_FUSO *on* P280MARCCOLS(PONA280.PRX)**  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Causa**O error log ocorre por falta do campo **P8\_FUSO** no ambiente  
  
**Solução**Para solucionar o problema é necessário:  
  
**1.** Se no dicionário existe o campo **P8\_FUSO** e na tabela **SP8** não existe, será necessário efetuar backup da tabela **SP8** e recriá-la para que o campo seja criado na tabela;  
  
**2.** Se o campo não existir no dicionário, será necessário rodar o UPDDISTR com o dicionário do pacote abaixo:  
  
Pacote Expedição Contínua RH: [MP - GPE - Como fazer o download (baixar) do pacote de expedição continua (acumulado) do modulo Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854)  
Em caso de dúvida sobre execução do UPDDISTR consulte a documentação:  
<https://tdn.totvs.com/display/public/framework/Upgrade+de+Release+do+Protheus+12>

**Informações complementares**Pacote de Expedição Contínua do eSocial:[https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051585234-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-acumulado-do-eSocial)  
Pacote de Expedição Contínua do Medicina e Segurança do Trabalho:<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057956773>  
  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
