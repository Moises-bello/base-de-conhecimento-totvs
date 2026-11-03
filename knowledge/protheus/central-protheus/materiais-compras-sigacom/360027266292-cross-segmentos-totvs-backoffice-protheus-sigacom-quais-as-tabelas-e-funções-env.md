---
article_id: 360027266292
category: Materiais - Compras (SIGACOM)
content_hash: 4795b5f07f983f893e6a2df1902f590f91dabb1ae7c1c63da1c041dfe10203d9
fetched_at: '2026-06-28T22:41:10.320817+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Quais as tabelas e
  funções envolvidas no processo de Entrada do Totvs Colaboração ?
type: support-article
updated_at: '2022-05-13T11:47:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027266292-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Quais-as-tabelas-e-fun%C3%A7%C3%B5es-envolvidas-no-processo-de-Entrada-do-Totvs-Colabora%C3%A7%C3%A3o
---

**Dúvida**Quais as tabelas e funções envolvidas no processo de Entrada do Totvs Colaboração ?

**Ambiente**  
Protheus – Compras – A partir da versão 12

**Solução**Ao utilizar o Totvs Colaboração essas são as tabelas e rotinas correspondentes.

| Tabela | Descrição | Versão 1.0 | Versão 2.0 |
| --- | --- | --- | --- |
| CKP | Parâmetros TOTVS Colaboração |  | X |
| CKQ | Monitor de Documentos TOTVS Colaboração. |  | X |
| CKO | Controle de arquivos TOTVS Colaboração. |  | X |
| CC0 | Manifesto Documentos Fiscais. |  | X |
| SDS | Cabeçalho Importação XML NF-e | X | X |
| SDT | Itens Importação XML NF-e | X | X |
| SF1 | Cabeçalho NF-e/CT-e | X | X |
| SD1 | Itens NF-e/CT-e | X | X |

| Rotina | Versão 1.0 | Versão 2.0 | Observação |
| --- | --- | --- | --- |
| COLABDOCUMENTOS.PRW |  | X |  |
| COLABGENERIC.PRW |  | X |  |
| COLAUTOREAD.PRW |  | X | A partir da data 22/01/16, Tratamento de threads.  Responsável pela leitura do XML e gravação na CKO. |
| COLREADCONTROL.PRW |  | X |  |
| COMXCOL.PRW | X | X | Monitor Totvs Colaboração |
| SCHEDCOMCOL.PRW | X | X | A partir da data 22/01/16, Tratamento de threads  A partir da data 05/04/16, Tratamento de e-mail Eventviewer.  Responsável pela leitura da CKO e geração do documento na SDS/SDT. |
| MATA140I.PRW | X | X | Importação de NFE/NFS |
| MATA140.PRW | X | X | Pre - Nota |
| MATA103.PRW | X | X | Documento de Entrada |
| MATA116I.PRW | X | X | Importação de CTE |
| MATA116.PRW | X | X | Conhecimento de Frete |
