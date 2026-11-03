---
content_hash: c629b51ad6c3200a104c7f2c81e6d22b37f1188deefbe97aaa96896262e4f614
fetched_at: '2026-06-29T00:08:28.639435+00:00'
page_id: '271676726'
product: rm
source: tdn-rm
title: 443052_DT_Bolsas_Que_Nao_Compoe_Contabilizacao_Por_Competencia
type: documentation
url: https://tdn.totvs.com/display/LRM/443052_DT_Bolsas_Que_Nao_Compoe_Contabilizacao_Por_Competencia
version: 112
---

# CONTABILIZAÇÃO POR COMPETÊNCIA

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Educacional.* |
| **Módulo:** | ***Totvs Gestão Educacional**.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Contabilização por competência* | *Contabilização de contratos por competência.* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Cadastro de bolsas** | **Cadastro de bolsas*.* | |  |  | |
| **Cadastros Iniciais:** | *Cadastro de bolsas.* |
| **Parâmetro(s):** | *Compõe a contabilização por competência* |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | *443052* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *MEDU-2620* |
| **País(es):** | *N/A* |
| **Banco(s) de Dados:** | *N/A* |
| **Tabelas Utilizadas:** | *SBOLSA* |
| **Sistema(s) Operacional(is):** | *N/A* |

## Descrição

O TOTVS Educacional possibilita a contabilização em regime de competência, através da integração nativa com o TOTVS Gestão Contábil. Através deste modelo, o sistema apropria toda a receita e a difere ao longo da prestação do serviço, conforme o número de competências parametrizadas. Fazem parte da contabilização as bolsas, descontos e serviços.

A contabilização de bolsas ocorre de forma análoga a contabilização dos serviços, onde é possível definir no evento contábil um item de evento com contas específicas para bolsas ou definir um item de evento que busque as contas contábeis de cada bolsa, através do default contábil de cada bolsa.

Ao gerar contabilização por competência, o sistema assume que todas as bolsas existentes no contrato compõe a contabilização por competência. Assim, para o caso onde se utiliza um item de evento que busque as contas configuradas em cada bolsa, é mandatório que todas as bolsas possuam contas parametrizadas, pois pode ocorrer do sistema não conseguir carregar nenhuma conta contábil. Assim, caso exista a necessidade de desconsiderar uma determinada bolsa do processo de contabilização por competência, o sistema não atende.

Com o novo modelo, de forma análoga como funciona o cadastro de serviços, cada bolsa poderá ser parametrizada para compor ou não a contabilização por competência. Assim, ao parametrizar uma bolsa para não ser contabilizada, o processo de contabilização por competência irá desconsiderar a bolsa de todos os cálculos e lançamentos contábeis.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação da release.

1. Uma vez definida qual a bolsa que não deverá compor a contabilização por competência, basta parametriza-la no cadastro de bolsas do TOTVS Educacional, conforme abaixo.
2. Para que a bolsa possa compor a contabilização por competência é mandatório que a bolsa seja do tipo incondicional.
3. Caso a bolsa seja definida para não compor a contabilização por competência, somente será possível contabilizar por competência contratos que nunca tiveram a bolsa contabilizada.

Imagem 01 – Parametrização da bolsa

## Procedimento para Utilização

Gerar a contabilização por competência. Caso o contrato possua uma bolsa que esteja definida para não compor a contabilização por competência, a contabilização será gerada com sucesso e os valores e contas contábeis referentes a bolsa não serão processados.

divs
