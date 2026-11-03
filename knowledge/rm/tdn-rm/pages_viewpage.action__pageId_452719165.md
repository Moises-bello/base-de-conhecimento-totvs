---
content_hash: f9fb397bd0caaad8882e30c669fd0afdbe9ea0adf5bfb7cb4939a0c0beda572a
fetched_at: '2026-06-29T00:10:03.858672+00:00'
page_id: '452719165'
product: rm
source: tdn-rm
title: Layout Para Importação de Histórico de Função (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719165
version: 2
---

**Importante:**  
 Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
 **Campos obrigatórios estão destacados em negrito.**  
 DELIMITADOR DE CAMPOS: ";"  
 Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
 Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
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
| **Chapa** | **String** | **16** | **1** | **PFHSTFCO.CHAPA** |
| **Data da Mudança (ddmmaaaa hh:mm:ss)** | **Data** | **17** | **2** | **PFHSTFCO.DTMUDANCA** |
| **Código do Motivo da Mud. De Função** | **String** | **2** | **3** | **PFHSTFCO.MOTIVO** |
| **Código da Função** | **String** | **10** | **4** | **PFHSTFCO.CODFUNCAO** |
| Nível Salarial | String | 10 | 5 | PFHSTFCO.CODFAIXA |
| Faixa Salarial | String | 10 | 6 | PFHSTFCO.CODNIVEL |
