---
content_hash: a9e74585e1c1b0c43513763a3066c1fc35b5263f9becb78dbdba7c1e40746cf5
fetched_at: '2026-06-29T00:11:45.659338+00:00'
page_id: '820569710'
product: rm
source: tdn-rm
title: Preparação para Conversão de Base (Clientes que já utilizam Portal de Imóveis)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=820569710
version: 12
---

Preparação para Conversão de Base de Dados do Portal de Imóveis

Importante

A funcionalidade de unificação de bases do Portal de Imóveis foi lançada inicialmente para clientes pilotos na versão **12.1.2310, com o Patch 138 no RM e o Patch 1** no Portal de Imóveis, como parte de um processo controlado de validação.

Agora, com a versão 12.1.2502, a funcionalidade continua disponível, mas é necessário solicitar e passar por uma análise específica para garantir a melhor experiência e atender às necessidades de cada cliente. Se tiver interesse, entre em contato com nossa equipe (consultores e suporte) para solicitar o processo de conversão.   
Após as validações finais, a funcionalidade será disponibilizada gradualmente para todos os clientes.

## Guia passo a passo

Selecione abaixo o tipo de contrato para prosseguir.

conversaoexistenteonpremiseCliente Instalação Padrão

1. Execute a **instalação** do RM, em uma **versão e patch** que tenha os requisitos mínimos exigidos, e também do Portal de Imóveis, na **mesma versão e patch específico**, conforme procedimentos especificados em [Portal de Imóveis - Instalação e configuração - Instalação](https://tdn.totvs.com/pages/releaseview.action?pageId=697715936#Portal-instalacao);

   Informações

   Em caso de erros relacionados ou na base de dados **Oracle**, execute os procedimentos especificados em [Portal de Imóveis - Instalação e configuração - Requisitos Oracle](https://tdn.totvs.com/pages/releaseview.action?pageId=697715936#Portal-oracle).
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
cloudCliente Cloud

1. Atualmente, estamos conduzindo testes iniciais com um grupo restrito de clientes (Pilotos) para garantir a qualidade e eficácia do processo de migração. Assim que a fase de testes for concluída e o processo estiver totalmente validado, informaremos todos os clientes sobre o procedimento para realizar a migração.
