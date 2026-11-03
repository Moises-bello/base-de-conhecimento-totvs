---
content_hash: bedce5a22f983971c967f0e456afe4b96381ebf86986e6619f827576875f2fb2
fetched_at: '2026-06-29T00:10:03.901430+00:00'
page_id: '452719171'
product: rm
source: tdn-rm
title: Layout Para Importação Histórico Função Confiança (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719171
version: 2
---

**Importante:**  
 Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
 **Campos obrigatórios estão destacados em negrito.**  
 DELIMITADOR DE CAMPOS: ";"  
 Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
 Entre ponto virgula ( **;;** ) "Correspondendo um campo NULL".  
 As tabelas abaixo são premissas para a importação, caso as mesmas estejam vinculadas a tabela de Histórico de Função da base de origem:  
 - PFUNC  
 - PFUNCAO  
 - PMOTMUDFUNCAO  
    
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
| **Chapa** | **String** | **16** | **1** | **PFHSTFUNCAOCONF.CHAPA** |
| **Data da Mudança (ddmmaaaa**   **hh:mm:ss)** | **Data** | **17** | **2** | **PFHSTFUNCAOCONF.DTMUDANCA** |
| **Código do Motivo da Mudança de Função** | **String** | **2** | **3** | **PFHSTFUNCAOCONF.MOTIVO** |
| **Código da Função** | **String** | **10** | **4** | **PFHSTFUNCAOCONF.CODFUNCAO** |
| Data Final da Mudança   (ddmmaaaa   hh:mm:ss) | Data | 17 | 2 | PFHSTFUNCAOCONF.DTFIMMUDANCA |
