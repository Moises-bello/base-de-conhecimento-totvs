---
content_hash: f52701aceb94ac5f11067a1293223237cebc9cb2379336e9001200f55f35c434
fetched_at: '2026-06-29T00:10:45.891219+00:00'
page_id: '553346911'
product: rm
source: tdn-rm
title: DT- Ajuste Dependente IRRF
type: documentation
url: https://tdn.totvs.com/display/LRM/DT-+Ajuste+Dependente+IRRF
version: 1
---

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | RH |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Ajuste Dependente IRRF |
| **Situação/Requisito:** | Inconsistência na atualização de dependente de IRRF através do processo de liberação de competência, ocorrendo somente quando o dependente tem o grau de parentesco "1-Filho Valido" ou "3-Menor Pobre". Para estes casos, o sistema desmarcou a incidência de IRRF no Cadastro do Dependente, mesmo quando a idade do dependente era inferior a 22 anos ou inferior a 25 anos e era universitário. |
| **Solução/Implementação:** | Criado o processo de Ajuste de Dependentes IRRF. Este processo irá fazer a comparação entre: -o valor do campo "Nro. Dependente IRRF" da competência anterior (Funcionários | Anexo | Históricos de Dependentes) -a quantidade de dependentes que possuem o grau de parentesco igual "1-Filho Valido" e "M-Menor Pobre". (Funcionários | Anexo | Dependentes) -a quantidade de dependentes que NÃO incide IRRF, que possuem o grau de parentesco igual "1-Filho Valido" e "M-Menor Pobre" e a idade do dependente é inferior a 22 anos ou inferior a 25 anos e é universitário.  Caso as três quantidades obtidas acima sejam iguais, o sistema irá realizar de forma automática a atualização (marcar a incidência de IRRF em todos os dependentes que deveriam estar incidindo). |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | <https://tdn.totvs.com.br/display/LRM/Ajuste+Dependente+IRRF> |
| **Pacote:** | N/A |
