---
content_hash: 33399072770d8eb045f6981a957cba4c63e1a1f9c87f76029cc455ce6ece62c6
fetched_at: '2026-06-29T00:11:54.097958+00:00'
page_id: '853287523'
product: rm
source: tdn-rm
title: Dados do Residente ou Domiciliado no Exterior do Autônomo Externo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=853287523
version: 8
---

**IMPORTANTE:**

* Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.
* **Campos obrigatórios estão destacados em negrito.**
* DELIMITADOR DE CAMPOS: ";"
* Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
  Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".

**OBSERVAÇÃO:**

* Código Pagamento dos Autônomos Externos deverá ser associado ao campo código da tabela pai (PPAGTOAUTONOMOEXT.CODIGO)****.****

**ATENÇÃO:** Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:

* 0 (zero) ou 1 (um) em campos do tipo **Booleano**;
* Números (00) em campos do tipo **Inteiro**;
* Números com vírgulas ou pontos (0,00 ou 0.00) em campos do tipo **Real**;
* (DDMMYYYY) em campos do tipo **Data**;
* (GRR20071514) em campos do tipo **String**;
* Começam /@ e terminam com @/ em campos do tipo **MEMO**.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Descrição** | **Tipo** | **Tamanho** | **Posição** | **Campo** |
| **Código Pagamento dos Autônomos Externos** | **Inteiro** | **6** | **1** | **PPAGTOAUTONOMOEXTRESIDEXTERIOR.CODIGOPAGTO** |
| **Código do País de Endereço (conforme tabela 06 do eSocial)** | **Inteiro** | **2** | **2** | **PPAGTOAUTONOMOEXTRESIDEXTERIOR.IDPAISEXTERIOR** |
| Logradouro do endereço | String | 80 | 3 | PPAGTOAUTONOMOEXTRESIDEXTERIOR.LOGRADOURO |
| Número do endereço | String | 10 | 4 | PPAGTOAUTONOMOEXTRESIDEXTERIOR.NUMERO |
| Complemento do endereço | String | 30 | 5 | PPAGTOAUTONOMOEXTRESIDEXTERIOR.COMPLEMENTO |
| Bairro do endereço | String | 60 | 6 | PPAGTOAUTONOMOEXTRESIDEXTERIOR.BAIRRO |
| Cidade do endereço | String | 40 | 7 | PPAGTOAUTONOMOEXTRESIDEXTERIOR.CIDADE |
| Estado do endereço | String | 40 | 8 | PPAGTOAUTONOMOEXTRESIDEXTERIOR.ESTADO |
| Código Postal do endereço | String | 12 | 9 | PPAGTOAUTONOMOEXTRESIDEXTERIOR.CODIGOPOSTAL |
| Telefone | String | 15 | 10 | PPAGTOAUTONOMOEXTRESIDEXTERIOR.TELEFONE |
| Indicativo NIF (Valores válidos 1, 2 e 3) | Inteiro | 1 | 11 | PPAGTOAUTONOMOEXTRESIDEXTERIOR.INDICATIVONIF |
| NIF | String | 30 | 12 | PPAGTOAUTONOMOEXTRESIDEXTERIOR.NIF |
| Forma de Tributação (conforme tabela 30 do eSocial) | String | 2 | 13 | PPAGTOAUTONOMOEXTRESIDEXTERIOR.FORMATRIBUTACAO |

**ATENÇÃO:** Liberado a partir das versões informadas no
