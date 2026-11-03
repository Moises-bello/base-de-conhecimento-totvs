---
article_id: 34605029826455
category: Escrita Fiscal - Configurador de Tributos
content_hash: eea289c3b805600ee0b022d510db24ad8e641fca8a0af69fda9d06a9428c2c79
fetched_at: '2026-06-28T22:39:17.324673+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Como calcular
  IPI no Configurador de Tributos?
type: support-article
updated_at: '2025-11-03T17:41:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34605029826455-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-IPI-no-Configurador-de-Tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34605026859159) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como calcular IPI no Configurador de Tributos?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

* **Cadastro do Produto**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34605026861463)

* **Tributo do IPI**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34607152668183)

* **Perfil do Produto**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34607100299159)

* P**erfil de Operação**

Esse perfil já traz uma listagem de cadastros ao realizar o primeiro acesso na rotina.   
A empresa pode selecionar um perfil já existente ou criar um novo.

**Importante:** o perfil de operação deve contar o mesmo CFOP que esta cadastrado no TES. Caso o TES não seja o mesmo, o calculo não é será apresentado no documento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34607152670231)

* **Perfil de Participante**

Vincule o cliente ou fornecedor que será utilizado na operação, conforme exemplo abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34607100300951)

* **Regra de Base de Calculo**

Configure conforme o valor que espera que seja considerado como base o IPI, por exemplo: Valor da Mercadoria

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34607152671895)

* **Regra de Alíquota**

A empresa pode cadastrar a alíquota por meio da Regra de Alíquota conforme demonstrado abaixo ou cadastrar na regra de ncm > aba alíquota por tributo (https://tdn.totvs.com/display/public/PROT/CFGTRIB+-+Configurador+de+Tributos#CFGTRIBConfiguradordeTributos-CadastrodeRegrasporNCM)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34607152672663)

* **Regra de Escrituração**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34607152674199)

* **Regra de Calculo - Documento Fiscal**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34607100305303)

Para que o valor seja levado para a coluna Outros na aba de Detalhamento da Formula de Calculo aba Outros  deve editar a formula para que o valor seja levado corretamente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34607100306583)

* **TES - Tipo de Entrada e Saida**

CFOP: 5102

O calculo do configurador de tributos sobrepõe o TES mesmo que os campos estejam habilitados para calcular o devido imposto.

* Pedido de Venda

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34607100307607)

Gravação das tabelas CD2/SF3/SFT de acordo com a configuração.

Dessa forma será gravada corretamente no campo Outros de acordo com a configuração.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34607100310167)

Materiais para apoio:

[CFGTRIB - Configurador de Tributos - P12](https://tdn.totvs.com/display/PROT/CFGTRIB+-+Configurador+de+Tributos+-+P12)

[CFGTRIB - Cálculos no Configurador de Tributos](https://tdn.totvs.com/pages/viewpage.action?pageId=676039354)
