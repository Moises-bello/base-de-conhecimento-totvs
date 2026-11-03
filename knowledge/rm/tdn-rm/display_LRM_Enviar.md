---
content_hash: bdd48842b79812041bada42610266dd517beb018964b49c03f19267a4b0f8bbe
fetched_at: '2026-06-29T00:09:20.564349+00:00'
page_id: '422545708'
product: rm
source: tdn-rm
title: Enviar
type: documentation
url: https://tdn.totvs.com/display/LRM/Enviar
version: 56
---

# Conteúdo

Conteúdo

# 1. Visão Geral

O processo de envio de Notas Fiscais Eletrônicas (NF-e) e Notas Fiscais de Consumidor Eletrônicas (NFC-e) no Módulo TOTVS Gestão de Estoque, Compras e Faturamento transforma os movimentos criados nesse módulo em documentos fiscais eletrônicos (xmls) que são enviados para a SEFAZ do Contribuinte.

# 2. Execução do Processo

O processo Enviar pode ser Executado conforme abaixo:

ExecuçãoEnviar (principal)

A execução deste processo ocorre através do menu *Menu **Documentos Eletrônicos | Nota Fiscal Eletrônica (NF-e/NFC-e) |*** **Processos |** ***Enviar.*** Este processo pode ser executado de duas formas:

1- Selecionando registros com status Inconsistente ou Rejeitado ou Contingência

2- Não selecionando nenhum registro e preenchendo os campos na tela de execução

Esta opção é interessante para o envio de vários documentos simultaneamente.

Enviar (a partir do Movimento)

A execução deste processo ocorre através da tela do Movimento *|* Processos | *Enviar NF-e,* sendo necessário selecionar os Movimento que serão enviados.

Esta opção é interessante para o envio pontual de Movimentos específicos, para grandes volumes de notas utilize a opção Enviar (principal)*.*

Enviar (automático por agendamento de job)

Esta opção trata uma automatização da opção *Enviar (principal).*

A execução deste processo ocorre através do menu *Menu **Documentos Eletrônicos | Nota Fiscal Eletrônica (NF-e/NFC-e) |** **Processos |** **Enviar**.*

Na tela de execução do processo, deixe o campo "Data Final" em branco e Defina a recorrência de execução do Job de acordo com a necessidade operacional (diária, semanal, etc.).

Ao configurar esta recorrência a transmissão das notas fiscais será de forma contínua e sem necessidade de intervenção manual, conforme ilustrado abaixo:

Enviar (ao salvar Movimento)

Através dos Parâmetros do Tipo de Movimento | Etapa 67 - Fiscal - Nota Fiscal Eletrônica

Configurando o parâmetro ***NF-e Estadual*** como ***Envia Automaticamente***, a nota será enviada na inclusão do movimento.

# 3. Transmissão para o ambiente do governo

A Transmissão da NF-e/NFC-e será realizada utilizando um dos serviços de integração **TSS** ou **TPF,**e ao executar o processo Enviar o sistema seguirá o fluxo de integração conforme abaixo

IntegraçõesTSS

O TSS (TOTVS Service SOA) é uma aplicação baseada na arquitetura orientada a serviços, em que o objetivo principal é prover os serviços de emissão e manutenção de documentos fiscais eletrônicos. Para mais informações acesse:

Abaixo segue uma representação do fluxo de comunicação entre o RM e o TSS durante o processo "Enviar" para os documentos NF-e e NFC-e

falseIntegracaoTSSEnviarNFefalseautohiddenfalse62010

TPF

O TOTVS Processos Fiscais é um software em nuvem que abrange a Transmissão, Recepção e Armazenamento de Documentos Fiscais Eletrônicos. Para mais informações acesse

Abaixo segue uma representação do fluxo de comunicação entre o RM e o TPF durante o processo "Enviar" para os documentos NF-e e NFC-e

falseEnviarNFeTPFfalseautohiddenfalse3111

# 4. Outras informações

Veja aqui a explicação dos status da NF-e:



Veja também:

* [Parametrização de movimento de saída para a emissão da NF-e](http://tdn.totvs.com/pages/viewpage.action?pageId=65208845)
* [Parametrização de movimento de entrada para emissão da NF-e](http://tdn.totvs.com.br/pages/viewpage.action?pageId=64652332)
