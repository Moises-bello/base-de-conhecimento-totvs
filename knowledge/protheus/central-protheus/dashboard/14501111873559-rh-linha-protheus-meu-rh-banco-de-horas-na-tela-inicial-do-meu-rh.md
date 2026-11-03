---
article_id: 14501111873559
category: DASHBOARD
content_hash: 50cc6e4228598a0d987e486f390d7c7e53f0ff6196f0400378b716bd1b4c50e3
fetched_at: '2026-06-28T22:44:41.371006+00:00'
product: protheus
section_id: 10299521604759
source: central-protheus
title: RH - Linha Protheus - MEU RH - Banco de Horas na tela inicial do Meu RH
type: support-article
updated_at: '2026-06-18T19:28:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14501111873559-RH-Linha-Protheus-MEU-RH-Banco-de-Horas-na-tela-inicial-do-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30615378029463) Tempo aproximado para leitura: **03:00 min**  
  
**Dúvida**  
RH - Linha Protheus - MEU RH - Banco de Horas na tela inicial do Meu RH  
  
**Ambiente**  
TOTVS RH - (Linha Protheus) - MEU RH - Todas as versões  
  
**Solução**  
A opção de **Saldo de Horas** no App Meu RH, presente na página inicial do funcionário, é um componente do *Dashboard* que exibe informação sobre **o saldo atual de banco de horas do funcionário**.   
  
Os dizeres sempre serão como Horas Positivas ou como Horas negativas, advindas diretamente do saldo existente no Protheus.  
  
Exemplo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14500476160023)  
  
Veja que, para este funcionário temos **-56:53** que é exatamente o saldo que ele possui no banco de horas, que também **pode-se consultar no módulo Ponto Eletrônico (16)**, pela rotina Atualizações -> Lançamentos -> **Banco de Horas**, gravado na tabela **SPI**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14500561550743)  
  
Veja que o Meu RH, demonstrou o valor final da coluna **Saldo**. Para demonstrar o valor da coluna Saldo Valorizado, podemos alterar o parâmetro **MV\_TCFBHVL** para .T.   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14500664590871)  
Este parâmetro, demonstrará no *dashboard*do Meu RH, as horas de Banco na **coluna saldo** caso seja preenchido **.F.** ou, da **coluna Saldo Valorizado** caso seja preenchido **.T.**.  
  
Assim, após **alterar** este parâmetro e acessar novamente no Meu RH, com este mesmo funcionário, o *dashboard* de **Meu Saldo de Horas** é apresentado com as **Horas Valorizadas**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14500740493719)  
  
Por fim, se o funcionário tiver **horas positivas** em seu **Banco de Horas (SPI)**, os dizeres serão da seguinte maneira:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14500954642967)  
  
**Saiba Mais**  
[**CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI para acessar a documentação de referências sobre o MEU RH**](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
