---
content_hash: 626e56d488cbd4910f9f3b06b0fdb17b52d935da656672459cd3a5377b0be7a0
fetched_at: '2026-06-29T00:11:46.041196+00:00'
page_id: '822677716'
product: rm
source: tdn-rm
title: DT - Informe de Rendimentos 2024
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+Informe+de+Rendimentos+2024
version: 39
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Informe de Rendimento - Detalhamento da Pensão Alimentícia |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | DRHROTRM-8686  DRHROTRM-5778 |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2302.259
* 12.1.2306.220
* 12.1.2310.152
* 12.1.2402.101

## **03. SITUAÇÃO/REQUISITO**

A partir de 2024, a geração do informe de rendimentos requer a utilização do FOPREL0008 - Informe de Rendimentos - NOVO MODELO, disponível no TOTVS Compartilhamento.

Este relatório oferece um design mais moderno, proporcionando uma experiência aprimorada no produto e maior satisfação aos nossos usuários. Além disso, disponibilizamos o detalhamento de pensão no campo 7 (Informações Complementares). 

## **04. SOLUÇÃO**

Adequação na folha de pagamento para abranger as seguintes modificações no campo 7 (Informações Complementares):

* Detalhamento da pensão sobre folha/férias, 13º salário, PLR e RRA, conforme demostrado abaixo:

PONTOS DE ATENÇÃO:

1. Os eventos relacionados à pensão sobre folha, 13º salário, férias e PLR devem ser registrados tanto na ficha financeira quanto no movimento de pensão do(s) dependente(s).
2. É necessário informar corretamente os valores da pensão no sistema para garantir uma geração precisa do detalhamento da pensão.
3. Quanto aos valores referentes ao RRA, é essencial que estejam devidamente registrados no histórico de RRA, incluindo o detalhamento da pensão por dependente.

**Exemplos:**

Ficha Financeira

Movimento da Pensão do Dependente, existente em Funcionários | Anexos | Dependentes:

Histórico RRA existente em Funcionários | Anexos | Históricos:

Detalhe da pensão por Dependente:

IMPORTANTE:

**1-**Para incluir a pensão alimentícia de forma discriminada no campo 7 (Informações Complementares), é imprescindível realizar a exclusão do relatório anterior e proceder com a importação do novo leiaute disponível no TOTVS Compartilhamento. Essa ação garantirá a correta exibição das informações detalhadas referentes à pensão alimentícia no relatório atualizado.

**2-**Para que o relatório (FOPREL0008 - Informe de Rendimentos-Novo Modelo.TotvsReport) seja gerado através do portal, é necessário configurá-lo no parametrizador. Para isso acesse o Parametrizador do RM Portal, edite o Grupo de Acesso correspondente e informe o relatório desejado (FOPREL0008 - Informe de Rendimentos-Novo Modelo.TotvsReport)

É importante ressaltar que, caso este campo não seja preenchido, o Informe de Rendimentos não será gerado.

## **05. DEMAIS INFORMAÇÕES**

[Comunicado DIRF 2024](https://tdn.totvs.com/display/LRM/Comunicado+DIRF+2024)

[DIRF/Informe de Rendimentos](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719351)

[DIRF 2024](https://tdn.totvs.com/display/public/LRM/DT+-+DIRF+2024)
