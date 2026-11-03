---
content_hash: a325f5a28969de68c6b622b4a5eabf4f7d8e76f86092d9611d6c9f96f85ee8d7
fetched_at: '2026-06-29T00:09:35.856538+00:00'
page_id: '425459396'
product: rm
source: tdn-rm
title: Consulta Funcionários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459396
version: 4
---

**Consulta Funcionários**

---

A Integração Consulta Funionários do TOTVS Folha de Pagamento x Gestor AVB (TOOLS) tem como objetivo buscar através de um XML informações como CPF, Matrícula (chapa), Data Limite Admissão, Código Situação e etc, dos funcionários existentes na base de dados. Essa consulta é feita através de um XML enviado pelo TOOLS. Esse XML deverá conter os campos CNPJ (que corresponde o código da coligada no TOTVS Folha de Pagamento), usuário e senha preenchidos obrigatoriamente para executar a consulta. Caso contrário o sistema irá apresentar uma mensagem de que os campos não estão preenchidos ou que as informações estão inválidas. Na tabela abaixo está indicado todos os campos que são utilizados para a consulta funcionário:

|  |  |
| --- | --- |
| **CAMPOS** | **OBRIGATÓRIO** |
| Código Coligada (CNPJ) | SIM |
| CPF (Funcionário) | NÃO |
| Matrícula Funcionário (Chapa) | NÃO |
| Data Limite de Admissão | NÃO |
| Código Situação Funionário | NÃO |
| Quantidade por lote | SIM |
| Usuário | SIM |
| Senha | SIM |

De acordo com a consulta feita o sistema pode retornar 'N' funcionários. Para isso o sistema TOOLS poderá definir um número determinado de lotes por consulta.  
    
 **Exemplo**

*O TOOLS enviou uma consulta de funcionários informando apenas o CNPJ de uma determinada coligada. O sistema retornará mais de dois mil funcionários.* *Para que o travamento ou lentidão do processo não aconteça, o TOOLS poderá definir uma quantidade de funcionários por lote.* *No exemplo suponhamos que ele informou o número 50. Então serão 50 funcionários por lote, ou seja, a consulta irá retornar vários lotes contendo 50 funcionários cada.*
