---
article_id: 16977343684503
category: PONTO ELETRÔNICO
content_hash: 5c853a0b587c856ac9645bcc904f16a1bf44b80df9a86c5f711be9eb5df0d212
fetched_at: '2026-06-28T22:44:36.581554+00:00'
product: protheus
section_id: 10299685322391
source: central-protheus
title: RH - Linha Protheus - Meu RH - Ao incluir marcação de ponto a um dia não trabalhado,
  há a perda da referência de Entrada ou Saída
type: support-article
updated_at: '2025-11-05T21:09:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16977343684503-RH-Linha-Protheus-Meu-RH-Ao-incluir-marca%C3%A7%C3%A3o-de-ponto-a-um-dia-n%C3%A3o-trabalhado-h%C3%A1-a-perda-da-refer%C3%AAncia-de-Entrada-ou-Sa%C3%ADda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16977300072215) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Ao incluir marcação de ponto a um dia não trabalhado, há a perda da referência de Entrada ou Saída  
  
**Ambiente**TOTVS RH - (Linha Protheus) - MEU RH - Todas as versões  
  
**Solução**Por vezes, temos via App Meu RH, uma **perda da referência do dia da marcação de ponto**, seja via **inclusão manual**, ou até mesmo por **geolocalização**.  
  
No exemplo abaixo, temos um horário padrão das **08:00 às 17:30 de segunda a sexta-feira**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16976215789463)  
  
Nota-se que as marcações de Entrada e Saída, foram **corretamente classificadas neste cenário**, porém se for incluída marcações para o dia seguinte **(12/08 - sábado)**, que pela escala padrão, **é um dia não trabalhado,** há a perda da referência de **Entrada e Saída**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16976334277911)  
  
Realizar a inserção da marcação de **Entrada no dia 12/08 as 06:00** e uma **Saída as 12:00**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16976409551383)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16976454585239)  
  
Ao final do processo de inclusão, acessando o Espelho de Ponto do funcionário, é notório o **desposicionamento** e a **perda da referência** de **Entrada as 06:00** e **Saída as 12:00**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16976531362583)  
  
Esse cenário ocorre pois, **a Tabela de Horário Padrão** do **turno que este funcionário está alocado**, está preenchida de **forma incorreta**, **sem os horários de referência para sábado e domingo**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16976787586839)  
  
Na Tabela de Horário Padrão, **é necessário preencher todos os dias da semana** com os horários, para quando houver uma situação igual a do exemplo, **onde o funcionário realiza marcação em um dia não trabalhado**, **seja posicionado corretamente as marcações de ponto** incluídas manualmente, ou por Geolocalização.  
  
No caso, replica-se **os mesmos dados aos dias de Sábado e Domingo**, **menos a coluna de Tipo dia**, onde ainda terá a informação de Compensado e DSR, respectivamente, para sábado e domingo.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16976918378135)  
\*\*\* Importante não alterar o Tipo dia, pois desta forma não haverá apontamento de Falta se o funcionário não realizar marcação aos sábados e domingos.  
  
Alterando a Tabela de Horário Padrão corretamente e, **reprocessando a rotina de Espelho de Ponto**, o posicionamento das marcações incluídas, é feito de acordo.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16977035333783)  
  
**Saiba Mais**Para saber mais sobre a rotina Tabela de Horário Padrão **[clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047920293-RH-Linha-Protheus-PON-Tabela-de-Hor%C3%A1rio-Padr%C3%A3o-)  
[CLIQUE AQUI](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)**[para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH) **[CLIQUE AQUI](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)** [para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
