---
content_hash: d775b0ea6779253d36de7f13887e7585d5614991eb25d3fd89a572666ed00596
fetched_at: '2026-06-28T21:35:22.110408+00:00'
page_id: '235320880'
product: fluig
source: tdn-fluig
title: SOC - Ao adicionar um grupo de usuários em uma comunidade, usuários adicionados
  posteriormente no grupo serão adicionados também na comunidade?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235320880
version: 6
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**TOTVS Fluig Plataforma

# Ocorrência

Adicionamos um grupo de usuários a uma comunidade por meio da opção 'Adicionar usuário por grupo', no entanto notamos que ao adicionar um novo usuário a este grupo, o sistema não insere este novo usuário na lista de participantes da comunidade.

É necessário incluir o usuário na comunidade novamente? Acreditamos que o ideal seria quando o usuário fosse adicionado ao grupo, automaticamente fosse inserido em todas as comunidades a qual o grupo foi adicionado.

# Solução

O recurso 'Adicionar usuário por grupo' que está disponível para o administrador da comunidade tem por objetivo facilitar a adição dos usuários. Ao executar este processo, o sistema pesquisa todos os usuários pertencentes ao grupo selecionado e adiciona na comunidade. Ou seja, o grupo não é vinculado com a comunidade, somente os usuários que fazem parte do mesmo naquele momento.  
  
Tendo em vista que o grupo não possuí vinculo com a comunidade, a plataforma Fluig não efetuará a adição automática caso novos usuários sejam incluídos no grupo.  
  
Para agilizar esta rotina, é possível criar um widget que adicione automaticamente os usuários nas comunidades. A plataforma Fluig possui alguns métodos em sua API pública que permitem adicionar usuários ou grupos na comunidade. A seguir, disponibilizamos a documentação oficial das APIs do TOTVS Fluig Plataforma e também as páginas para auxiliar no desenvolvimento de widgets:

* [API Publica Fluig CommunityServiceRest](https://api.fluig.com/old/resource_CommunityServiceRest.html)
* [Construção de componentes WCM no Fluig Studio](http://tdn.totvs.com/x/rYHIBg)
