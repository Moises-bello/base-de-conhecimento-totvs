---
article_id: 360024560374
category: Meu RH - Home
content_hash: 4023f290da9af25ae35ea4eddeb4e999f84fdc2e2fad7ad006dca036b8c4824b
fetched_at: '2026-06-28T22:47:34.675108+00:00'
product: rm
section_id: 1500000861702
source: central-rm
title: RH - RM - Meu RH - Como bloquear alterações no perfil do colaborador no Meu
  RH
type: support-article
updated_at: '2024-10-07T16:44:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024560374-RH-RM-Meu-RH-Como-bloquear-altera%C3%A7%C3%B5es-no-perfil-do-colaborador-no-Meu-RH
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22327980152983) Tempo aproximado para leitura: 00:02:59 min  
  
Dúvida**Como bloquear a edição de dados relacionados ao perfil do funcionário no Meu RH.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir da versão 12.1.17  
  
**Solução**Para desabilitar a edição dos campos do perfil do usuário no **Meu RH**, basta acessar basta acessar o caminho **Serviços Globais | Segurança | Perfil |** no Perfil associado ao usuário e proibir o acesso nos menus abaixo:  
  
[19.01.01.01.01] Identificação  
[19.01.01.02.01] Endereço  
[19.01.01.03.01] Documentos  
[19.01.01.03.02] Anotações

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22328079110935)

Para bloquear a edição outros campos como Telefone basta acessar o caminho **Serviços Globais | Segurança | Perfil | Acesso a Campos |** Localizar a tabela **PPESSOA** onde nesta tabela você terá acesso aos campos, ao selecionar o campo desejado será possível escolher entre as opções de **Permissões**Pode Consultar e Pode Alterar.  
Ao desmarcar a opção **Pode Consultar** o funcionário não terá mais acesso a visualizar esta opção.  
Ao desmarcar apenas opção **Pode Alterar** o funcionário irá visualizar porem não irá editar.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411244799895)

**Importante**  
Se o usuário estiver associado a mais de um perfil, deverá proibir o acesso em todos os perfis associados ao usuário, pois se algum perfil associado tiver acesso, o mesmo estará com acesso permitido para alteração.
