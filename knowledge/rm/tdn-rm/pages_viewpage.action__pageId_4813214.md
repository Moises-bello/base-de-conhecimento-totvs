---
content_hash: 877f547b2a040c56bb45f05631f02e113022b505ca648ae56fff861f17162b15
fetched_at: '2026-06-29T00:10:19.294130+00:00'
page_id: '4813214'
product: rm
source: tdn-rm
title: Natureza Inexistentes ou incompatível para o CliFor na Movimentação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4813214
version: 4
---

BLOCK

Natureza Inexistentes ou incompatível para o CliFor na Movimentação

FAQ: **Natureza Inexistentes ou incompatível para o CliFor na Movimentação**

|  |  |
| --- | --- |
| Produto: | Unspecified |
| Ambiente: | Unspecified |
| Versão: | 11.00 |

Sintoma

* **Sintoma**

Ao informar a CFOP no movimento é apresentada a seguinte mensagem: Código não existe ou é incompatível com estado do cliente

Causa

* **Causas**

1- A CFOP informada não esta cadastrada, esta inativa ou fora do exercício fiscal selecionado.

2- A origem destino da operação não esta compatível com a CFOP.

3- A CFOP informada esta incompatível com o tipo de seleção[1] definida no tipo de movimento.

A CFOP informada não é compatível com a regra de seleção definida nos parâmetros do “TOTVS GESTÃO FISCAL”, ou seja, o Tipo de Seleção2 (Não Seleciona, Simples, Completa, Avançada).

Solução

* **Solução**

1- Cadastrar a CFOP se não existir.

2- Ativar a CFOP caso esteja **NÃO** esteja ATIVA.

3- Se certificar que a CFOP esta dentro do exercício fiscal selecionado/vigente.

4- Os códigos da CFOP devem estar conforme origem destino da operação descritos abaixo:

**ENTRADA**

1 – ENTRADA E/OU AQUISIÇÕES DE SERVIÇOS DO ESTADO

2 – ENTRADA E/OU AQUISIÇÕES DE SERVIÇOS DE OUTROS ESTADOS

3 – ENTRADA E/OU AQUISIÇÕES DE SERVIÇOS DO EXTERIOR

**SAÍDAS**

5 – SAÍDAS OU PRESTAÇÕES DE SERVIÇOS PARA O ESTADO

6 – SAÍDAS OU PRESTAÇÕES DE SERVIÇOS PARA OUTROS ESTADOS

7 – SAÍDAS OU PRESTAÇÕES DE SERVIÇOS PARA O EXTERIOR

5- Certifica-se e se for o caso definir na CFOP para que a mesma esteja dentro das regras de seleção definidas no “TOTVS GESTÃO FISCAL”.

6- Informar uma CFOP compatível com a Origem Destino da Operação conforme diagrama abaixo:

[![clip_image002](http://lh6.ggpht.com/_G7KXZLoZDsY/TK3cRrW-QLI/AAAAAAAAB2U/sM5_VUkCNpQ/clip_image002_thumb%5B1%5D.jpg?imgmax=800 "clip_image002")](http://lh3.ggpht.com/_G7KXZLoZDsY/TK3cQwrS5gI/AAAAAAAAB2Q/ZoiNcESWQek/s1600-h/clip_image002%5B4%5D.jpg)

7- Informar uma CFOP compatível com o Participante da Operação conforme diagrama abaixo:

[![](http://lh6.ggpht.com/_G7KXZLoZDsY/TK3cTAdEYnI/AAAAAAAAB2c/o4akqFHejB0/clip_image002%5B5%5D_thumb%5B1%5D.jpg?imgmax=800 "clip_image002[5]")](http://lh4.ggpht.com/_G7KXZLoZDsY/TK3cSfyx4sI/AAAAAAAAB2Y/UTIQXynrF8M/s1600-h/clip_image002%5B5%5D%5B3%5D.jpg)

* **Informações Adicionais**

****[1]****Seleção Automática por Natureza:

* ***Não Seleciona*** - O sistema não fará nenhuma seleção e o usuário deverá digitar a natureza do movimento.
* ***Seleciona por Movimento*** - O sistema seleciona, de acordo com as regras de seleção de naturezas do TOTVS Gestão Fiscal, a(s) natureza(s) que melhor se adapta(m) ao movimento.
* ***Seleciona por Item***: O sistema seleciona a(s) natureza(s) para cada item do movimento, esta seleção também dependerá das regras determinadas no TOTVS Gestão Fiscal.

2 Os Tipos de Seleção da CFOP são:

* ***Não Seleciona*** - O sistema apresentará todas as CFOPs cadastradas e o usuário deverá selecioná-la a partir desta tabela. Neste tipo de seleção, o sistema não realiza nenhum tipo de pesquisa, ficando a encargo do operador a escolha da CFOP.
* ***Simples*** - Irá apresentar as CFOPs próprias à operação, baseado somente na informação relativa à origem ou destino da operação (operações de entrada e saída) e quanto a localização dos clientes ou fornecedores (estadual, interestadual ou exterior).
* ***Completa*** - O sistema fará uma pesquisa no cadastro de CFOP, procurando todas as que possivelmente podem atender à operação. Esta pesquisa é baseada nas “Regras” (restrições) associadas a cada natureza como: estado, cliente, produto, etc. indicadas no cadastro da natureza. Mesmo que sejam encontradas CFOP, sendo umas mais específicas que as outras, o sistema não fará distinção e apresentará uma lista para que escolha a CFOP desejada.
* ***Avançada*** - O sistema tentará encontrar a melhor CFOP para cada tipo de operação, ou seja, dada a (restrição) “regra” de cada CFOP, o sistema irá comparar primeiro as que atendem à operação e depois irá comparar entre as selecionadas, qual a que melhor atende ao caso solicitado.

Observações

O documento em questão está postado no blog da Totvs e pode ser consultado através do link : <http://totvsconnect.blogspot.com/2010/10/dica-natureza-inexistentes-ou.html>
