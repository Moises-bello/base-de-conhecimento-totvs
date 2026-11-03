---
content_hash: 4618ad130a5091f79d6b7da30d2f05ea06f08a86af5e240a5dd55cfb12e3957f
fetched_at: '2026-06-29T00:08:14.881030+00:00'
page_id: '244719734'
product: rm
source: tdn-rm
title: EF_Venda_Geração de Boleto Automático - 12.1.13
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244719734
version: 23
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Incorporação |
| **Versões:** | 12.1.13 |
| **Ocorrência/ Chamado:** | TQDOAV |
| **Ambiente:** | RM |
| **Passo a passo:** |  |
| **Observações:** | Especificação Técnica  o  [ER\_CPTIN001-255\_Agrupamento\_de\_Boleto\_Automatico](http://tdn.totvs.com/display/LRM/ER_CPTIN001-255_Agrupamento_de_Boleto_Automatico) |

# Objetivo

Permitir a geração automática de boletos de cobrança através da Venda TIN, conforme parametrização especifica para a versão revitalizada do TIN

# Regra de Negócio

A geração automática de boleto será um recurso da Venda Imobiliária TIN, onde será gerado o Nosso Número, já o código de barras será gerado no processo de remessa bancária.

Será criado um parâmetro para ***Gerar Boleto Automaticamente***, por coligada que será considerado default para os processos que geram lançamento financeiro ou que alteram lançamentos gerados.

O default deste parâmetro será **Desmarcado**, assim não altera o comportamento atual  e apenas os clientes que desejarem acionam o novo recurso. Ao marcar o parâmetro por Coligada, o mesmo default será aplicado ao parâmetro apresentado na tela de cada processo  que gera lançamento financeiro:

* Efetivar Venda;
* Desbloquear Lançamentos Financeiros;
* Efetivar Aditivo de Renegociação de Parcelas;
* Gerar IPTU;
* Gerar Seguro por Empreendimento.

O novo parâmetro afetara novas vendas e novos processos, e o legado deve ser tratado manualmente pelo usuário.

## Geração Automática de Boleto

A Geração automática dos boletos, ocorrerá desde que o parâmetro da venda esteja marcado, nos seguintes processos:

* **Efetivar Venda/ Desbloquear Lançamento Financeiro.**

Se o parâmetro *"Parâmetros->Integração Financeira->3/4-> **Efetivar venda e gerar Lançamento no RMFluxus**"* estiver Marcado a geração automática do boleto acontecerá na efetivação da venda, caso contrário acontece no processo "*Desbloquear Lançamento Financeiro"*.

* **Efetivar Aditivo de Renegociação de Contrato.**  
  Os demais aditivos como "Aditivo de Prorrogação de Vencimento", "Aditivo de Alteração de Vencimento", "Aditivo de Alteração de Valor" e "Troca de Comprador" devem atualizar o boleto e o código de barras ao efetivar, mas não há necessidade da criação de um novo boleto.

*Caso o aditivo altere algum dado que impacte no boleto, e o lançamento estiver Remetido a Banco, o sistema apresenta erro e não permite alteração. Para que o cliente possa criar um aditivo para o lançamentos financeiros remetidos a banco deverá acessar o modulo financeiro, cancelar o lançamento na remessa manualmente.*

*A geração do boleto usará os serviços do TOTVS Gestão Financeira que permitem a Inclusão e alteração de Boleto bem como a geração do Código de Barras.*

## Anexo Boleto

Será disponibilizado como anexo a visão de Venda TIN, a opção de "Boleto", que deve filtrar apenas os boletos relacionados ao registro selecionado, ou seja, associados aos lançamentos financeiros da venda. 

* Para Alterar data de vencimento do Boleto, deve ser usado o processo anexo ao boleto.

* A impressão dos boletos, deve ser feita pela visão de boletos (na venda ou no financeiro), bem como envio por e-mail.

## Geração Manual de Boleto

Além da geração automática será possível gerar o boleto manualmente através da visão de Boletos na Venda da Venda TIN via processo anexo ou na visão anexa de lançamentos Financeiros.

*O Código de Barras não será gerado automaticamente através desta opção e o usuário poderá criá-lo na visão de boleto anexa a lista de Venda TIN ou através do módulo Financeiro.*

# Agrupamento de Boleto ou Método de Inclusão de Boleto

Se o parâmetro para Gerar Boleto automaticamente estiver marcado o usuário deverá informar qual será o Método de Inclusão de boleto (agrupamento): (a partir da versão 12.1.14)

* **Um Boleto para cada Lançamento:**Esta opção permite que seja gerado um boleto para cada Lançamento Financeiro relacionado a venda.
* **Um Boleto para cada Cliente/Fornecedor e Data de vencimento**:Esta opção permite que sejam agrupados vários Lançamentos a receber do mesmo Cliente/Fornecedor  e mesma data de vencimento, mesmo que de Vendas **diferentes** em um único boleto. A data de vencimento do Boleto será a mesma data de vencimento dos Lançamentos selecionados. Neste caso, o valor do boleto(agrupado por Cliente/Fornecedor e data) será a soma dos valores líquidos dos Lançamentos na data do vencimento.
* **Um Boleto para cada Cliente/Fornecedor,  Data de vencimento e Venda**: Esta opção permite que sejam agrupados vários Lançamentos a receber do mesmo Cliente/Fornecedor,mesma data de vencimento e mesma venda em um único boleto. Neste caso aplica-se vendas que tenham mais de um componente gerador de parcela, onde alguns como sinal e mensal tem o mesmo vencimento e outros como balão e anual tem outro vencimento. A data de vencimento do Boleto será a mesma data de vencimento dos Lançamentos selecionados. Neste caso, o valor do boleto(agrupado por Cliente/Fornecedor e data) será a soma dos valores líquidos dos Lançamentos na data do vencimento.

**Atenção:**não serão disponibilizadas a opções "Um Boleto para cada Cliente/Fornecedor" e "Um Boleto para cada Cliente/Fornecedor e Venda", ou qualquer outra combinação com vencimento diferentes, pois o calculo de juros e multa é afetado, podendo gerar inconsistências.

 Este parâmetro só se aplica a geração automática de boleto da Venda TIN, pois para a geração manual será aplicado o método escolhido pelo usuário.

 Em virtude da alteração financeira para atender a determinação da [FEBRABAN](https://www.febraban.org.br/Acervo1.asp?id_texto=2660&id_pagina=85&palavra=)foi criado um novo tipo de registro de boleto, o On line que será liberado pelos bancos em substituição a geração dos boletos não registrados web, o agrupamento de boletos objeto desta especificação não poderá levar em consideração a existência de boletos de registro on line, pois estes serão de uso exclusivo do Portal TIN e não deve receber agrupamento vindo dos processos *winform*.

*Especificação Técnica para Agrupamento de Boleto liberado na versão 12.1.15 [ER\_CPTIN001-255\_Agrupamento\_de\_Boleto\_Automatico](http://tdn.totvs.com/display/LRM/ER_CPTIN001-255_Agrupamento_de_Boleto_Automatico)*

## Permissões

Serão criadas permissões especificas para:

* Acesso ao flag de "Gerar boleto automático" nos processos em que a opção for disponibilizada.

# Contra escopo

 Recurso disponível apenas na versão de Revitalização;

 Não será possível gerar boleto para os lançamentos do módulo de Locação;

 Não será possível gerar boleto para os lançamentos integrados com o Protheus.

*Mais informações sobre a geração de boleto financeiro acesse o link <http://wikihelp.totvs.com.br:1210/WikiHelp/FIN/FIN.Boleto.aspx>*
