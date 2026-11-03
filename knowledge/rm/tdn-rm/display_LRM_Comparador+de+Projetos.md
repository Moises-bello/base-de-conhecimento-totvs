---
content_hash: 948cc0340b0d6c905273a4d4b4ae3ac71897f5146a0a27af15de18f729b169e8
fetched_at: '2026-06-29T00:09:15.463946+00:00'
page_id: '421385385'
product: rm
source: tdn-rm
title: Comparador de Projetos
type: documentation
url: https://tdn.totvs.com/display/LRM/Comparador+de+Projetos
version: 15
---

---

Originalmente o comparador de projetos foi criado com a finalidade de comparar um projeto com sua revisão. Assim, o primeiro passo era a geração de projeto "Filho"(revisão), através da tela de Projetos, Processos -  "Revisão do projeto". A partir de então, as alterações necessárias seriam feitas no projeto "Filho"( Revisão), e havendo necessidade seria possível comparar o projeto "Principal" com o projeto "Revisão".

**Atualmente o comparador de projeto, permite também a comparação entre projetos que não são de revisão, ou seja, é possível comparar quaisquer projetos, inclusive projeto de outra coligada.**

As opções de comparação disponíveis são: Planilha de Atividades, Planilha de Serviços, Composições, Insumos, Parâmetros e Cenários:

**Planilha de Atividades**

Acessando um dos projetos e clicando no menu Projeto | Comparador de Projetos | Planilha de Atividades, será carregada a tela do comparador de projetos, onde o usuário deverá informar a coligada e o projeto, cuja planilha de atividades será comparada com a do projeto corrente:

Após informar o projeto, o usuário deverá clicar no botão "Confirmar comparação":

E os dados das planilha de atividades de ambos os projetos, serão carregados conforme a tela abaixo. A visão fica dividida em duas partes, uma para o projeto "Pai" (Projeto Principal), à esquerda; e outra para o projeto "Filho" (Revisão), à direita. Para visualizar apenas as diferenças entre os projetos, clique no botão do filtro em destaque abaixo (1):

Conforme destacado na legenda acima (2), o comparador indica o que foi alterado, deletado ou inserido na visão. Nas cores vermelha (Alterado), azul (Deletado) e verde (Inserido).

Através dos ícones das setas "Próxima alteração"  e "Alteração anterior", sinalizados abaixo, será possível navegar entre as diferenças apontadas no comparador:

Importante

A comparação é sempre entre dois projetos: o projeto aberto e o projeto selecionado no respectivo campo.  Conforme destacado na legenda, as linhas dos registros deletados em algum dos projetos ficarão em azul, dos registros alterados ficarão em vermelho em ambos e dos registros inseridos, em verde no projeto em que foi incluído, facilitando a identificação.

Ao acessar a tela do comparador para a Planilha de Atividades, algumas comparações poderão ser realizadas para o registro selecionado da planilha como: Composições, Insumos e Cronograma previsto da tarefa selecionada:

Só será exibido à tela do comparador de composição, caso o recurso associado à tarefa selecionada na tela anterior seja uma composição:

Da mesma forma, para visualização de insumo:

Somente será exibido à tela do comparador de insumo, caso o recurso associado a tarefa selecionada na tela anterior seja um insumo.

E ao clicar no botão Cronograma Previsto, será exibido comparador do cronograma caso a tarefa tenha cronograma previsto informado:

**Planilha de Serviços**

Acessando a opção do comparador para a Planilha de Serviços (Projeto | Comparador de Projetos | Planilha de Serviços), as comparações que poderão ser validadas a partir dessa tela serão: Composições, Insumos e Cronograma Previsto.

Só será exibido à tela do comparador de composição, caso o recurso associado ao serviço seja uma composição, caso contrário será apresentada a mensagem abaixo. No exemplo, trata-se de uma tarefa de valor cotado em ambos os projetos:

Só será exibido à tela do comparador de insumo, caso o recurso associado ao serviço seja um insumo, No exemplo abaixo, a mesma tarefa de valor cotado, sem nenhum recurso, seja composição ou insumo:

Só será exibido comparador do cronograma caso a tarefa, etapa ou obra tenha cronograma previsto informado. No exemplo, abaixo, o cronograma previsto de ambos os projetos é idêntico:

**Composições**

Acessando a opção Composições do Comparador de Projetos (Projeto | Comparador de Projetos | Composições), será possível expandir a lista dos recursos que compõe a composição, clicando no sinal '+', à frente do código dessa composição, o que possibilitará uma análise mais detalhada das diferenças existentes entre as composições dos dois projetos:

Observação:

As composições são incluídas separadamente quando utilizadas como composição auxiliar e utilizadas diretamente nas tarefas. As composições com o Check Box desmarcado na coluna Possui  tarefas vinculadas são composição auxiliares.

**Insumos**  
Ao acessar a opção Insumos no comparador de projetos (Projeto | Comparador de Projetos | Insumos), estará habilitado para comparar o Preço do insumo selecionado:

E ao clicar, os preços vinculados ao insumo, serão exibidos para os dois projetos:

**Parâmetros**

O comparador permite também a visualização dos parâmetros dos projetos:

**Cenários**

Através da opção Cenários,  (Projeto | Comparador de Projetos | Cenários), poderá ser comparado qualquer cenário do projeto atual com qualquer outro cenário de projeto de qualquer coligada,  será exibido a opção de selecionar qual projeto, cenário e planilha que deseja comparar

Atenção

* Para todas as opções disponíveis de comparação entre projetos, ficarão habilitadas as opções de comparar Parâmetros e Exportar para Excel destacadas abaixo:

* Com o intuito de permitir que o TCOP trabalhe de forma autônoma da solução da Microsoft, o processo de exportação para MS EXCEL foi modificado nas telas do comparador, e além da não obrigatoriedade de utilização de licenças do MS EXCEL no ambiente, será gerado um arquivo com a extensão XLS contendo duas pastas que receberão o nome Origem(projeto aberto) e Destino (projeto selecionado para comparação):

* Em todas as telas, assim como demonstrado no Comparador de Composições abaixo, será possível usar a Exportação de Dados da Visão dos Serviços Globais, caso haja a necessidade, porém essa exportação gera um arquivo apenas do projeto em que foi selecionada:

**Melhorias para Mercado Internacional Calculo por Rendimento Diário.**  
Disponível somente para o mercado internacional, para licitações públicas que exigem o detalhamento dos serviços (composições) por rendimento.  
O Comparador de composições contempla os campos jornada, rendimento de mão de obra e equipamentos. Em: Projeto/ Comparador de Projetos/ Composições.

 Veja Também

---
