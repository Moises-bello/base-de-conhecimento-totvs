---
content_hash: 0af2454492cd65baf73e21a48fbcddcf5605baa0714d67b292760c86f3a0553b
fetched_at: '2026-06-29T00:08:37.784160+00:00'
page_id: '284883738'
product: rm
source: tdn-rm
title: Formulário de Inscrição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284883738
version: 55
---

Índice

# **Formulário**

Importante

Para que o formulário do Portal de inscrições se comporte corretamente carregando todos os dados referentes a endereço e ordene os países em ordem alfabética, no cadastro de País no TOTVS BackOffice Gestão Fiscal, o campo descrição deve estar preenchido para **TODOS** os países cadastrados na base.

É possível parametrizar todo o formulário de inscrição do novo portal do processo seletivo, podendo marcar que um respectivo campo será somente visível ou visível e de preenchimento obrigatório, tanto para candidatos quanto para responsáveis. Os campos estão divididos em grupos para melhor visualização na tela.

Acesse o cadastro de Processo seletivo para parametrizar o formulário de inscrição.

 **TOTVS Processo Seletivo| Cadastros| Processo seletivo| Aba Parâmetros| Sub Aba Visibilidade/Obrigatoriedade de campo.**

Os campos que forem marcados como **obrigatórios,**serão exibidos no portal com um **caractere asterisco '\*'** ao lado do nome com o objetivo de indicar a sua obrigatoriedade.

Importante

A partir da versão **12.1.32.183** e **12.1.33.111** não será possível realizar a alteração de campos que sejam **critérios de unicidade de pessoa** (*CPF, Nome, Estado Natal, Naturalidade e Data de nascimento*).  
  
Portanto, é de suma importância se atentar no preenchimento das informações de unicidade, pois **não** será possível alterá-las posteriormente pelo portal.  
  
A regra se aplica ao candidato, pai(s), mãe(s), responsável financeiro, responsável acadêmico, responsável pela inscrição e também no processo de recuperação de dados do candidato.

* **Indicador de completude**

Em cada grupo das informações do usuários na inscrição é exibido uma imagem de status de completude de preenchimento do formulário. Esse status só ficará verde quando todos os campos obrigatórios estiverem preenchidos.

## **Alteração de dados pessoais**

Caso o candidato esteja fazendo uma nova inscrição ele passará pelo fluxo dos dados pessoais, sendo possível alterar, solicitar alteração ou não alterar os dados.

Caso esteja parametrizado para **Aproveitar dados do cadastro de pessoa** e tenha selecionado **solicitar alteração para o nível de ensino** ou **solicitação alteração para a filial** do item no grupo de **Alteração de dados cadastrais do candidato quando é aluno/pessoa**ao abrir o formulário para alteração será exibido um botão no **canto superior esquerdo** chamado **Solicitar alteração de dados**.

Para mais detalhes sobre os parâmetros acima acesse .

Além disso, uma mensagem de atenção será exibida ao candidato dizendo que não é permitido a alteração dos campos e-mail, endereço, telefone e demais dados preenchidos.

Para que seja possível solicitar a alteração, o candidato deverá clicar no botão **Solicitar alteração de dados** e efetuar a alteração dos campos.

Vale ressaltar que se o campo estiver em branco o candidato poderá informá-lo. Exemplo, se o e-mail estiver em branco, o candidato poderá informá-lo sem ter a necessidade de enviar uma solicitação, este comportamento é somente para campos em branco e-mail, endereço, telefone e demais campos.

Caso esteja parametrizado como **apenas consulta**e **permitir alteração** este botão de **solicitar alteração de dados** não será exibido.

# **Inscrição com estrangeiros**

Dica para inscrição com estrangeiros

Para utilizar inscrição com estrangeiros, o processo seletivo deve **obrigatoriamente** ter as seguintes parametrizações:

* O campo "Estado Natal" do grupo "Dados Básicos" deve ser visível, pois será a partir da seleção desse campo que o processo seletivo saberá se o candidato é estrangeiro ou não.

 **TOTVS Processo Seletivo| Cadastros| Processo seletivo| Aba Parâmetros| SubAba Visibilidade/Obrigatoriedade de campo.**

## **Alteração de dados pessoais**

* O campo "Nacionalidade" do processo seletivo deve ser preenchido.

Assim, quando o candidato for realizar uma inscrição e selecionar um país natal nos dados básicos, que seja diferente do informado na "Nacionalidade" nos parâmetros, o mesmo será considerado estrangeiro. Podendo de acordo com a parametrização, os campos de documentos ficarem somente visíveis.

Inscrição de candidato estrangeiro que já possui cadastro

Se o candidato for estrangeiro e já possuir cadastro, as informações dos campos destacados abaixo serão habilitadas para o preenchimento novamente

Isso ocorre quando o campo “Estado” cadastrado no RM não possuir vínculo com o "Pais" conforme o exemplo abaixo:

Para que este cenário não ocorra, o cadastro do “Estado” no RM deve possuir vínculo com o campo “Pais” conforme o exemplo abaixo.

Se o "Estado" possuir vinculo com o "Pais" as informações "Pais natal", "Estado natal", "Naturalidade"  serão carregadas automaticamente sem a necessidade do candidato informa-las novamente.

# **Responsáveis**

Utilização do parâmetro de responsável opcionalAtenção

Esta funcionalidade está disponível a partir da versão 12.1.24, patch 186.

Ao utilizar o parâmetro "Desconsiderar parametrização de obrigatoriedade para TODOS os campos do responsável", todos os campos daquele responsável serão opcionais, porém, caso o usuário preencha qualquer campo do responsável, então, para finalizar  a inscrição o usuário deverá preencher todos os campos obrigatórios daquele responsável.

 **Processo Seletivo| Cadastros| Processo Seletivo| Aba Parâmetros| Sub Aba Geral 1/3**

É possível habilitar a validações de débitos financeiros para o responsável financeiro. Para saber mais informações [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=727373766)

Pai / Mãe

Em concordância com a legislação realizamos um ajuste na apresentação das informações dos dados dos responsáveis para que não seja mais apresentado o descritivo “**Mãe**” ou “**Pai**”, agora será apresentado o descritivo “**Filiação 1**” e “**Filiação 2**”, sendo necessário indicar qual o tipo de filiação que será cadastrado.

Legislação:

***"A Lei de Registros Públicos (Lei nº 6.015/73) foi alterada em 2009, pela Lei nº 11.924, para tornar possível ter dois pais e duas mães no assento do nascimento da pessoa natural”***

Alterações disponíveis a partir das versões: 12.1.31.250 /12.1.32.189 / 12.1.33.116

**Apresentação no portal**

Na imagem abaixo, o dados da Filiação 1 e Filiação 2 serão opcionais.

Tipo de filiação

Com a mudança do descritivo das informações para “**Filiação 1**” e “**Filiação 2**” foi criada uma nova parametrização que permite definir o tipo de filiação que será obrigatório, sendo de total responsabilidade do cliente a parametrização.

Caso o **Tipo de filiação obrigatório**seja marcado como **"Não se aplica"**, o sistema não irá fazer validação para algum tipo de filiação específico.

Caso o **Tipo de filiação obrigatório**seja marcado como **"Pai"**, o sistema somente permitirá prosseguir caso seja informado **ao menos uma filiação** com o tipo **"Pai"**.

Caso o **Tipo de filiação obrigatório**seja marcado como **"Mãe"**, o sistema somente permitirá prosseguir caso seja informado **ao menos uma filiação** com o tipo **"Mãe"**.

Caso o **Tipo de filiação obrigatório**seja marcado como "**Ambos"**, o sistema somente permitirá prosseguir caso seja informado **uma filiação do tipo "Mãe" e uma do tipo "Pai".**

Opção disponível a partir da versão 12.1.32.206 e 12.1.33.128 sendo necessário executar o **RM Atualizador**.

Dados da filiação, responsável financeiro e acadêmico 

Não será possível cadastrar um pai/mãe, responsável financeiro ou acadêmico com o mesmo numero de cpf já informado no cadastro.

Importante

Validação disponível a partir da versão **12.1.2205.202.**

Caso o candidato, deseje associar pai ou mãe como responsável financeiro ou acadêmico deve selecionar no campo **"Utilizar o usuário selecionado como responsável".**

Responsavel financeiro e acadêmico 

O processo seletivo por padrão não impede que o responsável financeiro ou acadêmico sejam menores de 18 anos, porém é possível caso a instituição deseje, optar por impedir que estes papeis sejam preenchidos por pessoas menores de 18 anos.

Para mais informações acesse: 

# **Ensino Básico**

A partir das versões 12.1.27.314, 12.1.28.223, 12.1.29.153 e 12.1.31 e com todos os scripts executados o formulário de inscrição passou a exibir para o candidato os  ofertados na  como **primeira opção**, as outras opções não serão consideradas para trazer os itinerários. Além disso, as validações de mínimo e máximo de seleção de itinerários sempre será considerado também a  como **primeira opção**.

Importante

Para a exibição do itinerário formativo na Matrícula pela central de candidatos é necessário a seleção de pelo menos uma das disciplinas exibidas no grid de itinerário formativo.

Ao selecionar uma área de interesse na primeira opção que estiver ofertando **dois** itinerários e a quantidade **mínima** e **máxima** for **dois**, de forma automática os dois itinerários formativos já serão selecionados. O mesmo vale se a quantidade **mínima** e **máxima** for **três** e a área de interesse estiver ofertando **três** itinerários, também será marcado os **três** itinerários e assim por diante.

O candidato poderá escolher os  para efetuar a sua inscrição. Vale lembrar, que no cadastro da  é configurada quais são os itinerários que serão ofertados e qual será o mínimo e máximo. Ao finalizar a inscrição será validado se a quantidade de itinerários selecionados está atendendo ao mínimo e máximo, caso não esteja a inscrição não poderá ser efetuada. Ao finalizar a inscrição, será exibido uma tela com os dados para confirmação, esta tela também irá mostrar os itinerários selecionados, conforme abaixo.
