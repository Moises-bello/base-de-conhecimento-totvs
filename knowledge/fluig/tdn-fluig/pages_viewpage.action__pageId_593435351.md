---
content_hash: cc44189ce5929001c71f5747063b184424332bc581c6438431f5395f11905ea3
fetched_at: '2026-06-28T21:35:27.757238+00:00'
page_id: '593435351'
product: fluig
source: tdn-fluig
title: Plataforma ❙ Recurso de permissão para personificação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=593435351
version: 5
---

.\*ndice

# Falando de recurso de permissão para personificação...

---

Usuário é a pessoa que exerce funções públicas ou particulares dentro da instituição. Os usuários podem ser: funcionários, administradores, participantes, alunos, professores, monitores,

Personificação é quando uma pessoa executa ações em nome de outra. A plataforma possui serviços (APIs, datasets, webservices) que permitem que o usuário do contexto seja diferente do usuário logado. Por exemplo, o usuário acessa a API de workflow com o id "user1" e chama o método que movimenta uma solicitação workflow. Porém esse método tem um parâmetro que informa a partir de qual usuário será feita a movimentação, nesse caso pode ser passado o  id "user2", possibilitando que o user1 consiga movimentar uma solicitação que está com o user2. 

Esse recurso é essencial para automatizar alguns processos, no caso de ter um usuário "Integrador" que movimenta as solicitações atrasadas automaticamente. 

Importante!

Para que a personificação possa ser aplicada, além da permissão liberada, também é necessário que o serviço desejado tenha sido implementado com esse recurso. Veja todos os itens que receberam esse controle na documentação de .

## Controle de personificação

---

| Tipo | Nome do recurso | Opções de permissão |
| --- | --- | --- |
| Personification | Personificação de usuários | **Personificar**: Quando ativada, permite executar ações utilizando o ID de outro usuário. |

Aplicação da permissão

Caso não seja realizada nenhuma alteração nessas permissões, por padrão os recursos permanecem com acesso liberado. A partir do momento em que é configurado um grupo, papel ou usuário com a permissão, somente quem teve a permissão liberada passa a ter acesso ao recurso. Com exceção dos usuários com perfil administrador, que sempre terão acesso aos recursos.

Fique atento!

Esta documentação é válida a partir da atualização **Voyager (2.0)**. Se você utiliza uma atualização anterior, ela pode conter informações diferentes das quais você vê na sua plataforma.
