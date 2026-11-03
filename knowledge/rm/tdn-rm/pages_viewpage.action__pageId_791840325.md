---
content_hash: c72b41cba8108f7477f1effeed074257342070a91680f9da38c5e561f423522c
fetched_at: '2026-06-29T00:11:39.955639+00:00'
page_id: '791840325'
product: rm
source: tdn-rm
title: Alterações - S-2306 - S-1.2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=791840325
version: 14
---

false

**A partir das Versões:**

* 12.1.2302.235
* 12.1.2306.182
* 12.1.2310.116 e superiores

**CONTEÚDO**

IMPORTANTE!

---

## **01. VISÃO GERAL**

Apresentar as alterações no evento S-2306 para o leiaute do eSocial Versão S-1.2.

## **02. ALTERAÇÕES REALIZADAS**

### **02.01** **GRUPO <localTrabGeral> - LOCAL DE TRABALHO GERAL**

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {infoComplementares}: incluído grupo (localTrabGeral) e seus respectivos campos | - | **O** (se o código de categoria no RET for igual a [2XX, 304, 305, 4XX, 721, 722, 723, 731, 734, 738, 761, 771, 901, 902, 906] e dtAlteracao >= [2024-01-22]); **F** (se o código de categoria no RET for igual a [2XX, 304, 305, 4XX, 721, 722, 723, 731, 734, 738, 761, 771, 901, 902, 906] e dtAlteracao < [2024-01-22]); **N** (nos demais casos) |

****Alteração**:** Geração do grupo <***localTrabGeral***> no evento S-2306. 

Ao gerar o S-2306 para um funcionário com a categoria eSocial pertencente a [2XX, 304, 305, 4XX, 721, 722, 723, 731, 734, 738, 761, 771, 901, 902, 906], o sistema incluirá no XML o grupo <***localTrabGeral***> (dentro do grupo pai <***infoComplementares***>), o qual indicará o tipo de inscrição e o número de inscrição relacionado à seção do funcionário.

**Importante!** A tag <***descComp***>, que contém a descrição complementar do local de trabalho, não será incluída no XML. Como essa tag não é obrigatória, o XML pode ser transmitido normalmente sem ela.

## **03. MAPEAMENTO DO EVENTO**

Acesse o mapeamento do evento clicando no link abaixo:

* + [Evento S-2306](https://tdn.totvs.com/display/LRM/Evento+S-2306)
