---
content_hash: 319fa2ae7ee4c49a06e990d50b61da273210d962fb16fc72daf22a238bfc19c1
fetched_at: '2026-06-29T00:09:35.319407+00:00'
page_id: '425459308'
product: rm
source: tdn-rm
title: Dimensões Comerciais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459308
version: 3
---

**Dimensões Comerciais**

---

A Área Comercial é dividida em subgrupos e cada um possui suas tabelas Fatos, conforme descrito abaixo:

* **Administração de Clientes:** Contempla informações das Vendas, da Carteira de Vendas e da Avaliação de Crédito dos clientes, em valores e percentuais.

**1**. Avaliação de Crédito (Tabela Fato HL0): Apresenta informações históricas de limite de crédito dos clientes.

* **Administração de Vendas:** Contempla informações de Faturamento, Devolução de Vendas, Carteira de Vendas, Vendas, Previsão de Vendas e Cotas de Vendas, em valores, quantidades e percentuais.

**1**. Carteira de Vendas (Tabela Fato HL3): Apresenta informações dos pedidos de venda em aberto, armazenando o histórico diário da carteira de pedidos.  
    
 **2**. Devolução de Vendas (Tabela Fato HL6): Apresenta informações relacionadas às devoluções das vendas como valores e quantidades devolvidas, e impostos.  
    
 **3**. Faturamento (Tabela Fato HL2): Apresenta informações relativas às notas fiscais faturadas. Alguns exemplos são quantidades e valores faturados, ICMS, COFINS, comissões e despesas.  
    
 **4**. Vendas (Tabela Fato HL4): Apresenta informações dos pedidos de vendas como quantidades e valores dos pedidos de venda e impostos.  
    
 **5**. Previsão de Vendas (Tabela Fato HL1): Esta tabela Fato não é contemplada na integração com a Linha RM excepcionalmente.  
    
 **6**. Cotas de Vendas (Tabela Fato HL5): Esta tabela não é contemplada na integração com a Linha RM excepcionalmente.  
    
 **7**. Entregas de Vendas (Tabela Fato HL7): Esta tabela não é contemplada na integração com a Linha RM excepcionalmente.

Os Conceitos que serão utilizados para carga das tabelas fatos são:

* Fato - Comercial - Avaliação de Crédito
* Fato - Comercial - Carteira de Vendas
* Fato - Comercial – Vendas
* Fato - Comercial - Devolução de Vendas
* Fato - Comercial - Faturamento
* Fato - Comercial - Cotas de Vendas \***{**}
* Fato - Comercial - Previsão de Vendas \***{**}
* Fato - Comercial - Entregas de Vendas \*\*\*

 - **Não estão contempladas na integração - Linha RM.**  
    
 Os registros nestas tabelas serão incluídos na Stage Area através da execução dos Conceitos importados. Pra isto acontecer conforme demanda do cliente deve-se agendar os Conceitos para serem executados via Jobs. Este procedimento deverá ser configurado para todos os Conceitos.  
    
 Lembrando que a partir da versão 11.40.15 é possível realizar o agendamento nos Conceitos de maneira simultânea, ou seja, está disponível a opção de selecionar todos os Conceitos referentes aos Cadastros Comuns e definir Data, Hora e sua repetição de maneira simultânea. É indicado definir um horário que não tenha usuários utilizando os sistemas da Linha RM e também que não aja conflito com o horário de outras áreas do BI.  
    
 Para isto acontecer é necessário alterar os arquivos de configuração para utilizar o ambiente 3 Camadas. Deve-se adicionar nos arquivos a Tag abaixo:  
 <add key="JobServer3Camadas" value="True" />
