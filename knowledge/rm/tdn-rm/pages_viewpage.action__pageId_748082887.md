---
content_hash: f288fc78610361d7c5f8c50f98623acb1c0fafb01708523435be23eb7c548d9f
fetched_at: '2026-06-29T00:11:32.779782+00:00'
page_id: '748082887'
product: rm
source: tdn-rm
title: Relatórios - Recebimentos por Empreendimento por Período - Smart View
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=748082887
version: 7
---

Este relatório apresenta os **Recebimentos por Empreendimento por Período**, trazendo as seguintes informações:

Importante!

Para ter acesso a este relatório, é preciso que o Perfil do usuário tenha acesso à opção: *[01.02.01] - Empreendimento*, sem necessidade de dar permissões de acesso aos níveis abaixo deste.

* **Coligada:** Neste agrupador o sistema apresenta o Código da [Coligada](https://tdn.totvs.com/display/LRM/Coligada) e a sua Descrição no sub cabeçalho deste relatório.

Esta informação pode ser filtrada através do Parâmetro de Visualização *Cód Coligada*, onde o valor *-1*, que é o valor padrão/default, processa todas as coligadas e caso o usuário queira filtrar uma ou mais coligadas específicas, pode-se realizar esta ação alterando este valor e/ou acrescentando as demais coligadas, através do botão "+" localizado em frente à descrição do mesmo;

* **Empreendimento:** Nesta coluna é apresentado o Código do [Empreendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=435105154) e o seu Nome de Fantasia.

Nos Parâmetros de Visualização, o sistema trás por padrão o valor *-1*, que processa todos os empreendimentos e como ocorre com o parâmetro da entidade acima, caso o usuário tenha necessidade, pode-se filtrar um ou mais empreendimentos específicos através dos botões destinados a este fim;

* **Valor Total:** Esta coluna apresenta o somatório das parcelas a receber que estão ativas nos planos de financiamento das vendas, Como parcelas ativas entende-se, as parcelas com situação Em Aberto, Baixadas Parcialmente e Baixadas;
* **Valor Recebido:** Esta coluna apresenta o somatório do valor baixado de todas as parcelas das vendas efetivadas, por Empreendimento;

O sistema considera os valores do campo Valor Baixado, da tabela de [Lançamentos](https://tdn.totvs.com/pages/viewpage.action?pageId=421388578) do financeiro, que incorpora além dos valores calculados pelo reajuste do imobiliário, os valores calculados pelo financeiro, no momento da baixa;

* **Valor Recebido no Prazo:** Esta coluna apresenta o somatório dos valores das parcelas recebidas até a Data de Vencimento das mesmas, ou seja, das parcelas baixadas sem atraso;
* **Valor Recebido com Atraso:** Esta coluna apresenta o somatório dos valores das parcelas recebidas após a Data de Vencimento das mesmas, ou seja, das parcelas baixadas com atraso;
* **Recebido (%):** Esta coluna apresenta o cálculo Percentual do total dos valores recebidos no período selecionado, em relação ao somatório dos valores das parcelas, das vendas já efetivadas, na posição atual, agrupadas por empreendimento.
* **Atraso no Recebimento (%):** Esta coluna apresenta o cálculo Percentual dos valores das parcelas recebidas em atraso, ou seja, após a data de vencimento delas, durante o período selecionado, em relação ao somatório dos valores das parcelas, das vendas já efetivadas, na posição atual, agrupadas por empreendimento.

Ressaltamos que, por questões de performance, este relatório não realiza nenhum cálculo de atualização do Valor Líquido das Parcelas, cabendo ao usuário executar previamente os processos destinados à [atualização monetária](https://tdn.totvs.com/pages/viewpage.action?pageId=546260610) das parcelas das vendas.
