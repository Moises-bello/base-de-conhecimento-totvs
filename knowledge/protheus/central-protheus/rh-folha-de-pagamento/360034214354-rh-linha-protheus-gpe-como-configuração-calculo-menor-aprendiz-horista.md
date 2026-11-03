---
article_id: 360034214354
category: RH - Folha de Pagamento
content_hash: 58b0a9f9059aaf9b447c0685dc683ec60660d62abe66f860417639af934deffa
fetched_at: '2026-06-28T22:44:17.109435+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como configuração calculo Menor Aprendiz Horista
type: support-article
updated_at: '2025-08-22T19:48:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034214354-RH-Linha-Protheus-GPE-Como-configura%C3%A7%C3%A3o-calculo-Menor-Aprendiz-Horista
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34381013834263)  Tempo aproximado para leitura: 00:01:00 min  
  
Dúvida**Como configurar o parâmetro **MV\_MAPREND** para definição de calculo para Menor Aprendiz Horista?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Ao efetuar o cálculo do menor aprendiz horista com o parâmetro **MV\_MAPREND**ativo e o mnemônico **P\_LDSRHRSP** também ativo, o cálculo do menor aprendiz é feito com base nas horas do ponto, porém o mnemônico não deveria ser considerado quando o funcionário é menor aprendiz.  
  
Criado o mnemônico**P\_HRPONAPR** que será utilizado para ignorar o conteúdo do **P\_LDSRHRSP** quando o funcionário for menor aprendiz.  
  
Por padrão o mnemônico é desativado, para que a implementação surta o efeito desejado o mnemônico deverá ser ativado antes de efetuar o cálculo.

**Saiba Mais**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[Conferencia de cálculo quando parâmetro MV\_MAPREND= .T.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020439612-MP-GPE-Como-conferir-o-c%C3%A1lculo-do-jovem-aprendiz-quando-utilizado-o-par%C3%A2metro-MV-MAPREND-T-%C2%A0)
