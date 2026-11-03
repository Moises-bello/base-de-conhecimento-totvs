---
content_hash: 4e996daead39999679ac13d4a129e1666c5c43d757b97e77e5796fee62b6bcfc
fetched_at: '2026-06-29T00:11:40.844178+00:00'
page_id: '795085192'
product: rm
source: tdn-rm
title: Alterações - S-2210 - S-1.2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=795085192
version: 7
---

false

**A partir das Versões:**

* 12.1.2302.235
* 12.1.2306.182
* 12.1.2310.116 e superiores

**CONTEÚDO**

IMPORTANTE!

---

## **01. VISÃO GERAL**

Este documento visa apresentar as mudanças no evento S-2210 para atender o Leiaute do eSocial versão S-1.2.

## **02. ALTERAÇÕES REALIZADAS**

### **02.01.** **TAG <codAgntCausador> - CÓDIGO DO AGENTE CAUSADOR DO ACIDENTE**

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Campo {codAgntCausador}: alterada validação | Preencher com o código correspondente ao agente causador do acidente. **Validação**: Deve ser um código válido e existente na Tabela 14 ou na Tabela 15. | Preencher com o código correspondente ao agente causador do acidente. **Validação**: Se dtAcid >= [2024-01-22] e se tpAcid = [1, 3], deve ser um código válido e existente na Tabela 14. Se dtAcid < [2024-01-22] ou se tpAcid = [2], deve ser um código válido e existente na Tabela 14 ou na Tabela 15. |

**Alteração:**Caso a data do acidente seja maior ou igual a 22/01/2024 e o tipo do acidente seja '1' ou '3', o sistema aceitará apenas códigos correspondentes à Tabela 14 do eSocial.

Se uma CAT for registrada com o tipo de acidente (tpAcid) igual a 1 ou 3 e a data do acidente (dtAcid) for igual ou posterior a 22/01/2024, o código do agente causador do acidente deve ser selecionado a partir da Tabela 14 do leiaute do eSocial. Se, por acaso, um código da Tabela 15 for escolhido nessas condições, o sistema gerará o seguinte erro ao tentar gerar o XML:

*- Erro na validação do campo 'codAgntCausador': Se dtAcid = [2024-01-22] e se tpAcid = [1, 3], d**eve ser um código válido e existente na Tabela 14.*

Nas demais condições, o sistema aceitará tanto códigos da Tabela 14 quanto códigos da Tabela 15.

Exemplo de XML corretamente gerado:

## **03. MAPEAMENTO DO EVENTO**

Acesse o mapeamento do evento clicando no link abaixo:

* + [Evento S-2210](https://tdn.totvs.com/display/LRM/Evento+S-2210)
