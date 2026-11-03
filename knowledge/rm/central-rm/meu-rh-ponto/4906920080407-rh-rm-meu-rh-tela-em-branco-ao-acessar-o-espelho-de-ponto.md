---
article_id: 4906920080407
category: Meu RH - Ponto
content_hash: c33beb16e545c49d9d9f52ef0e773e006aa305367f09bfb097fcf8fc6411b454
fetched_at: '2026-06-28T22:47:30.332118+00:00'
product: rm
section_id: 1500000861782
source: central-rm
title: RH - RM - Meu RH - Tela em branco ao acessar o espelho de ponto
type: support-article
updated_at: '2025-02-03T17:45:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4906920080407-RH-RM-Meu-RH-Tela-em-branco-ao-acessar-o-espelho-de-ponto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24086996961175) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao acessar o Meu RH e clicar em espelho de ponto, está retornando uma tela em branco, não carregando os dados do ponto.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4906792285975)  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões  
  
**Causa**Esse incidente ocorre, pois a parametrização do Automação do Ponto está incorreta.   
  
**Solução**Para solucionar essa ocorrência, acesse o **RM | A****utomação de ponto | Configurações | Parametrizador | RM Portal > Edite o quiosque associado ao funcionário** e valide o parâmetro abaixo, que deverá ser **desmarcado**:  
![](https://totvssuporte.zendesk.com/attachments/token/AZ9loX26dfX40oSwaTE32XrsA/?name=inline464327850.png)  
  
O parâmetro **"Considera a primeira data do próximo período para edição de batidas"** deverá ser **desmarcado** e avançar até concluir o parametrizador.
