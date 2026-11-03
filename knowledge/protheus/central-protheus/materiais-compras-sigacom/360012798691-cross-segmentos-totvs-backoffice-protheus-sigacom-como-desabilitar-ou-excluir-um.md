---
article_id: 360012798691
category: Materiais - Compras (SIGACOM)
content_hash: 3db9aa84eefaaa26251b25ff6f491aa8cc34f388b7bda59e812a333eb582de47
fetched_at: '2026-06-28T22:41:07.606575+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como desabilitar ou
  excluir um aprovador do Grupo de Aprovadores ?
type: support-article
updated_at: '2026-02-09T13:24:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012798691-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-desabilitar-ou-excluir-um-aprovador-do-Grupo-de-Aprovadores
---

**Dúvida**  
Como desabilitar ou excluir um aprovador do Grupo de Aprovadores ?  
  
**Ambiente**  
Protheus – Compras – A partir da versão 12.1.17  
  
**Solução**  
À partir da release P12.1.17 não é mais possível excluir o Aprovador do Grupo de Aprovação, pois ao tentar excluir gera a mensagem de: FWFORMBEFORE - Violação de Integridade AL\_COD

![TABELA_SAL.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360008806552)

Neste caso é preciso Bloquear o Aprovador no próprio cadastro do Grupo de Aprovação criando o campo ***AL\_MSBLQL*** através do Configurador e no grupo de aprovação deixar este campo criado com o conteúdo = SIM.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25638703458455)

Desta forma o aprovador ficará bloqueado no grupo de Aprovação e não receberá documentos na alçada deste Grupo de Aprovação para que este libere pela rotina MATA094.

Abaixo, segue telas demonstrativas para habilitação do campo "Bloqueado?" (AL\_MSBLQL):

**Tela 1** - Abaixo mostra o acesso pelo configurador, na tabela SAL clicar no icone "Campos reservados"

![tela_1.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360008841351)

**Tela 2** - Ticar a opção "Bloqueio Automático", clique no botão finalizar e salve no Disquete do configurador

![tela_2.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360008841371)

**Tela 3** - Tela com o campo já configurado após o processo anterior

![tela_4.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360008841411)

**Tela 4** - Abaixo o Grupo de Aprovadores com o campo em funcionamento

![tela_5.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360008807632)

***Importante:***

Caso o campo não apareça na rotina verifique se o nível de campo é o mesmo do usuário logado:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5280036183447)

Ou Ajuste o nível do campo no configurador para Nível 1 assim todos usuários terão acesso a visualização do campo.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8427008359191)

***Obs:*** Essa nova configuração do grupo será aplicada para novos registros criados, os antigos registros necessitam ser aprovados pelo usuário que foi bloqueado ou alterados para entrar na nova regra de aprovação.

***Saiba Mais :***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como configurar para que outros usuários sem ser o Usuário Administrador possa visualizar o Campo Bloqueado AL\_MSBLQL no Grupo de Aprovação?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9350374476439-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-configurar-para-que-outros-usu%C3%A1rios-sem-ser-o-Usuario-Administrador-possa-visualizar-o-Campo-Bloqueado-AL-MSBLQL-no-Grupo-de-Aprova%C3%A7%C3%A3o)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como configurar para que Superiores tenham acesso as pendências de subordinados na aprovação de documentos ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020865271-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-configurar-para-que-Superiores-tenham-acesso-as-pend%C3%AAncias-de-subordinados-na-aprova%C3%A7%C3%A3o-de-documentos-?source=search)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Substituição de Aprovadores no Grupo de Aprovação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016495272-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Substitui%C3%A7%C3%A3o-de-Aprovadores-no-Grupo-de-Aprova%C3%A7%C3%A3o?source=search)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
