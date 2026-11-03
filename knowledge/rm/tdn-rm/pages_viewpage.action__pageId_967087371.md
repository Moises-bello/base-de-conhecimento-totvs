---
content_hash: 177bd3b34cb6f8fea84a42cfc9d4a9dd63d9a62509b789e4fa2cb8aec1c6ad95
fetched_at: '2026-06-29T00:12:14.193953+00:00'
page_id: '967087371'
product: rm
source: tdn-rm
title: 01. Contratos 2.0 | Pré-requisitos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=967087371
version: 27
---

Permisão de Acesso

As permissão de acesso as novas telas estão disponibilizadas junto à arvore de permissões do menu de contratos.

Mantemos todas as permissões para a visualização, inclusão, alteração e exclusão, além de todos os processos.

**Sistema**: Gestão de Estoque, Compras e Faturamento | Contratos | Gestão de Contratos

trueAPIAPIAPIConfigurando as portas da API

**Configurando as portas da API**

O aplicativo RM.Host é responsável por hospedar e expor os serviços de APIs.

Veja mais sobre a [configuração da porta webApi](https://tdn.totvs.com/display/LRM/Configurando+HttpPort+e+ApiPort).

A tag **ApiPort** configurada nesta etapa será utilizada durante a instalação das telas em Smart UI.

Importante

A execução do **Host** precisa ser como **administrador:**

* Caso o **Host** seja iniciado como **aplicativo** (RM.Host.exe), certifique-se que ao executá-lo, tenha selecionado a opção "**Executar como Administrador**".
* Caso o **Host** tenha sido instalado como **serviço**, o usuário vinculado ao serviço deve ser um administrador do sistema.
Validação de acesso as APIs

Para validar se as configurações de portas das APIs foram realizadas corretamente, acesse o browser e digite a URL  http://{IP ou domínio}:{porta}/api/swagger/.

Exemplo: <http://10.173.17.242:8051/api/swagger>

**Importante** na validação usar o IP, nome da máquina ou domínio.

Verifique se a página abaixo foi carregada

Conectando com o banco de dados

**Conectando com o banco de dados**

Para que a API saiba em qual banco de dados conectar quando for acionada pela tela, devemos configurar a tag DefaulDB.

Veja mais em .

Validação de acesso ao banco de dados através da API

Para validar se a configuração da comunicação com o banco de dados das APIs foi realizada corretamente, acesse a API via browser.

Exemplo: <http://10.173.17.242:8051/api/est/v1/Unitofmeasures>

Neste exemplo estamos usando o cadastro de Unidade de Medidas, ao acessar será solicitado um usuário do sistema que tenha acesso a este cadastro dentro do sistema.

Você deverá ter um resultado semelhante a este, onde lista os registros do cadastro de unidade de medida.

div.theme-default .ia-splitter #main {
margin-left: 0px;
}
.ia-fixed-sidebar, .ia-splitter-left {
display: none;
}
#main {
padding-left: 10px;
padding-right: 10px;
overflow-x: hidden;
}
.aui-header-primary .aui-nav, .aui-page-panel {
margin-left: 0px !important;
}
.aui-header-primary .aui-nav {
margin-left: 0px !important;
}
]]>
