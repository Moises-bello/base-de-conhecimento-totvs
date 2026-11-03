---
article_id: 9628171182231
category: RH - Folha de Pagamento
content_hash: ef05ffc8253f0c5fe6fabf998024346bffc7570c9c11b0737bfb97c19afb53c2
fetched_at: '2026-06-28T22:44:12.152976+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Cancelamento de cálculo - GPEM160
type: support-article
updated_at: '2025-08-13T16:44:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9628171182231-RH-Linha-Protheus-GPE-Cancelamento-de-c%C3%A1lculo-GPEM160
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19441392780055) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Qual o conceito de cancelamento de cálculo através da rotina GPEM160

**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.

**Solução**

A rotina GPEM160 não irá mais efetuar filtro de verba e/ou tipo ao efetuar a exclusão do cálculo de folha, efetuando a exclusão de todos os registros da tabela SRC do funcionário.

Ao fim do processamento, será exibido um log contendo a matrícula de todos os funcionários que tiveram a exclusão do cálculo da folha.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19441392786711)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19441365477399)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19441365483287)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19441365485207)

**Importante:**

Dessa forma, **todas** as verbas geradas na tabela SRC serão excluídas, sendo necessário efetuar o recálculo da folha do funcionário. Trata-se de uma **mudança** de conceito que visa evitar que o cálculo de folha do funcionário fique incorreta.

No entanto, essa mudança aplica-se apenas para a exclusão na tabela SRC; para a exclusão na tabela RGB ou SRK, o conceito antigo permanece, sendo possível excluir apenas uma ou algumas verbas, pois essas tabelas são intermediárias e não são a tabela final de cálculo. No entanto, para que a mudança reflita na folha, ainda sim continuará necessário efetuar o recálculo da folha.

Observe ainda que se na rotina GPEA580 de Lançamentos por Funcionário for efetuado a exclusão manual de uma verba que já foi calculada na folha, será exibido um aviso solicitando que seja efetuado recálculo para que a alteração reflita na folha. E no relatório da folha é possível avaliar divergências entre o líquido apurado e os proventos/descontos.

#### **Saiba Mais:**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

<https://tdn.totvs.com/pages/releaseview.action?pageId=698627791>
