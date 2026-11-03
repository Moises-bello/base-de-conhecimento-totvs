---
content_hash: 6b5ea2e07a922a1fad3f735e9d7a282e1e37ec76cacff8153f882b43257b8ccd
fetched_at: '2026-06-29T00:09:18.759030+00:00'
page_id: '421388782'
product: rm
source: tdn-rm
title: Compensar Extrato de Caixa
type: documentation
url: https://tdn.totvs.com/display/LRM/Compensar+Extrato+de+Caixa
version: 3
---

O processo de compensação de extrato de caixa é utilizado para definir que o valor de um registro do extrato já alterou o saldo de uma conta bancária ou de um caixa.  
 Ao compensar um registro do extrato de caixa o seu valor irá alterar o "Saldo Instantâneo" e o "Saldo Não Compensado" de uma Conta/Caixa.

**Exemplo**

Ao realizar o recebimento de cheque para um lançamento financeiro é gerado automaticamente um registro no cadastro de extrato de caixa, alterando o "Saldo Não Compensado" da Conta/Caixa.  
 Quando o valor do cheque for liberado no banco, você deve compensar o registro para que o valor saia do "Saldo Não Compensado" e entre no "Saldo Instantâneo da Conta/Caixa".  
 A compensação de extrato de caixa relacionado a lançamento com cheque apenas será permitida apos baixa do lançamento.

Com um lançamento, emitir um cheque para este lançamento - Baixar o Lançamento criado - Entrar na tela de extrato de caixa e executar o processo de compensação para o extrato gerado. Processo deve ser concluído com sucesso.

**Compensação manual**

O processo de compensação do registro de extrato de caixa é realizado através do menu "Processos" da janela de visão do cadastro de Extrato de Caixa.

Passo a Passo  
Marque o registro e clique na opção "Compensar" do menu "Processos";

* No Assistente de Compensação do Extrato de Caixa informe a "Data de Compensação" e confirme o processo.
* Na pasta de "Identificação" do cadastro do registro o campo "Compensado" será marcado e a data informada será apresentada.

**Observação**  
 A compensação dos registros que possuem a operação "Saque Transferência" obedecerá á funcionalidade do parâmetro "Compensar saque/depósito de transferência separadamente" (Assistente de Implantação de Processos | etapa Extrato de Caixa do Financeiro).

**Compensação automática**

A compensação também pode ser realizada automaticamente ao baixar um lançamento financeiro ou ao emitir/receber um cheque para um lançamento financeiro, dependendo de algumas parametrizações.

**Na baixa**

Marcando o parâmetro "Gerar Extrato Compensado na Baixa" (Assistente de Implantação de Processos | processo Baixa | etapa Baixa de Lançamentos Financeiros), ao realizar a baixa de lançamentos financeiros o sistema gera um registro já compensado no cadastro de extrato de caixa.  Com o parâmetro desmarcado a compensação deverá ser realizada posteriormente.  
 Com o parâmetro "Desvincular Baixa da Compensação de Cheques para Lançamentos a Pagar/Receber" (Assistente de Implantação de Processos | processos Contas a Pagar e Contas a Receber | Baixa a Pagar e Baixa a Receber | etapas Baixa de Lançamentos Financeiros a Pagar e a Receber) desmarcado, ao realizar a baixa de lançamentos financeiros que possuem cheques o sistema compensa automaticamente os registros de extratos vinculados a estes lançamentos. Com o parâmetro marcado a compensação deverá ser realizada posteriormente.

**Na emissão/recebimento**

Marcando o parâmetro "Emite cheque compensado" (Assistente de Implantação de Processos | processo Baixa | etapa Recebimento / Pagamento em Cheque), ao emitir/receber cheque para lançamentos financeiros o sistema gera um registro já compensado no cadastro de extrato de caixa. Com o parâmetro desmarcado a compensação deverá ser realizada posteriormente.  
 Mesmo com o parâmetro desmarcado é possível solicitar a compensação através da janela de cheque, marcando a opção "Compensar Extrato", localizada na pasta "Identificação" do cheque.

**Data de Compensação anterior a Data do Extrato de Caixa**

Para utilizar uma data de compensação que seja anterior à data do extrato de caixa você deve marcar o parâmetro "Permitir data de Emissão posterior à Data de Compensação do Extrato" (Assistente de Implantação de Processos | processo Baixa | Saque do Controle Bancário | etapa Extrato de Caixa do Financeiro).

**Compensação de registros de Extratos de Caixa dos tipos "Saque Transferência" e "Depósito Transferência"**

Utilizando o parâmetro "Compensar saque/depósito de transferência separadamente" (Assistente de Implantação de Processos | processo Baixa | Saques do Controle Bancário | etapa Extrato de Caixa do Financeiro) você pode compensar os extratos de saque transferência e de depósito transferência juntos ou separados.  
 Ao marcar o parâmetro você pode compensar um dos extratos sem o outro ser compensado no mesmo momento.  
 Com o parâmetro desmarcado ao compensar um dos extratos o outro será compensado ao mesmo tempo.
