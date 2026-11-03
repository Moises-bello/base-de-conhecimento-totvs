---
content_hash: 0b8027f4656e32c83cdadf7501e6fff35091f0ca2c107a4d6bb568f7467399ad
fetched_at: '2026-06-29T00:11:38.750874+00:00'
page_id: '784772369'
product: rm
source: tdn-rm
title: 02.06 Assinatura do contrato
type: documentation
url: https://tdn.totvs.com/display/LRM/02.06+Assinatura+do+contrato
version: 11
---

Este passo tem como objetivo exibir o contrato financeiro juntamente com uma validação de aceite dos termos do contrato.   
O contrato que será exibido deverá ser definido nos parâmetros financeiro da matrícula:

Importante

A utilização do componente de identificador de relatório (Certificador de Relatórios) não irá funcionar no contrato da Matrícula pela Central do Candidato (TABELA GRELBATCH).

Motivos:

1o – O usuário, que estiver realizando o processo de matricula pode ter acesso ao GUID sem antes ter finalizado o processo que confirma a matrícula, se realizar somente a confirmação do “li e aceito” e obter um código válido.

2- A execução de relatório do reports para a matrícula pela central do candidato, em sua jornada única, executa o mesmo relatório no mínimo duas vezes antes do “li e aceito” e duas após o “li e aceito”, gerando chaves diferentes. Isso acontece para que seja gerada uma imagem que  é exibida no modal da tela apresentada, para que não tenhamos popup. Uma outra geração é feita para que seja criado o PDF para impressão do relatório. Desta forma o usuário que estiver realizando o processo de matrícula pela central pode ter impresso um relatório que tenha uma chave inválida.

Orientamos o uso da integração com TAE (TOTVS Assinatura Eletrônica) para o que se propõe a fazer referente a segurança do controle de assinaturas e impressão do contrato.

Importante

Quando o parâmetro que define o próprio aluno como responsável financeiro estiver ativado, é essencial que o processo seletivo seja configurado para exigir o preenchimento dos campos de data de nascimento, naturalidade e estado natal. A ausência dessas informações pode impedir a conclusão da matrícula.

**Assinatura de contrato da matrícula utilizando token/chave de segurança**

Foi disponibilizado um nível de segurança a mais na matrícula, agora a instituição tem a possibilidade de ativar a opção de assinatura do contrato da matrícula com token. Com esse parâmetro marcado, será exibido para os candidatos/responsáveis da inscrição uma opção de assinatura do contrato informando um token que chegará no e-mail cadastrado do usuário que está logado no momento e realizando a matrícula, que pode ser o candidato ou responsável da inscrição.

false

Para enviar o e-mail com o token para o usuário que está realizando a assinatura do contrato, deve ser cadastrado uma nova mensagem de notificação com o objetivo "Enviar token para a validação da assinatura do contrato de matrícula".

Acesse a documentação para mais informações: <https://tdn.totvs.com/x/6fr6E>

Ao chegar na etapa de assinatura do contrato, o candidato/responsável da inscrição deve ler o contrato da matrícula, clicar no botão "Li e aceito os termos do contrato" e em seguida, só será possível finalizar a matrícula, após clicar em "assinar contrato", assim será enviado um e-mail para o usuário que está logado e o mesmo terá que informar o número do token recebido no e-mail no campo específico. Com o token correto, será possível finalizar a matrícula.

Caso o candidato/responsável da inscrição não finalize a matrícula naquele instante, volte mais tarde para finalizar, o token **não será regerado**, somente será reenviado o e-mail com o mesmo token.

Será salvo na tabela referente a assinatura, a data hora do envio do e-mail e para qual e-mail foi enviado.

Para realizar a parametrização, marque a opção "Utilizar token para validação da assinatura do contrato" na área de interesse ofertada do processo seletivo:

Instruções sobre a opção "Somente o responsável financeiro pode aceitar o contrato"

* **Envio de e-mail com o token**  
  Ao selecionar a opção *"Somente o responsável financeiro pode aceitar o contrato"*, o e-mail contendo o token será enviado exclusivamente para o endereço de e-mail cadastrado no responsável financeiro informado durante a matrícula. Assim, é imprescindível que exista um cadastro para o responsável financeiro e com um e-mail válido.

A opção *"Somente o responsável financeiro pode aceitar o contrato"*estará disponível somente para funcionalidade de assinatura do contrato via token.

* **Exclusividade do envio**  
  O token **não será enviado** para o e-mail do candidato ou do responsável pela inscrição, pois neste cenário, o contrato deve ser aceito unicamente pelo responsável financeiro.
* **Requisitos de e-mail do responsável financeiro**  
  Caso o responsável financeiro seja uma pessoa diferente do candidato ou do responsável pela inscrição, é obrigatório que o e-mail informado seja **diferente** do e-mail do candidato ou do responsável pela inscrição. Se os endereços forem iguais, o processo de matrícula **não será permitido**.

Observação importante

Para candidatos menores de idade, **não recomendamos** selecionar a opção *"Responsável financeiro é o próprio aluno"*. Nesse caso, orientamos optar pela configuração *"Responsável financeiro do Processo Seletivo"*.

Adicionalmente, verifique que a funcionalidade *"Permite cadastrar ou alterar dados do responsável financeiro"* esteja habilitada na aba *"Alteração de dados"*. Essa configuração exige o cadastro de um responsável financeiro, garantindo que o e-mail com o token para assinatura do contrato seja enviado corretamente.

Acessando a matrícula no portal de inscrições, etapa de assinatura do contrato, é possível visualizar o botão de assinar contrato, que só será habilitado após ler e aceitar os termos.

Exemplo do e-mail enviado para o usuário

Após realizar os passos acima, o candidato/responsável da inscrição pode finalizar a matrícula, salvando na tabela referente a assinatura, os dados dessa assinatura realizada.

Disponível somente na versão 12.1.29

Para consultar as assinaturas do contrato basta acessar nos anexos do contrato a opção de visualizar assinaturas.

**Utilizar Totvs Assinatura Eletrônica para assinatura do contrato**

Agora podemos utilizar a [Integração TOTVS Assinatura Eletrônica](http://tdn.totvs.com/pages/viewpage.action?pageId=578823895) para a assinatura do contrato quando o aluno realizar sua matrícula pela central do candidato. Foi disponibilizado um novo parâmetro com o objetivo de permitir que o contrato gerado imediatamente após a matrícula pela central do candidato não seja assinado no primeiro instante. Desta forma, podemos utilizar os recursos da [Integração TOTVS Assinatura Eletrônica](http://tdn.totvs.com/pages/viewpage.action?pageId=578823895) para realizar essa validação.

 Caminho de acesso para o novo parâmetro:

* **TOTVS Educacional Processo Seletivo| Cadastros| Área de interesse Ofertada| Aba Matrícula| Aba Financeiro**

Com o parâmetro **"Utilizar Totvs Assinatura Eletrônica para assinatura do contrato"** marcado, será obrigatório o preenchimento da mensagem de notificação **"Enviar e-mail informando que a assinatura do contrato será validada com Totvs Assinatura Eletrônica"**informando ao aluno que ele receberá um e-mail para realizar a assinatura do contrato.

Importante

Para indicar ao aluno que ele receberá um e-mail para realizar a assinatura do contrato, deve ser cadastrado a mensagem de notificação com o objetivo **"Enviar e-mail informando que a assinatura do contrato será validada com Totvs Assinatura Eletrônica"**. Caso contrário, o aluno não conseguirá prosseguir com sua matrícula pela central do candidato devido a seguinte validação.

Acesse a documentação para mais informações: <https://tdn.totvs.com/x/6fr6E>

Com o parâmetro marcado e a mensagem de notificação preenchida os contratos gerados após a matrícula pela central do candidato não serão assinados no primeiro momento. Além disso, será enviado um e-mail para o candidato informando que em breve ele receberá um e-mail para a assinatura do contrato. Desta forma, podemos realizar a validação através da [Integração TOTVS Assinatura Eletrônica](http://tdn.totvs.com/pages/viewpage.action?pageId=578823895).
