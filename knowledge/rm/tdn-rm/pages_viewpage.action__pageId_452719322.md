---
content_hash: 287334bb97cb009912fd35faa1034689d6fcb5e2012759c6d4dd5be665981363
fetched_at: '2026-06-29T00:10:06.625536+00:00'
page_id: '452719322'
product: rm
source: tdn-rm
title: Layout Para Importação de Contas Contábeis (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719322
version: 2
---

**Importante:**  
 Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
 **Campos obrigatórios estão destacados em negrito.**  
 DELIMITADOR DE CAMPOS: ";"  
 Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
 Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
 As tabelas abaixo são premissas para a importação, caso a mesma esteja vinculada a tabela de Agrupamento de Contas Contábeis da base de origem:  
 - PCODINTCONTFUNC  
 - PCODINTCONT  
 - PGRPCONTACONT  
 - PCCUSTO  
 - GFILIAL  
 - GDEPTO  
 - CCONTAS  
    
    
  **Atenção!** Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:  
 -  0 (zero) ou 1(um) em campos do tipo **Booleano**;  
 -  Números (00) em campos do tipo**Inteiro**;  
 -  Números com vírgulas ou Pontos (0,00 ou 0.00) em campos do tipo **Real**;  
 - (ddmmyyyy) em campos do tipo **Data**;  
 - (GRR20071514) em campos do tipo **String**;  
 - Começam /@ e terminam com @/ em campos do tipo **MEMO**.  
 Para o caso de importação de históricos a data da mudança deve sempre ser informada. Caso este campo não seja informado, o registro em questão não será importado.  
 É essencial o cadastramento da tabela dinâmica, centro de custo, filial e departamento e dados da Conta Saldus (quando necessário).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Descrição** | **Tipo** | **Tamanho** | **Posição** | **Campo** |
| Código da filial | Inteiro | 2 | 1 | PCONTAS.CODFILIAL |
| **Conta Saldus** | **String** | **40** | **2** | **PCONTAS.CONTASALDUS** |
| Código da coligada da conta |  | 2 | 3 | PCONTAS.CODCOLCONTA |
| Código do centro de custo | String | 25 | 4 | PCONTAS.CODCCUSTO |
| **Grupo da conta Contábil** | **String** | **22** | **5** | **PCONTAS.GRPCONTA** |
| Código de integração Contábil | String | 22 | 6 | PCONTAS.CODINTGR |
| Código de intgr. Funcionários | String | 22 | 7 | PCONTAS.INTEGRCFUNC |
| Código do departamento | String | 25 | 8 | PCONTAS.CODDEPARTAMENTO |
| Identificador do Item Contábil | Inteiro | 4 | 9 | PCONTAS.IDITEMCONTABIL |
| Identificador da Classe de Valor | Inteiro | 4 | 10 | PCONTAS.IDCLASSEVALOR |
