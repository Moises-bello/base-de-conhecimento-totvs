---
article_id: 37479306273047
category: Financeiro - Baixas a Receber
content_hash: 0a5299fb1c6c60468b3c8da07609b1a0965723ea634c418891ca6486c4fea7fa
fetched_at: '2026-06-28T22:37:43.830652+00:00'
product: protheus
section_id: 33820269506967
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Help FIN62003 ao tentar
  baixar título
type: support-article
updated_at: '2026-01-06T17:45:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37479306273047-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Help-FIN62003-ao-tentar-baixar-t%C3%ADtulo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37479306267799) Tempo aproximado para leitura: 04**:00 min**

**Dúvida:**  
Ao tentar realizar a baixa de um título no módulo Financeiro, o sistema apresenta a mensagem de erro: "FIN62003"

**Ambiente:**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - 12.1.33 e superiores

**Solução:**

Este incidente ocorre quando o título selecionado para baixa possui um processo **solicitação de transferência entre filiais** (FINA621 ou FINA620) iniciado, mas ainda não concluído (pendente).

No Protheus, enquanto houver uma solicitação de transferência ativa, o título fica bloqueado para movimentações de qualquer tipo (baixas, exclusões) na filial de origem para garantir a integridade.

![novo fina621.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/37479293514775)

Para resolver, siga as orientações abaixo:

1. Acesse a rotina de **solicitação de transferência entre filiais** **(**FINA621 ou FINA620**)**;
2. Verifique a **legenda** do título em questão. Caso ele esteja identificado com a cor **Vermelha**, confirma-se que há uma transferência entre filiais pendente;
3. Acesse a **filial de destino** (filial para a qual o título está sendo transferido);
4. Aprove ou rejeite a transferência para que seja possivel continuar com a movimentação do título.

![Sem nome (1908 x 898 px) (1).gif](https://centraldeatendimento.totvs.com/hc/article_attachments/37479873281047)
