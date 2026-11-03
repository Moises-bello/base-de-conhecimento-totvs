---
article_id: 8987009440407
category: Materiais - Compras (SIGACOM)
content_hash: cc1ec9047d735bacc08176497d033c6c521db7484b5a8fb6f0ad4313115d0fa6
fetched_at: '2026-06-28T22:41:14.533538+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como configurar Painel
  Gestão
type: support-article
updated_at: '2022-11-09T11:27:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8987009440407-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-configurar-Painel-Gest%C3%A3o
---

**Dúvida**Como configurar a exibição do painel de informações, chamados Painel de Gestão, nos módulos do Protheus

Saiba como configurar o Painel de Gestão acessando nossa pagina no YouTube:

Configuração: [How To | MP-SIGACOM Painel Gestão - YouTube](https://www.youtube.com/watch?v=rDEai5myC1o)  
  
**Ambiente**Protheus – Compras – A partir da versão 11.80  
  
**Solução**

O Painel de Gestão Online é um recurso que exibe alguns indicadores do módulo na tela principal do mesmo ao acessar o Smartclient. Para que esses indicadores sejam configurados, siga os passos abaixo:

- Abra o arquivo appserver.ini do Servidor de Aplicação do Protheus  
- Adicione as 2 linhas abaixo na seção do ambiente que vai utilizar o Painel Gestão:  
PANELSERVER= ip do servidor  
PANELPORT=porta TCP desse servidor

Exemplo:

(Esta configuração deve ser feita no Appserver que os usuários acessam. A "PANELPORT" indicada deve ser a porta [TCP] de um outro Appserver que vai iniciar apenas para processar o Painel de Gestão)

`[Environment]  
SourcePath=C:\TOTVS 12\Microsiga\protheus\apo\  
RootPath=C:\TOTVS 12\Microsiga\protheus_data  
...  
PANELSERVER=localhost  
PANELPORT=1299PANELPORT=1299`

Após configurar o arquivo appserver.ini, siga os passos abaixo:

- Acesse Configurador > Usuário > Senhas > Política  
- Entre na aba Outros / Painel On-Line  
- Marque do lado esquerdo da tela os módulos que deseja utilizar os respectivos indicadores  
- Clique no Módulo do lado esquerdo, e então do lado direito da tela serão exibidos os Painéis disponíveis para este módulo. Marque os que deseja utilizar.

- Clique em Confirmar

![](https://tdn.totvs.com/download/attachments/271183670/PO_01.png?version=1&modificationDate=1485459912000&api=v2)  
  
- Acesse Usuário > Senhas >Grupos  
- Clique no grupo Administradores e clique em Alterar  
- Na aba Grupo, clique na aba Painel OnLine  
- Habilite os painéis previamente selecionados na rotina Política  
- Clique em Confirmar

![](https://tdn.totvs.com/download/attachments/271183670/PO_02.png?version=1&modificationDate=1485459912000&api=v2)  
  
- Acesse Usuário > Senhas > Usuários  
- Clique sobre o usuário que irá utilizar o Painel OnLine, e clique em Alterar  
- Clique na aba Parametrização / Painel OnLine  
- Selecione, dos painéis disponíveis, quais esse usuário terá acesso, e clique em Confirmar

![](https://tdn.totvs.com/download/attachments/271183670/PO_03.png?version=1&modificationDate=1485459912000&api=v2)  
  
- Após essa configuração, o Painel Online estará pronto para uso. Segue abaixo imagem de exemplo de um Painel Online no módulo:

![](https://tdn.totvs.com/download/attachments/271183670/PO_06.png?version=1&modificationDate=1485459912000&api=v2)  
  
Obs.:

- O Painel Online só aparece na tela inicial do módulo se o acesso for feito via SIGAMDI

![](https://tdn.totvs.com/download/attachments/271183670/PO_05.png?version=1&modificationDate=1485459912000&api=v2)

 

- O usuário que for utilizar o Painel Online precisa ter mais de um acesso simultâneo configurado no seu cadastro

![](https://tdn.totvs.com/download/attachments/271183670/PO_04.png?version=1&modificationDate=1485459912000&api=v2)

***Saiba Mais :***

[FAQ's de Compras - Linha Microsiga Protheus](https://tdn.totvs.com/display/public/PROT/FAQ%27s+de+Compras)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
