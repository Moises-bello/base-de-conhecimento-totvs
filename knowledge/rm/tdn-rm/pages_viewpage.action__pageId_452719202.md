---
content_hash: f120795d332143c5329ad25d23588aec0a3c469c34fba69ab1e764eb1ec626d4
fetched_at: '2026-06-29T00:10:04.142844+00:00'
page_id: '452719202'
product: rm
source: tdn-rm
title: Layout Para Importação de Cargos (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719202
version: 2
---

**Importante:**  
 Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
 **Campos obrigatórios estão destacados em negrito.**  
 DELIMITADOR DE CAMPOS: ";"  
 Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
 Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
 As tabelas abaixo são premissas para a importação, caso as mesmas estejam vinculadas as tabelas de cargos da base de origem:  
 - CCLASSIFICACC  
 - GCCUSTO  
 - PCODINTCONT  
 - PCODINTGER  
    
  **Atenção!** Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:  
 -  0 (zero) ou 1(um) em campos do tipo **Booleano**;  
 -  Números (00) em campos do tipo**Inteiro**;  
 -  Números com vírgulas ou Pontos (0,00 ou 0.00) em campos do tipo **Real**;  
 - (ddmmyyyy) em campos do tipo **Data**;  
 - (GRR20071514) em campos do tipo **String**;  
 - Começam /@ e terminam com @/ em campos do tipo **MEMO**.stão   
 Para o caso de importação de históricos a data da mudança deve sempre ser informada. Caso este campo não seja informado, o registro em questão não será importado.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Descrição** | **Tipo** | **Tamanho** | **Posição** | **Campo** |
| **Cód. Identificador** | **String** | **16** | **1** | **PCARGO.CODIGO** |
| **Descrição do Cargo** | **String** | **40** | **2** | **PCARGO.NOME** |
| Jornada de trabalho | Inteiro | 10 | 3 | PCARGO.JORNADATRABALHO |
| Grupo Ocupacional | String | 10 | 4 | PCARGO.CODGRUPOOCUP |
| Descrição | Memo | 250 | 5 | PCARGO.DESCRICAO |
| Inativo | Booleano | 1 | 6 | PCARGO.INATIVO |
| Benefpontos | Inteiro | 10 | 7 | PCARGO.BENEFPONTOS |
| Classificação de Cargo/Função PPE | String | 3 | 8 | PCARGO. CODCLASSCARGO |
| Sigla | String | 30 | 9 | PCARGO.SIGLA |
