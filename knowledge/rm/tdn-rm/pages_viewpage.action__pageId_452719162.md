---
content_hash: b7b5348e9bed73d12d85348dc339e639d3ec33e83a588a44bcba5e35c00f9473
fetched_at: '2026-06-29T00:10:03.839831+00:00'
page_id: '452719162'
product: rm
source: tdn-rm
title: Layout Para Importação de Histórico de Encargos (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719162
version: 2
---

**Importante:**  
 Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
 **Campos obrigatórios estão destacados em negrito.**  
 DELIMITADOR DE CAMPOS: ";"  
 Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
 Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
 As tabelas abaixo são premissas para a importação, caso as mesmas estejam vinculadas a tabela de Histórico de Encargos da base de origem:  
 - PFUNC  
 - PENCARGO  
    
  **Atenção!**  Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:  
 -  0 (zero) ou 1(um) em campos do tipo **Booleano**;  
 -  Números (00) em campos do tipo**Inteiro**;  
 -  Números com vírgulas ou Pontos (0,00 ou 0.00) em campos do tipo **Real**;  
 - (ddmmyyyy) em campos do tipo **Data**;  
 - (GRR20071514) em campos do tipo **String**;  
 - Começam /@ e terminam com @/ em campos do tipo **MEMO**.  
 Para o caso de importação de históricos a data da mudança deve sempre ser informada. Caso este campo não seja informado, o registro em questão não será importado.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **DESCRIÇÃO** | **TIPO** | **TAMANHO** | **Posição** | **CAMPO** |
| **Chapa do Funcionário** | **String** | **16** | **1** | **PFENCARGO.CHAPA** |
| **Ano Competência** | **Inteiro** | **5** | **2** | **PFENCARGO.ANOCOMP** |
| **Mês Competência** | **Inteiro** | **5** | **3** | **PFENCARGO.MESCOMP** |
| **Código do Encargo** | **String** | **4** | **4** | **PFENCARGO.CODENCARGO** |
| Valor Nominal | Real | 15 | 5 | PFENCARGO.VALOR |
| Letra da Aplicação | String | 1 | 6 | PFENCARGO.APLICACAO |
| Base do Encargo | Real | 15 | 7 | PFENCARGO.BASEENCARGO |
