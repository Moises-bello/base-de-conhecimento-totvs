---
article_id: 360033487314
category: Originação de Grãos (OG)
content_hash: 33f6d20da2f0e0878837e5799c2294c3697d44416e3e6d0ba87d9aab9073ffe3
fetched_at: '2026-06-28T22:45:41.323413+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Parâmetro MV_AGRPREV Permitir incluir contratos
  de compra e venda sem informar previsão financeira
type: support-article
updated_at: '2025-06-24T11:04:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033487314-Agro-Linha-Protheus-AGR-Par%C3%A2metro-MV-AGRPREV-Permitir-incluir-contratos-de-compra-e-venda-sem-informar-previs%C3%A3o-financeira
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33012395945623)***Tempo aproximado para leitura: **00:00:30 min**  
**Dúvida**Para que serve o parâmetro **MV\_AGRPREV - Não Gera Previsão Financeira**?  
  
 **Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**O parâmetro **MV\_AGRPREV** é do tipo lógico e é utilizado quando é incluído um novo contrato sem informar os dados da primeira *grid*, referentes às previsões financeiras. O Sistema não força as informações desses dados quando o parâmetro **MV\_AGRPREV** está com o conteúdo **.T.** 

* **Opção .T. -> Não gera a Previsão Financeira;**
* **Opção .F. -> Gera a Previsão Financeira.**
