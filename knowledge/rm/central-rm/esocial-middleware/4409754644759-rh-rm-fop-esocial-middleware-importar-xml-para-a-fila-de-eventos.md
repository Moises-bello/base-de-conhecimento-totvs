---
article_id: 4409754644759
category: eSocial - Middleware
content_hash: f0ff73622b7746f59d42f2f75b432f1c4257fa127a66439681f40222100eed22
fetched_at: '2026-06-28T22:47:05.581435+00:00'
product: rm
section_id: 1500000834541
source: central-rm
title: 'RH - RM - FOP - eSocial - Middleware: Importar XML para a fila de eventos'
type: support-article
updated_at: '2026-02-25T12:51:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409754644759-RH-RM-FOP-eSocial-Middleware-Importar-XML-para-a-fila-de-eventos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15356827745687) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Como importar XML para fila de eventos no Middleware?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir da 12.1.31  
  
**Solução**  
Para a importação de XMLs para a fila de eventos quando a coligada estiver com o Middleware ativado, siga os passos abaixo:

- **Liberação de permissão no módulo**

1. Acesse o menu **Serviços Globais | Segurança | Perfis**;  
2. Selecione o sistema **Folha de pagamento** e edite o perfil desejado;  
3. Clique em **Acesso a Menus** e permita o acesso **[09.05.14] Importar XML**;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410080794391)

- **Importar XML**

1. No TOTVS Folha de Pagamento, acesse o menu **eSocial | Outros Processos | Importar XML**;

![](https://tdn.totvs.com/download/attachments/574384400/image2020-12-1_11-29-53.png?version=1&modificationDate=1606836922727&api=v2)

2. Selecione a pasta onde estão os eventos que deseja realizar a importação. O processo é dividido em **duas pastas diferentes**, sendo uma para os eventos que foram enviados ao RET (S-2200, S-2300, S-1200, etc) e outra para os respectivos retornos (S-5001, S-5011, etc). Avance e execute o processo. Para arquivos exportados do ambiente do Governo selecione a opção **Arquivos eSocial** ***Download**.*

![etttaaaaa.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/6141802324503)

3. Evento ficará disponível para visualização na fila de eventos correspondente.

![](https://tdn.totvs.com/download/attachments/574384400/image2020-12-2_13-17-39.png?version=1&modificationDate=1606929459907&api=v2)

**Importante**  
Este processo deverá ser utilizado exclusivamente para carregamento de registros do legado para a fila de eventos em casos de migração de software de terceiros;

Para a importação dos eventos referentes ao funcionário (S-2200, S-2300, S-1200, etc) é necessário que já possua seu cadastro no sistema, e caso seja um evento periódico é necessário que possua o período de apuração criado.

Os eventos importados devem estar em formato XML. Serão considerados somente os eventos **periódicos**, **não-periódicos** **(exceto os eventos de SMT)** e **totalizadores**.

Os eventos do portal do governo, deverão ser exportados através da solicitação de *download* [(CLIQUE AQUI)](https://www.gov.br/esocial/pt-br/noticias/esocial-download-para-facilitar-a-vida-do-empregador).   
Na opção de importação "**Arquivos eSocial Download**" serão importados somente os XMLs retornados com as verbas enviadas e o recibo, **não é feita a importação dos XMLs totalizadores**.

Para **Clientes** ***Cloud*** é necessário que o usuário abra um *ticket*, inserindo os arquivos XML's, para que a Equipe *Cloud* salve os arquivos no servidor e retorne com o direcionamento da pasta em que os arquivos foram salvos.

**Saiba mais**  
Para mais informações, acesse:  
     - [Importar XML Fila de Eventos eSocial](https://tdn.totvs.com/display/public/LRM/Importar+XML+Fila+de+Eventos+eSocial)  
     - [Migração Software Terceiros para RM Middleware](https://tdn.totvs.com/pages/viewpage.action?pageId=552096198)
