---
article_id: 26961234993559
category: Materiais - Compras (SIGACOM)
content_hash: b3cf3136fcc08fd99d33e6cb5c4b5b4403277c837ba820161ba85925be12aed8
fetched_at: '2026-06-28T22:41:24.195376+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Quais são os principais
  parâmetros na Integração do Importador XML x TOTVS Transmite?
type: support-article
updated_at: '2025-01-31T17:24:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26961234993559-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Quais-s%C3%A3o-os-principais-par%C3%A2metros-na-Integra%C3%A7%C3%A3o-do-Importador-XML-x-TOTVS-Transmite
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26961250777495) Tempo aproximado para leitura: **00:05 min** **Dúvida**Quais são os principais parâmetros na Integração do Importador XML x TOTVS Transmite?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - versão 12

**Solução**

| Parâmetro | Tipo | Conteúdo | Descrição | Observação |
| --- | --- | --- | --- | --- |
| MV\_IMPXML | L | T | Habilita integração Importador XML | Parâmetro deve ser T para que integração com o TOTVS Transmite funcione. |
| --- | --- | --- | --- | --- |
| MV\_DOCIMP | C | NFE/NFS/CTE/CTO | Tipo de XML a serem importados pela integração Importador XML x TOTVS Transmite |  |
| MV\_XMLCID | C |  | Client ID do TOTVS Transmite | Informação virá do TOTVS Transmite. Para obter a credencial:   * Na página Inicial do Transmite * Clicar no símbolo (interrogação) * Opção - Obter Credenciais |
| MV\_XMLCSEC | C |  | Client Secret do TOTVS Transmite | Informação virá do TOTVS Transmite  Para obter a credencial:   * Na página Inicial do Transmite * Clicar no símbolo (interrogação) * Opção - Obter Credenciais |
| MV\_XMLDIAS | N | 30 | Range dias para importar documentos do TOTVS Transmite. | Data Inicio: Data de hoje - MV\_XMLDIAS (30)  Data Final: Data de hoje |
| MV\_NGINN | C |  | Caminho para importar XMLs pelo Importador XML | Tratamento continuara funcionando mesmo com a integração com o TOTVS Transmite ativa  **Obs: Ambientes Linux deixar nomenclatura minúscula** |
| MV\_NGLIDOS | C |  | Caminho para onde o XMLs lidos da pasta IN serão armazenados. | Tratamento continuara funcionando mesmo com a integração com o Totvs Transmite ativa  **Obs1: Ambientes Linux deixar nomenclatura minúscula  Obs2: Documentos originados via Totvs Transmite, não serão salvos na pasta LIDOS, pois XML's já são armazenados no Totvs Transite.** |
| MV\_APITRAN | C | production | Indica ambiente do Totvs Transmite (production / staging / development) | Default: production |
| MV\_DTINITR | D | 20230101 | Data de inicio da integração do Importador XML x TOTVS Transmite | Obs: Se não informar será solicitado TODOS documentos no TOTVS Transmite, caso tenha informado, somente a partir da data será selecionado documentos no TOTVS Transmite |

***Saiba Mais:***

[Parâmetros](https://tdn.totvs.com/pages/releaseview.action?pageId=485869217)

[Pontos de Entrada disponíveis nas funções](https://tdn.totvs.com/display/public/PROT/IX02+-+Pontos+de+Entrada)

[Importador XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML)

[Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)

[CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
