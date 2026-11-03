---
content_hash: f14b93f45979b3322d13bd139e486f6ee23bd126d9783877fdf9db204a80bd42
fetched_at: '2026-06-29T00:11:43.374753+00:00'
page_id: '804620024'
product: rm
source: tdn-rm
title: TCGI - Comissão - Permissões de Acesso em Perfil de usuários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=804620024
version: 8
---

---

Com o uso da nova comissão, as permissões de acesso para os corretores e usuários que manipulam este cadastro no Portal de Imóveis passaram a ser tratadas diretamente no TCGI, porém ainda sofrem algumas influências dos parâmetros deste portal.

Neste documento, procuramos mapear este comportamento, para que estas permissões sejam aplicadas corretamente de acordo com a função do usuário que está acessando o Portal de Imóveis, doravante denominado PI.

Resumidamente, para que o corretor ou o seu supervisor tenham acesso à comissão e aos seus os itens no PI, devem ser aplicadas as permissões abaixo, que podem ser combinadas conforme o grupo e nível de acesso de cada usuário, sejam eles corretores, administradores de imobiliária, administrador/gestor do portal de imóveis, etc.:

* Permissões no Perfil do RM:
  + **[01.01.03.08] - Comissão: Visualizar** (obrigatório);
  + **[01.01.03.09] - Comissão: Incluir**;
  + **[01.01.03.10] - Comissão Editar**; e
  + **[01.01.03.10] - Comissão Excluir.**
* Permissões no Grupo do Portal de Imóveis:
  + **Papel Exercido: Corretor** (obrigatório);
  + **Permissões Comissão: Editar comissão** (opcional para se ter acesso à Comissão a partir da Visão de Propostas/Contratos);
  + **Ver Qualquer Proposta:** Ao aplicar esta permissão o usuário poderá manipular as comissões de todos os Corretores, independentemente dele ser o Administrador de Imobiliária. Geralmente esta permissão é aplicada a um usuário da Incorporadora responsável por gerenciar o Empreendimento;
  + **Ver Propostas dos Subordinados e seus Subordinados:** Ao aplicar esta permissão o usuário poderá manipular as comissões dos Corretores que estejam subordinados a ele. Geralmente esta permissão é aplicada a Administradores de Imobiliária;

### **Parametrizando o Grupo no PI:**

* No PI, o que define um corretor é a permissão aplicada no "papel exercido" de corretor, do grupo ao qual o mesmo está associado:

* Para que este usuário tenha acesso ao menu de comissão da tela de visão das propostas/contratos, é necessário dar permissão na opção

Ao aplicar esta permissão no PI, o usuário terá acesso ao menu de comissões a partir da Visão de Propostas e Contratos, sem a necessidade de editar a proposta:

* Nas Permissões de Proposta, as opções abaixo devem ser aplicadas conforme o nível de acesso dos usuários do PI (Corretor, Administrador Imobiliária, Administrador Portal de Imóveis, etc) porque elas afetam as ações destes na Comissão:

+ **Ver Qualquer Proposta:** Ao aplicar esta permissão o usuário poderá manipular as comissões de todos os Corretores, independentemente dele ser o Administrador de Imobiliária. Geralmente esta permissão é aplicada a um usuário da Incorporadora responsável por gerenciar o Empreendimento;
+ **Ver Propostas dos Subordinados e seus Subordinados:** Ao aplicar esta permissão o usuário poderá manipular as comissões dos Corretores que estejam subordinados a ele. Geralmente esta permissão é aplicada a Administradores de Imobiliária;

### Exemplo prático: as permissões aplicadas no PI combinadas com as permissões do RM

* **[01.01.03.08] - Comissão Visualizar:** Ao aplicar esta permissão, no PI, o corretor poderá visualizar os Itens da Comissão de cada comissionado listado na visão de comissões do portal.

Esta permissão é obrigatória para que todos usuários, independentemente do Grupo aos quais os mesmos estão associados,  tenham acesso aos *Itens de Comissão* do PI. Sem esta permissão será exibida uma exceção informando que o usuário não tem acesso a esta funcionalidade.

* **[01.01.03.09] - Comissão Incluir:** Ao aplicar esta permissão no PI, o corretor poderá Adicionar Comissionado à Proposta acessada, desde que a Modalidade de Comissão associada à mesma tenha em sua Regra a opção de Corretores Avulsos. É importante ressaltar que a Permissão de visualizar comissão também deve estar liberada, para que o Corretor tenha acesso à visão dos Itens da Comissão, no PI;

* **[01.01.03.10] - Comissão Editar:** Ao aplicar esta permissão no PI, o corretor poderá editar os Itens de Comissão da Proposta acessada. É importante ressaltar que a Permissão de visualizar comissão também deve estar liberada, para que o Corretor tenha acesso à visão dos Itens da Comissão, no PI;

* **[01.01.03.11] - Comissão Excluir:** Ao aplicar esta permissão no PI, o corretor poderá excluir os Itens de Comissão da Proposta acessada. É importante ressaltar que a Permissão de visualizar comissão também deve estar liberada, para que o Corretor tenha acesso à visão dos Itens da Comissão, no PI;

Resumidamente, para que o Corretor e o seu Supervisor tenha acesso aos Itens de Comissão no PI, devem ser aplicadas as Permissões abaixo, que devem ser combinadas conforme o Grupo de acesso de cada usuário neste portal (Corretor, Administrador de Imobiliária, Administrador do Portal de Imóveis):

* **[01.01.03.08] - Comissão: Visualizar** - Esta permissão é obrigatória para que todos usuários, independentemente do Grupo aos quais os mesmos estão associados,  tenham acesso aos Itens de Comissão do PI. Sem esta permissão será exibida uma exceção informando que o usuário não tem acesso a esta funcionalidade;
* **[01.01.03.09] - Comissão: Incluir** - Esta permissão deve ser aplicada aos usuários que podem acrescentar um comissionado avulso (Item de Comissão) à Proposta, desde que atenda à Regra citada anteriormente;
* **[01.01.03.10] - Comissão Editar:** Com esta permissão o corretor poderá editar os Itens de Comissão da Proposta acessada. É importante ressaltar que a Permissão de visualizar comissão também deve estar liberada, para que o Corretor tenha acesso à visão dos Itens da Comissão, no PI;

As demais permissões desta árvore são utilizadas exclusivamente para o acesso de processos no TCGI, não influenciado as funcionalidades do PI:
