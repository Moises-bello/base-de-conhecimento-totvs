---
content_hash: e30f8ac5ff39fccc7eddc177ceeff3c1af9f273f5d43be2dd4790b71dda0ff6c
fetched_at: '2026-06-28T21:35:27.426587+00:00'
page_id: '547233188'
product: fluig
source: tdn-fluig
title: Plataforma ❙ Recursos de permissão em APIs, datasets e webservices
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=547233188
version: 33
---

.\*ndice

# Falando de recursos de permissão em APIs, *datasets* e *webservices*...

---

Por meio das opções de permissão pode ser configurado o controle de acesso a todas as APIs públicas, *datasets* internos e todos os *webservices powered by* TOTVS Fluig. 

As permissões aplicadas são granulares: a segurança obedece à hierarquia, mas é possível conceder permissão individualmente nos métodos, ou seja, quem tem acesso a API completa, pode ter restrição a um determinado método.

Confira em  mais detalhes sobre as permissões apresentadas abaixo.

falsePermissõesBuscar recursoAplicar permissão

## Recursos para desenvolvedores

---

| Descrição | Tipo | Nome do recurso | Opções de permissão |
| --- | --- | --- | --- |
| API no modelo swagger | API | Consulte o nome da API e dos métodos individualmente em <https://api.fluig.com/>. | **Acessar**: Quando ativada, permite acessar o recurso. |
| APIs para gerenciamento de Papéis | API Pública | Papéis | **Todos**: Quando ativada, permite acessar todas as APIs – de criação, alteração e exclusão.  **Criar**: Quando ativada, permite acessar as APIs de criação.  **Alterar**: Quando ativada, permite acessar as APIs de alteração.  **Excluir**: Quando ativada, permite acessar as APIs de exclusão. |
| APIs para gerenciamento de Grupos | API Pública | Grupos | **Todos**: Quando ativada, permite acessar todas as APIs – de criação, alteração e exclusão.  **Criar**: Quando ativada, permite acessar as APIs de criação.  **Alterar**: Quando ativada, permite acessar as APIs de alteração.  **Excluir**: Quando ativada, permite acessar as APIs de exclusão. |
| API no modelo antigo | API | Consulte o nome da API e dos métodos individualmente em <https://api.fluig.com/old/>. | **Acessar**: Quando ativada, permite acessar o recurso. |
| *Webservice* | API | Consulte o nome do *webservice* e os métodos individualmente na documentação técnica de Utilização de *Webservices* | **Acessar**: Quando ativada, permite acessar o recurso. |
| *Dataset* | DATASET | Para consultar o nome do *dataset*, acesse o recurso de  do Painel de controle e filtre pelo tipo Interno.  **Atenção**: *Datasets* internos gerados pelo cliente (a partir de formulários) não possuem controle de permissões. | **Acessar**: Quando ativada, permite acessar o recurso. |

Aplicação da permissão

Caso não seja realizada nenhuma alteração nessas permissões, por padrão os recursos permanecem com acesso liberado. A partir do momento em que é configurado um grupo, papel ou usuário com a permissão, somente quem teve a permissão liberada passa a ter acesso ao recurso. Com exceção dos usuários com perfil administrador, que sempre terão acesso aos recursos.

## Exemplo de permissão granular

---

É possível configurar a permissão ao recurso principal ou a cada método do recurso. Sendo que a permissão mais granular é a que prevalece.

Por exemplo: Configuro permissão para o grupo "AB" ao *webservice* *ECMDashBoardService* e permissão aos grupos "CD" e "EF" no método *ECMDashBoardService/findMyRequests.* Os usuários do grupo "AB" terão acesso a todos os métodos do *webservice* *ECMDashBoardService*, com exceção do método *findMyRequests*, que somente os usuários dos grupos "CD" e "EF" terão acesso.

Ao acessar uma API ou *webservice* que o usuário não tem permissão, será retornado erro de permissão.

falsesample1Acesso sem permissãooculto

Traduções:

$("b:contains('oculto')").parent().parent().hide();
]]>Fique atento!

Esta documentação é válida a partir da atualização **Voyager (2.0)**. Se você utiliza uma atualização anterior, ela pode conter informações diferentes das quais você vê na sua plataforma.
