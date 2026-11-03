---
article_id: 360025389011
category: Cálculo
content_hash: ad4bae8f35b1334681eb41ecfdd86d5ff0fef490f87c6032f86deb17b697493e
fetched_at: '2026-06-28T22:46:29.229941+00:00'
product: rm
section_id: 1500000861662
source: central-rm
title: RH - RM - PTO - Calcular eventos no movimento
type: support-article
updated_at: '2025-02-19T01:00:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025389011-RH-RM-PTO-Calcular-eventos-no-movimento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16503361448087)**Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Como calcular eventos no movimento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 11.80  
  
**Solução**Para calcular eventos no movimento do funcionário, siga os passos abaixo.

1. Cadastre o evento de **Automação de Ponto** no **Parametrizador do Sindicato** na etapa **Eventos**e associe ao evento correspondente do **RM Labore**. Caso deseje lançar este evento posteriormente para a **Folha de Pagamento**, marque a opção **Cadastrar este evento nos eventos a serem lançados no Labore**.  
   ![2019-03-15_15_26_24-TOTVS_S_rie_T_Servi_os__RM__Alias__CorporeRM___1-TOTVS_SA.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360023904892)
2. Caso o funcionário não utilize o banco de horas, avance ao passo 4. Para funcionários que utilizam banco de horas, acesse a etapa **Banco de Horas** do **Parametrizador do Sindicato** e verifique se a opção **Considera atitude do evento** está marcada. Caso esteja, avance para o próximo passo. Caso não esteja marcada, verifique se a atitude da ocorrência desejada está como **Pagar** ou **Descontar**.  
   ![2019-03-15_15_27_41-Assistente_de_Implanta__o_de_Processos__Processo__08.02_-_Parametrizando_Sindica.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360023904912)
3. Acesse a etapa **Eventos** novamente e edite o evento criado. Selecione a aba **Informações Adicionais** e verifique se a opção **Movimento** em **Atitude a ser considerada no dia/evento** está marcada.  
   ![2019-03-15_15_28_37-.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360023935251)
4. Salve todos os cadastros realizados e conclua o processo de parametrização do **Sindicato**. Recalcule o espelho do funcionário e verifique se na etapa **Movimento** da **Janelas de Informações**, o evento será calculado.  
   ![2019-03-15_15_29_46-Espelho_do_Funcion_rio_00001_-_ITAMAR_MENDES_DA_SILVEIRA.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360023904932)

**Saiba Mais**  
Para maiores informações sobre eventos, acesse a documentação a seguir: [Eventos](https://tdn.totvs.com/display/LRM/Eventos+-+PTO).
