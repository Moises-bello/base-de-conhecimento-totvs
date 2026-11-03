---
content_hash: 5fefe1ea948c9cb760f33e3d510ad0e5af3b9f37071e298232aa1da777405736
fetched_at: '2026-06-29T00:09:16.333759+00:00'
page_id: '421385516'
product: rm
source: tdn-rm
title: Tornar Flexível e Customizável os dados de Apropriação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385516
version: 4
---

---

Essa funcionalidade foi implementada para possibilitar a definição de uma Consulta SQL para definir os valores do Cronograma Apropriado, que também terá seus dados considerados nos relatórios periódicos. (Histograma e Cronograma) Essa consulta será definida nos Parâmetros do Projeto - Cronograma - Gerais - Consulta SQL para Cronograma Apropriado e Relatório Periódico. Para que os dados de apropriação sejam exibidos de forma correta, é necessário que a consulta siga o seguinte padrão:

Para a consulta que irá retornar o cronograma é necessário que ela tenha obrigatoriamente as colunas: **(NUMPERIODO, MOEDA, VALOR)** e os parâmetros obrigatórios, somente: **(CODCOLIGADA, IDPRJ, IDTRF).**

Para a consulta que irá retornar os dados do relatório periódico é necessário que ela tenha obrigatoriamente as colunas: **(MOEDA, VALOR, DATAAPROPRIACAO, IDTRF, CODTRF, TIPOPLANILHA, IDCENARIO, PRECOUNITARIO, QUANTIDADE, IDISM)** e os parâmetros obrigatórios, somente **(CODCOLIGADA, IDPRJ).**

Exemplo: Definir nos parâmetros citados acima, a sentença SQL exemplo abaixo para Cronograma Apropriado: SELECT    (ROW\_NUMBER() OVER(ORDER BY VALOR)) AS NUMPERIODO, (MTAREFA.VALOR+(ROW\_NUMBER() OVER(ORDER BY VALOR)) \* 0.71) AS VALOR, MISMAPROP.MOEDA   FROM MISMAPROP (NOLOCK), MTAREFA (NOLOCK)  WHERE    (MISMAPROP.CODCOLIGADA=MTAREFA.CODCOLIGADA)   AND (MISMAPROP.IDPRJ=MTAREFA.IDPRJ)   AND (MISMAPROP.IDTRF=MTAREFA.IDTRF)   AND (MISMAPROP.CODCOLIGADA = :idColigada)   AND (MISMAPROP.IDPRJ = :idPrj)

**1) Colunas obrigatórias: NUMPERIODO, MOEDA E VALOR.**

**2) Parâmetros obrigatórios: CODCOLIGADA, IDPRJ, CODTRF, IDCENARIO, TIPOPLANILHA (necessariamente nesta ordem).**

**3) Obrigatório ordenação ORDER BY IDPERIODO**

Definir nos parâmetros citados acima, a sentença SQL exemplo abaixo para Relatório Periódico: SELECT    MISMAPROP.DATAAPROPRIACAO , MISMAPROP.MOEDA, MISMAPROP.IDISM   , MTAREFA.CODTRF,MTAREFA.IDTRF   , (MTAREFA.VALOR+(ROW\_NUMBER() OVER(ORDER BY VALOR)) \* 0.71) AS VALOR   , MTAREFA.TIPOPLANILHA, MTAREFA.IDCENARIO   , MISMAPROP.PRECOUNITARIO , MISMAPROP.QUANTIDADE  FROM MISMAPROP (NOLOCK), MTAREFA (NOLOCK)  WHERE    (MISMAPROP.CODCOLIGADA=MTAREFA.CODCOLIGADA)   AND (MISMAPROP.IDPRJ=MTAREFA.IDPRJ)   AND (MISMAPROP.IDTRF=MTAREFA.IDTRF)   AND (MISMAPROP.CODCOLIGADA = :codColigada)   AND (MISMAPROP.IDPRJ = :idPrj)

**1) Colunas obrigatórias: IDISM, PRECOUNITARIO, QUANTIDADE, DATAAPROPRIACAO, MOEDA, CODTRF, TIPOPLANILHA, IDCENARIO E VALOR.**

**2) Parâmetros obrigatórios: CODCOLIGADA, IDPRJ (necessariamente nesta ordem).**

---
