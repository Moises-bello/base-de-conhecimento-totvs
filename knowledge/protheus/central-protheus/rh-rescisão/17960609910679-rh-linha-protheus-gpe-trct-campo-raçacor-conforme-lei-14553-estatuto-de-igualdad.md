---
article_id: 17960609910679
category: RH - Rescisão
content_hash: e67498ff785773032ad0c8d4eff1e6de376bb7e3bc4a9fc459ae681ac5f83a53
fetched_at: '2026-06-28T22:43:54.479364+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - TRCT campo raça\cor conforme Lei 14.553 Estatuto
  de Igualdade Racial
type: support-article
updated_at: '2023-10-03T11:28:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17960609910679-RH-Linha-Protheus-GPE-TRCT-campo-ra%C3%A7a-cor-conforme-Lei-14-553-Estatuto-de-Igualdade-Racial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17960651876247) Tempo aproximado para leitura: **01:30 min** **Dúvida**Como imprimir TRCT contendo campo raça\cor conforme Lei 14.553 Estatuto de Igualdade Racial?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**

Conforme a LEI N° 14.553/2023 - TRCT, realizar a inclusão do campo 20.1 - Raça/Etnia nos fontes abaixo:

1. RdMake IMPRESH
2. Padrão GPER1001

Após criado o novo parâmetro:

| Campo | Conteúdo |
| --- | --- |
| Nome da variável (X6\_VAR): | MV\_L14553 |
| Tipo (X6\_TIPO): | Lógico |
| Descrição (X6\_DESCRIC): | Lei N 14.553/2023 impressao da raça/etnia no TRCT |
| Valor Padrão (X6\_CONTEUD): | .F. |

Para impressão do campo, é necessário alterar o conteúdo do novo parâmetro mencionado acima para .T.

Assim que o valor for alterado, a descrição do campo RA\_RACACOR passará a aparecer após o campo 20 "Nome da mãe".

Esta implementação possui alteração de dicionário (SX6), a ser disponibilizado na próxima Expedição Contínua. Alternativamente, é possível efetuar a criação do parâmetro conforme descritivo acima pelo Configurador.

**Exemplo:**

**Parâmetro**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17960581073687)

**TRCT**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17960562471319)

**Saiba mais**Para adquirir maior conhecimento acesse o *link* abaixo:

<https://tdn.totvs.com/pages/releaseview.action?pageId=777269571>
