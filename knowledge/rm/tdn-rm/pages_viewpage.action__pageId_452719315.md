---
content_hash: 5c8076e4d4e266c712160a442e6cf3cf46e6f61c7f25de29fe9b088e7443201e
fetched_at: '2026-06-29T00:10:06.559477+00:00'
page_id: '452719315'
product: rm
source: tdn-rm
title: Layout Para Importação do Movimento do Centro de Custo (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719315
version: 5
---

**Importante:**

Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
 **Campos obrigatórios estão destacados em negrito.**  
 DELIMITADOR DE CAMPOS: ";"   
 Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
 Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
 As tabelas abaixo são premissas para a importação, caso as mesmas estejam vinculadas a tabela de Movimento do Centro de Custo da base de origem:  
 - PFUNC  
 - PFPERFF  
 - PFFINANC  
 **Observação:** Não é permitido a importação para o período corrente.  
    
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
  | **Chapa** | **String** | **16** | 1 | **PFMOVCC.CHAPA** |
  | **Ano de Competência** | **Inteiro** | **4** | 2 | **PFMOVCC.ANOCOMP** |
  | **Mês de Competência** | **Inteiro** | **2** | 3 | **PFMOVCC.MESCOMP** |
  | **Nº do Período** | **Inteiro** | **2** | 4 | **PFMOVCC.NROPERIODO** |
  | **Código do Evento** | **String** | **4** | 5 | **PFMOVCC.CODEVENTO** |
  | Hora (Formato HHH: MM) | String | 6 | 6 | PFMOVCC.HORA |
  | Referência (Formato 999,99) | Real | 9 | 7 | PFMOVCC.REF |
  | Valor (Formato 999999,99) | Real | 9 | 8 | PFMOVCC.VALOR |
  | **Centro de Custo** | **String** | **25** | 9 | **PFMOVCC.CODCCUSTO** |
  | Flag de Evento Digitado/Importado | Inteiro | 2 | 10 | PFMOVCC.EDITADO |
  | Origem do Movimento | Inteiro | 2 | 11 | PFMOVCC.ORIGEMMOV |

 **Atenção!** Caso, possua dúvidas sobre o preenchimento correto do dados que serão inseridos nos campos, segue a baixo o exemplo:

Cada linha do arquivo deve possuir o formato descrito a seguir:

SSSSS\*\*\*\*\*\*\*\*\*\*\*;0000;00;00;0000;000:00;000,00;000000,00;\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*0.0.0;00;00;

* S representa um valor de string.
* Asterisco \* representa um espaço em branco.
* 0 representa um valor numérico obrigatório.

Caso o valor da chapa tenha o número de caracteres menor que 16, complete o restante do caracteres com espaços em branco a direita.

Caso o valor do centro de custo tenha o número de caracteres menor que 25, complete o restante do caracteres com espaços em branco a esquerda.
