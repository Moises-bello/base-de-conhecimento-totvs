---
article_id: 12036245382295
category: Chão de Fábrica (SIGASFC)
content_hash: d23bb91f4aaee3ce47b32380a25d4d6b31845e62b2606783dd06d21838912fd2
fetched_at: '2026-06-28T22:42:49.841797+00:00'
product: protheus
section_id: 360005696234
source: central-protheus
title: Manufatura - Linha Protheus - SIGASFC - Erro faltam dados para importação
type: support-article
updated_at: '2023-02-13T14:59:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12036245382295-Manufatura-Linha-Protheus-SIGASFC-Erro-faltam-dados-para-importa%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:48 min****Ocorrência**Ao tentar importar apontamentos de produção através da rotina **SFCA320 - Importação de apontamento**, e preencher somente os campos obrigatórios indicados na tela, a importação não ocorre e apresenta o erro **Faltam Dados para Importação**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Chão de Fábrica (SIGASFC) - Versão 12  
  
**Causa**Esse cenário ocorre porque apesar dos demais campos não serem obrigatórios, eles podem ser informados no apontamento de produção, desse modo, para que ocorra a importação correta do apontamento, deve-se informar o conteúdo em branco para esses dados não preenchidos;  
  
**Solução**  
Para os campos não preenchidos informe o conteúdo em branco, conforme imagem abaixo:

![Arquivo.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/12036068536855)
