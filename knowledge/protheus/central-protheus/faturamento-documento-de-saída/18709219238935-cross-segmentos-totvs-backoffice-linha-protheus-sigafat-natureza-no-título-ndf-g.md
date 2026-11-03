---
article_id: 18709219238935
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 9c2c408057fe174a1289061554b265896b66128193452491ead897c40c42f5e5
fetched_at: '2026-06-28T22:38:45.420226+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Natureza no
  título NDF gerado na devolução de vendas
type: support-article
updated_at: '2023-10-31T20:42:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18709219238935-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Natureza-no-t%C3%ADtulo-NDF-gerado-na-devolu%C3%A7%C3%A3o-de-vendas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18709196001943) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como informar a Natureza no título "NDF" ao realizar uma devolução de venda?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Solução**

Na Compensação do título, o campo **A2\_NATUREZ**deve ser preenchido no Cadastro do Fornecedor, caso não esteja é necessário alterar a NDF, e preencher o campo **E2\_NATUREZ**manualmente.

O Sistema não carregará a informação no campo **E2\_NATUREZ,**pois é possível devolver várias notas de Entrada  em uma só nota de saída, e cada uma dessas notas devolvidas poderá ter naturezas diferentes, por esta razão é fixa a busca através da natureza do Cadastro do Fornecedor.

Caso necessite realizar a customização do comportamento padrão, ela é possível através do ponto de entrada [M460FIM - Chamado após a gravação da NF de Saída](https://tdn.totvs.com/x/tIRn)

**Saiba mais**: [Gerar NDF pelo modulo de Faturamento (SIGAFAT)](https://tdn.totvs.com/x/u44jDw)
