---
content_hash: 46010e87d3df2797e53cecad3607a5b8f72cb3f7b8741f82543fc55e1a0eab52
fetched_at: '2026-06-29T00:09:32.355410+00:00'
page_id: '425458832'
product: rm
source: tdn-rm
title: Eventos Contábeis - Educacional
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458832
version: 17
---

---

Eventos Contábeis são cadastros utilizados para mapear e determinar as regras da contabilização de processos da empresa, realizados dentro do sistema.

No TOTVS Educacional, as regras ou as definições de como a contabilização por competência do contrato educacional será realizada, devem ser definidas dentro dos eventos contábeis. Assim, ao executar o processo para realização da contabilização do contrato educacional utilizando os eventos contábeis, não será necessária a indicação das contas contábeis, dos rateios gerenciais, percentuais, etc., pois o sistema irá contabilizá-lo de acordo com as regras parametrizadas nos eventos utilizados para este fim.

O sistema prevê a utilização dos eventos contábeis em algumas situações e, para cada uma destas situações devem-se cadastrar os respectivos eventos contábeis, discriminando-os através da indicação correta do **'Processo'** para o qual será utilizado no momento de sua criação. Eles devem ser cadastrados no menu *Financeiro/Contábil | Geração | Eventos Contábeis* e indicados para utilização nos parâmetros do sistema menu *Ambiente | Parâmetros | Educacional | Integração | Contabilidade*.   
   
Na aba [identificação](http://tdn.totvs.com/pages/viewpage.action?pageId=423938457) preencha corretamente qual *'Processo'* poderá utilizar este evento contábil. Destacamos aqui a importância de definir corretamente o local de onde o sistema deverá buscar a *'Filial/Departamento'* para preenchimento nos lançamentos contábeis e, se a informação puder ser encontrada em mais de um local, informe corretamente a ordem ou a prioridade de busca.

Da mesma forma, defina corretamente o local para se encontrar o *'Centro de Custo'* para preenchimento nos lançamentos contábeis, assim como a sua ordem ou a prioridade de busca.

Ao gerar a contabilização do contrato pelo TOTVS Educacional, para preencher o Centro de Custo nos lançamentos contábeis, o sistema irá busca-lo do local aqui marcado. Se mais de um local estiver marcado, a busca seguirá na ordem definida.  
   
**Observação:**   
Vale ressaltar que ao marcar a opção buscar centro de custo em *'Contrato'* ou, dependendo do processo, buscar centro de custo em *'Parcela'*, está sendo informado ao sistema que ao gerar a contabilização do contrato, os lançamentos contábeis gerados serão preenchidos com o centro de custo informado no Contrato do aluno. Segundo regra interna do sistema, se o Centro de Custo não estiver informado dentro do Contrato do aluno, o sistema ainda verificará o parâmetro de sistema *Ambiente | Parâmetros | Educacional | Integração | 'Centro de Custo'* e o buscará da *Matriz Aplicada* ou da *Turma*, conforme opção selecionada.

Para informações mais detalhadas sobre cada campo a ser preenchido, por favor [clique aqui](http://tdn.totvs.com/pages/viewpage.action?pageId=423938693) e acesse as informações das respectivas pastas do cadastro do Evento Contábil.

Na aba [item de evento](http://tdn.totvs.com/pages/viewpage.action?pageId=423938464) deverão ser cadastrados os itens para as partidas de Débito e para as partidas de Crédito que comporão os lançamentos contábeis.

As opções disponíveis em *'Aplicar'* definem onde o sistema irá buscar as informações para compor a partida do lançamento. Estas opções irão variar conforme o *Processo* definido inicialmente na tela anterior. A opção aqui escolhida irá definir de onde o sistema irá obter a conta contábil para o lançamento, seja informando-a diretamente ou buscando-a dentro de uma tabela default. As demais opções disponibilizadas para seleção irão variar conforme as opções inicialmente selecionadas.

Vale lembrar que o lançamento somente será incluído se a soma dos valores calculados para os itens de débitos for igual à soma dos valores calculados para os itens de créditos.  
   
Caso o evento contábil tenha sido configurado para utilizar fórmula para o cálculo do valor contábil do lançamento, poderão ser utilizadas as seguintes funções de fórmula: BuscaCampoParcelaCont, BuscaCampoParcelaBolsaCont, BuscaCampoParcelaServicoCont, BuscaCampoContrato, BuscaCampoContratoCont, BuscaCampoContratoServicoCont e BuscaCampoContratoBolsaCont. Essas funções devem ser utilizadas de acordo com o contexto onde o lançamento contábil será aplicado, para saber mais [clique aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=776127842&moved=true)

Observa-se que as funções BuscaCampoContratoCont, BuscaCampoContratoServicoCont e BuscaCampoContratoBolsaCont são compatíveis apenas com o modelo de contabilização que [Registra separadamente contabilizações de cancelamento e aumento](https://tdn.totvs.com/x/M-9bGQ). Caso não esteja sendo utilizado este modelo, para provisões de contrato, deverá ser utilizada a fórmula BuscaCampoContrato.

Dentro da aba [dados complementares](http://tdn.totvs.com/pages/viewpage.action?pageId=423938664) as informações preenchidas poderão compor o lançamento. Lembrando-se que se a opção *'Buscar Filial/Depto em'* selecionada inicialmente for igual a 'Evento Contábil' e não utilizar prioridade, o campo 'Filial' dos Itens de evento/Dados complementares deverá ser obrigatoriamente preenchido.

Sempre que uma conta contábil indicada na aba *Item de evento* possuir rateio gerencial, as informações para a realização deste rateio devem ser incluídas na aba Itens gerenciais.

As opções disponibilizadas para seleção na aba [itens gerenciais](http://tdn.totvs.com/pages/viewpage.action?pageId=423938439) irão variar conforme as opções anteriormente selecionadas.  Para cada conta contábil (*item de evento*) podem-se incluir vários *itens gerenciais* (rateios), sendo que a soma dos valores rateados (100%) deve ser igual ao valor lançado na conta contábil correspondente. Assim, o valor contábil dos lançamentos gerados na contabilização de um processo será rateado, ou seja, dividido ou apropriado proporcionalmente para uma ou mais contas gerenciais, possibilitando então um acompanhamento gerencial detalhado através da contabilização.

Um exemplo prático, entre vários, da utilização de *rateio gerencial* é a possibilidade de se gerenciar os valores de Bolsas separadamente por Curso: Para que isto seja possível, o sistema deve estar parametrizado para buscar o Centro de Custo da Matriz Aplicada. Dentro de cada Matriz Aplicada (curso) deve-se indicar o seu respectivo Centro de Custo e dentro deste a sua respectiva *Conta Gerencial*. No cadastro do evento, na aba *Itens gerenciais*, indique que a origem da conta será *Tabela Default* e que a tabela default será o *Centro de Custo*. Assim, ao gerar a contabilização o sistema buscará a conta contábil indicada no item de evento, porém aplicará o rateio gerencial na conta gerencial informada no centro de custo da tabela Master (que neste caso foi encontrada na Matriz Aplicada que corresponde ao *Curso*).

As permissões para incluir, excluir e editar o evento contábil devem ser definidos no perfil associado ao usuário em [Serviços Globais] / [Segurança] / [Perfis] / [Sistema: Educacional]

 Veja Também

---

[Tag para complemento de histórico contábil](http://tdn.totvs.com/pages/viewpage.action?pageId=425458850)
