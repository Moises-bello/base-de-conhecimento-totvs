---
content_hash: e6e16d23b406df2d79df86e184baa7c300deec4ab2fab1e88ca9edd789580b53
fetched_at: '2026-06-29T00:10:07.322483+00:00'
page_id: '452719401'
product: rm
source: tdn-rm
title: Importação de Controle de faltas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719401
version: 1
---

**Importação de Controle de faltas**   
Este módulo possibilitará o usuário realizar a importação de arquivo contendo os dados do Controle de Faltas do funcionário.   
Caso o parâmetro **Controle de faltas através do RM Chronus** esteja marcado, esta opção será desabilitada, e o controle passa a ser realizado via lançamento do RM Chronus.  
Layout de Importação:

|  |  |  |  |
| --- | --- | --- | --- |
| **Descrição** | **Tipo** | **Tamanho** | **Observação** |
| CHAPA | String | 016 |  |
| DATAINICIO | Data | 010 | Formato DD/MM/AAAA |
| OBSERVACAO | String | 100 |  |
| ABONAFALTA | Inteiro | 001 | Informe 0(zero) para não abonar e 1(um) para abonar. |
| DATAESTORNO | Data | 010 | Formato DD/MM/AAAA |
