---
article_id: 360008805472
category: Configurações
content_hash: 8ae37a7f7da77b5efaa5e9ba071a40df6a6b8bb233d13879706aa8db57aa42cf
fetched_at: '2026-06-28T22:46:49.669744+00:00'
product: rm
section_id: 1500000834621
source: central-rm
title: 'RH - RM - FOP - Afastamento: Como proporcionalizar eventos para afastados'
type: support-article
updated_at: '2025-03-13T09:57:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360008805472-RH-RM-FOP-Afastamento-Como-proporcionalizar-eventos-para-afastados
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como proporcionalizar Eventos considerando ou não os 15 primeiros dias de atestado médico?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para que o sistema proporcionalize eventos considerando os 15 primeiros dias de atestado, pagos pela empresa, siga os passos abaixo:  
  
01. Acesse o menu **Configurações | Parametrizador | Folha Normal | Afastamentos** e marque o parâmetro **Proporcionalizar eventos considerando os dias de atestado médico**:![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008158132/mceclip0.png)  
02. Marcando a opção acima, o evento do tipo valor também terá que estar com a opção de proporcionalizar **Afastamento** marcada em: **Administração de Pessoal | Eventos | Eventos**, edite o evento em questão e vá na aba **Identificação**. No campo **Proporcionalidade**, marque a opção **Afastamento**.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008199671/mceclip1.png)  
  
**Exemplo**Um funcionário ficou afastado de 01/07 até 20/07;  
Salario base = 1.000,00;  
Evento Insalubridade = 20% (937,00 sal min)  
  
Dias Trabalhados (10 dias) = 333,33;  
Atestado Médico (15 dias) = 500,00;  
Insalubridade = 156,17 (937,00 \* 0,20 = 187,40) <> (187,40 / 30 ) \* 10 = **62,47**03. Caso o parâmetro do passo 01 esteja desmarcado e o parâmetro do passo 02 esteja marcado, o sistema irá proporcionalizar o valor do evento, porém não irá considerar os 15 primeiros dias de afastamento.  
  
**Exemplo**Um funcionário ficou afastado do dia 01/07 ao dia 20/07;  
Salario base = 1.000,00;  
Evento Insalubridade = 20% (937,00 sal min)  
  
Dias Trabalhados (10 dias) = 333,33;  
Atestado Médico (15 dias) = 500,00  
Insalubridade = 156,17 (937,00 \* 0,20 = 187,40) <> (187,40 / 30 ) \* 25 = **156,17**
