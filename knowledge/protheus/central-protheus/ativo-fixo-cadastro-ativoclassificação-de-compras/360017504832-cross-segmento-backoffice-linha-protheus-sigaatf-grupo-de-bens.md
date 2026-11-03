---
article_id: 360017504832
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: e9059860242f56ff2b1d6ee1737fe25f5a58eaf6a1ba08797ac4b7bd4577c4ef
fetched_at: '2026-06-28T22:41:48.420819+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - Grupo de Bens
type: support-article
updated_at: '2023-12-26T20:50:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017504832-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-Grupo-de-Bens
---

**Dúvida**Classificação dos bens oriundos de documento de entrada.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Ativo Fixo - Todas as versões  
  
  
**Solução**

O campo **Grupo de Bens (N1\_GRUPO)** na classificação do documento de entrada (ATFA240), ou na inclusão manual (ATFA012) tem como intuito, facilitar o preenchimento dos dados contábeis do ativo gerado na inclusão do documento de entrada.

Ao utiliza-lo, ele possui os seguintes comportamentos:

* **Sobrepõe** - altera os dados do ativo com os dados presentes no cadastro do grupo;

* **Sem Efeito** - quando o campo no cadastro do grupo estiver em branco a rotina manterá o que veio da NF.

Exemplo prático:

Cadastro do grupo de bens:

| Conta Contábil | Item Contábil | Classe de Valor | Centro de Custo |
| --- | --- | --- | --- |
| 1.2.1.1 | 001 | 001 | [EM BRANCO] |

Ativo gerado pelo documento de entrada:

| Conta Contábil | Item Contábil | Classe de Valor | Centro de Custo |
| --- | --- | --- | --- |
| [EM BRANCO] | 002 | [EM BRANCO] | 01 |

No momento da classificação:

Ao selecionar o grupo informado anteriormente, a rotina irá preencher a conta contábil, o item e a classe de valor de acordo com o que esta no cadastro do grupo de bens, para o centro de custo como no cadastro do grupo não foi informado nenhuma informação ele não será alterado na classificação, ou seja manterá a informação que veio da NF.

Resultado do ativo na classificação ao preencher o campo Grupo de Bens:

| Conta Contábil | Item Contábil | Classe de Valor | Centro de Custo |
| --- | --- | --- | --- |
| 1.2.1.1 | 001 | 001 | 01 |

**Importante:**

O cadastro do grupo é apenas um facilitador, após o preenchimento dos campos, o usuário poderá edita-los, caso seja necessário.

**Observação:**

*Caso seja necessário alterar o grupo informado no bem, utilize a rotina de transferência.*

*A rotina tem opção de realizar a transferência para outro grupo, conforme imagem que segue.*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20128319709207)

Saiba Mais:

[Linha deletada Classificação do ativo](https://tdn.totvs.com/pages/releaseview.action?pageId=497920647)
