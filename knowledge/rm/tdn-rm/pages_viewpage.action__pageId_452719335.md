---
content_hash: 886ac5fe59a4ff825695e550164ef57b62ecfc0375a5f776c426808fb204256c
fetched_at: '2026-06-29T00:10:06.744916+00:00'
page_id: '452719335'
product: rm
source: tdn-rm
title: Layout Para Importação de Histórico de Faltas (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719335
version: 6
---

**Importante:**  
Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
**Campos obrigatórios estão destacados em negrito.**  
DELIMITADOR DE CAMPOS: ";"  
Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
Entre ponto virgula ( **;;** ) "Correspondendo um campo NULL".  
A tabela abaixo é premissa para a importação de Histórico de Faltas  
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
| **Chapa** | **String** | **16** | **1** | **PFHSTFALTA.CHAPA** |
| **Data de Início (ddmmaaaa hh:mm:ss)** | **Data** | **17** | **2** | **PFHSTFALTA.DATAINICIO** |
| **Data Final (ddmmaaaa hh:mm:ss)** | **Data** | **17** | **3** | **PFHSTFALTA.DATAFINAL** |
| Horas de Atraso | Inteiro | 4 | 4 | PFHSTFALTA.HORASATRASO |
| Desconta DSR | Booleano | 2 | 5 | PFHSTFALTA.DESCONTADSR |
| Abona Falta | Booleano | 2 | 6 | PFHSTFALTA.ABONA |
| Observação | String | 100 | 7 | PFHSTFALTA.OBSERVACAO |
| Status | Inteiro | 4 | 8 | PFHSTFALTA.STATUS |
| Mês Competência da Falta | Inteiro | 4 | 9 | PFHSTFALTA.MESCOMPFALTA |
| Ano Competência da Falta | Inteiro | 4 | 10 | PFHSTFALTA.ANOCOMPFALTA |
| Usuário que efetuou o estorno da Falta | String | 20 | 11 | PFHSTFALTA.USUARIO |
| Data em que o estorno foi realizado | Data | 8 | 12 | PFHSTFALTA.DATAESTORNO |
| Falta bloqueada p/ atualização automátic | Booleano | 2 | 13 | PFHSTFALTA.BLOQUEADO |
| Fração dia de falta  Campos a partir da 12.1.31 | Real | 15 | 14 | PFHSTFALTA.FRACAODIAFALTA |
| Desconsidera férias Campos a partir da 12.1.31 | Booleano | 1 | 15 | PFHSTFALTA.DESCONSIDERAFERIAS |
| Desconsidera 13 Salário Campos a partir da 12.1.31 | Booleano | 1 | 16 | PFHSTFALTA.DESCONSIDERADECIMOTERCEIRO |
