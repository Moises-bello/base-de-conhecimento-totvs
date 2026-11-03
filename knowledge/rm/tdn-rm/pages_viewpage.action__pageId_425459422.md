---
content_hash: 96d3c57a59aef86a0474e9ea7edb0b91d5b359c643da048cb530af2f20ed59d9
fetched_at: '2026-06-29T00:09:35.898044+00:00'
page_id: '425459422'
product: rm
source: tdn-rm
title: TOTVS Incorporação x BackOffice Protheus - Gerar Lançamentos Financeiros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459422
version: 2
---

**TOTVS Incorporação x BackOffice Protheus - Gerar Lançamentos Financeiros**

---

No processo Gerar Lançamentos Financeiros (visão de Contrato de Venda/Aluguéis) no TIN é iniciada uma transação no TOTVS Incorporação e são enviados para o Protheus.

Foi evoluída a integração TIN x Protheus para atender a demanda de realizar a Apuração de resultados (POC) integrado. Foi ajustado no adapter "Financing" (criada a versão 1.002), e nos sistemas TIN e Fluxus para que na geração de lançamentos, sejam enviadas ao Protheus as informações da Conta Gerencial, Item Contábil e Classe de valor, para serem usadas para a Apuração de resultados (POC).

No TIN na tela de Vendas, o processo de Gerar Lançamentos Financeiros cria a mensagem **'Financing'**. A mensagem 'Financing' nada mais é que uma série de informações no formato XML.

Para que a integração funcione perfeitamente, é necessário acessar o TIN, cadastro de Empreendimento, aba Integração, campos Item Contábil e Classe de Valor, preenchendo estes campos com o seu respectivo valor que é criado no Protheus.

Os outros processos que utilizam a geração de lançamentos financeiros no TIN também funcionarão da mesma forma gerando a mensagem.

É possível ver os detalhes da mensagem enviada em Integração / Integração / Mensagem Única / Fila de Mensagens Únicas. Esta tela mostra os campos: Identificador da transação, Uuid mensagem, Versão de Mensagem, Criação da mensagem e Identificador da Integração. Esta tela ainda possui um anexo que mostra as Informações de execução da mensagem.
