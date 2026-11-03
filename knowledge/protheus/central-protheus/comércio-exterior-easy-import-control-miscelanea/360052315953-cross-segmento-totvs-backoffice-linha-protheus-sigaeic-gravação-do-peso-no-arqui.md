---
article_id: 360052315953
category: Comércio Exterior - Easy Import Control - Miscelanea
content_hash: 18509792cc6424e3eadd4210208296b2499587e1b7783f0dfe3628f5ac13c397
fetched_at: '2026-06-28T22:39:41.996662+00:00'
product: protheus
section_id: 1500001549702
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Gravação do Peso
  no Arquivo TXT da Purchase Order, para envio ao Despachante.
type: support-article
updated_at: '2022-06-02T12:32:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052315953-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Grava%C3%A7%C3%A3o-do-Peso-no-Arquivo-TXT-da-Purchase-Order-para-envio-ao-Despachante
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como é preenchido o peso no arquivo TXT da Purchase Order, para envio ao despachante?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Easy Import Control - Todas as versões

**Solução**

O peso no arquivo de integração pode vir de dois locais diferentes, conforme a configuração do parâmetro MV\_EIC0041.

Quando este parâmetro está configurado com o numeral igual 1, o peso deve estar preenchido no cadastro de produtos (B1\_PESO).

Caso o parâmetro esteja com o numeral igual 2, o peso deverá estar no cadastro de Produto x Fornecedor (A5\_PESO). Vale lembrar  ainda que temos o parâmetro MV\_UNIDCOM que determina se deverá ser utilizada a primeira ou a segunda unidade de medida para o peso.

**Saiba mais:**

[Define se o processo deve utilizar o peso líquido da tabela SB1](https://tdn.totvs.com/pages/releaseview.action?pageId=126189579&preview=/126189579/126157008/EIC_BT_Criacao_Parametro_MV_EIC0041_BRA_TIHITC.pdf)

[Primeira e segunda unidade de medida no SIGAEIC](https://tdn.totvs.com/display/public/PROT/Primeira+e+segunda+unidade+de+medida+no+SIGAEIC)
