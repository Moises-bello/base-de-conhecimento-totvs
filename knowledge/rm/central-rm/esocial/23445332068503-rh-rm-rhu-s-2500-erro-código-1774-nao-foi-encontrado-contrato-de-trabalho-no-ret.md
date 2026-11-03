---
article_id: 23445332068503
category: eSocial
content_hash: bf2b7ae90ce34ea22fa9e764649f18d0b892655365a9826043eba1360d9e2a78
fetched_at: '2026-06-28T22:47:15.342448+00:00'
product: rm
section_id: 11645725240471
source: central-rm
title: 'RH - RM - RHU - S-2500: Erro código 1774: Nao foi encontrado contrato de trabalho
  no RET do eSocial para o trabalhador com mesma categoria e data de inicio.'
type: support-article
updated_at: '2026-06-02T18:21:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23445332068503-RH-RM-RHU-S-2500-Erro-c%C3%B3digo-1774-Nao-foi-encontrado-contrato-de-trabalho-no-RET-do-eSocial-para-o-trabalhador-com-mesma-categoria-e-data-de-inicio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23445332007319) Tempo aproximado para leitura: 00**:01:39 min**  
  
**Ocorrência**  
Ao gerar o XML do evento S-2500, a seguinte mensagem de erro é exibida: ***Erro código 1774: Nao foi encontrado contrato de trabalho no RET do eSocial para o trabalhador com mesma categoria XXX e data de inicio XX/XX/XXXX.***  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - **12.1.2209.155 e superiores.**  
  
**Causa**  
Esta mensagem de erro normalmente é emitida quando não foi inserida no cadastro do Processo Trabalhista a informação referente a matrícula do funcionário.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23445339466775)  
  
**Solução**  
Para que a situação possa ser corrigida, será necessário validar se o funcionário em questão possui eventos já constantes na base do eSocial - Governo, como o evento admissional - S-2190, S-2200 ou S-2300.   
  
Caso tenha, deverá informar no campo *'**Informações do evento**',* a opção ***'Sim'*** e inserir no campo ***'Matrícula'*** a mesma que foi informada nos eventos citados acima. 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23445339471127)

Caso contrário, deverá informar no campo *'**Informações do evento**',* a opção ***'Não'*** e no campo ***'Matrícula'*** inserir uma nova matrícula, criando uma fictícia, apenas para envio do S-2500. 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23445332014487)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23445339475735)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23445332019607)

Após ajustes, gentileza gerar o XML do evento novamente e valide se será possível enviá-lo sem erros.

**Saiba mais**  
Para maiores informações sobre os cadastros, acesse os links abaixo:

- [RH - RM - RHU - Processos Trabalhistas: Funcionário com vínculo de emprego formalizado em período anterior ao eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20469849558679)

- [RH - RM - RHU - Dúvidas frequentes: geração dos eventos de Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17623656599575)
