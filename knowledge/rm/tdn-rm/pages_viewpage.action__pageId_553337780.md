---
content_hash: 1aaecf6f737f59be866a371d9e72e6a32c64f77735c0de1644bef191b6464015
fetched_at: '2026-06-29T00:10:44.815446+00:00'
page_id: '553337780'
product: rm
source: tdn-rm
title: RascunhosInstrução de Trabalho | Como Configurar um Board na Ferramenta JIRA?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=553337780
version: 1
---

5%90%10%90%

Caso seja necessário alterar a nomenclatura das colunas do *Board*, configurações dos cards entre outras opções, siga as instruções de configurações abaixo:

1. Acesse a ferramenta JIRA (**<http://jiraproducao.totvs.com.br/>**).
2. No menu superior, clique em ***Boards*** para consultar o *board* criado.
3. Após, clique no botão ***Board*** disponível ao lado direito da tela, opção ***Configure***.
4. Na opção ***General***, você visualiza o filtro do seu *board* que determina as *Issues* que serão visualizadas. Pode ser baseado em um projeto ou em um filtro(JQL) personalizado que poderá trazer mais de um projeto, dependendo de suas necessidades.
   1. Nesta opção, você pode compartilhar a administração do seu *board* com outro usuário, clicando no campo ***Administrator*** e incluindo o usuário desejado.
5. Na opção ***Columns***, as colunas podem ser adicionadas, removidas, reordenadas e renomeadas. As colunas são baseadas em status globais e podem ser movidas entre as colunas. Nos boards do tipo ***Kanban*** podem ser definidas restrições mínimas e máximas para cada coluna mapeada.
   1. As colunas padrões são: *To Do, In Progress, Done*.
   2. Para adicionar uma nova coluna, clique na opção ***Add column***.
   3. Para tarefas serem apresentadas na coluna um status deve ser associado. Para isso é necessário arrastar um status para a nova coluna.
   4. É possível alterar a ordem das colunas também clicando sobre essas e arrastando para alterar a ordem.  
        
        
      Importante: Nos *boards* do tipo *Scrum*, os status que estiverem na última coluna(direita) serão considerados como concluídos, ou seja, irá realizar a baixa do *burndown* na *Sprint*.
6. Na opção ***Card layout***, é possível configurar até três campos adicionais que deseja visualizar no seu board.
   1. Os campos podem ser diferentes para o *Backlog* e para os *Active Sprints*, caso esteja utilizando um *Scrum Board*.
   2. Para incluir um campo no *card* do seu *backlog*, consulte o campo desejado na opção ***Field name*** e clique no botão ***Add***.
   3. Para incluir um campo no *card* da sua *active sprints*, consulte o campo desejado na opção ***Field name*** e clique no botão ***Add***.
   4. Para visualizar a criação de um *Board* e sua configuração na ferramenta JIRA, consulte o vídeo *[How to](http://fluig.totvs.com/portal/p/10097/videos/qualidadedesoft3300/5235839/5235845)*.

   As demais opções de configuração do *Board* são:

1. 1. **Swimlanes:** configura se haverá linhas de “raia” dividindo as subtarefas no *Board*. A configuração padrão separa as linhas de “raia” por *Story*.
   2. **Estimation:** configura como será tratada a estimativa de esforço no *Board*, poderá ser em horas ou *Story Point*. Essa informação é importante para a configuração dos *Reports* do *Board*.
   3. **Working Days:** configura os dias úteis utilizados para a execução das tarefas do *Board*.
   4. **Issue Detail View:** configura os dados das tarefas apresentadas na opção de visualização rápida do *Board*.
   5. **Card Colors:** configura as cores dos *cards* (tarefas) apresentados no *Board*.
   6. **Quick Filters:** opção de criação de filtros exibidos na parte superior da página do *Board*.

**Dicas**

1. As *Issues* criadas com status *backlog* são incluídas automaticamente no *backlog* do produto.
   1. As *issue types* *Story*, Manutenção, Legislação e Ponto de Entrada já iniciam no status *backlog*.
2. O Product Owner deve priorizar o que será entregue no próximo *release*.
3. Caso um item seja retirado do *backlog* do produto, este deve ser cancelado ou voltar para o *status* banco de ideias.
   1. No EPIC está disponível no *status* banco de ideias.
5%
div.theme-default .ia-splitter #main {
margin-left: 0px;
}
.ia-fixed-sidebar, .ia-splitter-left {
display: none;
}
#main {
padding-left: 10px;
padding-right: 10px;
overflow-x: hidden;
}
.expand-control-text {
color: #000000;
font-size: 13px !important;
font-weight:bold !important;
}
.expand-icon, .aui-icon, .aui-icon-small, .aui-iconfont-chevron-right {
color: #FF8000;
}
.aui-header-primary .aui-nav, .aui-page-panel {
margin-left: 0px !important;
}
.aui-header-primary .aui-nav {
margin-left: 0px !important;
}
]]>
