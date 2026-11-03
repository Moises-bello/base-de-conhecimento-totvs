---
article_id: 23088022363543
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 57f1a82557aa669e46593ecba7488f6f30c53127e2a11e251dd49edd6fb3b9d6
fetched_at: '2026-06-28T22:38:57.206158+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MV_VLDDOC funcionalidade
  do parâmetro
type: support-article
updated_at: '2025-03-12T12:18:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23088022363543-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MV-VLDDOC-funcionalidade-do-par%C3%A2metro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23088022345367) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**

Qual a funcionalidade do **parâmetro MV\_VLDDOC**, sendo que no padrão **não é permitido** número de Movimentos Internos (SD3) pelas rotinas que populam o **campo D3\_DOC**?

![MV_VLDDOC.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/23088621522711)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**

Ao incluir movimentações de Saldos Internos (MATA241, MATA261, MATA250, etc.) é gerado um número de Documento automaticamente pela função interna **[NEXTNUMERO](https://tdn.totvs.com/x/0Pxn)**, não é permitido a inclusão de **Documentos Internos (D3\_DOC)** **repetidos**.

Para controlar esse cenário é possível de duas formas com o **parâmetro MV\_VLDDOC**, veja abaixo:

|  |
| --- |
| **MV\_VLDDOC = S (Sim)** |

Com o **parâmetro habilitado**, no momento da inclusão apresenta o **HELP D3\_DOC** e impede a continuação da Digitação do Documento, **obrigando ajustar a numeração do Documento** antes de efetuar as digitações.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23088510640663)

|  |
| --- |
| **MV\_VLDDOC = N (Não)** |

Com o **parâmetro desabilitado**, permite incluir todas as linhas de itens ou movimentações, Salvar o Documento e **efetua o ajuste automaticamente do número de Documento** com o sequencial correto do campo **D3\_DOC**, veja o exemplo do print abaixo após a inclusão do saldo .

![D3_DOC 2.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/23090511780119)

![A240DOC.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/23089824598935)

|  |
| --- |
| **Observações importantes:** O campo D3\_DOC é aberto para alteração manual do registro, o que pode comprometer a ordenação dos documentos, caso algum usuário digitar um Documento com uma **numeração superior a existente**.    É possível pelo módulo Configurador **alterar a Propriedade do campo D3\_DOC** para **Visualizar**. |

![D3_DOC CFG.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/23089979754391)

***Saiba Mais:***

*[Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*

*[SIGAEST - Descontinuação da rotina MATA240](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7923335642903-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Descontinua%C3%A7%C3%A3o-da-rotina-MATA240)*
