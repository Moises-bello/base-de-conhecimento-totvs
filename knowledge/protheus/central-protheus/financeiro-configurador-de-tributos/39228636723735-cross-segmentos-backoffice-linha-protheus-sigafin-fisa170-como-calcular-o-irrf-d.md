---
article_id: 39228636723735
category: Financeiro - Configurador de Tributos
content_hash: 3d6f65af978c6108fc28f396921dff6796357692fb28d92d8dc90b06faabd3c7
fetched_at: '2026-06-28T22:37:45.827482+00:00'
product: protheus
section_id: 30946086151959
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FISA170 - Como calcular
  o IRRF de Pessoa Física sem o desconto simplificado via Configurador de Tributos?
type: support-article
updated_at: '2026-03-25T16:44:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39228636723735-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-Como-calcular-o-IRRF-de-Pessoa-F%C3%ADsica-sem-o-desconto-simplificado-via-Configurador-de-Tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39228636681623) Tempo aproximado para leitura: **00:05:00**  
  
**Dúvida:**

Como calcular o IRRF de Pessoa Física sem o desconto simplificado via Configurador de Tributos?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - a partir da versão 12.1.2410

**Solução**

Como existem cenários onde o fornecedor (Pessoa Física) pode ser não optante pelo desconto simplificado, a solução adequada no Configurador de Tributos é ter uma tabela progressiva sem o desconto simplificado vinculada a uma regra financeira aplicável a este fornecedor.

Para realizar essa configuração, siga os passos abaixo:

1. Acesse o módulo financeiro e direcione-se ao cadastro de **Tabelas Progressivas** no Configurador de Tributos.
2. Inclua uma nova tabela progressiva ou altere a tabela específica que será utilizada para essa exceção.
3. No cadastro da tabela progressiva, deixe o campo **Ded.Simplif** (`FKS_DEDSIM`) sem valor (ou seja, **0,00**).
4. Salve as alterações.
5. Certifique-se de vincular essa tabela progressiva específica à regra financeira que atende aos fornecedores não optantes pelo desconto simplificado.

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/39280895293591)](https://centraldeatendimento.totvs.com/hc/article_attachments/39280895293591)

Exemplo: **Com Desconto Simplificado** (Padrão Lei): Título de R$ 5.100,00 -> IR de R$ 35,81

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/39280884264471)](https://centraldeatendimento.totvs.com/hc/article_attachments/39280884264471)

Exemplo: **Sem** **Desconto Simplificado**: Título de R$ 5.100,00 -> IR de R$ 194,19

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/39280884266391)](https://centraldeatendimento.totvs.com/hc/article_attachments/39280884266391)

Exemplo de Regra Financeira  s/ Desconto Simplificado

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/39280895297431)](https://centraldeatendimento.totvs.com/hc/article_attachments/39280895297431)[![](https://centraldeatendimento.totvs.com/hc/article_attachments/39280884270487)](https://centraldeatendimento.totvs.com/hc/article_attachments/39280884270487)

**Saiba Mais:**

[FISA170 - IRPF conforme a Lei 15.270/2025 para títulos avulsos no Financeiro](https://tdn.totvs.com/pages/releaseview.action?pageId=1043719216)

[Configurador de Tributos - Regras Financeiras](https://tdn.totvs.com.br/display/public/PROT/Configurador+de+Tributos+-+Regras+Financeiras)
