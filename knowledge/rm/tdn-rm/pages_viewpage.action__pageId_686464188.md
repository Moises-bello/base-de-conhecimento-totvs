---
content_hash: f3e9e63b7eabc33e737ef3691834c770a83a7885746d523cd22cd662d81392b4
fetched_at: '2026-06-29T00:11:20.502422+00:00'
page_id: '686464188'
product: rm
source: tdn-rm
title: 1- Parametrização TOTVS Gestão Financeira
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=686464188
version: 13
---

false

Parametrização do TOTVS Gestão Financeira para utilização do TOTVS Pagamento Instantâneo, geração do QRCode de pagamento no Portal do Aluno, Sessão de caixa e Taxa de Inscrição do Processo Seletivo, realização de baixa dos lançamentos após pagamento, processo de ajuste de transações e conciliação do extrato de caixa.

Neste passo vamos informar os dados de acesso ao TOTVS Pagamento Instantâneo, para isso acessar:

**Ambiente | Parâmetros | TOTVS Gestão Financeira**

Após avançar o processo selecionar:

**Contas a Receber | TOTVS Pagamento Digital**

Avançar o processo e na próxima tela na guia Crendenciais, precisaremos informar os dados de acesso cadastrados no **RAAS**, que nos permite parametrizar as credenciais e dados para baixa e conciliação por Coligada ou Filial. Os cadastros precisam ser os mesmos no **RM** e **RAAS**, por Coligada ou Filial.

falseDados de Acesso no RASS

No exemplo acima estamos parametrizando o cadastro por Coligada.

Selecionar a Solução de Pagamento TOTVS Pagamento Instantâneo (TPI)

**Tenant** – Informar a Tenant cadastrada no RAAS que geralmente é o nome da instituição

**Usuário** – Informar o usuário cadastrado no RAAS

**Senha** – Informar a senha do usuário cadastrado no RAAS

Após preencher os dados de acesso na guia credenciais. Vamos preencher os dados solicitados na guia Baixa/Conciliação

**Baixa**

**Conta/Caixa** – Informar a Conta Caixa criada para simular a Conta Transitória e geração de extrato de caixa. 

**Conta caixa não precisa ter vínculos****bancários.**

**Meio de Pagamento** – Informar o Meio de Pagamento cadastrado para identificar os pagamentos realizados via PIX, o parâmetro Tipo Primitivo, **Pagamento Instantâneo (PIX)** marcado.

**Taxa** – A parametrização permite somente a configuração por valor, desconsiderar o parâmetro Percentual, e informar o valor que será descontado sobre cada transação aprovada.

**Conciliação**

**Conta Caixa** – Conta Caixa (integrada com Banco) que receberá os valores repassados pelo Banco Original, a mesma conta apontada pelo representante legal. 

**Evento Contábil** – Evento Contábil utilizado para conciliação do Extrato de Caixa, caso a instituição tenha um evento contábil parametrizado para composição do Extrato de Caixa.

O link abaixo com documentação criada com exemplo de evento contábil
