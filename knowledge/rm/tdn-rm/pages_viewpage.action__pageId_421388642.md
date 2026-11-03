---
content_hash: 4ad17bfe38189adb0db7b066fa2d4d66cd53fba5f7d4ebaa21f85dde3d2d9f2b
fetched_at: '2026-06-29T00:09:17.768637+00:00'
page_id: '421388642'
product: rm
source: tdn-rm
title: FIN - Borderô de Pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388642
version: 21
---

O Borderô de Pagamento é um recurso que consiste apenas no agrupamento de Lançamentos para fins de remessa ao Banco.

A baixa dos Lançamentos é realizada através da visão de lançamentos, de forma manual ou através de importação de arquivos de retorno disponibilizado pelo Banco.

É possível imprimir relatórios simplificados dos Lançamentos do Borderô, através do menu "Borderô de Pagamentos", basta selecionar o borderô e em Anexos | Lançamentos, habilite apenas as colunas desejadas e clique no ícone "Relatório Simplificado".

O cadastro de borderô está associado à tabela FBORDERO, onde será executado o controle/autorização dos pagamentos eletrônicos.

Vantagens

* Permite o agrupamento de Lançamentos Financeiros provenientes de qualquer segmento para remessa.
* Permite aprovação prévia.
* Permite inserção de novos Lançamentos ao Borderô.
* Permite que Lançamentos sejam desvinculados do Borderô.
* Permite relatório simplificado de Lançamentos do Borderô.
Regras de utilização

* Só é permitido a inclusão de borderô para lançamentos a pagar;
* Só é permitido a inclusão de borderô quando o campo relativo à “Forma de Pagamento” for preenchido no (s) lançamento (s). Este campo se encontra na aba “Integração Bancária” do lançamento em “[Dados Bancários](https://tdn.totvs.com/x/LeIdGQ)”, o cadastramento do campo será no cadastro do Cliente Fornecedor.
* Só será permitido a inclusão de borderô para lançamento que utilize conta caixa associada a um convênio. O convênio associado deve conter os dados necessários para geração da Remessa de pagamento do borderô, como por exemplo o Layout de pagamento de remessa.
Inclusão de Borderô

A inclusão de um borderô pode ser realizada pela visão de lançamentos, basta selecionar o (s) Lançamento (s) e acessar o Menu: Processos | Borderô de Pagamento | Incluir Borderô ou através da opção '[Borderô de pagamentos em lote](https://tdn.totvs.com/pages/viewpage.action?pageId=565741076)', localizada no menu 'Movimentações Bancárias - Clicar na seta ao lado da opção 'Borderô de pagamentos'. Todos os Lançamentos selecionados na visão de lançamentos farão parte desse borderô. Do mesmo modo, no processo de borderô de pagamento em lote todos os lançamentos retornados nos filtro executado serão considerados no borderô. Caso o parâmetro [Apresentar tela de vínculo ao Incluir Borderô de Pagamento/Vincular Borderô de Pagamento](https://tdn.totvs.com/display/LRM/FIN+-+Contas+a+pagar) esteja marcado, o sistema exibirá uma mensagem informando que existem lançamentos passíveis para vínculo com o (s) lançamento (s) selecionado (s) neste processo, possibilitando o usuário realizar o vínculo do lançamento antes de prosseguir com o processo de inclusão do borderô de pagamento.

No momento da inclusão será preciso informar uma conta caixa, o convênio associado a essa conta caixa será carregado como default.

Caso esteja parametrizado Integração Contábil > Contabilização > Usar Contabilização de Mútuo, será possível selecionar convênios da coligada proprietária da conta caixa também.

Se um ou mais lançamentos selecionados, formam criados com Conta Caixa/Convênio diferentes, o sistema apresenta a mensagem abaixo solicitando a confirmação da alteração e atualizará os lançamentos.

Campo “Data Pagamento”. A data selecionada será utilizada para cálculo do valor liquido dos lançamentos e como base para cumulatividade de retenção. No processo de remessa de pagamento essa mesma data será utilizada. As opões de preenchimento de data são:

* Vencimento
* Emissão
* Previsão de Baixa
* Data opcional (FLAN.DATAOPx)

Item de baixa

Ao incluir um Borderô de Pagamento o sistema gera um “Item de baixa” referente a esse Borderô, que será gerado com status igual a “Borderô”.  O status só será alterado quando o Borderô for remetido ao banco através do processo de “Remessa de Pagamento” e o status será atualizado para “Remetido”. O Item de Baixa está disponível no anexo “Baixas do Lançamento”.

Vincular Borderô de Pagamentos

É permitido que outros lançamentos sejam inseridos em um borderô, desde que esse borderô não tenha sido “Autorizado” ou “Remetido”. A vinculação do (s) lançamento (s) será através da opção “Vincular Borderô de Pagamentos", no menu de processos da Visão de Lançamentos.  Do mesmo modo do processo de inclusão de um novo borderô, o sistema permite realizar vínculos do (s) lançamento (s) selecionado (s) durante a execução deste processo, caso o parâmetro 'Apresentar tela de vínculo ao Incluir Borderô de Pagamento/Vincular Borderô de Pagamento' esteja marcado.

Na tela de execução do processo será possível selecionar somente borderô com status “Pendente” e somente esses serão apresentados para seleção. Após selecionar o borderô o campo convênio será preenchido como default do borderô já gerado.

Desvincular Borderô de Pagamentos

É permitido também que um ou mais lançamentos sejam desvinculados de um Borderô, desde que o mesmo não esteja com o status da remessa igual a “Autorizado”. A desvinculação do (s) lançamento (s) será através da opção “Desvincular Borderô de Pagamentos, no menu de processos da Visão de Lançamentos.

Autorização do Borderô

A autorização de um borderô deve ser processada para que seja permitido gerar Remessa de Pagamento (envio do arquivo de dados ao banco). A autorização será realizada através da visão de Borderô, menu de processos “Autorização de Borderô de Pagamentos”. A autorização terá validade e a data de validação será informada na tela de processando da autorização através do campo “ Nova Data de Validade da Autorização“.

Observação:

A data de validade do Borderô de Pagamentos, não pode ser menor que a data do sistema.

Veja Também

* [Procedimento da Integração do Borderô com o Fluig](http://tdn.totvs.com/x/BiYSCw)
