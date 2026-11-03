---
content_hash: 8e41171b172d5e11320cd7e13c016a0b9302167e9f34fd1bc9f2a249dcb1c0ca
fetched_at: '2026-06-29T00:06:14.551310+00:00'
page_id: '210047711'
product: rm
source: tdn-rm
title: Compartilhar Filtros Entre Módulos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=210047711
version: 125
---

# Como Compartilhar Filtros Entre Módulos

|  |  |
| --- | --- |
| **Produto:** | Framework |
| **Versões:** | 11.82.41, 12.1.8 |
| **Ocorrência:** | Novo parâmetro global "**Compartilhar filtros entre módulos**". |
| **Ambiente:** | Filtros em visões de cadastro compartilhadas por mais de um produto. |
| **Passo a passo:** | Na nova MDI, o parâmetro "Compartilhar filtros entre módulos" trata o comportamento dos filtros das visões de cadastros pertencentes a mais de um módulo.      Como exemplo utilizaremos a visão de Funcionários que é utilizada nos módulos Folha de Pagamento (Pai da visão) e Gestão de Pessoas:   falseNOTAS    * Este parâmetro afeta somente o uso do sistema através da nova MDI.  * "Pai da visão" – Utilizaremos este termo quando a visão de cadastro é originalmente de um produto. Como por exemplo: Funcionários em Folha de Pagamento que é compartilhado entre Gestão de Pessoas ou Cadastro de Clientes Fornecedores em Gestão Financeira que é compartilhado entre Gestão de Estoque Compras e Faturamento.    **1)       Quando o parâmetro esta desmarcado (Valor padrão deste parâmetro).**    Ao acessar a visão de Funcionários pelo módulo Folha de Pagamento (módulo Pai da visão), são exibidos filtros deste módulo.    Para exemplificar criamos um novo filtro e nomeamos “\_Módulo Folha de Pagamento”.    Ao acessar a visão de Funcionários pelo módulo Gestão de Pessoas, são exibidos apenas os filtros do módulo Gestão de Pessoas.    Exemplificando criamos um novo filtro e nomeamos “\_Módulo Gestão de Pessoas”.    Observe que os filtros mesmo que cadastrados na mesma visão **NÃO** estão compartilhados entre os módulos.     ---   **2)       Quando o parâmetro está marcado.**    Ao marcar o parâmetro, os filtros da visão pai passam a ser exibidos em todos os módulos que compartilham desta visão de cadastro. Caso um novo filtro seja criado em outro módulo que não seja o módulo pai, ele também será exibido em todos os módulos.   falseNOTAS  * Com o parâmetro marcado os filtros criados nas visões de outros produtos ficarão ocultos adotando os filtros da visão pai.    Ao acessar a visão de Funcionários pelo módulo Folha de Pagamento (módulo Pai da visão), são exibidos os filtros criados inicialmente no módulo Folha de Pagamento    Ao acessar a visão de Funcionários pelo módulo Gestão de Pessoas, são exibidos todos filtros da visão. Observe que são exibidos os filtros da visão pai.    Criando um novo filtro pelo módulo Gestão de Pessoas, com exemplo “\_Novo filtro Gestão de Pessoas” ele integrará aos filtros da visão pai.    Assim, o filtro também será exibido em outros módulos como o Folha de Pagamento (visão filho)      **Filtros compartilhados com Consulta SQL:**  Com o parâmetro 'Compartilhar filtro entre módulos' serão exibidas as consultas do contexto para o filtro IN (SQL). Exemplo: Ao acessar a tela de funcionários com o módulo 'Automação de Ponto' aberto, ao criar um filtro com operador IN (SQL), serão exibidas as consultas do sistema A (Automação de Ponto). Caso a tela de funcionários seja acessada com o módulo 'Folha de Pagamento' aberto, ao criar um filtro com operador IN (SQL), serão exibidas as consultas do sistema P (Folha de Pagamento). |
| **Observações:** |  |

divs
