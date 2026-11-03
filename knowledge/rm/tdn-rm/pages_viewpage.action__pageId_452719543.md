---
content_hash: adcba5c08e6f65bc39c5bc73a591cc75f25d61c90a1af68a8a33776e8b787325
fetched_at: '2026-06-29T00:10:08.593582+00:00'
page_id: '452719543'
product: rm
source: tdn-rm
title: Layout Para Importação de Observações Contratuais do Funcionário(Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719543
version: 3
---

**Importante:**  
Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
**Campos obrigatórios estão destacados em negrito.**  
DELIMITADOR DE CAMPOS: ";"   
Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
A tabela abaixo é premissa para a importação tabela de Controle de Substituição:  
- PFUNC  
   
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
| ID | Inteiro | 10 | 1 | PFUNCOBSERVACAO.ID |
| Chapa do funcionário | Inteiro | 16 | 2 | PFUNCOBSERVACAO.CHAPA |
| Observação | String | 255 | 3 | PFUNCOBSERVACAO.OBSERVACAO |

**Atenção:** O campo ID  deve ser número sequêncial .
