---
content_hash: aa398b06717ebbe5466e6b73e5d5f618cb2f15dbcf749df705e7fbf5a1356307
fetched_at: '2026-06-29T00:10:04.046208+00:00'
page_id: '452719189'
product: rm
source: tdn-rm
title: Layout Para Importação de Histórico de Empréstimo (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719189
version: 3
---

**Importante:**  
Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
**Campos obrigatórios estão destacados em negrito.**  
DELIMITADOR DE CAMPOS: ";"  
Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
As tabelas abaixo são premissas para a importação, caso as mesmas estejam vinculadas a tabela de Histórico de Empréstimos da base de origem:  
- PFUNC  
- PFEMPRT  
   
 **Atenção!** Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:  
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
| **Chapa** | **String** | **16** | **1** | **PFDESCEMPRT.CHAPA** |
| **Código do empréstimo** | **Inteiro** | **20** | **2** | **PFDESCEMPRT.CODIGO** |
| **Ano Competência** | **Inteiro** | **2** | **3** | **PFDESCEMPRT.ANOCOMP** |
| **Mês Competência** | **Inteiro** | **2** | **4** | **PFDESCEMPRT.MESCOMP** |
| **Período** | **Inteiro** | **2** | **5** | **PFDESCEMPRT.NROPERIODO** |
| **Número de parcelas lançadas** | **Inteiro** | **2** | **6** | **PFDESCEMPRT.TIPO** |
| **Valor do desconto** | **Real** | **9** | **7** | **PFDESCEMPRT.VALOR** |
| Número de parcelas lançadas | Inteiro | 2 | 8 | PFDESCEMPRT.NROPARCLANCADAS |
| Valor da correção do empréstimo | Real | 9 | 9 | PFDESCEMPRT.VALORCORRECAO |
| Valor da insuficiência de saldo | Real | 9 | 10 | PFDESCEMPRT.INSUFSALDO |
