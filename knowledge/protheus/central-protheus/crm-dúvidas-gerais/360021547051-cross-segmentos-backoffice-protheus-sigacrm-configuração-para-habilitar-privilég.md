---
article_id: 360021547051
category: CRM - Dúvidas Gerais
content_hash: 6f0fbaea65aec3c2c00caeadd6ff6d9580b0965637391e17771229e0ac266acf
fetched_at: '2026-06-28T22:40:27.654792+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGACRM - Configuração para habilitar
  privilégios no sistema
type: support-article
updated_at: '2024-04-25T12:09:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021547051-Cross-Segmentos-Backoffice-Protheus-SIGACRM-Configura%C3%A7%C3%A3o-para-habilitar-privil%C3%A9gios-no-sistema
---

**Dúvida**

Como habilitar os privilégios no configurador  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGACRM - A partir da release 12  
  
  
**Solução**

Definição de Privilégios do Usuário:

1.0 - Acesse Configurador/ Usuário/ Senha/ Privilégios

![pri](https://centraldeatendimento.totvs.com/hc/article_attachments/15917686730647)

1.1 - Selecionar a opção: (Privilégios) e clicar em Incluir;

![pri2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15917695427863)

1.2 - Lembre-se de verificar o campo: Acesso: pois se deixar como (Negado) - quando o usuário acessar a rotina o sistema irá gerar essa mensagem;

![pri3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15917686739863)

1.3 - Para que possa acessar a rotina cadastrada é necessário deixar como: (Permitido);

![pri4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15917695434903)

2.0 - Selecionar a rotina na aba: (Transação/Rotina), exemplo: CRMA070  
-  O sistema carrega as informações automaticamente, conforme abaixo:

![pri5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15917695438743)

2.1 - O processo de privilegio consegue determinar acessos para o usuário nas rotinas cadastradas.

* Veja que na opção: (Alterar) esta como: (Permitido) ou pode deixar (Negado) para o usuário não ter permissão.

![pri6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15917695442711)

* - Caso deseja cadastrar mais de uma rotina no privilégios o sistema permite.
* Clique em confirmar as informações.

3.0 - Após ter configurado os privilégios, é necessário acessar o cadastrado de usuários:

3.1 - Selecionar um determinado usuário que irá ter acesso restrição de acesso:  
  
3.2 - Clica na opção: Outras Ações: (Privilégios);

![pri7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15917695447063)

4.0 - Restrição de Acessos  
  
4.1 - Selecionar a Regra que cadastrou e deixar o campo: Aprovador (SIM);

![pri8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15917686763671)

* Salvar as informações

4.2 - Logar com o usuário (cadastrado) e amarrado no cadastro de privilégios.

* Acessar a rotina: Atualizações - Vendas - Contas - CLIENTES:  
    
  Ao clicar em alterar um cliente que não seja da mesma carteira do vendedor que esta logado, o sistema irá gerar a mensagem abaixo:

![pri9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15917686766103)

Mais se clicar em alterar em um cliente que seja da mesma carteira do vendedor que esta logado o sistema não gera mensagem, o processo esta correto.

**Observações:**

* Para o sistema validar a carteira de entidades como: Clientes, Suspect, Prospect é necessário que tenha uma estrutura de negocio cadastrada, dessa forma cada vendedor irá visualizar somente sua área de trabalho.
* Esse processo é valido para qualquer procedimento do sistema, que envolva área de trabalho

**Saiba mais:**

**[Restrições de usuário no Faturamento e CRM](https://tdn.totvs.com/pages/viewpage.action?pageId=336403802)**

**[Controle de Privilégios do CRM](https://tdn.totvs.com/pages/viewpage.action?pageId=439692702)**

**[COMO REFAZER OS PRIVILÉGIOS DOS REGISTROS NO SIGACRM PROTHEUS 12](https://tdn.totvs.com/display/PROT/CRM0020_REFAZER_PREVILEGIOS_REGISTROS_CRM)**

**[Como habilitar os privilégios no configurador](https://tdn.totvs.com/pages/viewpage.action?pageId=271180996)**
