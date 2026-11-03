---
content_hash: 2cbd485b445186f96ff6756aa7500ba72588a7dc48a3ffc83fabd384a03e51d7
fetched_at: '2026-06-29T00:05:55.244150+00:00'
page_id: '128680618'
product: rm
source: tdn-rm
title: RMPAT00001_Boletim Técnico - Associação de Cenários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=128680618
version: 5
---

|  |  |  |
| --- | --- | --- |
| **Produto** | : | TOTVS Gestão Patrimonial – **Versão:** 11.52 |
| **Processo** | : | Ferramenta de Criação/Associação de Cenários |
| **Subprocesso** | : | Associação de cenários para melhor controle de imobilizados. |
| **Data da publicação** | : | 11/03/2014 |

**Introdução**

A criação de um novo cenário de cálculo nos patrimônios possibilita ao usuário a utilização de taxas de depreciação diferentes dos cenários já existentes e, também, a caracterização dos novos cenários como fiscais, para que tenham informações diferentes do(s) cenário(s) que seja(m) contábil(eis). Ou seja, o sistema possibilitará ao usuário ter mais de uma visão sobre o controle do imobilizado de suas empresas, sendo esta visão contábil ou fiscal, como taxas de depreciação diferentes ou não das ditas pela legislação de imposto de renda, dando assim um horizonte diferenciado sobre a vida de seu imobilizado.

|  |
| --- |
| **Desenvolvimento/Procedimento**  Inicialmente, deveremos criar uma nova moeda e um novo cálculo para que sejam associados ao novo cenário para segunda visão "Depreciação fiscal".   * Primeiramente, deveremos criar uma nova moeda:     Cadastro > Moedas e Índice > Cadastrar moeda e cotação para o novo cenário;        Após a criação da moeda para informar a cotação selecione a respectiva moeda > Processos > Preencher intervalo de cotações:  Período aplicar: Poderá ser dentro do período em aberto Fator: 1,00 (ou o fator que achar adequado) Marcar: Subescrever datas do intervalo Marcar: Fator Fixo Desmarcar: Considerar Somente dias úteis * Em seguida, deve ser criado um cálculo para associar ao novo cenário:     Cadastro > Cálculos. * Em seguida criar um novo cenário:     Cadastro > Cenários. (Associar o cálculo e a moeda e o índice a este cenário).            O grupo de patrimônio deverá estar criado com seus respectivos bens já associado:     **Ressaltamos que esta etapa do processo deve ser executada** **exclusivamente através da MDI.**     A parametrização do processo é feita acessando o menu Utilitários >> Associação de Cenários. Neste, devem ser preenchidos obrigatoriamente os campos abaixo:            **Grupo de Patrimônio:** Grupo ao qual o cenário a ser criado será vinculado.     **Cenário de Cálculo:** Cenário ainda não vinculado ao Grupo de Patrimônio informado. Este campo só será habilitado quando o Grupo de patrimônio for preenchido.   No filtro, só serão apresentados cenários ainda não vinculados ao grupo.     **Cenário de Cálculo base para cálculos:** Qual será o cenário de cálculo que o sistema irá basear para criar os saldos patrimoniais do novo cenário informado.     **Taxa de Depreciação:** Qual será a taxa de depreciação padrão para o cenário a ser criado.     O usuário ainda poderá marcar as opções:     **Replicar estrutura contábil do Grupo de Patrimônio:**   Ao marcar esta opção, todos os eventos do cenário de Cálculo Base serão replicados para este novo cenário.     **Apenas converter valores para nova moeda:**   Ao criar um cenário com esta opção, o sistema apenas converterá os valores base, depreciações acumuladas e valores de testes de impairment de acordo com a moeda do novo cenário e sua cotação em relação à moeda do cenário base informado. Não efetuará cálculos dos saldos de acordo com a nova taxa default informados. * Realizando a parametrização conforme desejado, o processo poderá ser executado. O sistema irá realizar algumas validações para conclui-lo com sucesso. * Deve ser realizado o fechamento do período de cálculo anterior. Caso contrário, o sistema irá apresentar a mensagem: ***É necessário o Fechamento de Período para execução do processo.*** * Não poderão existir operações patrimoniais no período de cálculo atual. Caso contrário, o sistema irá apresentar a mensagem: ***Existem operações patrimoniais no período de cálculo atual que impossibilitam a execução do processo.*** * Não poderão existir contabilizações no período de cálculo atual. Caso contrário, o sistema irá apresentar a mensagem: ***Existem contabilizações no período de cálculo atual que impossibilitam a execução do processo.*** * Existir cotação. Se a moeda do cenário escolhido utilizar índice, verificar a existência das cotações para o período de cálculo atual e primeiro dia posterior ao período.       Se for parametrizado para somente converter valores para nova moeda, o sistema irá criar a estrutura de saldos dos patrimônios de acordo com a cotação da nova moeda, em relação à moeda do cenário base para cálculos que foi informado.       Caso contrário, o cálculo será criado da seguinte forma:     **Valor base novo:** Se cenário for fiscal, será igual ao (Valor Base do cenário base + Valor de Impairment do cenário base) convertido pela cotação da nova moeda em relação à moeda do cenário base;   Se não for fiscal, o cálculo será feito sem adição do Valor de Impairment ao Valor Base do cenário base;     **Depreciação mensal nova:** Taxa default mensal aplicada ao Valor base novo;     **Depreciação acumulada:** Depreciação mensal nova multiplicada pelo número de meses entre a data de início de vigência do cálculo do patrimônio até o período de cálculo atual. Se início de vigência for posterior ao período de cálculo atual, a depreciação acumulada será igual à zero;   Valores em índices serão calculados de acordo com a cotação atual do índice se a moeda no cenário em questão usar índice.         Fonte: <http://wikihelp.totvs.com.br/WikiHelp/PAT/PAT.AssociaCenario.aspx> |

Para maiores informações:

[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)

**COMUNIDADE**[**R@Contábil**](https://totvs.byyou.com/?space=rcontabil)

**Canais** **de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 2 – (Controladoria e Finanças), 2 – (Ativo Fixo).
