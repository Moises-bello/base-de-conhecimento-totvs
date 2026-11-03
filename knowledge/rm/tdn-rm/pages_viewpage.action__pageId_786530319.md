---
content_hash: de468e731a746a99a38d50b945fbd4e7834a4f4651ffde726c34871acc6b7de8
fetched_at: '2026-06-29T00:11:38.913388+00:00'
page_id: '786530319'
product: rm
source: tdn-rm
title: Pré requisitos técnicos - Gerais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=786530319
version: 5
---

As evoluções da Linha RM utilizam a integração da MDI atual com APIs, tudo isso de forma transparente ao usuário.  
Para o **correto** funcionamento dos novos recursos, é **essencial** realizar as configurações a seguir.

Importante

Essa documentação possui conteúdo totalmente **técnico**, direcione para o time de **TI** da empresa.

ConfiguracoesAPIConfiguração API

O primeiro passo é habilitar o uso das API's no ambiente, que são responsáveis por executar as ações e processos nas novas interfaces.

**1. Configurando as portas API**

O aplicativo **RM.Host** é responsável por hospedar e expor os serviços de **APIs.**   
Para este passo precisamos focar na configuração da tag **ApiPort** que será responsável por definir a porta pela qual as API's serão acessadas.

Veja com detalhes como realizar a configuração em [configuração da porta webApi](https://tdn.totvs.com/display/LRM/Configurando+HttpPort+e+ApiPort).

Importante

A execução do **Host** precisa ser como **administrador:**

* Caso o **Host** seja iniciado como **aplicativo** (RM.Host.exe), certifique-se que ao executá-lo, tenha selecionado a opção "**Executar como Administrador**".
* Caso o **Host** tenha sido instalado como **serviço do windows**, o usuário vinculado ao serviço deve ser um **administrador** do sistema.

Depois de realizada a configuração acima, é possível validar.

Validação de acesso as APIs

Acesse o browser e digite a URL  http://{IP ou domínio}:{porta}/api/swagger/.  
Exemplo: <http://10.173.17.242:8051/api/swagger>

Importante

{IP ou domínio} - Na validação é **extremamente** importante usar o **IP**, **nome da máquina** ou **domínio**, principalmente em casos de ambiente 3 camadas ou smart client.

{porta} - A porta informada na URL é a mesma configurada na tag **ApiPort**

A configuração terá sido realizada com sucesso, caso uma página semelhante ao print abaixo seja apresentada.

  

**2. Conectando com o banco de dados**

O segundo passo é definir em qual banco de dados as **APIs** vão se conectar.  
Para este passo precisamos focar na configuração da tag **DefaulDB** que será responsável por o banco de dados onde que a API vai consultar e salvar dados.

Veja com detalhes como realizar a configuração em .

Depois de realizada a configuração acima, é possível validar.

Validação de acesso ao banco de dados através da API

Acesse o browser e digite a URL  http://{IP ou domínio}:{porta}/api/framework/v1/companies  
Exemplo: <http://192.168.0.87:8055/api/framework/v1/companies>

Importante

{IP ou domínio} - Na validação é **extremamente** importante usar o **IP**, **nome da máquina** ou **domínio**, principalmente em casos de ambiente 3 camadas ou smart client.

{porta} - A porta informada na URL é a mesma configurada na tag **ApiPort**

Neste exemplo estamos acessando o cadastro de coligadas, será solicitado um usuário (mesmo usado para acesso ao sistema) que tenha acesso a este cadastro.

A configuração terá sido realizada com sucesso, caso uma página semelhante ao print abaixo seja apresentada, com as informações das coligadas da base.
