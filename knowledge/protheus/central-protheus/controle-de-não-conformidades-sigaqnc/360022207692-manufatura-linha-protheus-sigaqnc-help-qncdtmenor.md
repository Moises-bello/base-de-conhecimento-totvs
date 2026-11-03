---
article_id: 360022207692
category: Controle de Não Conformidades (SIGAQNC)
content_hash: 81413a00933dc6e0fa861d29a7864e086197989d692e35c552889a763a082ada
fetched_at: '2026-06-28T22:42:27.980816+00:00'
product: protheus
section_id: 360005876654
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQNC - Help QNCDTMENOR
type: support-article
updated_at: '2021-09-08T12:58:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022207692-Manufatura-Linha-Protheus-SIGAQNC-Help-QNCDTMENOR
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:00:50 min  
  
Ocorrência**Ao preencher uma data na tela de **Ação**, opção **Etapas**, no cadastro **QNCA030 - Plano de Ação**, é apresentada a mensagem: **QNCDTMENOR - A data não poderá ser menor que a data do lançamento anterior**.  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Não Conformidades (SIGAQNC) – Todas as versões  
  
**Causa**Trata-se de uma validação do parâmetro **MV\_QNCPRZ - Define se as datas das Ações/Etapas do Plano de Ação poderão ser diferentes/inferiores entre as etapas (1=SIM / 2=NAO )**.   
  
**Solução**Para sanar esta mensagem é necessário configurar o parâmetro **MV\_QNCPRZ** com conteúdo igual à **1-Sim**. Isto porque, ao configurar o parâmetro **MV\_QNCPRZ** como **2-Não**, o Sistema valida as informações da coluna **Prazo Execuc** e neste caso todas as datas informadas precisam estar em ordem crescente.
