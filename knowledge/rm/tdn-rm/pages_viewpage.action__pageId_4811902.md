---
content_hash: 4dfbf0bb2a79247fe335eb2f85bc291d6f525408064014bed8b788d54cc95d16
fetched_at: '2026-06-29T00:10:18.450490+00:00'
page_id: '4811902'
product: rm
source: tdn-rm
title: Rateios por Centros de CustoNatureza Orçamentária Financeira
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4811902
version: 4
---

BLOCK

Rateios por Centros de CustoNatureza Orçamentária Financeira

FAQ: **Rateios por Centros de Custo/Natureza Orçamentária Financeira**

|  |  |
| --- | --- |
| Produto: | Unspecified |
| Ambiente: | Unspecified |
| Versão: | 11.00 |

Solução

|  |
| --- |
| **Introdução**  A funcionalidade do Rateio é oferecer informações detalhadas por Centros de Custo, Natureza Orçamentária Financeira e Departamentos.    **Desenvolvimento/Procedimento**       1. Através do Assistente de Implantação de Processos, 02.01 Pagar, Recursos Adicionais, ativar o rateio por centros de custo, natureza ou ambos. Você pode inclusive definir obrigatoriedade. Dessa forma, o sistema irá consistir a falta dessa informação na inclusão do lançamento. 2. Opcionalmente você poderá definir também o rateio por Departamento. 3. Proceda o cadastro dessas tabelas através do Menu Cadastros.   Duvidas, consulte o help. 4. Você poderá informar no cadastro do Cliente/Fornecedor(Dados Adicionais), o rateio default. Lembrando que se o clifor for do tipo ambos, a tabela Natureza Orçamentária Financeira e Centros de Custo deverão ser informadas para a pagar e a receber. No momento da inclusão do lançamento, o sistema trará como default esses dados compatíveis com a natureza(pag/rec) do lançamento. |
| **Valores do Rateio por Centro de Custo**    É possível parametrizar o sistema para que os valores dos Rateios sejam calculados pelo valor Baixado, conforme exemplo abaixo:    ·         Valor original do Lançamento: 1000,00  ·         Rateio por Centro de Custo antes da baixa do Lançamento:  o   Centro de Custo – Administrativo: 500,00 / 50%  o   Centro de Custo – Vendas: 250,00 / 25%  o   Centro de Custo – RH: 250,00 / 25%  o   Total do Rateio: 1000,00  ·         Valor da Baixa do Lançamento: 500,00  ·         Rateio por Centro de Custo após a baixa do Lançamento:  o   Centro de Custo – Administrativo: 250,00 / 50%  o   Centro de Custo – Vendas: 125,00 / 25%  o   Centro de Custo – RH: 125,00 / 25%  o   Total do Rateio: 500,00    Esta funcionalidade não altera os valores Original e Líquido do Lançamento Financeiro, são apenas informações para um controle gerencial sobre as despesas e recebimentos, individualmente por centro de custo, de acordo com o Valor Baixado do Lançamento.    Essa consistência é definida através do parâmetro: 'Rateio por Centro de Custo e Departamento serão calculados pelo valor baixado' em menu opções > Parâmetros > RM Fluxus – Avançar > Contas A Pagar ou Contas A Receber > Processo 02.01.02 – Baixa – Avançar > Etapa Baixa ½. |
| **Departamento** Para aplicação do Rateio por Departamento no Lançamento é utilizado o mesmo processo descrito para Rateio por Centro de Custo/Natureza Orçamentária Financeira. |
| **Centro de Custo e Rateio por Centro de Custo**  Pode-se definir um Centro de Custo e um Rateio por Centro de Custo em um Lançamento Financeiro, sendo possível posteriormente criar relatórios para o controle destas informações, pois essas são armazenadas em tabelas diferentes:  Centro de Custo definido na guia Dados Adicionais do Lançamento – Campo CODCCUSTO da Tabela FLAN.   Centros de Custos definidos no Rateio por Centro de Custo do Lançamento – Tabela FLANRATCCU.    De acordo com a parametrização do sistema, pode-se trabalhar apenas com o preenchimento do campo Centro de Custo do Lançamento (CODCCUSTO da Tabela FLAN), de acordo com a necessidade da empresa. |
