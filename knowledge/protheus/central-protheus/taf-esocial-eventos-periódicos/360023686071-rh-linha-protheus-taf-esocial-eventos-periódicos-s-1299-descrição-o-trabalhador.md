---
article_id: 360023686071
category: TAF - eSocial - Eventos Periódicos
content_hash: 7c37d0c1da802e6ace97b2b4e8979be4d9da8facafa33b0ddbe4cd06c527574c
fetched_at: '2026-06-28T22:45:19.199531+00:00'
product: protheus
section_id: 1500001536901
source: central-protheus
title: 'RH - Linha Protheus - TAF - eSocial - Eventos Periódicos - S-1299 - Descrição:
  O trabalhador com CPF: XXXXXXXXXXX e Matrícula: XXX consta na base de dados do Ambiente
  Nacional do eSocial, mas não foi informada sua remuneração.'
type: support-article
updated_at: '2026-06-24T12:23:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023686071-RH-Linha-Protheus-TAF-eSocial-Eventos-Peri%C3%B3dicos-S-1299-Descri%C3%A7%C3%A3o-O-trabalhador-com-CPF-XXXXXXXXXXX-e-Matr%C3%ADcula-XXX-consta-na-base-de-dados-do-Ambiente-Nacional-do-eSocial-mas-n%C3%A3o-foi-informada-sua-remunera%C3%A7%C3%A3o
---

**Dúvida**

Inconsistências  no envio do evento S-1299 de código 162: O trabalhador com Matricula: xxxxx consta na base de dados do Ambiente Nacional do eSocial, mas não foi informada sua remuneração. Ação Sugerida: Verificar se a falta de informação é decorrente de dificuldade operacionais ou se é possível efetuar a regularização.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360021271452)

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Eventos Periódicos - S-1299 - Todas as versões  
  
  
**Solução**

- Verificar a situação do empregado identificado por CPF e matrícula na mensagem de erro.

**Por exemplo:**

* Caso o empregado esteja afastado, deve-se verificar se foi transmitido o evento S-2230 - Afastamento Temporário.
* Se o empregado foi desligado, deve-se enviar o evento S-2299 - Desligamento.
* Se o funcionário estiver ativo, é necessário transmitir o evento S-1200 - Remuneração RGPS

- Em seguida, enviar novamente, o evento S-1299 - Fechamento dos eventos periódicos.
