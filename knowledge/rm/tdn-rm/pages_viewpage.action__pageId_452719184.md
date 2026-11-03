---
content_hash: c30edb365a0958063437914c3c061f34b458a5c236ceb39e5d8aab88415fc589
fetched_at: '2026-06-29T00:10:04.009159+00:00'
page_id: '452719184'
product: rm
source: tdn-rm
title: Layout Para Importação de Controle de Substituição (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719184
version: 2
---

**Importante:**  
 Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
 **Campos obrigatórios estão destacados em negrito.**  
 DELIMITADOR DE CAMPOS: ";"   
 Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
 Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
 A tabela abaixo é premissa para a importação tabela de Controle de Substituição:  
 - PFUNC  
 **Observação:** O sistema possui uma regra onde caso importe um registro já existente na base, os campos NROHORAS e NROHORASORIGINAL serão somados com os valores já existentes.  
    
  **Atenção!** Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:  
 -  0 (zero) ou 1(um) em campos do tipo **Booleano**;

-  Números (00) em campos do tipo **Inteiro**;

-  Números com vírgulas ou Pontos (0,00 ou 0.00) em campos do tipo **Real**;

-  (ddmmyyyy) em campos do tipo **Data**;

-  (GRR20071514) em campos do tipo **String**;

-  Começam /@ e terminam com @/ em campos do tipo **MEMO**.  
 Para o caso de importação de históricos a data da mudança deve sempre ser informada. Caso este campo não seja informado, o registro em questão não será importado.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **DESCRIÇÃO** | **TIPO** | **TAMANHO** | **POSIÇÃO** | **CAMPO** |
| **Chapa do funcionário** | **String** | **16** | **1** | **PFSUBSTITUICAO.CHAPA** |
| **Ano da Substituição** | **Inteiro** | **4** | **2** | **PFSUBSTITUICAO.ANOCOMP** |
| **Mês da Substituição** | **Inteiro** | **2** | **3** | **PFSUBSTITUICAO.MESCOMP** |
| **Código da Função Substituída** | **String** | **10** | **4** | **PFSUBSTITUICAO.CODFUNCAO** |
| Código da Faixa Salarial Substituída | String | 10 | 5 | PFSUBSTITUICAO.CODGRUPOSAL |
| Chapa do Funcionário Substituída | String | 16 | 6 | PFSUBSTITUICAO.CHAPASUBST |
| Número de horas (Formato HHH:MM) | String | 6 | 7 | PFSUBSTITUICAO.NROHORAS |
| Número de horas original   (Formato HHH:MM) | String | 6 | 8 | PFSUBSTITUICAO.NROHORASORIGINAL |
| Nível Salarial | String | 10 | 9 | PFSUBSTITUICAO.CODNIVELSAL |
| Seção | String | 35 | 10 | PFSUBSTITUICAO.CODSECAO |
