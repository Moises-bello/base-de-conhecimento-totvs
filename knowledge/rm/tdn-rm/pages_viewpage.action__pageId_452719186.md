---
content_hash: e71722355f844cade983ef62483e3fc201f5bcb355dac8d8b6c43a6dd828b33a
fetched_at: '2026-06-29T00:10:04.024419+00:00'
page_id: '452719186'
product: rm
source: tdn-rm
title: Layout Para Importação de Códigos Fixos do Funcionário (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719186
version: 2
---

**Importante:**  
 Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
 **Campos obrigatórios estão destacados em negrito.**  
 DELIMITADOR DE CAMPOS: ";"   
 Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
 Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
 A tabela abaixo é premissa para a importação de Códigos Fixos do Funcionário;  
 - PFUNC  
    
  **Atenção!** Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:  
 -  0 (zero) ou 1 (um) em campos do tipo **Booleano**;  
 -  Números (00) em campos do tipo **Inteiro**;  
 -  Números com vírgulas ou Pontos (0,00 ou 0.00) em campos do tipo **Real**;

* (ddmmyyyy), em campos do tipo **Data**;
* (GRR20071514), em campos do tipo **String**;
* Começam /@ e terminam com @/ em campos do tipo **MEMO**.  
   Para o caso de importação de históricos a data da mudança deve sempre ser informada. Caso este campo não seja informado, o registro em questão não será importado.

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  | **Descrição** | **Tipo** | **Tamanho** | **Posição** | **Campo** |
  | **Chapa** | **String** | **16** | **1** | **PFCODFIX.CHAPA** |
  | **Código do Evento** | **String** | **4** | **2** | **PFCODFIX.CODEVENTO** |
  | Valor | Real | 15 | 3 | PFCODFIX.VALOR |
  | **Número de vezes** | **Inteiro** | **3** | **4** | **PFCODFIX.NROVEZES** |
  | **Tipo** | **Inteiro** | **2** | **5** | **PFCODFIX.TIPO** |
  | Mes inicial do código fixo | Inteiro | 2 | 6 | PFCODFIX.MESINICIO |
  | Ano inicial do código fixo | Inteiro | 2 | 7 | PFCODFIX.ANOINICIO |
  | Mes final do código fixo | Inteiro | 2 | 8 | PFCODFIX.MESFIM |
  | Ano final do código fixo | Inteiro | 2 | 9 | PFCODFIX.ANOFIM |
