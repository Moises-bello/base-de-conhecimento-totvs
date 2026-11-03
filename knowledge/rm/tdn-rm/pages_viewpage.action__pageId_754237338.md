---
content_hash: db0a860c1802f47ec634acc520e99215733c16f003e96208b0c20fcbafb5390a
fetched_at: '2026-06-29T00:11:33.225101+00:00'
page_id: '754237338'
product: rm
source: tdn-rm
title: Acesso a dados acadêmicos dos alunos pela filiação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=754237338
version: 27
---

A partir da versão 12.1.2306, ajudando a instituição no controle dos dados referente a LGPD, os responsáveis (pai e mãe) pelo aluno maior de idade não poderão mais acessar as informações do portal do aluno e app de seu filho. Caso isso seja necessário e a autorização do aluno seja captada pela instituição, ela poderá liberar o acesso no cadastro do aluno.  
A solicitação de autorização por parte do aluno pode ser captada pela instituição pelos meios que ela desejar. Nesse momento não iremos inferir algum meio específico para essa captação. 

A partir da versão 12.1.2406, foi disponibilizado um parâmetro para habilitar a permissão para pais (pai e mãe) de alunos maiores de 18 anos terem acesso aos dados Acadêmicos dos alunos independente da permissão concedida ou não no cadastro de filiação do aluno. 

Trata-se de um parâmetro por perfil de usuário, e o mesmo está disponível no módulo de Globais em Segurança > Perfis (Sistema Educacional - Educacional) > Parâmetros Educacionais > Aba Geral:

ACESSO A DADOS ACADÊMICOS

No portal do aluno, para alunos maiores de idade, a filiação só terá acesso aos itens de menus do portal do aluno relacionados aos assuntos acadêmicos, e visualização/alteração de dados cadastrais do aluno, quando o usuário de pai ou mãe possuir a permissão de acesso a Dados Acadêmicos no cadastro do aluno. Mesmo que o perfil do usuário da filiação tenha acesso aos itens de menus de assuntos acadêmicos concedida ao seu perfil.

Também terão acesso automaticamente, usuários de pai ou mãe que também sejam Responsáveis Acadêmicos do aluno, desde que possuam no perfil de usuário as permissões de acesso aos itens de menus de assuntos acadêmicos. Desta forma, mesmo não possuindo explicitamente a permissão na filiação para dados acadêmicos, será concedido o acesso, devido ao papel de Responsável Acadêmico do aluno.

Para alunos menores de idade, não terão alterações no comportamento de acesso aos dados acadêmicos, permanecendo a filiação com o acesso aos dados.

Também não terão alterações nas visualizações dos dados acadêmicos, o próprio aluno. Não sendo necessário qualquer tipo de concessão de permissionamento, a não ser as permissões do perfil de usuário.

O responsável financeiro do aluno tendo permissão no perfil para acesso a matrícula/rematrícula on-line (ensino superior/básico) independente de estar **marcado** o parâmetro **responsável financeiro com acesso aos dados acadêmicos** consegue executar todo o processo de matrícula/rematrícula no portal, basta ele acessar o portal com o usuário cadastrado no Cliente/Fornecedor. Vale frisar que, ao ter acesso ao menu de matrícula/rematrícula o responsável financeiro terá acesso a **todas** as etapas do processo de matrícula, sem nenhuma restrição, se assim estiver parametrizado para exibir os passos.

## Exemplos de filiações com permissões de acesso a Dados Acadêmicos:

Neste exemplo, o pai GERALDO VIEIRA COSTA, não possui a permissão de acesso a dados acadêmicos concedida pelo aluno, porém, ele está cadastrado como Responsável Acadêmico, o que passa a permitir o acesso a estes dados.

Neste exemplo, o pai GERALDO VIEIRA COSTA, possui a permissão de acesso a dados acadêmicos concedida pelo aluno, e não é um Responsável Acadêmico, o que permite o acesso a estes dados.

Neste exemplo, o pai GERALDO VIEIRA COSTA, possui tanto a permissão de acesso a dados acadêmicos concedida pelo aluno quanto também é um Responsável Acadêmico, o que permite o acesso a estes dados.

RESPONSÁVEL FINANCEIRO COM ACESSO A DADOS ACADÊMICOSComportamento depreciado

Até as versões **12.1.2402.237**, **12.1.2406.166**, **12.1.2410.103** e **12.1.2502** o responsável financeiro somente consegue fazer matrícula/rematrícula on-line se tiver permissão no perfil e com o parâmetro **responsável financeiro com acesso aos dados acadêmicos** no cadastro do aluno **marcado**.

A partir da versão 12.1.2306.180 foi incluída uma propriedade que da acesso acadêmico ao Responsável Financeiro do aluno maior de 18 anos, permitindo que ele visualize os dados acadêmicos no portal do aluno.

 

A mesma configuração também é possível no Responsável Financeiro pelo contrato do aluno.

Um detalhe importante relacionado configuração, é que se o Responsável Financeiro do Aluno for o mesmo Responsável Financeiro pelo Contrato, a propriedade fica desabilitada no cadastro de Responsável do Contrato. Neste cenário para que o Responsável Financeiro do contrato/aluno tenha acesso aos dados acadêmicos basta marcar a opção no Responsável Financeiro do cadastro de aluno.

Caso o Responsável Financeiro do aluno seja diferente do Responsável Financeiro do Contrato, é possível marcar a opção nos dois cadastros, permitindo que ambos visualizem os dados acadêmicos do aluno.

O Responsável Financeiro referente à parcela não possui essa parametrização e, portanto, não poderá acessar os dados acadêmicos, a menos que também seja o Responsável Financeiro do aluno ou do contrato.

ACESSO A DADOS FINANCEIROS

Para informações de acesso aos boletos do extrato financeiro consulte [Acesso aos boletos do extrato financeiro](https://tdn.totvs.com/x/5bL-L)
