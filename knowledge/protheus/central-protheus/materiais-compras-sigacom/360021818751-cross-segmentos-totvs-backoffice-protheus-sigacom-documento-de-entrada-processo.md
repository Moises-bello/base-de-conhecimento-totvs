---
article_id: 360021818751
category: Materiais - Compras (SIGACOM)
content_hash: f07fbdd0f99ca8a82ddb0da17e8b3e397b9ee5c4cd5e7ad50d84a04297190877
fetched_at: '2026-06-28T22:41:08.801494+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Documento de Entrada
  - Processo de Compra com Entrega Futura (tabela DHQ)
type: support-article
updated_at: '2025-09-26T13:59:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021818751-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Documento-de-Entrada-Processo-de-Compra-com-Entrega-Futura-tabela-DHQ
---

**Dúvida**Documento de Entrada - Processo de Compra com Entrega Futura (tabela DHQ)  
  
**Ambiente**Protheus – Compras – A partir da versão 12.1.17  
  
  
**Solução**Compra com entrega futura é a venda de mercadoria já produzida ou adquirida pelo fornecedor, mas que, por conveniência ou interesse do comprador, continuará em poder do fornecedor (este se transformando em mero depositário da mercadoria vendida) até que a entrega ocorra ao cliente, em um segundo momento, conforme critérios definidos na negociação entre fornecedor e cliente.  
  
O processo de compra com entrega futura ocorrerá basicamente da seguinte forma:  
  
**Passo 1:**   
Inclusão da nota fiscal de entrada de simples faturamento utilizando TES específica.  
Esta TES deve estar configurada como Atualiza Estoque = Não e Gera Duplicata = Sim e o campo relativo à compra futura **(F4\_EFUTUR) = 1-Recebimento da Compra com Entrega Futura.**  
Esta nota irá atualizar a tabela de controle **DHQ** criando o saldo a entregar para o produto em questão.  
Esta nota fiscal pode ou não estar vinculada a um pedido de compras. Caso seja incluído um pedido de compras utilizando a TES de recebimento da compra com entrega futura, este pedido irá atualizar o campo **B2\_SALPEDI** (mesmo que a TES não atualiza estoque). Este saldo previsto será efetivado quando da inclusão da segunda nota abaixo.  
  
**Passo 2:**   
Inclusão de nota fiscal de entrada de remessa de mercadoria utilizando TES específica.  
Esta TES deve estar configurada como **Atualiza Estoque = Sim** e **Gera Duplicata = Não** e o campo relativo à compra futura **(F4\_EFUTUR) = 2-Recebimento da Entrega da Compra com Ent. Futura.**  
Esta nota deverá obrigatoriamente ser vinculada à nota de origem, de simples faturamento e irá atualizar a tabela de controle **DHQ** criando os registros de entrega do produto em questão, atualizando a quantidade recebida, a quantidade original e o saldo em estoque do produto.

Na inclusão da nota de simples remessa, o sistema não carregará as informações de quantidade e valor, quando há o vínculo da nota de simples faturamento e nem gravará nos campos de origem, nota, serie e item, as informações referentes a nota de simples faturamento.

As informações de quantidade e valor não são carregados automaticamente, pois devem ser informados no momento da inclusão, baseado no que está sendo recebido.

Os campos de origem da SD1 não são gravados na tabela SD1, pois os vínculos são gerados na tabela DHQ.

Através do relatório gerencial COMR103 é possível acompanhar o processo de compra futura.

**DICA:** Aprenda também como gerar Processo de compra com Entrega Futura utilizando o conceito de entrega por terceiros (COMA001) [clicando aqui!](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004980311-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Processo-de-Entrega-Por-Terceiros?source=search)

**O que fazer quando não encontrar a nota fiscal origem (simples faturamento) para vincular na nota fiscal de remessa?**

- Validar as configurações de TES se estão corretas conforme mostrado acima

- Filtrar o documento da entrada na tabela **DHQ**, buscar pelo número da nota de simples faturamento e verificar se no campo **DHQ\_QTREC** se há saldo a ser recebido. Caso esteja preenchido com a quantidade original **DHQ\_QTORI** significa que não há mais saldo desse simples faturamento a ser recebido.

Caso ainda haja saldo, será necessário avaliação do por quê o sistema não está conseguindo localizar a nota de simples faturamento para efetuar o vínculo.

**IMPORTANTE :**

Para o processo de compra com entrega futura, temos disponibilizado no padrão o relatório **COMR103.**

**No menu do módulo de compras : Relatórios -> Documento de Entrada -> Compra com Entrega Futura.**

Em seus parâmetros, esse relatório possui as perguntas data inicial e data final :

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21563271358359)

**Porém, esse relatório referente as entregas futuras, não possui a funcionalidade para retroagir a posição do documento, de acordo com a data preenchida no parâmetro. Portanto, mesmo que, por exemplo,  a data final seja especificada como 31/12/2023, pois a nota de simples faturamento foi incluída nesse mês, e a nota de remessa tenha sido feita em 01/01/2024, o documento já está considerado encerrado. Logo com a pergunta Situação = Aberto, e a data do sistema em que o relatório estiver sendo emitido, por exemplo for 01/02/2024, o processo não será listado, pois ele já se encontra encerrado. Esse processo só será listado se for utilizada a situação : Todos ou Encerrados.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/21563287606807)**

***Saiba mais:***

***[Processo de Devolução de Entrega Futura](https://tdn.totvs.com/pages/viewpage.action?pageId=880054694)***

[Nf de complemento de preços no processo de compra com entrega futura](https://tdn.totvs.com/pages/releaseview.action?pageId=369628339)

[Detalhes do Processo de Compra com Entrega Futura](http://tdn.totvs.com.br/pages/releaseview.action?pageId=394211362)

[MATA103 Execauto para o processo de compra com entrega futura](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23234373176983-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Rotina-Autom%C3%A1tica-MATA103-Documento-Entrega-Futura?source=search)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
