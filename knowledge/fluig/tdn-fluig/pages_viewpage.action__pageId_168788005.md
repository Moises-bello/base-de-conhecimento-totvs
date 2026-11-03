---
content_hash: cf793a2b78a62631430785edc967dd2ea349fcc0eb67ffca28fcbb6c1ca08e31
fetched_at: '2026-06-28T21:35:18.597749+00:00'
page_id: '168788005'
product: fluig
source: tdn-fluig
title: Atualização 1.3.9
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=168788005
version: 31
---

Confira abaixo as novidades na atualização 1.3.9 do Fluig:

# BPM

**Eventos “*onNotify”* em notificações de atraso**

Agora o evento *workflow* "*onNotify*" também será executado quando as notificações são provenientes de uma tarefa atrasada. Nele é possível acessar a hAPI para ter acesso a dados da solicitação atrasada.

Nota

Mais informações sobre o "*onNotify*" podem ser obtidas em [Customização de Eventos](http://tdn.totvs.com/x/EIl8B) e [Customização de *Workflow*](http://tdn.totvs.com/x/widbB).

**Complemente sua lista de tarefas**

Você sabia? Mesmo que já tenha iniciado a solicitação de Lista de Tarefas, novas tarefas podem ser criadas conforme demanda mesmo com tarefas ainda pendentes.

Nota

Mais informações podem ser obtidas em [Gestão de Lista de Tarefas](http://tdn.totvs.com/x/3CeDC).

**Mais integridade na exportação e importação de processos modelados**

Crie diagramas ricos: com diferentes atividades, *swinlanes*, atividades em *pool*, anotações e muito mais! Posteriormente exporte e importe nos servidores e Studios desejados com confiança que tudo será apresentado.

**Consulta de solicitações mais enxuta**

Agora quando a consulta de solicitações gerar um número menor de registros é apresentada uma mensagem ao usuário questionando se ele deseja prosseguir. Quando utilizada a consulta em tela, apenas os primeiros 2000 registros são apresentados. Para a consulta completa utilize a opção de exportação.

**Datas independente da configuração do servidor**

Agora é possível utilizar *datasets* contendo filtros de data quando o idioma definido no sistema operacional do servidor é o inglês.

Importante!

Salienta-se que o padrão para utilizar datas em filtros, independentemente do idioma definido no sistema operacional, é "**dd/mm/yyyy**".

**Procure palavras em *datasets* com flexibilide**

Agora é possível criar *constraints* que fazem consultas utilizando o formato “LIKE” do SQL. Com isso é possível buscar por parte da palavra dentro de *dataset*.

Nota

Mais informações do novo atributo de c*onstraint* - **setLikeSearch** - podem ser obtidas na sessão "Acessando um *Dataset*" em [Customização de *Datasets*](http://tdn.totvs.com/pages/viewpage.action?pageId=73083770).

**Novas ações disponíveis para formulários em processos**

Agora é possível imprimir o formulário de uma solicitação acionando o botão “Imprimir em modo de visualização”, que permite visualizar o formulário e seus componentes durante a edição. Posteriormente, é possível retornar à edição acionando o botão "Voltar ao modo de edição", que possibilita continuar efetuando alterações no formulário.

# Fluig Studio

**Pesquisa de pastas mais específica na exportação de formulários**

Na exportação de formulário, pesquise a Pasta Destino, informando no campo de filtro o valor desejado. A busca trará resultados mais precisos considerando os caracteres inseridos.

# Correções

Nessa sessão listamos alguns *bugs* que matamos nessa atualização que garantem que tudo corra bem na sua plataforma.

* Recuperação das informações usando uma *constraint* com o campo "metadata#active" em ambientes com SQL Server;
* Botões de ação na tela de seleção de usuários para tarefas em *pool* que aceitavam mais de um clique na efetivação;
* Nos serviços SOAP do Fluig  em chamadas consecutivas, utilizando o ESB por exemplo;
* Liberação de versão de processos onde existe um fluxo de entrada na atividade inicial;
* Edição de formulários em processos Fluig agora sempre considera o último ID como base para criar o próximo registro;
* Atividades paralelas quando consultadas são destacadas em amarelo na visualização do processo;
* Criação do processo "Listar Tarefas" gerado automaticamente durante a conversão de processos;
* Sinais de envio e recebimento em processos antes e depois de atividades automáticas;
* Formulários com Pai x Filho para permitir que eles sejam manipulados em atualizações mais antigas do Fluig da mesma forma como são manipulados nas atualizações mais atuais;
* Retorno de varáveis no *zoom* quando essa possui um "." no nome;
* *E-mail* de notificação para o usuário que recebe tarefas de subprocessos AdHoc;
* Exportação de processos com atividades específicas do BPMN 2.0 (Envio, Negócio, Serviços, Manual, *Script* e Usuário) e visualização dos diagramas na Web;
* Filtro avançado que permite buscar publicações pelo seu autor, por comentários, pela descrição, dentre outros;

* *Template* de *e-mail* de compartilhamento com usuários.

  Atenção!

  Se você fez customizações neste *template* (TPLSHAREUSER), o *backup* da customização com a correção estará disponível em **<diretório padrão>/templates/tplmail\_backup/TPLSHAREUSER**.
