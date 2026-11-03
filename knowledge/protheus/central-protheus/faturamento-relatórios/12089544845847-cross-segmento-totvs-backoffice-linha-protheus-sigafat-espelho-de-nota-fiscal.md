---
article_id: 12089544845847
category: FATURAMENTO - RELATÓRIOS
content_hash: 7768191beccd247320b541d74a2e20525551e936ea7ed84cf0caab3712889c67
fetched_at: '2026-06-28T22:38:22.888632+00:00'
product: protheus
section_id: 1500001539381
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Espelho de Nota
  Fiscal
type: support-article
updated_at: '2024-04-09T14:51:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12089544845847-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Espelho-de-Nota-Fiscal
---

**Dúvida**

No módulo de Faturamento existe alguma rotina de espelho de nota fiscal?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.  
  
**Solução**

No módulo de Faturamento não há uma rotina específica de Espelho de Nota Fiscal.

A visualização do conteúdo do pedido, antes de preparar o documento de saída é possível através do relatório "Pré-Nota (MATR730)".

**MATR730- Pré -Nota/ Emissão da Confirmação do Pedido**

Permite a emissão da confirmação dos produtos faturados, relacionados a um pedido de venda, apresentando todas as características do pedido, tais como: quantidade, TES, valor dos impostos, condição de pagamento, transportadora, entre outros.

Importante mencionar que os impostos tratados são os calculados no Pedido de Vendas SC5 / SC6 (ex: ICM, IPI, ISS). Alguns outros impostos (ex:Pis, Cofins, Csl e IRF)apesar de serem exibidos na planilha financeira dentro do Pedido, não são gravados em nenhuma tabela na fase de Pedido por se tratarem apenas de prospecção, ou seja, o cálculo fiscal é realizado apenas para demonstração em tela mas são dados temporários visto que o fato gerador do imposto é a emissão da Nota (SF2).

Caso seja imprescindível, avalie a alternativa de customização, conforme detalhes acima.

* Demonstração de Alíquota de ICMS  
  É demonstrado quando o campo D2\_PICM é gravado  
  Verificar campos B1\_PICM , C7\_PICM eF2\_BASEICM

**Saiba mais**: [Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Relatórios do módulo Faturamento e suas particularidades](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015846111-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Relat%C3%B3rios-do-m%C3%B3dulo-Faturamento-e-suas-particularidades)
