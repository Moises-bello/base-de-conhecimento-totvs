---
content_hash: 59c0643c03b7123129a40a2c34ae538dc08ee5876012a6ee54baa0c6ce66ee47
fetched_at: '2026-06-29T00:09:25.156530+00:00'
page_id: '423938042'
product: rm
source: tdn-rm
title: Andamento da Ordem (Apontamento)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938042
version: 10
---

Nessa tela é possível acompanhar o andamento de uma ordem de produção.  
A tela de Andamento de Ordens de Produção é dividida da seguinte forma:  
Na parte superior está disponível a grid que permite visualizar as informações da Ordem de Produção escolhida.   
A grid central permite visualizar os Itens de Ordem que compõem a ordem selecionada na grid superior, também está disponível o Mapa de Engenharia do Item da Ordem (Acabado e Semiacabado). Na grid inferior são apresentadas as Atividades do Item de Ordem selecionado.

**Informações da Ordem de Produção**

Pode-se selecionar a ordem de produção digitando o código da mesma ou localizando a mesma através do campo de busca. Estarão disponíveis para escolha ordens contempladas pelo filtro executado no momento.  
***Atenção!*** Ao acessar o Andamento de Ordem a partir da visão de ordens, será visualizada somente a ordem de produção que estiver selecionada na visão de ordens e não haverá possibilidade de escolha de outra ordem e utilização de filtros.   
Seleção de ordens, navegação entre registros e filtros serão disponibilizados quando o acesso ao Andamento de Ordem não for realizado a partir da visão de ordens.

**Mapa Engenharia**

Ao selecionar um acabado ou semiacabado no Mapa da Engenharia, as atividades serão filtradas na grid Atividades do Item de Ordem. Ao clicar sobre o acabado ou semiacabado, com botão direito do mouse temos a opção para "Mostrar Todas as Atividades", que serão visualizadas na grid Atividades do Item da Ordem.  
***Atenção!*** O sistema irá explodir a estrutura do semiacabado no Mapa da Engenharia se houver necessidade de fabricação do mesmo (estoque igual a zero ou saldo insuficiente).

**Item de Ordem**

Nessa grid serão apresentados os itens de ordem conforme ordem de produção selecionada.  
Atividades Opcionais podem ser inseridas para o item de ordem através do Processo disponível nessa grid.  
É possível configurar colunas, navegar entre registros e procurar item de ordem através dos campos da grid.   
O parâmetro "Exibir apenas registros da procura", quando marcado, irá filtrar somente os registros que contêm a chave de pesquisa.

**Atividades Item de Ordem**

São apresentadas as atividades do item de ordem selecionado.  
Os processos da grid de Atividades do Item da Ordem permitem iniciar e interromper atividade, excluir atividade opcional, cancelar atividade, substituir atividade, transferir materiais entre atividades e reativar atividade.   
É possível configurar colunas, navegar entre registros e procurar atividade através dos campos da grid.

**Localização por Código de Barras**  
 No rodapé da tela está disponível o campo para leitura de código de barras, através da leitura do código de barras nesse campo é possível localizar um item de ordem e atividade desejada.  
   
 Layout de Código de Barras para localização de item de ordem e atividade:  
 ID!OP-0025/11!001.01.02!BASE!1  
***Onde**:*  
 ***ID: Identificador padrão de início de código de barras***  
 *OP-0025/11 = Código da Ordem*  
 *!: Separador Padrão*  
 *001.01.02 = Código da Estrutura*  
 *BASE: Código do Modelo da Estrutura*  
 *1: Identificador da atividade.*

---
