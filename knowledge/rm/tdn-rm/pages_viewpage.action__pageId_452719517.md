---
content_hash: 03c5104e4ff227b1e1bd0baee358bbb541e16d5e025f9bfe3d8955f00389741c
fetched_at: '2026-06-29T00:10:08.453726+00:00'
page_id: '452719517'
product: rm
source: tdn-rm
title: Como Parametrizar o Controle de Lotação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719517
version: 2
---

**Como Parametrizar o Controle de Lotação**

Para utilizar este controle é necessário seguir os seguintes passos:  
   
**1º. Passo – Controle de Vagas:**

1.1 – Para efetuar a parametrização do controle deverá acessar o menu Opções | Parâmetros | RM Vitae | Parametrizador, onde, inicialmente, será apresentada a tela inicial.

1.2 – Ao clicar em "Avançar" apresentará as opções gerais do parametrizador, devendo selecionar a opção na treeview "07.00.03 – Controle de Lotação" e clicar em <Avançar>;

1.3 – Ao selecionar a opção "Vagas" à esquerda, permitirá definir como serão controladas as vagas da coligada em questão, especificando o Tipo de Controle e como serão controlados os limites de vagas nas contratações. As opções disponíveis para parametrização do Tipo de Controle são:

* **Sem Controle:** Com esta opção não será feito nenhum controle de vagas na coligada;
* **Seção Folha:** Serão controladas as vagas somente pelas seções folha, ou seja, somente pelas seções onde os funcionários estão diretamente lotados, não permitindo disponibilizar para as seções "pais";
* **Seção em Qualquer Nível:** Serão controladas as vagas por qualquer registro de seção e não somente das seções folha;
* **Função:** Ao selecionar a opção de tipo de controle por função serão controladas as vagas de acordo com as funções cadastradas na coligada;
* **Quadro de Lotação:** O quadro de lotação é um controle feito por meio da função x seção, devendo ser acessado pelo anexo "Quadro de Lotação" no cadastro de funções;

1.4 – O Limite de Vaga na Contratação permite que flexibilize ou não os quantitativos informados de acordo com os controles citados anteriormente, possuindo as seguintes opções:

* **Nunca Excede:** Caso tenha atingido o número de vagas limite em um controle, ao tentar admitir algum funcionário na seção/função/quadro de lotação onde se atingiu o limite, o sistema não permitirá admitir o funcionário, a não ser que existam requisições aprovadas para vincular à admissão do funcionário;
* **Excede Indefinidamente:** Ao utilizar essa parametrização, o controle de vagas será feito, mas, caso tenha atingido o limite de vagas conforme sua parametrização, ao tentar admitir um funcionário, o usuário será informado que atingiu o limite de vagas, mas, permitindo efetuar a admissão.
* **Excede No. Afastados:** Quando usada esta opção, ao atingir o limite de vagas e tentar admitir um novo funcionário será verificado se possuem afastamentos conforme definidos em "Configurações", podendo determinar quais situações serão considerados para disponibilização de vagas. Para alterar essas definições, basta clicar em "Configurações" à esquerda no assistente.

1.5 – Após finalizadas as parametrizações é necessário efetuar a montagem automática pelo menu Gerência de RH | Controle de Lotação | Montagem Automática para ajustar o controle de lotação conforme cenário atual da empresa.  
   
**2º. Passo – Controle de Verbas:**  
   
2.1 – Para efetuar a parametrização do controle deverá acessar o menu Opções | Parâmetros | RM Vitae | Parametrizador, onde, inicialmente, será apresentada a tela inicial.

2.2 – Ao clicar em "Avançar" apresentará as opções gerais do parametrizador, devendo selecionar a opção na treeview "07.00.03

– Controle de Lotação" e clicar em <Avançar>;

2.3 – Ao selecionar a opção "Verbas" à esquerda, permitirá definir como serão controladas as verbas da coligada em questão, especificando o Tipo de Controle e como serão controlados os limites de verbas nas contratações. As opções disponíveis para parametrização do Tipo de Controle são:

* **Sem Controle:** Com esta opção não será feito nenhum controle de verba na coligada;
* **Seção Folha:** Serão controladas as verbas somente pelas seções folha, ou seja, somente pelas seções onde os funcionários estão diretamente lotados, não permitindo disponibilizar para as seções "pais";
* **Seção em Qualquer Nível:** Serão controladas as verbas por qualquer registro de seção e não somente das seções folha;
* **Função:** Ao selecionar a opção de tipo de controle por função serão controladas as verbas de acordo com as funções cadastradas na coligada;
* **Quadro de Lotação:** O quadro de lotação é um controle feito pela função x seção, devendo ser acessado pelo anexo "Quadro de Lotação" no cadastro de funções;

2.4 - A parametrização do tipo de verba permite que faça por dois tipos conforme segue detalhado abaixo:

* **Por Valor:** Ao especificar com tipo de verba por valor, permitirá que os valores sejam inseridos de acordo com o tipo de controle, ou seja, se seu controle for determinado por "Seção folha", no cadastro das seções, será permitido inserir os valores limites para cada seção folha conforme desejado.
* **Por Percentual:** Ao utilizar o tipo de verba por percentual será habilitado o campo "Verba Geral", onde deverá ser informado o valor que será considerado limite de verba geral para contratação e, permitirá que sejam inseridos os percentuais nos cadastros conforme parametrizado no tipo de controle, ou seja, se o tipo de controle for determinado como "Seção Folha", será disponibilizado o campo para inserção de percentual baseado na verba geral para cada seção folha.

Caso selecione o limite de verba com a opção "Excede No. Afastados" o sistema permite que determine quais tipos de afastamentos serão considerados para disponibilizar verba, para isso, basta clicar em "Configurações" nas opções da esquerda e definir conforme desejado;  
   
**Observação:** O valor considerado para o controle de verba será somente o campo salário do cadastro de funcionários, não sendo considerado nenhum valor adicional, tais como encargos, FGTS, INSS, etc.  
   
2.5 – O Limite de Verba na Contratação permite que flexibilize ou não os quantitativos informados de acordo com os controles citados anteriormente, possuindo as seguintes opções:

* **Nunca Excede:** Caso tenha atingido o valor de verba limite em um controle, ao tentar admitir algum funcionário na seção/função/quadro de lotação onde se atingiu o limite, o sistema não permitirá admitir o funcionário, a não ser que existam requisições aprovadas para vincular à admissão do funcionário;
* **Excede Indefinidamente:** Ao utilizar essa parametrização, o controle de verbas será feito, mas, caso tenha atingido o limite conforme sua parametrização, ao tentar admitir um funcionário, o usuário será informado que atingiu o limite de verbas, mas, permitirá efetuar a admissão.
* **Excede No. Afastados:** Quando usada esta opção, ao atingir o limite de verbas e tentar admitir um novo funcionário será verificado se possuem afastamentos conforme definidos em "Configurações", podendo determinar quais situações serão considerados para disponibilização de verbas.

Para alterar essas definições, basta clicar em "Configurações" à esquerda no assistente.

2.6 – Após finalizadas as parametrizações é necessário efetuar a montagem automática pelo menu Gerência de RH | Controle de Lotação | Montagem Automática para ajustar o controle de lotação conforme cenário atual da empresa.
