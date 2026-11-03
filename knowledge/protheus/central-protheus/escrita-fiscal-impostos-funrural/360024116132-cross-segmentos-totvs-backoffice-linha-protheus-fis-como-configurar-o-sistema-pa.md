---
article_id: 360024116132
category: Escrita Fiscal - Impostos - Funrural
content_hash: d3b659ff6b09690d6b15c28960fdae1dd55511837908a42ad2eac8c7547629a7
fetched_at: '2026-06-28T22:39:28.105642+00:00'
product: protheus
section_id: 1500001549822
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como configurar o
  sistema para calcular somente o SENAR?
type: support-article
updated_at: '2021-08-19T19:17:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024116132-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-sistema-para-calcular-somente-o-SENAR
---

**Dúvida:**

Na aquisições de mercadoria de fornecedor rural, como parametrizar o sistema para reter somente o SENAR,  quando os produtores optarem pelo recolhimento da contribuição previdenciária Gilrat e INSS sobre sua folha de pagamento (evento R2055)?

**Ambiente:**

Protheus – Livros Fiscais – A partir da versão 11.80

**Solução:**

A parametrização do Funrural continua da mesma forma, somente deverá criar um TES (tabela SF4) onde o campo Cont.Seg.Soc (F4\_CONTSOC) deve estar como 2-NÃO e sua natureza financeira (tabela SED) os campos Calcula INSS = N-NÃO e Porc INSS = 0,00.

Desta forma somente será calcula e o SENAR:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406675706263/mceclip0.png)

\* Importante destacar a importância do preenchimento no campo do fornecedor (tabela SA2) A2\_INDCP (Ind. Rural) a opção 2 - Sobre a Folha de Pagamento,  desta forma será gerado no XML o preenchimento da TAG  IndOpcCP= "S" corretamente no Reinf:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406675844247/mceclip1.png)

A configuração completa do Funrural é possível obter através do boletim técnico abaixo:

<https://tdn.totvs.com/display/public/PROT/FIS0111+-+SENAR+%2C+INSS+E+GILRAT>
