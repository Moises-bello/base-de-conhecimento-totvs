---
article_id: 39987163975319
category: Cadastros
content_hash: 4e5ed42f0fb108f9c2e21e9b6401b765f61dcd2dd9de97046284b5637ce85f12
fetched_at: '2026-06-28T22:46:28.402500+00:00'
product: rm
section_id: 1500000861582
source: central-rm
title: RH - RM - PTO - "Erro ao inserir abono"
type: support-article
updated_at: '2026-04-27T20:15:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39987163975319-RH-RM-PTO-Erro-ao-inserir-abono
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39987163941271) Tempo aproximado para leitura: **00:01:20 min**  
  
**Ocorrência**  
Ao incluir um abono para o funcionário, o sistema emite uma mensagem de erro: "Erro ao tentar inserir abono com coligada 1, chapa 12345, data de referência 01/01/2026 e número de horas 01:00:00. Erro ao inserir abono". Ou "Erro ao tentar inserir abono com coligada 1, chapa 12345, data de referência 01/01/2026 início 07:00 e fim 08:00. Problema: Chave duplicada"  
  
**Ambiente**  
RH - RH (Linha RM) - TOTVS Automação de Ponto - Todas as versões  
  
**Causa**  
Este erro ocorre normalmente quando o ID da tabela **GAUTOINC** está dessincronizado com o ID da tabela **AABONOFUNCIONARIO.**  
  
**Solução**  
Para verificar se há esta dessincronização, com o apoio de um DBA, deverá executar a query abaixo para conferência:  
Consulta 1:

SELECT \* FROM GAUTOINC WHERE CODAUTOINC = 'IDABONOFUNCIONARIO'

Consulta 2:

SELECT CODCOLIGADA, MAX(ID) AS ID FROM AABONOFUNCIONARIO GROUP BY CODCOLIGADA

* Se houver divergência entre os ID's retornados na consulta, no caso quando o **ID da AABONOFUNCIONARIO está maior** que o ID da GAUTOINC irá ocorrer o erro.
* Quando o ID da GAUTOINC estiver maior ou igual ao ID da AABONOFUNCIONARIO **não há problema**.

Imagem com os ID's dessincronizados, onde o ID da **AABONOFUNCIONARIO** é maior que o ID da GAUTOINC, que resulta no erro:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39991065305623)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39991018406807)

Com o apoio de um DBA, deverá executar o script abaixo para igualar os ID's (***efetuar um backup da base de dados antes da execução***):

UPDATE GAUTOINC SET VALAUTOINC = (SELECT MAX(ID) FROM AABONOFUNCIONARIO WHERE CODCOLIGADA = 1) WHERE CODAUTOINC = 'IDABONOFUNCIONARIO' AND CODCOLIGADA = 1

No exemplo acima, o problema foi identificado na coligada 1. Portanto, a query de UPDATE foi executada considerando essa coligada. Após a execução, e realizando novamente as consultas 1 e 2, mostrará sincronização:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39991018408471)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39991018406807)  
Após o ajuste poderá incluir o abono normalmente.

**Saiba mais**  
[**RH - RM - PTO - Como Inserir abono no espelho do funcionário**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018486631-RH-RM-PTO-Como-Inserir-abono-no-espelho-do-funcion%C3%A1rio)

**Importante**  
Caso você seja cliente Cloud Totvs, deverá abrir um ticket com o time de Cloud para solicitar a execução do UPDATE.  
  
Se ao executar a consulta para avaliar se há a dessincronização dos ID's, os mesmos estiverem sincronizados, a causa raiz poderá ser outra. Nesta situação deverá acionar o time de suporte para análise.
