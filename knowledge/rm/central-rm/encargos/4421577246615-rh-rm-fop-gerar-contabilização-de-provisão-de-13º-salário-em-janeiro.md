---
article_id: 4421577246615
category: Encargos
content_hash: 00cecd9ed4227a9a5856c0b9019c8d269e11b8a85d2ff5dfececeac77f016a05
fetched_at: '2026-06-28T22:46:53.189810+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Gerar contabilização de provisão de 13º salário em janeiro
type: support-article
updated_at: '2025-03-11T10:49:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4421577246615-RH-RM-FOP-Gerar-contabiliza%C3%A7%C3%A3o-de-provis%C3%A3o-de-13%C2%BA-sal%C3%A1rio-em-janeiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como fazer a geração dos lançamentos contábeis de provisão de 13º salário em janeiro.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**1.  Acessar **Configurações | Parametrizador | 13º salário |** marcar a flag **Bloqueia reversão automática de 13º salário no mês de janeiro** e avançar até salvar.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9854349030039)  
  
2. Entrar no menu **Funcionário**, ir em **Anexos | Histórico de Provisões** e filtrar o ano para verificar as informações que constam para o mesmo.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9854508142359)  
  
3. Entrar na aba **Encargos | Cadastro | Cadastro do Encargo de provisão acumulada de 13º** **salário**. Se a flag **Provisão Acumulada** disponível em **Opções** estiver marcada, o sistema leva o acumulado para os meses, mas como falamos de janeiro, o acumulado não se aplica, pois trata-se de apenas um mês. Se estiver, desmarcada, a rotina gera mensal e de todos os meses. Deve-se acessar a aba de códigos ativos, marcar a flag de provisão de 13º e avançar até salvar.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9854686548375)  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9854702928535)  
  
4. Ir na aba **Encargos** e gerar novamente os encargos, lembrando de selecionar os códigos ativos, avançar e finalizar **caso já tenha gerado o Histórico de provisão, pois se ainda não gerou, deverá gerar**.  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9854747379223)  
  
5. Verifique em **Encargos | Histórico | Encargos** Filtre um colaborador como exemplo.  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9855372839959)  
  
6. Processe novamente a Geração dos Lançamentos, verificando se deve sobrepor as informações no lote caso já tenha utilizado o mesmo em algum teste anterior.  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9855438840727)  
  
7. Feito isso, poderá verificar o seu lote, pois a informação irá constar no mesmo:  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9855580227095)  
  
**Saiba mais:**[RH - RM - FOP - 13º Salário: Bloqueia reversão do 13º na contabilização em janeiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060461433-RH-RM-FOP-13%C2%BA-Sal%C3%A1rio-Bloqueia-revers%C3%A3o-do-13%C2%BA-na-contabiliza%C3%A7%C3%A3o-em-janeiro-)  
[Encargos - Folha de Pagamento](https://tdn.totvs.com/display/public/LRM/Encargos+-+Folha+de+Pagamento)
