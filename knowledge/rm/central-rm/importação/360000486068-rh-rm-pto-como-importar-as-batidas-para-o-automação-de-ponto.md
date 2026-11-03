---
article_id: 360000486068
category: Importação
content_hash: 4e5b15ffc196311846282d5ba79b2901f08f8aa92cc91a30eab67aae693d8d6e
fetched_at: '2026-06-28T22:46:33.752035+00:00'
product: rm
section_id: 6045469428631
source: central-rm
title: RH - RM - PTO - Como importar as batidas para o Automação de Ponto
type: support-article
updated_at: '2026-01-02T20:13:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000486068-RH-RM-PTO-Como-importar-as-batidas-para-o-Automa%C3%A7%C3%A3o-de-Ponto
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16646846600471) Tempo aproximado para leitura: 00:01:30 min  
  
Dúvida**Como importar o arquivo AFD (Arquivo de Fonte de Dados) ou um arquivo de batidas customizado gerado pelo relógio de ponto (terminal de coleta) para o Automação de Ponto?

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - Todas as versões

**Solução**

Para realizar a importação das batidas, siga as instruções a seguir:

1. Acesse o menu **Entrada de Dados | Layout** no módulo de Automação de Ponto e proceda com o cadastro do layout desejado. Que pode ser de acordo com o layout AFD (Arquivo de Fonte de Dados) das portarias 671, que consideram o CPF e/ou PIS, ou 1510 que considera o PIS, ou um layout customizado que pode considerar a chapa ou crachá.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21836826474263)  
     
   No link a seguir, você encontrará os passos para cadastrar o layout customizado: [RH - RM - PTO - Cadastrar layout do terminal de coleta do Automação de Ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000485588)
2. Acesse o menu **Entrada de Dados | Cadastros** e realize o cadastro do terminal de coleta.   
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21836795602071)
3. Acesse o menu **Entrada de Dados | Importar**.   
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21836795611159)  
     
   Ao abrir a tela, é **obrigatório** especificar nos campos **"Arquivo para importação"** o local onde o arquivo .txt está armazenado, e preencher os campos **"Layout do Relógio"** e **"Terminal de Coleta para Histórico"**. Os demais campos devem ser preenchidos de acordo com suas necessidades.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21836795624983)

A seguir estão os detalhes relativos a cada campo:

* **Arquivo para importação:** O arquivo de importação deve ser do tipo texto para que o sistema possa lê-lo durante a importação.
* **Layout do Relógio:** Selecione o layout criado para a importação.
* **Na seção Grupo de Funcionários:** Especifique uma seção ou aplique filtros conforme necessário.
* **Período de Importação:** Por padrão, as datas de início e fim do período ativo serão exibidas nos campos correspondentes.
* **Terminal de Coleta para Histórico:** Escolha o terminal de coleta desejado. Em casos de layout personalizado, o terminal de coleta pode estar incluído, e a importação validará a utilização desse terminal pelo funcionário.
* **Considerando o período:** A primeira batida do período a ser importada não levará em conta a última batida do período anterior. O sistema calculará a natureza verificando se existe uma batida anterior menor que a batida a ser importada somente no período. Se existir, a natureza será oposta à da batida anterior. Caso não haja nenhuma batida no período, o sistema calculará a natureza com base na proximidade da natureza do horário planejado, assim como é feito na importação considerando o horário planejado.
* **Considerando o horário planejado:** A importação levará em conta o horário planejado para o dia, ou seja, o horário cadastrado para o funcionário. A natureza será calculada com base na proximidade da natureza do horário planejado. Se o horário estiver cadastrado como saída na primeira batida do dia, esta será importada como saída.
* **Considerando a jornada:** As batidas terão sua natureza calculada de acordo com a(s) jornada(s) planejada(s) do funcionário. Em vez de considerar a proximidade da natureza, será considerada a proximidade da jornada planejada. Isso aborda situações em que o funcionário tem mais de uma jornada planejada no dia ou mesmo funcionários com jornadas que se estendem de um dia para o outro.  
  **Observação:** Caso não selecione nenhum dos parâmetros para definir a natureza, o sistema verificará a natureza da última batida do período anterior para determinar a natureza da primeira batida do período a ser importada.
* **Não alterar a natureza das batidas que ultrapassem xx:xx horas:** Indique a quantidade de horas após as quais a natureza das batidas não deve ser alterada.  
  **Considerar Natureza Fixa:** A natureza da batida será fixada como Entrada ou Saída se o tempo mínimo entre as batidas (parametrizado no campo anterior) for ultrapassado ou se não houver batidas até 3 dias anteriores. Este parâmetro será habilitado somente se o parâmetro 'Acerta Natureza Considerando o Período' estiver marcado e o campo 'Não alterar a natureza das batidas que ultrapassem xx:xx horas' estiver preenchido. Ao utilizar este parâmetro, a importação será realizada em um único lote para ordenar as batidas, independentemente da quantidade de linhas no arquivo, o que pode afetar o desempenho.
* **Priorizar crachá e não chapa para importação de batidas:** A importação utilizando o layout de relógio personalizado fará referência à chapa ou ao código do crachá. Se marcado, a importação considerará o crachá associado ao funcionário em vez da chapa.
* **Considera a última linha importada**: Este parâmetro deve ser utilizado para a importação automática de batidas. A importação automática é realizada a partir do agendamento de processos dos serviços (jobs) para programar a importação de batidas. Ao processar a importação agendada, o arquivo será lido e a última linha importada será validada. Em uma segunda etapa, o agendamento dessa importação será realizado para evitar a importação repetida de batidas já importadas no processo anterior.
* **Executar recálculo do funcionário após importação:** Ao selecionar esse parâmetro, o sistema executará o processo de cálculo do ponto após a importação, utilizando o mesmo filtro de funcionário e considerando a parametrização mencionada.    
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21852111206423)
* **Exibição de informação de inatividade do funcionário no log**: Os funcionários em período de férias ou afastados terão suas batidas importadas normalmente. Ao final do processo, um aviso será apresentado para as datas em que o funcionário deveria estar ausente

**Importante:**

* Se o funcionário estiver bloqueado, possivelmente devido a alterações manuais em sua movimentação, a importação não será realizada.
* É possível cadastrar o tempo mínimo entre batidas no sindicato do funcionário. As batidas seguidas, cuja diferença seja menor que o tempo estipulado, serão desconsideradas na importação.
* Os campos "Utiliza Integração com TSA" e "Utiliza Integração com a Carol", ficam habilitados somente em casos integração com esses aplicativos.
* A customização é utilizada para considerar a chapa ou número do crachá ao importar as batidas de visitantes ou batidas específicas de refeição. Para obter mais informações sobre o cadastro de layout, consulte os links de referência em "saiba mais".

**Saiba Mais**[TDN - Terminais de Coleta](https://tdn.totvs.com/display/LRM/Terminais+de+Coleta)[TDN - Layout de Relógio](https://tdn.totvs.com/pages/viewpage.action?pageId=452718923)[TDN - Importação de Batidas](https://tdn.totvs.com/pages/releaseview.action?pageId=452719301)  
[RH - RM - PTO - Cadastrar layout do terminal de coleta do Automação de Ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000485588)  
[RH - RM - PTO - Realizar a importação automática de batidas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014195451)
