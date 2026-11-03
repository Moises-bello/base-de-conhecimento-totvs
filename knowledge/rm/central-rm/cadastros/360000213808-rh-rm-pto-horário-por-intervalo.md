---
article_id: 360000213808
category: Cadastros
content_hash: 8363aeed02071d6e0bc6595fa83babf9f5388e7360f0748a61478af203c20f44
fetched_at: '2026-06-28T22:46:28.590495+00:00'
product: rm
section_id: 1500000861582
source: central-rm
title: RH - RM - PTO - Horário por intervalo
type: support-article
updated_at: '2025-02-04T14:27:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000213808-RH-RM-PTO-Hor%C3%A1rio-por-intervalo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19408650864791) Tempo aproximado para leitura: 00:00:45 min**

**Dúvida**Como cadastrar horários por intervalo?

**Ambiente**RH - RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 11.80

**Solução**Para realizar o cadastro no **Automação de Ponto**, siga os passos abaixo:

1. Acesse o módulo de **Automação de Ponto** e vá em **Cadastros | Horários por Intervalo;**
2. Na tela de cadastro de horários, selecione a opção **Incluir;**
3. A janela de inclusão de horários será apresentada e defina o **Código do Horário**, **Descrição,**  **Data base** (data de referencia) e o **Tipo do Horário**. E informe as demais parametrizações conforme a regra de negocio a ser seguida;       
   ![2018-02-22_17_37_23-TOTVS_S_rie_T_Servi_os__RM__Alias__CorporeRM___1-TOTVS_SA.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360000812028)
4. Após preencher os campos básicos do horário, acesse a guia **Jornada** e clique no botão  **Processos | Criar jornada planejada,** e vai ser aberto um assistente para a criação da jornada;  
   ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10892478172695)
5. Ao abrir o assistente clique em avançar, e vai aparecer os seguintes passos:  
   - **Índice da jornada:** Associe a letra conforme o índice do horário, tenha como referência a data.   
   **![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10892701287063)**
6. **Tipo da Jornada:** Para cada índice devemos associar um tipo de jornada, onde:  
   **Trabalho**: Intervalo de horas normais que o funcionário deverá estar trabalhando, caso contrário será calculada falta ou atraso.  
   **Compensado**: Intervalo de horas que o funcionário deverá estar compensando, caso trabalhe será calculada hora extra de compensado.  
   **Descanso**: Intervalo de horas que o funcionário deverá estar descansando, caso trabalhe será calculada hora extra de descanso.  
   **Extra Normal (Batida Nula)**: Intervalo de horas que não são geradas horas normais para o funcionário e caso exista algum intervalo executado será calculada hora extra normal no dia.   
   ![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10893070192791)
7. **Intervalos Planejados da Jornada:** Os intervalos planejados da jornada podem ser as batidas de trabalho do horário que o funcionário deverá realizar, ou um intervalo de compensação ou mesmo de descanso para o funcionário.  
   **Lembre-se que para cada entrada deve existir uma saída correspondente.**  
   Além dos intervalos planejados nessa etapa é possível cadastrar os intervalos de tolerância para cada batida quando o tipo da jornada for de trabalho, as tolerâncias serão consideradas para cálculo de atrasos ou extras.  
   É possível então definir que nos dez minutos após a primeira batida do horário de trabalho não serão calculados atrasos, ou mesmo nos dez minutos que antecedem a primeira batida do horário de trabalho não serão calculadas extras, permitindo também que seja cadastrada um número de horas para abater a tolerância.  
   **Daqui em diante cada passo irá respeitar o tipo de horário escolhido, para mais detalhes acesse os links abaixo:**  
   [Jornada Planejada para Horário Rígido](https://tdn.totvs.com/pages/viewpage.action?pageId=452719134)  
   [Jornada Planejada para Horário Flexível](https://tdn.totvs.com/pages/viewpage.action?pageId=452718981)  
   [Jornada Planejada para Horário Núcleo](https://tdn.totvs.com/pages/viewpage.action?pageId=452718969)  
   [Jornada Planejada para Horário Semi-Flexível](https://tdn.totvs.com/pages/viewpage.action?pageId=452719135)      
   ![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10893189460247)
8. Após criar os intervalos de acordo com o tipo de horário definido, será apresentado um resumo do da jornada criada, e avance as etapa para concluir o processo;  
   ![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10893262677399)
9. Após a conclusão será apresentado o intervalo criado. Caso necessário, crie os demais as índices/jornadas para a composição do horário.  
   ![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10893293196695)  
    **Saiba Mais:**Para informações sobre os **parâmetros do horário**, acesse o documento [Parâmetros do Horário.](https://tdn.totvs.com/pages/releaseview.action?pageId=452719175)  
   Para informações sobre **jornadas** acesse o link [Jornadas](https://tdn.totvs.com/display/LRM/Jornada).  
   Para informações sobre os **tipos de horário** acesse o link [qual a diferença entre os tipos de horário por intervalo.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021943091-TOTVS-RH-Linha-RM-PTO-Qual-a-diferen%C3%A7a-entre-os-tipos-de-hor%C3%A1rio-por-intervalo)  
   Para informações sobre as **tolerâncias** acesse o link [como realizar o cadastro de tolerância no horário por intervalo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045915194-TOTVS-RH-Linha-RM-PTO-Como-realizar-o-cadastro-de-toler%C3%A2ncia-no-hor%C3%A1rio-por-intervalo)
