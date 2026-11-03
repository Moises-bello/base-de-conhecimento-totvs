---
article_id: 4466432523287
category: Materiais - Compras (SIGACOM)
content_hash: f61d0e544e1e344e201fb20a14a45f29c0b45ccd097fbbeee4eab30c67bc2bb5
fetched_at: '2026-06-28T22:41:17.630720+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Error log : array
  out of bounds [3] of [2]  on A103ATUSE2(MATA103.PRW) 09/02/2022 15:49:30 line :
  10624 na inclusão do documento de entrada'
type: support-article
updated_at: '2022-05-16T22:52:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4466432523287-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Error-log-array-out-of-bounds-3-of-2-on-A103ATUSE2-MATA103-PRW-09-02-2022-15-49-30-line-10624-na-inclus%C3%A3o-do-documento-de-entrada
---

**Dúvida**Ao tentar salvar um documento de entrada o sistema gera o error log :

**array out of bounds [3] of [2] on A103ATUSE2(MATA103.PRW) 09/02/2022 15:49:30 line : 10624**

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - Todas as versões  
  
**Solução**Verifique os parâmetros : **MV\_VISDIRF e MV\_AUTOISS.**

Quando o parâmetro **MV\_VISDIRF** está habilitado, ou seja com **conteúdo = 1** , o sistema busca informações de acordo com a configuração atual do parâmetro **MV\_AUTOISS.**

Configuração padrão do parâmetro **MV\_AUTOISS :**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4466381624983/mceclip0.png)**

**Exemplo de Preenchimento:**

{"Fornecedor","Loja","Gera DIRF","Cod. Retenção"} .

**Importante:** As duas primeiras posições são do ISS, a terceira e quarta tem relação com o IR, exemplo:

{"Fornecedor","Loja","SIM","1708"} . As 4 posições devem estar preenchidas, caso não queira informar nenhum conteudo, deve usar "", segundo exemplo da imagem acima.

Para saber como efetuar o correto preenchimento do parâmetro, verifique o documento que consta no link abaixo :

[**Como destacar o código de retenção do IRRF de forma automática**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041234634-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-destacar-o-c%C3%B3digo-de-reten%C3%A7%C3%A3o-do-IRRF-de-forma-autom%C3%A1tica)

***Saiba Mais :***

*[PÁGINA CENTRALIZADORA DO COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)*

*[Mais Artigos Materiais - Compras ( SIGACOM )](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)*
