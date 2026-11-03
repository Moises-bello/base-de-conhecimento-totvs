---
article_id: 360052521153
category: Faturamento - Orçamentos
content_hash: 0468ab6055720d99afed61b81054cd60089e793f2e5ce9153ee1c84aff9058ee
fetched_at: '2026-06-28T22:38:25.008402+00:00'
product: protheus
section_id: 1500001539281
source: central-protheus
title: MP-FAT-Venda Presencial no Orçamentos de Venda
type: support-article
updated_at: '2021-04-28T15:15:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052521153-MP-FAT-Venda-Presencial-no-Or%C3%A7amentos-de-Venda
---

**Dúvida**

Ao consultar a **Planilha Financeira** da rotina de **Orçamentos de Venda**, não está considerando a alíquota Interna em **Vendas Presenciais** de mercadorias destinada a **Consumidor Final**, sediado em outro Estado ou País.  
   
 **Ambiente**

Microsiga Protheus - a partir da 12.1.17 com garantia estendida.

**Solução**

Foi criado o campo **Tipo de Frete** (**CJ\_TPFRETE**) na tabela **SCJ - Cabeçalho do Orçamentos de Venda**, para que a **Planilha Financeira** da rotina de **Orçamentos de Venda** passe a considerar a alíquota interna em **Vendas Presenciais**, quando é utilizado em conjunto com os campos: **Tipo Cliente** (**CJ\_TIPOCLI**) e **Venda Presencial** (**F4\_VENPRES**).

Para implementação do campo,:

1- Aplique o pacote relacionado a sua release:

**12.1.25:<https://suporte.totvs.com/portal/p/10098/download?e=859284>** ; **12.1.23:<https://suporte.totvs.com/portal/p/10098/download?e=859283>** ; **12.1.17:<https://suporte.totvs.com/portal/p/10098/download?e=859282> (garantia estendida).**

2-Inclua o campo manualmente via configurador, conforme as instruções do documento técnico: [**https://tdn.totvs.com/x/cbIXHw**](https://tdn.totvs.com/x/cbIXHw)

**Obs: O campo CJ\_TPFRETE estará disponível no dicionário de dados a partir do release 12.1.27.**
