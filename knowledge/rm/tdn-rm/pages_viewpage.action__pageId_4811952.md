---
content_hash: 3a9bf4ddea6dcd1288846a85383da79619551dc72803f977d750a951cd15fe0f
fetched_at: '2026-06-29T00:10:18.458991+00:00'
page_id: '4811952'
product: rm
source: tdn-rm
title: RMFIN000010_Reconciliação Bancária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4811952
version: 6
---

BLOCK

Reconciliação Bancária

FAQ: **Reconciliação Bancária**

|  |  |
| --- | --- |
| Produto: | TOTVS Gestão Financeira |
| Ambiente: | Linha RM |
| Versão: | 11.00 |

Solução

**Introdução**

*Através do processo de Reconciliação é possível conferir de maneira automática se as movimentações bancárias de determinada Conta Corrente estão devidamente cadastradas no RM Fluxus. Desta forma, o cadastro de Extrato de Caixa será um espelho do Extrato Bancário e, o controle dos saldos e previsão financeira da empresa será mais ágil e exato.*

**Desenvolvimento/Procedimento**

*1º. Primeiramente, deve-se preencher o Layout Bancário referente à Reconciliação. Para isso, acesse o menu Cadastros | Bancos e Agências | Selecione o Banco em questão | Anexos Layout Bancário | pasta Reconciliação | Preencha os campos de acordo com as informações do manual para Conciliação Bancária, fornecido pelo banco e salve a alteração. Para os bancos que utilizam o padrão FEBRABAN 240 posições, não é necessário o preenchimento deste layout, pois este já foi cadastrado internamente.*

*2º. Acesse o menu Utilitários | Integração Bancária | Reconciliação Bancária | Na tela de filtro de Extratos que será apresentada, filtre os registros que deseja reconciliar, pelo Código da Conta/Caixa e um período, por exemplo | clique em OK para que a visão de Extratos de Caixa seja apresentada.*

*3º. Na tela de Importação que será apresentada, informe o caminho onde se encontra o arquivo de reconciliação, o Banco com o qual está sendo realizada a integração e a Conta/Caixa dos Extratos que precisam ser Conciliados.*

*Nesta tela, é possível redefinir o filtro da visão de Extratos de Caixa de acordo com a Data desejada. Para isso, deve-se verificar a opção Filtro por data. Nesta, é possível manter os extratos de caixa de acordo com o filtro utilizado na visão (filtro que foi apresentado no início do processo, quando o usuário escolheu a opção Reconciliação Bancária) ou se basear na Data dos Extratos que constam no arquivo.*

*Se o Número do Documento dos Extratos existentes no sistema forem maiores que os enviados pelo banco, é possível completar com zeros à esquerda esta numeração do Extrato informado no arquivo bancário. Para isso, a quantidade de posições desejada deve ser informada e a opção Período de acordo com o arquivo deve ser selecionada.*

*4º. Preenchidos todos os campos, clique em Importar para que a visão de Extratos seja apresentada. A visão de Extratos de Caixa será dividida ao meio, sendo os Extratos gravados no sistema apresentados na parte superior e os registros vindos do banco na parte inferior.*

*Através da barra de filtros apresentada na parte central da tela, é possível definir quais os registros vindos do banco que serão apresentados. Podem-se filtrar por Extratos Conciliados, Não Conciliados, Saques e Depósitos. Ainda na parte central, existem ícones para execução, controle e estorno do processo de Reconciliação. Através destes ícones é possível realizar a Reconciliação de forma automática, pode-se incluir um Extrato no sistema que possua as mesmas informações de um Extrato vindo do banco, imprimir a visão de Reconciliação e ainda realizar a Reconciliação Manual, registro por registro.*

*Ao realizar a Reconciliação Automática, no final do processo será apresentada uma janela informando quantos extratos foram reconciliados, o valor total reconciliado e quantos extratos bancários não foram encontrados. Ao finalizar a Reconciliação, pode-se sair da tela sem que as modificações executadas sejam efetivamente salvas. Para isso, deve-se clicar no ícone Cancelar processo de Conciliação sem salvar. Para salvar, basta clicar no ícone Finalizar processo de Conciliação.*

*Existe ainda a possibilidade de Conciliar um Extrato existente no RM Fluxus com vários registros vindos do banco, ou vice versa. Isso só será possível se a soma dos valores dos extratos coincidir e de forma manual. Além disso, só será realizada a conferência da soma dos valores dos extratos. Demais dados não serão conferidos.*

**Informações Adicionais**

*- O processo de Reconciliação Bancária implementado no RM Fluxus pode ser realizado no padrão FEBRABAN CNAB 240 e no padrão específico do Banco do Brasil.*

*- Na reconciliação do Banco do Brasil, mesmo tendo mais de uma conta corrente, é gerado apenas um arquivo texto para importação, sendo necessário, após clicar no botão "Importar", selecionar a conta que deseja fazer a reconciliação.*
