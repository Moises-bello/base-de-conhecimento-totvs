---
content_hash: 6aa929510593d626ae5dcd46628fd607bbda9548515bbcd85103242a1ec9b7bb
fetched_at: '2026-06-29T00:05:56.903862+00:00'
page_id: '159514675'
product: rm
source: tdn-rm
title: Gráfico no RM Reports
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=159514675
version: 39
---

# Índice:

---

.\*ndice:

# Objetivo:

---

O objetivo desta página é exemplificar como inserir um gráfico em um [relatório.net](http://tdn.totvs.com/display/LRM/RM+Reports). Existem dezenas de parâmetros que podem ser configurados tais como as series, eixos, legendas etc. Os exemplos abaixo abrangem as principais e necessárias configurações para inclusão de um gráfico.

# Introdução

---

O gráfico é uma ferramenta eficiente para organizações gerenciais. Nos produtos da linha RM é possível criar e editar [gráficos](http://tdn.totvs.com/pages/viewpage.action?pageId=271846009) utilizando como fonte de dados [consultas SQL](http://tdn.totvs.com/pages/viewpage.action?pageId=237383336). Nestes exemplos utilizaremos informações de um relatório.net como fonte de dados.

# Utilização

---

Para inclusão de um gráfico no RM Reports, é necessário possuir informações no relatório organizadas de forma que existam argumentos e valores correspondentes para que as séries existentes possam ser configuradas, por exemplo:

false

***Principais configurações;***

ITipo de Gráfico

Quando arrastamos um controle de gráfico para o corpo do [relatório](http://tdn.totvs.com/display/LRM/RM+Reports), um wizard de configuração iniciará, onde inicialmente definimos o tipo do gráfico, quais as séries existentes, e o visual da apresentação do gráfico.

Series

Definido o tipo do gráfico e a sua aparência, as séries devem ser configuradas. Um gráfico pode possuir N séries. Para cadastrar as séries deve-se acessar o wizard de configuração e selecionar a opção “Séries” no menu à esquerda.

Dados

Na opção “Dados” na aba “Binding de Séries”, associamos os campos utilizados no Argumento e no Valor.

false

Depois de configurar as opções de “Construção” do gráfico, as demais opções são utilizadas apenas para ajustes visuais que não afetam a forma como as informações são manipuladas pelo componente.

---

***Exemplos;***

ExemplosGráfico de BarrasGráfico de BarrasSQL

Vamos criar um gráfico de barras a partir da [consulta SQL](http://tdn.totvs.com/pages/viewpage.action?pageId=237383336) que retorna o código da seção e os seguintes totais por seção: funcionários e dependentes ativos, funcionários e dependentes inativos.

sql 'A'
AND CODSECAO = SEC.CODIGO) 'FUNCIONARIOS NÃO ATIVOS',
(SELECT COUNT(NRODEPEND)
FROM PFDEPEND
JOIN PFUNC ON (PFDEPEND.CHAPA = PFUNC.CHAPA
AND PFUNC.CODSITUACAO <> 'A')
WHERE PFUNC.CODSECAO = SEC.CODIGO) 'DEPENDENTES NÃO ATIVOS'
FROM PSECAO SEC
WHERE SEC.CODIGO IN ('01.02',
'01.03',
'03.01',
'01.14',
'01.10',
'02.02',
'01.01',
'01.04',
'01.08',
'01.09')]]>Relatório

Criamos um novo relatório e adicionamos a [consulta SQL](http://tdn.totvs.com/pages/viewpage.action?pageId=237383336) criada como fonte de dados. Associamos a consulta a banda Detalhe e os campos que desejamos visualizar.

Neste exemplo utilizaremos um único gráfico que exibirá todas as informações provenientes da banda Detalhe1. Para isso deve-se adicionar um rodapé de detalhe a banda que contém os dados. Clique com o botão direito do mouse sobre a banda detalhe a qual os dados foram associados, selecione a opção “Inserir Seção”, “Rodapé do Detalhe”.

Arraste para esta banda um componente do tipo gráfico

Gráfico

Depois de arrastar o componente para o rodapé do detalhe o wizard de configuração do gráfico iniciará. Selecionamos o tipo “Barra” e adicionamos uma série para cada uma das colunas de dados retornadas na [consulta SQL](http://tdn.totvs.com/pages/viewpage.action?pageId=237383336).

No Binding das Séries, todos os itens do argumento será “Qualitativo” e o campo CODIGO será associado ao argumento, no valor de cada série o tipo retornado pela consulta SQL é numérico, a ligação é feita por valores e o valor é associado ao campo correspondente na [consulta SQL](http://tdn.totvs.com/pages/viewpage.action?pageId=237383336).

Depois de configurada as séries e dados, o gráfico gerado do rodapé do [relatório](http://tdn.totvs.com/display/LRM/RM+Reports) será o seguinte:

Gráfico de TortaGráfico de TortaSQL

No exemplo a seguir criaremos um gráfico de torta a partir da [consulta SQL](http://tdn.totvs.com/pages/viewpage.action?pageId=237383336) que retorna a quantidade de relatórios existentes por cada aplicação do ERP.

sqlRelatório

Depois de criar a consulta SQL, criamos um novo relatório, adicionamos a [consulta SQL](http://tdn.totvs.com/pages/viewpage.action?pageId=237383336) criada como fonte de dados e adicionamos a banda Detalhe os campos que desejamos visualizar.

Neste exemplo, também utilizaremos um único gráfico que exibirá todas as informações provenientes da banda Detalhe1. Para isso deve-se adicionar um rodapé de detalhe a banda que contém os dados. Clique com o botão direito do mouse sobre a banda detalhe a qual os dados foram associados, selecione a opção “Inserir Seção”, “Rodapé do Detalhe”.

Arraste para esta banda um componente do tipo gráfico. Aba “Caixa de Ferramentas”, “Controles Avançados”, “Gráfico”.

Gráfico

Depois de arrastar o componente para o rodapé do detalhe o wizard de configuração do gráfico iniciará. Selecione o tipo “Torta”.

Adicione uma série para cada uma das colunas de dados retornadas na nossa [consulta SQL](http://tdn.totvs.com/pages/viewpage.action?pageId=237383336), neste caso, apenas uma série e pode-se utilizar a série criada automaticamente pelo wizard.

No Binding das Séries, o campo CODAPLICACAO deve ser o argumento, do tipo “Qualitativo”, já que distingue as informações e o campo TOTAL será associado ao valor da série.

Depois, a configuração da série e dos dados, o gráfico gerado do rodapé do relatório foi o seguinte:

Gráfico de LinhaGráfico de LinhaSQL

Vamos criar um gráfico de torta a partir da [consulta SQL](http://tdn.totvs.com/pages/viewpage.action?pageId=237383336) que retorna a quantidade de relatórios existentes por cada aplicação do ERP.

sqlRelatório

Após a criação da [consulta SQL](http://tdn.totvs.com/pages/viewpage.action?pageId=237383336), criamos um novo relatório, adicionamos a [consulta SQL](http://tdn.totvs.com/pages/viewpage.action?pageId=237383336) criada como fonte de dados e adicionamos a banda Detalhe os campos que desejamos visualizar.

Neste exemplo também utilizaremos um único gráfico que exibirá todas as informações provenientes da banda Detalhe1. Para isso deve-se adicionar um rodapé de detalhe a banda que contém os dados. Clique com o botão direito do mouse sobre a banda detalhe a qual os dados foram associados, selecione a opção “Inserir Seção”, “Rodapé do Detalhe”.

Arraste para esta banda um componente do tipo gráfico. Aba “Caixa de Ferramentas”, “Controles Avançados”, “Gráfico”.

Após arrastar o componente para o rodapé do detalhe será aberto o wizard de configuração do gráfico. Selecionamos o tipo “Linhas”.

Gráfico

Adicionamos uma série para cada uma das colunas de dados retornadas na nossa [consulta SQL](http://tdn.totvs.com/pages/viewpage.action?pageId=237383336).

No Binding das Séries, para todos os itens o argumento será “DateTime” e o campo DATAEMISSAO será associado ao mesmo, para cada uma das séries criadas associamos uma coluna em seu valor que é do tipo Numérico.

Após a configuração da série e dos dados, o gráfico gerado do rodapé do relatório foi o seguinte:

falsefalse

**Produto:** Framework

false

**Versão:** 11.XX

false

**Processo:** Criação de gráficos no Reports 

falsefalse

**Status:** Em alteração

false

**Data:**

false

**Autores:**
