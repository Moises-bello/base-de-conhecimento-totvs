---
article_id: 19636535750167
category: TAF - REINF
content_hash: 5ff58d6a6205b90b21c3885dc23d1977feaee100ea772b45740a64eadf602349
fetched_at: '2026-06-28T22:41:33.647931+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Como gerar evento R4099
  Fechamento/Reabertura
type: support-article
updated_at: '2023-12-07T17:35:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19636535750167-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-gerar-evento-R4099-Fechamento-Reabertura
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19636520074775) Tempo aproximado para leitura: 00:05:00 min****Dúvida**Como gerar evento R4099 Fechamento/Reabertura  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGATAF - Todas as versões  
  
**Solução**

O evento R-4099 - Fechamento/Reabertura Série R-4000 será utilizado para fechar e reabrir o período com os eventos da série R-4000. O controle de abertura e fechamento do período será realizado através da tabela **V3W** (R-4099- Fechamento dos Eventos), onde o campo Situação do Período **V3W\_SITPER** irá indicar quando o evento enviado ao RET se trata de um fechamento **V3W\_SITPER = 0** - Fechamento ou uma Reabertura **V3W\_SITPER= 1** - Reabertura.

1- **Requisitos para Fechamento:**

Deve haver pelo menos um registro da série R-4000 transmitido e autorizado no período para que seja realizado o fechamento. Períodos em que não existirem eventos da série R-4000 não devem ser fechados.

O período deve estar em aberto ou existir um evento de reabertura R-4099 do período mencionado na tela de apuração com status transmitido e autorizado.  
Não pode haver mais de um registro de fechamento R-4099 no mesmo período, sem que o anterior ainda não esteja fechado. Portanto, se houver um registro de fechamento R-4099 em aberto, não será possível gerar outro registro R-4099 para o mesmo período.

Para realizar o fechamento do período, na tela de Apurações de Eventos do Reinf, informe o mês/Ano que deseja realizar o fechamento. Se as condições acima forem atendidas, o R-4099 estará disponível para processamento.

Antes de realizar o fechamento, é importante certificar que os devidos eventos periódicos foram transmitidos e autorizados.

![image2023-1-3_12-10-53.png](https://tdn.totvs.com/download/attachments/344474121/image2023-1-3_12-10-53.png?version=1&modificationDate=1672758654123&api=v2)

**2- Requisitos para Reabertura:**

Deve existir um evento de fechamento R-4099 do período mencionado na tela de apuração com status transmitido e autorizado.

Para realizar a reabertura do período, na tela de Apurações de Eventos do Reinf, informe o mês/Ano que deseja realizar a reabertura. Se as condições acima forem atendidas, o R-4099 estará disponível para processamento no modo "Reabrir período".

![](https://tdn.totvs.com/download/attachments/344474121/image2023-8-25_11-49-10.png?version=1&modificationDate=1692974950507&api=v2)

Após clicar em Reabrir período são apresentados dois botões, Cancelar (reabertura) e Transmitir (reabertura).

![](https://tdn.totvs.com/download/attachments/344474121/image2023-8-25_11-51-3.png?version=1&modificationDate=1692975063663&api=v2)

Após o processamento do R-4099, é gerado um registro no cadastro R-4099.

Para acessar  a rotina **TAFA548** (Fechamento /reabertura período R4099) acesse:  Atualizações  -> Eventos Reinf -> Periódicos   -> Fechamento do período -> R4099  

![](https://tdn.totvs.com/download/attachments/344474121/image2023-1-3_12-9-11.png?version=1&modificationDate=1672758551467&api=v2)
