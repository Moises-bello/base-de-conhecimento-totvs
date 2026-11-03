---
article_id: 6845451064599
category: Gestão de Distribuição (SIGAOMS)
content_hash: fb9458bf3b6920f0c6e238550eab44155ea89c68bfc0844637f8b5b7af480098
fetched_at: '2026-06-28T22:45:49.892705+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Log para analise de Seleção de Pedidos na
  Montagem de Carga - OMSA200
type: support-article
updated_at: '2022-12-02T13:09:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6845451064599-Log%C3%ADstica-Linha-Protheus-OMS-Log-para-analise-de-Sele%C3%A7%C3%A3o-de-Pedidos-na-Montagem-de-Carga-OMSA200
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:18 min** **Dúvida**Como utilizar o **log** para **analise de Seleção de Pedidos** na **Montagem de Carga - OMSA200**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**Quando o processo de seleção de Pedidos na rotina **Montagem de Carga - OMSA200** apresentar morosidade na sua execução, considerando o número de informações que compõe a carga.  
  
Poderá ser ativado o parâmetro **MV\_OMSCMSG** para gravação de **log**, o qual servirá de apoio na identificação de problemas de **Seleção** e/ou **morosidade na Seleção de Pedidos**.  
  
**Este parâmetro deve ser ativado somente quando necessário e sob orientação do Atendimento TOTVS.**  
  
**Exemplo de utilização:**

1. Pelo **SIGACFG - Configurador do Protheus**, crie manualmente o parâmetro **MV\_OMSCMSG** e defina o valor com **.T.**
2. Acesse **Atualizações/Cargas/Montagem de Carga - OMSA200**, execute uma seleção de Pedidos
3. Após executar uma seleção de Pedidos na rotina **Montagem de Carga - OMSA200**, consulte o arquivo **console.log** localizado na pasta **AppServer** do **Protheus**.
4. No arquivo **console.log** serão geradas mensagens, podendo ser identifica pela **literal OMS**.

**Saiba mais**Mais informações poderão ser acessadas no *link*:  
[DLOGWMSMSP-9856 DT Lentidão na seleção de pedidos na montagem de carga OMSA200](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=546675794)
