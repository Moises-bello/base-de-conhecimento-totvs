---
content_hash: a034e4f74563564d2a10920059e7a32e51767cc582f763d40caf637941de20ba
fetched_at: '2026-06-29T00:09:35.316257+00:00'
page_id: '425459307'
product: rm
source: tdn-rm
title: Dimensões Financeiras
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459307
version: 2
---

**Dimensões Financeiras**

---

A Área Finanças é dividida em subgrupos e cada subgrupo possui suas tabelas Fatos, conforme descrito abaixo:

* **Gestão de Pagamentos:** Contempla informações da Carteira, dos Pagamentos, dos Vencimentos e das Emissões das Contas a Pagar, em valores.

**1**. Contas a Pagar – Carteira (Tabela Fato HLK): Apresenta informações históricas dos títulos a pagar que estão em aberto.  
    
 **2**. Contas a Pagar – Pagamento (Tabela Fato HLI): Apresenta informações dos títulos a pagar que foram parcialmente ou totalmente pagos.  
    
 **3**. Contas a Pagar – Vencimento (Tabela Fato HLD): Apresenta informações dos títulos a pagar que foram emitidos.

* **Administração de Conta a Receber:** Contempla informações da Carteira, dos Recebimentos Pagamentos, dos Vencimentos e das Emissões das Contas a Receber (CR), além de informações referentes à Avaliação de Crédito dos clientes, em valores.

**1**. Contas a Receber – Carteira (Tabela Fato HLL): Apresenta informações históricas dos títulos a receber que estão em aberto.  
    
 **2**. Contas a Receber – Recebimento (Tabela Fato HLJ): Apresenta informações dos títulos a receber que foram parcialmente ou totalmente recebidos.  
    
 **3**. Contas a Receber – Vencimento (Tabela Fato HLE): Apresenta informações dos títulos a receber que foram emitidos.

* **Gestão do Fluxo Financeiro:** Contempla informações de Fluxo de Caixa e Tesouraria (Realizado e Previsto), em valores e percentuais.

**1**. Fluxo de Caixa Previsto (Tabela Fato HLH): Apresenta informações de entrada, saída e saldo do fluxo de caixa previsto.  
    
 **2**. Fluxo de Caixa Realizado (Tabela Fato HL8): Apresenta informações de entrada, saída e saldo do fluxo de caixa realizado.

Os Conceitos que serão utilizados para carga das tabelas fatos são:

* Fato - Finanças - Contas a Pagar Carteira
* Fato - Finanças - Contas a Pagar Pagamento
* Fato - Finanças - Contas a Pagar Vencimento
* Fato - Finanças - Contas a Receber Carteira
* Fato - Finanças - Contas a Receber Recebimento
* Fato - Finanças - Contas a Receber Vencimento
* Fato - Finanças - Fluxo de Caixa - Previsão
* Fato - Finanças - Fluxo de Caixa - Realizado

Os registros nestas tabelas serão incluídos na Stage Area através da execução dos Conceitos importados. Pra isto acontecer conforme demanda do cliente deve-se agendar os Conceitos para serem executados via Jobs. Este procedimento deverá ser configurado para todos os Conceitos.  
    
 Lembrando que a partir da versão 11.40.15 é possível realizar o agendamento nos Conceitos de maneira simultânea, ou seja, está disponível a opção de selecionar todos os Conceitos referentes aos Cadastros Comuns e definir Data, Hora e sua repetição de maneira simultânea. É indicado definir um horário que não tenha usuários utilizando os sistemas da Linha RM e também que não aja conflito com o horário de outras áreas do BI.  
    
 Para isto acontecer é necessário alterar os arquivos de configuração para utilizar o ambiente 3 Camadas. Deve-se adicionar nos arquivos a Tag abaixo:  
 <add key="JobServer3Camadas" value="True" />
