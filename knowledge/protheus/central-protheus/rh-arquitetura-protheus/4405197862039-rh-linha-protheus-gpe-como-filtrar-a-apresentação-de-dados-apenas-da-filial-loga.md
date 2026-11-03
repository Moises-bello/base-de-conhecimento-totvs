---
article_id: 4405197862039
category: RH - Arquitetura Protheus
content_hash: 27dd59009e88321f09b65b318a105a25373214b69c4b3274ff47886b15544a31
fetched_at: '2026-06-28T22:43:03.204600+00:00'
product: protheus
section_id: 206960847
source: central-protheus
title: RH - Linha Protheus - GPE - Como filtrar a apresentação de dados apenas da
  filial logada
type: support-article
updated_at: '2024-11-12T14:30:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405197862039-RH-Linha-Protheus-GPE-Como-filtrar-a-apresenta%C3%A7%C3%A3o-de-dados-apenas-da-filial-logada
---

**Dúvida**Como filtrar as apresentações de dados no Gestão de Pessoal apenas da filial logada?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12  
  
**Solução**Para que no acesso ao módulo **Gestão de Pessoal** seja apresentado apenas os registros da **Filial logada**, é necessário que no cadastro do **Usuário - CFGA510** ou **Grupo de usuários - CFGA520** na aba **Acesso**, o item 114 esteja desmarcado.

1 - Acesse o seguinte caminho no módulo Configurador - SIGACFG do menu: **Usuário**->**Usuários ou Grupos**: selecione o usuário ou grupo no qual deseja efetuar esta parametrização, clique em Alterar.  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405193043479/mceclip1.png)  
  
2 - Localize a aba **Restrições** de Acesso, seguida da aba **Acessos**, efetue a busca pelo código **114 - MBrowse - Visualiza outras filiais**, desmarque esta opção, para que não seja possível executar processos de outras filiais desmarque o **115 - MBrowse - Edita registros de outras filiais**.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405192955671/mceclip0.png)  
  
**Saiba Mais**  
[Configurar usuários](https://tdn.totvs.com/pages/viewpage.action?pageId=271186036)  
[Criar um Grupo de Usuários](https://tdn.totvs.com/pages/viewpage.action?pageId=271388115)
