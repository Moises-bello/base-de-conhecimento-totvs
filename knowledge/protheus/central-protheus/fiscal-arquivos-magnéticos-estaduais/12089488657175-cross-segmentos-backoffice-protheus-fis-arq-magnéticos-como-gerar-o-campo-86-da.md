---
article_id: 12089488657175
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: ae5afd3d9ddaa20c039639608f3d9f3c83b9effad090c3aed382b4c821173ad5
fetched_at: '2026-06-28T22:42:09.143979+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  o campo 86 da DAPI?
type: support-article
updated_at: '2023-02-01T21:01:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12089488657175-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-o-campo-86-da-DAPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Como gerar o campo **86 - Valor Retido** da **DAPI**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

O campo **86 - Valor Retido** é  gerado com base nos valores totais das operações do período lançadas no livro **Registro de Entradas** nas seguintes condições:

1. No cadastro da **TES** o campo**Solid. Obs (F4\_OBSSOL)** esteja preenchido com **SIM**

2. O sistema recebe informações do campo **ICMS Solid. (D1\_ICMSRET).**
