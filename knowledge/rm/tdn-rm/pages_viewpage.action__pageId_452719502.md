---
content_hash: 84a002f0c306351f9f701c9c202f9053f5c29ed274eb60e608495055cea98ff9
fetched_at: '2026-06-29T00:10:08.047668+00:00'
page_id: '452719502'
product: rm
source: tdn-rm
title: Composição Salarial / Atividades Remuneradas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719502
version: 2
---

Neste menu serão demonstrados os eventos Reprogramados de Salário Composto, e os eventos reprogramados de Atividades Remuneradas por funcionário, com os respectivos valores e horas.  
 **Observação**  
 Este menu será habilitado somente quando o parâmetro "Usa salário hora / Jornada fixa" estiver desmarcado em Opções | Parâmetros | RM Labore | Gestão Educacional.  
 Através da edição é possível controlar:  
     
 **Salário Composto**  
 Nesta pasta serão visualizados todos os eventos que "compõe salário", que sofreram reprogramação salarial, ou que foram cadastrados manualmente pelo cadastro de funcionários, ou por este menu.  
 **Observação**  
 Ao excluir um determinado salário composto, o sistema abrirá uma janela solicitando a data da mudança e o motivo de alteração para inserir um registro no histórico salarial do funcionário com o salário composto e jornadas iguais a zero.  
 **Eventos**  
 Nesta visão é permitido incluir, excluir e configurar colunas dos eventos que compõem salário composto.  
 **Eventos por centro de custo**  
 Nesta visão é permitido incluir, excluir, editar e configurar colunas dos eventos que compõem o salário composto com seus respectivos centros de custos.  
 Caso o registro visualizado tenha sido gerado pela reprogramação salarial, o centro de custo associado ao evento é de origem da parametrização do RM Classis.  
 Serão visualizados eventos por centro de custo, caso o parâmetro "Reprogramação Salarial discriminada por Centro de Custo" do RM Labore da Gestão Educacional estiver marcado.  
 **Eventos relacionados**  
 Nesta visão é permitido incluir, excluir, editar e configurar colunas dos eventos relacionados aos eventos que compõem o salário composto.  
 Eventos relacionados que tenham sido cadastrados ou alterados manualmente, não serão reprogramados pelo módulo de Reprogramação Salarial.  
 **Observação**  
 Os botões Incluir\Excluir\Editar serão habilitados respeitando primeiramente o acesso a menus.   
 Estando habilitados no perfil de usuários, serão consideradas as regras abaixo  
 **Eventos**  
 Inserir: Sempre estará habilitado.  
 Editar: Não estará disponível. Deverá ser editado o evento por centro de custo. Somente ficará habilitado se não existir registro na janela de Salário composto.  
 Excluir: Somente será habilitado se não existir evento por centro de custo.   
 **Eventos por centro de custo**  
 Inserir: Estará habilitado somente se existir um evento cadastrado.  
 Editar: Estará habilitado somente se existir um evento cadastrado.  
 Excluir: Estará habilitado somente se existir um evento cadastrado e se não existir evento relacionado.  
 **Eventos relacionados**  
 Inserir Estará habilitado somente se existir um evento por centro de custo cadastrado  
 Editar: Estará habilitado somente se existir um evento relacionado. (Não será possível alterar o centro de custo do evento)   
 Excluir: Estará habilitado somente se existir um evento relacionado.  
 O centro de custo do evento relacionado não pode ser alterado.  
    
    
 **Pasta Atividades Remuneradas**  
 Nesta pasta serão visualizados todos os eventos que "não compõe Salário", que sofreram reprogramação ou foram cadastrados manualmente neste menu.  
    
 **Eventos**  
 Nesta visão é permitido incluir, excluir e configurar colunas dos eventos que serão considerados como "Não Compõe Salário", sendo apenas caracterizado como uma atividade Remunerada: Extra Classe ou Complementar.  
 **Eventos por centro de custo**  
 Nesta visão é permitido incluir, excluir, editar e configurar colunas dos eventos considerados como "Não Compõe Salário" com seus respectivos centros de custos.  
 Caso o registro visualizado tenha sido gerado pela reprogramação salarial, o centro de custo associado ao evento é de origem da parametrização do RM Classis.  
 **Observação**

* Serão visualizados eventos por centro de custo, caso o parâmetro "Reprogramação salarial detalhada por Centro de Custo" do RM Labore da Gestão Educacional estiver marcado.
* O campo Quantidade de Alunos, terá seu valor preenchido com zero, caso o parâmetro "Ratear pagamento de professores da turma/disciplina por Centro de Custo" Gestão Educacional  estiver desmarcado, Caso o parâmetro for marcado, o sistema seguirá a seguinte regra: [Parametrizador (Educacional)- Ratear pagamento de professores da turma/disciplina por Centro de Custo](http://tdn.totvs.com/display/LRM/Rateio+da+Folha+de+Pagamento+do+professor+por+centro+de+custo) .
