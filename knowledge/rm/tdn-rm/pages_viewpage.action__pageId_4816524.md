---
content_hash: ef4209436b2a549052133d8b4ad6d0abea22276ed2c1c9c02e298133100c381a
fetched_at: '2026-06-29T00:10:19.592727+00:00'
page_id: '4816524'
product: rm
source: tdn-rm
title: Inclusão de consultas SQL em anexos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4816524
version: 4
---

BLOCK

Inclusão de consultas SQL em anexos

FAQ: **Inclusão de consultas SQL em anexos**

|  |  |
| --- | --- |
| Produto: | Unspecified |
| Ambiente: | Unspecified |
| Versão: | 11.XX |

Solução

|  |
| --- |
| **Produto:** *Framework* **Versão:** *11.20* |
| **Processo:** *Inclusão de consultas SQL em anexos* |
|  |
|  |
| **Introdução**    *Este documento tem como objetivo demonstrar como proceder para realizar a inclusão de*  ***Consultas SQL*** *em anexo.* |

|  |  |
| --- | --- |
|  | **Desenvolvimento/Procedimento**     1. Primeiramente deverá possuir uma consulta SQL já salva no sistema para que a mesma seja utilizada. No nosso exemplo utilizaremos uma SQL que será aplicada no módulo gestão financeira.   **Esta consulta irá retornar os lançamentos vencidos e não pagos por cliente fornecedor.**    **SELECT** IDLAN, DATAEMISSAO, DATAVENCIMENTO, VALORORIGINAL  **FROM** FLAN  **WHERE** CODCFO = :CLIFOR  **AND** CODCOLIGADA = :COLIGADA  **AND** STATUSLAN = 0  **AND** CODCOLIGADA = 1   1. Utilizaremos o cadastro de cliente / Fornecedor para retornar os dados em anexo da consulta.  1. Ao acessar o cadastro de Cliente / Fornecedor clique em: Anexos àConsultas SQL à Inserir consultas SQL   [clip_image002](http://lh4.ggpht.com/_G7KXZLoZDsY/TQDKqbqGP2I/AAAAAAAAEfg/Q9SCtRGsdEU/s1600-h/clip_image002%5B10%5D.jpg)  No Wisard informe a descrição do processo.  [clip_image004](http://lh4.ggpht.com/_G7KXZLoZDsY/TQDKtatifVI/AAAAAAAAEfs/jyhS2NVHnxE/s1600-h/clip_image004%5B5%5D.jpg)  Selecione a consulta SQL que será utilizada no anexo.  [clip_image006](http://lh6.ggpht.com/_G7KXZLoZDsY/TQDKwAR9t0I/AAAAAAAAEf4/7RoSrGFHfYw/s1600-h/clip_image006%5B5%5D.jpg)  Na próxima tela, insira o valor do parâmetro correspondente a consulta.  Esta consulta SQL utiliza os parâmetros ***“CliFor” e “Coligada”*** deve-se neste caso informar o  campo chave da tabela para este parâmetro que é o campo **CODCFO e CODCOLIGADA**.  [clip_image008](http://lh6.ggpht.com/_G7KXZLoZDsY/TQDKzJbRc1I/AAAAAAAAEgE/wRG4jIWbAjU/s1600-h/clip_image008%5B6%5D.jpg)  Nesta tela é possível definir quais permissões de usuários para geração da consulta SQL.  No nosso caso utilizaremos todos, porém é possível determinar qual usuário / perfil terá acesso.  [clip_image010](http://lh4.ggpht.com/_G7KXZLoZDsY/TQDK15QITRI/AAAAAAAAEgQ/9AMLvVI7KOI/s1600-h/clip_image010%5B6%5D.jpg)  Finalizar o processo.  [clip_image012](http://lh3.ggpht.com/_G7KXZLoZDsY/TQDK3Cs-_aI/AAAAAAAAEgc/kcgB9DDz4l4/s1600-h/clip_image012%5B6%5D.jpg)  Processo executado com sucesso.  [clip_image014](http://lh4.ggpht.com/_G7KXZLoZDsY/TQDK7JFnHsI/AAAAAAAAEgo/-JfyfsWwJYs/s1600-h/clip_image014%5B5%5D.jpg) |
|  | 1. **Executando a consulta em anexo.**   Ao clicar em: ***Anexos*** ***à*** ***Consultas SQL***, será apresentada a consulta parametrizada.  Para execução clique sobre a consulta.  [clip_image016](http://lh3.ggpht.com/_G7KXZLoZDsY/TQDK9jSUdhI/AAAAAAAAEg0/V7RwqVHNrZo/s1600-h/clip_image016%5B6%5D.jpg)  Será executada a consulta SQL retornando os dados referentes a cada registro **(CLI / FOR)**  ***A cada seleção de Cli / For observe que a consulta SQL será recalculada de acordo com*** ***cada contexto existente.***  [clip_image018](http://lh3.ggpht.com/_G7KXZLoZDsY/TQDLBTlx0iI/AAAAAAAAEhA/7UNujsnx33Y/s1600-h/clip_image018%5B5%5D.jpg) |
