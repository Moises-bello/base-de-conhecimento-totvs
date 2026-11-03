---
article_id: 23458043220887
category: SIGAEST - MOVIMENTAÇÕES
content_hash: b44e559c72f69c98556671efed78fdba42770ad82a24936166bd4e04416ba1f3
fetched_at: '2026-06-28T22:38:56.990544+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA241 campo D3_LOCALIZ
  não permite indicar a Localização quando efetuado Devolução de Saldo
type: support-article
updated_at: '2025-03-12T12:27:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23458043220887-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA241-campo-D3-LOCALIZ-n%C3%A3o-permite-indicar-a-Localiza%C3%A7%C3%A3o-quando-efetuado-Devolu%C3%A7%C3%A3o-de-Saldo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23458043210775) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**

Ao incluir Devolução de Saldo pela rotina MOVIMENTOS INTERNOS (MATA241), não permite indicar a Localização, ***o campo D3\_LOCALIZ*** fica em branco mesmo digitando a Localização manualmente.

![PRINT 01.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/23458675938711)

![PRINT 02.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/23458675942935)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

Nesse cenário não se trata de erro,  no padrão é necessário após a inclusão da Devolução de Saldo a utilização da rotina **ENDEREÇAMENTO DE PRODUTO (MATA265)** para informar a destinação das Localizações dos produtos.

**Dica:** Somente na rotina Documento de Entrada (MATA103) utilizando o **parâmetro MV\_DISTMOV** que quando ativo, abrirá a tela para distribuição da quantidade de entrada em endereços/números de série, logo após a confirmação da inclusão de entrada, faturas de entrada, remito de entrada ou apontamento de produção. Veja a FAQ abaixo.  
  
[**Backoffice (Linha Protheus) - SIGAEST - Como endereçar Produto diretamente da rotina de Documento de Entrada "automaticamente"?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021637231-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-endere%C3%A7ar-Produto-diretamente-da-rotina-de-Documento-de-Entrada-automaticamente?source=search)  
  
Outra opção também é para os casos de endereçamento automático no Controle de Qualidade com o parâmetro MV\_DISTAUT, veja na FAQ abaixo sobre esse cenário.  
  
[**Backoffice (Linha Protheus) - SIGAEST - Armazém CQ endereçar automaticamente - MV\_DISTAUT - Como configurar?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10668896901015-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Armaz%C3%A9m-CQ-endere%C3%A7ar-automaticamente-MV-DISTAUT-Como-configurar?source=search)

**Saiba Mais:**

*[Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
