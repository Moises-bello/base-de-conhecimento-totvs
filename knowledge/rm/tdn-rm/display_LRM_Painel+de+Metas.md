---
content_hash: f88fdd47c6489efa04f84b6313407abcc85897c11b4dd478b9df59c692c33624
fetched_at: '2026-06-29T00:10:19.580297+00:00'
page_id: '4816380'
product: rm
source: tdn-rm
title: Painel de Metas
type: documentation
url: https://tdn.totvs.com/display/LRM/Painel+de+Metas
version: 9
---

BLOCK

Painel de Metas

FAQ: **Painel de Metas**

**Introdução**

**1.** **Painel de Metas**

O **Painel de metas** é um recurso, com base em Gráficos Medidores, onde se pode definir metas a serem alcançadas. É importante citar que o gráfico medidor é gerado com base em uma consulta SQL que retorna apenas um valor. A definição das metas é feita através de fórmulas. Essas fórmulas podem ser desde uma expressão simples até uma expressão complexa.

Para criarmos um painel de metas, devemos primeiramente ter nosso objetivo bem definido.

O exemplo que daremos será a criação de um painel de metas para avaliarmos quanto a empresa despende com vale alimentação e vale transporte para todos os seus funcionários.

Para esse painel de metas, necessitamos de dois gráficos de Gauge. O primeiro para verificarmos a valor gasto com vale transporte e o segundo, o valor gasto com vale alimentação.

**2. Liberando acesso ao menu Painel de Metas na nova MDI:**

Na nova MDI, selecione a opção Inteligência de Negócios, o menu Painel de Metas estará desabilitado:

[![clip_image002](http://lh5.ggpht.com/_G7KXZLoZDsY/TLw_gusqzcI/AAAAAAAAB6c/yV02-Bn0fug/clip_image002_thumb%5B1%5D.jpg?imgmax=800 "clip_image002")](http://lh3.ggpht.com/_G7KXZLoZDsY/TLw_gVkdqwI/AAAAAAAAB6Y/iClRTFlsrNk/s1600-h/clip_image002%5B52%5D.jpg)

Para permitir acesso a esse menu, é necessário conceder permissão ao perfil associado ao usuário. Selecione a opção Serviços Globais, aba Segurança à Perfis à Globais àInteligência de Negócios:

[![clip_image004](http://lh6.ggpht.com/_G7KXZLoZDsY/TLw_iKZZg1I/AAAAAAAAB6k/UCo-wAlPZ8M/clip_image004_thumb%5B1%5D.jpg?imgmax=800 "clip_image004")](http://lh5.ggpht.com/_G7KXZLoZDsY/TLw_hMW8rVI/AAAAAAAAB6g/w8ImH50feS8/s1600-h/clip_image004%5B12%5D.jpg)

No Sistema Inteligência de Negócios, selecione o perfil desejado.

Libere acesso ao menu Painel de Metas:

[![](http://lh3.ggpht.com/_G7KXZLoZDsY/TLw_jP5SHwI/AAAAAAAAB6s/selhR_JgsOs/clip_image002%5B4%5D_thumb%5B1%5D.jpg?imgmax=800 "clip_image002[4]")](http://lh4.ggpht.com/_G7KXZLoZDsY/TLw_isyF7sI/AAAAAAAAB6o/EOZkg2b1W7o/s1600-h/clip_image002%5B4%5D%5B3%5D.jpg)

**3. Criando gráficos de Gauge:**

Para criação de um novo Gráfico, é necessário acessar o Menu Gestão -> Gráfico.

[![](http://lh4.ggpht.com/_G7KXZLoZDsY/TLw_kSJW3bI/AAAAAAAAB60/KxzDPttF7Es/clip_image002%5B6%5D_thumb%5B1%5D.jpg?imgmax=800 "clip_image002[6]")](http://lh4.ggpht.com/_G7KXZLoZDsY/TLw_j6-8EAI/AAAAAAAAB6w/oAE42frYOtU/s1600-h/clip_image002%5B6%5D%5B3%5D.jpg)

Selecione a opção para inclusão de um novo gráfico:

[![](http://lh5.ggpht.com/_G7KXZLoZDsY/TLw_k9LBzQI/AAAAAAAAB68/kmxFIUDk1ks/clip_image002%5B8%5D_thumb%5B1%5D.jpg?imgmax=800 "clip_image002[8]")](http://lh6.ggpht.com/_G7KXZLoZDsY/TLw_kpebjvI/AAAAAAAAB64/eI3Dnu_aEm8/s1600-h/clip_image002%5B8%5D%5B3%5D.jpg)

Preencha todas as informações abaixo:

[![](http://lh5.ggpht.com/_G7KXZLoZDsY/TLw_l_ABy8I/AAAAAAAAB7E/eLPuGQLDEHg/clip_image002%5B10%5D_thumb%5B1%5D.jpg?imgmax=800 "clip_image002[10]")](http://lh5.ggpht.com/_G7KXZLoZDsY/TLw_le6PIgI/AAAAAAAAB7A/r2ltLNX08k8/s1600-h/clip_image002%5B10%5D%5B3%5D.jpg)

Observação: No preenchimento do campo categoria, deverá ser selecionada a categoria criada anteriormente com os perfis associados.

No gráfico de Gauge, as consultas SQL ficarão armazenadas no próprio sistema, em Gestão -> SQL, e devem conter apenas uma linha com resultado.

Na inclusão da consulta SQL, será exibida a tela abaixo, que permite a pesquisa de consultas já existentes, sendo possível também, a criação de uma nova consulta. Neste caso, selecione a opção “incluir”:

[![](http://lh5.ggpht.com/_G7KXZLoZDsY/TLw_ms3e5YI/AAAAAAAAB7M/JK0Dpi99pOs/clip_image002%5B12%5D_thumb%5B1%5D.jpg?imgmax=800 "clip_image002[12]")](http://lh6.ggpht.com/_G7KXZLoZDsY/TLw_mcvgjZI/AAAAAAAAB7I/53bIhnbKBUw/s1600-h/clip_image002%5B12%5D%5B3%5D.jpg)

Para exemplificarmos, criamos uma consulta para apresentar o total gasto com vale transporte:

[![](http://lh4.ggpht.com/_G7KXZLoZDsY/TLw_nr-ViII/AAAAAAAAB7U/jjRUDFoiS5M/clip_image002%5B14%5D_thumb%5B1%5D.jpg?imgmax=800 "clip_image002[14]")](http://lh4.ggpht.com/_G7KXZLoZDsY/TLw_nDC34RI/AAAAAAAAB7Q/l0moQCrrJMg/s1600-h/clip_image002%5B14%5D%5B3%5D.jpg)

Após a inclusão da sentença, clique em Salvar e retorne para a visão do Gráfico.

Após salvar o Gráfico, o sistema irá perguntar se deseja configurá-lo.

A configuração também pode ser acessada através do Menu Processos -> Assistente de Configuração de Gráfico.

[![image](http://lh6.ggpht.com/_G7KXZLoZDsY/TLw_ouOvp3I/AAAAAAAAB7c/iv8GNcwSLDI/image_thumb%5B1%5D.png?imgmax=800 "image")](http://lh5.ggpht.com/_G7KXZLoZDsY/TLw_oT6POOI/AAAAAAAAB7Y/-IEXHFbTdbs/s1600-h/image%5B3%5D.png)

Na tela de Assistente de Configuração de Gráficos, selecione a opção Medidor, em Tipos disponíveis para criação de um gráfico de Gauge.

[![](http://lh3.ggpht.com/_G7KXZLoZDsY/TLw_pUtN_yI/AAAAAAAAB7k/paWlO-5yH04/clip_image002%5B16%5D_thumb%5B1%5D.jpg?imgmax=800 "clip_image002[16]")](http://lh6.ggpht.com/_G7KXZLoZDsY/TLw_pNoteAI/AAAAAAAAB7g/StmnTcTMPcA/s1600-h/clip_image002%5B16%5D%5B3%5D.jpg)

Para visualizar o tipo do gráfico escolhido, deve-se marcar a opção pré-visualizar:

[![](http://lh3.ggpht.com/_G7KXZLoZDsY/TLw_qVkJ0DI/AAAAAAAAB7s/0iolY9noi6I/clip_image002%5B18%5D_thumb%5B1%5D.jpg?imgmax=800 "clip_image002[18]")](http://lh6.ggpht.com/_G7KXZLoZDsY/TLw_p6jWGvI/AAAAAAAAB7o/z7nGZwMUvKc/s1600-h/clip_image002%5B18%5D%5B3%5D.jpg)

Na próxima tela, defina as propriedades relativas ao medidor:

[![](http://lh6.ggpht.com/_G7KXZLoZDsY/TLw_rNqp4oI/AAAAAAAAB70/5ojbac6ZCtM/clip_image002%5B20%5D_thumb%5B1%5D.jpg?imgmax=800 "clip_image002[20]")](http://lh3.ggpht.com/_G7KXZLoZDsY/TLw_qhtYiwI/AAAAAAAAB7w/z4qm9fLQAWs/s1600-h/clip_image002%5B20%5D%5B3%5D.jpg)

Selecione a coluna que foi nomeada na consulta SQL para informar o valor de resultado.

O valor de escala define o valor inicial e final do seu gráfico.

A frequência demonstra os valores intermediários em seu gráfico.

Os marcadores ajudam na verificação dos valores (similar a uma régua).

Na opção de faixas de valor, podemos definir quais as faixas de valores o gráfico irá apresentar. Essas faixas

devem estar de acordo com o valor informado na escala.

[![](http://lh6.ggpht.com/_G7KXZLoZDsY/TLw_r-ZqQgI/AAAAAAAAB78/XrMpK4snCZU/clip_image002%5B22%5D_thumb%5B1%5D.jpg?imgmax=800 "clip_image002[22]")](http://lh5.ggpht.com/_G7KXZLoZDsY/TLw_rShLU4I/AAAAAAAAB74/q6euXn5WlZk/s1600-h/clip_image002%5B22%5D%5B3%5D.jpg)

Após as configurações de faixas, devemos configurar as ações que serão tomadas.

[![](http://lh5.ggpht.com/_G7KXZLoZDsY/TLw_snbO7iI/AAAAAAAAB8E/6ek_jM4BlTY/clip_image002%5B24%5D_thumb%5B1%5D.jpg?imgmax=800 "clip_image002[24]")](http://lh3.ggpht.com/_G7KXZLoZDsY/TLw_sFpa7LI/AAAAAAAAB8A/j76pvssjg7Y/s1600-h/clip_image002%5B24%5D%5B3%5D.jpg)

A configuração da ação irá variar de acordo com o conceito que o gráfico foi criado. Podemos optar apenas por enviar uma mensagem de aviso ou executar um processo específico.

Após essa configuração, o gráfico poderá ser executado e visualizado.

[![](http://lh5.ggpht.com/_G7KXZLoZDsY/TLw_tV__CCI/AAAAAAAAB8M/qhteOjS9TOc/clip_image002%5B26%5D_thumb%5B1%5D.jpg?imgmax=800 "clip_image002[26]")](http://lh5.ggpht.com/_G7KXZLoZDsY/TLw_tJEMvbI/AAAAAAAAB8I/17wKikY2d2s/s1600-h/clip_image002%5B26%5D%5B3%5D.jpg)

Duplo clique sobre o gráfico para visualizá-lo:

[![](http://lh5.ggpht.com/_G7KXZLoZDsY/TLw_ue7vLgI/AAAAAAAAB8U/2yCqRoSGm-8/clip_image002%5B28%5D_thumb%5B1%5D.jpg?imgmax=800 "clip_image002[28]")](http://lh6.ggpht.com/_G7KXZLoZDsY/TLw_tysKjgI/AAAAAAAAB8Q/uH4vH2ii0Ww/s1600-h/clip_image002%5B28%5D%5B3%5D.jpg)

Após a criação do primeiro gráfico, siga os mesmos passos para a criação de um novo gráfico. Nesse caso, foi criado um novo gráfico, para avaliarmos o valor gasto com Vale Alimentação. O resultado pode ser observado logo abaixo:

[![](http://lh3.ggpht.com/_G7KXZLoZDsY/TLw_vIFmPvI/AAAAAAAAB8c/X58SegQfOGs/clip_image004%5B4%5D_thumb%5B1%5D.jpg?imgmax=800 "clip_image004[4]")](http://lh3.ggpht.com/_G7KXZLoZDsY/TLw_ut-UtAI/AAAAAAAAB8Y/JIC0Xod7ZYo/s1600-h/clip_image004%5B4%5D%5B3%5D.jpg)

**4. Criando um Painel de Metas:**

Para criarmos um Painel de Metas, devemos criar um Gráfico de Gauge com a Fonte de Dados **Painel de Metas.**

[![](http://lh6.ggpht.com/_G7KXZLoZDsY/TLw_v8b-eZI/AAAAAAAAB8k/km3nfewx3xM/clip_image002%5B30%5D_thumb%5B1%5D.jpg?imgmax=800 "clip_image002[30]")](http://lh3.ggpht.com/_G7KXZLoZDsY/TLw_vQLd2bI/AAAAAAAAB8g/MSxeIUMszjE/s1600-h/clip_image002%5B30%5D%5B3%5D.jpg)

Selecione a opção Painel de Metas, em Inteligência de Negócios.

Insira um novo painel.

Preencha os campos abaixo:

[![](http://lh4.ggpht.com/_G7KXZLoZDsY/TLw_wrAFHcI/AAAAAAAAB8s/WE0csfaA8h8/clip_image002%5B32%5D_thumb%5B1%5D.jpg?imgmax=800 "clip_image002[32]")](http://lh5.ggpht.com/_G7KXZLoZDsY/TLw_wHJIvcI/AAAAAAAAB8o/clXxGaAmgps/s1600-h/clip_image002%5B32%5D%5B3%5D.jpg)

Como estamos nos baseando em dois valores (Vale Transporte e Vale Refeição) para obtermos o total pago de benefícios, precisamos utilizar os dois gráficos de Gauge e o gráfico (Fonte de Dados Painel de Metas) para elaborar o Painel de Metas.

Dessa forma, precisamos selecionar os três gráficos criados anteriormente para a criação do Painel de Metas.

Para formular as metas é necessário incluir os registros na Grid. A grid possui a funcionalidade de hierarquizar os registros. Isso permite que um registro seja filho direto de outro registro.

Insira 3 linhas, uma para cada gráfico:

[![](http://lh5.ggpht.com/_G7KXZLoZDsY/TLw_xV07LBI/AAAAAAAAB80/YGQx4kNdTao/clip_image004%5B6%5D_thumb%5B1%5D.jpg?imgmax=800 "clip_image004[6]")](http://lh5.ggpht.com/_G7KXZLoZDsY/TLw_xC0QtLI/AAAAAAAAB8w/CwZwJ3U-IKM/s1600-h/clip_image004%5B6%5D%5B3%5D.jpg)

Selecione os gráficos na coluna Medidor:

[![](http://lh4.ggpht.com/_G7KXZLoZDsY/TLw_yC07UwI/AAAAAAAAB88/t4caU1frIjA/clip_image002%5B34%5D_thumb%5B1%5D.jpg?imgmax=800 "clip_image002[34]")](http://lh4.ggpht.com/_G7KXZLoZDsY/TLw_x3GYt5I/AAAAAAAAB84/77ALLE5k1NE/s1600-h/clip_image002%5B34%5D%5B3%5D.jpg)

**[![](http://lh5.ggpht.com/_G7KXZLoZDsY/TLw_zef_dKI/AAAAAAAAB9E/ZSSG7bM1tOY/clip_image002%5B36%5D_thumb%5B1%5D.jpg?imgmax=800 "clip_image002[36]")](http://lh6.ggpht.com/_G7KXZLoZDsY/TLw_ykC_k-I/AAAAAAAAB9A/UE3ZqA2Ne7Q/s1600-h/clip_image002%5B36%5D%5B3%5D.jpg)**

Organize os gráficos em uma hierarquia (formato de árvore), de modo que o gráfico principal (Fonte de Dados Painel de Metas) seja o pai dos gráficos cuja fonte é Consulta SQL. Para organizar as linhas, clique no seletor de linha do registro que deseja que ele se torne filho e arraste para o registro que será pai do outro. Dessa forma o registro pai irá se tornar do tipo composta, habilitando assim a coluna expressão. Essa coluna Expressão para uma meta que seja Composta é de preenchimento obrigatório.

[![](http://lh6.ggpht.com/_G7KXZLoZDsY/TLw_0I-JmHI/AAAAAAAAB9M/3lhJNCKpk8o/clip_image002%5B38%5D_thumb%5B1%5D.jpg?imgmax=800 "clip_image002[38]")](http://lh4.ggpht.com/_G7KXZLoZDsY/TLw_zjB1g5I/AAAAAAAAB9I/yn8YFSbuUMo/s1600-h/clip_image002%5B38%5D%5B3%5D.jpg)

Selecione a expressão que será utilizada no Painel de Metas. No exemplo proposto, total de vale transporte e total de vale refeição, logo, a soma dos dois gráficos. Na coluna expressão existe um ícone com reticências, clicando nele será exibido o editor de expressão. Nele pode-se incluir inúmeros cálculos matemáticos para definir uma meta.

[![](http://lh5.ggpht.com/_G7KXZLoZDsY/TLw_03-NgtI/AAAAAAAAB9U/GZsoQLhbS5g/clip_image002%5B40%5D_thumb%5B1%5D.jpg?imgmax=800 "clip_image002[40]")](http://lh3.ggpht.com/_G7KXZLoZDsY/TLw_0XLh58I/AAAAAAAAB9Q/qripvXb-hPg/s1600-h/clip_image002%5B40%5D%5B3%5D.jpg)

[![](http://lh3.ggpht.com/_G7KXZLoZDsY/TLw_1t1sCoI/AAAAAAAAB9c/8e6wqB-segk/clip_image002%5B42%5D_thumb%5B1%5D.jpg?imgmax=800 "clip_image002[42]")](http://lh3.ggpht.com/_G7KXZLoZDsY/TLw_1D2mmrI/AAAAAAAAB9Y/befKylFVYEw/s1600-h/clip_image002%5B42%5D%5B3%5D.jpg)

[![](http://lh4.ggpht.com/_G7KXZLoZDsY/TLw_2Wn6cEI/AAAAAAAAB9k/iac0NLBhSLw/clip_image002%5B44%5D_thumb%5B1%5D.jpg?imgmax=800 "clip_image002[44]")](http://lh5.ggpht.com/_G7KXZLoZDsY/TLw_13aJqhI/AAAAAAAAB9g/CRiuO3ytbg0/s1600-h/clip_image002%5B44%5D%5B3%5D.jpg)

Selecioneum perfil para associar ao Painel de Metas, definindo quais perfis podem aprovar as metas do painel.

[![](http://lh3.ggpht.com/_G7KXZLoZDsY/TLw_3TEdEsI/AAAAAAAAB9s/9GycuceEC3I/clip_image002%5B46%5D_thumb%5B1%5D.jpg?imgmax=800 "clip_image002[46]")](http://lh3.ggpht.com/_G7KXZLoZDsY/TLw_2x0zr0I/AAAAAAAAB9o/jqHwnsIjTtw/s1600-h/clip_image002%5B46%5D%5B3%5D.jpg)

Clique em salvar e selecione a opção Processos -> Calcular Painel de Metas:

[![](http://lh6.ggpht.com/_G7KXZLoZDsY/TLw_4f4UOwI/AAAAAAAAB90/mutedrOrNyU/clip_image002%5B48%5D_thumb%5B1%5D.jpg?imgmax=800 "clip_image002[48]")](http://lh6.ggpht.com/_G7KXZLoZDsY/TLw_3wZqdMI/AAAAAAAAB9w/pFc9d7S1oms/s1600-h/clip_image002%5B48%5D%5B3%5D.jpg)

**[![](http://lh5.ggpht.com/_G7KXZLoZDsY/TLw_5Q1zzyI/AAAAAAAAB98/QWIuO2pr_Kw/clip_image004%5B8%5D_thumb%5B1%5D.jpg?imgmax=800 "clip_image004[8]")](http://lh6.ggpht.com/_G7KXZLoZDsY/TLw_4i7nNBI/AAAAAAAAB94/CZgfxcNLSdY/s1600-h/clip_image004%5B8%5D%5B3%5D.jpg)**

**[![clip_image006](http://lh5.ggpht.com/_G7KXZLoZDsY/TLw_6NPUbPI/AAAAAAAAB-E/zbkroKkQKxw/clip_image006_thumb%5B1%5D.jpg?imgmax=800 "clip_image006")](http://lh4.ggpht.com/_G7KXZLoZDsY/TLw_5nW9o-I/AAAAAAAAB-A/16Q0_3fNKnA/s1600-h/clip_image006%5B4%5D.jpg)**

A visualização do painel de metas será feita através do duplo clique no registro desejado na visão de

Painéis de metas.

[![](http://lh3.ggpht.com/_G7KXZLoZDsY/TLw_7KqWtPI/AAAAAAAAB-M/FCKzrGrfTto/clip_image002%5B50%5D_thumb%5B1%5D.jpg?imgmax=800 "clip_image002[50]")](http://lh6.ggpht.com/_G7KXZLoZDsY/TLw_6jJfCcI/AAAAAAAAB-I/H1OCjHu1s3I/s1600-h/clip_image002%5B50%5D%5B3%5D.jpg)

[![](http://lh4.ggpht.com/_G7KXZLoZDsY/TLw_73Io84I/AAAAAAAAB-U/T8T7__TnMC0/clip_image004%5B10%5D_thumb%5B1%5D.jpg?imgmax=800 "clip_image004[10]")](http://lh6.ggpht.com/_G7KXZLoZDsY/TLw_7WB0YvI/AAAAAAAAB-Q/miEWoKo2IcY/s1600-h/clip_image004%5B10%5D%5B3%5D.jpg)

A visualização é feita de forma hierárquica nos moldes da edição do painel. São exibidas as metas, seus status e valores, e um gráfico (medidor) indicando a posição da meta em relação à sua escala de forma visual. A cor de fundo do valor da meta será a cor da escala onde a meta se encontra. No nosso contexto, o Painel de Metas demonstra que, mesmo tendo o total de vale transporte Alto, o valor total da meta não foi ultrapassado, pois a soma dos dois benefícios ainda se encontra no limite aceitável (Média).

Nessa tela os valores das metas poderão ser alterados manualmente, de forma a simular um cenário. Assim que o valor for alterado será solicitado o recálculo do painel de metas, de forma que as metas compostas sejam recalculadas utilizando o valor digitado. Para isso dê um duplo clique na meta listada, será exibida uma tela para inserção de valores. Por default, vem preenchido com o valor atual. Após fazer a alteração, clique em ok para confirmar e acesse o item de Processo e o item Calcular Painel de Metas.

Obs.: Após alteração manual do valor da meta, é possível visualizar o valor do painel alterado, mas ao calcular a meta novamente, o Painel seleciona os valores anteriores dos gráficos como default.
