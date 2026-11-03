---
article_id: 38329085934103
category: Financeiro - Conciliação de Vendas
content_hash: 4ab51dc4abc37ab60813dc2088e646e0e854045bcfc91de72f7da6dc4126ae3d
fetched_at: '2026-06-28T22:37:26.273974+00:00'
product: protheus
section_id: 35058743504791
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA918 - Comportamento
  do título após cancelamento de baixa via FINA070 e nova conciliação via FINA918
type: support-article
updated_at: '2026-02-11T19:01:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38329085934103-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA918-Comportamento-do-t%C3%ADtulo-ap%C3%B3s-cancelamento-de-baixa-via-FINA070-e-nova-concilia%C3%A7%C3%A3o-via-FINA918
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38329085917847) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Qual o comportamento e o status de um título no Protheus após realizar o cancelamento de sua baixa pela rotina FINA070 e processar uma nova conciliação/baixa através da rotina FINA918 (Conciliador de Pagamentos)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**

A rotina **FINA918 (Conciliação de Pagamentos)** não dispõe, nativamente, de uma funcionalidade para "desconciliar" um registro.

Quando ocorre o cancelamento de uma baixa efetuada pelo conciliador através da rotina **FINA070 (Baixas a Receber)**, o sistema executa os seguintes processos:

1. **Reabertura do Título:** O título no **Contas a Receber (SE1)** retorna ao status de aberto.
2. **Liberação na** **Tabela FIF****:** O registro correspondente na tabela **FIF (Conciliação de Pagamentos)** é reaberto, permitindo que o operador realize uma nova conciliação e, consequentemente, uma nova baixa pelo processo do conciliador.

Ao final do reprocessamento, o título assumirá a posição de baixado conforme os novos parâmetros da conciliação efetuada.

Segue print de exemplo de processo de cancelamento e nova conciliação/baixa via **conciliador TEF**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38329085918103)

**Saiba Mais**

* [FINA918 - Conciliação de Pagamentos](https://tdn.totvs.com/pages/releaseview.action?pageId=655196877)
