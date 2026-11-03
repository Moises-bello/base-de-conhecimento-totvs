---
article_id: 4409524047383
category: TAF - eSocial -TSS
content_hash: 42a3e66d9186541a7d0d4a13cc844d1a10958d99361c88be0f70ca11668e5b31
fetched_at: '2026-06-28T22:45:21.949128+00:00'
product: protheus
section_id: 1500001536761
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Medicina - S-2240 - Erro durante Integração
  do XML de terceiros, SST
type: support-article
updated_at: '2024-05-24T19:19:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409524047383-RH-Linha-Protheus-TAF-eSocial-Medicina-S-2240-Erro-durante-Integra%C3%A7%C3%A3o-do-XML-de-terceiros-SST
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23691069712535) Tempo aproximado para leitura: **05:00:00 min****Ocorrência**Ao tentar integrar o XML do evento SST, S-2240 - Condições Ambientais do Trabalho, ocorre erro de integração, informando que o CPF do Trabalhador não existe na Base de Dados.

*Erro 1 - O valor 'xxxxxxxxxxx' informado na tag cpfTrab não existe na base de dados.*

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409523639319)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação Fiscal - e-Social - Medicina - S-2240 -Condições Ambientais do Trabalho – Fatores de Risco (TAFA264)- Todas as versões  
  
**Causa**Este erro ocorre quando o XML do terceiro não possui a tag <matricula>, para trabalhador que possui os eventos S-2190, S-2200 ou S-2300 transmitidos ao eSocial.

Exemplo:

Neste exemplo, o XML possui somente o número do CPF:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409523777431)

Essa estrutura de XML não atende ao Leiaute do eSocial versão S-1.0, conforme trecho retirado do mesmo.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409523804183)

**Solução**Integre novamente o XML do evento, com a tag <matricula>.

**Saiba mais:**

Consulte o Manual de Orientação do eSocial:

<https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-0-final-publicada-revisada.pdf>

Faça download do leiaute do eSocial:

<https://www.gov.br/esocial/pt-br/documentacao-tecnica>

Consulte nossas FAQ´s:

[TAF – ESOCIAL – IMPORTAR XML DE EVENTOS DE SST](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026153032)
