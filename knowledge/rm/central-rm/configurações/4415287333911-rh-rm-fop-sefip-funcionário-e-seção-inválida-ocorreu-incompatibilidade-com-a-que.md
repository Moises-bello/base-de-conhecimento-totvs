---
article_id: 4415287333911
category: Configurações
content_hash: 533b287e68285527e4b3cecf99444badff926b8659df0ca5688bec97ab5f8783
fetched_at: '2026-06-28T22:46:49.551231+00:00'
product: rm
section_id: 1500000834621
source: central-rm
title: 'RH - RM - FOP - SEFIP: Funcionário e Seção inválida. Ocorreu incompatibilidade
  com a Quebra de CNPJ'
type: support-article
updated_at: '2024-10-11T20:50:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415287333911-RH-RM-FOP-SEFIP-Funcion%C3%A1rio-e-Se%C3%A7%C3%A3o-inv%C3%A1lida-Ocorreu-incompatibilidade-com-a-Quebra-de-CNPJ
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:50 min****Duvida**Como corrigir o erro Funcionário XXXXX - Seção XXXXX inválida. Ocorreu incompatibilidade com a Quebra de CNPJ?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para a correção do erro apresentado, é necessário verificar se a máscara do código de quebra mestre corresponde ao número de caracteres informados em sua máscara de código de seção, como no exemplo abaixo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10988348607639)  
  
Ao gerar a SEFIP com a máscara dessa forma, o sistema apresentará o seguinte erro:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415286150551/mceclip1.png)  
  
Para que o processo seja gerado sem este erro, é necessário que faça a alteração no Parametrizador. Acesse a aba **Configurações | Parametrizador | RH - Máscaras e Quebras:**  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10988435934359)  
  
Altere para que fique conforme os **exemplos** abaixo:  
  
Máscara código de seção **##.####.####### = 15 caracteres**  
Código de quebra mestre: **??????????????? = 15 caracteres**Máscara código de seção: **##.## = 5 caracteres**Código de quebra mestre: **????? = 5 caracteres**Após esta alteração, execute a Liberação da Flags e gere a SEFIP novamente.

**Outra proposta de solução é verificar se existe alguma seção que esteja em uso desativada. Caso exista ative a mesma e execute o processo.   
  
Importante**Note que a quantidade de caracteres e máscara conforme descrito acima são apenas exemplos. O que deverá contar é que a quantidade de caracteres em ambas seja a mesma. Além disso, antes de aplicar quaisquer alterações de máscara em seu sistema, teste a alteração primeiramente em uma base de homologação.   
  
**Saiba mais**  
[RH - RM - FOP - Liberação de Flags de FGTS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415143205143-RH-RM-FOP-Libera%C3%A7%C3%A3o-de-Flags-de-FGTS?source=search)
