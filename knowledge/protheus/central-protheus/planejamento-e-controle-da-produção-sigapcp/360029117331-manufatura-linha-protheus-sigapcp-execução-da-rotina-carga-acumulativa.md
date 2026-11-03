---
article_id: 360029117331
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 6718c03dc839dce549b89c1fc0bc0be7808b69b52e43f4b3f82cc1f50717f77b
fetched_at: '2026-06-28T22:42:42.342489+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Execução da rotina Carga Acumulativa
type: support-article
updated_at: '2021-10-25T14:54:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029117331-Manufatura-Linha-Protheus-SIGAPCP-Execu%C3%A7%C3%A3o-da-rotina-Carga-Acumulativa
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:10 min****Dúvida**Como executar a rotina **MATA730 - Carga Acumulativa**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**  
Para executar a rotina **Carga Acumulativa** é necessário:

1. Cadastrar **Centros de trabalho** na rotina **MATA770 - Centro de Trabalho**;
2. No **MATA632 - Operações**, para os produtos que deseja executar a **Carga Acumulativa**, informar no campo **G2\_CTRAB** **- Centro Trab.** o **Centro de trabalho** criado;
3. Executar a rotina **MATA690 - Carga Máquina**;
4. Na rotina **Carga Acumulativa** preencher os campos relativos às **Datas** e **Número das ordens de produção**, e no parâmetro **Considera informações?** selecionar **Carga Máquina** para realizar o cálculo com base na alocação da **Carga Máquina** executada previamente;
5. Após confirmar será apresentada a relação das ordens de produção, selecionar as que deseja realizar o cálculo e confirmar no botão **Cálculo**.
