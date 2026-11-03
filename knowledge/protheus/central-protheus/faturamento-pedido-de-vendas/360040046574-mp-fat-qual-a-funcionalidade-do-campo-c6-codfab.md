---
article_id: 360040046574
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 7fb45f4c709d3e0e4d82e3d9035e60df8508573406ad81cc6b1306cba4adb8a4
fetched_at: '2026-06-28T22:38:41.312079+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: MP-FAT-Qual a funcionalidade do campo C6_CODFAB
type: support-article
updated_at: '2021-04-28T15:50:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040046574-MP-FAT-Qual-a-funcionalidade-do-campo-C6-CODFAB
---

**Dúvida**Qual a funcionalidade do campo **C6\_CODFAB**?  
   
 **Ambiente**

Microsiga Protheus - todas as versões.  
  
**Solução**

O campo **C6\_CODFAB** está relacionado ao campo **AA3\_CODFAB** (base de atendimento) do Gestão de Serviços, é utilizado na integração dos Módulos Gestão de Serviços com o Faturamento,na  rotina de Base de atendimento ( **TECA040** ) para registros de equipamentos/itens/produtos.  
  
Serve  para informar quem é o fabricante das peças/equipamento/produto usado em um serviço, locação e entre outros tipos de contratos que faz uso dos equipamentos/produtos/peças do Gestão de Serviços, e que geram pedido de venda após a efetivação da Ordem de Serviço.  
  
Assim ao registrar um contrato, ou pedido de venda que por sua vez irão conter peças/equipamentos/produtos saberemos quem é o fabricante das mesmas!  
  
Esses dados ficam no cadastro do cliente ( **MATA030** ) contendo todos os dados do fabricante.  
  
Maiores detalhes sobre base de atendimento, segue boletim que fala sobre a rotina ( TECA040 ):[http://tdn.totvs.com.br/pages/releaseview.action?pageId=239018487#BasesdeAtendimento-TECA040-GestãodeServiços-P12-Objetivo](http://tdn.totvs.com.br/pages/releaseview.action?pageId=239018487#BasesdeAtendimento-TECA040-Gest%C3%A3odeServi%C3%A7os-P12-Objetivo)
