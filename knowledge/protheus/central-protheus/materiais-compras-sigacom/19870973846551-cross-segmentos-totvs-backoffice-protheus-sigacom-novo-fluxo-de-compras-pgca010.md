---
article_id: 19870973846551
category: Materiais - Compras (SIGACOM)
content_hash: e9153ab22db29c06a0bba24907221f1571f6dd413a24614694860847342d30c3
fetched_at: '2026-06-28T22:41:12.822783+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus  - SIGACOM -  Novo fluxo de Compras
  PGCA010 (NFC) - Não é possivel visualizar alguns fornecedores ao iniciar cotação.
type: support-article
updated_at: '2025-06-26T12:49:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19870973846551-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Novo-fluxo-de-Compras-PGCA010-NFC-N%C3%A3o-%C3%A9-possivel-visualizar-alguns-fornecedores-ao-iniciar-cota%C3%A7%C3%A3o
---

**Dúvida**

Não é possível visualizar alguns fornecedores ao iniciar cotação.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras/GCT - Protheus Release 12.1.2210.

**Solução**

Por padrão, o NFC utiliza o cadastro do Produto x Fornecedor (MATA061) para listar todos os fornecedores disponiveis para o processo de cotação.

Se mesmo assim não aparecer, verifique se o campo C1\_FORNECE da rotina Solicitação de compras (MATA110) encontra-se preenchido, caso o mesmo esteja preenchido será possível visualizar somente o fornecedor que consta nesse campo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19870994582935)

Caso utilize o módulo Gestão de Qualidade deve ser verificado se o fornecedor encontra-se bloqueado por qualidade, confirmando o bloqueado não será possível visualizar o fornecedor ao iniciar a cotação.

- Validar cadastro dentro do módulo Gestão de Qualidade o **Produto x Fornecedor***(MATA061)*o campo **Situação (A5\_SITU) =***N/HABILITADO*

*![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19870994583959)*

***Saiba Mais:***

[*Novo Fluxo de Compras: Guia de Referência*](https://tdn.totvs.com.br/pages/releaseview.action?pageId=680260500)

[*Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Fornecedor não habilitado no Quality é impedido de participar do processo de cotação*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035979154-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Fornecedor-n%C3%A3o-habilitado-no-Quality-%C3%A9-impedido-de-participar-do-processo-de-cota%C3%A7%C3%A3o)
