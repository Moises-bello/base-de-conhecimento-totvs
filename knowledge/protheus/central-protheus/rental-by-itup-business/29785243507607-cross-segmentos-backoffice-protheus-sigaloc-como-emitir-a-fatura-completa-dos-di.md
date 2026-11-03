---
article_id: 29785243507607
category: Rental by ItUp Business
content_hash: 4bc81ba27366e7be21c52a00b523b1e3b64d09e722a0dffdbb1e95cde849793e
fetched_at: '2026-06-28T22:36:20.541988+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGALOC - Como emitir a fatura completa
  dos dias da locação quando a data de retorno é preenchida antes da data final do
  projeto?
type: support-article
updated_at: '2026-04-09T12:47:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29785243507607-Cross-Segmentos-Backoffice-Protheus-SIGALOC-Como-emitir-a-fatura-completa-dos-dias-da-loca%C3%A7%C3%A3o-quando-a-data-de-retorno-%C3%A9-preenchida-antes-da-data-final-do-projeto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29785235697175) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como emitir a fatura completa dos dias da locação quando a data de retorno é preenchida antes da data final do projeto?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGALOC - P12.1.2310.

1. Na rotina **LOCA001 - Manutenção de Projetos**, clique em **Outras Ações >> Ret. de Locação**.
2. Selecione o equipamento e preencha os **Dados da Retirada** com a data de fim da locação. Em seguida, atualize as informações.
3. Acesse o contrato e verifique se os campos **Prev. Retira (FPA\_DTPRRT)** e **Dat. Solic. Re (FPA\_DTSCRT)** estão preenchidos com a data informada nos **Dados da Retirada**.
4. Retorne para o navegador da rotina **LOCA001 - Manutenção de Projetos**, clique em **Outras Ações >> Ret. de Locação** e gere a nota fiscal de retorno da locação.

**Observação:** Mesmo que a **data da Nota Fiscal de Retorno de Locação (FPA\_DNFRET)** esteja preenchida com uma data anterior à data de término da locação, o sistema irá validar as datas nos campos **Prev. Retira (FPA\_DTPRRT)** e **Dat. Solic. Re (FPA\_DTSCRT)** para gerar automaticamente o faturamento com o período completo.
