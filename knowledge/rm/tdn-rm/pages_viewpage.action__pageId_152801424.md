---
content_hash: 454abc0cb1d4a000035bdd5953a2fd2e466d3d3d76b4f62f9c3c7ad728d7e0b2
fetched_at: '2026-06-29T00:05:56.584661+00:00'
page_id: '152801424'
product: rm
source: tdn-rm
title: Apuração de Tributos  - Tributos Retidos (PISRF, COFINSRF e CSRF)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=152801424
version: 3
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                      **Versão:** 11.82.3X |
| **Processo** | **:** | Apuração de Tributos |
| **Subprocesso** | **:** | Tributos Retidos (PISRF, COFINSRF e CSRF) |
| **Data da publicação** | **:** | 19/08/2014 |

Os **tributos retidos** são apurados pelo período de apuração no RM Liber, desde que haja lançamentos financeiros, no RM Fluxus, que contenham os tributos **RF** (**retidos**) com código da receita, base, alíquota e valor destacados.

**Obs.: O fato gerador das Contribuições Sociais retidas é a data da baixa do lançamento original, ou seja, a baixa deve estar dentro do período selecionado/encerrado**.

Realize a geração de guias à partir de Lançamentos Financeiros, através dos processos do período. Lembrando que o mesmo deve estar encerrado.

Será exibido uma tela para ser repassado os dados da fatura. Após, execute o processo.

É gerado uma guia DARF e automaticamente, o vencimento da fatura, é integrado com o RM Fluxus.

**ATENÇÃO**:

Caso sistema exiba uma mensagem de inconsistência, ao executar o processo de Geração de Guias à partir de Lançamentos Financeiros, segue abaixo as possíveis causas:

 

**Verifique:**

* Se já tenha sido executado o processo e as guias já foram geradas.

 

* Se a data da baixa do lançamento financeiro com este tributo está condizente com o período de apuração selecionado/encerrado.

 

* Se existe integração entre os sistemas está definida.  **Acesse: Ambiente | Parâmetros -> Integração de Sistemas - RM Liber <-> RM Fluxus e RM Fluxus <-> RM Liber**. Ambos os *flags* **Integração** e **Aplicar para todas as Coligadas**, devem estar marcados.

* Se o parâmetro de **Integração Fiscal**, está definido. **Ambiente | Parâmetros -> TOTVS Gestão Financeira ->****02.01. - Contas a Pagar****-> Etapa 25 -**

* Se os Lançamentos Financeiros estão com o tributo retido devidamente destacado.

 

Para maiores informações:

 [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ApuracaoTribuosRetidos.aspx)

**COMUNIDADE **[R@Fiscal](https://totvs.byyou.com/?space=rfiscal)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
