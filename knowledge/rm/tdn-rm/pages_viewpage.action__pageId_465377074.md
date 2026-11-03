---
content_hash: 9095a7d623aa5e90e4148ed693336e00b46006787e267f532c6e8d5bc69a2c98
fetched_at: '2026-06-29T00:10:15.839081+00:00'
page_id: '465377074'
product: rm
source: tdn-rm
title: Layout Para Importação de Histórico de Nº de Dependentes (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=465377074
version: 1
---

Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.

**Campos obrigatórios estão destacados em negrito.**

DELIMITADOR DE CAMPOS: ";"

Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:

Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".

A tabela abaixo é premissa para a importação de Histórico de Número de Dependentes

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
| **DESCRIÇÃO** | **TIPO** | **TAMANHO** | **Posição** | **CAMPO** |
| **Chapa do funcionário** | **String** | **16** | **1** | **PFHSTNDP.CHAPA** |
| **Data de mudança (ddmmaaaa hh:mm:ss)** | **Data** | **17** | **2** | **PFHSTNDP.DTMUDANCA** |
| Número de dep. que incidem no IRRF | Inteiro | 2 | 3 | PFHSTNDP.NRODEPENDIRRF |
| Número de dependentes de salário família | Inteiro | 2 | 4 | PFHSTNDP.NRODEPENDSALFAM |
