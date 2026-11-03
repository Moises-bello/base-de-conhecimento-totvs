---
article_id: 35827506470039
category: FÉRIAS
content_hash: 9b6d1bc37f914f33b3793b834746ce9370215459aaeedc94c21114ed4b77346e
fetched_at: '2026-06-28T22:44:34.474715+00:00'
product: protheus
section_id: 10299705719575
source: central-protheus
title: RH - Linha Protheus - Meu RH - O que conferir se o período de férias no Meu
  RH, se apresentar em duplicidade após aprovação da requisição
type: support-article
updated_at: '2026-06-19T19:04:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35827506470039-RH-Linha-Protheus-Meu-RH-O-que-conferir-se-o-per%C3%ADodo-de-f%C3%A9rias-no-Meu-RH-se-apresentar-em-duplicidade-ap%C3%B3s-aprova%C3%A7%C3%A3o-da-requisi%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35827510697111) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
O que conferir se o período de férias no Meu RH, se apresentar em duplicidade após aprovação da requisição  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**  
Este cenário ocorre quando o funcionário realiza uma solicitação de férias, o Gestor aprova e por consequência o RH atende dentro do Protheus, levando os dados para a rotina Controle de Dias de Direito.  
  
**Exemplo abaixo, funcionário solicitando 10 dias a partir de 10/02/2025**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35827506462871)  
  
Após esta inserção, é recomendado que a Equipe do RH quando efetuar o cálculo, **faça-o pela rotina de Cálculo de Férias Programadas - GPEM060**, porém também é possível realizar o Cálculo nesse cenário, na rotina GPEM030 - Cálculo de Férias.  
  
Quando o RH optar por realizar o cálculo na rotina GPEM030, **será possível alterar a data início das férias que foram programadas e requisitadas pelo funcionário com origem Meu RH.**  
  
**Veja o exemplo com a alteração para início em 17/02/2025**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35827510697623)  
  
Após as férias serem calculadas, **será necessário neste cenário, alterar também a data início na programação da rotina Controle de Dias de Direito - tabela SRF, que está com data de 10/02/2025.**  
  
Caso não seja alterada a data início assim como foi no cálculo efetivo, **a programação no Meu RH duplicará**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35827506464023)  
  
Nota-se que o funcionário antes possuía 30 dias de direito de gozo de férias, porém com esta duplicidade o Meu RH mostrará que ele possui somente 10 dias de direito agora.  
  
**Ao alterar a data início também na rotina Controle de Dias de Direito, a duplicidade não ocorrerá mais.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35827506464535)  
  
Resultado após alteração:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35827506464919)  
  
Diferentemente do Protheus, o Meu RH já apura o saldo em tempo real e disponibiliza para o usuário.  
  
Como a data de inicio das férias no cálculo está diferente da data de início das férias na programação, o Meu RH interpretará que aquela programação não foi cumprida.  
  
Em resumo, para o Meu RH, **a programação e o efetivo cálculo são férias diferentes.**  
  
**Saiba Mais:**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
