---
content_hash: f035b3d2cbf6cc128b2ce1733acf6991ad913fa23b1538e51de0b829b5f9ceb0
fetched_at: '2026-06-29T00:09:22.081198+00:00'
page_id: '422545960'
product: rm
source: tdn-rm
title: Parâmetros da ECF (Complementares)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545960
version: 5
---

Através do campos Complementares dos Parâmetros ECF - Escrituração Fiscal Contábil, é que será definido se os campos do registro 020 será gerado com "S (sim)" ou "N (Não)". Campos desmarcados serão gerados com "N" e marcados com "S". Segue a listagem dos campos:

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição / Campo da Base** | **Observações** |
| 01 | REG | Texto fixo contendo "0020". | Tela da rotina |
| 02 | IND\_ALIQ\_CSLL | PJ Sujeita à Alíquota da CSLL de 15% | Existirão vários períodos para o tributo CSLL. Entretanto, todos os períodos devem retornar 15% |
| 03 | IND\_QTE\_SCP | Quantidade de SCP da PJ - Sócio Ostensivo de SCP - Total de SCP. | Gerar com a quantidade de Filiais cujo parâmetro "SCP" esteja marcado.  Só deve ser preenchido se o campo 14 TIP\_EFD = 1. Senão deixar em branco. |
| 04 | IND\_ADM\_FUN\_CLU | Administradora de Fundos e Clubes de Investimento |  |
| 05 | IND\_PART\_CONS | Participações em Consórcios de Empresas |  |
| 06 | IND\_OP\_EXT | Operações com o Exterior |  |
| 07 | IND\_OP\_VINC | Operações com Pessoa Vinculada/Interposta Pessoa / País com Tributação Favorecida. |  |
| 08 | IND\_PJ\_ENQUAD | PJ Enquadrada no art. 58-A da IN RFB no 1.312/2012 |  |
| 09 | IND\_PART\_EXT | Participações no Exterior |  |
| 10 | IND\_ATIV\_RURAL | Existência de atividade rural |  |
| 11 | IND\_LUC\_EXP | Existência de lucro da exploração |  |
| 12 | IND\_RED\_ISEN | Isenção e redução do imposto para lucro presumido |  |
| 13 | IND\_FIN | Indicativo da existência de FINOR/FINAM/FUNRES |  |
| 14 | IND\_DOA\_ELEIT | Doações a campanhas eleitorais | *Descontinuado a partir da Versão 007 do Layout ECF* |
| 15 | IND\_PART\_COLIG | Participação permanente em coligadas ou controladas |  |
| 16 | IND\_VEND\_EXP | PJ efetuou vendas a empresa comercial exportadora com fim específico de exportação | *Descontinuado a partir da Versão 007 do Layout ECF* |
| 17 | IND\_ REC\_EXT | Rendimentos do exterior ou de não residentes |  |
| 18 | IND\_ATIV\_EXT | Ativos no exterior |  |
| 19 | IND\_COM\_EXP | PJ comercial exportadora | *Descontinuado a partir da Versão 007 do Layout ECF* |
| 20 | IND\_PGTO\_EXT | Pagamentos ao exterior ou a não residentes |  |
| 21 | IND\_E-COM\_TI | Comércio eletrônico e tecnologia da informação |  |
| 22 | IND\_ROY\_REC | Royalties recebidos do Brasil e do exterior |  |
| 23 | IND\_ROY\_PAG | Royalties pagos a beneficiários do Brasil e do exterior |  |
| 24 | IND\_REND\_SERV | Rendimentos relativos a serviços, juros e dividendos recebidos do Brasil e do exterior |  |
| 25 | IND\_PGTO\_REM | Pagamentos ou remessas a título de serviços, juros e dividendos a beneficiários do Brasil e do exterior |  |
| 26 | IND\_INOV\_TEC | Inovação tecnológica e desenvolvimento tecnológico |  |
| 27 | IND\_CAP\_INF | Capacitação de informática e inclusão |  |
| 28 | IND\_PJ\_HAB | PJ habilitada no Repes, Recap, Padis, PATVD, Reidi, Repenec, Reicomp, Retaero, Recine, Resíduos Sólidos, Recopa, Copa do Mundo, Retid, REPNBL-Redes, Reif e Olimpíadas |  |
| 29 | IND\_POLO\_AM | Pólo industrial de Manaus e Amazônia Ocidental |  |
| 30 | IND\_ZON\_EXP | Zonas de processamento de exportação |  |
| 31 | IND\_AREA\_COM | Áreas de livre comércio |  |
| 32 | IND\_DEREX | Declaração Sobre utilização de recursos em moeda estrangeira |  |
