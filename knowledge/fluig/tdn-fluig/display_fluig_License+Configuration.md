---
content_hash: 84db138ed23abb2a8423b3ab7c4e66c4711649c685286c555c13c1527c67c7c5
fetched_at: '2026-06-28T21:35:27.919995+00:00'
page_id: '6066535'
product: fluig
source: tdn-fluig
title: License Configuration
type: documentation
url: https://tdn.totvs.com/display/fluig/License+Configuration
version: 9
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**. 

Na aba License Configuration devem ser configuradas informações do licenciamento do produto, da empresa e dos usuários que utilizam o Fluig ESB.

As informações estão agrupadas em dois grupos: Contact Information e License Category.

### Contact Information

Permite configurar os usuários do Fluig ESB, conforme os campos abaixo.

| Campo | Descrição |
| --- | --- |
| Company Name | Razão social da empresa usuária do sistema. |
| Federal ID | Número do CNPJ da empresa. |
| Name | Nome do responsável pelo Fluig ESB. |
| E-mail | E-mail do contato. |
| Phone | Número do telefone do contato. |

### License Category

O grupo de licença permite configurar o licenciamento do produto. Existem três categorias de licença: **Hard Lock**, **Start Key** e **Emergency Key**.

A licença definitiva é a de categoria **Hard Lock**. Ao selecionar essa opção é necessário informar os dados de conexão do Servidor de Licenças TOTVS - LS, conforme campos abaixo.

| Campo | Descrição |
| --- | --- |
| Hostname | Nome ou endereço IP do servidor onde está carregado o servidor de licenças TOTVS (LS) com o dispositivo Hard Lock conectado. |
| LS Port | Porta utilizada no servidor informado acima para carregar o serviço de licença TOTVS (LS). |
| Client Port | Porta da máquina onde está instalado o Fluig ESB que será utilizada para conectar-se com a o serviço de licenças TOTVS (LS). |
| Test Conection | Esse botão tem a finalidade de testar a conexão entre a máquina onde está instalado o Fluig ESB com o servidor de licenças TOTVS (LS). |

A categoria **Start Key** se encontra impressa na nota fiscal de aquisição do produto e tem duração de 20 dias.

A categoria **Emergencial Key** é utilizada caso por algum motivo as categorias de licenças descritas acima não estarem disponíveis para configuração. Nesses casos é possível informar uma licença dessa categoria que possui validade de 48 horas.

Os campos disponibilizados para essas categorias são discriminados abaixo.

| Campo | Descrição |
| --- | --- |
| Key | Chave de licença **Start Key** ou **Emergencial Key**. |
| Test Validation | Esse botão tem a finalidade de testar se a chave informada é válida e ainda exibir o número de dias de expiração da licença. |
