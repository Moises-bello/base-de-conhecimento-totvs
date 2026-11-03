---
content_hash: b1df00f1e9acb2643fc020551c82bc448dc1b18b5ae3f010fbabf279c54e41f9
fetched_at: '2026-06-29T00:11:45.679078+00:00'
page_id: '820569861'
product: rm
source: tdn-rm
title: Preparação para Conversão de Base (Clientes novos do Portal de Imóveis)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=820569861
version: 9
---

Preparação para Conversão de Base de Dados do Portal de Imóveis

Importante

Esta unificação de bases está disponível **somente para alguns clientes Pilotos na versão 12.1.2310, a partir do Patch 138** e versões mais atuais do RM e **na versão 12.1.2310, a partir do Patch 1** e versões mais atuais do Portal de Imóveis. Depois dessa analise especifica, disponibilizaremos para todo o mercado.

## Guia passo a passo

Selecione abaixo o tipo de contrato para prosseguir.

conversaonovoonpremiseCliente Instalação Padrão

1. Execute a **instalação** do RM, em uma **versão e patch** que tenha os requisitos mínimos exigidos, e também do Portal de Imóveis, na **mesma versão e patch específico**, conforme procedimentos especificados em [Portal de Imóveis - Instalação e configuração - Instalação](https://tdn.totvs.com/pages/releaseview.action?pageId=697715936#Portal-instalacao);

   Informações

   Em caso de erros relacionados ou na base de dados **Oracle**, execute os procedimentos especificados em [Portal de Imóveis - Instalação e configuração - Requisitos Oracle](https://tdn.totvs.com/pages/releaseview.action?pageId=697715936#Portal-oracle).
2. Verifique se a **comissão** está na **versão 2.0**, conferindo se o resultado do campo **VALOR** para a consulta  seja igual **1**;

   falseExemplo de resultado da consulta.falseComo proceder caso a comissão não esteja na versão 2.0?
   1. Execute os procedimentos especificados em;
   2. Execute os procedimentos especificados em [Portal de Imóveis - Instalação e configuração - Configurando Comissão 2.0](https://tdn.totvs.com/pages/viewpage.action?pageId=697715936#Portal-configcomissao);
3. Verifique se **CORS** (compartilhamento de recursos com origens diferentes) está habilitado no arquivo **Web.config**;

   falseComo verificar se CORS (compartilhamento de recursos com origens diferentes) está habilitado no Web.config?

   Verifique a presença, e caso não possua realizar a inclusão, das tags **`<``add` `name``=``"Access-Control-Allow-Origin"` `value``=``"*"` `/>`** e **`<``add` `name``=``"Access-Control-Allow-Headers"` `value``=``"*"` `/>`**, dentro de <customHeaders>, conforme exemplo abaixo.

   xmlEclipseCors








   ]]>
cloudCliente Cloud

1. Enviar um e-mail para o **suporte**, solicitando a Conversão da Base e informando o **[link](https://tdn.totvs.com/pages/releaseview.action?pageId=697715936#Portal-conversaobasepi)** desta página, como referência e para agilizar, junto com a solicitação;
2. Aguarde o retorno do **suporte**;
