---
article_id: 360051503774
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 870460b8a9c11f47b4f9cce46903fffa85aa38c2607da44476b3b1ca196ce631
fetched_at: '2026-06-28T22:42:03.611616+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Sped Fiscal
  - G130 Campo 04 - Código do modelo de documento '
type: support-article
updated_at: '2024-04-16T21:26:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051503774-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Sped-Fiscal-G130-Campo-04-C%C3%B3digo-do-modelo-de-documento
---

**Ocorrência**Ao gerar o arquivo do **Sped Fiscal** ocorre o erro de validação no**Registro G130 -** **Campo 4 - COD\_MOD**:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081244834)  
  
**Ambiente**

Microsiga Protheus – Livros fiscais– A partir da versão 12.1.25  
  
**Causa**

O erro acontece pois falta a informação do Código de modelo de documento fiscal nos campos necessários.

Se **MV\_F9SKPNF** = **.F.** - > Será considerado as informações da nota fiscal **SD1, SF1, SF3 e SFT.**  
Se **MV\_F9SKPNF** = **.T.** - > Será considerado as informações do bem tabela **SF9.**  
  
**Solução:**

Esse campo deve ser preenchido com o modelo da nota 4.1.1, conforme exige o Guia Prático:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082352633)  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082352653)

Se **MV\_F9SKPNF** = **.F.** - > Verifique se os campos **F3\_ESPECIE** e **FT\_ESPECIE** estão preenchidos corretamente nas tabelas **SFT** e **SF3**.

Se **MV\_F9SKPNF** = **.T.** - >  Siga o procedimento abaixo:

 1- Crie o campo **F9\_ESPNF**, conforme a estrutura do **FT\_ESPECIE:**

Campo **F9\_ESPNF**  
Tipo: Carácter  
Tamanho: 5  
Formato: @!  
Contexto: Real  
Titulo: Espécie NF  
Texto: Informa Espécie da nota fiscal  
Help: Informa Espécie da nota fiscal para preenchimento do campo 04 do registro G130 SPEDFISCAL

2 - Amarre o campo ao parâmetro:

**MV\_F9ESP** = **F9\_ESPNF**

Mais Informações: <https://tdn.totvs.com/pages/releaseview.action?pageId=226527899>
