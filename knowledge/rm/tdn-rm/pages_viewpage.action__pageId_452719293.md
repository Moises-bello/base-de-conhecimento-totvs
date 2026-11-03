---
content_hash: 5bcd54b376d898871b940383f11ff5836dfe2ac626b8ded5a2301042558c9108
fetched_at: '2026-06-29T00:10:05.450308+00:00'
page_id: '452719293'
product: rm
source: tdn-rm
title: Layout Para Importação de Histórico de Afastamento (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719293
version: 5
---

**Importante:**  
Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
**Campos obrigatórios estão destacados em negrito.**  
DELIMITADOR DE CAMPOS: ";"  
Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
As tabelas abaixo são premissas para a importação, caso as mesmas estejam vinculadas a tabela de Histórico de Afastamento da base de origem:  
- PFUNC  
- PMUDSITUACAO  
- PCODAFAST  
- FCFO  
- VPROFISSIONALSAUDE  
- VCID  
   
**Observação:** Os campos CODCOLTOMADOR (Código da Coligada do Tomador) e CODTOMADOR (Código do Tomador) possuem tratamento interno no data. Pode ser que as informações desses campos fiquem diferentes na base de origem e destino.  
Para o campo DTINICONTINUIDADEAFT é necessário existir um histórico de afastamento com a data de início cadastrado ou informado no arquivo de importação. Caso não exista, o registro não será importando, informando para o usuário que a data inicial selecionada não existe para continuidade de afastamento. Este campo não é obrigatório, podendo ser informando com espaços em branco ou nulo: (; .  
   
 **Atenção!**  Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:  
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
| **Chapa** | **String** | **16** | **1** | **PFHSTAFT.CHAPA** |
| **Data de início** | **Data** | **8** | **2** | **PFHSTAFT.DTINICIO** |
| Data final | Data | 8 | 3 | PFHSTAFT.DTFINAL |
| **Tipo** | **String** | **1** | **4** | **PFHSTAFT.TIPO** |
| **Motivo do afastamento** | **String** | **2** | **5** | **PFHSTAFT.MOTIVO** |
| Observações | String | 50 | 6 | PFHSTAFT.OBSERVACAO |
| Estorna tempo de serviço | Inteiro | 1 | 7 | PFHSTAFT.ESTTEMPOSERVICO |
| Código da Coligada do Tomador | Inteiro | 2 | 8 | PFHSTAFT.CODCOLTOMADOR |
| Código do Tomador | String | 25 | 9 | PFHSTAFT.CODTOMADOR |
| Tipo do Tomador | Intero | 2 | 10 | PFHSTAFT.TPTOMADOR |
| Data de Requerimento | Data | 8 | 11 | PFHSTAFT.DATAREQUERIMENTO |
| CEI | String | 20 | 12 | PFHSTAFT.CEI |
| Codigo da Tabela CID | String | 10 | 13 | PFHSTAFT.CODCID |
| Ônus da Cessão | String | 1 | 14 | PFHSTAFT.INFOONUS |
| Código do Médico | Inteiro | 8 | 15 | PFHSTAFT.CODMEDICO |
| Tipo de Acidente de Trânsito | String | 1 | 16 | PFHSTAFT.TIPOACIDENTETRANSITO |
| Flag Acidente de Trânsito | Inteiro | 2 | 17 | PFHSTAFT.ACIDENTETRANSITO |
| CNPJ do sindicato | String | 18 | 18 | PFHSTAFT.CNPJSINDICATO |
| Informação onus da Remuneração | String | 1 | 19 | PFHSTAFT.INFOONUSREMUNERACAO |
| Código da estabilidade | Inteiro | 4 | 20 | PFHSTAFT.CODESTABILIDADE |
| Doença ou agravo de notificação compulsória | Inteiro | 2 | 21 | PFHSTAFT.DOENCANOTIFCOMPULSORIA |
| Cnpj do orgão a qual o funcionário foi cedido | String | 18 | 22 | PFHSTAFT.CNPJORGAOCEDIDO |
| Dt. Inicial da Continuidade de Aft. | Data | 8 | 23 | PFHSTAFT.DTINICONTINUIDADEAFT |
| Afastamento pela Previdência | Booleano | 1 | 24 | PFHSTAFT.AFASTPELAPREVIDENCIA |
