---
content_hash: 7a8c6cc862c7f519ccc015088c27f2e34b736c2fde2c0824aef64b1ce542b8a1
fetched_at: '2026-06-29T00:10:30.448395+00:00'
page_id: '520100384'
product: rm
source: tdn-rm
title: Meu Imóvel - Configurações Iniciais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520100384
version: 49
---

ConfigsIntrodução

O app Meu Imóvel permite aos usuários do TOTVS Construção Gestão de Imóveis, acessar suas funcionalidades com uma melhor usabilidade e adaptável a vários dispositivos mobile como tablets e smartphones. Está disponível na Play Store, para dispositivos Android e na App Store para iPhones.

Clique nos logos abaixo para ser redirecionado para a página de download do seu sistema operacional:

Pré-requisitos para utilização do aplicativo

**Clientes TOTVS:**

* Produto TOTVS na versão 12.1.25 ou superior;
* Acesso externo (público) ao servidor liberado.

**Mobile:**

* Android 7.0 ou superior;
* iOS 8.0 ou superior;
* Acesso à internet.
Procedimentos no Servidor

Para o funcionamento correto do aplicativo Meu Imóvel, é necessário que o **RM.Host.Service.config** esteja devidamente configurado, pois o mesmo conterá informações necessárias para o consumo de serviços do aplicativo. Sem o **RM.Host.exe** iniciado e o **RM.Host.Service.config** configurado, o aplicativo não consegue realizar requisições ao servidor de aplicação.

**Índice**

* **1) Instalação do Certificado no Servidor**
* **2) Configuração de tags no arquivo RM.Host.Service.config**
* **3) Testando a instalação e configuração**
* **4) Considerações finais**

# **1) Instalação do Certificado no Servidor**

---

      Um certificado digital pode ser adquirido através de uma autoridade certificadora (AC), são facilmente encontradas na web, mas também é possível gerar certificados digitais auto assinados.

      Existem várias maneiras de se gerar um certificado digital auto assinado. Abaixo alguns links para ajuda e um certificado auto assinado [**(Clique aqui para baixar)**](https://tdn.totvs.com/download/attachments/244911449/totvs.zip) que pode ser utilizado para cifrar a comunicação, lembrando que o recomendado é que seja adquirido um através de uma AC.

* [PowerShell](https://technet.microsoft.com/library/hh848633)
* [IIS](https://technet.microsoft.com/pt-br/library/ff710475(v=ws.10).aspx)
* [Open SSL](https://www.openssl.org/source/)

falseImportante:

É recomendável que a AC escolhida para gerar o certificado já esteja no diretório de autoridades confiáveis raiz, do gerenciamento de certificados do computador, pois desta forma não será necessário importar a AC em todas as máquinas clientes.

       Salve o certificado no servidor e instale-o conforme imagens abaixo:

false.

**Processo de Instalação:**

1º Passo:2º Passo:3º Passo:4º Passo: 5º Passo: 6º Passo:

 Abra o gerenciamento de **certificados** **do computador (certlm.msc) como administrador** e dê permissão para o usuário do Host nas chaves privadas do certificado:

7º Passo:

 Abra o certificado e copie a impressão digital (thumbprint no inglês) e armazene:

Em seguida, gere um GUID através do site <https://www.guidgenerator.com/online-guid-generator.aspx> e também armazene para ser utiliza-lo nos próximos passos.

# **2) Configuração de tags no arquivo RM.Host.Service.config**

---

<add key="JWTCERTIFICATETHUMBPRINT" value="b4def01ef76a1ff154faef805e6eafce3d411459" />  
- o valor do campo "value" é exatamente o valor do GUID que está contido na Impressão Digital.

<add key="DefaultDB" value="CorporeRM" />  
<add key="HttpPort" value="8028" />

Na seção **<appSettings>**, informe as seguintes tags.

* Informar a tag **JWTCERTIFICATETHUMBPRINT** com o GUID gerado acima. Exemplo:

   

* Informar a tag **DEFAULTDB** com o alias da base de dados. Exemplo:

* Informar a tag **HTTPPORT** com o endereço da porta utilizada para consumir serviços HTTP do host. Exemplo:

# **3) Testando a instalação e configuração**

---

Para garantir que a instalação do certificado a configuração das tags foram bem sucedidas, recomenda-se reiniciar o **RM.Host** e realizar os seguintes testes:

* Utilizando o navegador, acessar o seguinte endereço:  **http://{url do ambiente}/api/swagger/ui/index.**  Como no exemplo abaixo, caso a resposta seja uma tela semelhante, significa que o ambiente de API's está **ativo e respondendo conforme esperado**.

* Utilizando uma ferramenta de **teste de API**, tal como Postman,  realize uma requisição **POST** para o endereço **http://{url do ambiente}/api/connect/token.**Como no exemplo abaixo, caso a resposta seja uma tela semelhante, significa que a autenticação no ambiente de API's está funcionando corretamente.

**Observações:**

* Para este teste, atente-se às opções destacadas na imagem acima. Neste caso foi utilizado como exemplo o usuário "mestre".
* Na aba "Headers", deve-se informar as seguintes opções:

# **4) Considerações finais**

---

Importante garantir também que os parâmetros do aplicativo sejam configurados corretamente, para tanto, siga as instruções no link abaixo.

Primeiro acesso ao Meu Imóvel

**Índice**

* **1) Passo a passo da configuração**
* **2) Termos e Condições**

# **1) Passo a passo da configuração**

---

Vamos seguir esta pequena introdução com as telas iniciais do aplicativo e realizar sua primeira configuração. Lembrando que a configuração é a mesma, tanto para dispositivos Android ou iOS.

Esta é a primeira tela do aplicativo, e é exibida sempre em sua inicialização.

No primeiro momento em que abrimos o aplicativo, teremos acesso a tela de **Boas Vindas**, com a primeira configuração de acesso a ser realizada. neste momento poderemos escanear o QR Code, na opção "**Configurar com o QRCode**" e outra opção manual, **"Não Tenho o QRCode, e agora?"** caso não possua o QR Code disponível.

Iremos detalhar estas opções logo abaixo.

* **Configurar com o QR Code**: Realizar a leitura do QR Code que será disponibilizado na interface do Portal do Cliente, menu "Configurar App". Após a leitura do mesmo através deste menu, será apresentada nova tela para que seja digitada a senha do usuário.

Para a leitura do QR Code, pode ser utilizado quaisquer aplicativos com a propriedade de leitura de QR Codes. Há vários disponíveis na Play Store assim como na App Store.

*QR Code sendo apresentado ao usuário no menu "Configurar APP" do PDC.*

* **Não tenho o QR Code**: Caso não possua acesso ao QR Code, pode-se realizar a configuração manualmente, inserindo a URL de acesso ao Portal do Cliente como mostra a imagem abaixo.

* **Endereço (URL):** Url de acesso ao Portal do Cliente. É a mesma url que utilizamos para acessar o PDC normalmente via browser.

Ao clicar em Concluir, após o preenchimento da URL corretamente, ou caso a configuração tenha sido feita via QRCode, o usuário será direcionado para a tela de login onde deverá informar o usuário e a senha de acesso, bem como parametrizar a biometria para facilitar os seus acessos.

* **CPF ou Usuário:** Seu usuário de acesso ao Portal;
* **Senha:** Sua senha de acesso ao Portal;
* **Leitor biométrico:** Esta opção estará disponível para os celulares que possuam algum tipo de leitor biométrico, facilitando o login. Ao ativar a opção "Leitor biométrico" o aplicativo necessitará ainda das configurações de usuário e senha para um primeiro acesso.  
  Após confirmar a opção de login através da biometria o sistema não necessitará da senha para logar. A interface será alterada para refletir esta mudança:

Importante!

* Caso o usuário necessite, poderá desativar esta opção, logando novamente da maneira tradicional utilizando usuário e senha.
* Caso o celular possua algum tipo de biometria, porém sem nenhuma opção cadastrada no sistema, o Meu Imóvel não apresentará a opção de Leitor biométrico para login.
* Ao minimizar ou deixar o Meu Imóvel em segundo plano, o sistema irá solicitar a biometria novamente para que o aplicativo seja utilizado.

Não esquecer de informar o caminho de URL externo nos Parâmetros do Portal no TCGI. Mesma Porta do HOST.

Problema conhecido de certificado SSL para segurança com protocolo HTTPS

Caso o chamador "Android" não confie no emissor do certificado SSL para o protocolo HTTPS o aplicativo irá apresentar a seguinte mensagem: "Serviço não disponível neste momento, verifique as informações digitadas ou tente novamente mais tarde."  
Porém a mensagem interna do App Meu Imóvel Android é esta: (java.security.cert.CertPathValidatorException: Trust anchor for certification path not found.)  
Neste caso podem haver algumas explicações sobre este problema conforme a documentação oficial do Android:  
<https://developer.android.com/training/articles/security-ssl?hl=pt-br#CommonProblems>  
Os 3 motivos possíveis são:  
1 - <https://developer.android.com/training/articles/security-ssl?hl=pt-br#UnknownCa> => você utiliza uma CA (Autoridade de certificação) em que o sistema não confia. Pode ser que você tenha um certificado de uma nova CA em que o Android ainda não confia.  
2 - <https://developer.android.com/training/articles/security-ssl?hl=pt-br#SelfSigned> => ocorre devido a um certificado auto assinado, o que significa que o servidor se comporta como sua própria CA (Autoridade de certificação). Isso é semelhante a uma autoridade de certificação desconhecida, então é possível usar a mesma abordagem da seção anterior, de CA em que o Android ainda não confia.  
3 - <https://developer.android.com/training/articles/security-ssl?hl=pt-br#MissingCa> => ocorre devido a uma CA intermediária ausente. A maioria das CAs públicas não assinam certificados de servidores diretamente. No entanto, sistemas operacionais como o Android geralmente confiam apenas em CAs raiz diretamente.  
Assim de acordo com esta documentação caso ocorra este tipo de problema de certificado é necessário entrar em contato com o respectivo provedor de certificados, para obter assistência e verificar a possibilidade de ajuste do certificado para permitir o acesso do aplicativo em plataforma Android.

Link complementar: [RH - RM - Meu RH - Erro de carregamento do APP na utilização via HTTPS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035159453-RM-FOP-Meu-RH-Erro-de-carregamento-do-APP-na-utiliza%C3%A7%C3%A3o-via-HTTPS-)

# **2) Termos e Condições**

---

Lei de Proteção Geral de Dados - LGPD

A partir da versão 12.1.27 do TOTVS Incorporação, atendendo a nova legislação de uso de dados, o sistema passará a exibir os **Termos e Condições**para a utilização do **Meu Imóvel** quando o usuário fizer seu primeiro login no aplicativo. O login só será possível se os **Termos e Condições** forem aceitos.

Para que os **Termos e Condições** sejam apresentados, deverá ser parametrizado primeiramente nos parâmetros do TOTVS Incorporação localizado em: **Portal do Cliente > Termo de Aceite > Relatório para exibição do Termo de Aceite.**O relatório poderá ser qualquer relatório definido pelo cliente, que atenda os requisitos da **LGPD**.

O sistema também possuirá um campo para versionamento do Termo de Aceite, localizado em **Portal do Cliente > Termo de Aceite > Versão**. A versão do termo deverá ser sempre incremental, preenchida por um número inteiro e não será possível incluir uma versão anterior a já cadastrada.

Quando se altera o relatório e/ou a versão do termo, o sistema obrigará a exibição do mesmo para o cliente ao realizar o login e só permitirá este login após uma nova confirmação de leitura dos termos.

Para cada confirmação do usuário o sistema gravará na tabela **XAUTORIZACAOLPD** toda a informação do relatório, bem como versionamento, usuário e outros dados.

Feitas estas configurações iniciais, o usuário estará pronto para acessar o aplicativo Meu Imóvel e consultar seus boletos, verificar o status da obra, ver seus comunicados e relatórios pertinentes.

**Outras informações:**

* Está disponível a consulta SQL TINAPPQRCODE.TotvsSQL nos objetos gerenciais para retornar o conteúdo do QR Code. Você pode utilizar essa consulta em relatórios do RM Reports para montar o seu QR Code. Está disponível em versões SQL Server e Oracle.   
  Segue abaixo a consulta SQL para SQL Server:

  
📘 API´S
→
]]>
