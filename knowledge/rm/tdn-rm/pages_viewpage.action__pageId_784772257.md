---
content_hash: b6b0c6e5a1b1f111400e2885eacc9c3735ea54ade5e10ffbeea866ca7aa43d46
fetched_at: '2026-06-29T00:11:38.739435+00:00'
page_id: '784772257'
product: rm
source: tdn-rm
title: 02.04 Planos de pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=784772257
version: 3
---

Este passo tem como objetivo exibir os planos de pagamentos para que o candidato possa visualizar ou alterar o plano de pagamento para aquela matrícula.  
Essa tela será exibida na matrícula, caso o parâmetro "Cadastrar contrato" seja habilitado, possua um plano de pagamentos de pagamento definido para o período letivo e matriz aplicada da área ofertada.  
Caso seja informado um plano de pagamento padrão, este será marcado automaticamente na tela, se o parâmetro "Permite alterar o plano de pagamento no portal" estiver desmarcado, será exibido somente o plano de pagamento padrão, caso o parâmetro esteja desmarcado e possua mais de um plano de pagamento, o sistema irá dar a liberdade ao candidato ou responsável de escolher o plano.

 Caminho de acesso aos parâmetros no sistema: 

* **TOTVS Educacional Processo Seletivo| Cadastros| Área de interesse Ofertada| Aba Matrícula**

Plano de pagamento e bolsa associado ao prospect

Para informações referentes à prospecções, clique [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=702373785).

ATENÇÃO

A partir dos patches **12.1.2306.197** e **12.1.2310.131** na realização da matrícula na central do candidato, caso o candidato tenha prospecções de bolsas, o sistema irá considerar as datas de vencimentos das parcelas do plano de pagamento vinculado à área de interesse considerada na matrícula para verificação da validade das bolsas.

Concurso de Bolsa

Se o candidato tiver adquirido uma bolsa processada através da funcionalidade “**Concurso de Bolsa**”, os valores apresentados pela simulação do plano de pagamento já serão mostrados considerando o desconto da bolsa.

Conforme a imagem abaixo, será apresentado um texto informando ao candidato.

Para saber mais sobre "**Concurso de bolsa**" [clique aqui](https://tdn.totvs.com/display/LRM/Concurso+de+Bolsa).

Informações sobre .

* É importante ressaltar que nos casos de cursos que os seus valores são calculados baseado no número / valor de crédito, e que a parcela do plano de pagamento esteja parametrizada para que o valor seja calculado automaticamente, o campo “Código da Turma” disponibilizado na aba “Acadêmico” deverá ser devidamente preenchido para que seja possível disponibilizar a simulação dos valores do Plano de Pagamento
* É possível parametrizar o TOTVS Educacional para que ao criar as parcelas no contrato do aluno a partir do plano de pagamento, sejam consideradas do plano de pagamento somente as parcelas com vencimento a partir do mês da inclusão do plano de pagamento no contrato. Para saber mais [clique aqui](https://tdn.totvs.com/display/LRM/Tesouraria) ( recurso disponível a partir da versão 12.1.33 ).

Importante

Caso a parametrização citada anteriormente esteja habilitada, é importante que as parcelas que terão lançamentos gerados estejam de acordo com o plano de pagamento.

Em alguns casos podem estar parametrizado como **"Parcela inicial" = 1** e **"Parcela final" = 1**, e se a parcela de número 1 estiver vencida, a mesma será desprezada, e com isso não haverá parcelas com lançamentos gerados ocasionando a apresentação da mensagem abaixo ao realizar a matricula.
