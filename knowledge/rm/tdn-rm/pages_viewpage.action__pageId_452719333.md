---
content_hash: 5418750ceabcc242c78601c657c14832875e1fce1062dc172007b64cfc675220
fetched_at: '2026-06-29T00:10:06.720676+00:00'
page_id: '452719333'
product: rm
source: tdn-rm
title: Layout Para Importação de Linhas de Vale Transporte (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719333
version: 2
---

**Importante:**  
 **Campos em** **vermelho** **foram inseridos nos arquivos de uma versão para outra.**  
 **Campos obrigatórios estão destacados em negrito.**  
 **DELIMITADOR DE CAMPOS: ";"**   
 **Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:**  
 **Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".**  
   
  **Atenção!Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:**  
 **-  0 (zero) ou 1(um) em campos do tipo Booleano;**  
 **-  Números (00) em campos do tipo Inteiro;**  
 **-  Números com vírgulas ou Pontos (0,00 ou 0.00) em campos do tipo Real;**  
 **- (ddmmyyyy) em campos do tipo Data;**  
 **- (GRR20071514) em campos do tipo String;**  
 **- Começam /@ e terminam com @/ em campos do tipo MEMO.**  
 **Para o caso de importação de históricos a data da mudança deve sempre ser informada. Caso este campo não seja informado, o registro em questão não será importado.**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Descrição** | **Tipo** | **Posição** | **Tamanho** | **Campo** |
| **Código** | **String** | **1** | **20** | **PVALETR.CODIGO** |
| Descrição da linha Transporte | String | 2 | 50 | PVALETR.NOMELINHA |
| **Código da Tarifa** | **String** | **3** | **3** | **PVALETR.CODTARIFA** |
| Grupo de Transporte | String | 4 | 2 | PVALETR.GRUPOTRANSP |
| Tipo de Transporte:   B-Barca   I-Integração   M-Metrô   N-Bonde   O-Ônibus   T-Trem | String | 5 | 2 | PVALETR.TIPOTRANSP |
| Código do Itinerário | String | 6 | 5 | PVALETR.CODITINERARIO |
| Apenas um Vale Transporte:   0- Não   1- Sim | Inteiro | 7 | 1 | PVALETR.UNICO |
| Ativo | Inteiro | 8 | 2 | PVALETR.ATIVO |
