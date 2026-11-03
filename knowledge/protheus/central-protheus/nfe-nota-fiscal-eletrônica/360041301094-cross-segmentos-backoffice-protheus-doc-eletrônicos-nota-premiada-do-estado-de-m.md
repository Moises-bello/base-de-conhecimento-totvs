---
article_id: 360041301094
category: NFe - Nota Fiscal Eletrônica
content_hash: 55358dab506abcb5763c707b111402cb3710867823a9d2b3cf4c014b6be4470f
fetched_at: '2026-06-28T22:40:01.886613+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota premiada
  do Estado de MS  '
type: support-article
updated_at: '2021-07-07T12:20:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041301094--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Nota-premiada-do-Estado-de-MS
---

**Dúvida**

Como destacar as dezenas da Nota Premiada no Danfe para UF de MS?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

A obrigatoriedade de gerar a mensagem referente a nota premiada em ambiente de produção teve inicio no dia 01/02/2020.

* **Conforme o link abaixo:**

<http://www.nfe.ms.gov.br/programa-nota-ms-premiada/>

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056023373/mceclip0.png)

1 - Para que seja destacado **no DANFE** é necessário que o parâmetro **MV\_IMPDIR** esteja com o conteúdo **.F.**

**![](https://lh3.googleusercontent.com/-FD0lzU52Kts/Xh5A6sBy5_I/AAAAAAAAA1k/Z19NdC-QMxkXE8AkPV32YvV6stWQZVmzgCK8BGAsYHg/s0/2020-01-14.png)**

2-Para implementação do processo necessário **estar com as atualizações abaixo:**

* **Protheus**

[MP - NFE - Documentos Eletrônicos NFe / NFSe / MDFe / MDe](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043005493)

* **TSS**

[MP - TSS - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-MP-TSS-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS?source=search)

Segue abaixo o exemplo do destaque das dezenas no campo Reservado ao Fisco no **DANFE e XML**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055915453/mceclip0.png)

![](https://lh3.googleusercontent.com/-G0B7jiQTvpk/Xhzc5eZRjmI/AAAAAAAABtE/iF3UCxR3whEpPo2RS0coaTJiSkP-KLkPwCK8BGAsYHg/s0/2020-01-13.png)

* **Saiba mais:**

As dezenas serão geradas pela **SEFAZ/MS** nas seguintes regras básicas:

* Serão geradas 8 dezenas para cada **NF-e/NFC-e**;
* Valor da **NF-e/NFC-e** maior ou igual a R$ 1,00 (um real);
* Considerar **NF-e/NFC-e** emitidas por contribuintes de Mato Grosso do Sul (**UF\_EMIT** = MS);
* Considerar **NF-e/NFC-e** com **CPF** devidamente preenchido;
* Considerar **NF-e/NFC-e** com a Inscrição Estadual (**IE**) do destinatário não preenchida (**null**) ou preenchida com literal “**ISENTO**”;
* Considerar **NF-e/NFC-e** com o indicador operação com consumidor final, tag **indfinal** = 1 (consumidor final);
* Para **NF-e**, considerar o indicador da **IE** do destinatário, tag **indiedest** = 9 (não contribuinte) ou 2 (isento);
* Para **NFC-e**, considerar tag **indiedest** = 9 (não contribuinte);
* Considerar **NF-e/NFC-e** com a finalidade de emissão da **NF-e/NFC-e**, tag **finnfe** = 1 (**NORMAL**);
* Considerar **NF-e/NFC-e** com o tipo de operação, tag **tpnf** = 1 (**Operação de SAÍDA**);
* Para **NF-e**, considerar o tipo de emissão da **NF-e**, tag **tpemis** = 1 (emissão normal) ou 2 (**FS – Formulário de Segurança**) ou 5 (**FS-DA – Formulário de Segurança de Documento Auxiliar**) ou = 4 (**EPEC – Emissão Prévia de Emissão em Contingência**). Observando que as formas de emissão em contingência (2, 5 e 4) retro citadas somente terão dezenas geradas no momento da transmissão e autorização da **NF-e**.
* Obs.: Para as **NF-e** autorizadas com a tag **tpemis**=7 (**SVC-RS – SEFAZ Virtual de Contingência do Rio Grande do Sul**) não serão geradas dezenas, em função de o ambiente autorizador ser diverso da **SEFAZ-MS**;

* Para **NFC-e**, considerar o tipo de emissão da **NF-e**, tag **tpemis** = 1 (emissão normal) ou 9 (emissão em contingência off-line), observando neste último caso que a geração de dezenas só ocorrerá no momento da transmissão e autorização da **NFC-e**.

Obs: Não é necessário alterações cadastrais no ERP apos as atualizações.
