---
content_hash: 80934a69b4d3f39738e13b96db6c70461a4e51ae1871657827f280a921b7a672
fetched_at: '2026-06-29T00:10:08.509586+00:00'
page_id: '452719527'
product: rm
source: tdn-rm
title: Definição por Competências
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719527
version: 1
---

**Definição por Competências**

---

A Definição de Mapa de Conhecimento tem como objetivo definir o mapeamento dos conhecimentos esperados para os funcionários de uma empresa, sem necessariamente fazer uma gestão por competências.  
Será possível mapear para função, seção, lotação, função no posto de trabalho, tarefa, funcionário ou nível de carreira, competências exigidas e/ou desejadas para que os funcionários desempenhem determinada função.
  
**1 – Parametrizador**  
Acessar Configurações | Parametrizador, menu: 07.00.11 – Mapa de Conhecimento, para determinar as preferências para definição do mapa de conhecimento.  
**Por Competências**  
**"Data de Expiração Obrigatória em Dias"**: marcando este parâmetro será obrigatória a informação dos dias de expiração na vinculação de Requisitos de Acesso à Competências no cadastro de Competências.
  
**2 – Cadastro**  
Acessar Acompanhamento | Mapa de Conhecimento | Definição por Competências para criar uma nova definição.  
**Tipo de Vínculo**: será definido o tipo de vínculo do mapa de conhecimento dentre as seguintes opções:

* Função
* Seção
* Lotação
* Função no posto de trabalho
* Tarefa
* Funcionário
* Nível de Carreira

**Competências**: será definida a competência esperada para os funcionários.  
Tendo para tal definição as opções:   
·         **Código da Competência:** Escolher a competência a partir do seu cadastro.   
·         **Código da Graduação:** Escolher a graduação da competência para esta definição.  
      **Tipo:** Classifica se o requisito de acesso será Exigido ou Desejado neste mapeamento.  
**Data Inclusão:** Este campo traz como sugestão a data atual como data de inclusão da definição. Não sendo este de preenchimento obrigatório.   
**Observação:** Este campo dá ao usuário a liberdade de incluir alguma observação relevante em relação à definição cadastrada.  
**Ativo**: Indica que uma definição de mapeamento encontra-se ativa.   
\*\*\*Ao ser desativado, a competência deixa de ser considerada em todos os pontos do sistema que utilizam o Mapa de Conhecimento por Competências.  
Ao salvar uma definição por competências o sistema irá incluir neste mapeamento automaticamente, todos os itens de performance ativos da competência selecionada com os pesos definidos nesses itens. Sempre que for incluído um novo item de performance na competência, o sistema automaticamente irá incluí-lo em todos os mapeamentos relacionados a esta competência.
  
**3 – Processos**  
**Cópia de Definições de Mapa de Conhecimento por Competências**  
Será disponibilizado um processo que permitirá copiar definições existentes para diferentes tipos de vínculos. As cópias irão contemplar todos os detalhes do mapeamento de origem para o mapeamento de destino.  
Com o mapeamento aberto acessar: Processos | Cópia de Definições de Mapa de Conhecimento por Competências.   
**Origem da Cópia:**  
**Tipo de Vínculo:** Será possível escolher uma dentre as opções de vínculo já mapeadas: Função, Seção, Lotação, Função no Posto de Trabalho, Tarefa, Nome do Funcionário ou Nível de Carreira. A opção escolhida irá direcionar os filtros que poderão ser aplicados e o formato de exibição dos itens que serão copiados.  
**Legenda**: Competências classificadas como Exigidas, serão exibidas na cor "Azul", já as classificadas como Desejadas, serão exibidas na cor "Verde".  
**Ordenar por:** Será possível definir se o resultado do filtro será ordenado por: Código ou Nome.  
Após aplicar o filtro, será montada uma árvore de acordo com o tipo de vínculo escolhido.   
O sistema disponibilizará os botões:   
·          **Expandir todos:** Clicando neste botão, a árvore expandirá e será possível visualizar todos os requisitos de acesso vinculados.  
·         **Recolher todos:** Clicando neste botão, a árvore irá recolher as informações dos requisitos de acesso vinculados.  
**Destino da Cópia:**  
**Tipo de Vínculo:** Será possível escolher uma dentre as opções de vínculo já mapeadas: Função, Seção, Lotação, Função no Posto de Trabalho, Tarefa, Nome do Funcionário ou Nível de Carreira. A opção escolhida irá direcionar os filtros que poderão ser aplicados e o formato de exibição dos itens que serão copiados.  
Após aplicar o filtro e estar visualizando tanto os dados de origem quanto os de destino da cópia, o usuário poderá fazer a cópia dos itens desejados. Para isso ele irá clicar no item no grupo de origem e irá arrastar para o destino desejado. Se o usuário clicar no agrupador de origem e arrastar para o destino, todos os itens do agrupador selecionado serão copiados para o destino escolhido.  
Abaixo do grupo de destino, o sistema irá exibir um aviso com a quantidade de itens adicionados durante o processo.  
Após terminar de arrastar os itens que deseja copiar, o usuário irá clicar  "Avançar" o processo. Será exibido um resumo de todas as cópias que serão efetuadas ao concluir o processo. Após conferir se está de acordo com sua necessidade, o usuário irá "Finalizar" o processo, efetivando assim a cópia dos registros.  
Será exibido um log ao final do processo indicando os itens copiados e se houve algum problema que impediu a cópia de algum item.  
   
**Cópia de Definições entre Coligadas**  
Com o mapeamento aberto acessar: Processos | Cópia de Definições entre Coligadas.   
O processo de cópia de Definição de Mapa de Conhecimento entre Coligadas foi criado para facilitar a replicação de definições para empresas que utilizam várias coligadas.   
A partir da seleção das definições que se deseja copiar, o usuário irá escolher para quais coligadas serão copiadas as definições.  
O sistema irá validar se nas coligadas de destino escolhidas pelo usuário existem as entidades relacionadas às definições escolhidas. Para cada tipo de vínculo será feita a validação necessária.  
Caso a validação seja bem-sucedida, a cópia será realizada para as coligadas escolhidas.    
As informações sobre as validações e cópias realizadas serão exibidas após a execução do processo no Log de Execução.  
Exemplo de validação na cópia de Definição por Competências:   
·         Origem da cópia: definição da competência 00003, vinculada à função código 00001 e coligada 1.  
·         Destino da cópia: coligadas 2 e 3.   
·         O sistema irá validar se a competência 00003 e a função 00001 existem nas coligadas 2 e 3.
