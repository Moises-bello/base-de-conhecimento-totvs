---
content_hash: 9fda6524cb4944a8bae41dffedec7bcd604d4d1f9089201d9501df9606e627d0
fetched_at: '2026-06-29T00:10:21.732738+00:00'
page_id: '493617288'
product: rm
source: tdn-rm
title: FISCAL01-9265 DT Cadastro do INSS/PJ - Alteração de label e inclusão de um
  hint
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=493617288
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Cadastro do INSS/PJ |
| Ticket: | FISCAL01-9265 |
| Requisito/Story/Issue (informe o requisito relacionado) : | Cadastro do INSS/PJ |

## **02. SITUAÇÃO/REQUISITO**

Alteração do nome do campo *"Código de Receita do INSS"* para *"Identificador"* no cadastro de INSS/PJ.

Inclusão de um hint sobre o campo *Código da Receita - SENAR*, informando ao usuário que ele só deve preencher esse campo se a empresa possuir liminar para a não retenção do Funrural e que quando informado a guia do SENAR será gerada à parte no Período de Apuração.

## **03. SOLUÇÃO**

No Cadastro INSS/PJ, (BackOffice Nucleus →  Cadastros (Fiscais) → Mias ... → INSS/PJ):

* Campo  *"Código de Receita do INSS"* alterado para “Identificador”.
* Foi adicionado um alerta para aparece, quando se clicar no campo *Código da Receita - Senar*. Ao pousar o mouse em cima, é exibida a mensagem: "Este campo só deve ser preenchido se a empresa possuir liminar para a não retenção do Funrural. Quando informado, a guia do SENAR será gerada à parte no Período de Apuração".
