---
content_hash: c001a80c71142d6e99cee3b9b20c6616d402c8de9eb4c7507db7b783f97e4625
fetched_at: '2026-06-29T00:05:52.842128+00:00'
page_id: '1060235971'
product: rm
source: tdn-rm
title: Troubleshooting Data Sharing
type: documentation
url: https://tdn.totvs.com/display/LRM/Troubleshooting+Data+Sharing
version: 3
---

# Índice

---

2Índice

# Análise de problemas conhecidos

---

Análises a serem feitas de erros e possíveis soluções para problemas específicos sobre a integração Data Sharing.

Conforme situações forem encontradas, elas serão adicionadas nesta documentação.

## Inconsistência nos dados enviados

Caso haja algum tipo de inconsistência nos dados enviados, como discrepância na quantidade, as análises a seguir podem ajudar:

### Query para verificar sumários enviados

sql

Nesta tabela estão armazenados os dados dos sumários enviados ao SmartLink.

Análise da tabela:

* + O BATCHID é o campo identificador que é utilizado como referência tanto no banco de dados quanto na plataforma do SmartLink.
  + Utilizando o BATCHID em conjunto com o RECOURDCOUNT e o SUMMARYSENT (1 para enviado, 0 para não enviado), é possível saber a quantidade de dados enviado por cada *batch*.

### Query para verificar tabelas enviadas

sql

Esta tabela é utilizada como tabela muro do sistema; ou seja, os dados armazenados aqui são cruciais para avaliarmos o que vamos ou não vamos enviar para o SmartLink.

No entanto, exatamente por ser utilizada constantemente, fazemos uma sanitização constante nela. Por este motivo, esta query é um pouco menos eficaz para detectar números.

Análise da tabela:

* + Caso alguma tabela que deveria estar integrando não esteja presente no resultado desta query, duas coisas podem estar acontecendo:
    - ela não está presente nas entidades a serem integradas pelo produto no SmartLink;
    - algum erro na query de execução desta tabela está acontecendo. Estes erros podem ser verificados utilizando o TRACKLOG.
  + Pode-se ter uma ideia de qual BATCHID foi utilizado por último para enviar uma tabela.
