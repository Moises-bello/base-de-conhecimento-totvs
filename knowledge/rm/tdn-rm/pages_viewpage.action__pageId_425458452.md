---
content_hash: 2c6fad146402e2640a165be22c1425ff6ed660bad96f0da679bd5b1c0d0708c5
fetched_at: '2026-06-29T00:09:30.373761+00:00'
page_id: '425458452'
product: rm
source: tdn-rm
title: Estatística de Atendimentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458452
version: 2
---

**Estatística de Atendimentos**

---

A Estatística de Atendimentos permite apresentar um relatório dos atendimentos com seus respectivos status. Além do atendente responsável, alarmes, repasses e conclusões. Todos os atendentes configurados serão apresentados na relação, vale ressaltar que existe um Serviço que deverá ser executado (conforme configuração de recorrência) para atualizar as informações.   
    
 Para facilitar a visualização, quatro filtros estarão disponíveis para apresentação dos registros:  Atendente, Atendente por período, Hierarquia, Hierarquia por Período.  
    
 Filtro Atendente:  
 Busca os atendentes existentes na coligada (logada) e aguarda seleção do atendente para apresentar o relatório.  
    
 Filtro Atendente por período:  
 Busca os atendentes da coligada (logada), aguarda seleção do atendente e do período: data inicial e final para apresentar o relatório.  
    
 Filtro Hierarquia:  
 Busca as hierarquias existentes da coligada (logada) e aguarda a seleção da mesma para gerar o relatório de todos os atendentes pertencente a esta hierarquia.  
    
 Filtro Hierarquia por período:  
    
 Busca as hierarquias existentes da coligada (logada), aguarda a seleção da mesma e o período: data inicial e final para gerar o relatório de todos os atendentes pertencente a esta hierarquia.  
    
 Vale ressaltar que não haverá edição disponível por se tratar de informações para consulta e que somente os atendentes que apresentarem o parâmetro "Gerar Estatística para este Atendente" marcado no cadastro (de atendente) serão listados.  
    
 Os relatórios apresentados serão no máximo diários, ou seja, se o serviço for executado mais de uma vez no dia, ele só atualiza o existente, ou pode ser configurado para rodar de 2 em 2 dias, semanalmente, só existe restrição para mais de uma vez por dia, pois o campo data é chave primária e isso impede dois registros(data) iguais, se forem iguais ele atualiza os dados existentes.
