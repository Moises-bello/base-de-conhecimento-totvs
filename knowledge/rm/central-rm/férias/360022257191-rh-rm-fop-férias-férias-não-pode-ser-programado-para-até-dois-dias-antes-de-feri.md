---
article_id: 360022257191
category: Férias
content_hash: ed85579962799d47eda98f657e9a38d77ee70754ea9e54ca522a1f34dbb93487
fetched_at: '2026-06-28T22:46:56.462688+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: 'RH - RM - FOP - Férias: Férias não pode ser programado para até dois dias
  antes de feriado'
type: support-article
updated_at: '2024-06-17T14:06:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022257191-RH-RM-FOP-F%C3%A9rias-F%C3%A9rias-n%C3%A3o-pode-ser-programado-para-at%C3%A9-dois-dias-antes-de-feriado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24229485299607) Tempo aproximado para leitura: **00:00:40 min  
  
Ocorrência**Ao tentar realizar o cadastro de férias para funcionários o sistema apresenta mensagem informando que não é possível realizar o cadastro de férias próximo a dias de descanso ou feriados: **Inicio de férias não pode ser programado para até dois dias antes de feriado ou dia de descanso**.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Essa mensagem é gerada pois o sistema está parametrizado para impedir o cadastramento de férias próximo a essas datas.  
  
**Solução**Para solucionar essa ocorrência deverá seguir os passos:

1. Acesse: **Configurações | Parametrizador | RM Portal | Férias.**

2. Na tela de parametrização do Quiosque avance até a etapa **3- Férias** e verifique se o parâmetro **Impedir início de férias em feriados, dias de descanso ou até 2 dias antes destes** está **marcado:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9800781830167)**  
3. Caso esteja marcado, **desabilite** este parâmetro e avance até concluir.

4. Realize um *logout/login* no sistema e tente realizar o cadastro das férias novamente.  
  
**Saiba mais**  
[Parâmetros do RM Portal](https://tdn.totvs.com/pages/releaseview.action?pageId=452719215#:~:text=solicitando%20sua%20aprova%C3%A7%C3%A3o.-,Impedir%20in%C3%ADcio%20de%20f%C3%A9rias%20em%20feriados%2C%20dias%20de%20descanso%20ou,e%20dias%20de%20descanso%20remunerado.)
