---
content_hash: 0ca5434a82717bf6702e72b8d54693886ca5053b49be00bdc80d1864128e1deb
fetched_at: '2026-06-29T00:08:41.431489+00:00'
page_id: '286728337'
product: rm
source: tdn-rm
title: RMFIS00009_Apuração de Tributos Retidos - PIS RF, COFINS RF e CSLL RF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286728337
version: 3
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | Totvs Gestão Fiscal |
| **Versões:** | 12.X |
| **Ocorrência:** | Apuração de tributos retidos |
| **Ambiente:** |  |
| **Passo a passo:** | Os **tributos retidos** são apurados pelo período de apuração no RM Liber, desde que haja lançamentos financeiros, no RM Fluxus, que contenham os tributos **RF** (**retidos**) com código da receita, base, alíquota e valor destacados.        **Obs.: O fato gerador das Contribuições Sociais retidas é a data da baixa do lançamento original, ou seja, a baixa deve estar dentro do período selecionado/encerrado**.      Realize a geração de guias à partir de Lançamentos Financeiros, através dos processos do período. Lembrando que o mesmo deve estar encerrado.        Será exibido uma tela para ser repassado os dados da fatura. Após, execute o processo.          É gerado uma guia DARF e automaticamente, o vencimento da fatura, é integrado com o RM Fluxus.              **ATENÇÃO**:    Caso sistema exiba uma mensagem de inconsistência, ao executar o processo de Geração de Guias à partir de Lançamentos Financeiros, segue abaixo as possíveis causas:             **Verifique:**    * Se já tenha sido executado o processo e as guias já foram geradas.       * Se a data da baixa do lançamento financeiro com este tributo está condizente com o período de apuração selecionado/encerrado.       * Se existe integração entre os sistemas está definida.  **Acesse: Ambiente | Parâmetros -> Integração de Sistemas - RM Liber <-> RM Fluxus e RM Fluxus <-> RM Liber**. Ambos os *flags***Integração**e **Aplicar para todas as Coligadas**, devem estar marcados.      * Se o parâmetro de **Integração Fiscal**, está definido. **Ambiente | Parâmetros -> TOTVS Gestão Financeira ->****02.01. - Contas a Pagar****-> Etapa 25 -**          * Se os Lançamentos Financeiros estão com o tributo retido devidamente destacado. |
| **Observações:** |  |
