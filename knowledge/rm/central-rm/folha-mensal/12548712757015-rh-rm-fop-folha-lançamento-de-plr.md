---
article_id: 12548712757015
category: Folha Mensal
content_hash: cbc283081b1175816ef73a9a2005566be7a310000a1170be0ba3f978971d95e8
fetched_at: '2026-06-28T22:46:58.263871+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Folha: Lançamento de PLR'
type: support-article
updated_at: '2024-09-16T18:41:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12548712757015-RH-RM-FOP-Folha-Lan%C3%A7amento-de-PLR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Como realizar lançamento de PLR?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
Para lançamento correto de PLR é necessário verificar se a tabela de IRRFPL está devidamente cadastrada em **Administração de Pessoal - Cálculos - Tabelas de Cálculo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13056993784599)** **![](https://centraldeatendimento.totvs.com/hc/article_attachments/13057029011351)**  
Verificar se existem cadastrados os seguintes eventos:

* [CC121 - Pensão Alimentícia Participação nos Lucros;](https://tdn.totvs.com/pages/viewpage.action?pageId=452718805)
* [CC126 - Participação nos Lucros;](https://tdn.totvs.com/pages/viewpage.action?pageId=452718798)
* [CC127 - IRRF Participação nos Lucros;](https://tdn.totvs.com/pages/viewpage.action?pageId=452718705)
* [CC143 - Dedutível  IRRF Participação nos Lucros;](https://tdn.totvs.com/pages/viewpage.action?pageId=452718492)

Devido às particularidades de cada empresa (sindicato) para pagamento de PLR, o valor do evento não é calculado automaticamente pelo sistema, devendo a empresa possuir uma fórmula de valor vinculada ao ao evento. O cálculo do IRRF é realizado automaticamente.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13057042243351)  
  
**Importante**  
Sugerimos que o evento de PLR seja lançando pelo grupo de eventos, ficando a critério da empresa se irá criar um novo grupo ou incluir em um grupo existente.   
  
A fórmula deverá ser criada internamente pela empresa.  
  
**Saiba mais**[RH - RM - FOP - Lançamento do Grupo de Eventos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014011632-RH-RM-FOP-Lan%C3%A7amento-do-Grupo-de-Eventos)  
[RH - RM - FOP - Fórmulas e Funções](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061764374-RH-RM-FOP-F%C3%B3rmulas-e-Fun%C3%A7%C3%B5es)  
[RH - RM - FOP - Códigos de Cálculo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412890806807-RH-RM-FOP-C%C3%B3digos-de-C%C3%A1lculo)
