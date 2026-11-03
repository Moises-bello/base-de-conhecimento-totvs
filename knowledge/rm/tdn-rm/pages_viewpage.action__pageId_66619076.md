---
content_hash: 08d8717a10f8414448b56236066874e03e7bf16fd614b7c1634c374629b2fd6b
fetched_at: '2026-06-29T00:11:16.304896+00:00'
page_id: '66619076'
product: rm
source: tdn-rm
title: RMFIN00001_Aplicação Financeira - TOTVS Gestão Financeira
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=66619076
version: 8
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Financeira                         **Versão:** 11.0.7 |
| **Processo** | **:** | Aplicação Financeira |
| **Subprocesso** | **:** | Informações Gerais sobre Aplicação Financeira |
| **Data da publicação** | **:** | 15/07/2013 |

O sistema possui um gerenciador de Aplicações Financeiras, que controla diversos Tipos de Aplicações assim como Poupança, CDB e Fundos de Investimentos. Gerencia a abertura de vários tipos de Aplicações Financeiras para diversas Contas/Caixas, podendo controlar o Valor Mínimo Inicial, o valor Mínimo para Aplicação, o Saldo Mínimo, o Valor Mínimo para Resgate (esses dados informados pelos Bancos) e Carência para o IOF (Imposto sobre Operações Financeiras).

**Recursos disponíveis:**

* Controle de Rendimentos de cada Aplicação Financeira, dependendo da inclusão de índices financeiros no cadastro de Moedas.

* Realização de Resgates das Aplicações Financeiras, onde serão gerados Extratos de Caixa e atualização dos saldos das Contas/Caixa, caso o usuário deseje.

* Geração automática de Resgates de IR (Imposto de Renda), nos períodos determinados por lei.

* Geração automática de lançamentos de IOF sobre rendimentos, para Aplicações Financeiras que estão sujeitas a tributação.

* Contabilização dos lançamentos através de defaults contábeis ou de eventos contábeis.

* Ajuste de saldos de Aplicações Financeiras, para que sejam corrigidas diferenças de arredondamento entre o saldo do sistema e o saldo informado pela instituição financeira.

Além das diversas funcionalidades relativas às operações bancárias, o sistema ainda oferece o **Simulador de aplicações financeiras**, que  é uma ferramenta que permite visualizar o comportamento de uma determinada aplicação sem a necessidade de realizar o processo comum de cadastramento. Além disso, é possível utilizar índices passados ou previsões de índices futuros.

**Benefícios do Simulador de Aplicações**

* Produz diversos cenários, que podem ser comparados através de gráficos.
* Permite realizar os cálculos das aplicações financeiras, suportando as características de cada tipo de Aplicação.
* Permite a exportação/importação da simulação, tornando o processo mais dinâmico.

#### Desenvolvimento/Procedimento

1 -     Inclua a Conta/Caixa que será utilizada pelo Tipo de Aplicação (menu cadastros | Contas Caixa).

2 -     Inclua a moeda que será utilizada como Indexador do Tipo de Aplicação (menu cadastros | Moedas). O campo "Número de Casas decimais" deve ser preenchido com o número 9 (nove), para que não ocorram diferenças no cálculo de “quantidade de cotas”.

3 -     Cadastre as cotações da moeda que será utilizada como Indexador do Tipo de Aplicação (menu cadastros | Cotações). As cotações devem ser cadastradas de acordo com a data da aplicação, pois é através dessa cotação (índice/fator) que o sistema irá processar os cálculos de “quantidade de cotas” e “valor disponível da aplicação”. Os outros dados são opcionais.

4 -     Defina como será a contabilização dos lançamentos do tipo de aplicação financeira, por “Default Contábil” ou por “Evento Contábil”.

5 -     Se a contabilização for por evento contábil, inclua os Eventos Contábeis que serão utilizados para contabilizar as Aplicações, os Resgates, os Rendimentos, o IOF e o IR (menu cadastros | Eventos Contábeis). Vale ressaltar que para realizar a contabilização dos ajustes, é necessário que na mesma data do ajuste exista uma movimentação efetiva referente ao ajuste.

 Exemplo: Se no dia 31/10/2010 existir um “Ajuste de Rendimento”, para que esse ajuste seja contabilizado, deve existir nessa mesma data uma movimentação de “Rendimento”, gerada a partir do encerramento de período.

 6 -     Verificar se o usuário já tem permissão de acesso para o módulo de Aplicações Financeiras. Para isso, acesse o Menu Cadastros | Segurança | Perfis, clique duas vezes sobre o perfil que deseja e na pasta "Acesso a Menus", verifique se a opção “Aplicação Financeira” está na coluna "Itens Permitidos". Se não estiver, transfira-a e efetue um novo “login”, assim, a opção já estará disponível.

 7 -     Inclua um novo Tipo de Aplicação Financeira. Ao incluir um novo Tipo de Aplicação Financeira, será necessário informar o Código da Conta/Caixa, a Natureza da Aplicação (CDB, Poupança, Fundo Fixo, etc), o Código Indexador (moeda/índice). Poderão ser informados ainda Valor Mínimo Inicial e de Aplicação, Saldo Mínimo e Valor Mínimo de Resgate, bem como os eventos contábeis para a contabilização de cada movimentação ou até mesmo definir o default contábil da aplicação.

 8 -     Inclua uma nova Aplicação Financeira. Nessa inclusão, deverá ser definido se as movimentações gerarão extratos de caixa, e se gerar, se os mesmos serão contábeis. É de suma importância que sejam informados ainda a data inicial, taxa fixa e data de vencimento (ou número de dias). Poderão ser informadas ainda tabelas opcionais, centro de custo e departamento que serão carregados nos extratos de caixa.

9 -     Acompanhe a movimentação da Aplicação Financeira, controlando o IOF, o Imposto de Renda, realizando Resgates, Contabilizando os lançamentos ou excluindo lançamentos do tipo de aplicação financeira.

 10 - Para que o sistema controle a movimentação do tipo de aplicação financeira por mês, é necessário Encerrar o Período do Tipo de Aplicação Financeira no principio de cada mês. Caso ocorram diferenças de arredondamento entre os saldos do sistema e os saldos informados pela instituição financeira, realize os ajustes de saldos. Quanto aos ajustes de saldos, vale ressaltar que para contabilizá-los, na mesma data deve existir uma efetiva movimentação relativa ao ajuste. Vide exemplo citado anteriormente, no item 5.

***Atenção:***

É muito importante que o Calendário esteja atualizado de forma a não comprometer os cálculos/rendimentos do processo.

Para Maiores Informações

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)

**COMUNIDADE **[R@MATERIAS E FINANÇAS](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 2 – (Controladoria e Finanças),5 – (Planej. e Contr. Orçam.) e 4 –  (RMFluxus).
