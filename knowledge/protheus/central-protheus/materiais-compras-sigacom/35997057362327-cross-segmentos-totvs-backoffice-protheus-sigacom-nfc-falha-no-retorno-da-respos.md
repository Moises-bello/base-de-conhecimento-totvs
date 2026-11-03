---
article_id: 35997057362327
category: Materiais - Compras (SIGACOM)
content_hash: 563c9dce1a8bb9e14e777751f0da32bd76d1294543d5a80e9a44a12af9d9da7f
fetched_at: '2026-06-28T22:41:21.790288+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - Falha no retorno
  da resposta do formulário WF da cotação via e-mail para dentro do Protheus
type: support-article
updated_at: '2025-10-30T19:09:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35997057362327-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-Falha-no-retorno-da-resposta-do-formul%C3%A1rio-WF-da-cota%C3%A7%C3%A3o-via-e-mail-para-dentro-do-Protheus
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35997057341207) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
O que fazer quando o preenchimento do formulário WF do fornecedor não for retornado no Protheus? O que validar quando a proposta do Fornecedor preenchida via Workflow não atualizar os dados da tabela SC8?  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Compras - a partir da Release 12.1.2310

**Solução**  
Para corrigir esse erro, efetue os dois procedimentos abaixo:

**1º passo:**Por gentileza realize teste em ambiente de Homologação com as atualizações a seguir:

- [Acumulado Compras conforme sua versão](https://tdn.totvs.com/pages/releaseview.action?pageId=522011099)  
- [Acumulado Gestão de Contratos conforme sua versão](https://tdn.totvs.com/pages/viewpage.action?pageId=679961416)  
- [Acumulado SIGAGCP conforme sua versão](https://tdn.totvs.com/pages/viewpage.action?pageId=679961656)  
- [LIB Atual](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/) - [Harpia](https://suporte.totvs.com/portal/p/10098/download?e=1050526) | [Onca](https://suporte.totvs.com/portal/p/10098/download?e=1168735)  
- [Appserver](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/) - [Harpia R.33](https://suporte.totvs.com/portal/p/10098/download#detail/1112215) | [Onca](https://suporte.totvs.com/portal/p/10098/download?e=1168420)

- Smartclient - [Harpia R.33](https://suporte.totvs.com/portal/p/10098/download#detail/1112221)

- Smartclient WebApp - [Onca](https://suporte.totvs.com/portal/p/10098/download?e=1168455)

- DBAccess - [MP - FRAME - Atualização do DBAccess](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033789713-MP-FRAME-Atualiza%C3%A7%C3%A3o-do-DBAccess?source=search)

Obs: Recomendamos backup e validação primeiramente em ambiente teste.

**2º passo:** Verifique se o formulário HTML que está utilizando está com a versão correta atualizada. Para receber instruções de como efetuar essa verificação, consulte documentação abaixo.

[Cross Segmentos - Totvs Backoffice Linha Protheus - SIGACOM - O que fazer quando o Novo Fluxo de Compras (PGCA010) não encontra os formulários do Workflow?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/30904114589719-Cross-Segmentos-Totvs-Backoffice-Linha-Protheus-SIGACOM-O-que-fazer-quando-o-Novo-Fluxo-de-Compras-PGCA010-n%C3%A3o-encontra-os-formul%C3%A1rios-do-Workflow)

**3º passo:** Abra o appserver.ini do serviço Workflow (onde o WF do Novo Fluxo de Compra esteja configurado) e verifique como está escrita a chave ROOTPATH, escrita correta é **ROOTPATH** certifique-se que esteja assim. Se estiver escrito incorretamente (por exemplo **ROOTHPATH)** corrija, salve reinicie os serviços e faça novos testes.

<https://tdn.totvs.com/display/tec/RootPath>

**4º passo:** Analise se há alguma validação customizada nos campos da tabela SC8 - Cotações que possa estar impactando no retorno da proposta via Workflow.

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Linha Protheus - SIGACOM - O que fazer quando o Novo Fluxo de Compras (PGCA010) não encontra os formulários do Workflow?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/30904114589719-Cross-Segmentos-Totvs-Backoffice-Linha-Protheus-SIGACOM-O-que-fazer-quando-o-Novo-Fluxo-de-Compras-PGCA010-n%C3%A3o-encontra-os-formul%C3%A1rios-do-Workflow)

<https://tdn.totvs.com/display/tec/RootPath>

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Novo Fluxo de Compras - NFC (PGCA010)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19838751317655-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Novo-Fluxo-de-Compras-NFC-PGCA010)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
