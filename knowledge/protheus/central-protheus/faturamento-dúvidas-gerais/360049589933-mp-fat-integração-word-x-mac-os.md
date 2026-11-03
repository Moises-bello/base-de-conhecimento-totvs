---
article_id: 360049589933
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: b1a338cbcfe272306f53b827a0b4a86b88b0d6de068b672d34047a2f4b59143d
fetched_at: '2026-06-28T22:38:31.232715+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT-Integração Word x Mac Os
type: support-article
updated_at: '2021-04-28T15:53:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049589933-MP-FAT-Integra%C3%A7%C3%A3o-Word-x-Mac-Os
---

**Dúvida**

Ocorre um erro na impressão da proposta comercial(**Fata600**) com integração Word em um terminal onde se utiliza o sistema operacional MAC OS. O programa é compatível na utilização com sistema operacional Mac OS ou somente sistema operacional Windows?

**Ambiente**

Microsiga Protheus - desde a versão 11.  
  
**Solução**

O componente utilizado internamente pelo Binário para integração Office é "Component Object Model(COM)" e pertence à Microsoft conforme pode ver nesta documentação: **<https://pt.wikipedia.org/wiki/Component_Object_Model>** .   
  
Com isso não há suporte ao Mac OS(apple) , não sendo compatível a impressão de propostas com integração word para o Mac OS.   
  
Para realizar da impressão em uma máquina  Mac Os, será necessário instalar o Windows em uma máquina virtual e realizar a impressão por ela.  Esse processo é de responsabilidade do cliente, a Totvs não auxilia na criação da máquina virtual, neste caso, verifique com o TI da empresa, o processo necessário para efetuar a instalação.

Para mais informações obre configuração de impressão da proposta comercial por integração Word, acesse:**[FAT0081\_Configuração\_de\_Integração\_Word\_na\_Oportunidade Vendas \_<Int Word>](https://tdn.totvs.com/pages/viewpage.action?pageId=239035266)**
