---
content_hash: 549e1682e3dcb1c989a50ee465ee71f8bd855b199f064cd05ef9787f8b45567f
fetched_at: '2026-06-29T00:10:02.445486+00:00'
page_id: '452718911'
product: rm
source: tdn-rm
title: Layout Para Importação de Contas Gerenciais (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718911
version: 2
---

**Importante:**  
 Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
 **Campos obrigatórios estão destacados em negrito.**  
 DELIMITADOR DE CAMPOS: ";"   
 Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
 Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
 - PCODINTGERFUNC  
 - PGRPCONTAGER  
 - PCCUSTO  
 - GFILIAL  
 - GDEPTO  
 - CCONTAS  
 - PCODINTGER  
    
  **Atenção!** Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:  
 -  0 (zero) ou 1(um) em campos do tipo **Booleano**;  
 -  Números (00) em campos do tipo **Inteiro**;  
 -  Números com vírgulas ou Pontos (0,00 ou 0.00) em campos do tipo **Real**;  
 - (ddmmyyyy) em campos do tipo **Data**;  
 - (GRR20071514) em campos do tipo **String**;  
 - Começam /@ e terminam com @/ em campos do tipo **MEMO**.  
 Para o caso de importação de históricos a data da mudança deve sempre ser informada. Caso este campo não seja informado, o registro em questão não será importado.  
  

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Descrição** | **Tipo** | **Tamanho** | **Posição** | **Campo** |
| Código da filial | Inteiro | 2 | 7 | PCONTASGER.CODFILIAL |
| **Conta Saldus** | **String** | **40** | **6** | **PCONTASGER.CONTASALDUS** |
| Código da coligada da conta | Inteiro | 2 | 5 | PCONTASGER.CODCOLCONTA |
| Código do centro de custo | String | 25 | 9 | PCONTASGER.CODCCUSTO |
| **Grupo da conta gerencial** | **String** | **22** | **2** | **PCONTASGER.GRPCONTA** |
| Código de integração gerencial | String | 22 | 3 | PCONTASGER.CODINTEGR |
| Código de integração Funcionários | String | 22 | 4 | PCONTASGER.INTEGRCFUNC |
| Código do departamento | String | 25 | 8 | PCONTASGER.CODDEPARTAMENTO |
