---
content_hash: 122f1b7eb5693b27fa10b25eacdbbca009e7e53e76c9fa53ac20a354b752ced2
fetched_at: '2026-06-29T00:09:25.426932+00:00'
page_id: '423938147'
product: rm
source: tdn-rm
title: Excluir Contabilização de Movimentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938147
version: 3
---

Esta opção somente será visualizada se o tipo de movimento for parametrizado para [Utilizar Evento Contábil](http://tdn.totvs.com/display/LRM/Contabilizar+Movimentos) (Parâmetros do Tipo de Movimento | etapa Contabilização).   
O processo de excluir a contabilização dos movimentos é utilizado quando há alguma modificação no escopo contábil do Evento Contábil utilizado para a contabilização de movimentos.   
Desta forma, este processo exclui todos os lançamentos contábeis dos movimentos selecionados, deixando o movimento pronto para uma nova Contabilização.   
Este processo somente poderá ser executado se o movimento já estiver contabilizado.  
Após a execução do processo de excluir a contabilização dos movimentos, a rotina de [Contabilizar Movimentos](http://tdn.totvs.com/pages/viewpage.action?pageId=423938693) estará disponível para ser utilizada.

A partir da versão/patch **12.1.2605.275**, os processos de Excluir Contabilização de Movimentos poderá ser configurados para utilizar o fracionamento de jobs, utilizando a classe à seguir:

* MovEstornarContabilidadeMovProc

Os processos de Excluir Contabilização de Movimentos poderão ser executados com ou sem fracionamentos de jobs. 

Para informações detalhadas sobre o fracionamento de jobs, consultar a documentação [Configuração de fracionamento de jobs.](https://tdn.totvs.com/x/lpR-I)
