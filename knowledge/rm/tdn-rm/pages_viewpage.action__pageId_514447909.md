---
content_hash: bc76f511cf0a5208383c91c651965a9bed04a10d3a9bcd8e643d174e32109dc1
fetched_at: '2026-06-29T00:10:26.716622+00:00'
page_id: '514447909'
product: rm
source: tdn-rm
title: Layout Para Importação de Histórico da Categoria eSocial (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=514447909
version: 4
---

**Importante:**  
Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
**Campos obrigatórios estão destacados em negrito.**  
DELIMITADOR DE CAMPOS: ";"  
Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
As tabelas abaixo são premissas para a importação, caso as mesmas estejam vinculadas a tabela de Histórico da categoria eSocial da base de origem:  
- PFUNC  
  
   
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
| **Chapa do funcionário** | **String** | **16** | **1** | **PFHSTCATEGORIAESOCIAL.CHAPA** |
| **Data de mudança (ddmmaaaa hh:mm:ss)** | **Data** | **17** | **2** | **PFHSTCATEGORIAESOCIAL.DTMUDANCA** |
| **Código****da categoria eSocial** | **Inteiro** | **3** | **3** | **PFHSTCATEGORIAESOCIAL.CODCATEGORIAESOCIAL** |
