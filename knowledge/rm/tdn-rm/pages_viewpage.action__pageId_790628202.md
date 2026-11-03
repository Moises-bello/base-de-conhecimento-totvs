---
content_hash: b0918940f6b3bdb87d9d9f6d911dc9611bca34d93a437b7f49a41be7e1454dbb
fetched_at: '2026-06-29T00:11:39.830005+00:00'
page_id: '790628202'
product: rm
source: tdn-rm
title: Alterações - S-2300 - S-1.2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=790628202
version: 17
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

Este documento visa apresentar as mudanças no evento S-2300 para atender o Leiaute do eSocial versão S-1.2.

## **02. ALTERAÇÕES REALIZADAS**

### **02.01.** **TAG <descrDep> - DESCRIÇÃO DA DEPENDÊNCIA**

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {dependente}: incluído campo (descrDep) | - | Informar a descrição da dependência. **Validação:** Informação obrigatória e exclusiva se tpDep = [99]. |

**Alteração:** Criado o campo "**Descrição da Dependência**" no cadastro de dependentes. Quando preenchido, ele gerará a tag <***descrDep***>.

Ao informar no campo "**Grau de parentesco**" a opção "**9-Outros**", será habilitado o campo "**Descrição da Dependência**".

O campo "**Descrição da Dependência**" será obrigatório quando na aba incidência estiver marcado IRRF:

### 02.02. **GRUPO <localTrabGeral> - LOCAL DE TRABALHO GERAL**

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {infoComplementares}: incluído grupo (localTrabGeral) e seus respectivos campos | - | **O** (se codCateg = [2XX, 304, 305, 4XX, 721, 722, 723, 731, 734, 738, 761, 771, 901, 902, 906] e dtInicio >= [2024-01-22]);  **F** (se codCateg = [2XX, 304, 305, 4XX, 721, 722, 723, 731, 734, 738, 761, 771, 901, 902, 906] e dtInicio < [2024-01-22]); **N**(nos demais casos) |

**Alteração:**Geração do grupo <***localTrabGeral***> no evento S-2300.

Ao realizar a geração do S-2300 para um funcionário com categoria eSocial entre 2XX, 304, 305, 4XX, 721, 722, 723, 731, 734, 738, 761, 771, 901, 902 e 906, o sistema incluirá no XML o grupo <***localTrabGeral***> (dentro do grupo pai <i***nfoComplementares***>), que indicará o tipo e o número de inscrição correspondente à seção do funcionário.

**Importante!** A tag <***descComp***>, que contém a descrição complementar do local de trabalho, não será incluída no XML. Como essa tag não é obrigatória, o XML pode ser transmitido normalmente sem ela.

## **03. MAPEAMENTO DO EVENTO**

Acesse o mapeamento do evento clicando no link abaixo:

* + [Evento S-2300](https://tdn.totvs.com/display/LRM/Evento+S-2300)
