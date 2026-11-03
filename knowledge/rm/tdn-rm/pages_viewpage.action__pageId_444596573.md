---
content_hash: 1c0c103d1582563d83d4e8f2b08edcb1c971de15e3f9cb612a1b7bafa2b70d43
fetched_at: '2026-06-29T00:09:54.224786+00:00'
page_id: '444596573'
product: rm
source: tdn-rm
title: Apuração do IRRF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=444596573
version: 3
---

A cada inserção de Guias automaticamente, o sistema irá gerar guias para os lançamentos que estão em aberto, sem nenhuma fatura relacionada.

O sistema estará verificando os parâmetros de Geração das Guias em Ambiente | Parâmetros | TOTVS Gestão Financeira | Apuração de Tributos | IRRF Pessoa Física – Etapa 11, nele é possível definir se as guias serão geradas por Beneficiário, por lançamento ou por Filial, neste o sistema estará verificando se o campo Filial Matriz do Estabelecimento está preenchido em Ambiente | Parâmetros | TOTVS Gestão Financeira | Apuração de Tributos - Etapa 22 - Filial Matriz, se este estiver marcado, o usuário deverá gerar as guias em cada Filial  caso contrário as guias de todas as filiais serão geradas na Filial matriz.

Ao gerar as Guias Darf´s para o tributo IRRF o sistema irá considerar o parâmetro "Data Base para Geração do IRRF" no TOTVS Gestão Financeira, em Ambiente | Parâmetros | TOTVS Gestão Financeira | Manutenção de lançamentos | Cálculo de tributos – IRRF | Geração IRRF.

Para os lançamentos gerados pelo **TOTVS Gestão de Folha de Pagamento** (Classificação 13) o sistema sempre considera a Data de Emissão para os Lançamentos de "IRRF", independente do parâmetro acima informado.

Ao gerar a Guia DARF o sistema estará considerando os lançamentos de "IRRF a pagar" gerados pelo **TOTVS Gestão de Folha de pagamento**. Para isto, o usuário deverá selecionar o tipo de funcionário na grade de seleção e informar o Código da Receita do Lançamento Financeiro no momento da geração dos Lançamentos. Caso existam os dois tipos de funcionário na empresa o usuário deverá realizar o processo uma vez para cada (mais detalhes verificar help do **TOTVS Gestão de Folha de pagamento**). Estes lançamentos passarão a ser considerados pelo Sistema de Gestão Fiscal na geração de DARF e consequentemente, estas DARFs constarão na DCTF gerada pelo Sistema de Gestão Fiscal.Para o tributo IRRF, se as guias forem inseridas manualmente, a pasta RATEIOS será habilitada para sejam informados os rateios por centro de custo e departamentos.
