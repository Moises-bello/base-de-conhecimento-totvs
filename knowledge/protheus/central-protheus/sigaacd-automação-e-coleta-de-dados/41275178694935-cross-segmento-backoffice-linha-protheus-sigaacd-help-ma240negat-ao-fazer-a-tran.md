---
article_id: 41275178694935
category: SIGAACD - Automação e Coleta de Dados
content_hash: 1601f0d15f76c0ef842f20d6530d444730a7db2112a09441c0495c735b1833dc
fetched_at: '2026-06-28T22:39:12.739342+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Help MA240NEGAT ao
  fazer a transferência usando o meu Coletor de Dados
type: support-article
updated_at: '2026-06-16T20:10:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41275178694935-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Help-MA240NEGAT-ao-fazer-a-transfer%C3%AAncia-usando-o-meu-Coletor-de-Dados
---

O erro HELP MA240NEGAT ocorre no Aplicativo Meu Coletor de Dados ao realizar transferências devido à configuração incorreta do campo B1\_QE (Embalagem do Produto) no cadastro. Para resolver, deve-se deixar esse campo em branco, pois a rotina não trata embalagens configuradas. A funcionalidade já foi implementada para inventário guiado.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41275178675351) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Ao fazer uma transferência no Aplicativo Meu Coletor de Dados, apresenta o HELP MA240NEGAT e não conclui a transferência.   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41275178678295)  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.

**Causa**  
Esse incidente ocorre, pois a parametrização do sistema está incorreta ao configurar o campo B1\_QE no cadastro do produto e apresenta o Help MA240NEGAT.   
  
**Solução**  
No momento que realiza a transferência usando o aplicativo Meu Coletor de Dados, apresenta o HELP MA240NEGAT, o motivo por aparecer essa mensagem seria o cadastro do produto, ter configurado o campo B1\_QE (Embalagem do Produto), por nativo do sistema a rotina de transferência no aplicativo não tem tratativa para uso de campo de embalagem configurada.

Para não exibir mais a mensagem é necessário deixar o campo de embalagem em branco, no campo B1\_QE.

Essas informações apresenta no [Guia do Meu Coletor de Dados](https://tdn.totvs.com/pages/releaseview.action?pageId=506994322):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41275147974551)

Essa funcionalidade já foi implementada no inventário, usando o aplicativo:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Quantidade por Embalagem Inventário Guiado.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/40497415797271-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Quantidade-por-Embalagem-Invent%C3%A1rio-Guiado)

**Saiba Mais:**

[*Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
