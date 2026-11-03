---
content_hash: 6fc5960436b3a549a7c5da7901adbebd10e476d03edadd69122fa560d71b22f9
fetched_at: '2026-06-29T00:10:06.839517+00:00'
page_id: '452719343'
product: rm
source: tdn-rm
title: Layout Para Importação de Eventos Programados (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719343
version: 2
---

**Importante:**  
 Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
 **Campos obrigatórios estão destacados em negrito.**  
 DELIMITADOR DE CAMPOS: ";"  
 Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
 Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
 As tabelas abaixo são premissas para a importação de Eventos Programados do Funcionário;  
 - PFUNC  
 - TPEVTPROG  
    
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
| **Chapa do Funcionário** | **String** | **16** | **1** | **PFEVENTOSPROG.CHAPA** |
| **Código do Evento** | **String** | **4** | **2** | **PFEVENTOSPROG.CODEVENTO** |
| **Mês de início do lançamento** | **Inteiro** | **2** | **3** | **PFEVENTOSPROG.MESINIC** |
| **Ano de Inicio do lançamento** | **Inteiro** | **4** | **4** | **PFEVENTOSPROG.ANOINIC** |
| Mês final para lançamento | Inteiro | 2 | 5 | PFEVENTOSPROG.MESFIM |
| Ano final para lançamento | Inteiro | 4 | 6 | PFEVENTOSPROG.ANOFIM |
| Programação por tempo indeterminado | Booleano | 1 | 7 | PFEVENTOSPROG.SEMPREVALIDO |
| **Tipo de cálculo** | **Inteiro** | **2** | **8** | **PFEVENTOSPROG.TIPO** |
| Campo complementar para fins diversos | String | 30 | 9 | PFEVENTOSPROG.COMPLEMENTO1 |
| Campo complementar para fins diversos 2 | String | 30 | 10 | PFEVENTOSPROG.COMPLEMENTO2 |
| Código do Centro de Custo de lançamento | String | 25 | 11 | PFEVENTOSPROG.CODCCUSTO |
| Valor do evento a ser lançado | Real | 15 | 12 | PFEVENTOSPROG.VALOR |
