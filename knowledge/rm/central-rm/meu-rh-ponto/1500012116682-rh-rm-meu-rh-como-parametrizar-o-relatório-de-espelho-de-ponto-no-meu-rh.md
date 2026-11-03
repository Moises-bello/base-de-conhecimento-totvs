---
article_id: 1500012116682
category: Meu RH - Ponto
content_hash: c8e242ed459d3c97347519b9ea5597de9abcd2c6e19dfd5df5bd7a95cad529e9
fetched_at: '2026-06-28T22:47:30.367601+00:00'
product: rm
section_id: 1500000861782
source: central-rm
title: RH - RM - Meu RH - Como parametrizar o relatório de espelho de ponto no Meu
  RH
type: support-article
updated_at: '2025-01-20T19:52:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012116682-RH-RM-Meu-RH-Como-parametrizar-o-relat%C3%B3rio-de-espelho-de-ponto-no-Meu-RH
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:02:56 min**

**Dúvida**Como parametrizar o relatório de espelho de ponto no Meu RH?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir da versão 12.1.28  
  
**Solução**Para gerar o relatório é necessário que a estrutura do mesmo esteja parametrizada no grupo de quiosque associado aos funcionários desejados:  
  
**Automação de Ponto |  Configurações |  Parametrizador | RM Portal |  Espelho funcionário | Código do Relatório**:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500015859902/mceclip1.png)  
  
Para que a estrutura seja disponibilizada no campo citado acima, é necessário que na sua estrutura o campo **Tipo** esteja parametrizado com o tipo **181**, como na imagem a seguir:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500015860862/mceclip2.png)  
  
É necessário criar um perfil de parâmetros com o nome " **MeuRH**" na geração de relatórios com os  parâmetros desejados para que sejam aplicados na geração do relatório utilizando o app Meu RH.  
**Automação de Ponto |  Relatórios |  Espelho do Cartão |**![](https://totvssuporte.zendesk.com/attachments/token/E5mS1ktMYZT8OwU5vE0X3jHAX/?name=inline1601044054.png)​  
  
![](https://p23.zdusercontent.com/attachment/888110/Y3DogPP09j99thmnJMI2zg0o3?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..JSinnmGzqVs_TjpQmTx61w.sJN6Xp5dTwCR1-T00JH_xengmtiK7I8kRoLbD9pSBtZkJ1rh_EqBIMOimbQbZxTE6map-W_7N-uwlJKlO7BGZdLx_9YIcYJSjYcZrXO0Dy98kpXMGT3ZZHGfcQh4F5tI6a1t0wxCHgF2F3dftm2zRQLopKqHHVLj01p3Ug_opnJmJTb_tc271SL9YeTvdrFPwDX1iX247UvF2JUypASCPliuxnaeQ70UHLPc679cWdM6MOid7GyqitvR8MxNmzL4TgB_woIeNsTWLwZYdK8GuSHLOQYN2D-e1IoDOuHv9wA.2sXxSE549BHg2lQ9iGK2pw)

Acessando o App Meu RH, o download do espelho de ponto pode ser feito clicando no ícone ![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019281042/mceclip3.png).

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019302962/mceclip0.png)

Acessando o Meu RH pelo navegador web, o download do espelho de ponto pode ser feito clicando no ícone ![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019281042/mceclip3.png).

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019281902/mceclip4.png)

O relatório do espelho do ponto é gerado em arquivo formato PDF, sendo possível as seguintes ações:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019282182/mceclip6.png)

**Observação:** Em dispositivos que utilizam o sistema IOS, o download não é possível, assim sendo necessário utilizar a ferramenta de compartilhamento para gerar o relatório.

**Saiba Mais**

[Como habilitar o download do espelho de ponto no Meu RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10759355849367-RH-RM-Meu-RH-Como-habilitar-o-download-do-espelho-de-ponto-no-Meu-RH)

[Como informar a descrição do abono no relatório do espelho de ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010132622-RH-RM-Meu-RH-Informar-a-descri%C3%A7%C3%A3o-do-abono-no-relat%C3%B3rio-do-espelho-de-ponto)
