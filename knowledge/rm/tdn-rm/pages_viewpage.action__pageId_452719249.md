---
content_hash: 5b3069f46993663daf817674cc0ed1b24c5e90850cc02f799a9449e5381935a5
fetched_at: '2026-06-29T00:10:04.780024+00:00'
page_id: '452719249'
product: rm
source: tdn-rm
title: Layout para importação de linha do vale transporte (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719249
version: 1
---

**Layout para importação de linha do vale transporte (Versão 12.1)**   
 **Importante:**  
Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
**Campos obrigatórios estão destacados em negrito.**  
DELIMITADOR DE CAMPOS: ";"   
Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
   
 **Atenção!** Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:  
-  0 (zero) ou 1 (um) em campos do tipo **Booleano**;  
-  Números (00) em campos do tipo **Inteiro**;  
-  Números com vírgulas ou Pontos (0,00 ou 0.00) em campos do tipo **Real**;

* (ddmmyyyy), em campos do tipo **Data**;
* (GRR20071514), em campos do tipo **String**;
* Começam /@ e terminam com @/ em campos do tipo **MEMO**.  
  Para o caso de importação de históricos a data da mudança deve sempre ser informada. Caso este campo não seja informado, o registro em questão não será importado.  

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  | **DESCRIÇÃO** | **TIPO** | **TAMANHO** | **Posição** | **CAMPO** |
  | Chapa | String | 16 | 1 | PFVALETR.CHAPA |
  | Nº de Viagens | Inteiro | 2 | 2 | PFVALETR.NROVIAGENS |
  | Nº de viagens de meio Expediente | Inteiro | 2 | 3 | PFVALETR.NROVIAGMEIOEXP |
  | **Código da Linha** | **String** | **20** | **4** | **PFVALETR.CODLINHA** |
  | **Data início de uso da linha** | **Data** | **8** | **5** | **PFVALETR.DTINICIO** |
  | Data final de uso da linha | Data | 8 | 6 | PFVALETR.DTFIM |
