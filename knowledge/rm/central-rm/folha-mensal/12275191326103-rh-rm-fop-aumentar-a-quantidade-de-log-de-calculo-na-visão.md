---
article_id: 12275191326103
category: Folha Mensal
content_hash: de658d724296c20004d8c5a12877931e6d88fde4d88644ded999dc76dbba741e
fetched_at: '2026-06-28T22:46:58.274756+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Aumentar a quantidade de Log de Calculo na visão
type: support-article
updated_at: '2024-09-16T18:52:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12275191326103-RH-RM-FOP-Aumentar-a-quantidade-de-Log-de-Calculo-na-vis%C3%A3o
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)****Tempo aproximado para leitura:****00:01:46 min**  
Dúvida**Como aumento a quantidade de Log de Calculo exibidos na visão?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para aumentar a quantidade de funcionários exibidos na visão, sigo os passos abaixo:  
  
1. Acesse **Serviços Globais | Serviços | Servidores de Aplicação**;  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12274666607895)  
2. Ao abrir esta tela, caso exista cadastro do server **FopGerlogCalculoData****,** edite o cadastro conforme passo 03. Caso não exista, crie um novo cadastro informando no campo ID do Server o server **FopGerlogCalculoData**;  
  
3. No campo **Número máximo de registro**, informe o máximo de funcionários desejado para serem visualizados na visão ou informe 999999 e salve.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12274626691735)  
  
**Observação:**Para identificar o ID do Server correspondente ao cadastro que deseja exibir mais registros, acesse o menu correspondente a ele e pressione: Ctrl + Alt + F9, conforme exemplo no print abaixo:  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12274678187543)
