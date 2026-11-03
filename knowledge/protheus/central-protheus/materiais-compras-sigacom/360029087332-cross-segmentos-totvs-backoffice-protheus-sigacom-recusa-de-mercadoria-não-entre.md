---
article_id: 360029087332
category: Materiais - Compras (SIGACOM)
content_hash: 8ce0137b87d8ff12bb930428531a58a2dc123e0381a95df7a3006854301d6632
fetched_at: '2026-06-28T22:41:24.358103+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Recusa de Mercadoria
  não Entregue - Processo do módulo Compras
type: support-article
updated_at: '2022-07-14T12:06:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029087332-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Recusa-de-Mercadoria-n%C3%A3o-Entregue-Processo-do-m%C3%B3dulo-Compras
---

**Dúvida**

Recusa de Mercadoria não Entregue - Processo do módulo Compras

**Ambiente**  
Protheus – Comptas – A partir da versão 12  
  
**Solução**

Recusa de mercadoria por parte do cliente, no qual o Emitente deverá realizar a inclusão de recebimento da recusa utilizando CFOP 1.201/2.201 - devolução de venda de produção do estabelecimento; e (ii) 1.410/2.410 - devolução de venda de produção do estabelecimento em operação com produto sujeito ao regime de substituição tributária. Bem como incluindo seus dados de Emitente como Destinatário.

Na devolução de mercadoria não entregue ao destinatário *(em atendimento ao Artigo 453, I, do RICMS/2000 SP*) será considerado os dados do próprio estabelecimento como destinatário (ao invés do cliente padrão da nota) quando o campo "*F1\_DEVMERC*" for informado com S – Sim.  
O campo "*F1\_DEVMERC*" ficará habilitado para seleção somente para notas de devolução com formulário próprio = Sim.

Exemplo do processo Rejeição de mercadoria não entregue:

O campo **F1\_DEVMERC** deve existir no **SX3** da tabela **SF1**- Cabeçalho da Nota Fiscal de Entrada:

|  |  |
| --- | --- |
| **Campo** | F1\_DEVMERC |
| **Tipo** | C |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Dev.merc.n.r |
| **Descrição** | Devol. merc. não recebida |
| **Nível** | 1 |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Opções** | S=Sim;N=Não |
| **Val. Sistema** | Pertence(" SN") |
| **Help** | Campo utilizado para identificar se é uma devolução de mercadoria que não foi entregue ao destinatário em atendimento ao Artigo 453, I, do ICMS/2000 SP. |

1 - No módulo SIGACOM, acesse Atualizações > Movimentos > Documento de Entrada (*MATA103*), clique em Ações Relacionadas > Retornar.

2 - Na tela de parâmetros para seleção da nota de saída, informe o código do cliente, a data de saída da nota e clique em Ok.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030722172/mceclip0.png)

3 - Selecione a nota de venda cuja mercadoria não foi recebida pelo cliente e clique em Retornar. O sistema apresenta a nota de devolução para confirmação.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030722352/mceclip1.png)

4 - Certifique-se de que o campo Formulário Próprio está informado como **SIM** e clique na aba *Informações* *DANFE*. Preencha o campo **Merc.não entregue (F1\_DEVMERC)** com **SIM**.

Confira os dados e confirme a inclusão da nota de devolução com formulário próprio.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030691151/mceclip2.png)

6 - No módulo SIGAFAT, acesse Atualizações > Faturamento > Nfe Sefaz (*SPEDNFE*).

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030723032/mceclip3.png)

8 - Transmita a nota de devolução em Ações Relacionadas > Transmissão.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030723112/mceclip4.png)

9 - Após a autorização da nota, imprima o DANFE e observe no quadro DESTINATÁRIO / REMETENTE que os dados lá informados são os dados do próprio emitente.

Parecer da Consultoria de segmentos:<http://tdn.totvs.com/pages/releaseview.action?pageId=269448809>
