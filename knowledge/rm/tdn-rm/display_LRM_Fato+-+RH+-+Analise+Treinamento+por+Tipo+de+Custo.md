---
content_hash: 4a2a8d9b30de2524b10c1fa67a81fd76b4d2801027355633be2fcd4b780beaa6
fetched_at: '2026-06-29T00:09:37.357237+00:00'
page_id: '425459590'
product: rm
source: tdn-rm
title: Fato - RH - Analise Treinamento por Tipo de Custo
type: documentation
url: https://tdn.totvs.com/display/LRM/Fato+-+RH+-+Analise+Treinamento+por+Tipo+de+Custo
version: 4
---

**Fato Análise de Treinamentos**

---

Esta analise é responsável por retornar os dados de treinamentos que foram realizados pelos colaboradores da organização. No IBM Cognos foram disponibilizados alguns relatórios como: "Treinamentos realizados por Centro de Custo, Treinamentos realizados por Curso".  
 Segue abaixo o De/Para para extração destes dados da base RM.

**Tabela Stage Área: HLM**

|  |  |  |
| --- | --- | --- |
| **DESCRIÇÃO** | **CAMPO**   **STAGE ÁREA** | **CAMPO RM** |
| NÚMERO REGISTRO - PK | HLM\_RECNO | AUTOINC |
| LINHA DE PRODUTO | HLM\_LINPRO | R |
| INSTÂNCIA | HLM\_ISTCIA | 1 |
| EMPRESA - FK | HLM\_EMPRES | MD5 (CODCOLIGADA) |
| ESTABELECIMENTO - CÓDIGO | HLM\_FILIAL | CODFILIAL |
| ESTABELECIMENTO - FK | HLM\_ESTABL | MD5(CODCOLIGADA + CODFILIAL) |
| FAIXA SALARIAL - FK | HLM\_FXASAL | MD5(COLIGADA + CODFAIXA) |
| MOEDA - FK | HLM\_MOEDA | - |
| CATEGORIA SALARIAL – FK \* | HLM\_CATSAL | MD5(PCODRECEB.CODCLIENTE) |
| SINDICATO - FK | HLM\_SINDIC | MD5(PSINDIC.CODIGO) |
| TURNO - FK | HLM\_TURNO | O RM NÃO POSSUI ESTA ENTIDADE |
| MÃO DE OBRA - FK | HLM\_TIPMOB | O RM NÃO POSSUI ESTA ENTIDADE |
| COLABORADOR – FK \* | HLM\_COLABR | MD5(CODPESSOA) |
| PLANO CENTRO CUSTO - FK | HLM\_PLCCST | O RM NÃO POSSUI ESTA ENTIDADE |
| CENTRO DE CUSTO - FK | HLM\_CCUSTO | MD5(VDESPESA.CODCCUSTO) |
| UNIDADE DE NEGÓCIO - FK | HLM\_UNDNEG | O RM NÃO POSSUI ESTA ENTIDADE |
| INSTITUIÇÃO - FK | HLM\_INSTIT | MD5(VENTIDADES.CODENTIDADE) |
| INSTRUTOR - FK | HLM\_INSTRU | MD5(PPESSOA.CODPESSOA) |
| CURSO - FK | HLM\_CURSO | MD5(COLIGADA + VCURSOS.CODCURSO) |
| TIPO DE CURSO - FK | HLM\_TIPCUR | MD5(VTURMAS.INTERNO) |
| REGIÃO - FK | HLM\_REGIAO | MD5(CODMUNICIPIO + CODETD) |
| ESTADO CIVIL - FK | HLM\_ESTCIV | MD5(PCODESTCIVIL.CODCLIENTE) |
| FAIXA ETÁRIA - FK | HLM\_FXAETA | O RM NÃO POSSUI ESTA ENTIDADE |
| GRAU DE INSTRUÇÃO - FK | HLM\_GRAINS | MD5(PPESSOA.GRAUINSTRUCAO) |
| NÍVEL HIERÁRQUICO - FK | HLM\_NIVHIE | O RM NÃO POSSUI ESTA ENTIDADE |
| RELAÇÃO TRABALHO - FK | HLM\_RELTRB | MD5(PTPFUNC.CODCLIENTE) |
| TEMPO CASA - FK | HLM\_TPCASA | MD5(COLIGADA + CHAPA + DATAADMISSAO) |
| TEMPO CARGO – FK \* | HLM\_TPCARG | MD5(COLIGADA + CHAPA + DATAMUDANCA) |
| CARGO – FK \* | HLM\_CARGO | MD5(COLIGADA + CODCARGO) |
| TREINAMENTO CONCLUÍDO | HLM\_STTREI | VTURMAS.ATIVO |
| DATA DE REALIZAÇÃO DO TREINAMENTO | HLM\_DATA | VTURMAS.DTINICIO |
| QTDE HORAS TREINAMENTO | HLM\_QHTREI | VTURMAS.CARGAHORARIA |
| VL TREINAMENTO | HLM\_VTREIN | HLM\_TURMASDESPESAS.DESPESAS |
| SEÇÃO - FK | HLM\_SECAO | MD5(COLIGADA + CODSECAO) |
| BOLSA DE ESTUDO – FK  \* | BOLSA | HLM\_BOLSA |
| MOTIVO TREINAMENTO - FK | MOTTRE | HLM\_MOTTRE |
| - | - | HLM\_REALIZ |
| VL INVESTIMENTO EMPRESA | VINVEP | HLM\_VINVEP |
| VL INVESTIMENTO COLABORADOR | VINVCL | HLM\_VINVCL |
| QTDE DIAS BOLSA ESTUDO | DBOLSA | HLM\_DBOLSA |
| QTDE COLABORADORES BOLSISTAS | QBOLSA | HLM\_QBOLSA |
| QTDE COLABORADORES TREINADOS | HLM\_QCTREI | HLM\_TURMASDESPESAS.QTDEALUNOS |

**Data de Extração:** Data de Realização do Treinamento - VTURMAS.DTINICIO  
    
 **Conceito de Extração:** Fato - RH - Analise Treinamentos  
    
 **View:** HLM\_TreinamentosColaboradores - HLM\_TURMASDESPESAS  
    
 **Parâmetros:**

Será utilizado somente os parâmetros de extração gerais.  Os dados desta analise são recuperados do Vitae. (Sistema de Gestão Pessoas)  
 Será utilizado também o parâmetro de Tipo de Categoria de Beneficio para bolsa, o usuário neste parâmetro devera informar quais benefícios serão considerados bolsa, este parametro afetara a extração dos dados: Valor Investimento Empresa, Valor Investimento Colaborador, Qtde Dias Bolsa Estudo, Qtde Colaboradores Bolsistas. O Anexo B fala mais detalhes sobre esta extração de dados de bolsa.  
    
 **Observações:**\*

Será retornado o ultimo cargo do funcionário, como podemos ter vários funcionários cadastrados para uma mesma pessoa, será retornado o de maior data de admissão.  
 Sobre o tempo de cargo, será retornado o tempo de cargo do cargo atual do funcionário.
