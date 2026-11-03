---
article_id: 27793496467095
category: SIGAEST - RELATORIOS
content_hash: d7f4f566a7c7fd98a50181e4bfdf05d564935b8ca9290eef6fa3c2abee379925
fetched_at: '2026-06-28T22:39:06.135411+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR300 - Consulta
  de "branco" até "ZZZZZZ" não exibe todas as movimentações
type: support-article
updated_at: '2024-12-20T12:31:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27793496467095-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR300-Consulta-de-branco-at%C3%A9-ZZZZZZ-n%C3%A3o-exibe-todas-as-movimenta%C3%A7%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27793537675415) Tempo aproximado para leitura: **00:01:30 min****Ocorrência**Consulta de "branco" até "ZZZZZZ" não exibe todas as movimentações no relatório MATR300  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Causa**

Uma das causas para esse comportamento pode ser a configuração do Collation do Banco de Dados:

* **[Consulta de "branco" até "Z" ou até "ZZZZZZ" não retorna produtos iniciados com a letra Z](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8907262948631-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR260-Consulta-de-branco-at%C3%A9-Z-ou-at%C3%A9-ZZZZZZ-n%C3%A3o-retorna-produtos-iniciados-com-a-letra-Z)**

Quando isso ocorre, provavelmente o documento que gerou a movimentação é iniciado com um caractere minúsculo, e como na tabela ASCII as letras minúsculas vem após a letra Z, realizando um filtro até "ZZZZZZ" não contempla os documentos começados com as letras minúsculas abcd...

![NILTU.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27794113006999)

**Solução**

Solicite ao seu DBA (Administrador de Banco de Dados) verificar a configuração do Colation do Banco.

Um paliativo para o cenário:

Uma OP gerada com o número(C2\_NUM) = c00016, após requisitar a MP, será registrado uma movimentação na SD3 com o número do documento(D3\_COD) = c00016.

MATA650 - OP criada

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27793537676567)

MATA241 - Após Requisitar/Apontar OP  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27793496445079)

Ao extrair o relatório MATR300 com os perguntes  de **OP e Documento de "branco" até "zzzzz"**, as movimentações são geradas de forma esperada.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27793496445719) ![](https://centraldeatendimento.totvs.com/hc/article_attachments/27793537683479)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27794220797207)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Relatórios do Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538841-SIGAEST-RELATORIOS)*
