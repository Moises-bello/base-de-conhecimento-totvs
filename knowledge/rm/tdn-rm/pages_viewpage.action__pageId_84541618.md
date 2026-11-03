---
content_hash: 5245f42554f0a4ec19abf447789be6ce963cee98dec067b502616c6e6f4dbe4c
fetched_at: '2026-06-29T00:11:50.843330+00:00'
page_id: '84541618'
product: rm
source: tdn-rm
title: Apuração tributo RET
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=84541618
version: 2
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                       **Versão:**11.52 |
| **Processo** | **:** | Apuração de Tributos |
| **Subprocesso** | **:** | Geração de Guia Automática para o tributo RET (Regime Especial de Tributação) |
| **Data da publicação** | **:** | 12/09/2013 |

***Definição do Processo***

O objetivo deste documento é oferecer uma visão geral a respeito das implementações realizadas no TOTVS Gestão Fiscal para a geração da guia automática do Tributo RET.

***Regras Gerais***

O sistema de Gestão Fiscal foi alterado para tratar a apuração da RET conforme Instrução Normativa RFB nº 934, de 27 de abril de 2009, bem como a geração dos dados na DCTF.

Dispõe sobre o regime especial de tributação aplicável às incorporações imobiliárias e sobre o pagamento unificado de tributos aplicável às construções de unidades habitacionais contratadas no âmbito do Programa Minha Casa, Minha Vida.

***Parametrização Necessária***

**1.****Cadastro do Tributo**

Para apuração da RET deverá ser criado um novo tributo, mensal, referente à RET e associado ao novo Tipo Tributo denominado “RET”

**2.****Evento Tributário**

A apuração será realizada através de Evento Tributário, desta forma, deverá ser criado um evento tributário para o tributo RET. Em “Regras tributárias” a regra deverá ser igual à forma de tributação “Outros”.

**3. Vigência Evento Tributário**

Incluir uma vigência e vincular o evento tributário.

***Como fazer a geração a rotina***

Criar um período de apuração do tributo RET, ao encerrar o período o sistema calcula o Saldo Credor/Devedor do tributo conforme simulação do evento tributário.

No menu Processos realizar a Geração automática das Guias referentes para pagamento equivalente da receita mensal recebida. O Código da Receita será informado pelo usuário.

**Para maiores informações:**

[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)

**COMUNIDADE **[R@Fiscal](https://totvs.byyou.com/?space=rfiscal)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
