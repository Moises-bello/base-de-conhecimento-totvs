---
content_hash: 74c89b7e18efcaf892bcaedfbd2aa06dfa9f647e593e9f928f3426b9cfb1d92c
fetched_at: '2026-07-02T19:24:28.540376+00:00'
page_id: '795103682'
product: protheus
source: tdn-tec
title: Versão 01.04.05
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=795103682
version: 3
---

GreenAppserver 20.3.2.1

## Correção

* Ajustes nos comandos de translate utilizados no REST\_DOC para considerar User Function, sem a necessidade de chave de compilação
* Ajuste na execução dos testes do PROBAT para deixar uma mensagem de erro mais amigável quando não houver resultados, ou seja, sem testes para serem executados (assert)
* O GUI Monitor poderia apresentar falha na conexão com o ambiente ao recarregar a tela

---

## Melhoria

* Foram criadas funções no PROBAT para permitir o registro de resultados de execuções externas (scripts, por exemplo)
* Agora é possível utilizar um skip em toda a classe e não somente nos métodos
* Os skips passam a registrar sua condição no xml que contém o resultado da execução dos testes
* No PROBAT a propriedade isFreak foi alterada para [BlockedWords](https://tdn.totvs.com/display/tec/c+-+INI)
* Foi inserida uma opção no PROBAT (IGNORE\_SKIP) para ignorar todos os Skips definidos (criar tarefa de documentação para as novas chaves)
