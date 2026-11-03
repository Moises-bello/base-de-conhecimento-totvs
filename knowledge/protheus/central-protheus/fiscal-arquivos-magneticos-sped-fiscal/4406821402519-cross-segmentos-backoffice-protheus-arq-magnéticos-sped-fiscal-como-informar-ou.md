---
article_id: 4406821402519
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: b4fb4d6c743a5eba50c92c95c83959a6b6f6c7420347d8b750d638b6325169ab
fetched_at: '2026-06-28T22:42:00.766434+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Arq. Magnéticos - SPED FISCAL - Como
  informar ou alterar o perfil da empresa para geração do Sped Fiscal?
type: support-article
updated_at: '2022-07-25T16:44:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406821402519-Cross-Segmentos-Backoffice-Protheus-Arq-Magn%C3%A9ticos-SPED-FISCAL-Como-informar-ou-alterar-o-perfil-da-empresa-para-gera%C3%A7%C3%A3o-do-Sped-Fiscal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**  
Como informar ou alterar o perfil da empresa para geração do Sped Fiscal?

**Ambiente**Cross Segmento - TOTVS Backoffice (**Linha Protheus**) - A partir da versão **12.1.17.**  
  
**Solução**Para gerar o perfil da empresa no registro **0000- Abertura do Arquivo Digital e Identificação da Entidade,** campo **14- IND\_PERFIL** o sistema valida  o conteúdo do parâmetro **MV\_PRFSPED.**

Se o conteúdo for vazio, será apresentada a pergunta de perfil no Wizard da rotina.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406815699095/mceclip0.png)

Com o parâmetro vazio á aberta a possibilidade de definir em qual perfil o Sped Fiscal será gerado.  Se no parâmetro for definido o perfil, não é possível alterar a informação na wizard de geração do Sped Fiscal, visto que, o sistema valida primeiro o conteúdo do parâmetro e passa a levar a informação fixamente ao arquivo.
