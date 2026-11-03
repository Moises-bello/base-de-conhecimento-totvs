---
content_hash: c72e0508d2afc224ca613b59fbfb8081f62080422cd98b9f56b6f4ab9bddfcaf
fetched_at: '2026-06-29T00:11:10.030665+00:00'
page_id: '641155479'
product: rm
source: tdn-rm
title: Dados Benefício Suspensão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=641155479
version: 2
---

**Importante:**  
Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
**Campos obrigatórios estão destacados em negrito.**  
DELIMITADOR DE CAMPOS: ";"  
Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
**Observação:** O Código da pessoa solicitante da anotação poderá não ser o mesmo na coligada destino, caso isso ocorra, deverá ser feito de/para.  
A tabela abaixo é premissa para a importação de Anotações de Funcionário;  
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
| **Descrição** | **Tipo** | **Tamanho** | **Posição** | **Campo** |
| Código Identificador da Coligada | string | 2 | 1 | CODCOLIGADA |
| Chapa do Funcionário | string | 16 | 2 | CHAPA |
| Número do benefício | string | 20 | 3 | NUMEROBENEFICIO |
| Data da suspensão do benefício | Data | 8 | 4 | DATASUSPENSAOBENEFICIO |
| Tipo de suspensão do benefício | Inteiro | 2 | 5 | TIPOSUSPENSAO |
| Motivo da suspensão do benefício | string | 2 | 6 | MOTIVOSUSPENSAOBENEFICIO |
| Descrição do motivo da suspensão do benefício | string | 255 | 7 | DESCRICAOMOTIVOSUSPENSAOBENEF |
| Data da reativação do benefício | Data | 8 | 8 | DATAREATIVACAOBENEFICIO |
| Data de início dos efeitos financeiros da reativação do benefício | Data | 8 | 9 | DATAEFEITOREATIVACAOBENEFICIO |
| CNPJ do órgão público sucessor | string | 30 | 10 | CNPJORGAOSUCESSOR |
