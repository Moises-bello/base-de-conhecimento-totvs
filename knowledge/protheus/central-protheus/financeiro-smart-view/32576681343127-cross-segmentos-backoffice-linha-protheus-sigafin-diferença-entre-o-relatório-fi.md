---
article_id: 32576681343127
category: Financeiro - Smart View
content_hash: d037ed3e8bd3db26f566d6c810757d7c46702cdfebd78ebe0851b78075d4ec06
fetched_at: '2026-06-28T22:37:44.722518+00:00'
product: protheus
section_id: 32632656432151
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Diferença entre o relatório
  FINR470 (Extrato Bancário) x FINSV014 (Smartview)
type: support-article
updated_at: '2026-04-02T11:33:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32576681343127-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Diferen%C3%A7a-entre-o-relat%C3%B3rio-FINR470-Extrato-Banc%C3%A1rio-x-FINSV014-Smartview
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32576641416599) Tempo aproximado para leitura: 00:08 min**  
  
**Dúvida**

Diferença entre relatório de extrato bancário (FINR470) x FINSV014 (Smartview). O que avaliar?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release 12.1.2210

**Solução**

A diferença entre os relatórios acontece por causa das tabelas usadas para gerar as informações:

O relatório de extrato bancário (FINR470) utiliza os dados da tabela SE5, que registra as baixas realizadas.

Já o extrato exibido no SmartView usa a tabela FK5.

Quando uma baixa é feita, o sistema grava informações nas duas tabelas (SE5 e FK5). Porém, elas se comportam de forma diferente quando essa baixa é excluída:

* Na tabela SE5, ao excluir uma baixa, nenhum novo registro é gerado.
* Na tabela FK5, a exclusão é registrada normalmente.

Além disso, houve uma atualização no sistema onde a tabela FK5 passou a registrar também as exclusões. Por isso, ela é utilizada no SmartView e no novo conciliador.

No modelo antigo de conciliação, que utilizava a SE5, essas exclusões não apareciam no relatório FINR470. Isso pode causar diferenças entre os relatórios, principalmente se já houve exclusões de baixa.

**OBS: No novo conciliador foi implementado um filtro com a opção de****remover registros estornados****, o que impede a exibição de dados referentes a exclusões e cancelamentos.**

**Saiba mais**

[Reestruturação Financeiro - Baixas e Movimento Bancário](https://tdn.totvs.com.br/pages/releaseview.action?pageId=181965434)
