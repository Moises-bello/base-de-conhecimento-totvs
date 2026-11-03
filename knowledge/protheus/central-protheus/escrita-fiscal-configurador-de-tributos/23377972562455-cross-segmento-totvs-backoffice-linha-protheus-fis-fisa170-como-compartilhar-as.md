---
article_id: 23377972562455
category: Escrita Fiscal - Configurador de Tributos
content_hash: 83335cbd096b52405c7e57db133d6d2d3eae7ec97510b03b7cf82e7e29b16be6
fetched_at: '2026-06-28T22:39:17.380575+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Como compartilhar
  as regras dos perfis entre filias no FISA170?
type: support-article
updated_at: '2025-11-03T15:02:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23377972562455-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-compartilhar-as-regras-dos-perfis-entre-filias-no-FISA170
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23377972538647) Tempo aproximado para leitura: **00:03:00min** **Dúvida**Como compartilhar as regras dos perfis entre filias no FISA170?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

Dentro do módulo do SIGACFG (Configurador > Base de Dados > Dicionário > Bases de Dados > Tabela “XXX”), será necessário proceder com o compartilhamento das seguintes tabelas:

**Perfis**

F20, F21, F22, F23, F24, F25, F26 e CIO

**Cadastros**

SB1, SA1 e SA2

**Atenção:** Lembre-se de realizar o backup das tabelas antes de compartilhá-las para evitar a perda dos cadastros existentes.

* Cadastros dos produtos

![](https://totvssuporte.zendesk.com/attachments/token/joeK856tmiXyGiBMzdcPR0Zyp/?name=FISA170+-+MATA010.gif)

* Perfil de Produto

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23377972540567)

Se possuir mais de uma regra de perfil cadastrada como apresentado, ao acionar o comando "Outras Ações > Facilitadores", poderá selecionar mais regras para vincular os produtos desejados.
