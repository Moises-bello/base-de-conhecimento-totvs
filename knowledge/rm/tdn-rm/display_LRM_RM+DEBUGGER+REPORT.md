---
content_hash: aa48bb346e9e579a6d209ffed8df863c0aba05314ce1e3618de625aa68721561
fetched_at: '2026-06-29T00:11:20.729089+00:00'
page_id: '687742696'
product: rm
source: tdn-rm
title: RM DEBUGGER REPORT
type: documentation
url: https://tdn.totvs.com/display/LRM/RM+DEBUGGER+REPORT
version: 22
---

## Índice

1

# Introdução

O RM Debugger Report é um serviço de análise de dump do RM que nos permite fazer um diagnóstico completo do processo no momento que o arquivo de despejo é gerado.   
Podemos analisar eventuais vazamentos de memória, crashes de processos (crash dump), consultas com grande volumes de dados, relatórios com problemas e também uma série de outros fatores que podem estar comprometendo a saúde da aplicação.

Pode ser realizado no ambiente de produção do cliente.

# Visão Geral

Acesse o site, <https://rmdbg.totvs.com.br/>

São necessários 3 passos básicos para utilizar a ferramenta.

1. Criar o arquivo de despejo
2. Upload do arquivo
3. Análise do Dump

# 1) Criando o arquivo de despejo

Para criar o arquivo de despejo vamos utilizar o Gerenciador de Tarefas do Windows. Selecione processo desejado, clicando com o botão direito, selecionar Criar arquivo de despejo.

Aguarde o processamento e após, será apresentada a seguinte tela para salvar o arquivo.

# 2) Upload do arquivo

Antes de realizar o envio do arquivo de despejo ele deverá ser compactado. Geralmente é muito grande, portanto mesmo compactado o envio pode demorar.

Gere um arquivo zip do arquivo de despejo (Compactar o arquivo)

Agora o arquivo compactado deverá ser enviado para o site, [https://rmdbg.totvs.com.br](https://rmdbg.totvs.com.br/)

Ao arrastar ou selecionar o arquivo zip, será apresentada a seguinte tela:

Selecione Iniciar envio para realizar o upload. Aguarde o processo...

Será apresentada outra tela com a Chave para consulta(ID Hash) que identifica o Dump para ser analisado.

Copie esta chave e guarde para realizar a consulta.

ATENÇÃO

Caso fechar esta tela sem copiar a chave, ela poderá ser obtida no menu Análise → Últimas Análises

# 3) Análise do Dump

Finalizado o envio o dump estará disponível para análise, guarde o ID para realizar a consulta.

**Consulta Análise**

Serão apresentadas as seguintes análises:

* Assemblies
* Threads
* Objetos em memória
* Fila de finalização
* Objetos RM em memória
* Grandes Data Tables em memória
* Data Tables de muitos registros
* Objetos de grandes volumes
* Relatórios

**Baixar arquivo de análise (.mdbg)**

Realiza do download do arquivo json com o resultado da análise, conforme apresentado abaixo:

**Últimas Análises**

Listagem que permite ver a últimas análises processadas e visualizar novamente uma consulta.

# Informações do Dump

Apresenta o resultado da análise com informações detalhadas para tomadas de decisão.

## Assemblies

Listagem de todas as Dlls carregadas.

## Threads

Informa todas as Threads que estão sendo executadas no momento da geração do Dump.

## Objetos em memória

Listagem de todos os objetos que estão alocando memória no momento do Dump.

## Fila de finalização

Lista de objetos que estão para serem liberados da memória.

## Objetos RM em memória

Lista de objetos do tipo RM que estão em memória.

## Grandes Data Tables em memória

DataTables que estão alocando grande quantidade de memória.

## Data Tables de muitos registros

DataTables que estão em memória e com muitos registros.

## Objetos de grandes volumes

Lista de objetos do mesmo tipo(iguais), que estão alocados em memória.

## Relatórios

Lista dos relatórios que estão alocados em memória.
