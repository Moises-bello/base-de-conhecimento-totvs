---
article_id: 8133280226199
category: Meu RH - Ponto
content_hash: 4b8df537633c8086de7a9f7f3e1b03e549c80e580539f127227d845840e24b6e
fetched_at: '2026-06-28T22:47:30.300099+00:00'
product: rm
section_id: 1500000861782
source: central-rm
title: RH - RM - Meu RH - Só é possível realizar alterações em determinado dia ao
  solicitar abono
type: support-article
updated_at: '2025-02-03T19:18:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8133280226199-RH-RM-Meu-RH-S%C3%B3-%C3%A9-poss%C3%ADvel-realizar-altera%C3%A7%C3%B5es-em-determinado-dia-ao-solicitar-abono
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24085179126423) Tempo aproximado para leitura: **00:02:17 min****Ocorrência**Ao tentar solicitar um abono é apresentado a mensagem: **É possível realizar alterações somente a partir do dia [...]**  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) – Meu RH – Todas versões  
  
**Causa**Essa mensagem é apresentada quando a data da inserção foge das registradas no período e quando o seu sistema está configurado para validar o período futuro como ativo.  
  
**Solução**Caso a mensagem seja apresentada e queria alterar a parametrização e não trabalhar com período futuro, siga os passos abaixo:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8130013481623)

1. Vá em Automação de Ponto > Configurações > Parametrizador > 08.04 RM Portal > "Edite o grupo de acesso do usuário em questão" > Período, e desmarque a flag

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8130619507223)

2. Na mesma tela, mude para a aba "Gestão por Escala" e verifique a opção selecionada

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8130421447063)

Período de alteração:

* **A partir da data atual:** Irá considerar a data atual e as datas futuras.
* **A partir do período ativo:**  Irá considerar o período atual e os períodos futuros.

**Saiba mais**

[**Gestão por Escala**](https://tdn.totvs.com/pages/releaseview.action?pageId=452718997)

[**Período PTO**](https://tdn.totvs.com/pages/releaseview.action?pageId=452719997)
