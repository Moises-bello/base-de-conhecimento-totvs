---
content_hash: d2d2093f231f25e17d9103f7ca8e1261bb03fc02c3a32f7cc72ed68059b33ec0
fetched_at: '2026-06-29T00:11:45.673330+00:00'
page_id: '820569765'
product: rm
source: tdn-rm
title: Preparação para Conversão de Base (T-Cloud)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=820569765
version: 9
---

Preparação para Conversão de Base de Dados do Portal de Imóveis

Importante

Esta unificação de bases está disponível **somente para alguns clientes Pilotos na versão 12.1.2310, a partir do Patch 138** e versões mais atuais do RM e **na versão 12.1.2310, a partir do Patch 1** e versões mais atuais do Portal de Imóveis. Depois dessa analise especifica, disponibilizaremos para todo o mercado.

## Guia passo a passo

Selecione abaixo o tipo de contrato para prosseguir.

conversaotcloudnovoCliente novo do Portal de Imóveis

1. Execute a **instalação** do RM, em uma **versão e patch** que tenha os requisitos mínimos exigidos, e também do Portal de Imóveis, na **mesma versão e patch específico**, conforme procedimentos especificados em [Portal de Imóveis - Instalação e configuração - Instalação](https://tdn.totvs.com/pages/releaseview.action?pageId=697715936#Portal-instalacao);

   Informações

   Em caso de erros relacionados ou na base de dados **Oracle**, execute os procedimentos especificados em [Portal de Imóveis - Instalação e configuração - Requisitos Oracle](https://tdn.totvs.com/pages/releaseview.action?pageId=697715936#Portal-oracle).  
   Em caso de erros ao acessar o portal, pode ser necessário utilizar o arquivo **Web.config** disponível ;
2. Verifique se a **comissão** está na **versão 2.0**, conferindo se o resultado do campo **VALOR** para a consulta  seja igual **1**;

   falseExemplo de resultado da consulta.falseComo proceder caso a comissão não esteja na versão 2.0?
   1. Execute os procedimentos especificados em;
   2. Execute os procedimentos especificados em [Portal de Imóveis - Instalação e configuração - Configurando Comissão 2.0](https://tdn.totvs.com/pages/viewpage.action?pageId=697715936#Portal-configcomissao);
3. Verifique se **CORS** (compartilhamento de recursos com origens diferentes) está habilitado no arquivo **Web.config**;

   falseComo verificar se CORS (compartilhamento de recursos com origens diferentes) está habilitado no Web.config?

   Verifique a presença, e caso não possua realizar a inclusão, das tags **`<``add` `name``=``"Access-Control-Allow-Origin"` `value``=``"*"` `/>`** e **`<``add` `name``=``"Access-Control-Allow-Headers"` `value``=``"*"` `/>`**, dentro de <customHeaders>, conforme exemplo abaixo.

   xmlEclipseCors








   ]]>
existenteCliente que já utiliza o Portal de Imóveis

1. Execute a **instalação** do RM, em uma **versão e patch** que tenha os requisitos mínimos exigidos, e também do Portal de Imóveis, na **mesma versão e patch específico**, conforme procedimentos especificados em [Portal de Imóveis - Instalação e configuração - Instalação](https://tdn.totvs.com/pages/releaseview.action?pageId=697715936#Portal-instalacao);

   Informações

   Em caso de erros relacionados ou na base de dados **Oracle**, execute os procedimentos especificados em [Portal de Imóveis - Instalação e configuração - Requisitos Oracle](https://tdn.totvs.com/pages/releaseview.action?pageId=697715936#Portal-oracle).  
   Em caso de erros ao acessar o portal, pode ser necessário utilizar o arquivo **Web.config** disponível ;
2. Abra o arquivo **versao.inf** (dentro de <Local\_Onde\_Está\_Instalado\_PI>\api\) e verifique se o mesmo contem a **versão mínima exigida**, assim como a **versão correta do patch**, ou versão mais atual do Portal de Imóveis;

   falseComo saber qual o local onde está instalado o Portal de Imóveis?

   Abra o **Gerenciador do Serviços de Informações das Internet (IIS)** e localize o **Site do Portal de Imóveis**, conforme exemplo abaixo.

   falseComo proceder caso patch esteja diferente do mínima exigido?

   Altere a versão contida no arquivo para a **versão mínima exigida**, assim como a **versão correta do patch**, ou versão mais atual do Portal de Imóveis, conforme exemplo abaixo.
3. Abra o arquivo **versao.cliente.inf** (dentro de <Local\_Onde\_Está\_Instalado\_PI>\api\) e **apenas confirme** se ele contem a mesma versão presente no arquivo **versao.inf**;

   falseComo saber qual o local onde está instalado o Portal de Imóveis?

   Abra o **Gerenciador do Serviços de Informações das Internet (IIS)** e localize o **Site** do Portal de Imóveis, conforme exemplo abaixo.

   falseComo proceder caso a versão dos arquivos versao.inf e versao.cliente.inf estejam diferentes?

   Abra o Portal de Imóveis e clique no número da versão atualmente instalada, na parte inferior direita do portal (após o login), para que o mesmo realize as atualizações necessárias e, verifique novamente se o arquivo **versao.cliente.inf** foi atualizado corretamente;
4. Verifique se a **comissão** está na **versão 2.0**, conferindo se o resultado do campo **VALOR** para a consulta  seja igual **1**;

   falseExemplo de resultado da consulta.falseComo proceder caso a comissão não esteja na versão 2.0?
   1. Execute os procedimentos especificados em;
   2. Execute os procedimentos especificados em [Portal de Imóveis - Instalação e configuração - Configurando Comissão 2.0](https://tdn.totvs.com/pages/viewpage.action?pageId=697715936#Portal-configcomissao);
5. Execute os procedimentos especificados em ;

   Em caso de erros nesta etapa, que não foram disponibilizadas informações nos [conteúdos de ajuda](https://tdn.totvs.com/pages/releaseview.action?pageId=697715936#Portal-errosesolucoes), favor reporta-los ao **suporte**/**produto**.
6. Altere os dados dos parâmetros **server**, **user**, **pass**, **database** e **port** encontrados no arquivo **config\_db.php** (dentro de <Local\_Onde\_Está\_Instalado\_PI>\api\) para os mesmos utilizados na conexão com a **base do RM**;

   Após este procedimento a base **individual** do Portal de Imóveis **não será** mais ser usada pelo Portal de Imóveis;

   falseComo saber qual o local onde está instalado o Portal de Imóveis?

   Abra o **Gerenciador do Serviços de Informações das Internet (IIS)** e localize o **Site** do Portal de Imóveis, conforme exemplo abaixo.

   falseComo alterar os dados de conexão ao banco no Portal de Imóveis?
7. Verifique se o Portal de Imóveis está utilizando a **base do RM**;

   falseComo verificar se o Portal de Imóveis está utilizando a base do RM?
   1. Após o o login no Portal de Imóveis, acesse **Backend** > **Sistema** > **Inspeção Técnica**;
   2. Se ao executar a consulta SQL abaixo, invés de exibir uma listagem com os registros encontrados, apresentar uma mensagem de erro em vermelho (conforme imagem abaixo) repita este passo, informando os dados de conexão para que o Portal de Imóveis possa conectar com a **base do RM**;
8. Verifique se **CORS** (compartilhamento de recursos com origens diferentes) está habilitado no arquivo **Web.config**;

   falseComo verificar se CORS (compartilhamento de recursos com origens diferentes) está habilitado no Web.config?

   Verifique a presença, e caso não possua realizar a inclusão, das tags **`<``add` `name``=``"Access-Control-Allow-Origin"` `value``=``"*"` `/>`** e **`<``add` `name``=``"Access-Control-Allow-Headers"` `value``=``"*"` `/>`**, dentro de <customHeaders>, conforme exemplo abaixo.

   xmlEclipseCors








   ]]>
