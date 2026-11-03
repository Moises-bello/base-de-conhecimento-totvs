---
content_hash: 21283b22dacd4e1ab53585774bcf56807ff0a748485c37ea636ada9b18eb5a84
fetched_at: '2026-06-29T00:10:07.088734+00:00'
page_id: '452719363'
product: rm
source: tdn-rm
title: Layout Para Importação de Histórico de Salário (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719363
version: 7
---

**Importante:**  
Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
**Campos obrigatórios estão destacados em negrito.**  
DELIMITADOR DE CAMPOS: ";"  
Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
As tabelas abaixo são premissas para a importação, caso as mesmas estejam vinculadas a tabela de Histórico de Salário da base de origem:  
- PFUNC  
- PMOTMUDSAL  
**Observação:** O campo PERCENTAPLICADO (Percentual Aplicado) poderá ser recalculado pelo sistema após a importação.  
   
 **Atenção!** Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:

-  0 (zero) ou 1(um) em campos do tipo **Booleano**;

-  Números (00) em campos do tipo**Inteiro**;

-  Números com vírgulas ou Pontos (0,00 ou 0.00) em campos do tipo **Real**;

- (ddmmyyyy hh:mm:ss) em campos do tipo **Data**;

- (GRR20071514) em campos do tipo **String**;

- Começam /@ e terminam com @/ em campos do tipo **MEMO**;

- (HHH:mm) em campos do tipo **Hora**.

Para o caso de importação de históricos a data da mudança deve sempre ser informada. Caso este campo não seja informado, o registro em questão não será importado.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **DESCRIÇÃO** | **TIPO** | **TAMANHO** | **Posição** | **CAMPO** |
| **Chapa** | **String** | **16** | **1** | **PFHSTSAL.CHAPA** |
| **Data de mudança (**ddmmaaaa hh:mm:ss**)** | **Data** | **17** | **2** | **PFHSTSAL.DTMUDANCA** |
| **Motivo de alteração salarial** | **String** | **2** | **3** | **PFHSTSAL.MOTIVO** |
| **Número do salário** | **Inteiro** | **2** | **4** | **PFHSTSAL.NROSALARIO** |
| **Valor atual do salário** | **Real** | **15** | **5** | **PFHSTSAL.SALARIO** |
| **Jornada de Trabalho (HHH:mm)** | **Hora** | **8** | **6** | **PFHSTSAL.JORNADA** |
| **Data de referência da alteração salarial (**ddmmaaaa hh:mm:ss**)** | **Data** | **17** | **7** | **PFHSTSAL.DATADEREFERENCIA** |
| Código do evento de salário | String | 4 | 8 | PFHSTSAL.CODEVENTO |
| Data da inclusão do aumento salarial | Data | 8 | 9 | PFHSTSAL.DATADEINCLUSAO |
| Alteração de Jornada? | Booleano | 2 | 10 | PFHSTSAL.ALTERACAOJORNADA |
| Percentual Aplicado | Real | 9 | 11 | PFHSTSAL.PERCENTAPLICADO |
| Historico Tabela Salarial | String | 10 | 12 | PFHSTSAL.HISTORICOTABELASALARIAL |
| Historico Faixa | String | 10 | 13 | PFHSTSAL.HISTORICODEFAIXA |
| Historico Nivel | String | 10 | 14 | PFHSTSAL.HISTORICODENIVEL |
| Identificador de executação da Alteração Global de Salário. | Inteiro | 10 | 15 | PFHSTSAL.IDAUMENTO |
| Referência | Real | 15 | 16 | PFHSTSAL.REFERENCIA |
