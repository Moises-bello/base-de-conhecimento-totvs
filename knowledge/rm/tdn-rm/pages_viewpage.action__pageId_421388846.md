---
content_hash: 5d1d79285948aa7d37e87dccc7e4fdeebd4f32132b5a6cb66ab2a8b4e37fdc55
fetched_at: '2026-06-29T00:09:19.358986+00:00'
page_id: '421388846'
product: rm
source: tdn-rm
title: Controle de Alçada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388846
version: 5
---

O Controle de Alçada foi desenvolvido com o objetivo de gerenciar as permissões concedidas a um grupo de usuários para acessar/executar o cadastro de Template de Acordo e os processos vinculados a rotina, será realizado através do serviço de  [Globais no Perfil.](http://tdn.totvs.com/x/bbAQG)

Criado dois processos com as opções de permissão:

* Template de Acordo (Inserir | Editar | Remover)
* Gerenciar Acordo  (Editar | Excluir | Cancelar e Aprovar)

Será necessário vincular ao Perfil, no Menu: Anexos | Templates de Acordo Financeiro o(s) Template(s) de Acordo desenvolvido para realização da negociação.

A utilização dos Templates para realizar o Acordo dependerá também do Valor Líquido dos Lançamentos de origem sendo compreendidos pelo Valor da Faixa dos valores a negociar, disponível no Cadastro do Template de Acordo.

No Totvs Gestão Financeira ao ser chamado o processo de gerar acordo, será exibido os templates permitidos cabendo ao usuário selecionar o desejado. Caso exista somente um Template que atenda as regras o mesmo será selecionado automaticamente.   
Para que seja efetivo a liberação ou restrição de acesso é necessário realizar Logout / Login após alterações no perfil de usuários.

Ao excluir registro de template de acordo excluir também os meios de pagamentos vinculados (FTEMPLATEACORDOPAGTO), os vínculos do template com perfis (informados no cadastro de perfil, FTEMPLATEACORDOPERFIL) e as matrizes curricular vinculadas (FTEMPLATEACORDOHABILITFILIAL).

Veja Também
