---
article_id: 20822236713111
category: Materiais - Compras (SIGACOM)
content_hash: fecdf3875955110c85a5eeac085780e00b172774d80a6f0d52d5d815986862ac
fetched_at: '2026-06-28T22:41:10.500773+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Campo CR_TOTAL preenchido
  na liberação de uma Solicitação de Compra por Entidade Contábil.
type: support-article
updated_at: '2024-01-24T14:14:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20822236713111-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Campo-CR-TOTAL-preenchido-na-libera%C3%A7%C3%A3o-de-uma-Solicita%C3%A7%C3%A3o-de-Compra-por-Entidade-Cont%C3%A1bil
---

**Dúvida**Campo CR\_TOTAL preenchido na liberação de uma Solicitação de Compra por Entidade Contábil.

**Ambiente**Protheus – Compras – A partir da versão P12.1.17 

**Solução**

O campo CR\_TOTAL (Valor Total) na rotina Liberação de Documentos é preenchido de acordo com o conteúdo do campo B1\_UPRC no cadastro do Produto, esse campo armazena o valor unitário do Último Preço de Compra do Produto.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20822236687895)

Porém esse campo só será preenchido quando o campo F4\_UPRC possuir o conteúdo igual a 'SIM' no cadastro da TES que é utilizada para esse produto, caso o conteúdo desse campo seja igual a 'NÃO' o sistema não irá armazenar o Último Preço de Compra do Produto. 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20822233873175)

**Importante:**Na rotina de Documento de Entrada (MATA103), clicando em F12, existem dois perguntes relacionados a atualização do campo B1\_UPRC:

1. "Ultimo preco c/Desc" - Opção utilizada para considerar o valor de desconto na atualização dos campos B1\_UPRC (Último preço de compra), no momento da gravação do Documento de Entrada:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20822236689943)

2. "Atualiza ultimo preço por" - Caso o usuário tenha a necessidade de considerar a data de recebimento, será gravado o conteúdo do campo D1\_DTDIGIT (Data de Digitação), caso necessite considerar a data de emissão, será gravado o conteúdo do campo D1\_Emissão (Data de Emissão):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20822236692375)

**Saiba Mais:**

**[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como atualizar o campo B1\_UPRC com o ultimo preço de Compra?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412738117399-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-atualizar-o-campo-B1-UPRC-com-o-ultimo-pre%C3%A7o-de-Compra?source=search)**

**[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Alçada de Solicitação de Compras por Entidade Contábi](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017527952-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Al%C3%A7ada-de-Solicita%C3%A7%C3%A3o-de-Compras-por-Entidade-Cont%C3%A1bil)**
