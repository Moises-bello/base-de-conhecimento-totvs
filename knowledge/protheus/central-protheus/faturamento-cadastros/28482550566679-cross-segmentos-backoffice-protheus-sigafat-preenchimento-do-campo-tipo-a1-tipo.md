---
article_id: 28482550566679
category: Faturamento - Cadastros
content_hash: 4463a9117efbe93fc4cb253b01cf5f0cd62f449bb0cafd10b0d199fd43f90d5a
fetched_at: '2026-06-28T22:38:36.818790+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Preenchimento do campo "Tipo
  (A1_TIPO)" em Clientes (CRMA980)
type: support-article
updated_at: '2024-12-12T18:53:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28482550566679-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Preenchimento-do-campo-Tipo-A1-TIPO-em-Clientes-CRMA980
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28482550524951) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Qual o preenchimento do campo "Tipo (A1\_TIPO)" em Clientes (CRMA980)?  
  
**Ambiente**Cross Segmentos - BackOffice Protheus - SIGAFAT - Todas as versões  
  
**Solução** **Tipo**: A seleção do campo Tipo, influencia diretamente no tipo do documento a ser emitido. Pode ser informado:

* **F - Consumidor Final:** O tipo de cliente consumidor final é importante para a geração das [Notas Fiscais de Venda ao Consumidor Final.](https://tdn.totvs.com/x/9yfAFQ)
* **L - Produtor Rural:** O tipo de cliente produtor rural é importante para a geração das [Notas Fiscais de Venda ao Produtor Rural.](https://tdn.totvs.com/x/YynAFQ)
* **R - Revendedor:** O tipo de cliente revendedor pode ser utilizado em várias situações tributárias distintas, o que irá definir o cálculo dos impostos e taxas. A forma de tributação é o TES de saída utilizado na emissão da nota fiscal.
* **S - Solidário:** O tipo de cliente solidário é importante para a geração das [Notas Fiscais de Venda com Substituição Tributária](https://tdn.totvs.com/x/5WfAFQ), ou seja, com o cálculo de ICMS Solidário ou Retido na Fonte.
* **X - Exportação:** O tipo de cliente exportação é importante para a geração das [Notas Fiscais de Exportação.](https://tdn.totvs.com/x/5ynAFQ)

**Observação**

Não é possível **adicionar** novos tipos de clientes no campo, pois essa configuração está bloqueada no configurador. Isso ocorre porque essas informações são utilizadas pela área fiscal, e alterações podem gerar conflitos futuros não mapeados.

Como alternativa, sugerimos criar um campo adicional que permita configurar os tipos de cliente de acordo com sua necessidade. Caso precise de ajuda para criar esse campo, contate a Equipe Protheus Framework.

**Saiba mais:**  
[Clientes (MATA030/CRMA980 - SIGAFAT)](https://tdn.totvs.com/x/mQ8NF)
