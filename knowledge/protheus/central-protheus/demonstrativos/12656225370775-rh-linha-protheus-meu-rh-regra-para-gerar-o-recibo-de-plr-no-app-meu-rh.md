---
article_id: 12656225370775
category: DEMONSTRATIVOS
content_hash: 475e6834a80c25196d13fae8d26d72f421258b612f69a90894c658882e2ea57b
fetched_at: '2026-06-28T22:44:38.388481+00:00'
product: protheus
section_id: 10299629664279
source: central-protheus
title: RH - Linha Protheus - MEU RH - Regra para gerar o recibo de PLR no App Meu
  RH
type: support-article
updated_at: '2026-06-16T18:08:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12656225370775-RH-Linha-Protheus-MEU-RH-Regra-para-gerar-o-recibo-de-PLR-no-App-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19276146626967) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Regra para gerar o recibo de PLR no App Meu RH  
  
**Ambiente**TOTVS RH (Linha Protheus) -Meu RH – todas as versões  
  
**Solução**No App Meu RH, temos a possibilidade de gerar o recibo de todos os roteiros que compõem o cadastro de período do SIGAGPE, como por exemplo, roteiro FOL, FER, VEX e PLR.  
  
**No caso do roteiro PLR**, temos no App Meu RH, um parâmetro que controle **qual o dia do mês que esse recibo será disponibilizado** para o funcionário realizar a visualização.  
  
Este parâmetro é o **MV\_TCFDEXT**, que como dito acima, define o dia do mês a partir do qual os valores extras e o PLR estão liberados para consulta no RH *Online*.  
  
Para modificar o parâmetro, será necessário realizar o acesso ao **SIGACFG - Configurador, no rotina Ambiente > Cadastros > Parâmetros e localizar o MV\_TCFDEXT**.  
  
Exemplo de configuração:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23528707101463)  
  
Nesse caso, **independentemente do mês que o PLR for calculado e pago aos funcionários,** em qualquer processo que o roteiro esteja cadastrado, **será disponibilizado o recibo a partir do dia 25 daquele mês de pagamento**.  
  
Nesse período abaixo, por exemplo, de Maio/2024, realizo o pagamento sempre no dia 31 do próprio mês do período, em regime Competência, como o parâmetro em questão está com o conteúdo 25, o recibo do PLR quando **já estiver calculado pelo módulo SIGAGPE,** **será disponibilizado a partir do dia 25 daquele mês de Folha** via App Meu RH, para os funcionários que estão vinculados a este processo.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23528717260311)  
  
Importante retificar que, o holerite do PLR, somente irá aparecer no Meu RH **se e somente se, for calculado pelo módulo SIGAGPE no roteiro PLR padrão**.  
  
Por questões de Desenvolvimento do Produto, não temos a possibilidade de termos mais que um parâmetro para este controle, pois uma vez que nele for cadastrado um dia do mês, para todos os processo de Folha e para todos os meses do ano, será disponibilizado sempre no mesmo dia do mês.  
  
**Saiba Mais  
[CLIQUE AQUI](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)**[para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH) **[CLIQUE AQUI](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)**[para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
