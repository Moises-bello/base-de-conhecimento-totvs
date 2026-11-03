---
content_hash: 63650ead45ceaa7ca1b982ed187a78154725050ccb1845fc8626dcbcb6e1e72e
fetched_at: '2026-06-29T00:09:14.116175+00:00'
page_id: '421385130'
product: rm
source: tdn-rm
title: Adiantamento de Contratos para Argentina
type: documentation
url: https://tdn.totvs.com/display/LRM/Adiantamento+de+Contratos+para+Argentina
version: 2
---

Foi realizada uma melhoria no controle de adiantamento de contratos para a Argentina, pois lá incidem impostos sobre essa operação financeira. Essa funcionalidade está disponível apenas para o Totvs Obras e Projetos, quando está integrado ao Backoffice Protheus e a base de dados está localizada para Argentina (Mnemônico 'ARG' no campo país da tabela GPARAMS do RM).  
 Para o Totvs Obras e Projetos quando o país está definido como Brasil, ou qualquer outro diferente de Argentina o comportamento do adiantamento de contratos permanece o mesmo.

**Passos para realizar a liberação de adiantamentos:**

* Realizar no módulo financeiro do Protheus (SIGAFIN), um adiantamento a fornecedor "PA" (se contrato a pagar) ou um adiantamento recebido "RA" (se contrato a receber).
* Um detalhe importante é que o adiantamento deverá ser vinculado a um projeto; - O PA ou RA será transmitido ao RM;
* Acessar , no TOP, o processo "Importar Adiantamentos do Financeiro", dentro da visão de contratos;
* Selecionar o adiantamento e vincular ao respectivo contrato;
* Executar.

**Importante:** Se for necessário cancelar ou excluir um adiantamento no Protheus será necessário executar no TOP o processo "Cancelar Liberação de Adiantamento", que irá desbloquear o adiantamento no Protheus permitindo sua edição/exclusão.  
Antes de usar a funcionalidade é necessário que os projetos do TOP sejam sincronizados com o Protheus. Também é necessário definir no Protheus o parâmetro "Centro de Custo padrão para integração", com o centro de custo utilizado no projeto/contrato.
