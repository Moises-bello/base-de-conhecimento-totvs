---
article_id: 4409677920663
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: ada8ad304dd5875dc2f8844e3d93f0c2624280fb7c62460d0e2e801147cf6928
fetched_at: '2026-06-28T22:39:07.866924+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como restringir acesso
  as rotinas do Estoque Custos?
type: support-article
updated_at: '2025-12-11T14:14:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409677920663-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-restringir-acesso-as-rotinas-do-Estoque-Custos
---

É possível restringir o acesso a menus específicos da rotina MATA010 ou outras do módulo Estoque Custos no Protheus. A restrição é feita via Configurador (SIGACFG), selecionando o usuário e configurando limitações em "Outras Ações / Restrição de rotina no menu". Pode-se bloquear acesso total ou parcial, como exclusão de registros. Também é possível aplicar restrições por grupo/privilégios, facilitando a gestão.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36942721470487) Tempo aproximado para leitura: **00:02:45 min**

**Dúvida**

É possível restringir acesso, sob alguns menus da rotina MATA010, ou demais rotinas do módulo Estoque Custos?   
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Sim, é possível efetuar a restrição de acesso as rotinas no Protheus com exemplo no passo a passo abaixo para a rotina CADASTRO DE PRODUTOS (MATA010), **esse processo pode ser efetuado para qualquer rotina do ERP**.

Para efetuar restrições de rotinas específicas dentro do Protheus, acessar o **Configurador (SIGACFG)** com o cadastro do Administrador, e executar a configuração abaixo:

Local: **Usuário/ Senhas / Usuários**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409681815959)

Selecionar o **usuário** que deseja restringir o acesso, e clicar na opção **Alterar**:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409681836311)

Conferir os módulos liberados para acesso desse usuário. No exemplo utilizado o usuário tem acesso somente ao módulo 04 - Estoque Custos (SIGAEST).

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409681853847)

Para selecionar a rotina que deve ter acesso restrito ao usuário: Clicar em **Outras Ações** / **Restrição de rotina no menu**:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409681860503)

Então, demonstrará todas as rotinas, as quais o usuário tem acesso:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409681872919)

Selecionar a rotina desejada e clicar em Acesso, no exemplo abaixo foi utilizado a rotina MATA010:

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409681879063)

Nesta opção existe a possibilidade de restringir o acesso do usuário a todos os itens da rotina ou apenas alguns. Neste exemplo, será restringido o acesso do usuário para efetuar a **Exclusão** de informações na rotina:

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409681888919)

Quando o usuário for acessar a rotina MATA010- Atualizações/Cadastros/Produtos, ao tentar Excluir algum registro sobre a opção **"Outras ações/Excluir"**, o sistema apresentará a seguinte mensagem:

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409676804119)

Dessa forma, o usuário não tem permissão a exclusão na rotina, as restrições também podem ser configuradas via "**Grupo / Privilégios**", para no caso não precisar configurar usuário por usuário, esse conceito pode ser aplicado, seguindo o mesmo conceito de restrição por usuário.

Onde é se criado um "Privilegio" de acesso em uma rotina, e o mesmo é se atribuído a um "Grupo".

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409676860823)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
