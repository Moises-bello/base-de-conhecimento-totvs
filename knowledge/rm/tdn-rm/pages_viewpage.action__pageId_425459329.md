---
content_hash: e96de4cc0f553febdd7bcd87fa49ac2f02ec4bab391899b0d8f1c567b870dbf5
fetched_at: '2026-06-29T00:09:35.368398+00:00'
page_id: '425459329'
product: rm
source: tdn-rm
title: Dimensões Materiais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459329
version: 3
---

**Dimensões Materiais**

---

A Área Materiais é dividida em subgrupos e cada subgrupo possui suas tabelas fatos, conforme descrito abaixo:

* **Gestão de Compras:** Contempla informações de Compras, Devoluções de Compras, Carteira de Compras e Recebimento de Materiais, em valores, quantidades e percentuais.

**1**. Compras Carteira (Tabela Fato HKQ): Apresenta informações históricas de quantidade e valor das ordens e pedidos de compra que não foram recebidas.  
    
 **2**. Compras (Tabela Fato HKO): Apresenta informações de quantidades e valores relacionados às ordens e pedidos de compras.  
    
 **3**. Devolução de Compras (Tabela Fato HKL): Apresenta informações das quantidades e valores relacionados ao processo de devolução de compras.

* **Desempenho dos Recebimentos:** Contempla informações de Recebimento de Compras, em valores, quantidades e percentuais.

**1**. Recebimento das Compras (Tabela Fato HKM): Apresenta informações relacionadas ao controle de pedidos, estimando em valores e quantidades recebidas no processo de compra.

* **Gestão de Estoque:** Contempla informações de Estoque (Mensal e Diário) e Saldo Diário dos Estoques, em valores, quantidades e percentuais.

**1**. Estoque Diário (Tabela Fato HKS): Apresenta informações de movimentações diárias de entrada e saída de itens no estoque.  
    
 **2**. Estoque Mensal (Tabela Fato HKR): Apresenta informações mensais de entrada, saída e saldo dos itens no estoque.  
    
 **3**. Saldo do Estoque Diário (Tabela Fato HKT): Apresenta informações relacionadas aos saldos dos itens no estoque.  
    
 Os Conceitos que serão utilizados para carga das tabelas fatos são:

* Fato - Materiais - Gestão de Compras - Compras Carteira
* Fato - Materiais - Gestão de Compras - Compras
* Fato - Materiais - Gestão de Compras - Devolução Compras
* Fato - Materiais - Gestão de Compras - Recebimentos Compras
* Fato - Materiais - Gestão de Estoque - Estoque Diário
* Fato - Materiais - Gestão de Estoque - Estoque Mensal
* Fato - Materiais - Gestão de Estoque - Saldo Estoque Diário

Os registros nestas tabelas serão incluídos na Stage Area através da execução dos Conceitos importados. Pra isto acontecer conforme demanda do cliente deve-se agendar os Conceitos para serem executados via Jobs. Este procedimento deverá ser configurado para todos os Conceitos.  
    
 Lembrando que a partir da versão 11.40.15 é possível realizar o agendamento nos Conceitos de maneira simultânea, ou seja, está disponível a opção de selecionar todos os Conceitos referentes aos Cadastros Comuns e definir Data, Hora e sua repetição de maneira simultânea. É indicado definir um horário que não tenha usuários utilizando os sistemas da Linha RM e também que não aja conflito com o horário de outras áreas do BI.  
    
 Para isto acontecer é necessário alterar os arquivos de configuração para utilizar o ambiente 3 Camadas. Deve-se adicionar nos arquivos a Tag abaixo:  
 <add key="JobServer3Camadas" value="True" />
