---
article_id: 25256999555735
category: NFe - Nota Fiscal Eletrônica
content_hash: aab5511875df32ae1bd61ed7f75f647f8c9071ee4ce818fe90f14498a65c22e4
fetched_at: '2026-06-28T22:40:00.058656+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como configurar
  wizard.config rotina SPEDNFE
type: support-article
updated_at: '2026-02-09T17:52:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25256999555735-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-configurar-wizard-config-rotina-SPEDNFE
---

**Dúvida**

Como configurar wizard.config para transmissão de notas modelo 55?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos

**Solução**

1- Ao acessar a rotina será apresentada a tela de boas vindas:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25256999539223)

2- Em seguida é solicitada a URL do TSS, que deve ser preenchida exatamanete como declarado no appserver.ini do TSS:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25257007611415)

3- Nesta etapa é necessário informar o certificado digital da empresa a ser utilizado, antes de configurar é necessário que realizem a exportação do certificado conforme indicamos [neste link.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018673092-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-instalar-configurar-cadastrar-o-certificado-digital-modelo-A1)

Devem alterar o formato e deixar como .pfx.

Buscar no drive o arquivo exportado .pfx - **A busca pode ser realizada tanto no servidor quanto na máquina local, o TSS vai converter os arquivos .pfx em .pem e alimentar a pasta certs da sua estrutura, dessa forma não é necessário manter o certificado no servidor.**

Preencher a senha do certificado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25256999541783)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25257007615127)

Ao avançar o certificado será validado e a tela de configuração do e-mail será apresentada.

Em caso de dúvidas referente ao preenchimento desta tela podem consultar os artigos abaixo:

[MP - TSS - Envio de e-mail do danfe gerado pelo erp (customização disponível via rdMake)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041452974-MP-TSS-Envio-de-e-mail-do-danfe-gerado-pelo-erp-customiza%C3%A7%C3%A3o-dispon%C3%ADvel-via-rdMake?source=search)

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como enviar DANFE e XML por e-mail via TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043007793--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-enviar-DANFE-e-XML-por-e-mail-via-TSS)

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 008 - erro no teste de e-mail de envio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063424133--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-008-erro-no-teste-de-e-mail-de-envio)

A tela do wizard grava as informações no momento que é avançado, ou seja não é necessário seguir até a ultima tela caso não precise fazer alterações em todos os parametros. Não sendo mais necessário alterar as configurações subsequentes podem clicar em "cancelar" sem prejudicar a tela anterior preenchida.

Os dados armazenados não ficam gravados na tela, as informações preenchidas nessa configuração são armazenadas nas tabelas do Protheus e TSS e ao reabrir o wizard serão apresentadas em branco para um novo preenchimento.
