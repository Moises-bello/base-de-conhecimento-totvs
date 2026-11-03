---
article_id: 360028699051
category: Escrita Fiscal - CIAP
content_hash: 93d0114850fa0ac4b2d744b26dc3ed02f0c587f4e9956b146717de8c2ca0d2ed
fetched_at: '2026-06-28T22:39:33.824683+00:00'
product: protheus
section_id: 1500001538561
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como deduzir as parcelas
  não utilizadas de CIAP?
type: support-article
updated_at: '2023-10-06T17:02:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028699051-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-deduzir-as-parcelas-n%C3%A3o-utilizadas-de-CIAP
---

**Dúvida**

Como deduzir as parcelas não utilizada de Ciap?

**Ambiente**

Protheus– Livros Fiscais – A partir da versão 11.80

**Importante**

Somente o administrador do sistema deve possuir acesso a esta rotina, que deve ser executada na implantação do processo ou quando houver a necessidade de atualizar o saldo de parcelas do bem (nos casos em que não houveram saídas tributadas em determinado mês para realizar a apropriação), pois efetua a atualização dos campos **Num. Parc.** **(F9\_QTDPARC)** e **Saldo Parc.** **(F9\_SLDPARC)** de acordo com a tabela Estorno dos Créditos (SFA) e do parâmetro **MV\_LC102**, que indica o número de parcelas a serem estornadas para os ativos. Por esse motivo, é necessário que a **tabela Estorno dos Créditos (SFA)** esteja com os lançamentos corretos.

**Solução :**

**1.** No Configurador (SIGACFG), acesse Ambiente/ Cadastros/ Menus, inclua no menu do módulo Livros Fiscais (SIGAFIS) a opção para execução da função Atualiza SF9 (M906SF9), conforme especificação a seguir:

**2.** Execute a opção **Miscelânea/ Acertos/ Atualiza SF9 (M906SF9)**:

**3.** Clique em **Parâmetros.** São apresentadas as seguintes informações:

A atualização da tabela Tipos de Entrada e Saída (SF4) pode ocorrer de duas formas distintas (nas duas opções, a janela apresenta uma breve explicação dos processos que serão executados):

**1 = Parcial**: Indica que somente atualizará os ativos que possuírem o campo **Num. Parc**. (F9\_QTDPARC) zerado (sem valor). Com a seleção dessa opção e confirmação da rotina, se nenhuma alteração for efetuada, é apresentada a mensagem **Nenhuma atualização efetuada**. Clique em **Ok** para prosseguir.

**2 = Geral**: Indica que, independente dos campos possuírem ou não valores inseridos, são recalculados e atualizados conforme tabela Tipos de Entrada e Saída (SF4). Com a seleção desta opção e confirmação e processamento da rotina, é apresentado um relatório resumo para os ativos atualizados.

Se gerada a rotina **ATUALIZA SF9 (M906SF9),** será verificada a quantidade de meses da inclusão do item até a data base e deduzidas deste campo.

Por exemplo:

**ATIVO 001 - CADASTRADO EM 01/12/2019**

**QTD PARCELAS = 48**

**SLD PARCELAS = 48**

Ao rodar rotina ATUALIZA SF9 é aplicada a alteração:

**DATA BASE = 28/02/2020**

**QTD PARCELAS = 48**

**SLD PARCELAS = 45**

Mesmo que não haja apropriação na SFA, será aplicada esta regra, uma vez que a legislação determina que o crédito deve ser calculado mês a mês e caso a empresa não tenha saídas tributadas esse valor é perdido, não sendo possível desconsiderar um mês, para utilizar o crédito posteriormente.

<http://tdn.totvs.com/pages/releaseview.action?pageId=51251122>
