---
content_hash: 75524376b54ba30bafdb9f4abe8481e43d135f72c85a5cacf75fba2fcbf1a40c
fetched_at: '2026-06-29T00:09:08.570484+00:00'
page_id: '389554844'
product: rm
source: tdn-rm
title: Criação do aplicativo do Google
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=389554844
version: 17
---

Índice:

---

.\*ndice:

Atenção A partir da versão 2302, devido a limitações técnicas por parte do Google, não é possível logar no RM.exe (MDI) utilizando autenticação Google.

# Objetivo

---

       A seguir será apresentado o passo-a-passo de como criar um aplicativo do Google para ser usado no RM, como provedor de login.

       Para mais informações sobre as opções de login, acesse o .

# Criando um novo aplicativo do Google

---

**1º-** Acesse o website de desenvolvimento do Google (<https://console.developers.google.com>).

Atenção

Para criar um novo aplicativo do Google, é necessário que a instituição tenha um cadastro válido na plataforma do Google.

**2**º**-** Acesse a opção para selecionar Projeto e depois clique em**Novo Projeto**:

**3º-** Crie um novo Projeto Google, informando o **Nome do Projeto**(Nome do aplicativo) e a **Localização** (opcional) (Organização responsável pelo aplicativo). No exemplo a seguir usaremos o nome: “TOTVS Login Google”:

**4º-**  O próximo passo é gerar as credenciais para acessar as APIs. Acesse o menu **Credenciais > Criar credenciais > ID do cliente OAuth.**

Neste momento, o Google solicita a definição do nome do produto. Basta clicar no botão **Configurar tela de consentimento**.

**5º** **-** Você será redirecionado para a **Tela de permissão OAuth**. Primeiramente, é necessário selecionar o tipo de usuário que terá acesso à sua aplicação. Neste caso, iremos trabalhar com usuários do tipo **Externo**. Após, clique em **Criar**:

Logo após, é necessário preencher as informações dos campos tal qual demonstrado abaixo. O campo **Nome do App** deve receber o nome que aparecerá quando os usuários forem autenticar. Este e o campo **Email para suporte ao usuário** são de preenchimento obrigatório. Também é possível definir configurações adicionais, como: Logo da empresa, URL da política de privacidade, URL de Termos de Serviço e etc (que são opcionais para o funcionamento do serviço desejado, mas recomendável que a instituição faça seu preenchimento).

Avance o restante dos passos, adicione usuários de teste se necessário e finalize a configuração da **tela de permissão OAuth**.

**6º-**  Volte à tela de criação de **Credenciais** (**Passo 4**). Será necessário adicionar para qual plataforma nosso aplicativo será utilizado. Selecione a opção **Aplicativo da Web**e defina o nome do ID Cliente OAuth.

É necessário preencher a **URIs de redirecionamento autorizados**.

Exemplo:

* Para o portal do aluno de teste, nós poderíamos informar um endereço baseado em “localhost”, pois o Portal do Aluno de exemplo encontra-se na mesma máquina em que é feito a configuração (definimos o endereço: <http://localhost:8080/web/app/Edu/PortalEducacional/login/>).
* Para o portal que está configurado com SSL informe o endereço correto de redirecionamento. (Neste exemplo usamos: <https://testeframe.com.br/RM12122/Login.aspx> ou <https://localhost/Corpore.Net/Login.aspx>)
* Para o correto funcionamento do login na MDI, preencha com: <https://www.google.com.br>

**7º-**  Nesse momento, foram gerados o **ID do cliente** e a **chave secreta do cliente**. Esses dados são importantes para fazermos a configuração do aplicativo com o sistema RM. Acesse a credencial criada e anote os dados destacados conforme a imagem abaixo:

falseVer exemplo da configuração deste app no RM. 

Chave Pública (RM) - ID do cliente (Aplicativo Google)

Chave Privada (RM) - Chave Secreta do cliente (Aplicativo Google)

Url de Retorno - Campo preenchido por padrão com o valor "**https://www.google.com.br**"

 e veja mais sobre a configuração dos aplicativos no RM

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.22

false

**Processo:** Aplicativo do Google

falsefalse

**Status:** Em andamento

false

**Data:**

false

**Autores:**

.
