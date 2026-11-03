---
content_hash: ee4e3920b6327515faac8314b28c669c06db28b50a3c3dbb728636575ca264d0
fetched_at: '2026-06-29T00:08:07.698312+00:00'
page_id: '237385004'
product: rm
source: tdn-rm
title: TOTVS API Services
type: documentation
url: https://tdn.totvs.com/display/LRM/TOTVS+API+Services
version: 46
---

# Descrição

---

       O TOTVS API Services (TAS) é uma poderosa ferramenta capaz de realizar a interface entre serviços públicos da internet e os sistemas TOTVS. Serviços como Consulta de CEP, Consulta de Qualificação no eSocial, Consulta de CPF e CNPJ pela receita federal, Sintegra, Suframa, entre outros, são consumidos pelas aplicações de forma transparente para o usuário e sem necessidade de acesso direto ao browser de internet.

# Integração com o RM

---

       O TAS é integrado nativamente ao RM, bastando apenas configurar endereço de Url e Chave de Autenticação, em *Parâmetros Globais*, conforme .

Url de serviços do TOTVS API Services: [https://totvsapiservices.totvs.com.br](https://totvsapiservices.totvs.com.br/)  
Chave de Autenticação (Token): Verifique no próximo tópico como conseguir sua chave.

# Exemplos de uso do TAS dentro do RM

---

## Completar cadastro

Já se deparou com sites onde você escreve o CEP e o sistema completa os dados de Rua, Bairro, Cidade e Estado?

O mesmo pode ser feito utilizando os serviços de TAS, como por exemplo, completar os dados de Razão Social, Inscrição Estadual, Endereço, Situação cadastral, Telefone e Email, apenas digitando o CNPJ do fornecedor.

---

## Configurando o TAS para completar cadastro

Para que o autocompletar funcione nos formulários do RM, é necessário configurar a Integração com o formulário que deve receber os dados do TAS.  
Como exemplo vamos configurar o serviço “**Correios - Pesquisa de CEP**”, esse é um serviço liberado e com consumo ilimitado das consultas, e a tela que usamos para exemplo é a tela de Cadastro de Coligadas em **Serviços Globais > Administração > Cadastros > Coligadas.**

Primeiro devemos entrar no formulário de Endereços que deve ser preenchido. Esse formulário deve possuir o menu do **TAS** (TOTVS API Services), conforme imagem abaixo:

Ao clicar no menu, ele abre a opção de **Gerenciar**.

O primeiro botão é para “**Fazer a integração dessa tela com o serviço TOTVS API Services**”

O segundo botão é para  “**Gerenciar serviço TOTVS API Services associados à essa tela**”.

Escolha “**Fazer a integração dessa tela com o serviço TOTVS API Services**”. Deve abrir a tela de Seleção de Serviços.

Essa tela possui 3 campos.

* **Pesquisar por**: Tudo, Título, Nome, Descrição, Provedor e Tag;
* **Pesquisa**: onde colocamos o termo da pesquisa;
* **Resultados**: Onde aparece o resultado da pesquisa feita;

> **OBS**: O campo de pesquisa, dependendo do serviço do TAS que está sendo usado, pode ser "case sensitive", quer dizer que pode ser sensível a maiúsculo e minúsculo. No nosso exemplo dos Correios, pesquisando por cep ao invés de CEP tem diferença no resultado.

Temos um exemplo na imagem abaixo:

Preencha o campo de Pesquisa com o termo que necessita e clique no botão "**Pesquisar"**. Após, selecione o item na lista de Resultados e clique no botão “**Selecionar**” no canto inferior direito da tela. A janela do **TOTVS API Services** deve aparecer da seguinte forma.

A partir desse ponto, devemos configurar o de/para das informações que devem vir do TAS para os campos do formulário.

Mas para que funcione, devemos observar que, cada serviço que vamos integrar possuem duas configurações a serem feitas:

1. **Parâmetros**: São os parâmetros de entrada para a consulta ao serviço utilizado, nesse exemplo o serviço de pesquisa de CEP exige somente o parâmetro CEP.
2. **Resultados**: São os campos de resultado do retorno da pesquisa ao serviço. Eles devem ser exibidos após o vínculo dos campos do formulário com os campos do serviço.

No nosso exemplo de “**Correios - Serviço de CEP**” temos como parâmetro o campo CEP, que nada mais é do que o valor do CEP a ser pesquisado no Serviço. Posicionando o mouse em cima do parâmetro, ele exibe a informação de uso.

Clique na caixa de seleção CEP e arraste até o controle para fazer o vínculo.

Isso fará com que o valor digitado no campo CEP seja usado como parâmetro na consulta ao serviço de CEP.

Agora a funcionalidade de vínculo já deve estar disponível nos campos do formulário, para conseguir visualizar, posicione o mouse em cima do campo, deve aparecer um ícone no canto superior. Clicando nele podemos fazer o vínculo do campo com o resultado do serviço.

Os resultados são os campos que o Serviço retorna com os dados solicitados. Em sequência temos as seguintes funcionalidades:

1. **Expressões**: Caso necessite trabalhar de alguma forma o valor do campo que vai ser preenchido, podemos usar uma Função para isso. Um bom exemplo seria usar a função de texto Upper para colocar todos os caracteres do campo em maiúsculo. Mais adiante teremos um exemplo disso.
2. **Remover Ligação dos Controles**: Remove o vínculo do campo do formulário com o campo do Resultado do serviço.
3. **Salvar**: Salva a configuração realizada.
4. **Cancelar**: Cancela a configuração realizada.

Os vínculos devem ser feitos agora campo a campo, clique no ícone de vínculo e clique duas vezes em uma das opções. Podemos acompanhar os campos configurados na janela do TOTVS API Services que aparece junto ao formulário de cadastro.

> **Exemplo**: No campo Rua, clique no ícone de vínculo e depois dois cliques em Endereço.

Após o término dos vínculos, é possível salvar as configurações no botão de “**Salvar alterações do serviço TOTVS API Services**” ou cancelar no botão de “**Cancelar alterações do serviço TOTVS API Services**”.

**Exemplo de uso**

## Editando a Configuração

Também é possível editar e alterar uma configuração já feita anteriormente.

**Usando Expressões para incluir os resultados nos campos vinculados.**

Como exemplo vamos alterar o campo Cidade para que ele fique com todas os caracteres em maiúsculo.

No modo de Edição, clique no ícone de vínculo do campo Cidade e escolha o botão “Alterar para expressão”.

Dentro dos parênteses, inclua o parâmetro Cidade, conforme exemplo abaixo.

Clique no botão Salvar.

E na tela da **API TOTVS Serices**, clique em “**Salvar alterações do serviço TOTVS API Services**”.

**Exemplo de uso**

## Removendo uma configuração existente

Para excluir uma configuração existente, basta ir no menu **API TOTVS Services > Gerenciar**, escolher no menu de **“Gerenciar serviço TOTVS API Services associados a essa tela**”, escolha o serviço configurado e depois clique em Remover.

Com isso a configuração existente no menu é removida.

## Ao editar um cadastro existente.

Quando entramos em um cadastro já existente, a localização TOTVS API Services é o mesmo, porém cuide pois ele deve aparecer conforme imagem abaixo:

---

## Automatizar saneamento do cadastro

Apesar de ter a certeza de ter cadastrado os dados corretamente, sabemos que os mesmos são mutáveis e nem sempre temos tempo de revisar e ajustar os dados acompanhando a velocidade que o mesmos mudam.

Agora a atualização de todos os registros da sua base (ou apenas dos que você selecionar) está a 1 clique de distância!

Utilizando uma Fórmula Visual como Processo (fazer download do exemplo ), a verificação e atualização dos dados é feita de forma automática de acordo com os dados da Receita Federal.

Cadastrando uma Fórmula Visual como Processo

Utilize a [documentação a seguir](https://tdn.totvs.com/pages/viewpage.action?pageId=271660317#Par%C3%A2metrosdeexecu%C3%A7%C3%A3odeF%C3%B3rmulaVisualviaprocesso-ExecutandoaF%C3%B3rmulaVisual:) para aprender a cadastrar uma Fórmula Visual para ser disparada como um Processo dentro de uma Visão

# Contratando o TAS

---

> Uau! Esse TAS é muito maravilhoso, como eu faço para conseguir usar?
>
> É gratuito? É caro? Tem como testar antes de contratar, ou usar um volume pequeno?

Vamos por partes, o TAS é um serviço em nuvem que gera custos para a TOTVS ao ser utilizado, por isso é necessário um contrato a parte para funcionar. Porém, existem **planos gratuitos** e planos pagos.

Para maiores informações, sobre quantas requisições e quais serviços estão disponíveis no plano gratuito, ou quanto custa o plano e cada requisição adicional, procure no [página oficial do TAS no TDN](https://tdn.totvs.com.br/display/public/TASS/Sobre+o+Totvs+API+Services#SobreoTotvsAPIServices-Ades%C3%A3o), pois por motivos comerciais, estas informações podem mudar constantemente.

# Adesão

---

Para saber sobre os planos disponíveis e outras informações sobre o TOTVS API Services, consulte [Sobre o Totvs API Services](https://tdn.totvs.com/x/4inFK).

# Chave de autenticação (Token)

---

Contratações do TAS após novembro/2025 não necessitam de preenchimento da Chave de autenticação (Token). O contrato do TAS estará vinculado ao License Server.

Contratações anteriores, o preenchimento é opcional. A Chave de autenticação pode ser consultada no portal manager,totvs.app.

# Serviços disponíveis

---

# Avisos

---

Possibilidade de indisponibilidade

Por se tratarem de serviços públicos, estamos sujeitos a mudanças de comportamento e à disponibilidade destes serviços. Sendo assim pedimos compreensão quando houver decorrência destes.

A TOTVS continuamente buscará soluções para manter a disponibilidade destes serviços, mas nos reservamos o direito de remover, a qualquer momento, sem aviso prévio, alguns dos serviços, bem como não nos responsabilizamos por qualquer prejuízo causado pelas informações ou disponibilidade dos serviços.

Suporte ao desenvolvimento

A TOTVS não oferece suporte para o desenvolvimento ao TAS, pois seu uso é restrito aos softwares da TOTVS.

Anexos:

Exemplo de Fórmula Visual: AcertaSituacaoCadastral.TotvsWF

250
