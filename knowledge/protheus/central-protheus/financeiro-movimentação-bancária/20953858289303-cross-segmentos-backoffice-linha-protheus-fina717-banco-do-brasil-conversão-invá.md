---
article_id: 20953858289303
category: Financeiro - Movimentação Bancária
content_hash: 6f950241892c6f3554d885dcbb05d1383a50af8734bfe943bee5e231b71fd709
fetched_at: '2026-06-28T22:38:19.420708+00:00'
product: protheus
section_id: 1500001550402
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - FINA717 - Banco do Brasil -
  Conversão inválida: valor não pode ser representado no tamanho definido'
type: support-article
updated_at: '2024-01-30T14:36:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20953858289303-Cross-Segmentos-Backoffice-Linha-Protheus-FINA717-Banco-do-Brasil-Convers%C3%A3o-inv%C3%A1lida-valor-n%C3%A3o-pode-ser-representado-no-tamanho-definido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20953874547351) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**No módulo Financeiro, ao tentar realizar o registro de pagamentos via API para o Banco do Brasil, é apresentado retorno com erro, e ao exportar e converter o JSON, a mensagem **"Conversão inválida: valor não pode ser representado no tamanho definido"** é apresentada no retorno do banco.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões a partir da release 2210  
  
**Causa**  
Esse incidente ocorre, pois o número da agência está sendo informada com 5 ou mais dígitos.  
O campo agência permite no máximo 4 dígitos. *Por padrão, a agência é informada sem o dígito.*

**Solução**

**Através da rotina FINR130(Parâmetros de Banco), altere os campos abaixo **EE\_AGEOFI, EE\_CTAOFI e EE\_DVCTOFI** e atribua os respectivos conteúdos corretamente, conforme informações do seu banco.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/20953858241687)**

**Saiba mais:**

[Banco do Brasil - Configuração pagamentos](https://tdn.totvs.com/pages/viewpage.action?pageId=734394173)
