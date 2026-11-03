---
content_hash: f981a1cf7c59ca1301756ad4d774196e60aa0039d0310bdd9628bae54729be30
fetched_at: '2026-06-29T00:09:10.391568+00:00'
page_id: '397383270'
product: rm
source: tdn-rm
title: RMFIS00019_Registro D100
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00019_Registro+D100
version: 5
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.1.7 |
| **Ocorrência:** | Parametrização do Registro D100 - EFD Contribuições. |
| **Ambiente:** |  |
| **Passo a passo:** | Este registro deve ser apresentado por todos os contribuintes adquirentes dos serviços relacionados, que utilizem os documentos previstos para este registro, cuja operação dê direito à apuração de crédito à pessoa jurídica contratante, na forma da legislação tributária.     * + Para o tipo de documento informado no lançamento fiscal - Deve existir código de modelo de documento e este deve ser pertinente a rotina;        * Informar o Tipo Frete, na aba de Transporte/ Sub aba Identificação;        * Preencher os dados de Coleta e Entrega, na aba de Transporte/ Sub aba Coleta e Entrega;            * Nos itens do lançamento os tributos PIS e COFINS destacados de acordo com a operação;       Segue abaixo resultado do exemplo:    |D001|0| |D010|21867387000158| |D100|0|1|F00002|57|00|1||44444||31082018|31082018|0||3000,00|0,00|0|3000,00|3000,00|540,00|0,00||| |D101||3000,00|50||3000,00|1,6500|49,50|| |D105||3000,00|50||3000,00|7,6000|228,00|| |D990|6| |
| **Observações:** | Não podem ser informados dois ou mais registros com a combinação de mesmos valores dos campos :    1. emissão de terceiros : IND\_EMIT+NUM\_DOC+COD\_MOD+SER+SUB+COD\_PART;  2. emissão própria: IND\_EMIT+NUM\_DOC+COD\_MOD+SER+SUB. Para cada documento informado e relacionado em cada registro D100, obrigatoriamente deve ser apresentado o detalhamento das informações, por item do documento, referentes ao PIS/Pasep (D101) e à Cofins (D105). |
