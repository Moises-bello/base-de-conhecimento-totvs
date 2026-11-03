---
content_hash: 02f3f06a53e26613b95ddaf0a8d2cc38a40fea2d14fb17f26b6a5a259c8d5948
fetched_at: '2026-06-29T00:10:13.944008+00:00'
page_id: '458771763'
product: rm
source: tdn-rm
title: Layout de Importação do Detalhamento das Verbas geradas pela Diferença de Férias
  (Envelope)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=458771763
version: 3
---

O layout de importação do "Detalhamento das Verbas geradas pela Diferença de Férias (Envelope)"  foi desenvolvido para que sejam importadas as verbas geradas por diferença de férias com base no envelope de pagamento e não no recibo de férias. Está separação se fez necessária para distinguir as verbas que incidem INSS nas suas devidas competências ( No mês e no Próximo mês).    
    
 **Importante**

* Os campos em negrito são obrigatórios.
* O delimitados dos campos é ';'.
* Quando o campo não é obrigatório e não tenha valor, o mesmo deve ser informado no arquivo entre ponto-virgula: **;;**
* As tabelas premissas para importação:
  + PFUNC
  + PEVENTO
  + PDADOSDIS (caso o campo seja informado)
  + PFPERFF

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Descrição | Tipo | Tamanho | Posição | Campo |
| **Chapa do Funcionário** | **String** | **16** | **1** | **PFVERBASDIS.CHAPA** |
| **Ano da Competência** | **String** | **04** | **2** | **PFVERBASDIS.ANOCOMP** |
| **Mês de Competência** | **String** | **02** | **3** | **PFVERBASDIS.MESCOMP** |
| **Número do Período** | **String** | **02** | **4** | **PFVERBASDIS.NROPERIODO** |
| **Código do Evento** | **String** | **04** | **5** | **PFVERBASDIS.CODEVENTO** |
| **Data de Pagamento** | **Data** | **08** | **6** | **PFVERBASDIS.DTPAGTO** |
| **Ano de Referência** | **String** | **04** | **7** | **PFVERBASDIS.ANOREF** |
| **Mês de Referência** | **String** | **02** | **8** | **PFVERBASDIS.MESREF** |
| **Período de referência** | **String** | **02** | **9** | **PFVERBASDIS.PERIODOREF** |
| Hora | String | 06 | 10 | PFVERBASDIS.HORA |
| Referência | Decimal | 15 | 11 | PFVERBASDIS.REF |
| Valor | Decimal | 15 | 12 | PFVERBASDIS.VALOR |
| Valor Original | Decimal | 15 | 13 | PFVERBASDIS.VALORORIGINAL |
| **Dissidio** | **String** | **02** | **14** | **PFVERBASDIS.DISSIDIO** |
| Número do período de férias | String | 02 | 15 | PFVERBASDIS.NROPERIODOFERIAS |
| Data de vencimento | Data | 08 | 16 | PFVERBASDIS.DTVENCIMENTO |
| Motivo de aumento salarial | String | 02 | 17 | PFVERBASDIS.MOTIVO |
| Código do acordo/dissídio | Inteiro | 04 | 18 | PFVERBASDIS.IDDADOS |
| verba de diferença de 13º salário | String | 02 | 19 | PFVERBASDIS.VERBA13SALARIO |
