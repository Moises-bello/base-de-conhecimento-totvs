---
article_id: 1500010132622
category: Meu RH - Ponto
content_hash: 7a5f1bcad7dc34a0b174a8cb60897f930e3691225a1978ce50e3fed048fa2f96
fetched_at: '2026-06-28T22:47:30.372141+00:00'
product: rm
section_id: 1500000861782
source: central-rm
title: RH - RM - Meu RH - Informar a descrição do abono no relatório do espelho de
  ponto
type: support-article
updated_at: '2025-09-12T19:22:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010132622-RH-RM-Meu-RH-Informar-a-descri%C3%A7%C3%A3o-do-abono-no-relat%C3%B3rio-do-espelho-de-ponto
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:02:56 min****Dúvida**Como informar a descrição do abono no relatório do espelho de ponto?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir da versão 12.1.27

**Solução**Para gerar o relatório é necessário que a estrutura do mesmo esteja parametrizada no grupo de quiosque associado aos funcionários desejados:  
**Automação de Ponto |  Configurações |  Parametrizador | RM Portal |  Espelho funcionário | Código do Relatório**:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500015859902/mceclip1.png)

Para que a estrutura seja disponibilizada no campo citado acima, é necessário que na sua estrutura o campo **Tipo** esteja parametrizado com o tipo **181**, como na imagem a seguir:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500015860862/mceclip2.png)  
  
É recomendado  que se crie e salve um perfil de parâmetros com o nome " **MeuRH**" na geração de relatórios com os  parâmetros que deseje que sejam aplicados na geração do relatório utilizando o app Meu RH.  
**Automação de Ponto |  Relatórios |  Espelho do Cartão |**

![](https://totvssuporte.zendesk.com/attachments/token/E5mS1ktMYZT8OwU5vE0X3jHAX/?name=inline1601044054.png)​  
  
![](https://p23.zdusercontent.com/attachment/888110/Y3DogPP09j99thmnJMI2zg0o3?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..JSinnmGzqVs_TjpQmTx61w.sJN6Xp5dTwCR1-T00JH_xengmtiK7I8kRoLbD9pSBtZkJ1rh_EqBIMOimbQbZxTE6map-W_7N-uwlJKlO7BGZdLx_9YIcYJSjYcZrXO0Dy98kpXMGT3ZZHGfcQh4F5tI6a1t0wxCHgF2F3dftm2zRQLopKqHHVLj01p3Ug_opnJmJTb_tc271SL9YeTvdrFPwDX1iX247UvF2JUypASCPliuxnaeQ70UHLPc679cWdM6MOid7GyqitvR8MxNmzL4TgB_woIeNsTWLwZYdK8GuSHLOQYN2D-e1IoDOuHv9wA.2sXxSE549BHg2lQ9iGK2pw)

Para que as descrições do abono sejam apresentadas no relatório o parâmetro abaixo tem que esta marcado no perfil salvo para geração do relatório​.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500016144881/mceclip0.png)

Após a parametrização ao gerar o relatório as informações devem aparecer ao gerar o relatório.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500016985941/mceclip0.png)

**Saiba Mais**

[Consultar Espelho Ponto](https://tdn.totvs.com/display/public/NPR/8.0++Consultar+Espelho+Ponto)
