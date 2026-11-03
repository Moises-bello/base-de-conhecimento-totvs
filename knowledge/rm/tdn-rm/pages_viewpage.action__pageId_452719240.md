---
content_hash: b04000d1202b4d009d9aaed91df1971b60648456f407bdbcdf3568b68e1ecb05
fetched_at: '2026-06-29T00:10:04.721272+00:00'
page_id: '452719240'
product: rm
source: tdn-rm
title: Layout Para Importação de Linhas de Vale Transporte Utilizadas (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719240
version: 2
---

**Importante:**  
 Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
 **Campos obrigatórios estão destacados em negrito.**  
 DELIMITADOR DE CAMPOS: ";"  
 Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
 Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
 As tabelas abaixo são premissas para a importação, caso as mesmas estejam vinculadas a tabela de Linhas de Vale Transporte Utilizadas da base de origem:  
 - PFUNC  
 - PVALETR  
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
| **Chapa do funcionário** | **String** | **16** | **1** | **PFVALETR.CHAPA** |
| **Código da linha** | **String** | **20** | **2** | **PFVALETR.CODLINHA** |
| **Data início uso da linha** | **Data** | **8** | **3** | **PFVALETR.DTINICIO** |
| Data final do uso da linha | Data | 8 | 4 | PFVALETR.DTFIM |
| Número de viagens | Inteiro | 2 | 5 | PFVALETR.NROVIAGENS |
| Número de viagens no expediente | Inteiro | 2 | 6 | PFVALETR.NROVIAGMEIOEXP |
