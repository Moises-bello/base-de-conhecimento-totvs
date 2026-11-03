---
article_id: 32292447017239
category: eConsignado (Crédito do Trabalhador)
content_hash: afbf0f6b35d90726a5ad465af023e5d1e43ac1dae4c3063c17810845de118a17
fetched_at: '2026-06-28T22:43:07.197513+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH - Linha Protheus - GPE - Como cadastrar as verbas de Provisionamento nas
  Férias e Adiantamento referente ao eConsignado (Programa Crédito do Trabalhador)
type: support-article
updated_at: '2026-01-14T17:56:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32292447017239-RH-Linha-Protheus-GPE-Como-cadastrar-as-verbas-de-Provisionamento-nas-F%C3%A9rias-e-Adiantamento-referente-ao-eConsignado-Programa-Cr%C3%A9dito-do-Trabalhador
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32292453336983)** Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Como cadastrar as verbas de Provisionamento nas Férias e Adiantamento referente ao eConsignado   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - TOTVS Gestão de Pessoal - Todas as versões  
  
**Solução**  
Por ocasião de férias e adiantamento, o funcionário pode não ter valores disponíveis para o desconto do eConsigando na folha de pagamento e por isso deve ser criado uma forma dos valores referente ao empréstimo serem provisionados, para posterior desconto em folha.

Foram criados seis novos identificadores de cálculo com as seguintes parametrizações:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35930669703575)  
  
  
**Observações:**-As verbas **não possuem incidências**, pois servirão apenas para circular entre as férias/adiantamento e a folha.   
-No caso de férias, o **cadastro da verba de mês seguinte é opcional**, podendo ser feito todo o processo apenas com a verba do mês  
-A verba com ID 1972, diferente do usual, deve ser relacionada com a verba de ID 1973 e não 1971. Da mesma forma, a verba com ID 1974 deve ser relacionada com o ID 1975.   
-Foram realizados testes de envio para o eSocial com as naturezas descritas acima. Como as verbas não possuem incidências, não houve qualquer impacto no cálculo, nem no retorno dos eventos S-5001, S-5002 e S-5003 pelo RET.  
  
**Exemplo** do cadastro da verba de ID 1971- Provisão eConsigado Férias  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32292600173207)

Obs.: Para as verbas de provisionamento do ADI e de Férias os campos referente a REF a Férias e REF a ADI, devem estar = Não.   
**As verbas de Provisionamento não possuem nenhum tipo de incidência.**   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33822093385111)

Para cadastrar a verba de desconto para Empréstimo Consignado acesse **Atualizações> Definições de Cálculo> Verbas** e selecione a opção **incluir.**  
  
**Liquido de Férias**

O id de cálculo **1979** foi criado para possibilitar a **contrapartida** do **provisionamento** das **férias** na folha, **sem alteração do liquido**. Se ela for criada, será gerada na folha com o valor total do provisionamento, sem alteração do liquido. Caso ela não exista, o sistema continuará ajustando o liquido para realizar a contrapartida.  
  
**Saiba Mais**  
[Manual Crédito Trabalhador](https://tdn.totvs.com/pages/viewpage.action?pageId=944703898)  
[RH - Linha Protheus - GPE - Como cadastrar a verba de desconto do eConsignado (Programa Crédito do Trabalhador)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/31149947210519-RH-Linha-Protheus-GPE-Como-cadastrar-a-verba-de-desconto-do-eConsignado-Programa-Cr%C3%A9dito-do-Trabalhador)  
[RH - Linha Protheus - GPE - Como calcular na folha de pagamento o Credito Trabalhador eConsignado Medida Provisória nº 1.292/2025](https://centraldeatendimento.totvs.com/hc/pt-br/articles/31152092269591-RH-Linha-Protheus-GPE-Como-calcular-na-folha-de-pagamento-o-Credito-Trabalhador-eConsignado-Medida-Provis%C3%B3ria-n%C2%BA-1-292-2025)
