---
content_hash: 1edeb08fb8659218edc5905e38c6e829a09787f7bc1b104acd9bedbc1f817d7d
fetched_at: '2026-06-29T00:06:00.264491+00:00'
page_id: '195300226'
product: rm
source: tdn-rm
title: RMFIS00003_12.003 - Perguntas e Respostas
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00003_12.003+-+Perguntas+e+Respostas
version: 7
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                      **Versão: todas** |
| **Processo** | **:** | ECF - Escrituração Contábil Fiscal |
| **Subprocesso** | **:** | ECF - Escrituração Contábil Fiscal |
| **Data da publicação** | **:** | 27/07/2015 |

## **Para que as informações do tributo\apuração sejam apresentadas na ECF é necessário encerrar o período de apuração?**

Sim, para correta geração da rotina é necessário que os períodos de apuração estejam encerrados.

## **Como corrigir a mensagem apresentada ao gerar a ECF?**

**“*Ocorreu o seguinte erro as informações referentes ao bloco J: Não foi identificado nenhum período para apuração das informações pelo Módulo Contábil*”**

Para corrigir a mensagem apresentada é necessário verificar se os períodos de apuração para os IRPJ e CSLL estão cadastrados e encerrados no sistema. Para os clientes que possuíam os períodos cadastrados antes da atualização do sistema para a ECF será necessário abrir e encerrar os períodos de apuração para que o sistema possa atualizar as informações.

**“*****Ocorreu o seguinte erro as informações referente ao bloco J:Não há linha na posição 0.*****”**

Esse erro ocorre quando o Plano de Contas Referencial não foi informado nos **Parâmetros Contábeis** do Anexo "Parâmetros Escrituração Contábil Fiscal" no Cadastro da Filial.

## **Existirá aba com IPI como existia na DIPJ?**

As informações sobre a apuração do IPI não foram migradas para a ECF.

## **Como gerar ECF imune e isenta?**

A geração da ECF para Imune e Isenta é parecida com a parametrização abordada no Workshop – Lucro Real, a diferença está apenas no modo de cálculo interno do sistema. Para informações sobre Imune e Isenta acesse: <http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.EventoImuneIsenta.aspx>

## **Para empresas Imune e Isenta onde os únicos tributos recolhidos são PIS sobre folha de pagamento e as retenções de Pis/Cofins/CSLL. Ao gerar a ECF, o sistema buscará esses valores?**

Na geração da ECF será considerado as informações sobre o IRPJ e CSLL de acordo com as contas contábeis cadastradas no Evento tributário e apuração do RM Liber. Se não ocorrer apuração desses tributos, poderá ser recuperado no validador da ECF as contas apresentadas no SPED Contábil (ECD).

Para mais informações sobre Imune e Isenta acesse: <http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.EventoImuneIsenta.aspx>

## **A empresa que é imune e isenta precisa informar na ECF os valores de pis/cofins/csll retidos na fonte através das notas fiscais de compra de terceiros?**

Não. Na ECF não são declarados valores retidos de terceiros.

## **Poderia explicar a geração do registro Y570 com informações provenientes do RM Fluxus?**

Sim, para geração do Y570 utilizando informações do RM Fluxus será necessário entrar em contato com o Suporte e solicitar o Script ExecSql.RMLIBER.TSGAP6. Ao executar o script será criado o parâmetro “Carregar Retenções do Fluxus” nos parâmetros da ECF no cadastro da Filial. Marcando esse parâmetro o sistema irá verificar os lançamentos financeiros com os tributos CSLL-RF, IRRF. Caso o parâmetro esteja desmarcado o sistema irá verificar as informações somente no RM Liber. **IMPORTANTE:** Indicamos que inicialmente o Script seja executado em base teste.
