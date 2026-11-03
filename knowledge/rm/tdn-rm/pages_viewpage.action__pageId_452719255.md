---
content_hash: d8efb1c78a7d2b71ddd6ec2bbb0a0f9fa7cc3a1723d4aeb4cdf0c4d31a770215
fetched_at: '2026-06-29T00:10:04.804801+00:00'
page_id: '452719255'
product: rm
source: tdn-rm
title: Layout Para Importação de Histórico de Seção (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719255
version: 2
---

**Importante:**  
 Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
 **Campos obrigatórios estão destacados em negrito.**  
 DELIMITADOR DE CAMPOS: ";"  
 Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
 Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
 As tabelas abaixo são premissas para a importação, caso as mesmas estejam vinculadas a tabela de Histórico de Seção da base de origem:  
 - PFUNC  
 - PSECAO  
 - PMOTMUDSECAO  
    
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
| **Chapa** | **String** | **16** | **1** | **PFHSTSEC.CHAPA** |
| **Data da Mudança (ddmmaaaa hhmmss)** | **Data** | **17** | **2** | **PFHSTSEC.DTMUDANCA** |
| **Código do Motivo da Mud. De Seção** | **String** | **15** | **4** | **PFHSTSEC.MOTIVO** |
| **Código da Seção** | **String** | **8** | **5** | **PFHSTSEC.CODSECAO** |
