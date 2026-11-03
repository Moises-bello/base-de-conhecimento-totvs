---
article_id: 360061049894
category: NFe - Nota Fiscal Eletrônica
content_hash: 603fef6a72c5e7f21c2def5fcc823a0140976d06128b59e79ffe5f3f771531ae
fetched_at: '2026-06-28T22:40:05.033441+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 435 Rejeição :
  NF-e não pode ter o indicativo do intermediador'
type: support-article
updated_at: '2025-07-25T18:36:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061049894-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-435-Rejei%C3%A7%C3%A3o-NF-e-n%C3%A3o-pode-ter-o-indicativo-do-intermediador
---

**Dúvida**Como solucionar a rejeição abaixo:

435 Rejeição : NF-e não pode ter o indicativo do intermediador ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Se Informado indicativo de presença, TAG **indPres, DIFERENTE de 1, 2, 3, 4 ou 9** - **Proibido o preenchimento** do campo Indicativo do Intermediador **(tag: indIntermed)**

* A TAG ***indPres*** pode ter os conteúdos abaixo:

**0=**Não se aplica (por exemplo, Nota Fiscal complementar ou de ajuste);   
**1=**Operação presencial;   
**2=**Operação não presencial, pela Internet;   
**3=**Operação não presencial, Teleatendimento;   
**4=**NFC-e em operação com entrega a domicílio;   
**5=**Operação presencial, fora do estabelecimento;   
**9=**Operação não presencial, outros. 

Se **preencher  TAG *indPres*** *como* ***0 ou 5 não pode ser gerada a TAG indIntermed*:**

**1-** No pedido de vendas preencher o campo **Presença Com "C5\_INDPRES "=  0**

**![indpres.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33721528203927)**

**2-** Os campos **não devem** ser preenchido "**Código do intermediador"  no pedido de vendas C5\_CODA1U e no documento de entrada F1\_CODA1U.**  
  
  
<https://tdn.totvs.com/pages/releaseview.action?pageId=603466647>

**ou**

1- No pedido de vendas preencher o campo **Presença Com** "**C5\_INDPRES "=  5**

**![venda_presencial_fora.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33721480609431)**

2- No pedido de vendas é necessário haver uma nota referenciada que gere o grupo **refNFe ou refNF.**

* **refNFe =** Modelo 55 Espécie = SPED
* **refNF=** Modelo 01, 01A, 02 Espécie = NF, NFe, NFA ou **NFCF (modelo novo incluído na 4.00)**

Caso haja dúvidas de como **gerar a espécie "modelo" da nota:**

[MP - FAT - Criação de série de NFs para utilizar em Documentos de Saída](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020162851-MP-FAT-Cria%C3%A7%C3%A3o-de-s%C3%A9rie-de-NFs-para-utilizar-em-Documentos-de-Sa%C3%ADda?source=search)

3- No pedido de venda será necessário preencher os campos **NF . Ori , Serie Ori e Item Ori .**

Para referenciar a nota de origem os três campos precisam estar preenchidos:

**D2\_ITEMORI, D2\_SERIORI, D2\_NFORI (nota de saída)**

![referenciar_a_nota.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33721480610455)

4- Quando for referenciar duas notas de saída do tipo normal para gerar a chave além de referenciar será necessário incluir os **CFOPS da nota no parâmetro:**

![MV_REFNFE.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/33721480610967)

* **Parâmetro MV\_REFNFE = Informar o CFOP separado por vírgula conforme a FAQ:**  
  [NF-e - Parâmetro para nota referenciada](http://tdn.totvs.com/pages/viewpage.action?pageId=181144492)

![MV_REFNFE.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33721480613399)

5- Os campos **não devem** ser preenchido "**Código do intermediador"  no pedido de vendas C5\_CODA1U.**  
  
  
<https://tdn.totvs.com/pages/releaseview.action?pageId=603466647>

* **Importante:**

Se precisar informar o**intermediador,** no pedido de vendas preencher o campo **Presença Com C5\_INDPRES =** **1, 2, 3, 4 ou 9.**

Para ***gerar o intermediador*** realizar os passos abaixo:

1. Preencher o intermediador em  Faturamento -> Cadastros -> Intermediadores **Nome "A1U\_NOME" e CNPJ "A1U\_CGC"**

**![20220401_150016.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5174407245463)**

        2.  Preencher o  no pedido de vendas **Presença Com** "**C5\_INDPRES"**  igual a  **2**, **3**,ou **9;**

**![20220401_150932.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5174696917911)**

    3.  Preencher no **Pedido de Venda Cod. Intermed** "**C5\_CODA1U";**

**![20220401_151123.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5174738208023)**

         4. Após isso, ***transmita novamente a Nota fiscal eletrônica.***

* **Validação da Sefaz:**

![435_rejei__o.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/1500017786322)
