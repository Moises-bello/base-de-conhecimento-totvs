---
content_hash: 9c03b8e87a8f20bcb0e1d2669d26b52e3bcb757fc1923eab29093153dd13dd6d
fetched_at: '2026-06-29T00:10:58.823226+00:00'
page_id: '607323048'
product: rm
source: tdn-rm
title: 2.14.2 Associação do Template de Acordo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=607323048
version: 3
---

* **Matriz Aplicada**: Possibilita vincular qualquer Template de Acordo à Matriz Aplicada do Módulo Educacional. Essa opção somente será apresentada caso haja integração entre os módulos: TOTVS Educacional e o TOTVS Gestão Financeira e ser verificado no Menu: *Ambiente | Parâmetros | Integrações de Sistemas.*É necessário informar a matriz aplicada pelos campos Curso, Habilitação, Matriz Curricular e Turno. Este vinculo será realizado com o intuito de integrar o Template ao Portal do Educacional, para o TOTVS Gestão Financeira o vínculo deste não interfere nas negociações realizadas pela Visão de Lançamentos. No contexto do TOTVS Gestão Financeira será preciso verificar o nível de ensino do Educacional, para que a Matriz Aplicada seja apresentada corretamente.

* **Serviço**: Possibilita vincular qualquer “Template de Acordo” a um ou vários serviços do TOTVS Educacional. Basta criar um novo e informar o código do serviço. Essa vinculação facilitará e permitirá controlar os modelos de acordo por tipo de serviço de contrato do Educacional, garantindo mais flexibilidade para direcionar a negociação para o modelo mais compatível. Ao gerar um acordo serão buscados todos os templates vinculados ao serviço, e caso não existam nenhum, trará todos que atendam as demais regras de seleção existentes para o template.

No Portal Educacional caso não exista template vinculado ao serviço o processo de negociação é barrado.

* **Perfil do usuário**: Após a criação dos Templates no menu *Contas a Pagar/Receber > Acordo > Template Acordo*, é necessário ainda associa-los no perfil do usuário que irá gerar o Acordo. Assim, é possível estabelecer critérios e alçadas para utilização dos Templates e um perfil X poderá ter acesso apenas a um grupo de Templates, por exemplo. Para realizar a associação dos Templates no perfil do usuário, realize o seguinte procedimento: Acesse o contexto *Serviços Globais > Vá no menu Segurança > Clique na opção Perfis > Filtre e selecione o Perfil que está associado ao usuário que pretende incluir o Acordo > Na opção Sistema que fica na barra superior da visão, escolha a opção Gestão Financeira > Clique em Anexos > Templates de Acordo Financeiro > No anexo que será exibido na parte direita da tela, clique no ícone Incluir > Na tela que será exibida, informe o Template que poderá ser utilizado pelo usuário na geração do Acordo > Clique em Salvar para gravar a nova associação.*

É possível associar mais de um Template ao mesmo perfil.

Aparecerá a tela de filtro, clique em executar;

É possível incluir um template novo ou editar;
