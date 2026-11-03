---
content_hash: fc70025f27822c7c17c391c79e018cdf2c8fe46d6ab6a8ce8db0bb4e42f16ae7
fetched_at: '2026-06-29T00:05:45.079725+00:00'
page_id: '1003469490'
product: rm
source: tdn-rm
title: Enviar CT-e OS
type: documentation
url: https://tdn.totvs.com/display/LRM/Enviar+CT-e+OS
version: 6
---

# Conteúdo

Conteúdononenone

# 1. Visão Geral

O processo de Enviar CT-e OS no Módulo TOTVS Gestão de Estoque, Compras e Faturamento transforma os movimentos criados nesse módulo em documentos fiscais eletrônicos (xmls) que são enviados para a SEFAZ do Contribuinte.

Neste processo serão enviados os CT-es OS, de acordo com os dados informados. Após o envio o status do CT-e OS fica como Autorizado.  
No envio o sistema realiza algumas consistências, havendo problemas o status fica como Rejeitado e após a alteração do impedimento, o CT-e OS pode ser selecionado e reenviado.

# 2. Execução do Processo

O processo Enviar pode ser executado conforme abaixo

ExecuçãoEnviar CT-e (principal)

A execução deste processo ocorre através do menu *Menu **Documentos Eletrônicos | Conhecimento de Transporte Eletrônico Outros Serviços (CT-e OS) |*** **Processos |** ***Enviar CT-e OS.*** Este processo pode ser executado de duas formas:

1- Selecionando registros com status Inconsistente ou Rejeitado ou Contingência. Esta opção é ideal para emissão isoladas e não deve ser utilizada para emissão de grandes volumes de CT-e OS.

2- Não selecionando nenhum registro e preenchendo os campos na tela de execução. Esta opção é interessante para o envio de vários documentos simultaneamente, ela tem melhor desempenho e facilidade para emitir grandes volumes de CT-e OS em uma única execução.

Enviar CT-e (a partir do Movimento)

A execução deste processo ocorre através da tela do **Movimento** ***|* Processos |** ***Enviar CT-e OS**,* sendo necessário selecionar os Movimento que serão enviados.

Esta opção é interessante para o envio pontual de Movimentos específicos, para grandes volumes de CT-e OS utilize a opção Enviar CT-e OS (principal)*.*

# 3. Transmissão para o ambiente do governo

A Transmissão do CT-e OS será realizada utilizando um dos serviços de integração **TSS** ou **TPF,**e ao executar o processo Enviar CT-e OS o sistema seguirá o fluxo de integração conforme abaixo

Dica

Para verificar qual a integração esta sendo utilizada, acesse o tópico "Parâmetros" da página principal do CT-e OS:

Fluxo do ProcessoIntegrado com TSS

Abaixo segue uma representação do fluxo de comunicação entre o RM e o TSS durante o processo "Enviar CT-e OS".

trueEnviar CT-e RM x TSSfalseautohiddentrue7534

Integrado com TPF

Abaixo segue uma representação do fluxo de comunicação entre o RM e o TPF durante o processo "Enviar CT-e OS"

trueEnviar CT-e RM x TPFfalseautohiddentrue4412
