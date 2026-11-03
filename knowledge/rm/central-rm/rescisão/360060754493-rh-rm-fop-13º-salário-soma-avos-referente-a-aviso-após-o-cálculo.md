---
article_id: 360060754493
category: Rescisão
content_hash: d1419a1dd4db590b3f34d78194f3168ac733bf8601e37285ea444ee347e83bf9
fetched_at: '2026-06-28T22:46:55.266980+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - 13º Salário: Soma Avos Referente a Aviso Após o Cálculo'
type: support-article
updated_at: '2024-09-16T20:05:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060754493-RH-RM-FOP-13%C2%BA-Sal%C3%A1rio-Soma-Avos-Referente-a-Aviso-Ap%C3%B3s-o-C%C3%A1lculo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26412243397911) Tempo aproximado para leitura: **00:03:39 min****Dúvida**Qual a funcionalidade do parâmetro **Soma Avos Referente a Aviso Após o Cálculo** para o 13º salário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**O parâmetro **Soma avos ref. aviso após o cálculo** está presente em **Configurações | Parametrizador | Rescisão | Aviso Prévio.**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8905077104919)  
 **Exemplo:**Funcionário com demissão em 07/02/14 e com 39 dias de aviso prévio indenizado.  
  
**--> Parâmetro Marcado:****13º proporcional:**  Funcionário terá direito ao avo de 13º salário proporcional de janeiro, porém não tem direito ao de fevereiro pois não completou 15 dias trabalhados no mês.  
  
**13º indenizado:**  Funcionário tem 39 dias de aviso prévio indenizado, então 30 dias dá direito a 1 avo indenizado, porém os outros 9 dias não dão direito ao novo avo indenizado.  
  
**Resultado Final:** Sistema irá lançar 1 avo proporcional e 1 avo indenizado.  
  
**--> Parâmetro Desmarcado:**Sistema irá verificar quando acaba o período de trabalho + o aviso prévio indenizado:  07/02/2014, data da demissão, + 39 dias = 18/03/2014. Sendo 18/03/2014, o sistema irá lançar da seguinte forma: 1 avo proporcional referente a janeiro e 2 avos indenizados referentes a Fevereiro e Março, os 15 dias de fevereiro completaram com os dias de aviso indenizado e 18 dias trabalhados em março.  
  
**Saiba Mais**[Como funciona o parâmetro Soma Avos Referente a Aviso Após o Cálculo para 13º](https://tdn.totvs.com/pages/viewpage.action?pageId=149881815)
