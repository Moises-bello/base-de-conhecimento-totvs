---
article_id: 25128258571287
category: Materiais - Compras (SIGACOM)
content_hash: 8703e6010cfc45e6b1a0cceea707fdb24960ae53f7eb474d726acfc3b5691470
fetched_at: '2026-06-28T22:41:07.282958+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Como configurar o
  WorkFlow através do Wizard no Novo Fluxo de Compras - NFC (PGCA010)?
type: support-article
updated_at: '2026-03-02T13:42:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25128258571287-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Como-configurar-o-WorkFlow-atrav%C3%A9s-do-Wizard-no-Novo-Fluxo-de-Compras-NFC-PGCA010
---

**Dúvida**  
Como configurar o WorkFlow através do Wizard no Novo Fluxo de Compras - NFC (PGCA010)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras/GCT - Protheus Release 12.1.2210.  
  
**Solução**

Para iniciar o processo de configuração de Workflow via NFC, o usuário logado deve ser do tipo administrador no Protheus. Para configuração, siga as etapas abaixo:

1. Acesse a rotina do Novo Fluxo de Compras com usuário administrador;
2. Clique no botão de perfil (ícone a direita, na parte superior da tela), para exibir os submenus existentes. Clique no menu com o nome Configuração Workflow

![toolbar.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25128395144983)

Siga as etapas do wizard, informando os dados solicitados:

No primeiro passo do configurador - o sistema irá explicar para que serve o Wizard de WorkFlow e seus objetivos, para que o usuário possa compreender seu funcionamento.

![image-2024-4-12_19-30-28.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25128425106327)  
  
Na segunda etapa do wizard - Parâmetros e arquivos - informe no campo Diretório de trabalho do Workflow o local (pasta) onde os arquivos físicos do wizard serão gravados no servidor. Por exemplo, se os arquivos serão gravados na estrutura Protheus\_Data\workflow, informe \workflow no campo.  
  
![passo 2.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/25128425112343)  
  
Na terceira etapa - Dados do servidor - informe o Endereço (IP) público do servidor de workflow, é obrigatório inserir http:// antes de informar o IP; informe a Porta do Servidor de workflow; informe o Nome do Ambiente onde o workflow é executado e no campo Nome/IP e porta do servidor, o sistema monta automaticamente a sugestão, com o endereço ip, porta e nome do ambiente.  
  
**Observação:**Caso o seu ambiente esteja hospedado no CLOUD da TOTVS é necessário que realize a criação de um ticket para que seja disponibilizado um endereço e porta para utilização no Workflow. 

![passo 3.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/25128823635607)  
  
Na quarta etapa - Porta Multiprotocolo, o sistema avisará se existe a chave[MULTIPROTOCOL] no ambiente e se está ativa.

Clique no botão **Próxima Etapa**, para avançar no wizard.

![image-2024-4-12_19-49-39.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25128823638679)  
  
Na quinta etapa - Parâmetros de e-mail dos compradores, informe os dados solicitados na tela, como endereço e porta do servidor SMTP e POP3/MAP, para que quando o parâmetro MV\_PGCWF estiver ativo, os usuários não necessitem e informar estes campos no wizard de configuração de e-mail.

**Observação:** O preenchimento desse campo varia de acordo com o serviço de email que esteja utilizando, verifique com a sua equipe interna de infraestrutura quais são as informações que devem ser inserida para prosseguir com a configuração do Novo Fluxo de Compras.  
  
Clique no botão **Próxima Etapa**, para avançar no wizard.  
  
![passo 5 (1).gif](https://centraldeatendimento.totvs.com/hc/article_attachments/25128823640343)  
  
Na sexta etapa - Finalização, o sistema alerta que ao avançar, os dados serão gravados na base e o sistema irá montar o modelo de appserver.ini, além de apresentar uma notificação de sucesso.  
  
Após o sistema gerar o modelo de configuração, insira essas informações em seu appserver.ini, caso exista alguma TAG redundante a mesma pode ser retirada do modelo de configuração. Caso o seu ambiente esteja hospedado no CLOUD da TOTVS é necessário realizar a criação de um ticket para que o processo de configuração seja finalizado.

![passo 6.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/25128834208407)

**Observação:**Caso o seu ambiente esteja hospedado no CLOUD da TOTVS é necessário realizar a criação de um ticket para que incluída as informações do exemplo gerado no seu appserver.ini.

Sem essas configurações informadas no appserver o NFC não funciona corretamente.

**Saiba Mais:**

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
