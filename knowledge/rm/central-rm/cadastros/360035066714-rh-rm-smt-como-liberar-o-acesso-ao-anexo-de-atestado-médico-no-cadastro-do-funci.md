---
article_id: 360035066714
category: Cadastros
content_hash: 09654ab367ddbb6608af969d4d11427d01b66093e014269c311b096e146b42ac
fetched_at: '2026-06-28T22:47:36.420519+00:00'
product: rm
section_id: 1500000834961
source: central-rm
title: RH - RM - SMT - Como liberar o acesso ao anexo de atestado médico no cadastro
  do funcionário
type: support-article
updated_at: '2025-11-28T21:07:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035066714-RH-RM-SMT-Como-liberar-o-acesso-ao-anexo-de-atestado-m%C3%A9dico-no-cadastro-do-funcion%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16035467680663) Tempo aproximado para leitura: 00:01:30 min**  
  
**Dúvida**  
Como liberar o acesso ao anexo de atestado médico do cadastro do funcionário?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Segurança e Saúde Ocupacional – A partir da versão 11.80

**Solução**

Para ter acesso ao anexo de atestados, siga o passo a passo abaixo: 

1. Acesse no módulo de **Gestão de Pessoas**, o menu **Ambiente** | **Parâmetros**  | **Integração entre Sistemas** e confira se o RM Vitae e o RM Labore estão integrados. Caso não esteja habilite a integração entre os módulos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26948161519895)

2. Acesse o módulo de **Serviços Globais**, o menu **Segurança** | **Usuários** e selecione o sistema **Segurança e Saúde Ocupacional.** Edite o usuário que não visualiza o anexo e clique na aba **Segurança** e confira quais perfis estão associados para a coligada em questão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26948161523991)

3. Ainda no menu **Segurança** em **Serviços Globais**, acesse **Perfis** e selecione o sistema **Segurança e Saúde Ocupacional.** Edite o perfil vinculado ao usuário e valide se a opções **01.01.03.05.01 - Incluir atestado**, **01.01.03.05.02 - Excluir atestado** e **01.01.03.05.03 - Editar atestado** estão liberados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26948138193559)

Após liberar as permissões, faça logout/login e valide se o menu estará acessível. Caso ainda assim, não apareça, reinicie o serviço do host do RM iniciado.

[Framework - Linha RM - Frame - Reiniciar Host](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000095827)

**Importante**

* Caso ​tenha mais de um perfil de acesso vinculado ao usuário, a liberação deve ocorrer para todos os perfis.
* Os números dos menus podem ter uma variação de acordo com a versão, caso não localize pesquise pelo nome.

**Saiba mais**

Para maiores informações, acesse:   
- [RH - RM - SMT - Dúvidas frequentes: Atestados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23511154711447)
