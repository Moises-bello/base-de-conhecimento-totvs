---
content_hash: e0c6621dd4a6a75ade93b75420c7965abfb70c336f21031154af3e7e20cdc619
fetched_at: '2026-06-29T00:09:16.845973+00:00'
page_id: '421385577'
product: rm
source: tdn-rm
title: WebService de Exportação de Dados de Folha Tarefa para Coletor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385577
version: 2
---

---

Para que o apontamento do Avanço Físico das tarefas do projeto seja efetuado é preciso que o coletor móvel associado esteja carregado com os dados das Folhas Tarefa.  
 A rotina de exportação de dados de Folha Tarefa para coletores carrega os coletores móveis com as Folhas Tarefa criadas no TOTVS Obras e Projeto, para que seja possível realizar os apontamentos de Avanço Físico das Tarefas. O WebService do TBC - TOTVS Business Conector, disponibiliza os dados de Folhas Tarefa cadastradas no TOTVS Obras e Projetos.  O processo de exportação é inicializado pelo Coletor, que fará a autenticação do usuário para ativar a exportação de Dados de Folhas Tarefa de acordo com o coletor associado.   
 O usuário acessa o Coletor Móvel e insere nome e senha para autenticar seu acesso, através de um WebService o sistema fará autenticação no TOTVS Obras e Projetos. Após a autenticação, caso possua Folha Tarefa associada ao coletor o sistema irá exportar todas as Folhas Tarefa geradas e associadas a este coletor móvel. O processo de exportação poderá ser iniciado pelo usuário ou por job agendado no coletor. Após a exportação dos dados da Folha Tarefa para o coletor, o status da mesma é modificado para "Carregada".  
    
 **Atenção:**

A exportação dos dados para o coletor atenderá às seguintes regras:

* Apenas Folhas Tarefa associadas a este coletor móvel e prontas para carga serão enviadas para o coletor móvel solicitante;
* Uma Folha tarefa poderá ser apontada e/ou carregada por todos os coletores a ela associados desde que o coletor esteja habilitado (ativo) e a função de apontamento esteja disponível para este coletor.  
   Caso ocorra algum problema no processo de exportação, será gerado um log de erros.   
   Após a transmissão de dados para o equipamento móvel, o WebService irá gravar em tabelas de "Log", os dados de Identificação do usuário logado no coletor, identificação do equipamento (IMEI), identificação do processo (Importação e Exportação dos dados), Data e Hora da exportação.
