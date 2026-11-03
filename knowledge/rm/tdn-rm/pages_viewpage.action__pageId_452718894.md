---
content_hash: bba74a191fabfb86f748702b2b098a5fae56ef2b97726264ea91667e4790374f
fetched_at: '2026-06-29T00:10:02.410531+00:00'
page_id: '452718894'
product: rm
source: tdn-rm
title: Assistente Integração com RMNucleus
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718894
version: 2
---

**Assistente Integração com RMNucleus**

Este processo estará disponível apenas para usuários que possuem o Totvs Segurança e Saúde Ocupacional, integrado com o Totvs Gestão de Estoques, Compras e Faturamento através do parâmetro "Integrado com RM Nucleus" disponível através do Parametrizador, no menu Opções / Parâmetros / RM SSO.

Ao integrar o Totvs Segurança e Saúde Ocupacional com o Totvs Gestão de Estoques, Compras e Faturamento, deverão ser informados no momento da integração os tipos de movimento:

**Tipo de Movimento Entrada, Tipo de Movimento Descarte, Tipo de Movimento Empréstimo e Tipo de Movimento Devolução.**

Informações estas previamente cadastradas no Totvs Gestão de Estoques, Compras e Faturamento.

O assistente do processo de integração está disponível através do menu:

Na nova MDI: EPI/EPC-> Integração RM Nucleus. No executável em: Segurança e Saúde Ocupacional-> Integração RM Nucleus.

**Observação:**

A integração só ocorrerá com os EPIs da coligada corrente.

**Realizando a integração:**

Abrir o processo de Integração RM Nucleus, e clicar em Avançar. Na segunda tela do assistente nas três primeiras colunas, serão exibidos apenas os EPI's do Totvs Segurança e Saúde Ocupacional que ainda não foram vinculados a algum produto do Totvs Gestão de Estoques, Compras e Faturamento.

Nas três colunas seguintes, serão exibidas informações do produto a ser integrado. A sétima coluna, traz um lookup, que permite escolher a qual produto do Totvs Gestão de Estoques, Compras e Faturamento será vinculado o EPI do Totvs Segurança e Saúde Ocupacional.

**Observação:**

O sistema realizará a vinculação apenas a produtos que não possuam seu estoque zerado.

Caso não deseje integrar todos os produtos de uma só vez, poderá fazê-lo por partes. Na terceira tela do assistente, o usuário deverá selecionar o EPI na lista à esquerda, e preencher os dados necessários que aparecerão na parte direita da tela.

Na aba identificação, o usuário deverá obrigatoriamente informar o Identificador do Lote, o Identificador Inicial e a Quantidade de EPI é trazida automaticamente do Totvs Gestão de Estoques, Compras e Faturamento.

Após o preenchimento de todos os campos necessários, o usuário deverá clicar no botão: "Lançar Lote".

Ainda na mesma tela, na aba: "Lotes Lançados",  o sistema exibe todas as informações do lote lançado e caso algum lançamento tenha sido feito equivocadamente, o sistema permite a exclusão deste.

Na mesma tela, na aba: "EPI's Emprestados" caso existam itens emprestados, será necessário que o usuário selecione o EPI do lote que acabou de ser cadastrado para que os EPIs antigos possam ser descartados.

No último passo, será disponibilizado o botão "Executar" que irá processar as informações da integração e gerar o estoque de produtos correspondentes no Totvs Gestão de Estoques, Compras e Faturamento.

Após a integração o controle de unidades de EPI será totalmente realizado pelo Totvs Gestão de Estoques, Compras e Faturamento.

A inclusão de novos EPIs também deverá ser feita pelo Totvs Gestão de Estoques, Compras e Faturamento, bem como o acréscimo de novas unidades de EPI´s já existentes.
