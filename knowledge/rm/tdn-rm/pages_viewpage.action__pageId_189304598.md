---
content_hash: a43e18874cd4a555f48203ebc1cd3baf21d540c1106562716da0f7f9c4cda5eb
fetched_at: '2026-06-29T00:05:58.838824+00:00'
page_id: '189304598'
product: rm
source: tdn-rm
title: RMFIS00002_11.002 - Apuração do Lucro Real
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=189304598
version: 7
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                      **Versão:**11.82.38/12.1.4 |
| **Processo** | **:** | ECF - Escrituração Contábil Fiscal |
| **Subprocesso** | **:** | Apuração de Tributos IRPJ e CSLL |
| **Data da publicação** | **:** | 26/05/2015 |

O objetivo deste documento é oferecer orientações sobre apuração do tributo IRPJ/CSLL no **Lucro Real**. Como regras gerais, o Lucro Real é a sistemática de apuração da base de cálculo do IR, que considera os registros contábeis e fiscais efetuados de acordo com as leis comerciais/fiscais. O lucro real é o lucro contábil depois de considerados os ajustes de adições, exclusões e compensações prescritas e autorizadas pela legislação fiscal.

**Importante:** Para geração da rotina ECF, os Clientes que realizavam a apuração do IRPJ/CSLL através do TOTVS Gestão Fiscal no período anterior da rotina, será necessário reabrir todos os períodos de apuração dos tributos e encerra-los novamente para atualização dos dados conforme parametrização específica da rotina ECF. Para Clientes que não apuram o IRPJ/CSLL através do aplicativo, será necessário realizar essa apuração através do sistema TOTVS Gestão Fiscal para correta geração da rotina ECF.

***Parametrização Necessária***

---

Inclua um Evento Tributário. Acesse o menu: **Obrigações Principais | Eventos Tributários -> Estrutura**. Insira um novo Evento/registro. Informe o **Código**,  a **Descrição**, o **Tributo** e a **Forma** **de Tributação** (Campos obrigatórios). No exemplo abaixo será utilizado o Tributo IRPJ com periodicidade **Trimestral**. O sistema consiste a periodicidade informada no cadastro do tributo para apuração do imposto.

Na aba de **Regras Tributárias** será possível parametrizar:

* + Resultado Contábil
  + Adições do Lucro
  + Adições por doação
  + Exclusões do Lucro
  + Compensação de Prejuízo
  + Deduções do Tributo
  + Compensações do Tributo

Resultado Contábil:

No campo *Demonstração Contábil* o usuário deve informar o registro previamente cadastrado. Para demais orientações deste cadastro acesse o artigo publicado no [TDN](http://tdn.totvs.com/pages/releaseview.action?pageId=187534222). Já no campo *Código da Tabela Dinâmica do Registro ECF*,  o usuário deve informar o código correspondente. Documentação de auxílio da Importação das Tabelas Dinâmicas, clique [aqui](http://tdn.totvs.com/pages/releaseview.action?pageId=187831106).

Informe o *Fato Contábil do Resultado Operacional* e *Resultado Não Operacional*. Informe as contas nas abas correspondentes (**Regras Tributárias**): Adições do Lucro, Adições por doação, Exclusões do Lucro, Compensação de Prejuízo, Deduções do Tributo e Compensações do Tributo.

Cálculo da Apuração Lucro Real:

**Regras Tributárias**

Para informar a conta correspondente ao Lucro, Adições, Prejuizo(...),  será aberto a janela de Regras tributárias onde o usuário deverá preencher a origem da informação, código da Tabela Dinâmica ECF, Operação e a Conta Contábil com o tipo da conta correspondente (Débito ou Crédito).

**Vigência do Evento Tributário**

No cadastro, o usuário deverá incluir um período de Vigência para vincular ao Evento Tributário previamente cadastrado. Acesse: **Obrigações Principais | Eventos Tributários -> Vigência:**

O cadastro de Vigência determinará o período válido para a *Regra Tributária* cadastrada no Evento. Selecione o Evento Tributário e informe a Data Inicial e Final de vigência.

**Período de Apuração**

O usuário deverá inserir o período de apuração conforme periodicidade cadastrada no Tributo. No exemplo abaixo foram incluídos períodos trimestrais para o tributo IRPJ

Ao encerrar o período de apuração o sistema irá calcular automaticamente o saldo *Credor/Devedor* do imposto. Para geração da guia o usuário deverá selecionar o registro de apuração e acessar o menu: **Processos | Geração de Guias Automaticamente.**

**As parametrizações desse documento será válida para os tributos IRPJ e CSLL, no regime do Lucro Real. Para os regimes Lucro Presumido/Arbitrado, Imunidade/Isenção, Lucro Real Estimativa, a única alteração é a forma como o imposto será calculado. O Cálculo e outras informações sobre a apuração acesse os links:  [Lucro Real](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.EventoLucroReal.aspx), [Lucro Presumido/Arbitrado](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.EventoLucroPresumidoArbitrado.aspx), [Imunidade/Isenção](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.EventoImuneIsenta.aspx) e [Lucro Real Estimativa](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.EventoLucroRealEstimativa.aspx).**

**Para mais instruções sobre o processo de apuração pelos Eventos Tributários, acesse este [artigo](http://tdn.totvs.com/pages/viewpage.action?pageId=84541593).**

Para mais informações:

 [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)

**COMUNIDADE **[R@Fiscal](http://fluig.totvs.com/portal/p/10097/subject/rfiscal)****

**Canais de Atendimento:**

**Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
