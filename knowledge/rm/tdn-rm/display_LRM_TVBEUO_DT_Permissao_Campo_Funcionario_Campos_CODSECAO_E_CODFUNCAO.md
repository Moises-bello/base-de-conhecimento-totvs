---
content_hash: 09fb20af368ae858f34c7389e71cf9ee49638e0f184831120b90d2034067133a
fetched_at: '2026-06-29T00:08:11.566919+00:00'
page_id: '243012965'
product: rm
source: tdn-rm
title: TVBEUO_DT_Permissao_Campo_Funcionario_Campos_CODSECAO_E_CODFUNCAO
type: documentation
url: https://tdn.totvs.com/display/LRM/TVBEUO_DT_Permissao_Campo_Funcionario_Campos_CODSECAO_E_CODFUNCAO
version: 113
---

# FUNCIONÁRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cadastro de Funcionário* |
| **Situação/Requisito:** | Verificamos que ao retirar a opção “Pode alterar” dos campos “codfuncao, codsecao e salario” da tabela PFUNC dos perfis associados a um usuário, ao editar o cadastro do funcionário estes campos são apresentados corretamente (somente podem ser visualizados), mas no momento de admitir um novo funcionário, os campos “codfuncao, codsecao" estão livres para inserção de dados diferente do campo “salario” que está sendo apresentado somente para visualização.  Neste caso, entendemos que todos devem possuir o mesmo comportamento. |
| **Solução/Implementação:** | *Ajustado permissão dos campos CODFUNCAO e CODSECAO após executar a inclusão de funcionário.* |
| **Chamados relacionados:** | *TVBEUO* |

divs
