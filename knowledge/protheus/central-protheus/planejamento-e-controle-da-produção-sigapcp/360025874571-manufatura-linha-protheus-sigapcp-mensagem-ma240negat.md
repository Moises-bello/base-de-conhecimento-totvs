---
article_id: 360025874571
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 95178f20f4f57344806fb20357a9cabd20873507231b6cc20fc6f9c749f87f4c
fetched_at: '2026-06-28T22:42:44.484634+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem MA240NEGAT
type: support-article
updated_at: '2021-05-26T11:47:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025874571-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-MA240NEGAT
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:01:05 min**  
  
**Ocorrência**Ao realizar o apontamento na rotina **MATA681 - Produção PCP Mod2** de uma operação em que não há nenhum componente sendo requisitado é apresentada a mensagem****MA240NEGAT****.  
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**A mensagem **MA240NEGAT** pode ocorrer quando na tela de parâmetros da opção **F12** no **MATA681** o parâmetro**Ver Saldo por Opera** está igual a **Sim**.   
  
**Solução**Quando o parâmetro acima está preenchido com **Sim**, o Sistema verifica o saldo dos componentes baseados no saldo de empenhos em cada apontamento de produção, mesmo que não seja a última operação.   
Se a operação apontada tem definidos componentes para serem baixados, ou ainda, a operação apontada for a última do roteiro de operações, será verificado o saldo dos empenhos ainda não requisitados.   
Para que não seja validado o saldo dos outros componentes da estrutura, que não está sendo baixado na operação, é necessário que altere o parâmetro para **Não**.
