---
content_hash: 5096ea0bc46c70d09fb3863ff62a0306196e3374209a19ca162076bbcc67c0c7
fetched_at: '2026-06-29T00:11:44.745926+00:00'
page_id: '815576346'
product: rm
source: tdn-rm
title: Pré-requisitos técnicos - Páginas PO-UI
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=815576346
version: 12
---

Importante

Essa documentação se aplica **somente** as páginas em PO-UI da linha RM, e é **essencial** para o correto funcionamento dos módulos.

Conteúdo totalmente técnico, direcione para o time de TI da empresa.

Configuracoes

## **CONFIGURAÇÃO PARA ACESSO ÀS API's**

As evoluções da Linha RM, utilizam a integração da MDI atual com telas em HTML, tudo isso de forma transparente ao usuário.

Para utilizar esse novo recurso, é necessária a realização de algumas configurações que irão habilitar o uso das APIs que fazem a execução das ações e processos da nova interface.

**Configurando as portas API**

O aplicativo RM.Host é responsável por hospedar e expor os serviços de APIs. 

Como visto na documentação sobre a [configuração da porta webApi](https://tdn.totvs.com/display/LRM/Configurando+HttpPort+e+ApiPort)., nos arquivos **RM.Host.exe.config** e **RM.Host.Service.exe.config** devem ser adicionadas as TAGS relacionadas a porta 8051.

A tag **ApiPort** configurada nesta etapa será utilizada para acessar as APIs que fazem parte das rotinas das páginas.

Importante

A execução do **Host** precisa ser como **administrador:**

* Caso o **Host** seja iniciado como **aplicativo** (RM.Host.exe), certifique-se que ao executá-lo, tenha selecionado a opção "**Executar como Administrador**".
* Caso o **Host** tenha sido instalado como **serviço**, o usuário do sistema operacional vinculado ao serviço deve ser um administrador.
Validação de acesso as APIs

Para validar se as configurações de portas das APIs foram realizadas corretamente, acesse o browser e digite a URL  http://{IP ou domínio}:{porta}/api/swagger/.

Exemplo: <http://10.173.17.242:8051/api/swagger>

**Importante** na validação usar o IP, nome da máquina ou domínio.

Verifique se a página abaixo foi carregada

  

**Conectando com o banco de dados**

Para que a API saiba em qual banco de dados conectar quando for acionada pelo Módulo, deve-se configurar os arquivos do Host.

Como visto na documentação sobre a ., nos arquivos **RM.Host.exe.config** e **RM.Host.Service.exe.config** devem ser adicionadas a TAG **DefaultDB.**

Validação de acesso ao banco de dados através da API

Para validar se a configuração da comunicação com o banco de dados das APIs foi realizada corretamente, acesse a API via browser.

Exemplo: <http://10.173.17.242:8051/api/financial/v1/paymenttypes/1>

Neste exemplo estamos buscando do cadastro de Meios de Pagamento todos os que são pertencentes à coligada 1, ao acessar será solicitado um usuário do sistema que tenha acesso a este cadastro dentro do sistema.

Você deverá ter um resultado semelhante a este, onde lista os registros do cadastro de meios de pagamento da coligada 1.
