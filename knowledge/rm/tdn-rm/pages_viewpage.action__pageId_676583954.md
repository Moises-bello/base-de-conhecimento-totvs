---
content_hash: 5dceed81eb2b72140bdccb6722cd949634c84acbf03c996c33e2eaff3d5dde2e
fetched_at: '2026-06-29T00:11:17.078034+00:00'
page_id: '676583954'
product: rm
source: tdn-rm
title: Layout Para Importação de Histórico do Estatutário (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=676583954
version: 5
---

**Importante:**  
Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
**Campos obrigatórios estão destacados em negrito.**  
DELIMITADOR DE CAMPOS: ";"  
Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
A tabela abaixo é premissa para a importação de Histórico do Estatutário  
- PFUNC  
   
**Atenção!** Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:  
-  0 (zero) ou 1(um) em campos do tipo **Booleano**;  
-  Números (00) em campos do tipo**Inteiro**;  
-  Números com vírgulas ou Pontos (0,00 ou 0.00) em campos do tipo **Real**;  
- (ddmmyyyy) em campos do tipo **Data**;  
- (GRR20071514) em campos do tipo **String**;  
- Começam /@ e terminam com @/ em campos do tipo **MEMO**.  
Para o caso de importação de históricos a data da mudança deve sempre ser informada. Caso este campo não seja informado, o registro em questão não será importado.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Origem:** Arquivo informado no campo "Histórico do Estatutário" | | | | | |
| **Destino:  PFHSTESTATUTARIO** | | | | | |
| **Layout** | | | | | |
| **Flg** | **Descrição** | **Tipo** | **Tam.** | **Pos.** | **Campo** |
|  | Código Identificador da Coligada | String | 2 | 1 | PFHSTESTATUTARIO.CODCOLIGADA |
|  | Chapa do Funcionário | String | 16 | 2 | PFHSTESTATUTARIO.CHAPA |
|  | Data da Mudança | Data | 8 | 3 | PFHSTESTATUTARIO.DTMUDANCA |
|  | Tipo de provimento | String | 2 | 4 | PFHSTESTATUTARIO.TIPOPROVIMENTO |
|  | Data da entrada em exercício pelo servidor | Data | 8 | 5 | PFHSTESTATUTARIO.DTEXERCICIO |
|  | Tipo de plano de segregação da massa | String | 2 | 6 | PFHSTESTATUTARIO.TIPOPLANOSEGREGACAOMASSA |
|  | Sujeito ao teto do RGPS | Inteiro | 2 | 7 | PFHSTESTATUTARIO.TETORGPS |
|  | Recebe abono permanência | Inteiro | 2 | 8 | PFHSTESTATUTARIO.ABONOPERMANENCIA |
|  | Data de inicio do abono permanência | Data | 8 | 9 | PFHSTESTATUTARIO.DTINICIOABONO |
|  | Indicar se o servidor optou pela remuneração do cargo efetivo | Inteiro | 2 | 10 | PFHSTESTATUTARIO.INDICATIVOREMUNERACAOCARGO |
|  | Tipo de regime trabalhista mandato eletivo | Inteiro | 2 | 11 | PFHSTESTATUTARIO.TIPOREGTRABMANDATOELETIVO |
|  | Tipo de regime previdenciário mandato eletivo | Inteiro | 2 | 12 | PFHSTESTATUTARIO.TIPOREGPREVMANDATOELETIVO |
|  | Código da categoria de origem do servidor público com mandato eletivo | Inteiro | 3 | 13 | PFHSTESTATUTARIO.CODCATEGORIAMANDATOELETIVO |
|  | CNPJ do orgão público de origem com mandato eletivo | String | 20 | 14 | PFHSTESTATUTARIO.CNPJMANDATOELETIVO |
|  | Matrícula do servidor no orgão público de origem com mandato eletivo | String | 30 | 15 | PFHSTESTATUTARIO.MATRICULAMANDATOELETIVO |
|  | Data de exercício do servidor no orgão público de origem com mandato eletivo | Data | 8 | 16 | PFHSTESTATUTARIO.DTEXERCICIOMANDATOELETIVO |
