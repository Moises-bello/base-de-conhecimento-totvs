---
content_hash: 398af0218a99181f9421f86aaedaa5a51bac0000b54ff77666fb6a5a3797df7f
fetched_at: '2026-07-02T19:24:25.836320+00:00'
page_id: '513421878'
product: protheus
source: tdn-tec
title: DBTools
type: documentation
url: https://tdn.totvs.com/display/tec/DBTools
version: 12
---

DBTools

## O que é o DBTools

O utilitário DBTools é uma ferramenta de linha de comandos multi-plataforma (para Windows e Linux, 32 e 64 bits) criada para permitir operações adicionais relacionadas ao true e aos dados e ambientes acessados.

Além da ferramenta não depender de uma interface gráfica, ela também permite a execução de procedimentos em modos batch, mediante arquivo de configuração e parâmetros de linha de comando.

* O DBTools está disponível nos pacotes oficiais do true com versão igual ou superior a 20.1.1.5;
* A utilização deste utilitário requer um true com versão igual ou superior a 19.2.1.0;
* Os SGBDs de destino suportados são MSSQL, Oracle e PostgreSQL;
* Os SGBDs de origem suportados são, DB2, Informix, MSSQL, OpenEdge, Oracle e PostgreSQL.

---

## Migrador de Ambientes

A primeira funcionalidade implementada é um assistente para migração de dados entre SGBDs utilizando o true para acessar os ambientes de origem e destino da cópia de dados.

Este recurso permite:

* Cópia de múltiplas tabelas em processos simultâneos, com leitura e gravação otimizada
* Parametrização para inserir ou excluir uma ou mais máscaras de filtro para selecionar as tabelas
* Ordenação automática (em ordem decrescente por tamanho)
* Copiar ou ignorar tabelas sem registros
* Criar os índices das tabelas no SGBD de destino baseado nas definições de índices de origem
* Criar as tabelas no ambiente de destino respeitando as definições avançadas e adicionais de tabelas permitidas pelo true, como utilização de campos CLOB e numeração automática de registros pelo SGBD

Todos os detalhes dessa funcionalidade estão descritos no tópico 

---

## Modos de Operação

Como uma ferramenta do tipo "console" ou "terminal", ela pode ser executada em ambientes Windows e/ou Linux, com ou sem interface gráfica.

Ela utiliza uma interface de terminal ANSI, o que permite que a ferramenta seja executada sem restrições, inclusive em conexões remotas de terminal (em ambientes Linux, com o Putty, por exemplo).

A utilização da ferramenta permite um acionamento em modo "batch", o que permite seu uso em automação de processos ou scripts com disparo sem interface.

Caso o terminal em uso não tenha a capacidade de emular o modo ANSI, que permite cores e reposicionamento de cursor, a aplicação pode ser iniciada com um parâmetro de linha de comando que desliga o modo ANSI e mantém as funcionalidades originais, apenas com um layout de tela mais simples.

Para maiores detalhes sobre os parâmetros de linha de comando, veja a documentação no tópico **Parâmetros de linha de comando****.**

---

## Veja também

* [Descontinuação Bancos de Dados DB2 e Informix para Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047923734-Descontinua%C3%A7%C3%A3o-Bancos-de-Dados-DB2-e-Informix-para-Protheus)
