---
content_hash: fff5a881a4e05d88e8c535483c7625b3993157b4af55a0e44a8e47a53ef69cd4
fetched_at: '2026-06-29T00:11:10.022886+00:00'
page_id: '641155465'
product: rm
source: tdn-rm
title: Dados Benefício
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=641155465
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
| Tipo do benefício | string | 4 | 4 | TIPOBENEFICIO |
| Data de início do benefício | Data | 8 | 5 | DATAINICIOBENEFICIO |
| Data da concessão do benefício | Data | 8 | 6 | DATACONCESSAOBENEFICIO |
| Situação do benefício | Inteiro | 2 | 7 | SITUACAOBENEFICIO |
| Tipo de plano de segregação da massa | Inteiro | 2 | 8 | TIPOPLANOSEGREGACAOMASSA |
| Descrição da situação que originou o pagamento do benefício | string | 255 | 9 | DESCRICAOORIGEMBENEFICIO |
| Informa se o benefício foi concedido por determinação judicial | Inteiro | 2 | 10 | BENEFICIODETERMINACAOJUDICIAL |
| Tipo de pensão por morte | Inteiro | 2 | 11 | TIPOPENSAOMORTE |
| CPF do instituidor da pensão por morte | string | 15 | 12 | CPFINSTITUIDORPENSAOMORTE |
| Data de óbito do instituidor da pensão por morte | Data | 8 | 13 | DTOBITOINSTITUIDORPENSAOMORTE |
| Suspensão do benefício | Inteiro | 2 | 14 | SUSPENSAOBENEFICIO |
| Término do benefício | Inteiro | 2 | 15 | TERMINOBENEFICIO |
