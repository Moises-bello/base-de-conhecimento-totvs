---
content_hash: f39c53531c59543e92499e95f6f227576cf47b907b6e24746d65319979bc9382
fetched_at: '2026-06-29T00:11:49.341569+00:00'
page_id: '830947643'
product: rm
source: tdn-rm
title: Enviar CT-e
type: documentation
url: https://tdn.totvs.com/display/LRM/Enviar+CT-e
version: 16
---

# Conteúdo

Conteúdononenone

# 1. Visão Geral

O processo de Enviar CT-e no Módulo TOTVS Gestão de Estoque, Compras e Faturamento transforma os movimentos criados nesse módulo em documentos fiscais eletrônicos (xmls) que são enviados para a SEFAZ do Contribuinte.

# 2. Execução do Processo

O processo Enviar pode ser executado conforme abaixo

ExecuçãoEnviar CT-e (principal)

A execução deste processo ocorre através do menu *Menu **Documentos Eletrônicos | Conhecimento de Transporte Eletrônico (CT-e) |*** **Processos |** ***Enviar CT-e.*** Este processo pode ser executado de duas formas:

1- Selecionando registros com status Inconsistente ou Rejeitado ou Contingência. Esta opção é ideal para emissão isoladas e não deve ser utilizada para emissão de grandes volumes de CT-e

2- Não selecionando nenhum registro e preenchendo os campos na tela de execução. Esta opção é interessante para o envio de vários documentos simultaneamente, ela tem melhor desempenho e facilidade para emitir grandes volumes de CT-e em uma única execução.

Enviar CT-e (a partir do Movimento)

A execução deste processo ocorre através da tela do **Movimento** ***|* Processos |** ***Enviar CT-e**,* sendo necessário selecionar os Movimento que serão enviados.

Esta opção é interessante para o envio pontual de Movimentos específicos, para grandes volumes de CT-e utilize a opção Enviar CT-e (principal)*.*

# 3. Transmissão para o ambiente do governo

A Transmissão do CT-e será realizada utilizando um dos serviços de integração **TSS** ou **TPF,**e ao executar o processo Enviar CT-e o sistema seguirá o fluxo de integração conforme abaixo

Dica

Para verificar qual a integração esta sendo utilizada, acesse o tópico "Parâmetros" da página principal do CT-e:

Fluxo do ProcessoIntegrado com TSS

Abaixo segue uma representação do fluxo de comunicação entre o RM e o TSS durante o processo "Enviar CT-e".

trueEnviar CT-e RM x TSSfalseautohiddentrue7533

Integrado com TPF

Abaixo segue uma representação do fluxo de comunicação entre o RM e o TPF durante o processo "Enviar CT-e"

trueEnviar CT-e RM x TPFfalseautohiddentrue4413
