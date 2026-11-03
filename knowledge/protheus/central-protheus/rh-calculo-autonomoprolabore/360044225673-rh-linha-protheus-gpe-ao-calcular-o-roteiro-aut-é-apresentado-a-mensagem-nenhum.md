---
article_id: 360044225673
category: RH - Calculo Autonomo/Prolabore
content_hash: 83f2b3a01bd6483a1e456b9abf10ed4788644b5c759fc8bfd5256ec48325c481
fetched_at: '2026-06-28T22:43:15.062452+00:00'
product: protheus
section_id: 360011983113
source: central-protheus
title: 'RH - Linha Protheus - GPE - Ao calcular o roteiro AUT é apresentado a mensagem:
  Nenhum Funcionário Processado nessa Requisição'
type: support-article
updated_at: '2025-08-08T11:35:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044225673-RH-Linha-Protheus-GPE-Ao-calcular-o-roteiro-AUT-%C3%A9-apresentado-a-mensagem-Nenhum-Funcion%C3%A1rio-Processado-nessa-Requisi%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25027576994839)** Tempo aproximado para leitura:**00:01:00 min**

**Ocorrência**Ao calcular o roteiro AUT sem lançar nenhuma verba para o funcionário na RGB, existindo salário na SRA, é apresentado a mensagem: Nenhum Funcionário Processado nessa Requisição

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058890174)

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Causa**

Essa mensagem é apresentada uma vez que, o parâmetro **MV\_AUTOSRC**está habilitado.

Com parâmetro AUTOSRC habilitado, sistema só irá calcular a folha caso exista lançamentos para o funcionário.

**Solução**

Para calcular a folha do autônomo com salário na SRA, sem lançar a verba de pagamento, altere o parâmetro **MV\_AUTOSRC = .F.** o Configurador **SIGACFG** em**Ambiente > Cadastros > Parâmetros,** pesquise pelo parâmetro e realize o ajuste. Acesse o sistema novamente e calcule o roteiro AUT.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31945169314839)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31945169323543)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31945198903319)

**Saiba Mais**

[RH - Calculo Autonomo/Prolabore](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983113-RH-Calculo-Autonomo-Prolabore)
