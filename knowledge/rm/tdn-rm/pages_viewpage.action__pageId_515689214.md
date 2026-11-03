---
content_hash: 23f8465532f782cd0b28a85bc517e6661240ee266bd1d4b5be01fe114c4ef340
fetched_at: '2026-06-29T00:10:26.973136+00:00'
page_id: '515689214'
product: rm
source: tdn-rm
title: Alteração no mecanismo de execução de relatórios .Net
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=515689214
version: 55
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       A partir da versão 12.1.23 implementamos uma melhoria na execução de relatórios do RM Reports que tende a evitar que relatórios possam gerar o que chamamos de "produto cartesiano". Esta melhoria poderá acarretar inconsistências em relatórios quando houverem bandas com mais de uma tabela e o relacionamento entre seus campos estiverem incorretos.

# Detalhes da melhoria:

---

       Esta alteração obtém ganho de performance na execução dos relatórios. Explicaremos os cenários antes e pós alteração.

falseExemplosExemplo 1Cenário Anterior e Pós MelhoriaCenário Anterior e Pós MelhoriaEstruturaAnteriorEstruturaAnteriorBandas do RelatórioBandas do Relatório

No exemplo do cenário anterior utilizaremos a seguinte estrutura no relatório;

1) - Banda pai (Detalhe1) = Ligada na tabela PFUNC

1.1) - Banda filha (SubDetalhe1)= Ligada na tabela PFDEPEND

EstruturaAnteriorControles do RelatórioControles do Relatório

Em cada banda utilizamos os seguintes controles (no exemplo são utilizados controles de campo da base);

1) - Banda pai:

[PFUNC.CODCOLIGADA, PFUNC.CHAPA, PFUNC.SALARIO e PPESSOA.CPF]

false

 Neste exemplo temos um controle da tabela principal ligado a outro controle da tabela secundária (PPESSOA.CPF).

1.1) - Banda filha:

[PFDEPEND.CODCOLIGADA e PFDEPENDE.NOME]

EstruturaAnteriorFiltros do RelatórioFiltros do Relatório

Filtro do relatório utilizados na banda pai do relatório.

1) - Banda pai: PFUNC.CODCOLIGADA = 1

AND PPESSOA.CPF = '0027515458'

false

 Neste caso temos uma parte do filtro ligado a tabela secundária da banda pai.

EstruturaAnteriorMecanismo de Execução AnteriorMecanismo de Execução Anterior

Quando o relatório é executado, o mecanismo de execução vai gerar duas sentenças sql’s dinamicamente baseadas nas configurações das bandas e controles.

Nesse exemplo serão geradas duas sentenças sql’s:

1. A) - Primeira sentença: relacionada a banda pai;

SELECT PFUNC.CODCOLIGADA,  
               PFUNC.CHAPA,  
               PFUNC.SALARIO,  
               PPESSOA.CPF  
FROM PFUNC  
LEFT OUTER JOIN PPESSOA (NOLOCK) ON (PFUNC.CODPESSOA = PPESSOA.CODIGO)  
WHERE PFUNC.CODCOLIGADA = 1  
      AND PPESSOA.CPF = '0015154515'

false

  Na sentença acima, o mecanismo adiciona uma clausula (*Left Outer Join*) para tabela PPESSOA. Isso ocorre devido ao controle "CPF" existente na banda pai pois o mesmo não existe na tabela principal da banda "PFUNC".

1. B) - Segunda sentença: relacionada a banda filha:

SELECT PFDEPEND.CODCOLIGADA,  
PFDEPENDE.NOME  
FROM PFDEPEND  
INNER JOIN PFUNC (NOLOCK) ON (PFUNC.CODCOLIGADA = PFDEPEND.CODCOLIGADA  
                                                    AND PFUNC.CHAPA = PFDEPEND.CHAPA)  
WHERE PFUNC.CODCOLIGADA = 1

false

  Perceba que a query acima retornará todos os dependentes de todos os funcionários da Coligada 1. Nesse caso, teremos **considerado consumo de memória e performance**.

EstruturaAnteriorMecanismo de Execução Pós AlteraçãoMecanismo de Execução Pós Alteração

Primeira sentença: Relacionada a banda pai;

SELECT PFUNC.CODCOLIGADA,  
               PFUNC.CHAPA,  
               PFUNC.SALARIO,  
               PPESSOA.CPF  
FROM PFUNC  
LEFT OUTER JOIN PPESSOA (NOLOCK) ON (PFUNC.CODPESSOA = PPESSOA.CODIGO)  
WHERE PFUNC.CODCOLIGADA = 1  
      AND PPESSOA.CPF = '0015154515'

false

  Nada muda em relação à query executada atualmente.

Segunda sentença: Relacionada a banda filha;

SELECT PFDEPEND.CODCOLIGADA,  
               PFDEPENDE.NOME  
FROM PFDEPEND  
INNER JOIN PFUNC (NOLOCK) ON (PFUNC.CODCOLIGADA = PFDEPEND.CODCOLIGADA  
                                                    AND PFUNC.CHAPA = PFDEPEND.CHAPA)  
LEFT OUTER JOIN PPESSOA (NOLOCK) ON (PFUNC.CODCOLIGADA = PPESSOA.CODCOLIGADA  
                                                                     AND PFUNC.CODPESSOA = PPESSOA.CODIGO)  
WHERE PFUNC.CODCOLIGADA = 1  
      AND PPESSOA.CPF = '0015154515'

false

  Nesta execução, a query de Dependentes retornará somente dependentes ligados ao Funcionário com CPF "0015154515"

Em resumo com a passagem da clausula "LEFT OUTER JOIN PPESSOA" da query ligada a banda pai para a query ligada a banda filha, somente os dependentes que participam da listagem do relatório serão recuperados da base. ***Isso melhorará consideravelmente a performance e memória do Host***.  

       Depois do ajuste, percebermos um cenário que poderá trazer dados desnecessários no relatório, ficando a sensação de inconsistência no RM Reports.

falseExemplosExemplo 2Relatórios mapeados depois do ajusteRelatórios após o ajusteDepoisdaAlteracaoDepoisdaAlteracaoBandas do RelatórioBandas do Relatório

No exemplo utilizaremos a seguinte estrutura no relatório;

1) - Banda pai (Detalhe1) = Ligada na tabela "PFUNC"

1.1) Banda filha (SubDetalhe1)= Ligada na tabela "PFDEPEND"

DepoisdaAlteracaoControles do RelatórioControles do Relatório

Em cada banda contem os seguintes controles (utilizados controles de campo da base);

1) - Banda pai:   
[PFUNC.CODCOLIGADA, PFUNC.CHAPA, PFUNC.SALARIO, ABATFUN.DATA]

false

 Neste exemplo temos um controle da tabela principal ligado a outro controle da tabela secundária (ABATFUN.DATA).

1.1) - Banda filha: [PFDEPEND.CODCOLIGADA, PFDEPENDE.NOME]

DepoisdaAlteracaoMecanismo de Execução ErrôneaMecanismo de Execução Errônea

Quando o relatório é executado, o mecanismo de execução vai gerar duas sentenças sql’s dinamicamente baseadas nas configurações das bandas e controles. Nesse caso serão geradas duas sentenças sql.

Primeira sentença: Relacionada a banda pai;

SELECT PFUNC.CODCOLIGADA,  
               PFUNC.CHAPA,  
               PFUNC.SALARIO,  
               ABATFUN.DATA  
FROM PFUNC  
LEFT OUTER JOIN ABATFUN (NOLOCK) ON (PFUNC.CODCOLIGADA = ABATFUN.CODCOLIGADA  
                                                                   AND PFUNC.CHAPA = ABATFUN.CHAPA)  
WHERE PFUNC.CODCOLIGADA = 1  
      AND ABATFUN.DATA < :DATAATUAL

false

 Nada muda em relação à query que será executada depois da melhoria.

Segunda sentença: Relacionada a banda filha;

SELECT PFDEPEND.CODCOLIGADA,  
               PFDEPENDE.NOME  
FROM PFDEPEND  
INNER JOIN PFUNC (NOLOCK) ON (PFUNC.CODCOLIGADA = PFDEPEND.CODCOLIGADA  
                                                    AND PFUNC.CHAPA = PFDEPEND.CHAPA)  
LEFT OUTER JOIN ABATFUN (NOLOCK) ON (PFUNC.CODCOLIGADA = ABATFUN.CODCOLIGADA  
                                                                    AND PFUNC.CHAPA = ABATFUN.CHAPA)  
WHERE PFUNC.CODCOLIGADA = 1  
      AND ABATFUN.DATA < :DATAATUAL

---

Neste cenário, a primeira sql, ao ser executada, retornará dados repetidos para o funcionário, visto que, existirá várias batidas para um único funcionário. Isso gera o que chamamos de "***produto cartesiano***". A query de dependentes retornará os dependentes ligados ao funcionário que possua batidas < que "DATAATUAL", *gerando também, produto cartesiano para os dependentes*.Sendo assim, ao gerar o relatório, na banda de dependentes, aparecerá vários dependentes repetidos de acordo com as batidas de um determinado funcionário.

---

---

---

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.23 ou superiores

false

**Processo:** Execução de Relatórios

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
