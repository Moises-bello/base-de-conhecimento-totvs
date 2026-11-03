---
content_hash: 6b75e01d3f10b2480c9bc3c5e602b4955fbc84e69c90ad90f0a69416cef455c4
fetched_at: '2026-06-29T00:11:53.715450+00:00'
page_id: '850703039'
product: rm
source: tdn-rm
title: 14. Carteirinha
type: documentation
url: https://tdn.totvs.com/display/LRM/14.+Carteirinha
version: 19
---

A Carteirinha tem como objetivo exibir a identificação do aluno por meio de um QR Code, que poderá ser utilizado nas dependências que exigem sua apresentação.

Configurações necessárias

Para o correto funcionamento da carteirinha, é necessário seguir os seguintes passos:

* O [URL Rewrite](https://tdn.totvs.com/pages/viewpage.action?pageId=789399208) e o [Application Request Routing Cache (ARR)](https://tdn.totvs.com/pages/viewpage.action?pageId=549518554) ;
* Configurar a URL do FrameHTML em **Ambiente | Parâmetros | Parâmetros Globais |Frame HTML**

Configuração das informações a serem exibidas na carteirinha

As informações apresentadas na **Carteirinha Digital** são parametrizadas em: **Gestão Educacional → Parâmetros → eduCONNECT → Carteirinha Digital.**

Abaixo estão os campos disponíveis para exibição:

* + **CPF**
  + **Curso**
  + **Campus/Polo**
  + **Data de Nascimento**
  + **Data de Validade**: A data de validade da carteirinha considera, prioritariamente, a **Data de Validade da Carteirinha** definida no sistema.  
    Caso essa informação não esteja preenchida, será utilizada a **Data de Término** ou **Previsão de Término** cadastrada no **Período Letivo** da **matrícula mais recente** do aluno.
  + **Foto do Aluno**: Se o aluno não possuir uma foto cadastrada em seu perfil, ao acessar o aplicativo será exibida uma **imagem padrão (sem foto)**.
  + **Habilitação**
  + **Série**
  + **Logotipo**: O administrador do sistema pode definir se será utilizado o **logotipo cadastrado na Coligada** ou na **Filial**.
  + **RA**
  + **RG**
  + **QRCode para Automação**: Para habilitar essa funcionalidade, é necessário marcar a opção **“Ativar QRCode para automação”.** O QRCode é utilizado para identificação do aluno em dependências e serviços que façam uso desse recurso. O QRCode, tem como objetivo exibir a identificação (conforme a parametrização). O Administrador do sistema tem a opção em parametrizar uma das opções:

* + **RA**: Se esta opção for selecionada, ao realizar a leitura do QRCode será exibido o **RA do aluno**.
  + **Código do Usuário**: Se esta opção for selecionada, ao realizar a leitura do QRCode será exibido o **Código do Usuário** do aluno — ou seja, o código utilizado para **acesso ao aplicativo**.

* + #### **QRCode para automação gerado através do:** O QRCode, tem como objetivo exibir a identificação (conforme a parametrização). O Administrador do sistema tem a opção em parametrizar uma das opções

#### 

* + **Campo Complementar**: Se esta opção for selecionada, ao realizar a leitura do QRCode será exibido o **valor do Campo Complementar** definido para o aluno. A configuração desse campo é feita em: **TOTVS Gestão Educacional → Configurações → Campos Complementares → Aluno.**

* + **Nº da Carteirinha**: Se esta opção for selecionada, ao realizar a leitura do QRCode será exibido o **número da carteirinha** do aluno. Essa informação é parametrizada em: **TOTVS Gestão Educacional → Currículo e Oferta → Aluno e Professor → Aluno → Aba “Carteirinha” (Anexo Matrículas no Período Letivo).**

Contexto Ensino Básico

Para o contexto de **Ensino Básico**, serão exibidas as **opções de dados pessoais do aluno**, além da **opção de Série** correspondente ao seu nível de ensino.

Contexto Ensino Superior

Para o contexto de **Ensino Superior**, serão exibidas as **opções de dados pessoais do aluno**, além das opções de **Habilitação** e **Campus/Polo** vinculadas à matrícula do aluno.

Nome do aluno

O **nome do aluno** será **sempre exibido** na carteirinha, não sendo possível remover ou ocultar esta informação.

Regra de negócio para exibição da carteirinha

Para que a **Carteirinha Digital** seja exibida corretamente, é necessário atender aos seguintes critérios:

* **Status no Período Letivo**: O aluno deve ter o **Status “Aluno Ativo”** marcado no Período Letivo correspondente para que a carteirinha seja exibida.

* **Cadastro do Período Letivo**: Na matrícula do aluno, é necessário que esteja preenchida **a Data de Validade da Carteirinha**, ou, alternativamente, **a Data de Término** ou **a Previsão de Término** do Período Letivo correspondente.

Permissão de acesso a carteirinha no eduCONNECT

Para acessar a funcionalidade da **Carteirinha Digital**, o aluno deve possuir a **permissão configurada em**:

**Serviços Globais | Segurança | Perfil | "Sistema" Educacional | eduCONNECT | Permitir acesso a Carteirinha Digital.**

**Configurações | Parâmetros | eduCONNECT | eduCONNECT 5/5**

Visualização da carteirinha no eduCONNECT

Ao **logar no aplicativo** com as permissões adequadas e clicar no menu **“Carteirinha”**, será exibida a **Carteirinha Digital**, apresentando todas as **informações previamente parametrizadas para o aluno**.

 

A **Carteirinha Digital** é de **uso pessoal** e, portanto, está disponível apenas para o **usuário correspondente ao aluno**.

Matrícula em Mais de um Curso/Habilitação

Caso o aluno esteja **matriculado em mais de um Curso ou Habilitação**, serão exibidas **Carteirinhas separadas** para cada curso correspondente.

Ampliação do QRCode

O aluno pode **aumentar a visualização do QRCode** para melhor leitura. Para isso, basta **clicar sobre o QRCode** no aplicativo.

Autenticidade da carteirinha

A **Autenticidade da Carteirinha** tem como objetivo **certificar que os dados apresentados estão validados junto à Instituição de Ensino**, garantindo sua **legitimidade**.

Para que o **link de validação** seja exibido na carteirinha, é necessário habilitar o parâmetro **“Validação da autenticidade”** em: **Gestão Educacional → Parâmetros → eduCONNECT → Carteirinha Digital**.

O **QRCode** é gerado com base nas **informações exibidas na Carteirinha** e **criptografado**, garantindo que o usuário **não possa manipular a autenticidade dos dados**.

Consulta pública

As informações da **Carteirinha Digital** são de **consulta pública**. Portanto, **não é necessário usuário ou senha** para acessar os dados. Ou seja, **qualquer pessoa pode consultar as informações** a partir da leitura do **QRCode** exibido na carteirinha do aluno.

Página de verificação da autenticidade da carteirinha

A página de **autenticidade da Carteirinha** pode apresentar as seguintes situações ao ser acessada:

Aluno(a) regularmente matriculado(a) na instituição

O sistema exibirá a mensagem: **“Aluno(a) regularmente matriculado(a) na instituição”** quando a carteirinha estiver **válida**.

Caso os parâmetros de **Curso** e **Logotipo** estejam habilitados para exibição na carteirinha, eles também serão apresentados na página de autenticidade, conforme configurados em:

Aluno(a) não se encontra regularmente matriculado(a)

O sistema exibirá a mensagem: **“Aluno(a) não se encontra regularmente matriculado(a)”** quando a carteirinha **não estiver mais válida**. Isso pode ocorrer, por exemplo, se o aluno tentar utilizar um **print do QRCode** obtido anteriormente, após a sua matrícula ter sido encerrada.

Caso o parâmetro de **Logotipo** esteja habilitado para exibição na carteirinha, ele será apresentado na página de autenticidade, conforme configurado em: **Gestão Educacional → Parâmetros → eduCONNECT → Carteirinha Digital**.

**Observação:** Mesmo que o parâmetro de **Curso** esteja habilitado para exibição na carteirinha, **essa informação não será exibida** na página de autenticidade quando a carteirinha estiver inválida.

Token de autenticidade da carteirinha inválido

O sistema exibirá a mensagem: **“Token de autenticidade da carteirinha inválido”** quando o **token enviado para validação** não for válido. Isso pode ocorrer, por exemplo, se o aluno tentar **manipular a chave do token** gerada pelo sistema.

Para a consulta de autenticidade válida, aplicam-se as seguintes regras:

* A **personalização de cores** não será considerada, mesmo que definida na parametrização do tema do eduCONNECT;
* O **logotipo** não será exibido conforme cadastrado na parametrização. Em vez disso, será apresentada a **logo informada na tela de login do Portal do Aluno**, localizada em:  
  `FrameHTML\web\app\Edu\PortalEducacional\login\assets\img\logo-responsivo.png`.

Personalização de cores do eduCONNECT

A **página de verificação da autenticidade** respeita a **personalização de cores** configurada no **eduCONNECT**, garantindo que a aparência esteja alinhada com o tema definido pela instituição.
