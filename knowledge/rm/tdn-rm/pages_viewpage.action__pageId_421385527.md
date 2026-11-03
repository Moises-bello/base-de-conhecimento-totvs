---
content_hash: bf5a8919f89b9c1d87337f281b3af66f011d72703d1d26307915971942d69a72
fetched_at: '2026-06-29T00:09:16.391372+00:00'
page_id: '421385527'
product: rm
source: tdn-rm
title: Sincronismo MS Project 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385527
version: 17
---

Para realizar o sincronismo, primeiramente é necessário que seja realizada a configuração dos parâmetros de importação em   na aba  . Para isso acesse: "Projeto | Construção & Projetos | Gerais | Configuração MS Project".   
Também deve ser feita a configuração dos   na  , e para isso, acesse: "Projeto | Construção & Projetos | Projetos (F6) | Integração | MS Project".  
Após estas configurações terem sido realizadas, será possível executar o sincronismo em: "Planejamento | Integração com o MS Project | Sincronismo com o MS Project".

Para que os dados a serem sincronizados estejam atualizados, recomenda-se fortemente que seja realizado o Cálculo do Projeto antes de se efetuar o Sincronismo.  
   
Serão apresentados os campos para configuração das preferências do usuário para realizar a sincronização, que são:  
   
**Criar novo arquivo:**Esse campo deve ser marcado se for necessário criar um novo arquivo. Quando o mesmo é marcado automaticamente o Plano Programado completo também é marcado e sincronizado.   
   
**Informe a localização do arquivo MS Project:** Este campo será utilizado para informar o local em que o arquivo novo será salvo caso o campo citado anteriormente esteja marcado, ou para selecionar o local em que se encontra o projeto que será sincronizado. Caso nos [Parâmetros](http://tdn.totvs.com/pages/viewpage.action?pageId=421385171) este setado um local do arquivo vinculado o sistema irá considerar.  
   
**Cenário:** Selecione o cenário a ser utilizado.   
   
**Planilha:** Selecione a planilha a ser utilizada, Atividades ou Serviços.   
   
**Prioritário (em caso de conflito priorizar):** Defina qual a preferência de sincronização, ou seja, determine se em caso de conflito prevalecerão os dados do Totvs Obras e Projetos ou os do MS Project.

   
**Plano Programado:**  
**Completo:** O plano programado Completo irá realizar o sincronismo entre os  campos Datas Inicio e Fim Programado e a Duração.   
**Duração:** O plano Programado Duração irá realizar o sincronismo entre a Duração Programada.  
    
**Plano Base:** O plano base irá realizar o sincronismo entre os seguintes campos TOP/ MS Project:   
Linha Base do arquivo é preenchida com as Datas Início e Fim Programada, estes dados não voltam para o PERT apenas é levado do Totvs obras e Projetos para o MS Project.  
Linha Base do arquivo é preenchido de acordo com a Linha Base do PERT, estes dados não voltam para o PERT apenas é levado do Totvs obras e Projetos para o MS Project.  
   
Ao sincronizar o Plano Base e o mesmo não possuir Data Inicio Base e Data Fim Base, o mesmo não será preenchido com a Data Início do Projeto.  
   
**Plano Real:** O plano real irá realizar o sincronismo entre os seguintes campos TOP/ MS Project:   
   
**Percentual Concluído:** O Percentual Concluído irá sincronizar os seguintes campos TOP/ MS Project:   
% Físico Concluído, estes dados não voltam para o PERT apenas é levado do Totvs obras e Projetos para o MS Project;  
   
**Ligações:** As ligações serão sincronizadas nos seguintes campos TOP/ MS Project:

Quando sincronizado, todas as atividades terão seu tipo no MS Project setadas como Unidade Fixa, sendo que as atividades que possuírem predecessão serão marcadas como agendamento automático e as que não possuírem predecessão serão marcadas como manual.

O Percentual Concluído das atividades serão enviados para a coluna %físico concluído do MS Project e as Datas Programadas do PERT serão enviadas para a Linha Base do MS Project respeitando sempre o [Parâmetro Geral](http://tdn.totvs.com/pages/viewpage.action?pageId=421385171) de Linha Base para envio da Duração e das Datas Programadas no Sincronismo com MS-Project.

A Data Fim realizado de uma etapa e obra será preenchida no Project apenas quando todas as suas atividades filhas forem concluídas. Desta forma esta data poderá ser diferente do PERT.

Na criação de um novo arquivo através do Sincronismo, será obrigatório o Plano Programado completo. No sincronismo terá disponível as opções de sincronismo completo ou apenas a Duração das atividades.

**Observação:**

A criação de um novo arquivo ou sincronismo respeita o Parâmetro de Projeto Arquivo do Project Vinculado caso esteja habilitado e preenchido em Projeto | Construção e Projetos | Projeto (ou atalho F6) | Integração | MS Project. Se preenchido o caminho e não exista o arquivo o sistema marca automaticamente a opção de Criar novo Arquivo.

Abaixo os campos sincronizados no MS-Project X TOP:

|  |  |  |  |
| --- | --- | --- | --- |
| Plano | PERT | Project | Base de Dados |
| Plano Programado | OLE\_LINK1OLE\_LINK2OLE\_LINK3OLE\_LINK4Data Início Programado | Início/ Start | DATAINICIOCALC |
|  | Data Fim Programado | Término/ Finish | DATAFIMCALC |
|  | Data Início Programado | Início Linha Base1  \* | DATAINICIOCALC |
|  | Data Fim Programado | Término Linha Base1  \* | DATAFIMCALC |
|  | Duração Programado | Duração/ Duration | DURACAOCALC |
|  | Data Início Cedo | Início Antecipado/ Early Start | DATAINICIOCEDO |
|  | Data Fim Cedo | Término Antecipado/ Early Finish | DATAFIMCEDO |
|  | Data Início Tarde | Início Atrasado/ Late Start | DATAINICIOTARDE |
|  | Data Fim Tarde | Término Atrasado/Late Finish | DATAFIMTARDE |
| Plano Base | Data Início Base | Início da Linha de Base/ Baseline Start | OLE\_LINK5OLE\_LINK6DATAINICIOBASE |
|  | Data Fim Base | Término da Linha de Base/Baseline Finish | DATAFIMBASE |
| Plano Real | Data Início Real | Início Real/ Actual Start | DATAINICIOREAL |
|  | Data Fim Real | Término Real/Actual Finish | DATAFIMREAL |
|  | Duração Real | Duração Real/Actual Duration | DURACAOREAL |
| Percentual Concluído | Percentual Concluído | %Concluído | PERCCONCLUIDO |
|  |  |  |  |
|  | Percentual Físico Concluído | %Físico Concluído | PERCCONCLUIDO |

Abaixo os Campos que são Sincronizados do TOP para o MS-Project:

| TOP | Coluna no MS-Project |
| --- | --- |
| Código da Tarefa | EDT |
| Valor Unitário \* Quantidade | Custo |

O Totvs Obras e Projetos (TOP) também envia para o MS Project os campos parametrizados no "Parâmetro Geral" da [Configuração MS Project](http://tdn.totvs.com/pages/releaseview.action?pageId=421385202). Ressaltando que, os campos parametrizados são enviados somente do TOP para o MS Project e não são sincronizados do MS Project para o TOP. Essas configurações funcionam para o Processo Sincronizar com MS Project .

**Atenção:** Somente são utilizados no Sincronismo, os campos abaixo sinalizados com **\***.

Os sincronismos dos campos Linha Base \* respeitará o Parâmetro geral de Linha Base para envio da Duração e das Datas Programadas no Sincronismo com o MS-Project. Este envio se faz necessário pois o MS-Project pode alterar o valor da Duração e das Datas Programadas. O campo é de apenas de escrita no MS-Project, sem o retorno destes valores no Sincronismo.

 Após realizar esse processo, tanto o projeto do Totvs Obras e Projetos (TOP) como o do MS Project estarão sincronizados.  
   
Somente arquivos gerados por este processo podem ser sincronizados, assim, caso o usuário realize a Exportação do arquivo através do antigo processo de "Exportar para o Project", e tente realizar o Sincronismo através do processo "Sincronismo com MS Project " o sistema não irá permitir e irá emitir uma mensagem informando "O arquivo informado foi gerado pelo processo de "Exportar para o project'. Gere um novo arquivo através deste processo."

**Observações:**  
   
A configuração do MS Project permite trabalhar com no máximo 2 (duas) casas decimais. Esta parametrização pode sofrer impacto no momento do cálculo total do custo do Projeto e Percentuais.  
   
Os Feriados cadastrados no Calendário parametrizado no TOP, são enviados para o Project no momento do Sincronismo para o campo Exceção do Calendário Padrão do Project.

A partir da versão 12.1.34, este sincronismo está homologado para funcionar com a versão do MS Project 2013, 2016, 2019 e 2021.

---
