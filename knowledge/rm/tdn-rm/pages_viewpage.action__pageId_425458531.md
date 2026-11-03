---
content_hash: ff892698589310d2b49082406d86a05a2c6b9b49214d6c589fd9296c2f2ef5dd
fetched_at: '2026-06-29T00:09:30.811757+00:00'
page_id: '425458531'
product: rm
source: tdn-rm
title: Informações Estratégicas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458531
version: 1
---

**Informações Estratégicas**   
A tela Informações estratégicas sobre o cliente exibe informações relativas ao cliente inclusive sobre informações financeiras e produtos adquiridos. Nesta constam vários anexos com informações sobre a situação do cliente: financeira (valores que foram pagos, valores em aberto, valores em atraso, valores faturados, valor mensal), produtos adquiridos, resumo dos atendimentos abertos, projetos entre outros.     
   
As várias informações são apresentadas mediante a SQL fixos dentro do código fonte do sistema, mas podem ser parametrizados para refletir a realidade e necessidade do cliente. O termo "pode ser parametrizado" significa que é possível criar consultas SQL e associar aos respectivos parâmetros de acordo com o retorno das consultas elaboradas (se a consulta retorna os valores que um cliente está devendo então associar ao parâmetro "valores em aberto' e assim por diante).  
   
Os parâmetros disponibilizados o que significa quais informações podem ser customizadas pelo próprio cliente são: valores pagos, valores em aberto, valores em atraso, valores faturados, valor mensal, produtos adquiridos, projetos. Para a elaboração de tais consultas deve-se atentar que as mesmas devem ter obrigatoriamente um parâmetro chamado COLIGADA e outro parâmetro que pode ser CODCFO ou CODCFO\_S (CODCFO indica que os valores retornados são relativos a apenas ao cliente e o CODCFO\_S significa que os valores retornados são relativos ao cliente e ao grupo de empresas ao qual o cliente pertence).     
   
Exemplo:  
   
                SELECT C1, C2, C3   
          FROM T1  
          WHERE T1.CODCOLIGADA = :COLIGADA AND  
                T1.CODCFO = :CODCFO   
   
          SELECT C1, C2, C3  
          FROM T1   
          WHERE T1.CODCOLIGADA = :COLIGADA AND  
                T1.CODCFO IN (:CODCFO\_S)

* Consulta SQL para Valor Faturado (QUERYVALORFATURADO)
* Consulta SQL para Valor Pago (QUERYVALORPAGO)
* Consulta SQL para Valor em Aberto (QUERYVALORABERTO)
* Consulta SQL para Valor em Atraso (QUERYVALORATRASO)
* Consulta SQL para Valor Mensal (QUERYVALORMENSAL)

* Consulta SQL para Produtos (QUERYPRODUTO)
* Consulta SQL para Projeto (QUERYPROJETO)

**Observação**: Caso o usuário não preencha os campos acima, o sistema executará as consultas SQL's que estão fixas no código para carregar as abas Informações Financeiras e Produto do Cliente.
