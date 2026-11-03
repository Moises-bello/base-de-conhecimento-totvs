---
article_id: 21251682512919
category: SIGAEST - SALDOS
content_hash: c598802f6d0f96fa8f319b91caddc28d50efa278240fabd829771a1bb89ba9a1
fetched_at: '2026-06-28T22:39:14.797854+00:00'
product: protheus
section_id: 1500001538801
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - B2_SALPEDI - Quantidade
  de Entrada Prevista Negativa
type: support-article
updated_at: '2025-03-12T12:22:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21251682512919-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-B2-SALPEDI-Quantidade-de-Entrada-Prevista-Negativa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21251682499479) Tempo aproximado para leitura: **00:02:27 min** **Dúvida**O que fazer para corrigir quando o B2\_SALPEDI - Quantidade de Entrada Prevista está negativo

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**A Quantidade de Entrada Prevista, assim como os demais empenhos e acumulados de um produto, são saldos quantitativos que em suma não foram concebidos para se ter saldos negativos.

**Se tratando do B2\_SALPEDI, é o campo que é alimentado mediante:**

* Quantidade prevista por Pedido de compras;
* Solicitação de Compra;
* Transferências entre Filiais pela rotina MATA311 em aberto;
* Ordem de Produção em aberto.

**O que fazer quando o Saldo desse campo está negativo?**

O primeiro passo é entender, por meio das rotinas origens que geram saldo nele, baseando-se no produto em questão, se houve algum processo de pedido de compras, solicitação de compras, transferência entre filiais de uma quantidade errônea.

Um relatório pode ser utilizado de apoio para conferência do saldo são os relatórios MATR440 e MATR290. Exemplo abaixo:

![QTD_ENTPREV.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21251682500631)

Não havendo diagnostico de rotina que tenha gerado saldo negativo no campo B2\_SALPEDI, recomendamos validar internamente a possibilidade de executar a rotina Refaz Empenhos (MATA215) em modo exclusivo. Esta rotina prevê refazer todos os empenhos (não só o B2\_SALPEDI) de todos os produtos conforme as rotinas que originaram os saldos. Se for um saldo inconsistente, o previsto é que o negativo seja limpo.

Se persistir mesmo processando, é recomendável ser aberto um chamado no Suporte Técnico munido das evidências dessas validações documentadas para avaliação.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011930291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR900-Como-configurar-corretamente-o-relat%C3%B3rio-Kardex-para-an%C3%A1lise-de-Custos-e-Movimenta%C3%A7%C3%B5es#:~:text=Saiba%20mais%3A,Custos%20no%20Estoque)*
