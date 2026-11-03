---
content_hash: 95047b5cb2e4999f1981f0b05c2cc4d9d0d9d6655a2a6c7070a92722ab4a4316
fetched_at: '2026-06-29T00:05:51.204010+00:00'
page_id: '1049382611'
product: rm
source: tdn-rm
title: 8 - Baixa do Boleto Híbrido e Consulta do Extrato de Caixa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1049382611
version: 6
---

Após a **baixa do lançamento/boleto**, o sistema executa o **Job "Ajustar Transações"**, responsável por atualizar o status da transação.

Quando esse processo ocorre:

* O status da transação é alterado de **Pagamento Solicitado** para **Pagamento Concluído**
* É criado automaticamente um **Extrato de Caixa**, com a **operação de depósito**, referente à baixa do boleto

Acesse o menu:

**Contas a Pagar / Receber → Boleto Híbrido → Transações**

Utilize os **filtros da tela** para localizar a transação desejada.

Ao localizar a transação, verifique o campo **Status**.

Quando o status estiver como **Pagamento Concluído**, significa que:

* A **baixa bancária do boleto foi realizada**
* O **lançamento foi baixado**
* O sistema **gerou automaticamente o extrato de caixa**

Para facilitar a identificação do **Extrato de Caixa gerado**, será necessário criar uma **Consulta SQL** que exibirá:

* **Id do Lançamento**
* **Id do Extrato de Caixa**
* **Id do Boleto**

Na tela de **Transações**, acesse:

**Anexos → Consultas SQL → Inserir Consulta SQL**

Clique em **Avançar**

Clique no botão **(...)** no campo **Consulta SQL**.

Em seguida, clique no ícone **+** para criar uma nova consulta.

Informe:

* **Código** da consulta
* **Título** da consulta

Depois copie e cole a consulta abaixo no campo destacado.

SELECT  FLANBAIXA.IDLAN 'Id. Lançamento',   
              FLANBAIXA.IDXCX 'Id. Extrato',   
              FBOLETO.IDBOLETO 'Id. Boleto'  
FROM FINTEGRACAOCARTAO (NOLOCK)   
JOIN FBOLETO (NOLOCK)   
        ON (FINTEGRACAOCARTAO.CODCOLIGADA = FBOLETO.CODCOLIGADA   
        AND FINTEGRACAOCARTAO.IDBOLETO = FBOLETO.IDBOLETO)  
  
JOIN FLANBOLETOBAIXA (NOLOCK)   
        ON (FBOLETO.CODCOLIGADA = FLANBOLETOBAIXA.CODCOLIGADA   
        AND FBOLETO.IDBOLETO = FLANBOLETOBAIXA.IDBOLETO)  
  
JOIN FLANBAIXA (NOLOCK)   
       ON (FLANBOLETOBAIXA.CODCOLIGADA = FLANBAIXA.CODCOLIGADA   
       AND FLANBOLETOBAIXA.IDLAN = FLANBAIXA.IDLAN   
       AND FLANBOLETOBAIXA.IDBAIXA = FLANBAIXA.IDBAIXA)  
  
WHERE FINTEGRACAOCARTAO.IDTRANSACAO = :IDTRANSACAO  
       AND FLANBAIXA.STATUS = 0

Salvar → OK

Clique em **Avançar**

No campo **Valor**, selecione **[IDTRANSACAO]**.

Selecione a opção **Todos** e clique em **Avançar**.

Cliquem em **Executar**

Cliquem em **Fechar**

Acesse novamente:

**Anexos → Consulta SQL**

Selecione a **consulta criada**.

A tela exibirá as informações retornadas pela consulta, incluindo o **Id do Extrato de Caixa**.

Com o **Id do Extrato** obtido na consulta, acesse:

**Movimentações Bancárias → Extrato de Caixa**

Informe o **Id do Extrato** no filtro de pesquisa.

O extrato correspondente será exibido.

Abra o extrato localizado e verifique as informações geradas no momento da baixa do boleto.

Confirme principalmente:

* Operação registrada (**Depósito na baixa**)
* Valor do lançamento
* Conta bancária utilizada
* Data da criação
* Data da compensação

Após esse processo, será possível:

* Confirmar a **baixa do boleto**
* Identificar o **lançamento associado**
* Localizar o **extrato de caixa gerado automaticamente pelo sistema**
