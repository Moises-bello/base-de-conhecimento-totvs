---
article_id: 22540793658647
category: PMS - Projetos
content_hash: a7e0dacebe5a1b337c6cb96cd411e54ed4bbe3974e86db10aebedf649d9a9b21
fetched_at: '2026-06-28T22:37:14.966542+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Quantidade do item e geração
  de solicitações de compras pelo projeto (MV_PMSCSC)
type: support-article
updated_at: '2024-04-05T12:16:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22540793658647-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Quantidade-do-item-e-gera%C3%A7%C3%A3o-de-solicita%C3%A7%C3%B5es-de-compras-pelo-projeto-MV-PMSCSC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22540782545047) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como administrar a quantidade do item e geração de solicitações de compras pelo projeto (MV\_PMSCSC)  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAPMS - Todas as versões.  
  
**Solução**

Pode ser configurado como gerar ou não solicitações de compras pelos projetos (SIGAPMS), assim como quando gerar, quantos itens faltantes serão solicitados, ele depende do parâmetro MV\_PMSCSC.

**Funcionamento MV\_PMSCSC = .T.**

Enquanto não for gerado documento de entrada para baixar a solicitação de compras, o sistema entenderá que foi requerido de maneira geral ao sistema a quantidade 10, então todos os projetos poderiam usar esse saldo. Só será gerado solicitação de compras agora, caso seja requerido uma quantia maior que as informadas anteriormente (total do item no campo AFG\_QUANT)

Exemplo 1:

É criado o primeiro planejamento para geração de solicitação de compras com quantidade 10:  
"Projeto" AFA\_PROJET = 'PMS001'

"Item" AFA\_ITEM = '01'

"Quantidade" AFA\_QUANT = 10 (AFA - Recursos do projeto)

**Resultado (1/2):**

* "Projeto" AFG\_PROJET = 'PMS001'
* "Quantidade" AFG\_QUANT = 10 (AFG - Solicitação de Compras x Projeto)
* "Quantidade" C1\_QUANT = 10 (SC1 - Solicitação de Compras)

Ao tentar criar um planejamento novo do mesmo item em outro projeto ou não com quantidade (AFA\_QUANT) do mesmo item anterior:

* "Projeto" AFA\_PROJET = 'PMS001'
* "Item" AFA\_ITEM = '02'
* "Quantidade" AFA\_QUANT = 10

NÃO será gerado a solicitação de compras**,** pois o sistema entende que no momento, há uma solicitação desse item genérica para atender a demanda.  
  
**Resultado (2/2) ao criar a outra solicitação do mesmo item com quantia menor ou igual a solicitação anterior, no mesmo projeto em um projeto diferente:**  
Não gera a tabela "AFG" e nem "SC1"

Exemplo 2:

É criado o primeiro planejamento para geração de solicitação de compras com quantidade 10:

* "Projeto" AFA\_PROJET = 'PMS001'
* "Item" AFA\_ITEM = '01'
* "Quantidade" AFA\_QUANT = 10 (AFA - Recursos do projeto)

**Resultado (1/2):**

* "Projeto" AFG\_PROJET = 'PMS001'
* "Quantidade" AFG\_QUANT = 10 (AFG - Solicitação de Compras x Projeto)
* "Quantidade" C1\_QUANT = 10 (SC1 - Solicitação de Compras)

Ao tentar criar um planejamento novo do mesmo item em outro projeto com quantidade (AFA\_QUANT = 40) maior que a solicitação do item anterior (AFA\_QUANT = 10), SERÁ gerado a solicitação de compras no valor da diferença solicitada, pois o sistema entende que a requisição vigente anterior não atende completamente a demanda:

* "Projeto" AFA\_PROJET = 'PMS001'
* "Item" AFA\_ITEM = '02'
* "Quantidade" AFA\_QUANT = 40

**Resultado (2/2) ao criar a outra solicitação do mesmo item com quantia menor ou igual a solicitação anterior, no mesmo projeto em um projeto diferente:**

* "Projeto" AFG\_PROJET = 'PMS001'
* "Quantidade" AFG\_QUANT = 30 (AFG - Solicitação de Compras x Projeto)

[40 (pedida na nova solicitação) - 10 (pedido na primeira solicitação) = 30]

* "Quantidade" C1\_QUANT = 30 (SC1 - Solicitação de Compras)

**Funcionamento MV\_PMSCSC = .F.**

Não valida o total do item em outros solicitações de projetos na tabela "AFG - Solicitação de Compras x Projeto"

Exemplo 1:  
É criado o planejamento para geração de solicitação de compras com quantidade 10:

* "Projeto" AFA\_PROJET = 'PMS001':
* "Item" AFA\_ITEM = '01'
* "Quantidade" AFA\_QUANT = 10 (AFA - Recursos do projeto)

**Resultado (1/2):**

* "Projeto" AFG\_PROJET = 'PMS001'
* "Quantidade" AFG\_QUANT = 10 (AFG - Solicitação de Compras x Projeto)
* "Quantidade" C1\_QUANT = 10 (SC1 - Solicitação de Compras)

Ao tentar criar um planejamento novo do mesmo item em outro projeto com quantidade (AFA\_QUANT) do mesmo item anterior, SERÁ gerado a solicitação de compras, mesmo que em outros projetos tenha sido requerido a mesma quantia ou uma quantia menor.

* "Projeto" AFA\_PROJET = 'PMS001'
* "Quantidade" AFA\_QUANT = 10
* "Item" AFA\_ITEM = '02'

**Resultado (2/2) ao criar a outra solicitação do mesmo item com quantia menor ou igual a solicitação anterior, no mesmo projeto em um projeto diferente:**

* "Projeto" AFG\_PROJET = 'PMS001'
* "Quantidade" AFG\_QUANT = 10 (AFG - Solicitação de Compras x Projeto)
* "Quantidade" C1\_QUANT = 10 (SC1 - Solicitação de Compras)
