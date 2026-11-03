---
article_id: 360039752154
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: d9b3640ef000febb1255ff168be235d24b4b6ed988fdad0b55d9bc0912c7cad6
fetched_at: '2026-06-28T22:42:44.715037+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Para produtos de apropriação indireta,
  para qual armazém é gerada a OP intermediária
type: support-article
updated_at: '2022-04-01T13:14:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039752154-Manufatura-Linha-Protheus-SIGAPCP-Para-produtos-de-apropria%C3%A7%C3%A3o-indireta-para-qual-armaz%C3%A9m-%C3%A9-gerada-a-OP-intermedi%C3%A1ria
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura:**00:01:00**  
**Dúvida**Ao empenhar um produto de apropriação indireta, que também é um **PI - Produto Intermediário**, para qual armazém será gerado a **OP - Ordem de Produção** intermediária?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**O Sistema obedece a regra definida no parâmetro **MV\_OPIPROC - Indica se o saldo de OP's Intermediárias de semi-acabados geradas automaticamente pelo Sistema deve ser destinado ao local de processo:**

* Se esse parâmetro tiver o conteúdo **.T.** será gerada a **OP** para o armazém de processo, definido no parâmetro **MV\_LOCPROC - Local padrão a ser enviado os materiais indiretos em processo**.
* Se o conteúdo desse parâmetro for **.F.**, a **OP** intermediária será gerada no armazém padrão do produto, de acordo com a informação do campo **B1\_LOCPAD** ou **BZ\_LOCPAD**, conforme parâmetro **MV\_ARQPROD - O parâmetro configura se os dados de indicadores de produto serao considerados pela tabela "SB1" ou se serão considerados pela da tabela "SBZ"**.
