---
content_hash: f06fdff2920a22985fb48e8636ef7b67f999087bdea6bbe98c19dce5e7af8a25
fetched_at: '2026-06-29T00:09:49.224088+00:00'
page_id: '435105256'
product: rm
source: tdn-rm
title: Portal do Cliente - PDC - Relatórios (Comprador)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105256
version: 24
---

**Descrição**  
Disponibiliza as opções de relatórios para o comprador, através do Portal do Cliente.

No menu "Relatórios", será visível os relatórios conforme permissões do usuário logado.   
Nesta opção, será exibido o campo "Unidade", onde o usuário irá selecionar para qual unidade deseja gerar os relatórios e irá exibir a listagem com os relatórios disponíveis, conforme permissão de segurança do usuário logado.

As opções de relatório possíveis são:

* **Ficha financeira:** O Relatório de Ficha Financeira é um relatório fixo, já disponível no sistema através do Totvs Incorporação, e ficará disponível também no Portal do Cliente, exibindo as informações referentes à venda do cliente, de acordo com a unidade selecionada.   
  Para ser gerado, é necessário que esteja configurado em **"Ambiente > Parâmetros > Totvs Incorporação > Portal do Cliente > Relatórios"** qual o modelo que deverá ser considerado para a geração do relatório.   
  Caso não esteja configurado, será exibida a mensagem para o usuário, informando a impossibilidade da geração e a necessidade de entrar em contato com a administração do portal.

Parâmetro liberado da versão 31 em diante. Ficha Financeira com Deságio no PORTAL e APP.

A Ficha Financeira pode ter o cálculo do deságio ou não. Se o parâmetro estiver habilitado, a ficha financeira parametrizada para ser utilizada no PDC e no App deverá apresentar os cálculos com deságio.

Parâmetros | Gestão de Imóveis | Portal do Cliente.

Marcar o parâmetro novo : Considerar deságio ao gerar Ficha Financeira no Portal e no APP.

**Informe de pagamentos:** O Relatório de Informe de Pagamentos é um relatório fixo, já disponível no sistema através do Totvs Incorporação, e ficará disponível também no Portal do Cliente, exibindo as informações de pagamentos referentes à venda do cliente de acordo com a unidade selecionada.

* O usuário deverá selecionar qual o ano desejado do Informe de Pagamentos. Por default o sistema trará selecionado o ano anterior e as opções se limitam ao período de 5 anos.   
  Para ser gerado, é necessário que esteja configurado em **"Ambiente > Parâmetros > Totvs Incorporação > Portal do Cliente > Relatórios"** qual o modelo que deverá ser considerado para a geração do relatório.   
  Caso não esteja configurado, será exibida a mensagem para o usuário informando a impossibilidade da geração e a necessidade de entrar em contato com a administração do portal.

Importante!

Os valores serão impressos no relatório atendendo as seguintes regras:

* A data de entrada do comprador na venda. A data de entrada é determinante para a impressão das parcelas pagas sobre a responsabilidade do comprador no informe de rendimentos.
* Comprador tem participação no contrato.
* Comprador está no período da baixa.

* **Relatórios do cliente:**Serão exibidos também os relatórios do cliente que estiverem configurados para serem disponibilizados no Portal do Cliente, através da opção **"Relatórios > Gerenciamento de Relatório Web"**.   
  Para estes relatórios, o cliente poderá elaborar seus próprios layouts e se valer dos seguintes campos para serem utilizados como filtros:
  + Número da Coligada: CODCOLIGADA;
  + Número da coligada do Cliente / Fornecedor: CODCOLCFO;
  + Código do Cliente / Fornecedor: CODCFO;
  + Número do Contrato: NUM\_CONT;
  + Código do Empreendimento: COD\_PESS\_EMPR;
  + Número da Unidade: NUM\_UNID;
  + Número da Subunidade: NUM\_SUB\_UNID;
  + Código da Modalidade de venda: COD\_MOD\_VENDA.

O sistema também passa a exibir, a partir da versão **12.1.27**, os relatórios de aluguel. Para isso, o usuário deverá selecionar o seu contrato de aluguel no botão **Alterar Empreendimento / Contrato.**  
Da mesma forma, o gestor do PDC poderá elaborar seus próprios relatórios de aluguel, se valendo dos campos abaixo para serem utilizados como filtros:

* Coligada do contrato de locação: CODCOLIGADA
* Numero do contrato de locação: NUM\_CONT
* Código do contrato de locação: COD\_CONT
* Coligada do cliente/fornecedor locatário: CODCOLCFO
* Código do cliente/fornecedor locatário: CODCFO
* Identificador do locatário: ID\_LOCATARIO

Atenção

Quando o PDC é acessado através de um **dispositivo móvel** (smartphone, tablet, etc), ao solicitar a geração de um Relatório, o sistema irá gerá-lo diretamente no RM, respeitando a fila de jobs e somente após a finalização da geração do mesmo, é que o botão para **fazer o download do PDF** desse relatório será habilitado.

Portanto, essa ação irá depender do tempo necessário para que o ambiente RM gere este relatório, para disponibilizá-lo para download ao Usuário.

Importante

No contexto do contrato de aluguel, somente serão apresentados os relatórios que estão configurados através da opção **"Relatórios > Gerenciamento de Relatório Web",** e que possuírem o tipo (Tabela RRPTREPORT, coluna TIPO) listado abaixo:

* Relatório de Contrato de Locação -> 1000;
* Relatório de Contrato de Administração -> 1001;
* Relatório de Rescisão de Contrato Locação -> 1016;
* Relatório de Pendencias para Rescisão -> 1017;
* Relatório de Lançamentos Mensais -> 1020
NOVO PDC

Este novo Portal de Atendimento ao Cliente encontra-se disponível na versão 12.1.2502 em diante.

 Recursos Adicionais

---

**Atalho para relatórios na tela de Situação Financeira:**  
Para facilitar o acesso do usuário, os relatórios Ficha Financeira e Informe de Pagamentos possuirá um atalho a partir da tela de Situação Financeira, onde serão consideradas as mesmas regras que da tela de Relatórios do Portal. A única diferença é que, para o relatório de Informe de Pagamentos, será considerado sempre a data do ano anterior.

Veja Também

---

* Relatórios Empreendimentos
