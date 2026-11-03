---
article_id: 360045164793
category: Chão de Fábrica (SIGASFC)
content_hash: 01cf352836f8fb63f96fd6915ca71947a414f29c5ec7f266071fdcf38277db9e
fetched_at: '2026-06-28T22:42:49.848114+00:00'
product: protheus
section_id: 360005696234
source: central-protheus
title: Manufatura - Linha Protheus - SIGASFC - Funcionalidade do parâmetro MV_REQAUT
  no Chão de Fábrica
type: support-article
updated_at: '2022-03-28T16:45:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045164793-Manufatura-Linha-Protheus-SIGASFC-Funcionalidade-do-par%C3%A2metro-MV-REQAUT-no-Ch%C3%A3o-de-F%C3%A1brica
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:27 min**  
**Dúvida**Qual a funcionalidade do parâmetro **MV\_REQAUT** **-****Verifica se o Sistema deve ou não gerar requisições automáticas**no **Chão de Fábrica**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Chão de Fábrica (SIGASFC) - Versão 12   
  
**Solução**O parâmetro **MV\_REQAUT** para o **Chão de fábrica** tem funcionalidade diferente que para o **PCP - Planejamento e Controle da Produção**.  
Quando o parâmetro **MV\_REQAUT** estiver igual a **A** os componentes que serão requisitados são os que foram cadastrados no **PCP** no momento da abertura da **OP - Ordem de produção**, gerando movimentação de requisição como **RE1 - Requisição Automática**.  
Quando o parâmetro **MV\_REQAUT** estiver igual a **D** os componentes que serão requisitados são os que estão apresentados na tela de apontamento do **Chão de Fábrica**. Neste caso é possível incluir mais componentes ou excluí-lo, gerando movimentação de requisição como **RE0 - Requisição Manual**.  
Quando o parâmetro for utilizado como **D**, ao realizar o apontamento é necessário excluir os componentes que já foram requisitados manualmente, caso contrário o Sistema irá requisitar novamente.
