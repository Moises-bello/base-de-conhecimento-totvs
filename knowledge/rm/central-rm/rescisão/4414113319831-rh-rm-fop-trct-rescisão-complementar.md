---
article_id: 4414113319831
category: Rescisão
content_hash: ee5d9524bca24d1d7a1c67cfd984565d9ed698a3d9f225b08704a0cb7ba0a9f5
fetched_at: '2026-06-28T22:46:54.443023+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - TRCT: Rescisão Complementar'
type: support-article
updated_at: '2024-05-15T18:13:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414113319831-RH-RM-FOP-TRCT-Rescis%C3%A3o-Complementar
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23510143537815)**Tempo aproximado para leitura:**00:01:36 min  
  
Dúvida**  
Como realizar geração TRCT para rescisão complementar?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**1.**Passo:**

O funcionário Chapa: 0002 – João teve cálculo de rescisão em 10/12/2010.

Houve cálculo de rescisão complementar para o João em 15/07/2011 na Competência do Movimento:

Mês: 07, Ano: 2011, Período: 5  
  
 Para a correta emissão do TRCT a seguinte parametrização deverá ser informada:

![](https://tdn.totvs.com/download/attachments/42042615/61.png?version=1&modificationDate=1350592398000&api=v2)  
  
2.**Passo:**

1- CAMPO 50 SEMPRE ZERADO

* Devido a ser um TRCT de complementar, o cliente pode optar por sempre levar o campo 50 zerado, assim os valores de diferença de saldo de salario, faltas e atrasos podem ser levados separadamente nos outros campos do TRCT (escolhidos pelo RH, mas sugiro o campo "Outros Proventos").

* Para fazer esta configuração o cliente deverá criar outra formula para o campo 50 com o texto "0"(sem aspas), e informar esta formula como formula de valor para o campo 50 nas configurações da emissão do TRCT.

2 - CAMPO 50 COM OS VALORES DE DIFERENÇA DE SALDO DE SALARIO, FALTAS E ETC...

* Caso o cliente opte por levar os valores de diferença de saldo de salario, faltas e quaisquer outros no campo 50, deve-se criar uma nova formula buscando o valor destes eventos desejados (o cliente pode usar o texto atual da formula do campo 50 para criar uma nova mudando os eventos), o cliente apenas deve-se atentar para retirar as rubricas TRCT destes eventos para que não saiam em duplicidade no TRCT.

3. **Passo:**   
Marque a flag **"TRCT de rescisão complementar".**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23510133824407)  
  
**Saiba mais**  
Para maiores informações sobre quais rubricas utilizar em quais campos ou para maiores informações sobre o TRCT, [CLIQUE AQUI](https://tdn.totvs.com/pages/releaseview.action?pageId=42042615#:~:text=Na%20gera%C3%A7%C3%A3o%20do%20TRCT%2C%20para,ter%20relacionada%20sua%20respectiva%20rubrica.).
