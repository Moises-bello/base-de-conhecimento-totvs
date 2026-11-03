---
article_id: 17082346859799
category: eSocial - Gerar XML/ Integração Evento
content_hash: e40641814196980ef1b31a32885f1a3244977c7ccdc93c53a293a8c545b27b0d
fetched_at: '2026-06-28T22:47:11.889253+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Ao encaminhar o evento de admissão do trabalhador
  para o governo ocorre o erro 356: O Tipo do Trabalhador é incompatível com a classificação
  tributária do empregador'
type: support-article
updated_at: '2026-04-17T18:05:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17082346859799-RH-RM-FOP-eSocial-Ao-encaminhar-o-evento-de-admiss%C3%A3o-do-trabalhador-para-o-governo-ocorre-o-erro-356-O-Tipo-do-Trabalhador-%C3%A9-incompat%C3%ADvel-com-a-classifica%C3%A7%C3%A3o-tribut%C3%A1ria-do-empregador
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17082361820439) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao encaminhar o S-2200 ou S-2300 ocorre o erro **356** **O Tipo do Trabalhador é incompatível com a classificação tributária do empregador**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17081931330327)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**  
Esse incidente ocorre ao encaminhar um evento de admissão em que o código da categoria do trabalhador não é compatível com a classificação tributária do empregador.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Verifique no **XML de admissão qual o código de categoria do trabalhador**, através da tag *codCateg*;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17082024000791)

2. Verifique no **S-1000 qual é a classificação tributária**, através da tag *classTrib*;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17082013103767)

3. Será necessário verificar no **S-1020 qual é o tipo de lotação tributária** que o trabalhador está associado. Sendo assim, acesse o evento de tabela de lotação tributária e localize a tag *tpLotacao;*

*![](https://centraldeatendimento.totvs.com/hc/article_attachments/17082105892503)*

4. Após acesse o Anexo I do Leiautes do eSocial Tabelas e identifique na **Tabela 11**se as informações de categoria do trabalhador, classificação tributária e tipo de lotação são compatíveis.  
No exemplo acima a categoria do trabalhador 201 é compatível com a classificação tributária 09 e tipos de lotações tributárias 01 ou 08. Neste caso, faz-se necessário conferir quais das informações foram cadastradas incorretamente e alterá-las.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17082203917591)

**Saiba mais:**

Para saber mais consulte o link abaixo:

* [Documentação Técnica - eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)
