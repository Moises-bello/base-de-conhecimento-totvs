---
article_id: 11467075990807
category: Cálculo
content_hash: 3f72ac05e88857cdf084478e6a0797db929677e002d7fdd8f5730e40caeb6726
fetched_at: '2026-06-28T22:46:29.184864+00:00'
product: rm
section_id: 1500000861662
source: central-rm
title: RH - RM - PTO - Batidas com jornada referência errada após realização de recálculo
type: support-article
updated_at: '2026-05-29T12:20:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11467075990807-RH-RM-PTO-Batidas-com-jornada-refer%C3%AAncia-errada-ap%C3%B3s-realiza%C3%A7%C3%A3o-de-rec%C3%A1lculo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18493387445911) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Ao realizar o recálculo do ponto, as batidas perdem a data de referência. O que fazer?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto- Todas as versões  
  
**Solução**

Abaixo segue as recomendações mais usuais de parametrização, para que ao importar as batidas a jornada de referência seja aplicada no cálculo:

1. Acesse o menu **Configurações | Parametrizador | Funcionário** e selecione o funcionado desejado e edite. Avance até etapa **12- Jornada Referência,** e defina como será realizado o cálculo da jornada de referência da batida:   
     
   **- Com base na data batida (Recomendamos a utilização deste parâmetro no caso de horário noturno)**  
   Marque a flag do parâmetro**: Considera a data do intervalo executado para definir jornada de referência**  
   **![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11465843430423)**  
     
   **- Caso seja com base na aproximação do horário planejado:**  
     
   **Marque a flag do parâmetro: Define se a jornada referência do intervalo executado por aproximação:** Caso o intervalo executado não faça interseção com o intervalo planejado atual(Horário planejado) é feita a seguinte conta: Fim do último intervalo executado da jornada que está sendo verificada + o valor (recomendamos o valor de 02:30) a ser informando no campo.  
     
   **Tempo considerado na continuação da jornada:** Informe a quantidade de horas desejadas no parâmetro **'Tempo de acréscimo para jornadas sem trabalho ao se definir a jornada de referência do intervalo executado',** recomendamos que o tempo preenchido seja de 06:00**.**  
   **![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11465543738135)**  
     
   **Observação**: O tempo informando irá variar de acordo com cada jornada. O cálculo para chegar ao número de horas, ​que deve ser informando no campo, é o seguinte:

   Encontre a diferença da jornada anterior com a jornada posterior e divida por 2.  
   Pegue resultado subtraia pela quantidade de horas de acréscimo informado campo **'**Tempo de acréscimo para jornadas sem trabalho ao se definir a jornada de referência do intervalo executado' da etapa 12- Jornada de Referência. O tempo de acréscimo será considerado para alocação das batidas que fazem interseção com a jornada de trabalho. Exemplo:

   Considerando que está definido o valor de 3:00, as batidas serão alocadas no dia 16/07/2021 somente se a batida de saída ocorre até as 09:20 do dia 17.

   Como a saída ocorreu as 06:37, a batida será considerada para a jornada de trabalho.

   ![](https://tdn.totvs.com/download/attachments/452719137/image2022-7-21_10-40-18.png?version=1&modificationDate=1658410818590&api=v2)

   ![](https://tdn.totvs.com/download/attachments/452719137/image2022-7-21_10-41-5.png?version=1&modificationDate=1658410865377&api=v2)

   Caso deseje alterar os parâmetros dos funcionários de forma global acesse o link abaixo:  
   [RH - RM - PTO - Alteração global de parâmetros dos funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019945111-TOTVS-RH-Linha-RM-PTO-Como-fazer-a-altera%C3%A7%C3%A3o-global-de-par%C3%A2metros-dos-funcion%C3%A1rios)
2. Acesse o menu: **Configurações | Parametrizador | Sindicato** e selecione o sindicato vinculado ao funcionário. Avance até etapa 12**- Jornada Referência** e valide o parâmetro **'Quebra intervalo executado entre jornadas planejadas que fazem interseção' irá ficar marcado ou não.** Este parâmetro deve ser utilizado para definir como o sistema deve considerar o cálculo da jornada do funcionário conforme as batidas efetuadas por ele e sua jornada planejada. Por default a flag virá marcada, mas o utilize conforme sua regra de negócio.    
   **![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11465945613847)**
3. Acesse o menu **Cadastros | Horários por Intervalo** e selecione e edite o horário vinculado ao funcionário e valide se a flag **Considerar a data final da jornada como data referência.** Por default esse parâmetro virá desmarcado e o sistema irá considerar a movimentação do funcionário com base na data de entrada da jornada, caso ele seja marcado será considerada a data final da jornada. Marque conforme sua regra de negócio.    
   ![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11466508732439)

**Saiba Mais:**  
Parametrizador Funcionário: [Jornada Referência](https://tdn.totvs.com/pages/viewpage.action?pageId=452719137)  
Parametrizador Sindicato: [Jornada referência](https://tdn.totvs.com.br/pages/releaseview.action?pageId=634488105)  
Parametrizador horário: [Considerar a data final da Jornada como data referência](https://tdn.totvs.com/pages/viewpage.action?pageId=555272447)  
[O que fazer para que o ajuste data de referência da batida não seja desfeito?](https://totvssuporte.zendesk.com/knowledge/articles/11484794648215/pt-br?brand_id=1509248)  
[Batidas desposicionadas (natureza errada) no processo de importação de batidas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042820233)
