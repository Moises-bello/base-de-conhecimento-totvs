---
content_hash: 40b379c6f11b94ee608860e40f1b21e342dbed60a44f952c071e32f743ea9253
fetched_at: '2026-06-29T00:09:14.718128+00:00'
page_id: '421385238'
product: rm
source: tdn-rm
title: Exportar para o MS Project
type: documentation
url: https://tdn.totvs.com/display/LRM/Exportar+para+o+MS+Project
version: 3
---

**Introdução**  
 O processo de Exportar projeto para MS-Project, está disponível através do menu: Planejamento >Integração com o MS Project> Exportar para o Project e consiste em filtrar cenário, planilha, selecionar opções da tela conforme necessidade e assim gerar um arquivo de exportação na extensão \*.MPP.  
  
**Processo**  
 Exportar Percentual Concluído:  
 Serão exportados para o MS Project o somatório dos percentuais constantes no módulo do Percentual Concluído do PERT de cada tarefa para a coluna Porcentagem (%) Concluída do MS Project.  
  
 Exportar Recursos Horários:  
 Serão exportados para o MS Project os recursos do construção e Projetos cuja unidade é hora e que estejam sendo utilizados em alguma tarefa do filtro de obras em questão.  
 Os preços dos recursos também são exportados. Eles são exportados para a visão Planilha de Recursos, campo "Taxa Padrão".   
 Os insumos do grupo de custo de mão-de-obra são exportados com o valor das leis sociais embutido.

**Exemplo:**  
O insumo que tem o preço unitário de 11,11 e a taxa de leis sociais é 2,345, o valor a ser exportado será 11,11 x 2,345 = 26,05.  
   
Exportar Recursos Materiais:  
Serão exportados para o MS Project os recursos do Construção e Projetos cuja unidade seja diferente de H. Os preços dos recursos também são exportados. Eles são exportados para a visão Planilha de Recursos, campo "Taxa Padrão".  
   
Exportar Somente Etapa:  
Serão exportadas somente as etapas.

**Observação:**  
Ao selecionar a opção "exportar somente etapas", as demais opções ficarão desabilitadas.  
  
Igualar Duração com a Quantidade das Tarefas:  
A quantidade das tarefas será exportada para o campo duração no MS Project.  
  
Igualar Trabalho com a Quantidade das Tarefas:  
A quantidade das tarefas será exportada para o campo trabalho no MS Project.  
  
Unidade da coluna duração  
Seta a unidade padrão da informação enviada para a duração, às opções serão:

* Meses
* Semanas
* Dias
* Horas
* Minutos  
  A informação padrão do parâmetro será Dias.

**Exemplo:**  
Uma tarefa que tem a duração no Construção e Projetos de 3 dias irá para o MS Project como:

* 0,15 Meses
* 0,60 Semanas
* 3 Dias
* 24 Horas
* 1440 Minutos  
    
  Como base para os cálculos será considerado o parâmetro de projeto do Construção e Projetos "Jornada". Se esse parâmetro estiver vazio será considerado automaticamente 8 horas como jornada diária de trabalho. Portanto, para se chegar na informação das horas foi feito o seguinte cálculo:  
  3 dias x 8 horas diárias de trabalho = 24 horas  
  3 dias x 8 horas diárias de trabalho x 60 qtde. de minutos = 1440 minutos  
  Aplicação de fator  
  Essa parametrização somente estará disponível se o parâmetro "Igualar duração com a quantidade das tarefas" ou o parâmetro "Igualar trabalho com a quantidade das tarefas" estiver habilitado. Ele vai interferir na coluna duração ou trabalho do MS Project, permitindo aplicar um fator no valor informado.  
  **Exemplo:**  
  Foi solicitado enviar a quantidade para a duração da tarefa, e determinada tarefa possui quantidade no Construção e Projetos de 221 und. Será então enviado para a coluna duração do MS Project 221 dias, mas se a aplicação de valor estiver parametrizada para multiplicar e o fator for 2, a coluna duração do MS Project receberá 442 dias.

**Observação:**  
 Tarefas com nome e descrição, o sistema deverá exportar a tarefa para o Project preenchendo a coluna "Nome da tarefa do Project" com a coluna Nome da tarefa do Totvs Obras e Projetos.  
  
 Tarefas sem o campo nome preenchido, mas com a Descrição preenchida, o sistema deverá exportar a tarefa para o Project preenchendo a coluna "Nome da tarefa do Project" com a coluna   
 Descrição da tarefa do Totvs Obras e Projetos.  
  
 Tarefas sem preenchimento de nome e descrição, o sistema deverá exportar a tarefa para o   
  
 Project preenchendo a coluna "Nome da tarefa do Project"  com a coluna Código da tarefa do Totvs Obras e Projetos.  
  
 Todas as atividades da planilha de tarefas serão enviadas para o MS-Project, inclusive as inativas.

**Atenção!**  
É possível gerar o arquivo de exportação com a extensão \*.MPP sem a obrigatoriedade da licença do Microsoft Project®, ou seja, mesmo que o ambiente não contenha a licença, o processo gera o arquivo de exportação.
