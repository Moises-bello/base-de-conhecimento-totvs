---
content_hash: 45bf1730dfa1753ce9463662e2e2742bc2ca76c74ece5be9a1ea8d7fae5d651b
fetched_at: '2026-06-29T00:09:50.111723+00:00'
page_id: '435105401'
product: rm
source: tdn-rm
title: Evento Financeiro - Processo - Incluir lançamento financeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105401
version: 4
---

**Incluir lançamento financeiro**    
A "inclusão de lançamento" do evento financeiro é um processo do evento financeiro que permite a geração de lançamentos financeiros no módulo de gestão financeira da linha RM ou Protheus. Assim é possível gerenciar os pagamentos e recebimentos dos lançamentos através do módulo de gestão financeira. O processo de inclusão de lançamentos financeiros faz a leitura do parcelamento do evento financeiro e gera a distribuição das parcelas e inclui os lançamentos financeiros correspondentes aos dados informados na distribuição do parcelamento. Para cada distribuição da parcela do evento financeiro é gerado um lançamento financeiro correspondente no módulo de gestão financeira da linha RM ou Protheus.   
Só serão gerados lançamentos financeiros para eventos que possuam a situação igual a "Não integrado" ou "Parcialmente Integrado".  
Após a realização deste processo a parcela estará da seguinte forma:

* Os lançamentos financeiros são integrados ao módulo de gestão financeira da linha RM ou Protheus. - A situação de um evento financeiro com lançamentos financeiros gerados será: "Integrado" se todas  as parcelas do evento forem integradas, ou "Parcialmente Integrado", caso o evento tenha parcelas não integradas. - A distribuição das parcelas do evento financeiro recebe o identificador dos lançamentos financeiros gerados. - O evento financeiro bem como o parcelamento e respectiva distribuição fica bloqueado para alteração, caso todas as parcelas sejam integradas, ou apenas os dados do evento ficam bloqueados para alteração, caso evento fique em situação "Parcialmente Integrado".

**Memória de Cálculo**

A memória de cálculo é uma funcionalidade que permite visualizar os cálculos realizados durante o processo de inclusão de lançamentos financeiros, associados aos contratos de aluguel. Para acessar a memória de cálculo, deve seguir os seguintes passos:

1. Acessar o cadastro de Evento Financeiro em Aluguel / Evento Financeiro.
2. Selecionar o evento financeiro gerado e clicar em editar, ou dar dois cliques sobre o mesmo.
3. Na aba "Parcelamento", clicar duas vezes na parcela de uma determinada competência.
4. Acessar a aba "Memória de cálculo".

Observações

* Só será possível analisar a memória de calculo de uma parcela, quando houver inclusão de lançamentos financeiros no evento financeiro.
* Nem todos os processos geram uma memória de cálculo, mas rotinas como fundo promocional, aluguel complementar e outras irão trazer essa informação.
* É possível analisar tanto as parcelas "Integradas" quanto as "Não Integradas".
