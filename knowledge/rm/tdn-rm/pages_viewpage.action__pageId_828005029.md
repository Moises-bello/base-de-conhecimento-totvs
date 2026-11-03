---
content_hash: d72323c9cd42cc7acaf88d86163f8dd56843352903f2a9b9de0dd24a525c3511
fetched_at: '2026-06-29T00:11:48.809401+00:00'
page_id: '828005029'
product: rm
source: tdn-rm
title: Alterações - S-2240 - S-1.2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=828005029
version: 5
---

false

**A partir das Versões:**

* 12.1.2306.232
* 12.1.2310.171
* 12.1.2402.111 e superiores

**CONTEÚDO**

IMPORTANTE!

---

## **01. VISÃO GERAL**

Este documento visa apresentar as mudanças no evento S-2240 para atender o Leiaute do eSocial versão S-1.2.

## **02. ALTERAÇÕES REALIZADAS**

Após a liberação da versão será necessário executar os script's de adequação da tabela e campo do sistema através do sistema **RM.Atualizador.exe.**

### **02.01.** **TAG <nrProcJud> - número do processo**

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {agNoc} incluído campo (nrProcJud) | - | Em caso de agente nocivo incluído por determinação administrativa ou judicial, preencher com o número do processo. **Validação**: Informação obrigatória e exclusiva se codAgNoc = [05.01.001]. Se dtIniCondicao < [2024-01-22], o preenchimento é opcional. |

Criado o campo **Número de Processo** em RH | Segurança e Saúde Ocupacional | PPRA/PGR | Reconhecimento e Avaliação de Risco

XML:

## **03. MAPEAMENTO DO EVENTO**

Acesse o mapeamento do evento clicando no link abaixo:

* + [Evento S-2240](https://tdn.totvs.com/display/LRM/Evento+S-2240)
