---
content_hash: 5e26e5e8ac55e13186524361620ed63bed2f537ae690d68a599305819a3ba22d
fetched_at: '2026-06-29T00:11:39.834474+00:00'
page_id: '790628217'
product: rm
source: tdn-rm
title: Alterações - S-2405 - S-1.2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=790628217
version: 6
---

false

**A partir das Versões:**

* 12.1.2302.233
* 12.1.2306.181
* 12.1.2310.115 e superiores

**CONTEÚDO**

IMPORTANTE!

---

## **01. VISÃO GERAL**

Este documento visa apresentar as mudanças no evento S-2405 para atender o Leiaute do eSocial versão S-1.2.

## **02. ALTERAÇÕES REALIZADAS**

### **02.01.****TAG <descrDep> - DESCRIÇÃO DA DEPENDÊNCIA**

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {dependente}: incluído campo (descrDep) | - | Informar a descrição da dependência. **Validação:** Informação obrigatória e exclusiva se tpDep = [99]. |

**Alteração:** Criado o campo "**Descrição da Dependência**" no cadastro de dependentes que ao ser preenchido será gerando a tag <descrDep>

Ao informar no campo Grau de parentesco a opção (9-Outros),será habilitado o campo "Descrição da Dependência".

O campo "**Descrição da Dependência**" será obrigatório quando na aba incidência estiver marcado IRRF 

    Ao preencher ou alterar o campo "**Descrição da Dependência**"  será gerado um gatilho S-2205.

## **03. MAPEAMENTO DO EVENTO**

Acesse o mapeamento do evento clicando no link abaixo:
