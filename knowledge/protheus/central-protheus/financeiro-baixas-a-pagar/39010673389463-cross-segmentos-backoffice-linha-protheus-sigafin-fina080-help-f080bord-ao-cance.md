---
article_id: 39010673389463
category: Financeiro - Baixas a Pagar
content_hash: 4d759d8dc4765f7de3f4aabef7ba7fc7dd1a825676624623bdc9521793553cf0
fetched_at: '2026-06-28T22:37:24.887977+00:00'
product: protheus
section_id: 38295862957335
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA080 - HELP: F080BORD
  ao cancelar baixa de título manual'
type: support-article
updated_at: '2026-03-27T03:03:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39010673389463-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA080-HELP-F080BORD-ao-cancelar-baixa-de-t%C3%ADtulo-manual
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39010701560599) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Ao tentar efetuar o cancelamento de uma baixa manual através da rotina Baixas Pagar Manual (FINA080), o sistema apresenta o Help: F080BORD

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39010673386263)

**Ambiente**  
  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**

Este incidente ocorre quando o título faz parte de um borderô que foi baixado via **Baixa Automática (FINA090)** em lote, gerando um registro agrupado na tabela de movimentos bancários (**SE5**). Quando o valor total desse lote/borderô é conciliado através do **Conciliador Backoffice (CTBA940)**, o sistema bloqueia o cancelamento individual da baixa para manter a integridade dos saldos bancários conciliados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39010701561367)

Para resolver, é necessário estornar a conciliação do lote correspondente antes de tentar cancelar a baixa do título.

Acesse o módulo **Financeiro (SIGAFIN)**;

Vá em **Atualizações > Movimento Bancário > Conciliador Backoffice (CTBA940)**;

Utilize os filtros para localizar a conciliação efetuada (Banco, Agência, Conta e Data);

Identifique o registro com o **Valor Total do Lote** (conforme demonstrado na tabela **SE5**, campo **E5\_LOTE**);

Selecione o movimento e clique em **Outras Ações > Cancelar Match**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39010701562007)

Após a confirmação do cancelamento da conciliação, retorne à rotina de **Baixas Pagar Manual (FINA080)**;

Localize o título desejado e realize o cancelamento da baixa normalmente.

**Saiba mais**

[**Permitir estorno de baixas conciliadas**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409633386391-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA100-Bloquear-estorno-de-movimentos-conciliados)
