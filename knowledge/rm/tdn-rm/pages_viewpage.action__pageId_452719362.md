---
content_hash: 6409a3144ec468986bcbeb2978f9133e5460ff6624dbb3558701a1d59c1f3c1e
fetched_at: '2026-06-29T00:10:07.078067+00:00'
page_id: '452719362'
product: rm
source: tdn-rm
title: Layout Para Importação de Histórico de Endereço (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719362
version: 2
---

**Importante:**  
 Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
 **Campos obrigatórios estão destacados em negrito.**  
 DELIMITADOR DE CAMPOS: ";"  
 Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
 Entre ponto virgula ( **;;** ) "Correspondendo um campo NULL".  
 As tabelas abaixo são premissas para a importação, caso as mesmas estejam vinculadas a tabela de Histórico de Endereço da base de origem:  
 - PFUNC  
 - DTIPORUA  
 - GETD  
    
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
| **DESCRIÇÃO** | **TIPO** | **TAMANHO** | **Posição** | **CAMPO** |
| **Chapa do Funcionário** | **String** | **16** | **1** | **PFUNC.CHAPA** |
| **Data da mudança (dd/mm/aaaa hh:mm:ss)** | **Data** | **17** | **2** | **PFHSTEND.DTMUDANCA** |
| Rua | String | 140 | 3 | PFHSTEND.RUA |
| Número | String | 8 | 4 | PFHSTEND.NUMERO |
| Complemento | String | 60 | 5 | PFHSTEND.COMPLEMENTO |
| Bairro | String | 80 | 6 | PFHSTEND.BAIRRO |
| **Estado** | **String** | **2** | **7** | **PFHSTEND.ESTADO** |
| Cidade | String | 32 | 8 | PFHSTEND.CIDADE |
| CEP | String | 9 | 9 | PFHSTEND.CEP |
| País | String | 60 | 10 | PFHSTEND.PAIS |
| Telefone | String | 15 | 11 | PFHSTEND.TELEFONE |
| Telefone (Opção II) | String | 15 | 12 | PFHSTEND.TELEFONE2 |
| Telefone (Opção III) | String | 15 | 13 | PFHSTEND.TELEFONE3 |
| Fax | String | 15 | 14 | PFHSTEND.FAX |
| Cod. Tipo Rua | Inteiro | 2 | 15 | PFHSTEND.CODTIPORUA |
| Código da Pessoa | Inteiro | 4 | 16 | PFHSTEND.CODPESSOA |
