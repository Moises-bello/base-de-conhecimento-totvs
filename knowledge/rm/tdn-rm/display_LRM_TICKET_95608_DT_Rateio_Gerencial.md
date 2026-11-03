---
content_hash: 625f8e19b2ee9d7b7b2b5bd1bf680c5e68c2dfd5563291da48b6c047b511dbce
fetched_at: '2026-06-29T00:08:23.376550+00:00'
page_id: '270082472'
product: rm
source: tdn-rm
title: TICKET_95608_DT_Rateio_Gerencial
type: documentation
url: https://tdn.totvs.com/display/LRM/TICKET_95608_DT_Rateio_Gerencial
version: 112
---

# Conversor

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Educacional.* |
| **Módulo:** | *Totvs Gestão Contábil.* |
| **Função:** | *Conversor.* |
| **Situação/Requisito:** | *Ao realizar a conversão da Base de Dados (versão 12.1.12) o sistema apresenta o seguinte log de erro:ALTER TABLE CHISTRATEIOLAN ADD CONSTRAINT PKCHISTRATEIOLAN PRIMARY KEY (CODCOLIGADA, IDHIST)The CREATE UNIQUE INDEX statement terminated because a duplicate key was found for the object name 'dbo.CHISTRATEIOLAN' and the index name 'PKCHISTRATEIOLAN'. The duplicate key value is (1, 3).Conforme análise realizada, foi possível verificar que a PK da tabela CHISTRATEIOLAN possuía - na versão 11.82 - quatro campos (CODCOLIGADA, IDHIST, CODLOTE, IDLANCAMENTO), possibilitando assim, que os valores dos campos CODCOLIGADA e IDHIST fossem informados mais de uma vez.Com a inclusão da PK (CODCOLIGADA, IDHIST) foi gerada a violação da PK.Segundo o desenvolvimento do RM Saldus a alteração foi realizada, pois o sistema permitirá valores nulos para o campo IDLANCAMENTO em determinadas situação.Acredito que será necessário utilizar outro campo para receber a informação do campo IDLANCAMENTO, possibilitando a criação da PK com quatro campos, consequentemente não será apresentada a inconsistência durante a conversão.Obs.: Tabela preenchida pelo processo de Mapa de Rateio do RM Saldus; Log e registros correspondentes anexado no chamado.BENEFÍCIOS ALCANÇADOS: Ao realizar a conversão da Base de Dados, a inconsistência citada não será apresentada.* |
| **Solução/Implementação:** | \* Implementação da nova PK no conversor da 12.1.1 e da 12.1.15  \* Implementar no sistema a segurança defensiva que verifica se a base contem ou não a nova PK ao salvar o histórico do mapa de rateio*.* |
| **Conversores e Parâmetros:** | *conversor 12.1.15.* |
| **Tickets relacionados:** | *N/A* |
| **Requisito (informe o requisito relacionado):** | N/A |

divs
