---
content_hash: 0f861642ee9826a656f45dc70246d5ca83123fe6fbdd4ff7138240e7a033572f
fetched_at: '2026-06-29T00:10:04.082079+00:00'
page_id: '452719194'
product: rm
source: tdn-rm
title: Layout Para Importação de Histórico de Encargos por Centro de Custo (Versão
  12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719194
version: 2
---

**Importante:**  
 Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
 **Campos obrigatórios estão destacados em negrito.**  
 DELIMITADOR DE CAMPOS: ";"  
 Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
 Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
 As tabelas abaixo são premissas para a importação, caso as mesmas estejam vinculadas a tabela de Histórico de Encargos por Centro de Custo da base de origem:  
 - PFUNC  
 - PENCARGO  
 - PFENCARGO  
    
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
| **DESCRIÇÃO** | **TIPO** | **TAMANHO** | **Posição** | **CAMPO** |
| **Chapa do Funcionário** | **String** | **16** | **1** | **PFENCCC.CHAPA** |
| Ano Competência | Inteiro | 4 | 2 | PFENCCC.ANOCOMP |
| Mês Competência | Inteiro | 2 | 3 | PFENCCC.MESCOMP |
| Código do Encargo | String | 4 | 4 | PFENCCC.CODENCARGO |
| **Cód. Centro de Custo do Labore** | **String** | **25** | **5** | **PFENCCC.CODPCCUSTO** |
| Valor do Evento | Real | 9 | 6 | PFENCCC.VALOR |
| Flag de Evento Digitado/Importado | Inteiro | 2 | 7 | PFENCCC.EDITADO |
| Cód. Centro de Custo Global | String | 25 | 8 | PFENCCC.CODGCCUSTO |
