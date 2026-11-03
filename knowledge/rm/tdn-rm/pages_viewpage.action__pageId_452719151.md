---
content_hash: b0983a553d3d29585bd58afe1a27ee85032904e423c6bc8c520439ecb66596c8
fetched_at: '2026-06-29T00:10:03.741665+00:00'
page_id: '452719151'
product: rm
source: tdn-rm
title: Layout Para Importação de Verbas de Férias (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719151
version: 3
---

**Importante:**  
Campos em vermelho foram inseridos nos arquivos de uma versão para outra.  
Campos obrigatórios estão destacados em negrito.  
DELIMITADOR DE CAMPOS: ";"  
Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
A tabela abaixo é premissa para a importação, caso a mesma esteja vinculada a tabela de Verbas de Férias da base de origem:  
PFUFERIASRECIBO

**Atenção!**

Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:

* 0 (zero) ou 1(um) em campos do tipo Booleano;
* Números (00) em campos do tipo Inteiro;
* Números com vírgulas ou Pontos (0,00 ou 0.00) em campos do tipo Real;
* (ddmmyyyy) em campos do tipo Data;
* (GRR20071514) em campos do tipo String;
* Começam /@ e terminam com @/ em campos do tipo MEMO.
* (HHH:mm) em campos do tipo **Hora**.

Para o caso de importação de históricos a data da mudança deve sempre ser informada. Caso este campo não seja informado, o registro em questão não será importado.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Descrição** | **Tipo** | **Tamanho** | **Posição** | **Campo** |
| **Chapa do Funcionário** | **String** | **16** | **1** | **PFUFERIASVERBAS.CHAPA** |
| **Data final do período aquisitivo** | **Data** | **8** | **2** | **PFUFERIASVERBAS.FIMPERAQUIS** |
| **Data de pagamento das férias** | **Data** | **8** | **3** | **PFUFERIASVERBAS.DATAPAGTO** |
| **Código do evento** | **String** | **4** | **4** | **PFUFERIASVERBAS.CODEVENTO** |
| Quantidade de hora do evento | Hora | 6 | 5 | PFUFERIASVERBAS.HORA |
| Valor referência do evento | Real | 9 | 6 | PFUFERIASVERBAS.REF |
| Valor da verba | Real | 9 | 7 | PFUFERIASVERBAS.VALOR |
| Ind. de evento alterado pelo usuário | Booleano | 2 | 8 | PFUFERIASVERBAS.ALTERADOMANUAL |
