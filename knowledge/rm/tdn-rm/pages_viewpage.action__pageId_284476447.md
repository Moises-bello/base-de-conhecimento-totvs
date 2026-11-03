---
content_hash: 7c9540891e3ee63a6e428ca672c5dd3029e6a642dfdc9a393f0b2ec7b4215762
fetched_at: '2026-06-29T00:08:36.820646+00:00'
page_id: '284476447'
product: rm
source: tdn-rm
title: DT_Período de Apuração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284476447
version: 4
---

|  |  |
| --- | --- |
| Descrição | Período de Apuração |
| Observações | Neste cadastro são montadas as definições referentes ao período de movimentação que será enviado para o eSocial.  O período de apuração é a competência da movimentação que será enviada ao eSocial. |

A seguir demonstramos como criar um o Período de Apuração.

1. Para criar o Período de Apuração acesse: TOTVS Folha de Pagamento| eSocial (beta)| Período de Apuração

Nessa tela encontraremos os campos:

**Competência**: Informe a Competência (mês e ano) da movimentação que será enviada ao eSocial.

**Indicativo de período de apuração**:

* Mensal: Movimentação da Folha Normal.
* Anual: Somente para o 13 Salário.

**Responsável**: Informações do responsável pelo envio de eSocial.

**Atenção:  
Alguns campos podem estar desabilitados nesse cadastro, pois dependem de regras específicas definidas no leiaute do eSocial:**

**Indicativo de Substituição**: Válido apenas para  empresa enquadrada nos artigos 7 a 9 da Lei 12.546/2011, conforme classificação tributária indicada no evento de [Informações do Empregador.](http://fwrm-wiki:9999/WikiHelp/FOP/FOP.Informa%C3%A7aoEmpregador.aspx)

**Percentual de Redução:** Será definido como 0 se o Indicativo de Substituição for "Integralmente Substituída", senão o campo estará habilitado para que seja informado o percentual correspondente à razão entre a receita de atividades não relacionadas nos artigos 7 e 8 da Lei 12.546/2011 e a receita bruta total.

**Fator Mês e Fator 13º Salário nas Atividades Concomitantes**: Somente será habilitado se nas [Informações do Empregador](http://fwrm-wiki:9999/WikiHelp/FOP/FOP.Informa%C3%A7aoEmpregador.aspx), a Classificação Tributária for "03 - Empresas enquadradas no regime de tributação Simples com tributação previdenciária substituída e não substituída".

**Houve repasse para Sócios no Ano Anterior**: Habilitado para preenchimento exclusivamente no período de apuração relativo ao mês de Janeiro de cada ano.

**Informações Complementares para apuração da Alíquotas de RAT/FAP:**Informe se o FAP é definido por empresa ou por estabelecimento.

Eventos que utilizam os dados destes cadastro como base para geração das informações:

Eventos Periódicos: [S-1200](http://fwrm-wiki:9999/WikiHelp/FOP/FOP.S1200.aspx), [S-1210](http://fwrm-wiki:9999/WikiHelp/FOP/FOP.S1210.aspx), [S-1280](http://fwrm-wiki:9999/WikiHelp/FOP/FOP.S1280.aspx), [S-1298](http://fwrm-wiki:9999/WikiHelp/FOP/FOP.S1298.aspx), [S-1299](http://fwrm-wiki:9999/WikiHelp/FOP/FOP.S1299.aspx) e [S-1300](http://fwrm-wiki:9999/WikiHelp/FOP/FOP.S1300.aspx).

   2. Eventos da Folha e Social:  Nesta Aba é possível visualizar os eventos periódicos gerados para os empregados.

Eventos que serão visualizados:

###### [S-1200 - Remuneração do Trabalhador](http://fwrm-wiki:9999/WikiHelp/FOP/FOP.S1200.aspx) [S-1210 - Pagamentos de Rendimentos do Trabalho](http://fwrm-wiki:9999/WikiHelp/FOP/FOP.S1210.aspx) [S-1280 - Informações Complementares aos Eventos Periódicos](http://fwrm-wiki:9999/WikiHelp/FOP/FOP.S1280.aspx) [S-1298 - Reabertura dos Eventos Periódicos](http://fwrm-wiki:9999/WikiHelp/FOP/FOP.S1298.aspx) [S-1299 - Fechamento dos Eventos Periódicos](http://fwrm-wiki:9999/WikiHelp/FOP/FOP.S1299.aspx) [S-1300 - Contribuição Sindical Patronal](http://fwrm-wiki:9999/WikiHelp/FOP/FOP.S1300.aspx)

Lembrando que é possível filtrar por cada evento, conforme demonstrado na imagem acima, ou visualizar todos. Além de ser possível, Gerar o XML, Abrir o XML gerado e Integrar com o TAF ( TOTVS Automação Fiscal.

Através da mesma tela, poderemos consultar o status dos eventos, o Tipo de operação e o Ticket TAF ( protocolo de integração TOTVS Folha de Pagamento X TAF).
