---
content_hash: 56f5ddaa12db5abe74988f48654af5b7f00e8a3f18dec9f968ff88a457e71e19
fetched_at: '2026-06-29T00:10:06.651891+00:00'
page_id: '452719325'
product: rm
source: tdn-rm
title: Layout para importação Valores pagos a pensão de Dependentes (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719325
version: 1
---

**Layout para importação Valores pagos a pensão de Dependentes (Versão 12.1)**

---

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
  | **Chapa** | **String** | **16** | **1** | **PFDEPEND.CHAPA** |
  | **Número do Dependente** | **Inteiro** | **2** | **2** | **PFDEPEND.NRODEPEND** |
  | **Sexo** | **String** | **20** | **3** | **PFDEPEND.SEXO** |
  | **Grau de Parentesco** | **Inteiro** | **1** | **4** | **PFDEPEND.GRAUPARENTESCO** |
  | **Estado Civil** | **String** | **10** | **5** | **PFDEPEND.ESTADOCIVIL** |
  | **Mês de Competência** | **Inteiro** | **2** | **6** | **PFFINANC.MESCOMP** |
  | **Ano de Competência** | **Inteiro** | **4** | **7** | **PFFINANC.ANOCOMP** |
  | **Número do período** | **Inteiro** | **2** | **8** | **PFFINANC.NROPERIODO** |
  | Mês Caixa | Inteiro | 2 | **9** | PFDEPEND. |
  | Tipo de Movimento da Pensão | Inteiro | 1 | **10** | PFDEPEND.TIPOPENSAO |
  | Valor (formato 999999999999,99) | Real | 15 | **11** | PFDEPEND.VALOR |
  | Valor Original (formato 999999999999,99) | Real | 15 | **12** | PFDEPEND.VALOROROGINAL |
  | Indicativo de alteração manual | Inteiro | 1 | **13** | NULL |
