---
content_hash: 7141209bcce1df18e9e0469c1c392861ddf5df37a44ebe46b050d3c9e287f887
fetched_at: '2026-06-29T00:09:37.508178+00:00'
page_id: '425459624'
product: rm
source: tdn-rm
title: Fato Análise Treinamento por Tipo de Custo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459624
version: 2
---

**Fato Análise Treinamento por Tipo de Custo**

---

Esta analise é responsável por retornar os dados de treinamentos que foram realizados pelos colaboradores da organização, categorizando por tipo de custo. (TREINAMENTO, TRANSPORTE, HOSPEDAGEM) No IBM Cognos foram disponibilizados alguns relatórios como: "Treinamentos realizados por Centro de Custo, Treinamentos realizados por Curso"  
 Segue abaixo o De/Para para extração destes dados da base RM.  
    
 Tabela Stage Área: HQV

|  |  |  |
| --- | --- | --- |
| **DESCRIÇÃO** | **CAMPO**   **STAGE ÁREA** | **CAMPO RM** |
| NÚMERO REGISTRO - PK | HQV\_RECNO | AUTOINC |
| LINHA DE PRODUTO | HQV\_LINPRO | R |
| INSTÂNCIA | HQV\_ISTCIA | 1 |
| EMPRESA - FK | HQV\_EMPRES | MD5 (CODCOLIGADA) |
| ESTABELECIMENTO - CÓDIGO | HQV\_FILIAL | CODFILIAL |
| ESTABELECIMENTO - FK | HQV\_ESTABL | MD5(CODCOLIGADA + CODFILIAL) |
| FAIXA SALARIAL - FK | HQV\_FXASAL | MD5(COLIGADA + CODFAIXA) |
| MOEDA - FK | HQV\_MOEDA | - |
| CATEGORIA SALARIAL - FK | HQV\_CATSAL | MD5(PCODRECEB.CODCLIENTE) |
| LOCALIDADE - FK | HQV\_LOCALI | - |
| SINDICATO - FK | HQV\_SINDIC | MD5(PSINDIC.CODIGO) |
| TURNO - FK | HQV\_TURNO | O RM NÃO POSSUI ESTA ENTIDADE |
| MÃO DE OBRA - FK | HQV\_TIPMOB | O RM NÃO POSSUI ESTA ENTIDADE |
| COLABORADOR - FK | HQV\_COLABR | MD5(CODPESSOA) |
| PLANO CENTRO CUSTO - FK | HQV\_PLCCST | O RM NÃO POSSUI ESTA ENTIDADE |
| CENTRO DE CUSTO - FK | HQV\_CCUSTO | MD5(GCCUSTO.CODCCUSTO) |
| PLANO DE LOTAÇÃO – FK | HQV\_PLOTAC | O RM NÃO POSSUI ESTA ENTIDADE |
| UNIDADE DE LOTAÇÃO - FK | HQV\_ULOTAC | O RM NÃO POSSUI ESTA ENTIDADE |
| UNIDADE DE NEGÓCIO - FK | HQV\_UNDNEG | O RM NÃO POSSUI ESTA ENTIDADE |
| INSTITUIÇÃO - FK | HQV\_INSTIT | MD5(VENTIDADES.CODENTIDADE) |
| INSTRUTOR - FK | HQV\_INSTRU | MD5(PPESSOA.CODPESSOA) |
| CURSO - FK | HQV\_CURSO | MD5(COLIGADA + VCURSOS.CODCURSO) |
| TIPO DE CURSO – FK | HQV\_TIPCUR | MD5(VTURMAS.INTERNO) |
| REGIAO – FK | HQV\_REGIAO | MD5(CODMUNICIPIO + CODETD) |
| ESTADO CIVIL – FG | HQV\_ESTCIV | MD5(PCODESTCIVIL.CODCLIENTE) |
| FAIXA ETARIA – FK | HQV\_FXAETA | O RM NÃO POSSUI ESTA ENTIDADE |
| GRAU DE INSTRUÇÃO – FK | HQV\_GRAINS | MD5(PPESSOA.GRAUINSTRUCAO) |
| NIVEL HIERARQUICO – FK | HQV\_NIVHIE | O RM NÃO POSSUI ESTA ENTIDADE |
| RELAÇÃO TRABALHO - FK | HQV\_RELTRB | O RM NÃO POSSUI ESTA ENTIDADE |
| TEMPO DE CASA – FK | HQV\_TPCASA | MD5(COLIGADA + CHAPA + DATAADMISSAO) |
| TEMPO DE CARGO – FK | HQV\_TPCARG | MD5(COLIGADA + CHAPA + DATAMUDANCA) |
| CARGO – FK | HQV\_CARGO | MD5(COLIGADA + CODCARGO) |
| SECAO – FK | HQV\_SECAO | MD5(COLIGADA + CODSECAO) |
| BOLSA – FK | HQV\_BOLSA | HLM\_BOLSA |
| TIPO DE CUSTO - FK | HQV\_TIPCST | - |
| MOTIVO DE TREINAMENTO – FK | HQV\_MOTTRE | - |
| SITUACAO DO TREINAMENTO | HQV\_STTREI | - |
| DATA | HQV\_DATA | VTURMAS.DTINICIO |
| VALOR DO TREINAMENTO | HQV\_VTREIN | HLM\_TURMASDESPESAS.DESPESAS |

**Data de Extração:** Data de Realização do Treinamento - VTURMAS.DTINICIO  
    
 **Conceito de Extração:** Fato - RH - Analise Treinamentos por Tipo de Custo  
    
 **View:** HQV\_TreinamentosColaboradores  
    
 **Parâmetros:** Será utilizado somente os parâmetros de extração gerais.  Os dados desta analise são recuperados do Vitae. (Sistema de Gestão Pessoas).  
 Será utilizado também o parâmetro de Tipo de Categoria de Beneficio para bolsa, o usuário neste parâmetro devera informar quais benefícios serão considerados bolsa, este parametro afetara a extração dos dados: Valor Investimento Empresa, Valor Investimento Colaborador, Qtde Dias Bolsa Estudo, Qtde Colaboradores Bolsistas. O Anexo B fala mais detalhes sobre esta extração de dados de bolsa.
