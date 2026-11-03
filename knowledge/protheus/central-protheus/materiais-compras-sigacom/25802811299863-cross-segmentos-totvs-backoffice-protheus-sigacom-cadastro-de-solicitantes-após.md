---
article_id: 25802811299863
category: Materiais - Compras (SIGACOM)
content_hash: 62e6929c85ce624b5cc0b557f81811eeea991867c48ebed1697f35cbae3fdfdc
fetched_at: '2026-06-28T22:41:14.282171+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Cadastro de Solicitantes
  - Após migração de versão as Entidades Contabeis vinculadas e existentes na tabela
  DBK não são visualizadas no Cadastro
type: support-article
updated_at: '2025-06-10T14:27:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25802811299863-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Cadastro-de-Solicitantes-Ap%C3%B3s-migra%C3%A7%C3%A3o-de-vers%C3%A3o-as-Entidades-Contabeis-vinculadas-e-existentes-na-tabela-DBK-n%C3%A3o-s%C3%A3o-visualizadas-no-Cadastro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25802824966423) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Após migração de versão as Entidades Contábeis vinculadas e existentes na tabela DBK não são visualizadas no Cadastro

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras - Todas as versões

**Solução**Referente a esta ocorrência, uma possibilidade existente que orienta-se a verificação, é a análise na base de dados em questão nos registros da tabela ***DBK,*** checando se o campo ***DBK\_DOMINI*** se encontra Vazio, sendo que no padrão ele deve possuir a mesma informação contida no campo análogo da tabela ***SAI***, campo ***AI\_DOMINIO:***

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25803055815959)

Nesta situação, orienta-se a realização da manutenção da base de dados, nos registros da tabela ***DBK***, com o preenchimento do campo ***DBK\_DOMINI*** com a mesma informação do campo ***AI\_DOMINIO*** do registro referente a este cadastro.

Caso necessite de apoio para a manutenção de registros na base de dados, orientamos a verificação junto ao ESN Totvs para solicitação de um analista especialista em loco para essa manutenção.

***Saiba Mais :***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como é definido cadastro de Solicitantes ( MATA084 ) no Módulo de Compras ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007049611-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-%C3%A9-definido-cadastro-de-Solicitantes-MATA084-no-M%C3%B3dulo-de-Compras)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
