---
article_id: 38336024171799
category: SIGAACD - Automação e Coleta de Dados
content_hash: b817f66ebe9ea97a743d6323f6f3451011f813a81d69384eac7560ff62df36c1
fetched_at: '2026-06-28T22:39:12.873357+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - O campo CBC_QUANT
  não digita mais de dois dígitos, como corrigir?
type: support-article
updated_at: '2026-02-11T20:10:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38336024171799-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-O-campo-CBC-QUANT-n%C3%A3o-digita-mais-de-dois-d%C3%ADgitos-como-corrigir
---

O artigo explica que, na rotina de Lançamentos do Inventário (ACDA035) do TOTVS Protheus, o campo de Quantidade (CBC\_QUANT) não permitia digitar dois números devido a um formato incorreto da máscara e do campo. Após ajustar o campo no configurador conforme o padrão nativo do sistema, a funcionalidade foi normalizada.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38335993005975) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Na rotina de Lançamentos do Inventário (ACDA035), quando vou alterar ou incluir algum registro, no campo de Quantidade (CBC\_QUANT) não consigo digitar dois números.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**  
Identificado que no campo CBC\_QUANT o tamanho da máscara e do campo, se encontrava com o formato incorreto, conforme a  imagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38336024157079)

Ao realizar o ajuste no configurador  conforme o nativo do sistema da  imagem abaixo, voltou a funcionar normalmente na rotina de lançamentos do SIGAACD.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38336024157719)

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
