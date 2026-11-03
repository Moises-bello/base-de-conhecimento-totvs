---
article_id: 360015392251
category: Cálculo
content_hash: b4c1c06effc8a7383a3fd124c798cfbcf633e2cf6a9284c764c0f5301ff9806a
fetched_at: '2026-06-28T22:46:29.259673+00:00'
product: rm
section_id: 1500000861662
source: central-rm
title: RH - RM - PTO - Calcular DSR (Descanso Semanal Remunerado) e DSP (Descanso
  Semanal Perdido)
type: support-article
updated_at: '2026-01-02T20:24:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015392251-RH-RM-PTO-Calcular-DSR-Descanso-Semanal-Remunerado-e-DSP-Descanso-Semanal-Perdido
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16981710850711) Tempo aproximado para leitura: 00:01:20 min**

**Dúvida**Como calcular os eventos de D.S.R e D.S.P?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto – A partir da versão 11.80  
  
**Solução**Para realizar o cálculo dos eventos de D.S.R e D.S.P, siga os passos abaixo:

1. Acesse o **Parametrizador do Funcionário** através de **Configurações | Parametrizador | Funcionário**.   
   ![2018-08-31_16_27_19-TOTVS_S_rie_T_Servi_os__RM__Alias__CorporeRM___1-TOTVS_SA.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360010339172)
2. Acesse a etapa **D.S.R** e marque a opção **Paga D.S.R** e insira o número de horas desejado.   
   ![2018-08-31_16_27_58-Assistente_de_Implanta__o_de_Processos__Processo__08.03_-_Funcion_rio__00001_.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360010364751)
3. Acesse o agora o **Parametrizador do Sindicato** através de **Configurações | Parametrizador | Sindicato**.
4. Acesse a etapa **D.S.R** e marque as opções desejadas.   
   ![2018-08-31_16_29_09-Assistente_de_Implanta__o_de_Processos__Processo__08.02_-_Parametros_Sindicato__.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360010339232)
5. Avance até a etapa **Eventos** e insira os eventos de **D.S.R** e **D.S.P**, que possuem os códigos de cálculo **0003 - Descanso Semanal Remunerado** e **0035 - Descanso Semanal Perdido**, respectivamente.   
   ![2018-08-31_16_30_07-Assistente_de_Implanta__o_de_Processos__Processo__08.02_-_Parametros_Sindicato__.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360010364791)  
   ![2018-08-31_16_31_51-TOTVS_S_rie_T_Servi_os__RM__Alias__CorporeRM___1-TOTVS_SA.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360010364771)  
   ![2018-08-31_16_32_12-TOTVS_S_rie_T_Servi_os__RM__Alias__CorporeRM___1-TOTVS_SA.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360010339192)
6. Associe aos eventos desejados do **Totvs Folha de Pagamento.**

**Saiba Mais**Caso deseje mais informações sobre as opções de parametrização do sindicato para o D.S.R, acesse a documentação [Descanso Semanal Remunerado](https://tdn.totvs.com/display/public/LRM/Descanso+Semanal+Remunerado).

Para maiores informações sobre as opções de parametrizar funcionário acesse: [Funcionário D.S.R.](https://tdn.totvs.com/display/public/LRM/D.S.R)
