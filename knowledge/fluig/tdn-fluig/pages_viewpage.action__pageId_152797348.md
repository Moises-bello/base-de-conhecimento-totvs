---
content_hash: 265ad5f71efec042e1e222a514bb27d9d4f893e7556ab33e4204c7688753dbfb
fetched_at: '2026-06-28T21:35:18.151556+00:00'
page_id: '152797348'
product: fluig
source: tdn-fluig
title: Atualização 1.3.5
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=152797348
version: 49
---

Confira abaixo as novidades na atualização 1.3.5 do Fluig:

# ECM

**********Visualização de registros de formulários aprimorada**********

Agora é possível visualizar os registros de formulário por meio de relatórios quando, na publicação do formulário, foi utilizada a opção de armazenamento “Em uma única tabela”.

# BPM

********Atribuição de campo de formulário aperfeiçoada********

Agora, mesmo quando o formulário não está no servidor, ou seja, quando é utilizada a configuração do diagrama como local, é possível definir atribuição por campo de formulário.

********Imagem do processo com mais qualidade********

Foi aprimorada a geração da imagem do processo que é apresentada nas solicitações para garantir uma representação fiel dos artefatos que foram modelados.

********Consulta de solicitações mais prática********

A partir de agora é possível visualizar todas as solicitações independentemente da quantidade existente, tornando a consulta mais prática e eficiente.

********Customizações mais abrangentes********

Nessa atualização é possível identificar, na implementação de eventos, se um formulário ou processo está sendo acessado por meio de um aplicativo *mobile*, possibilitando customizações específicas para estes casos. O parâmetro utilizado para esse fim é o *"WKMobile"* e o método é o *"getMobile*".

Nota

Informações adicionais podem ser obtidas em [Customização de Formulários](http://tdn.totvs.com/x/U4l8B) e [Customização de Workflow](http://tdn.totvs.com/x/widbB).

********Comunicação com o usuário mais clara********

Ao excluir uma pasta que contenha formulários associados a processos, o Fluig apresenta uma mensagem explicando o motivo e informando qual formulário está impedindo a exclusão da pasta.

**********Mais rastreabilidade em tarefas de sub processos**********

Agora, o Fluig registra no histórico quando uma solicitação iniciada ou cancelada é referente a um sub processo de uma solicitação do processo pai, permitindo a rastreabilidade da tarefa pelo usuário que a recebe.

# Social

**********Histórico de interações em artigos**********

A partir dessa atualização, na galeria de artigos de uma comunidade é possível visualizar os apoios e os comentários do artigo independentemente de sua versão, permitindo que seja mantido um histórico de interações dos usuários no artigo.

********Publicação e visualização de artigos aperfeiçoadas********

Foi otimizada a publicação de artigos em comunidades, garantindo que eles estejam acessíveis e sejam visualizados a qualquer momento.

*********Links* mais específicos em publicações e comentários********

Agora, o Fluig aceita URLs que contenham referência a uma âncora da página em questão, gerando o *link* e direcionando para o conteúdo marcado com a âncora.

********Criação de formulários mais segura********

Criar formulários, tanto em processos quanto em comunidades, está mais seguro. Agora o Fluig informa quando um caracter não pode ser utilizado no título do formulário, garantindo assim a integridade das informações.

 

********Timeline com experiência de uso aperfeiçoada********

Agora a timeline do Fluig apresenta os conteúdos com mais rapidez, proporcionando ao usuário uma nova experiência de uso, com agilidade e eficiência.

************Novidade na criação de artigos************

Agora, ao publicar um artigo pertencente a um assunto que não está parametrizado como obrigatório, é possível definir se será ou não emitida notificação para os usuários que o tem como assunto de interesse, por meio do campo *“Notificar?”*, disponível na criação de artigos.

# Arquitetura

********Monitor de serviços do Fluig mais dinâmico********

A partir dessa atualização, é possível alterar a porta de acesso padrão utilizada pelo monitor de usuários conectados no Fluig - parâmetro ***jmxPort=<parâmetro>*** -, permitindo assim, que o monitor seja utilizado em ambientes compartilhados.

Nota

Mais informações podem ser obtidas em [Monitor de Serviços Fluig](http://tdn.totvs.com/x/QCCDC).

**********Configurações mais automatizadas**********

Agora, se a aplicação possuir permissão de alteração na base, ela efetua automaticamente a configuração do nível de isolamento transacional do SQL Server necessário para o Fluig.

Nota

Informações adicionais podem ser obtidas em [Configuração do banco de dados SQL Server](http://tdn.totvs.com/x/NRhbB).

# Fluig Studio

********Formulários em HTML mais dinâmicos********

Agora, ao criar um formulário em HTML, é possível definir um código de campo e um nome com até 70 caracteres, tornando-os mais específicos e de acordo com sua necessidade e preferências.

# Plataforma

********Documentação sobre *datasets* mais completa********

Foi atualizada e complementada a documentação para implementação de *datasets*, no tópico Construindo *Datasets* Customizados, que visa facilitar e orientar sua construção e utilização. Agora a documentação conta com mais exemplos.

Nota

A documentação atualizada está disponível em [Customização de *Datasets*](http://tdn.totvs.com/x/eitbB).
