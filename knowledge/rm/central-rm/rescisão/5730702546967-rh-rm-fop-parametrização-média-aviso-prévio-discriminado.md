---
article_id: 5730702546967
category: Rescisão
content_hash: 41959265e3f9bad8c20bd5d5857a22735b6f22499673d2c3c5568cefdf00f30c
fetched_at: '2026-06-28T22:46:54.372153+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - Parametrização: Média Aviso Prévio discriminado'
type: support-article
updated_at: '2022-04-28T12:11:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5730702546967-RH-RM-FOP-Parametriza%C3%A7%C3%A3o-M%C3%A9dia-Aviso-Pr%C3%A9vio-discriminado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:02:36 min  
  
Dúvida**  
Como parametrizar o sistema para calcular Média Aviso Prévio?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução  
1.**Parametrize evento que é lançado mensal/quinzenal/semanal conforme empresa desejar no envelope do funcionário respeitando a seguinte documentação:  
  
[RH - RM - FOP - Como verificar as incidências de médias de um evento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004195671-RH-RM-FOP-Como-verificar-as-incid%C3%AAncias-de-m%C3%A9dias-de-um-evento?source=search)  
  
Veja exemplo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5730260132375/mceclip0.png)  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5730286082071/mceclip1.png)  
  
**2.** Cadastre o **Evento de Média** da 1 ETAPA respeitando a seguinte documentação:  
  
[RH- RM - FOP - Médias: Discriminar médias de aviso prévio indenizado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015649111-RH-RM-FOP-M%C3%A9dias-Discriminar-m%C3%A9dias-de-aviso-pr%C3%A9vio-indenizado?source=search)  
  
Veja exemplo:  
  
Evento da Média com **CC - 62 Aviso Prévio**  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5730282964503/mceclip2.png)  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5730319548311/mceclip3.png)  
  
Evento da Diferença Média com **CC - 99 Diferença Aviso Prévio**  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5730359338647/mceclip4.png)  
  
**3.** Evento lançado no envelope do funcionário, exemplo abaixo:  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5730387930135/mceclip6.png)  
  
**4.** Parametrize o Sindicato conforme a empresa deseja realizar a média do evento, documentação de auxilio abaixo:  
  
[RH - RM - FOP - Parametrização do Cálculo de Médias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5178597213719-RH-RM-FOP-Parametriza%C3%A7%C3%A3o-do-C%C3%A1lculo-de-M%C3%A9dias?source=search)  
  
Exemplo abaixo Sindicato parametrizado para 6 meses:  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5730439504407/mceclip7.png)  
  
Após acesse aba **"Eventos p/Pagamento Média Aviso Prévio":**  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5730468768151/mceclip8.png)

Informe mesmo **Grupo** conforme parametrização da **Incidência Média** do evento cadastro:  
  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5730463045271/mceclip9.png)  
  
**5.** Realize o calculo da rescisão do funcionário:  
  
![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5730602123031/mceclip10.png)  
  
Após calcular veja o **Log de Calculo** e **Log de Média**:  
  
Envelope:  
  
![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5730605687959/mceclip11.png)  
  
Log de Média:  
  
![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5730622535319/mceclip12.png)  
  
**Saiba Mais**  
[RH - RM - FOP - Considerar média no desconto do aviso prévio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411799067031-RH-RM-FOP-Considerar-m%C3%A9dia-no-desconto-do-aviso-pr%C3%A9vio?source=search)
