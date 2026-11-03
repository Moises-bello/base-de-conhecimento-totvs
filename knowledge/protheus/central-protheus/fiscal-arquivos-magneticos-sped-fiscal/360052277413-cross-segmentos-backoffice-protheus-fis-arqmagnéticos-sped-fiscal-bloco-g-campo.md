---
article_id: 360052277413
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 4d49636ee9f85f7fc5dfd96a6d680d31690f2c12527b04d8322e85f6dacf4f53
fetched_at: '2026-06-28T22:42:02.684117+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Sped Fiscal  -
  BLOCO G - CAMPO 5 (UND) - REGISTRO G140
type: support-article
updated_at: '2025-01-10T17:21:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052277413-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Sped-Fiscal-BLOCO-G-CAMPO-5-UND-REGISTRO-G140
---

**Ocorrência**

Ao gerar o arquivo do **Sped Fiscal** ocorre o erro de validação no registro **G140** **campo 5 - UNID**:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082355053)

**Ambiente**

Microsiga Protheus – Livros fiscais– A partir da versão 12.1.17  
  
**Causa**

O erro acontece pois falta a informação da Unidade do item nos campos necessários.  
  
O Parâmetro **MV\_F9SKPNF** define de qual tabela o **SPED** buscará a informação para este campo:

Se **MV\_F9SKPNF** = **.F.** - > Será considerado as informações da nota fiscal **SD1, SF1, SF3 e SFT.**  
Se **MV\_F9SKPNF** = **.T.** - > Será considerado as informações do bem tabela **SF9.**

**Solução**Se **MV\_F9SKPNF = .F.** - > Verifique se na tabela SB1 o campo B1\_UM está preenchido corretamente com a unidade de medida.  
Se **MV\_F9SKPNF = .T.** - >  Siga o procedimento abaixo:

1**-** Crie um campo **F9\_CODPROD**, na tabela **SF9**:  
  
Campo: F9\_CODPROD  
Tipo: Caracter  
Tamanho: 30  
Decimal: 0  
Formato: @!  
Contexto: Real  
Titulo: Cod Prod SPD  
Texto: Informa codigo do produto  
Help: Informa codigo do correspondente ao bem no documento fiscal, preenchimento do campo 03\_COD\_ITEM G140 **SPED FISCAL**

2- Amarre o campo ao parâmetro:

**MV\_F9PROD** = **F9\_CODPROD**

Informações adicionais:

CIAP - Crédito de ICMS sobre o Ativo Permanente

<https://tdn.totvs.com/pages/releaseview.action?pageId=708871751>
