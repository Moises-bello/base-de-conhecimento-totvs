---
article_id: 34293172640151
category: Gestão de Armazenagem (WMS)
content_hash: 815fbf5e397de2595f5349c576ff1ec68c3dfc43ee4a3ce9c5479defd2f1662a
fetched_at: '2026-06-28T22:45:47.961869+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: Distribuição - Linha Protheus - WMS - Reabastecimento do picking unitário pelo
  picking master
type: support-article
updated_at: '2025-08-22T12:58:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34293172640151-Distribui%C3%A7%C3%A3o-Linha-Protheus-WMS-Reabastecimento-do-picking-unit%C3%A1rio-pelo-picking-master
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34293189129111) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como funciona o reabastecimento do **picking unitário** pelo **picking master**?  
  
**Ambiente**  
**TOTVS Distribuição** - **TOTVS WMS** (Linha Protheus) - Gestão de Armazenagem (**WMS**) - Todas as versões  
  
**Solução**  
O parâmetro **MV\_WMSPKMA - Permite o abastecimento do endereço de** ***picking*** **com outras estruturas de** ***picking*** **de quantidade mínima maior**, quando informado com **.T.** , indica que durante a geração do reabastecimento por demanda, caso seja necessário reabastecer o ***picking*** **unitário**, deverá priorizar esse reabastecimento pelo ***picking*** **master**.  
  
Logo, além da parametrização, é necessário configurar na **Sequência de Abastecimento - WMSA030** outra estrutura física de ***picking***, isto é, o ***picking*** **master**, com a **Separação Mínima - DC3\_QTDUNI** maior que a estrutura a ser abastecida.   
  
**Por exemplo:**  
Estrutura Física 000002 - ***PICKING*** - Separação Mínima 0 - como ***picking*** **unitário**  
Estrutura Física 000006 - ***PICKING*** **II** - Separação Mínima 25 - como ***picking*** **master**

![Seq.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/34299445824151)

Quando existir saldo no ***picking*** **master** deverá reabastecer o ***picking*** **unitário**. Se não existir saldo no ***picking*** **master** para reabastecer o ***picking*** **unitário**, será efetuada uma busca na estrutura de **pulmão** para esse reabastecimento.   
  
**Saiba mais**  
Verifique na documentação a seguir mais informações sobre o tema: [DT Abastecimento de Picking Fracionado Somente Pelo Picking Caixa](https://tdn.totvs.com.br/display/public/PROT/DT+Abastecimento+de+Picking+Fracionado+Somente+Pelo+Picking+Caixa)
