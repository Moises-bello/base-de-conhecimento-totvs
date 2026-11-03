---
article_id: 360029308291
category: Configurador
content_hash: 3b77249e8bac4e7077b1e6ba8774ada118cfa3d505d58cf3d50c4031c1545434
fetched_at: '2026-06-28T22:42:19.078964+00:00'
product: protheus
section_id: 360000076767
source: central-protheus
title: Framework - Linha Protheus  - Otimização de ambiente - Economia de Recursos
type: support-article
updated_at: '2024-05-08T11:53:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029308291-Framework-Linha-Protheus-Otimiza%C3%A7%C3%A3o-de-ambiente-Economia-de-Recursos
---

**Dúvida**  
Existe alguma maneira de configurar o ambiente de forma otimizada para economizar recursos?  
  
**Ambiente**  
Protheus - Configurador - Todas as versões  
  
**Solução**  
Sim. Para adequar o Microsiga Protheus às diversas realidades de uso, principalmente para os casos em que o acesso ao Sistema se dá remotamente ou para clientes que não dispõem de muitos recursos em suas estações de trabalhado, o Sistema oferece a funcionalidade de Economia de Recursos, que possibilita restringir o acesso dos usuários ou o acesso a recursos específicos do sistema.  
  
A otimização dos recursos deve ser avaliada de acordo com a necessidade de acesso ao Sistema ou de disponibilidade de equipamentos, identificada pelo administrador do ambiente.  
  
Estão disponíveis a restrição dos recursos de interface, tais como:  
  
- Menu Funcional  
- Painel Online  
- Browser de Internet  
- Detalhes do Browse  
- Painel Transparente  
  
**Procedimentos de Configuração**Para configuração deste recurso utilize uma das opções a seguir:  
  
**Configuração do sistema pelo arquivo AppServer.ini**  
No arquivo de configuração do Appserver, adicione na seção do ambiente desejado a chave ECONOMYRES, cujo valor pode ser:  
  
01 – para Menu Funcional;  
02 – para Painel Online;  
03 – para Browse de Internet no menu inicial;  
04 – para Detalhes apresentados nas telas de Browse;  
05 - para exibição de Paineis Transparentes em interfaces de destaque.  
  
Exemplo  
[ENVIRONMENT]  
...  
ECONOMYRES=01;02;04;  
  
**Configuração através da opção de Política de Segurança**  
- Acesse Configurador > Usuário > Senhas > Política  
- Clique na aba Outros  
- Em Recursos do Sistema, desmarque as caixinhas das opções que quer desabilitar para o sistema  
  
**Configuração através da opção Usuários**  
- Acesse Configurador > Usuário > Senhas > Usuário  
- Selecione o usuário desejado e clique em Alterar  
- Clique na aba Parametrização  
- Em Recursos do Sistema, desmarque as caixinhas das opções que quer desabilitar para o usuário  
  
**Configuração através da opção Grupo de Usuários**  
- Acesse Configurador > Usuário > Senhas > Grupos  
- Selecione o grupo desejado e clique em Alterar  
- Clique na aba Parametrização  
- Em Recursos do Sistema, desmarque as caixinhas das opções que quer desabilitar para o grupo
