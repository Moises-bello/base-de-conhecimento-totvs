---
content_hash: 7e45fa22094494f74cf7101affd1bfb3ecce89f663b81ffdbefd5879177bf2d4
fetched_at: '2026-06-29T00:11:37.395096+00:00'
page_id: '777273992'
product: rm
source: tdn-rm
title: Layout para Importação do Dependente do Autônomo Externo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=777273992
version: 5
---

**Importante:**

Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
Campos obrigatórios estão destacados em **negrito.**  
DELIMITADOR DE CAMPOS: ";"   
Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:

Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".

O campo "Código Pagamento dos Autônomos Externos" deverá ser associado ao campo código da tabela pai (PPAGTOAUTONOMOEXT.CODIGO)****.****

**Atenção!**

Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:

-  0 (zero) ou 1(um) em campos do tipo **Booleano**;

-  Números (00) em campos do tipo **Inteiro**;

-  Números com vírgulas ou Pontos (0,00 ou 0.00) em campos do tipo **Real**;

-  (ddmmyyyy) em campos do tipo **Data**;

-  (GRR20071514) em campos do tipo **String**;

-  Começam /@ e terminam com @/ em campos do tipo **MEMO**.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Descrição** | **Tipo** | **Tamanho** | **Posição** | **Campo** |
| **Código Pagamento dos Autônomos Externos** | **Inteiro** | **6** | **1** | **PPAGTOAUTONOMOEXTDEPEND.CODIGOPAGTO** |
| CPF do Dependente | String | 11 | 2 | PPAGTOAUTONOMOEXTDEPEND.CPF |
| Nome do Dependente | String | 70 | 3 | PPAGTOAUTONOMOEXTDEPEND.NOME |
| Data de Nascimento do Dependente | Data | 8 | 4 | PPAGTOAUTONOMOEXTDEPEND.DTNASCIMENTO |
| Tipo de Dependente | String | 2 | 5 | PPAGTOAUTONOMOEXTDEPEND.TIPODEPENDENTE |
| Descrição do Dependente | String | 100 | 6 | PPAGTOAUTONOMOEXTDEPEND.DESCRICAODEPENDENCIA |
| Valor de Dedução | Real | 15 | 7 | PPAGTOAUTONOMOEXTDEPEND.VALORDEDUCAO |
| Valor de Dedução de Pensão | Real | 15 | 8 | PPAGTOAUTONOMOEXTDEPEND.VALORDEDUCAOPENSAO |
