---
content_hash: f49db6580899a8d4476c52eb0229f5e1ac9dec0939b26f1cc22b70a5623d7eab
fetched_at: '2026-06-28T21:35:18.247583+00:00'
page_id: '152802533'
product: fluig
source: tdn-fluig
title: Atualização 1.3.6
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=152802533
version: 45
---

Confira abaixo as novidades na atualização 1.3.6 do Fluig:

# ECM

************Cópia controlada com mais compatibilidade************

A habilidade de cópia controlada foi aprimorada, agora são aceitas diferentes extensões de arquivo (.doc, .docx, .xls, .xlsx), aumentando a compatibilidade e facilitando sua utilização.

**Novas propriedades em documentos**

Agora é possível saber quem foram os aprovadores de um documento por meio das propriedades de cópia controlada "Fluig.LevelX.ApproverY" (onde X e Y variam de 1 a 5) que possuem os nomes dos aprovadores separados por nível de aprovação.

Também foi criada a propriedade "Fluig.User.Project", que informa o projeto configurado para o usuário.

# BPM

************Versionamento de formulários mais dinâmico************

Agora é possível escolher se as alterações feitas em formulários e eventos devem manter a versão existente do formulário ou criar uma nova versão.

************Gestor de processo com mecanismo customizado************

Agora a opção "Minhas tarefas sob gerência" – da central de tarefas – somente é apresentada para o gestor do processo. Ao definir um mecanismo de atribuição customizado, é necessário informar a matrícula do usuário que pode visualizar a tarefa.

************Atualização de processos e mensagem otimizadas************

Foi otimizada a atualização da montagem de processos de *workflow* para versões mais novas, evitando inconsistências de conversão e criação, e reformulada a mensagem que é apresentada ao usuário, tornando-a mais clara.

************Descrição de componentes mais clara************

Foram aprimoradas as descrições dos componentes – principalmente nos mecanismos de anotação e condicionais – no Fluig Studio, tornando a apresentação mais detalhada e limpa visualmente.

************Imagem do processo com mais qualidade************

Foi aprimorada a geração da imagem do processo que é apresentada nas solicitações para garantir uma representação fiel dos artefatos que foram modelados.

************Exportação de processo com componente Link otimizada************

A geração e edição de processos *workflow* no Fluig Studio e na Web foram aprimoradas para permitir a inclusão de nomes para os *links* entre as atividades. Agora também é possível exportar os nomes/descrições para a WEB, edita-los e importa-los novamente para o Fluig Studio.

***************Download* de anexos em processos mais abrangente**************

A partir de agora, usuários sem o perfil de administrador também podem realizar *download* e impressão de anexos de processos *workflow*.

**Novo método no *webservice* de sinal**

Foi criado o método “*fireSignal*” no *webservice* para envio de sinal de processos *workflow*.

Nota

Informações adicionais podem ser obtidas em [Utilização de *Webservices*](http://tdn.totvs.com/x/ZyxbB).

**Envio de sinais em processos *workflow* mais eficiente**

Foi aperfeiçoado o envio de sinais em processos *workflow*, agora o sistema envia sinal depois de atividades automáticas.

# Social

************Apresentação de comunidades mais completa************

Na tela onde são apresentadas todas as comunidades, ao posicionar o mouse sobre uma comunidade agora é exibido o nome completo dela, facilitando sua identificação.

************Aviso sobre a remoção de artigos************

Agora, quando um artigo é excluído e um usuário tenta acessá-lo por meio da publicação existente na *timeline*, o Fluig informa que ele foi removido.

************Novos compartilhamentos em comunidades ocultas************

A partir de agora é possível compartilhar publicações e documentos de uma comunidade pública em uma comunidade oculta, bem como compartilhar em uma comunidade oculta documentos que pertencem a ela.

# Arquitetura

************Mais segurança na configuração Web Service************

Os serviços SOAP que fazem uso de permissionamento foram otimizados para oferecer mais segurança e garantir a integridade das informações.

# WCM

***************************Logout* do Fluig personalizável**************************

A partir de agora é possível customizar a URL de *logout* a ser utilizada pelo *Identity*. Foi adicionado o parâmetro “java:global/totvs/idp/logoutURL” no arquivo “standalone.xml”, que indicará para onde será feita a requisição de *logout* pelo *Identity* quando a opção "Encerrar sessão do Fluig Identity ao efetuar *logoff*" estiver marcada.

E quando o Fluig *Identity* está sendo utilizado, ao efetuar *logout*, o Fluig emite uma mensagem informando que outras sessões podem ser encerradas.

# Plataforma

************Página de ajuda mais completa e de fácil acesso************

Agora o Fluig conta com a página de ajuda mais completa e com a navegação facilitada, o que auxilia o usuário na realização de seu trabalho diário.
