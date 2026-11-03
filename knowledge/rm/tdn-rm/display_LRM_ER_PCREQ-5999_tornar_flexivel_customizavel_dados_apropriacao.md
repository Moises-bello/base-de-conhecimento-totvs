---
content_hash: f7a5ac1ef3d81f0032e15d57b0a362767159144a3baddfbe3b8ba660afbe481c
fetched_at: '2026-06-29T00:06:00.450824+00:00'
page_id: '196806979'
product: rm
source: tdn-rm
title: ER_PCREQ-5999_tornar_flexivel_customizavel_dados_apropriacao
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-5999_tornar_flexivel_customizavel_dados_apropriacao
version: 91
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | Totvs Gestão de Obras e Projetos |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | R\_C&P\_TOP007 | **IRM1** | PCREQ-5477 |
| **Requisito1** | PCREQ-5999 | **Subtarefa1** | PDR\_CP\_TOP007-1275 |
| **Chamado2** | - | | |
| **Release de Entrega Planejada** | 12.1.8 | **Réplica** | não |
| **País** | (x) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | |  |  |  | | --- | --- | --- | | 1 | Projetos | <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.Projetos.aspx> | | 2 | Cronograma | <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.Cronograma.aspx> | | 4 | Consulta SQL para Dados de Apropriação | $/RM/Documentos/Prj-Projetos/\_versao1200/Consulta SQL para o Cronograma Apropriado.doc | |  |  |  | | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

* Possibilitar  que os dados de apropriação sejam exibidos através de uma consulta SQL personalizada.

## Definição da Regra de Negócio

## 

## **Consulta SQL Personalizada para Dados de Apropriação**

* Serão criados dois campos de inclusão de consulta personalizada para os dados de apropriação. O primeiro será destinado a geração do cronograma apropriado e o segundo para a geração dos relatórios periódicos (cronograma e histograma).
* Se a consulta do relatório for informada, ao abrir a tela de relatório periódico e marcar o checkbox ‘Apropriado’, (para evidenciar que a consulta será gerada a partir da consulta personalizada), será adicionado um terceiro checkbox ‘Consulta personalizada’ que aparecerá marcado, e os outros dois ‘RM Solum e RM Nucleus’ serão desabilitados.
* Para estes novos campos de inclusão da consulta personalizada, será emitido um aviso no sentido de conscientizar que é possível a personalização, porém o ideal é que seja usado os dados de apropriação que o sistema disponibiliza.
* Relatórios (fornecidos pelo produto) de apropriação baseados no gerador não irão olhar a consulta personalizada.

## 

## **Parâmetro**

* A consulta SQL será definida nos Parâmetros de Projeto | Cronograma | Gerais | Consulta SQL Personalizada para Dados de Apropriação, conforme ilustra o protótipo 01.

## **REGRA:**

* Para que os dados de apropriação sejam exibidos de forma correta, é necessário que a consulta siga o seguinte padrão:  
    
  + Para a consulta que irá retornar o cronograma é necessário que ela tenha obrigatoriamente as colunas   
    (NUMPERIODO, MOEDA, VALOR) e os parâmetros obrigatórios (CODCOLIGADA, IDPRJ, CODTRF, IDCENARIO, TIPOPLANILHA ) nesta ordem.
  + Para a consulta que irá retornar os dados do relatório periódico é necessário que ela tenha obrigatoriamente as colunas   
    (IDISM, PRECOUNITARIO, QUANTIDADE, DATAAPROPRIACAO, MOEDA, CODTRF, TIPOPLANILHA, IDCENARIO, VALOR)   
    e os parâmetros obrigatórios (CODCOLIGADA, IDPRJ) nesta ordem.

## EXEMPLO:

 

**SELECT**

**/\*(coluna obrigatória para ambos) \*/** MOEDA

**/\* (coluna obrigatória para ambos) \*/**,**SUM**(VALOR) VALOR 

**/\* (coluna obrigatória  para cronograma apropriado) \*/**, APROP.NUMPERIODO  

**/\* (coluna obrigatória para relatório)** **\*/**, APROP.DATAINICIOPERIODO **AS** DATAAPROPRIACAO 

**/\* (coluna obrigatória para relatório) \*/**, APROP.IDISM, APROP.PRECOUNITARIO, APROP.QUANTIDADE 

**/\* (coluna obrigatória para relatório)** **\*/**, APROP.CODTRF, APROP.IDCENARIO, APROP.TIPOPLANILHA 

**FROM** 

(**SELECT**P.IDPERIODO **AS** NUMPERIODO, 

              I.MOEDA,

              P.DTINICIO DATAINICIOPERIODO

              ,I.IDISM, I.PRECOUNITARIO, I.QUANTIDADE

              ,MTRF.CODTRF ,MTRF.IDCENARIO ,MTRF.TIPOPLANILHA

              ,(I.QUANTIDADE \* I.PRECOUNITARIO \* (**CASE** I.MOEDA **when** PR.valorstr **then** 1 **else** (fator / 10000) **end**)) **AS** VALOR 

      **FROM** MTAREFA **MTRF** (**NOLOCK**), MISMAPROP **I** (**NOLOCK**)  

      **JOIN** MPERIODO **P** (**NOLOCK**) **ON** I.CODCOLIGADA = P.CODCOLIGADA  **AND** I.IDPRJ = P.IDPRJ

      **LEFT** **JOIN** (**SELECT** GCOTACAO.\*  

                  **FROM** GCOTACAO 

                  **JOIN** ( **SELECT** SIMBOLO, **MAX**(DATA) **AS** DATA 

                          **FROM** GCOTACAO 

                          **WHERE** DATA <= (**SELECT** VALORDATA 

                                          **FROM** MPARAMETRO 

                                          **WHERE** PARAMETRO = 'DATABASECONVERSAO' 

                                          **AND** CODCOLIGADA = :codColigada 

                                          **AND** IDPRJ = :idPrj) 

                          **GROUP BY** SIMBOLO) MAXCOT 

                  **ON** GCOTACAO.SIMBOLO = MAXCOT.SIMBOLO **AND** GCOTACAO.DATA = MAXCOT.DATA) C 

                  **ON** I.MOEDA = C.SIMBOLO  

      **JOIN** MPARAMETRO PR  **ON** PR.CODCOLIGADA = I.CODCOLIGADA **AND** PR.IDPRJ = I.IDPRJ 

      **WHERE** PR.PARAMETRO = 'MOEDASECUNDARIA'  

          **AND** MTRF.CODCOLIGADA=I.CODCOLIGADA  

          **AND** MTRF.IDPRJ=I.IDPRJ  

          **AND** MTRF.IDTRF=I.IDTRF  

          **AND** I.DATAAPROPRIACAO **BETWEEN** P.DTINICIO **AND** P.DTFIM  

          **/\* (obrigatório para ambos) \*/** **AND**  MTRF.CODCOLIGADA = :codColigada

          **/\*** **(obrigatório para ambos) \*/** **AND**  MTRF.IDPRJ = :idPrj  

****/\***** **(obrigatório para cronograma apropriado****) \*/** **AND**  MTRF.CODTRF LIKE :codTrf  

****/\***** **(obrigatório para** **cronograma apropriado****) \*/** **AND**  MTRF.IDCENARIO = :idCenario 

****/\***** **(obrigatório para** **cronograma apropriado****) \*/** **AND**  MTRF.TIPOPLANILHA = :tipoPlanilha

 

**UNION ALL**

 

**SELECT** P.IDPERIODO **AS** NUMPERIODO, 

             TMOV.CODMOEVALORLIQUIDO **AS** MOEDA 

             ,P.DTINICIO **AS** DATAAPROPRIACAO 

             ,MISMAPROP.IDISM, TITMMOV.PRECOUNITARIO, TITMMOV.QUANTIDADE 

             ,MTRF.CODTRF, MTRF.IDCENARIO, MTRF.TIPOPLANILHA 

             ,(**CASE** TTMVEXT.TIPORATEIO 

                **WHEN** 'P' **THEN** ( **COALESCE**(TITMMOV.QUANTIDADE \* TITMMOV.PRECOUNITARIO \* TITMMOVRATCCU.PERCENTUAL / 100, TITMMOVRATCCU.VALOR) ) 

                **ELSE** ( **COALESCE**(TITMMOVRATCCU.VALOR, TITMMOV.QUANTIDADE \* TITMMOV.PRECOUNITARIO \* TITMMOVRATCCU.PERCENTUAL / 100) ) 

             **END** ) **AS** VALOR 

      **FROM** **TITMMOV**(**NOLOCK**)

      **JOIN** **TMOV**(**NOLOCK**) **ON** (TITMMOV.CODCOLIGADA = TMOV.CODCOLIGADA **AND** 

TITMMOV.IDMOV = TMOV.IDMOV) 

**JOIN** **TITMMOVRATCCU** (**NOLOCK**) **ON**(TITMMOV.CODCOLIGADA = TITMMOVRATCCU.CODCOLIGADA

           **AND** TITMMOV.IDMOV = TITMMOVRATCCU.IDMOV

           **AND**TITMMOV.NSEQITMMOV = TITMMOVRATCCU.NSEQITMMOV) 

**JOIN** MTAREFA **MTRF**(**NOLOCK**) **ON**(TITMMOVRATCCU.CODCOLIGADA = MTRF.CODCOLIGADA

 **AND** TITMMOVRATCCU.IDPRJ = MTRF.IDPRJ

           **AND** TITMMOVRATCCU.IDTRF = MTRF.IDTRF) 

**JOIN** MPERIODO **P**(**NOLOCK**) **ON** (MTRF.CODCOLIGADA = P.CODCOLIGADA

           **AND** MTRF.IDPRJ = P.IDPRJ)   

**JOIN** **TTMVEXT**(**NOLOCK**) **ON**(TMOV.CODCOLIGADA = TTMVEXT.CODCOLIGADA

           **AND** TMOV.CODTMV = TTMVEXT.CODTMV)  

      **JOIN** **MISMAPROP** (**NOLOCK**) **ON**(MISMAPROP.CODCOLIGADA = MTRF.CODCOLIGADA

           **AND** MISMAPROP.IDISM = MTRF.IDISM) 

 

**WHERE**

**/\*** **(obrigatório para ambos)  \*/**P.CODCOLIGADA = :codColigada

**/\*** **(obrigatório para ambos)** **\*/****AND**  P.IDPRJ = :idPrj 

**/\*** **(obrigatório para cronograma apropriado)****\*/****AND**  MTRF.CODTRF LIKE :codTrf 

**/\*****(obrigatório para cronograma apropriado)****\*/****AND**  MTRF.IDCENARIO = :idCenario

****/\* **(******obrigatório para cronograma apropriado)****\*/******AND**  MTRF.TIPOPLANILHA = :tipoPlanilha

 

**AND** TTMVEXT.GERAAPROPRIACAO = 1

**AND** TMOV.APROPRIADO = 1

**AND** TMOV.STATUS <> 'C') APROP 

     

      

**GROUP BY** APROP.NUMPERIODO,MOEDA,APROP.DATAINICIOPERIODO, APROP.IDISM, APROP.PRECOUNITARIO, APROP.QUANTIDADE, APROP.CODTRF, APROP.IDCENARIO, APROP.TIPOPLANILHA

 **ORDER BY** APROP.NUMPERIODO,APROP.MOEDA **DESC**

 

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [Parâmetros de Projetos] | [Inclusão] | [Selecionar Projetos -> Parâmetros do Projeto -> Cronograma -> Gerais -> Consulta SQL Personalizada Para Dados de Apropriação -> Por Tarefa] | - |
| [Parâmetros de Projetos] | [Inclusão] | [Selecionar Projetos -> Parâmetros do Projeto -> Cronograma -> Gerais -> Consulta SQL Personalizada Para Dados de Apropriação -> Múltiplas Tarefas] |  |
|  |  |  | - |

## Protótipo de Tela

**Protótipo 01 - Parâmetros de Projeto**

****Protótipo 02 - Cronogramas****

******Protótipo 03 - Relatório Periódico - Consulta Personalizada******
