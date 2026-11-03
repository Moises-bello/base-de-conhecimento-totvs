---
article_id: 360021053871
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 226302d940eebaba4c7fb9f12f3addb585ddd816952dd97c55deaff9a54d39af
fetched_at: '2026-06-28T22:42:03.795417+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: MP - FIS - Ponto de Entrada MTMODNOT - Retorna Código do Modelo de Documento
  Fiscal
type: support-article
updated_at: '2022-02-23T16:38:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021053871-MP-FIS-Ponto-de-Entrada-MTMODNOT-Retorna-C%C3%B3digo-do-Modelo-de-Documento-Fiscal
---

**Dúvida**Quais os procedimentos de utilização do ponto de entrada MTMODNOT?  
  
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**Este ponto de entrada é utilizado para retornar o código do modelo de documento fiscal que não conste na lista de modelos de documentos fiscais oficial, a partir do Convenio 31/99. A espécie utilizada é passada como parâmetro, retornando o código válido.

Ponto de chamada: na função aModNot, que retorna o código do modelo.

Programa Fonte

```
.PRW
```

Sintaxe

MTMODNOT - Retorna código do modelo de doc. fiscal ( < cEspecie> ) --> cCodigo

Parâmetros:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Descrição |  |  | Default |  |  | Obrigatório |  |  | Referência |  |
|  | cEspecie |  |  | Array of Record |  |  |  |  |  |  |  |  | X |  |  |  |  |

Retorno

**cCodigo**

(caracter)* Código válido do modelo de documento fiscal, com dois dígitos.

Abaixo link contendo documentação:

<https://tdn.totvs.com/pages/releaseview.action?pageId=655876036>
