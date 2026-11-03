---
content_hash: 7bbd3ab50a110c725297115707974eb4fc14988c77fd0aba8c93ca4cfa62a4b9
fetched_at: '2026-06-29T00:11:03.453293+00:00'
page_id: '622513802'
product: rm
source: tdn-rm
title: Pré-Venda - Pessoas (Portal não migrado)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=622513802
version: 66
---

#FF9000Cadastro de Pessoas no Portal de Imóveis

Na visão de pessoas é possível visualizar alguns campos do cadastro de pessoas e também realizar ações rápidas como edição, exclusão, enviar para banco, visualizar histórico de atendimentos e atribuir a corretor.

Visão de Pessoas Cadastradas

Ao importar o cadastro de pessoas de outras forntes, é importante prestar atenção em dois campos específicos do layout:  **pessoa\_naturalidade\_id** e **id\_conjuge\_naturalidade**.

Quando preencher esses campos com o ID correspondente à naturalidade já existente no banco de dados, o sistema utilizará esses IDs para buscar e retornar o nome do município associado. Em seguida, o campo **NATURALIDADE** nos cadastros da pessoa e do cônjuge será preenchido automaticamente com o nome do município correto.

**Exemplo:** Se você importar um registro onde o **pessoa\_naturalidade\_id** é 123, e esse ID está associado ao município de "São Paulo" no banco de dados, o sistema preencherá o campo NATURALIDADE com "São Paulo".

Abaixo do nome da pessoa e de alguns dados como telefone e e-mail, haverá uma tag indicando a sua situação dentro do sistema. As opções que hoje são exibidas são:

* Novo: pessoa recém cadastrada no sistema e que ainda não teve nenhuma ação para ela. Quando houver algum interesse cadastrado ou uma proposta simulada, esta pessoa terá a sua situação transformada em **Atendimento**.  
    
  ****Status disponíveis:****

  ---
* **Atendimento:** Quando o status deste registro da pessoa é alterado para **Atendimento**, indica que houve ropostas para ela e/ou interesses cadastrados.
* **Comprador:** pessoa que teve a sua proposta efetuada e já foi registrada no Backoffice (RM)
* **Banco:** Quando o status do registro desta pessoa é alterado para Banco, nesta situação a pessoa perde o corretor que está associado ao seu registro e a partir deste momento ficará disponível para outros corretores visualizarem e utilizarem este registro.

Observação:

Para que o Corretor não tenha acesso aos prospects que possuem seu status alterado para banco será necessário desmarcar os parâmetros no perfil associado a este corretor:

Ao editar uma pessoa ou adicionar um novo registro, uma tela será aberta para inclusão dos dados:

Tela de Edição de Prospects

* Ao selecionar estado civil '**União Estável**' ou '**Casado**', os campos de relacionamento **Regime de Casamento** e **Data de Casamento** serão liberados para edição.   
    
  ***Atenção:** Os IDs **2 (padrão: Casado)** e **7 (padrão: União Estável)** são responsáveis pela lógica de exibição do regime no portal e **não devem ser editados**. Labels podem variar por customização, mas os IDs fixos ativam a regra.*
* O campo **Nascimento** só exibirá a data, se o **Pessoa** for salva com uma data de nascimento válida.

**Atribuir Corretor**

---

Possibilitará atribuir um corretor ao(s) prospect(s) selecionado(s).

Para que esta funcionalidade seja liberada, será necessário acessar : Backend > Usuários > Grupos (editando o grupo associado ao usuário que está realizando o processo). Em seguida na lsita de parâmetros marque a opção nas **Permissões: Prospect** "***Vincular prospect ao corretor (ao editar)"***

**Aba Prospect:** Informações relevantes para as pessoas que serão cadastradas e outras informações tais como financeiras, dados profissionais, dados do cônjuge, perfil, etc. O cadastro de pessoas por padrão é parametrizado para ser realizado com o CPF, pois é um campo único que poderá identificar corretamente todas as pessoas cadastradas. Porém é possível parametrizar o portal para o cadastro de pessoas sem o CPF, mas é importante mencionar que cadastrar pessoas sem este identificador poderá levar a duplicidades de informação.

É importante destacar, que é possível realizar a inclusão de um Lead através do **RD STATION,** onde após o mesmo ser inserido através desta aplicação, será apresentado no cadastro deste Lead, um ícone do RD Station, este ícone, ao ser acessado irá apresentar ao usuário os dados cadastrais respectivos deste Lead.

 

Importante: Ao inserir o **CPF** no cadastro, caso o cliente/fornecedor exista no Backoffice, os dados poderão ser importados para o Portal de Imóveis. Se o cliente/fornecedor do Backoffice estiver associado à um corretor, o mesmo será importado para o Portal de Imóveis.

Dentro desta aba ainda existe o campo situação que disponibiliza como opção para preenchimento as situações cadastradas nas opções globais de **Situação Cadastro Pessoa**.

Lead

**Lead**: O campo será atualizado automaticamente após o cadastro da pessoa conter as seguintes informações preenchidas: "Cpf ou Cnpj", "Celular", "E-mail" e "Empreendimento", após este preenchimento o mesmo será definido como Lead: "Não" e Descritivo: "Prospect"

**Aba Interesses**: Após salvar a pessoa cadastrada, é possível navegar pelas abas existentes no topo da tela. A primeira delas é a aba de interesses que serve para descrever qual interesse da pessoa cadastrada. Esta informação poderá gerar relatórios futuros indicando quantidade de pessoas com interesse, o termômetro referente ao interesse desta pessoa (quente, morno, frio), além de informações que poderão ser filtradas através de relatórios desenvolvidos pela empresa, conforme necessidade.

**Aba Documentos:**O tipo do documento da pessoa deve ser cadastrado primeiramente no backend. Ao cadastrar o documento, devemos marcá-lo como vinculado a Pessoa.

Importante: A partir da versão 12.1.32, o limite máximo de tamanho de arquivo passa a ser de 10mb.

Após este cadastro, através desta aba de documentos conseguiremos enviar os arquivos pertinentes à Pessoa.

Tela de Documentos e de Interesses

**Observação:** A partir da versão 12.1.35, é possível que o usuário exclua um cadastro de interesse indevido, onde ele pode criar um outro motivo de interesse ou qualquer outra situação que retrate isto.

    

**Cadastro de interesses:**

* **Termômetro:** Define o nível de interesse do prospect (Frio, Morno, Quente).
* **Tipo de Imóvel:** Define se o imóvel é Residencial, Comercial, etc.
* **Sol:** Indica a posição solar desejada (ex.: Manhã, Tarde).
* **Banheiros:** Quantidade mínima de banheiros desejada.
* **Suítes:** Quantidade mínima de suítes desejada.
* **Área:** Área mínima do imóvel, em metros quadrados.
* **Quartos:** Quantidade mínima de quartos desejada.
* **Vagas:** Número mínimo de vagas de garagem.
* **Valor Máximo:** Valor máximo do imóvel desejado.
* **Empreendimento:** Lista os empreendimentos disponíveis. Ao selecionar um, os campos Bairro e Cidade são preenchidos automaticamente e ficam não editáveis.
* **Bairro:** Preenchido automaticamente com base no empreendimento selecionado. Não editável.
* **Cidade:** Preenchida automaticamente com base no empreendimento selecionado. Não editável.
* **Empreendimento em lançamento:** Checkbox para demonstrar interesse nos empreendimentos em fase de lançamento.
* **Unidade:** Lista as unidades do empreendimento selecionado.
* **Situação:** Define o status do interesse (Aberto, Ganho, Perdido).
  + **Aberto:** Campos Proposta e Motivo permanecem desabilitados.
  + **Ganho:** Habilita o campo Proposta para seleção da proposta que resultou no ganho.
  + **Perdido:** Desabilita o campo Proposta e habilita o campo Motivo, para registrar o motivo da perda.
* **Proposta:** Habilitado apenas quando a situação for Ganho. Permite selecionar a proposta associada.
* **Motivo:** Habilitado apenas quando a situação for Perdido. Permite informar o motivo da perda.

Vinculando Documentos a Pessoa no Backend

**Aba Propostas:**Esta aba é meramente informativa e indica todas as propostas já feitas para a pessoa selecionada.

**Aba Contratos:**Esta aba é meramente informativa e indica todos as propostas que já se efetivaram como vendas e estão no ERP. Mesmo que a venda presente no ERP não seja uma venda realizada pelo portal de vendas, nesta aba, veremos todas as compras feitas pela pessoa selecionada e a situação destas vendas, como: quitada, distratada, etc. Não será demonstrada a situação financeira dos clientes.

Visualizar propostas de uma pessoa

Importante: Somente o usuário com o papel de correspondente bancário, poderá editar as informações financeiras de um prospect, seja no cadastro de pessoa ou na edição da proposta.

Além das informações financeiras, estará disponível também a aba de documentos, bem como a aba de propostas. Todos os outros cadastros permanecerão bloqueados.

**Quando o papel exercido é o de corretor, as informações financeiras ficarão bloqueadas.**

#FF9000Aprovar - Reprovar

A partir da **versão 12.1.33**, quando o usuário que acessa a visão de pessoas faz parte de um grupo cujo papel é o de correspondente bancário, o Portal de Imóveis irá apresentar no final da tela de cadastro as opções **Aprovar e Reprovar.**

Quando clicar na opção **Aprovar**, o correspondente bancário responsável pelo prospect irá aprovar os dados financeiros inseridos na seção de Informações Financeiras. Para que a aprovação seja realizada é necessário preencher o campo data de avaliação.

Ao clicar na opção Reprovar surgirá na tela um campo que deverá ser preenchido informando o motivo da reprovação do cadastro.

As opções Reprovar e Aprovar também estarão disponíveis na edição do cadastro, para visualizar se aquele cadastro foi Aprovado ou Reprovado, basta verificar o seu status na seção de informações financeiras do prospect como mostra a imagem abaixo.

Além disso, quando a validade de avaliação estiver expirada o sistema irá mostrar (Expirado) ao lado do Label "Informações Financeiras".

Quando uma ficha financeira for aprovada, o correspondente que estiver cadastro junto a pessoa, irá receber um e-mail informando sobre a aprovação, da mesma forma, se a ficha financeira for reprovada o corresponde receberá o e-mail, informando a reprovação assim como o motivo.

Se o corresponde estiver vinculado a alguma pessoa que já possui uma proposta que foi cadastrado com aquela pessoa, ele também receberá o e-mail informando a reprovação ou aprovação.

#FF9000Associação de Correspondente Bancário ao Prospect

A partir da **versão 12.1.33,** será possível associar no cadastro da Pessoa, o Correspondente bancário cadastrado no Portal de Imóveis. Somente será possível associar um correspondente bancário a uma pessoa, os dados do correspondente bancário cadastrado na pessoa serão exibidos na seção de dados do proponente ao inserir uma nova proposta.

O correspondente terá acesso somente as abas de prospect e proposta.

\*\*\* Ao utilizar a integração com a ferramenta RD Station, deve ser adicionado o número de telefone e celular completos com DDI. Exemplo (número brasileiro): +55 31 3544 5893

#FF9000Filtros para Correspondentes Bancários

A partir da **versão 12.1.33**, foram criados novos filtros que serão apresentados para os usuários do grupo de correspondentes bancários.

* Todos sem validade de avaliação: Exibe todos os prospects que não possuem o campo Validade da Avaliação preenchida nas informações financeiras;
* Todos com avaliação vencida: Exibe os prospects que possuem o campo Validade da Avaliação preenchido, porém cuja data de validade é anterior a data de hoje;
* Todos com propostas pendentes de avaliação: Exibe os prospects que possuem proposta e cujo o campo Validade da Avaliação não está preenchido.
true#FF9000Cônjuge

No cadastro de pessoa temos a opção do Estado Civil, se a pessoa for casada existe a opção de adicionar dados do **cônjuge**, quando o estado civil for diferente de **Casado**e possuir dados do cônjuge, exibirá um botão para excluir  os Dados do Cônjuge.   
Quando clicar no botão **Excluir dados do cônjuge**, os dados do cônjuge serão apagados do banco de dados e suas informações serão perdidas. Caso não queira excluir não precisa tomar nenhuma ação. 

**OBS**: Ao realizar a inclusão de um novo registro de pessoas **(que possua o mesmo CPF \ CNPJ utilizado em um conjuge já cadastrado e este registro possuir um corretor associado)** o sistema irá apresentar uma mensagem informando que este CPF\CNPJ já encontra-se cadastrado ***(porém, este registro poderá ser salvo, se, o corretor que estiver incluindo esta pessoa for o mesmo que está associado a este cadastro que já encontra-se salvo no sistema).**Caso a pessoa **(que possui este conjuge cadastrado)** não possuir nenhum corretor associado **(o conjuge poderá ser cadastrado no sistema por qualquer usuário).***

true#FF9000Celular | Whatsapp

No cadastro de pessoa temos o campo **Celular**, onde é possível ver o ícone referente ao aplicativo **WhatsApp** quando o telefone está preenchido e é válido. Ao clicar no ícone o usuário será direcionado para uma conversa com o número preenchido. 

true#FF9000Filtros Customizados

Na opção de filtros customizados o usuário pode inserir condições de acordo com os campos selecionados, criando visões particulares e voltadas a uma determinada atuação dentro da visão de prospects.  
podem ser selecionadas lista de valores dinâmicos, ou operadores comuns. Abaixo a imagem representa um filtro customizado, buscando pelo campo "Empreendimento procurado" e por determinado corretor:
