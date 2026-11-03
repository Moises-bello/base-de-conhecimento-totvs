---
content_hash: 21f993a2be3c567b25562c4fff99744fc7bd71e25ad8e0b957d89096ad0498f8
fetched_at: '2026-06-29T00:09:14.174037+00:00'
page_id: '421385143'
product: rm
source: tdn-rm
title: Alocação de Recurso
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385143
version: 2
---

A alocação de membros de uma determinada equipe à uma determinada tarefa, se dará através do anexo na planilha de atividades: "Timesheet - Alocação de Recursos". Para que esse anexo esteja disponível o   "Utilizar Alocação de Membros de Equipes nas Tarefas de Timesheet" deverá estar marcado. Nesse novo anexo, será possível informar o membro e a quantidade de horas alocadas para o respectivo membro. Os membros disponíveis serão os mesmos relacionados aos insumos da tarefa. Sempre que um nova linha for inserida nesse anexo a quantidade padrão deverá ser o saldo da quantidade programada para o insumo menos a quantidade já alocada para o mesmo.

Exemplo:

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  | **Quantidade** | **Total** |
| Tarefa: 001.01.01 - Compatibilização de Projetos |  |  |  |  |  |  |  |  |  | 100 | **100** |
|  | Recurso: |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Composição: |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | Insumo: ISM001 - ENGENHEIRO |  |  | 1,00 | **100** |
|  |  |  |  |  | Insumo: ISM002 - ESTAGIÁRIO |  |  | 0,50 | **50** |

|  |  |  |
| --- | --- | --- |
| **Insumo** | **Membro** | **Quantidade** |
| ISM002 - ESTAGIÁRIO | MARIA APARECIDA | 50 |
| ISM001 - ENGENHEIRO | JOSÉ DA SILVA | 60 |
| ISM001 - ENGENHEIRO | JOÃO DE SOUZA | **40** |

A quantidade de horas dos insumos da tarefa não deve, necessariamente, corresponder ao total de horas da tarefa. No exemplo acima pode ser observado que o total de horas dos recursos ultrapassa as horas da tarefa. Para uma tarefa de 100 horas, são necessárias 150 horas de ENGENHEIRO e de ESTAGIÁRIO.  
 Conforme demonstrado acima, ao incluir o membro JOÃO DE SOUZA, a quantidade apresentada será de 40 horas, pois, o total necessário é de 100 horas, porém a quantidade já alocada para o membro JOSÉ DA SILVA é de 60 horas estando disponível apenas as 40 horas para a alocação.  
 As informações de alocação são armazenadas nas mesmas tabelas de dados da alocação de recursos padrão do sistema presente nos anexos da planilha de atividades, e a quantidade alocada é distribuída entre os períodos nos quais a tarefa faz parte.

**Algumas consistências devem ser consideradas:**

 Somente atividades do tipo serviço e do tipo timesheet poderão receber alocações, um alerta deverá ser exibido caso a alocação seja feita pra etapas ou obras; • A alocação só será realizada se existirem insumos associados à tarefa pois os membros são filtrados a partir desta associação; • Apenas responsáveis por equipes podem alocar membros em tarefas; • Não será possível salvar alocações com quantidade igual a 0 (zero); • Não será possível alterar as alocações de tarefas que estejam em execução; • A tarefa deve ter as datas inicial e final definidas; • É necessário existir períodos de cronograma para realizar a alocação; • A quantidade total alocada para os membros não pode ultrapassar a necessidade do insumo na tarefa; • Deverá ser criado um controle de segurança, sendo item da planilha de atividades para o anexo de alocação.

**Importante**  
Se o anexo de alocação não for utilizado, de acordo com o parâmetro, a alocação a ser considerada levará em conta a associação do insumo à tarefa, assim como os apontamentos, execução de tarefas e acompanhamento de projetos, porém a existência de membros de equipes associados aos insumos é necessário para que os apontamentos possam ser registrados pois é através destes que se conhece o usuário. Portanto existem duas formas de alocação: através da relação Membro de Equipe/Insumo/Tarefa e através da Alocação de Membros, sendo que serão norteados pelo parâmetro de "Utilizar Alocação de Membros de Equipes nas Tarefas de Timesheet".

Informações Complementares

Timesheet  
    
 Equipe de Timesheet  
    
 Monitor de Tarefas  
    
 Apontamento em tarefas  
    
 Tarefas de Timesheet e Recursos  
    
 Análise de Valor Agregado  
    
 Gestão de Riscos  
    
 Contratos de Timesheet  
    
 Contrato de Insumo  
    
 Parâmetros Gerais  
    
 Parâmetros do Projeto  
    
 Parâmetros do Projeto - Contratos  
  

|  |  |
| --- | --- |
|  | Como Fazer |

---

Executar/Parar Apontamento via Barra de Ferramentas  
    
 Parâmetros Gerais - Timesheet  
    
 Parâmetros do Contrato- Timesheet
