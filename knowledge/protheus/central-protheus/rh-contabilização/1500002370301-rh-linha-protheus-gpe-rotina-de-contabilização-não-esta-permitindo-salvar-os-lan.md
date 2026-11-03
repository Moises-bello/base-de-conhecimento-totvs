---
article_id: 1500002370301
category: RH - Contabilização
content_hash: cc7d6aa44bd2066f1644e90ff0c53576db303be96ea4cec144d8088439e46488
fetched_at: '2026-06-28T22:43:46.050104+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Rotina de Contabilização não esta permitindo salvar
  os Lançamentos Contábeis
type: support-article
updated_at: '2025-07-31T19:04:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002370301-RH-Linha-Protheus-GPE-Rotina-de-Contabiliza%C3%A7%C3%A3o-n%C3%A3o-esta-permitindo-salvar-os-Lan%C3%A7amentos-Cont%C3%A1beis
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33856714004887)** Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**Depois de preencher todos os parâmetros para geração da **Contabilização**, os dados são apresentados em tela, mas não permite salvar os lançamentos para que eles sejam integrados no **módulo SIGACTB** ou exportados em arquivo de texto.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Causa**O sistema não está permitindo salvar os dados pois existe a falta e/ou informações incorretas nos dados contabilizados, exemplo **Centro de Custo**, **Item Contábil** ou **Classe de Valor** obrigatório.

Par que estes ***Helps*** sejam apresentados é necessário habilitar o conteúdo do parâmetro **MV\_CT105MS** **para S,** desta forma será demonstrado em tela o motivo pelo qual os dados contabilizados não estão sendo salvos, permitindo que seja efetuado o ajuste.  
  
**Solução**Para resolver essa questão altere o conteúdo dos parâmetros **MV\_CT105MS** e **MV\_ALTLCTO** para S:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33856735922199)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33856735926423)

**Saiba Mais**  
[Artigos Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)
