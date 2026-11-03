---
content_hash: b2da73fbe4d347477442c6b5c8b16ad7b800cc6c457b42d013f00d2f6b0e358f
fetched_at: '2026-06-29T00:08:44.408631+00:00'
page_id: '307851482'
product: rm
source: tdn-rm
title: Artigo 578/545/582 – Contribuição Sindical
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=307851482
version: 11
---

**Assunto**

|  |  |
| --- | --- |
| **Produto:** | RM |
| **Versões:** |  |
| **Ocorrência:** | Art. 578. As contribuições devidas aos sindicatos pelos participantes das categorias econômicas ou profissionais ou das profissões liberais representadas pelas referidas entidades serão, sob a denominação de contribuição sindical, pagas, recolhidas e aplicadas na forma estabelecida neste Capítulo, desde que prévia e expressamente autorizadas.”(NR)  Art. 545. Os empregadores ficam obrigados a descontar da folha de pagamento dos seus empregados, desde que por eles devidamente autorizados, as contribuições devidas ao sindicato, quando por este notificados.  Art. 582. Os empregadores são obrigados a descontar da folha de pagamento de seus empregados relativa ao mês de março de cada ano a contribuição sindical dos empregados que autorizaram prévia e expressamente o seu recolhimento aos respectivos sindicatos. |
| **Ambiente:** | Cadastro de Funcionário - Winforms |
| **Passo a passo:** | Art. 545/582 – Contribuição Sindical .    Siga os passos abaixo:  1º) MDI  > RH > Folha de pagamento > Configurações > Parametrizador > Folha Normal > Geral  Marque o parâmetro: Ativar alterações da Reforma Trabalhista de acordo com a Lei Nº 13.467 de 13 de Julho de 2017    2º ) MDI> RH> Folha de pagamento> Administração de Pessoal> Funcionários> Editar funcionário.   Devido ao artigo 545, foi criado uma nova opção de Contribuição Sindical ("X - Não Optante") para os funcionários que não optarem por contribuir com o sindicato de acordo com a Reforma Trabalhista de Julho de 2017.    3º ) MDI  > RH > Folha de pagamento > Administração de Pessoal > Funcionários > Incluir.  No campo “Contribuição Sindical” em Sindicato > Dados do Sindicato o campo permanece vindo vazio. Cajo queira que seja "Não Optante" altere o valor default.   Vazio:    Valor default como "Não Optante":      4º ) MDI > RH > Folha de pagamento > Administração de Pessoal > Alterações Cadastrais > Alteração Campos do Cadastro > Funcionários > Contribuição Sindical.  Trocar globalmente o valor da Contribuição Sindical para o tipo O (Não Optante).    Exemplo de fórmula: |
| **Observações:** |  |
