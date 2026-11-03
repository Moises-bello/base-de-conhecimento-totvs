---
article_id: 360022683331
category: RH – DIRF
content_hash: 92ffb42626cf7e53586b3079ff2381ebb7a64175affa0c9f86ff8445fc8a95e6
fetched_at: '2026-06-28T22:44:06.802803+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Como cadastrar a Previdência complementar para
  DIRF
type: support-article
updated_at: '2025-08-05T17:20:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022683331-RH-Linha-Protheus-GPE-Como-cadastrar-a-Previd%C3%AAncia-complementar-para-DIRF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21026760604823) Tempo aproximado para leitura:** **00:02:00 min****Dúvida**Como cadastrar a previdência complementar para gerar na DIRF?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Desde o ano de 2017 é necessário informar para a RFB os valores referentes a Previdência Complementar, agrupando por Fornecedor (Bancos, Entidades de Fundos, Cooperativas).  
  
Antes da geração da DIRF é necessário vincular o funcionário ao Fornecedor de Previdência Complementar o qual o funcionário fez o pagamento no decorrer do ano.  
  
**Para realizar este vínculo o usuário deverá:**

1. Em **>Atualizações >Definição de Cálculos >Manutenção de Tabelas**, incluir os dados na tabela **S073** dos fornecedores de Previdência Complementar.   
Deve-se, **obrigatoriamente**, informar o**código**, **CNPJ**, **Nome e verba de desconto** e também as verbas principais de FAPI ou Previdência Privada nos campos reservados para todos os tipos de Previdência Complementar, lembrando que essas verbas devem ter sido utilizadas na Folha de Pagamento e devem constar na Tabela de Acumulados **SRD**:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10136001880471)  
  
2. Faça o relacionamento do funcionário com o fornecedor na rotina **Manutenção de Previdência** pelo caminho **>Atualizações >Benefícios >Previdência Complementar >Manutenção de Previdência.  
OBS.:** É possível incluir a previdência complementar em lote, clicando em **>Outras Ações >Geração Automática:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21027003186199)**  
Manutenção previdência após relacionamento  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10136068956311)  
  
3. Configure a verba de previdência complementar para a DIRF na rotina de Verbas, pelo caminho **>Atualizações >Definições cálculos >Verbas**, aba **Anuais**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21027003203479)

O vídeo contido no *link* abaixo demonstra o **processo de cadastro de fornecedor de previdência complementar e o vínculo manual com o funcionário** (assistir em tela cheia para melhor visualização):  
<https://www.youtube.com/watch?v=1QRLDVcl7BM>  
  
O vídeo abaixo demonstra **o vínculo em lote entre fornecedor funcionário**, muito útil para quando a empresa trabalha com um único fornecedor ou possui uma forma de filtrar os funcionários que devem ser vinculados a um fornecedor específico (assistir em tela cheia para melhor visualização):  
<https://www.youtube.com/watch?v=O9hne3324JQ>   
  
  
**Saiba Mais:**[RH - Linha Protheus - GPE - Quais as Incidências de Verba para Dirf de Previdência Complementar](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwh0b%2B3SUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBqWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyMTA2MTQ5Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUXVhaXMtYXMtSW5jaWQlQzMlQUFuY2lhcy1kZS1WZXJiYS1wYXJhLURpcmYtZGUtUHJldmlkJUMzJUFBbmNpYS1Db21wbGVtZW50YXIGOwhUOg5zZWFyY2hfaWRJIilhMTM3MjZiZS0zYTY3LTRhMDktYWM0ZS05ZjFiNWRmYzFlZGEGOwhGOglyYW5raQk6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIh1wcmV2aWRlbmNpYSBjb21wbGVtZW50YXIGOwhUOhJyZXN1bHRzX2NvdW50aQKvBQ%3D%3D--a36f00ea1eace99b9e5acc2e5d14b61c201fe92d)  
[RH - Linha Protheus - GPE - Errorlog na rotina de Manutenção de Previdência, ao selecionar a lupa do Código Fornecedor](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXnW88LAc6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBymh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzc4ODY1NzM5MDMxMjctUkgtTGluaGEtUHJvdGhldXMtR1BFLUVycm9ybG9nLW5hLXJvdGluYS1kZS1NYW51dGVuJUMzJUE3JUMzJUEzby1kZS1QcmV2aWQlQzMlQUFuY2lhLWFvLXNlbGVjaW9uYXItYS1sdXBhLWRvLUMlQzMlQjNkaWdvLUZvcm5lY2Vkb3IGOwhUOg5zZWFyY2hfaWRJIik4M2Y2NmIxNi00NzEwLTQxZGMtYTRiZS1iNjc2ZmNlYzJlMGEGOwhGOglyYW5raQc6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIglzMDczBjsIVDoScmVzdWx0c19jb3VudGkR--b2f87e653efaddbd267fe3c1498c7420fe352259)
