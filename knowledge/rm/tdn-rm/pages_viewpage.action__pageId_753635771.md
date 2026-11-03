---
content_hash: e93e81ae19a44fbd5062a894110d8cd5e24d632a3fd1251f2abd7633b16388c1
fetched_at: '2026-06-29T00:11:33.210160+00:00'
page_id: '753635771'
product: rm
source: tdn-rm
title: Relatórios - Análise de Carteira - Smart View
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=753635771
version: 5
---

O relatório de **Análise de Carteira** apresenta informações relativas às parcelas dos contratos de vendas ativos das coligadas e empreendimentos filtrados, promovendo os insumos para a tomada de decisão aos gestores.

Como contratos ativos são considerados as vendas com as situações: Em Preparação, Efetivados, Quitados e Bloqueados.

Importante!

Para ter acesso a este relatório, é preciso que o Perfil do usuário tenha acesso à opção: *[01.02.01] - Empreendimento*, sem que seja necessário dar permissão nas demais opções abaixo desta.

Ao acessar este relatório no Smart View, é possível de se aplicar os seguintes *Parâmetros de Visualização*:

* **Código da Coligada:** Neste parâmetro é possível de se filtrar as Coligadas, onde o valor padrão *-1*, processa todas as coligadas e caso o usuário queira filtrar uma ou mais coligadas específicas, pode-se realizar esta ação alterando este valor e/ou acrescentando as demais coligadas, através do botão "+" localizado em frente à descrição do mesmo;
* **Código do Empreendimento:** Neste parâmetro é possível de se filtrar o Código do Empreendimento, onde o valor padrão -1, processa todos os empreendimentos e como ocorre com o parâmetro da entidade acima, caso o usuário tenha necessidade, pode-se filtrar um ou mais empreendimentos específicos através dos botões destinados a este fim;

Após definir estes parâmetros e gerar o relatório, o sistema apresentará as seguintes informações:

* Agrupador **Consolidado**: Onde é apresentado um totalizador com o resumo de todas as coligadas e empreendimentos selecionados com os seguintes campos:
  + **Nº. de Parcelas Recebidas:** É a soma da quantidade de todas as parcelas recebidas em relação aos parâmetros aplicados acima;
  + **Valor Recebido:** É a soma dos valores baixados de cada parcela. Este valor considera além dos valores do imobiliário, os valores inseridos pelo módulo financeiro;
  + **% de Parcelas Recebidas:** É o percentual de parcelas recebidas sobre o número total de parcelas filtradas pelos parâmetros deste relatório;
  + **Nº. de Parcelas Futuras:** É soma da quantidade de todas as parcelas que irão vencer após a data de geração deste relatório;
  + **Vr. a Receber das Parcelas Futuras:** É a soma dos valores a receber das parcelas futuras, que estão consolidados/gravados na base de dados. Ou seja, este relatório não executa nenhum cálculo de atualização destes valores, em memória;
  + **% de Parcelas Futuras:** É o percentual das parcelas futuras, em relação à quantidade total de parcelas filtradas nos parâmetros do relatório;
  + **Nº. de Parcelas em Atraso:** É a soma da quantidade de todas as parcelas a receber em atraso, considerando a data de geração deste relatório;
  + **Vr. a Receber em Atraso:** É a soma dos valores a receber das parcelas em atraso, que estão consolidados na base;
  + **% de Parcelas em Atraso:** É o percentual das parcelas em atraso, em relação à quantidade total de parcelas filtradas nos parâmetros do relatório.

* Detalhamento por **Coligada**: Neste agrupador o sistema apresenta as seguintes informações detalhadas por coligada:

* + **Empreendimento:** É o nome de fantasia do empreendimento. Caso o mesmo não esteja preenchido, esta informação ficará em branco;
  + **Nº de Parcelas Recebidas:** É a soma da quantidade de parcelas recebidas, dos contratos de vendas deste empreendimento;
  + **Valor Recebido:** É a soma dos valores baixados de cada parcela, das vendas deste empreendimento. Este valor considera além dos valores do imobiliário, os valores inseridos pelo módulo financeiro;
  + **Nº de Parcelas Futuras:** É soma da quantidade de todas as parcelas das vendas deste empreendimento, que irão vencer após a data de geração deste relatório;
  + **Vr. a Receber das Parcelas Futuras:** É a soma dos valores a receber das parcelas futuras, dos contratos de vendas deste empreendimento, que estão consolidados/gravados na base de dados;
  + **Nº. de Parcelas em Atraso:** É a soma da quantidade de todas as parcelas a receber em atraso, para as vendas deste empreendimento, considerando a data de geração deste relatório;
  + **Vr. a Receber em Atraso:** É a soma dos valores a receber das parcelas em atraso, para as vendas deste empreendimento, que estão consolidados na base;
  + **% de Parcelas em Atraso:** É o percentual das parcelas em atraso, das vendas deste empreendimento, em relação à quantidade total de parcelas filtradas nos parâmetros do relatório.
