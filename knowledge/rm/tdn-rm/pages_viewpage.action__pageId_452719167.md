---
content_hash: 84352c7043386bb5a8cd4e60e5d65d102199169f88d41db32d4c966d48939654
fetched_at: '2026-06-29T00:10:03.873910+00:00'
page_id: '452719167'
product: rm
source: tdn-rm
title: Layout Para Importação de Fórmulas (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719167
version: 4
---

**Tela Principal Layout**  
 **Importante:**  
**Campos em****vermelho****foram inseridos nos arquivos de uma versão para outra.**  
**Campos obrigatórios estão destacados em negrito.**  
**DELIMITADOR DE CAMPOS: ";"**  
**Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:**  
**Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".**  
  
 **Atenção! Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:**  
**-  0 (zero) ou 1(um) em campos do tipo Booleano;**  
**-  Números (00) em campos do tipo Inteiro;**  
**-  Números com vírgulas ou Pontos (0,00 ou 0.00) em campos do tipo Real;**  
**- (ddmmyyyy) em campos do tipo Data;**  
**- (GRR20071514) em campos do tipo String;**  
**- Começam --- e terminam com --- em campos do tipo MEMO.**  
**Para o caso de importação de históricos a data da mudança deve sempre ser informada. Caso este campo não seja informado, o registro em questão não será importado.**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Descrição** | **Tipo** | **Tamanho** | **Posição** | **Campo** |
| **Código** | **String** | **08** | **1** | **GFORMULA.CODIGO** |
| Título | String | 70 | 2 | GFORMULA.TITULO |
| Crítica Global (0-Não / 1-Sim) | Inteiro | 01 | 3 | GFORMULA.CRITICAGLOBAL |
| Indicador de Fórmula de Seleção (0-Não / 1-Sim) | Inteiro | 01 | 4 | GFORMULA.INDSELECAO |
| Número de Decimais | Inteiro | 02 | 5 | GFORMULA.NUMERODECIMAIS |
| Grupo | String | 01 | 6 | GFORMULA.GRUPO |
| Texto (começa com --- e termina com ---) | Memo |  | 7 | GFORMULA.TEXTO |
