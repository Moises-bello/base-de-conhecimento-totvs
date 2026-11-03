---
content_hash: 7d05a06251140f04c90093074bea10c398cd7a1f675a5c120d6999a85375e6ec
fetched_at: '2026-06-29T00:11:38.342892+00:00'
page_id: '784771213'
product: rm
source: tdn-rm
title: Conversor de Comissão - Regras Utilizadas para a Conversão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=784771213
version: 2
---

O processo de conversão das comissões considera as seguintes condições:

* Os Parâmetros para Integração com Movimento são lidos da tabela de Comissão e migrados para a tabela de Parâmetros do Movimento, sendo posteriormente serem associados a nova comissão;
* São migrados os dados da integração financeira e folha de pagamento;
* Em cenários em que existe o vendedor e não existe comissão associada, será criado um item para cada caso, na comissão com valores zerados;
* Em cenários em que existem um vendedor e existe mais de uma comissão associada, será criado um item para cada caso com os seus respectivos valores;
* Nas comissões migradas, só pode haver um único [Corretor da Proposta](https://tdn.totvs.com/display/LRM/Regra), os demais comissionados/vendedores serão classificados como Outros Comissionados;
* O Corretor da Proposta na nova comissão, é definido pelo vendedor principal ou de maior valor na antiga comissão ou o primeiro registro caso os valores sejam iguais;
* A Data da Comissão é definida como a Data da Venda, ao qual ela está associada;
* A Data de Vencimento utilizada como Data Base da comissão é, ou a data da competência, quando houver integração com a folha de pagamento, ou a data da venda, quando não houver esta integração;
