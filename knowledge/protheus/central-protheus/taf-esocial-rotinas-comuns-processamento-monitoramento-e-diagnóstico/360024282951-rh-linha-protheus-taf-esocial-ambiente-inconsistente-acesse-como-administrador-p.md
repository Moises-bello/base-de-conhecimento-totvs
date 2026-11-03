---
article_id: 360024282951
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: fc9b28d96ba71901397e517fa9496578a22ebdbc02dd3fe8ddb52fc9dd1e02c7
fetched_at: '2026-06-28T22:45:21.127663+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Ambiente Inconsistente, ACESSE COMO ADMINISTRADOR
  para mais
type: support-article
updated_at: '2026-06-26T11:52:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024282951-RH-Linha-Protheus-TAF-eSocial-Ambiente-Inconsistente-ACESSE-COMO-ADMINISTRADOR-para-mais
---

**Dúvida**  
Ao tentar acessar modulo 84 - TAF - Totvs Automação Fiscal, é apresentado a mensagem abaixo:

Ambiente Inconsistente, ACESSE COMO ADMINISTRADOR para mais

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360022285332)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - eSocial -Todas as versões   
  
**Solução**

Geralmente esse problema ocorre quando é apresentando algum problema durante a Wizard de configuração. No link abaixo, identifiquei a informação:   
  
<http://tdn.totvs.com/pages/releaseview.action?pageId=185752114>  
  
"Caso ocorra algum problema durante a execução da Wizard de configuração o usuário deve alterar o conteúdo do parâmetro **MV\_TAFWIZ**para **.F.**para liberar o ambiente do TAF aos usuários, porém as rotinas como geração das obrigações fiscais e integração das informações NÃO serão executadas até o problemas ser sanado e o parâmetro **MV\_TAFWIZ**alterado novamente para **.T."**Outro ponto identificado com o problema apresentando na mensagem acima, é por motivo do usuário que esta tentando acessar o TAF não ser um usuário administrador do sistema.  
  
Como ao acessar o módulo 84, o mesmo tenta atualizar as tabelas autocontidas, o acesso é bloqueado pois é identificado que o módulo esta sendo acessado por um usuário não administrador.   
  
A atualização das tabelas autocontidas somente é efetuada quando o módulo é acessado por um usuário administrador.   
  
Uma sugestão de teste é acessar o módulo 84 com um usuário de administrador para que  o mesmo atualize as tabelas autocontidas, e em seguida, solicite o usuário diferente de administrador um novo acesso.

"Caso mesmo realizando a atualização das "Tabelas Autocontidas " não resolva é necessário enviar ao Suporte o arquivo " Analise de IDS" para que o suporte verifique se existe algum ID duplicado.

Para enviar o  arquivo  de Analise de IDS acesse a "Tela de Diagnostico" :

[Automação Fiscal - Rotinas Comuns - Como acessar a tela de diagnóstico no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17988545143063)

Em seguida clique em "Outras Ações" e depois " "Analisar numeração de IDs"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26612044013975)
