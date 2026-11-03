---
article_id: 360040971753
category: Ativo Fixo - Transferência
content_hash: 6190e67fba1768df5273987872bb6f948dc8e129d806d2f8214d7fabd7a229f9
fetched_at: '2026-06-28T22:41:52.137571+00:00'
product: protheus
section_id: 1500001536061
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA060 -  TRANSFERÊNCIA
  DE ATIVOS NÃO PREENCHE CAMPOS DO GRUPO DESTINO (FN9_GRPDES) (FNR_GRPES)
type: support-article
updated_at: '2022-07-18T14:46:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040971753-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA060-TRANSFER%C3%8ANCIA-DE-ATIVOS-N%C3%83O-PREENCHE-CAMPOS-DO-GRUPO-DESTINO-FN9-GRPDES-FNR-GRPES
---

**Ocorrência**

Na execução da rotina de transferência (ATFA060)  os campos correspondentes ao grupo destino não são preenchidos.

**Ambiente**Protheus  – Ativo Fixo  – A partir da versão 12  
  
**Causa**

Este campo não é preenchido para que não ocorram os seguintes efeitos colaterais:

* Um ambiente onde a tabela de Grupo de Bens (FNG) está exclusiva entre empresa/filial, ao efetuar uma transferência, se houver gatilho, o grupo do bem de destino pode não existir na filial de destino e/ou o grupo do bem de destino pode não ter as mesmas características da filial de destino.

Desta forma, afim de atender todos os cenários, o campo Grupo de Bens Destino **não será preenchido**ao executar-se uma transferência.

**Solução**

Caso seja necessário o preenchimento dos campos destino na transferencia , como sugestão pode ser criado um gatilho customizado.

Linkk referente aos campos Grupo de Bens na Transferência

<https://tdn.totvs.com/pages/releaseview.action?pageId=517122324>
