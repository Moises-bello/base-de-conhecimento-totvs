---
content_hash: 73c634104d51f91ca7be9b65134357864640e7ea52203e9fa113f6b97b80cd5a
fetched_at: '2026-06-29T00:10:05.380234+00:00'
page_id: '452719286'
product: rm
source: tdn-rm
title: Layout Para Importação de Centros de Custos (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719286
version: 2
---

Tela Principal Layout  
    **Importante:**  
 Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
 **Campos obrigatórios estão destacados em negrito.**  
 DELIMITADOR DE CAMPOS: ";"  
 Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
 Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
 A tabela abaixo é premissa para a importação, caso a mesma esteja vinculada a tabela de centro de custo da base de origem:  
 - VGRUPOOCUPACIONAL  
    
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
| **Código** | **String** | **25** | **1** | **PCCUSTO.CODCUSTO** |
| Código do Centro de Custo Global | String | 25 | 2 | PCCUSTO.CODCCGLOBAL |
| Nome | String | 40 | 3 | PCCUSTO.NOME |
| Campo Vazio (UTILIZE ";;") |  |  | 2 | 4 |
| Campo Vazio (UTILIZE ";;") |  |  | 22 | 5 |
| Rua | String | 32 | 6 | PCCUSTO.RUA |
| Número | String | 8 | 7 | PCCUSTO.NUMERO |
| Complemento | String | 20 | 8 | PCCUSTO.COMPLEMENTO |
| Bairro | String | 20 | 9 | PCCUSTO.BAIRRO |
| Cidade | String | 32 | 10 | PCCUSTO.CIDADE |
| Estado | String | 2 | 11 | PCCUSTO.ESTADO |
| CEP | String | 9 | 12 | PCCUSTO.CEP |
| Código do INSS | String | 22 | 13 | PCCUSTO.CODINSS |
| Código de Terceiros | String | 4 | 14 | PCCUSTO.CODTERCINSS |
| Complemento da Guia | String | 120 | 15 | PCCUSTO.COMPLEMENTO\_GUIA |
| Percentual de Terceiros (Formato 99999,99) | Real | 8 | 16 | PCCUSTO.PERC\_TERC |
| Cód. Da Integração Contábil | String | 22 | 17 | PCCUSTO.INTGRCONTABIL |
| Cód. Da Integração Gerencial | String | 22 | 18 | PCCUSTO.INTGRGERENCIAL |
| Número da Filial Contábil | Inteiro | 7 | 19 | PCCUSTO.NUMEROFILIALCONTAB |
| Campo Vazio (UTILIZE ";;") |  |  | 15 | 20 |
| Contribui para SESI/SENAI (0-Não/1-Sim) | Inteiro | 1 | 21 | PCCUSTO.CONTRIBUISESI\_SENAI |
| Percentual de Acidente de Trabalho (Formato 99999,99) | Real | 8 | 22 | PCCUSTO.PERC\_ACTRAB |
| Código de Departamento Contábil | String | 7 | 23 | PCCUSTO.CODDEPTOCONT |
| Centro de Custo Ativo | Booleano | 1 | 24 | PCCUSTO.ATIVO |
| Permite Lançamento | Booleano | 1 | 25 | PCCUSTO.PERMITELANC |
