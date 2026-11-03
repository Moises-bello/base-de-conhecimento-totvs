---
content_hash: 7399ab5de662038d20eb515802a0845119605737fd29c433dee4783b40e083f9
fetched_at: '2026-06-29T00:09:18.865731+00:00'
page_id: '421388803'
product: rm
source: tdn-rm
title: Encerramento Período
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388803
version: 34
---

## **01. Visão Geral**

Ao encerrar um período, o sistema irá alterar o seu status para encerrado e atualizar o seu saldo credor/Devedor.  
Para manter a integridade de saldo dos períodos, sabendo que este é atualizado no momento do seu encerramento, o sistema irá fazer algumas consistências antes de Encerrar um período:

## **02. Regras**

### Regras Específicas

* Na utilização do campo Usa Lotes no módulo: Opções | Parâmetros | Gerais/Tabelas | Escrituração - o sistema somente permitirá o encerramento de um período, se os todos os lotes referenciados a este estiverem com Status de Liberado.
* Ao encerrar o período de IRRF da Filial Matriz, todos os períodos deste tributo das outras filiais, com as mesmas datas, inicial e final, serão também encerrados. Isto se o parâmetro "Filial" não estiver marcado através do menu Opções | Parâmetros | Gerais/ Tabelas / Apuração de Tributos - IRRF - Guias de Recolhimento 4/4 - Regras de geração DARF.
* O sistema possibilita cadastrar mais de um tributo do tipo PIS e COFINS e para apuração desses tributos é necessário realizar o cadastro e configurações dentro de [Rotinas Fiscais/Anexo Parâmetros de Rotina](https://tdn.totvs.com/pages/viewpage.action?pageId=842699260).
* Ao encerrar períodos do tipo PIS/COFINS será executado o processo do [Pré-Processamento](https://tdn.totvs.com/pages/viewpage.action?pageId=853282471) automaticamente. Se não houver um  do tipo "EFD Pis Cofins" com data de vigência abrangendo o período sendo encerrado o processo é interrompido com uma mensagem de erro.

### Regras Gerais

* O sistema somente permitirá o encerramento de um período, se todos os períodos anteriores estiverem com Status de **Encerrado**.
* O sistema somente permitirá a reabertura de um período se todos os períodos posteriores estiverem com Status **Aberto**.
* Não será possível alterar o Status do Período na tela de cadastrado, o status será alterado somente quando realizar **Abertura** ou **Encerramento** do Período através dos processos.

***Observação*:**O campo Fim Período somente poderá ser alterado se não existirem lançamentos em datas posteriores a "nova data", ou a data final do Lote (caso utilize lote no sistema) associado ao período for menor ou igual a nova data. Para os tributos que são apurados através de eventos tributários ( PIS, COFINS, CSSL, IRPJ, OUTROS E RET) no encerramento é necessário verificar a existência de Vigência Eventos Tributários para a correta apuração.

## **03. Cálculo para a apuração dos tributos PIS/COFINS**

Para que seja feito o cálculo para a apuração dos tributos PIS/COFINS, é necessário realizar o cadastro e configurações dentro de [Rotinas Fiscais/Anexo Parâmetros de Rotina](https://tdn.totvs.com/pages/viewpage.action?pageId=842699260).

## **04. Consolidação dos valores no encerramento do Período de Apuração**

Para fins gerenciais, o sistema possibilita cadastrar mais de um tributo do tipo PIS e COFINS, neste cenário é necessário que seja configurado dentro do cadastro da [Rotina Fiscal/Anexo Parâmetros da Rotina](https://tdn.totvs.com/pages/viewpage.action?pageId=842699260), qual o tributo principal para que no Encerramento do Período de Apuração, os valores sejam consolidados.

A configuração do tributo principal deve ser realizada conforme abaixo:

* Para apuração do PIS/COFINS é necessário cadastrar dois parâmetros internos, chave e valor, em **Anexo Parâmetros da Rotina**.
* Com o campo "Chave" **APURACAO\_PIS** ou **APURACAO\_COFINS** e o campo "Valor" deverá ser preenchido com o código do tributo que deve ser igual ao Código do Tributo do Período de Apuração.

  Exemplo da Configuração dos Parâmetros de RotinaObservaçãoO campo "Valor" deve ser igual ao Código do Tributo do Período de Apuração que se deseja fazer os Cálculos da Consolidação PIS/COFINS.
