---
content_hash: b08f7f8fac5d2a4da8e12ebbf3ab3949fe8fade0ec6494deab8a2261fbe9426f
fetched_at: '2026-06-29T00:10:04.565568+00:00'
page_id: '452719219'
product: rm
source: tdn-rm
title: Layout Para Importação de Incidências de Médias nos Evento (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719219
version: 2
---

**Importante:**  
 Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
 **Campos obrigatórios estão destacados em negrito.**  
 DELIMITADOR DE CAMPOS: ";"   
 Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
 Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
 A tabela abaixo é premissa para a importação de Incidência de Média nos Eventos:  
 - PEVENTO  
    
  **Atenção!** Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:  
 -  0 (zero) ou 1(um) em campos do tipo **Booleano**;  
 -  Números (00) em campos do tipo **Inteiro**;  
 -  Números com vírgulas ou Pontos (0,00 ou 0.00) em campos do tipo **Real**;

* (ddmmyyyy) em campos do tipo **Data**;
* (GRR20071514) em campos do tipo **String**;
* Começam /@ e terminam com @/ em campos do tipo **MEMO**.  
   Para o caso de importação de históricos a data da mudança deve sempre ser informada. Caso este campo não seja informado, o registro em questão não será importado.

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  | **Descrição** | **Tipo** | **Tamanho** | **Posição** | **Campo** |
  | **Código do Evento** | **String** | **4** | **1** | **PEVTMED.CODEVENTO** |
  | **Tipo da Média**       **(1- Incide Férias**       **2 - 13º Salário Rescisão**       **3-Aviso Prévio**       **4-Licença Maternidade**       **5 – 13º Salário**       **6 – Férias na Rescisão)** | **Inteiro** | **1** | **2** | **PEVTMED.TIPOMEDIA** |
  | Grupo (Valor de estar entre 0 e 49) | Inteiro | 1 | 3 | PEVTMED.GRUPO |
  | Evento de Último Valor? (0 - Não/ 1 - Sim) | Inteiro | 1 | 4 | PEVTMED.UTIMOVALOR |
