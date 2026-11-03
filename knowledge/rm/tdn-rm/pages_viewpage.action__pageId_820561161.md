---
content_hash: ce6c4c42c12204367db876aef50d05dbad0c2d5034edb92e3597fa7944bcfea9
fetched_at: '2026-06-29T00:11:45.627416+00:00'
page_id: '820561161'
product: rm
source: tdn-rm
title: 1- Parametrização TOTVS Gestão Financeira.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=820561161
version: 4
---

Parametrização do TOTVS Gestão Financeira para utilização do TOTVS Pagamento Digital, geração do QRCode de pagamento no Portal do Aluno, Sessão de caixa e Taxa de Inscrição do Processo Seletivo, realização de baixa dos lançamentos após pagamento, processo de ajuste de transações e criação do extrato de caixa.

Neste passo vamos informar os dados de acesso ao TOTVS Pagamento Instantâneo, para isso acessar:

**Ambiente | Parâmetros | TOTVS Gestão Financeira**

Após avançar o processo selecionar:

**Contas a Receber | TOTVS Pagamento Digital**

Avançar o processo e na próxima tela na guia Credenciais, precisaremos informar os dados de acesso cadastrados no **RaaS**, que nos permite parametrizar as credenciais e dados para baixa e conciliação por Coligada ou Filial. Os cadastros precisam ser os mesmos no **RM** e **RaaS**, por Coligada ou Filial.

No exemplo acima estamos parametrizando o cadastro por Coligada.

Selecionar a Solução de Pagamento TOTVS Pagamento Digital (TPD)

O campo Dias após pagamento para gerar extrato de tarifa: é utilizado para informar que a movimentação Saque manual seja criada com a data do numero de dias informado após a data da baixa do lançamento financeiro criado no processo Ajuste de transações responsável pela baixa dos lançamento. Deixando o valor como 0 a taxa data de criação da taxa será a mesma da baixa do lançamento.

**Tenant** – Informar a Tenant cadastrada no RAAS que geralmente é o nome da instituição

**Usuário** – Informar o usuário cadastrado no RAAS

**Senha** – Informar a senha do usuário cadastrado no RAAS

Após preencher os dados de acesso na guia credenciais. Vamos preencher os dados solicitados na guia Baixa/Conciliação

**Baixa**

**Conta/Caixa**– Ficará inativo e será replicada a conta Caixa informada no campo de conciliação

**Meio de Pagamento** – Informar o Meio de Pagamento cadastrado para identificar os pagamentos realizados via PIX, o parâmetro Tipo Primitivo, **Pagamento Instantâneo (PIX)** marcado.

**Taxa**–  Para criação da operação 'Saque Manual' no extrato de caixa, é necessário informar no campo 'Valor', a taxa contratada junto ao banco prestador de serviço.   
Caso não opte pelo preenchimento, o extrato não é criado no momento da baixa.

OBSERVAÇÃO: Este campo é de caráter informativo, pois não há vinculo com as API's bancárias para fins de validações. Neste exemplo, não iremos preencher o campo, cenário compatível com os bancos que realizam a cobrança das taxas pelo modelo de bilhetagem, ou seja, o valor referente às taxas é cobrado mensalmente compreendendo determinado período de transações.

**Conta Caixa** – Conta Caixa (integrada com Banco) que receberá os valores repassados pelo Banco Original, a mesma conta apontada pelo representante legal. 

**Evento Contábil** – Evento Contábil utilizado quando o default contábil no extrato extrato de caixa seja contábil e o campo taxa estiver preenchido.

O link abaixo com documentação criada com exemplo de evento contábil
