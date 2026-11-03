---
article_id: 360020820911
category: NFe - Nota Fiscal Eletrônica
content_hash: c1ce2b8458f420a3f6fd31b3487f7d9f936975ff489e7aa6765ae81815017a71
fetched_at: '2026-06-28T22:40:05.405177+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 864 Rejeição :
  NF-e com indicativo de Operação presencial, fora do estabelecimento e não informada
  NF referenciada'
type: support-article
updated_at: '2025-06-16T17:06:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020820911-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-864-Rejei%C3%A7%C3%A3o-NF-e-com-indicativo-de-Opera%C3%A7%C3%A3o-presencial-fora-do-estabelecimento-e-n%C3%A3o-informada-NF-referenciada
---

**Dúvida**Como resolver a 864 Rejeição :**NF-e com indicativo de Operação presencial,** fora do estabelecimento e não informada NF referenciada ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

No layout da 4.00 foi criado na TAG indPres a opção **5=Operação presencial, fora do estabelecimento**

![indpres.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360101258754)

1- Ao utilizar essa nova opção 5 no campo **Presença Com** "**C5\_INDPRES" = 5**

**![venda_presencial_fora.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360103876013)**

2- No pedido de vendas é necessário haver uma nota referenciada que gere o grupo **refNFe ou refNF.**

* **refNFe =** Modelo 55 Espécie = SPED
* **refNF=** Modelo 01, 01A, 02 Espécie = NF, NFe, NFA ou **NFCF (modelo novo incluído na 4.00)**

Caso haja dúvidas de como **gerar a espécie "modelo" da nota:**

[MP - FAT - Criação de série de NFs para utilizar em Documentos de Saída](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020162851-MP-FAT-Cria%C3%A7%C3%A3o-de-s%C3%A9rie-de-NFs-para-utilizar-em-Documentos-de-Sa%C3%ADda?source=search)

3- No pedido de venda será necessário preencher os campos **NF . Ori , Serie Ori e Item Ori .**

Para referenciar a nota de origem os três campos precisam estar preenchidos:

**D2\_ITEMORI, D2\_SERIORI, D2\_NFORI (nota de saída)**

![referenciar_a_nota.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360103876233)

4- Quando for referenciar duas notas de saída do tipo normal para gerar a chave além de referenciar será necessário incluir os **CFOPS da nota no parâmetro:**

![MV_REFNFE.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002854042)

* **Parâmetro MV\_REFNFE = Informar o CFOP separado por vírgula conforme a FAQ:**

![MV_REFNFE.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360101730894)

* **Saiba mais:**

Caso não seja uma Operação Presencial fora do Estabelecimento

* A TAG***indPres***pode ter os conteúdos abaixo:

**0=**Não se aplica (por exemplo, Nota Fiscal complementar ou de ajuste);  
**1=**Operação presencial;  
**2=**Operação não presencial, pela Internet;  
**3=**Operação não presencial, Teleatendimento;  
**4=**NFC-e em operação com entrega a domicílio;  
**9=**Operação não presencial, outros. 

1 - Altere o conteúdo do campo **Presença Com** "**C5\_INDPRES" = 0, 1, 2, 3, 4 ou 9.**

2- Após isso, **exclua a nota e gere novamente.**

* **Caso** apresente a **rejeição 434 conforme o link abaixo:**

[Cross Segmentos - Backoffice Protheus - 434 Rejeição : NF-e sem indicativo do intermediador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062802333)
