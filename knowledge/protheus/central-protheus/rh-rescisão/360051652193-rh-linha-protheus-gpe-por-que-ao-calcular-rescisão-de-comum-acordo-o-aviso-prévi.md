---
article_id: 360051652193
category: RH - Rescisão
content_hash: 3f489c6fa9d39202065bbb9ce33b87bd55d1e03c00b9496fad44aab7267f24dc
fetched_at: '2026-06-28T22:43:49.841738+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Por que ao calcular rescisão de comum acordo o
  aviso prévio não é considerado pela metade
type: support-article
updated_at: '2025-06-12T12:18:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051652193-RH-Linha-Protheus-GPE-Por-que-ao-calcular-rescis%C3%A3o-de-comum-acordo-o-aviso-pr%C3%A9vio-n%C3%A3o-%C3%A9-considerado-pela-metade
---

**Dúvida**Por que ao calcular rescisão de comum acordo o aviso prévio não é considerado pela metade?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Esse incidente ocorre, porque o preenchimento da tabela S043 para o tipo de rescisão por acordo esta incorreto.  
Para solucionar esse incidente, realize os seguintes passos:  
  
1.Entre na rotina de Manutenção de tabelas pelo caminho **>Atualizações > Definições de Cálculo > Manutenção Tabelas > Tabela S043;**  
A coluna **Aviso Prévio** deve ficar com **A** para o tipo de rescisão por comum acordo, mantendo as mesmas características do Aviso Indenizado, apenas trocando o percentual da multa do FGTS para 20%:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079997633/mceclip0.png)

Foi criado o tipo de aviso prévio “A” para no momento do cálculo de rescisão o sistema calcular 50% dos dias de aviso.   
Exemplo, se o funcionário estiver na empresa por 4 anos, ele teria direito a 42 dias (30 + 12 = 42) de aviso prévio se fosse uma rescisão diferente de comum acordo. No caso de comum acordo serão calculados 21 dias (42 \* 50% = 21).  
  
**Saiba Mais:**

Para adquirir maior conhecimento acesse o *link* abaixo:

[MP - GPE - Como efetuar um cálculo de rescisão por acordo?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025690513-MP-GPE-Como-efetuar-um-c%C3%A1lculo-de-rescis%C3%A3o-por-acordo-?source=search)

[RH - Linha Protheus - GPE - Como parametrizar a tabela S043 para cadastrar um novo tipo de rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004395831-RH-Linha-Protheus-GPE-Como-parametrizar-a-tabela-S043-para-cadastrar-um-novo-tipo-de-rescis%C3%A3o?source=search)
