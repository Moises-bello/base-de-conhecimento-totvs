---
article_id: 4410476266775
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 8faa2dedca6052d5e743118a6f5f6303ed89d0936c3da0b3f43e10ce8e89efe0
fetched_at: '2026-06-28T22:38:43.958370+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT- remessa de de
  ativo imobilizado para uso fora do estabelecimento no Faturamento
type: support-article
updated_at: '2021-10-13T14:14:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410476266775-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-remessa-de-de-ativo-imobilizado-para-uso-fora-do-estabelecimento-no-Faturamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como emitir um nota de remessa de de ativo imobilizado para uso fora do estabelecimento?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT- Todas as versões  
  
**Solução**

No módulo do Faturamento o processo que pode ser efetuado seria como um processo de comodato:

***1 -***Pedido de vendas (**mata410**)***do tipo****N- normal;***

***2-***Informe o cliente para quem se efetuará o empréstimo;

***3***- Informe a condição de pagamento (a informação é necessária,  devido o campo ser obrigatório o preenchimento no pedido de venda);

**4-**Informe o produto na linha item do pedido;

***5-***Informe **um TES (mata080)**que controla **poder de terceiros remessa**, movimentação de ***estoque igual a sim*** ,***não gera financeiro. CFOP 5554, cst icms 41 e cst pis/cofins 49;***

**6**-Confirme o Pedido, libere-o e fature-o.

O que  está em/de poder de terceiros poderá  avaliar diretamente na tabela **SB6** ou pelo relatório do estoque **MATR480** .

Para esse processo não tem um vínculo com o módulo de Ativo Fixo, e no módulo de Ativo não tem operação para geração de notas de remessa.

**Saiba mais sobre remessa e devolução de  poder de terceiros: [FAT0285 - Poder DE/EM Terceiro](https://tdn.totvs.com/x/xyCgGg)**
