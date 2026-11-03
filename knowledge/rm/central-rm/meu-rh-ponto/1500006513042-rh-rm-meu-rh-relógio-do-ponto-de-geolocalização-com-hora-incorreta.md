---
article_id: 1500006513042
category: Meu RH - Ponto
content_hash: 7f058c85d2181aed2fd58b3a662eee4cf73337be14467f3b2e0b69c8ff27e200
fetched_at: '2026-06-28T22:47:30.398113+00:00'
product: rm
section_id: 1500000861782
source: central-rm
title: RH - RM - Meu RH - Relógio do ponto de geolocalização com hora incorreta
type: support-article
updated_at: '2025-02-03T13:47:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006513042-RH-RM-Meu-RH-Rel%C3%B3gio-do-ponto-de-geolocaliza%C3%A7%C3%A3o-com-hora-incorreta
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23534924618263) Tempo aproximado para leitura: 00:04:03 min  
  
Ocorrência**Ao acessar o Relógio no Meu RH o horário que é apresentado esta com uma diferença de horas do fuso horário local.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) – Meu RH – A partir da versão 12.1.27  
  
**Causa**Esse incidente ocorre, pois a parametrização da hora/data no servidor ainda permanece no padrão de horário de verão acrescentando 1h a mais no relógio, ou o local de acesso do Meu RH está em um fuso diferente do definido no servidor de banco de dados e de aplicação onde esta instalado o Meu RH.  
  
**Solução**Ao Verificar no Meu RH o horário é apresentado com a diferença de 1h comparado com o horário apresentado no relógio do computador.  
![KCS.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008621001)  
  
Com o fim do horário de verão no Brasil alguns servidores não receberam a atualização do novo horário brasileiro (BRT).  
  
Verifique se o Windows esta atualizado com o pacote KB4507704, caso não esteja verifique as atualizações pendentes e instale este pacote.  
  
**Após atualizar o pacote KB4507704,** caso a situação persista, recomendamos utilizar a ferramenta TZEDIT para alterar as configurações dos horários no **servidores do Meu RH e servidor de banco de dados**.  
  
Para realizar o download do TZEDIT [clique aqui](https://drive.google.com/file/d/1E3hvGVX14ab2QJ24JwipqOOSIqDyvAe6/view?usp=sharing).  
  
Será necessário ajustar a configuração de **todos os horários que possuam + ou - horas em parênteses** recomendamos realizar em todos os UTCs segue exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29708521014551)  
  
Para realizar os ajustes em cada horário, segue um exemplo do processo sendo feito no horário de Brasília, é necessário 2 passos:

**1° Passo:**Dê um duplo clique em Brasília.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008629021)  
  
Acessando as configurações do horário de Brasília a flag "Automatically set Daylight Time" esta marcada, deverá ser **desmarcado** e clique em OK.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008634801)  
  
**2° Passo:** Clicar com botão direito do mouse em Brasília, após clique em Dynamic DST, nas configurações irá visualizar os períodos dos anos no qual estão ativos o horário de verão, basta selecionar todos os anos, a partir de "2020" e **desmarque** o horário de verão através da flag "Automatically set Daylight Time".  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500009018661)  
  
**Importante**O Procedimento deve ser realizado em todos os horários grifados no print inicial.  
Após os procedimentos, é obrigatório a reinicialização dos serviços RM.host e IIS.
