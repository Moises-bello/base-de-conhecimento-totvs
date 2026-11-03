---
content_hash: 5658522cf3edfb0435a342f9c154027abf848e62c0b3baed2ef79501c8853beb
fetched_at: '2026-06-29T00:10:04.700660+00:00'
page_id: '452719236'
product: rm
source: tdn-rm
title: Layout Para Importação Histórico Indicador de Contribuição Substituída (Versão
  12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719236
version: 2
---

**Importante:**  
 **Campos em vermelho foram inseridos nos arquivos de uma versão para outra.**  
 **Campos obrigatórios estão destacados em negrito.**  
 **DELIMITADOR DE CAMPOS: ";"**  
 **Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:**  
 **Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".**  
 **As tabelas abaixo são premissas para a importação, caso as mesmas estejam vinculadas a tabela de Histórico de Função da base de origem:**  
 **- PFUNC**  
 **- PFUNCAO**  
 **- PMOTMUDFUNCAO**  
   
  **Atenção!  Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:**  
 **-  0 (zero) ou 1(um) em campos do tipo Booleano;**  
 **-  Números (00) em campos do tipo Inteiro;**  
 **-  Números com vírgulas ou Pontos (0,00 ou 0.00) em campos do tipo Real;**  
 **- (ddmmyyyy) em campos do tipo Data;**  
 **- (GRR20071514) em campos do tipo String;**  
 **- Começam /@ e terminam com @/ em campos do tipo MEMO.**  
 **Para o caso de importação de históricos a data da mudança deve sempre ser informada. Caso este campo não seja informado, o registro em questão não será importado.**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **DESCRIÇÃO** | **TIPO** | **TAMANHO** | **Posição** | **CAMPO** |
| **Chapa** | **String** | **16** | **1** | **PFHSTINDSIMPLES.CHAPA** |
| **Data da Mudança (ddmmaaaa**   **hh:mm:ss)** | **Data** | **17** | **2** | **PFHSTINDSIMPLES.DTMUDANCA** |
| **Código do Indicador de Contribuição Substituída** | **String** | **1** | **3** | **PFHSTINDSIMPLES.CODIGO** |
