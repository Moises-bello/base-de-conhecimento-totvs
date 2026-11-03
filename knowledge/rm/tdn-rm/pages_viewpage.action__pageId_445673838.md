---
content_hash: f404aec9c73d7d3f107dedfc250c2baff79d1e2a9b0c08228f14de988d6cee31
fetched_at: '2026-06-29T00:09:55.007007+00:00'
page_id: '445673838'
product: rm
source: tdn-rm
title: Contrato de Locação - Processo - Prorrogar Contrato por Tempo Indeterminado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=445673838
version: 10
---

A partir da versão 12.1.22, o processo "Prorrogar contrato por tempo indeterminado", possibilita ao usuário prorrogar um ou vários contratos de locação por tempo indeterminado, sem que sejam associados aditivos de prorrogação aos Contratos.  
Para que o processo seja executado corretamente é necessário habilitar o parâmetro 'Permite o Contrato de Locação ter prazo indeterminado', presente em Ambiente / Parâmetros / TOTVS Incorporação / Aluguel / Contrato de Locação:

É necessário também, habilitar a permissão no perfil do usuário que irá realizar o processo:

* [02] Aluguel
  + [02.03] Contrato de Locação
    - [02.03.01] Contrato de Locação 
      * [02.03.01.49] Prorrogar contrato por tempo indeterminado

Somente contratos de locação em situação [Efetivado] podem ter prazo indeterminado;  
Somente contratos de locação com Final vigência e Prorrogação vigência podem ser prorrogados para prazo indeterminado;  
Não poderão participar do processo, contratos que possuam o prazo de contabilização "Período do contrato" ou marcado para "Aplicar Linearização".  
Só será possível parametrizar o sistema para permitir prazo indeterminado caso a configuração da Contabilidade "Período de contabilização do contrato" esteja parametrizada como "Informar Período".

Para executar a funcionalidade, basta selecionar um ou n contratos de locação e acessar **Processos / Prorrogar contrato por tempo indeterminado.**Caso as condições sejam atendidas o processo prorroga o prazo do contrato de locação por tempo indeterminado e com isso, a data de prorrogação de vigência será alterada para "Prazo Indeterminado.", como mostra a figura abaixo:

Não haverá alterações na data de final de vigência, representando o final do período onde o contrato tinha prazo determinado.

A data final dos locatários associados ao contrato, também serão alteradas para nulo:

A execução deste processo também gera um registro no histórico do contrato de locação.
