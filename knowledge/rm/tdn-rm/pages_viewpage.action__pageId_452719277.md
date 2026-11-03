---
content_hash: 06b7edd415617036d7474d87205c1d0a2203c8715943941d54bff2050c97873b
fetched_at: '2026-06-29T00:10:05.172863+00:00'
page_id: '452719277'
product: rm
source: tdn-rm
title: Layout Para Importação de Encargos (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719277
version: 2
---

**Importante:**  
 Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
 **Campos obrigatórios estão destacados em negrito.**  
 DELIMITADOR DE CAMPOS: ";"  
 Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
 Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
 As tabelas abaixo são premissas para a importação, caso as mesmas estejam vinculadas a tabela de Encargos da base de origem:  
 - GFORMULA  
 - PRATEIO  
 - PCONTAS  
 - PCONTASGER  
 - CHISTP  
    
  **Atenção!** Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:  
 -  0 (zero) ou 1(um) em campos do tipo **Booleano**;  
 -  Números (00) em campos do tipo**Inteiro**;  
 -  Números com vírgulas ou Pontos (0,00 ou 0.00) em campos do tipo **Real**;  
 - (ddmmyyyy) em campos do tipo **Data**;  
 - (GRR20071514) em campos do tipo **String**;  
 - Começam /@ e terminam com @/ em campos do tipo **MEMO**.  
 Para o caso de importação de históricos a data da mudança deve sempre ser informada. Caso este campo não seja informado, o registro em questão não será importado.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Descrição** | **Tipo** | **Tamanho** | **Posição** | **Campo** |
| **Código Identificador do Encargo** | **String** | **4** | **1** | **PENCARGO.CODIGO** |
| **Descrição do Encargo** | **String** | **40** | **2** | **PENCARGO.DESCRICAO** |
| **Tipo do Encargo** | **String** | **2** | **3** | **PENCARGO.TIPOENCARGO** |
| Porcentagem do Encargo | Real | 9 | 4 | PENCARGO.PORCENTAGEM |
| Código Identificador da Fórmula de Valor | String | 8 | 5 | PENCARGO.CODFORMVALOR |
| Indicativo de Provisão Acumulada | Inteiro | 2 | 6 | PENCARGO.PROVACUMULADA |
| Código do Sind. que Incide no Salário | Inteiro | 2 | 7 | PENCARGO.CONSIDINCSALARIO |
| Indicativo de Consideração do Mês Atual | Inteiro | 2 | 8 | PENCARGO.CONSIDMESATUAL |
| Indicativo de Status de Atividade | String | 40 | 9 | PENCARGO.ATIVO |
| Código da Fórmula de Seleção | String | 8 | 10 | PENCARGO.CODFORMSELECAO |
| Número da Conta para Crédito | String | 22 | 11 | PENCARGO.CONTACREDITO |
| Número da Conta para Débito | String | 22 | 12 | PENCARGO.CONTADEBITO |
| Número do Histórico Padrão | String | 10 | 13 | PENCARGO.NROHISTPADRAO |
| Complemento do Histórico | String | 60 | 14 | PENCARGO.COMPLHISTORICO |
| Código da Aplicacao do Encargo | String | 1 | 15 | PENCARGO.APLICACAO |
| nº  Conta Gerencial para Credito | String | 22 | 16 | PENCARGO.CGCREDITO |
| nº  Conta Gerencial para Debito | String | 22 | 17 | PENCARGO.CGDEBITO |
| Existe Intgr Contábil Conta Crédito | Inteiro | 2 | 18 | PENCARGO.TEMINTCONTCC |
| Existe Intgr Contábil Conta Dédito | Inteiro | 2 | 19 | PENCARGO.TEMINTCONTCD |
| Existe Intgr Contábil Conta Ger Crédito | Inteiro | 2 | 20 | PENCARGO.TEMINTCONTGC |
| Existe Intgr Contábil Conta Ger Dédito | Inteiro | 2 | 21 | PENCARGO.TEMINTCONTGD |
| Existe Intgr Func Contab Conta Crédito | Inteiro | 2 | 22 | PENCARGO.TEMINTFUNCCC |
| Existe Intgr Func Contab Conta Dédito | Inteiro | 2 | 23 | PENCARGO.TEMINTFUNCCD |
| Existe Intgr Func Ger Conta Crédito | Inteiro | 2 | 24 | PENCARGO.TEMINTFUNCGC |
| Existe Intgr Func Ger Conta Dédito | Inteiro | 2 | 25 | PENCARGO.TEMINTFUNCGD |
| Indicativo para Contab. Parcial | Inteiro | 2 | 26 | PENCARGO.CONTPARCIAL |
| Preenchido com ";" |  | 2 | 27 |  |
| Fórmula para compor Compl. Histórico | String | 8 | 28 | PENCARGO.FORMCOMPLHIST |
| Período de cálculo do rateio de encargos | Inteiro | 2 | 29 | PENCARGO.PERCALCRATEIO |
| Código do rateio que o encargo segue | String | 8 | 30 | PENCARGO.CODRATEIO |
| Conta Reversão | String | 22 | 31 | PENCARGO.CONTAREVERSAO |
| Considera Valor Ant.da Transferência | Booleano | 2 | 32 | PENCARGO.CONSIDERAVALORTRANSF |
| Aplicar Arredondamento sob valor total | Booleano | 2 | 33 | PENCARGO.ARREDTOTAL |
| Considera Seção Ant ao gerar lançamento | Booleano | 2 | 34 | PENCARGO.CONSIDSECANT |
| Tipo de percentual | Inteiro | 2 | 35 | PENCARGO.TIPOPERC |
| Segue Rateio Movimento Ensino Importado | Booleano | 2 | 36 | PENCARGO.SEGUERATEIOMOVENSINOIMP |
| Incide no Custo do funcionário | Inteiro | 2 | 37 | PENCARGO.INCIDECUSTOFUNCIONARIO |
| Aplicar alíquota FAP do estabelecimento no cálculo do encargo | Inteiro | 2 | 38 | PENCARGO.APLICARFAPESTABELECIMENTO |
| Abate Adiantamento 13º | Booleano | 2 | 39 | PENCARGO.ABATEADIANT13O |
