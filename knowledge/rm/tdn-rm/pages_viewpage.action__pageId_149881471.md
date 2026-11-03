---
content_hash: a8e7af12fcbbc70cdabad0b2e1c612928dddf5a7a65bff0488789e693dee03f7
fetched_at: '2026-06-29T00:05:56.308886+00:00'
page_id: '149881471'
product: rm
source: tdn-rm
title: Utilizando a atividade "Executar Web Service"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=149881471
version: 14
---

# Índice:

---

* Objetivo:
* Especificação:

# Objetivo:

---

     Este documento tem por objetivo especificar a atividade “Executar Web-Service” disponível na Fórmula Visual.

# Especificação:

---

     A atividade “Executar Web Service” permite que um Web Service (TBC ou Externo) seja consumido. Seu retorno pode ser utilizado em diversas atividades disponíveis na fórmula visual.

Para começarmos a utilizar a atividade, temos que conhecer os parâmetros que ela recebe.

| N° | Nome do Parâmetro | Descrição do Parâmetro | Obrigatoriedade |
| --- | --- | --- | --- |
| 1 | Method (Método) | Método do Serviço que será chamado. | GreenObrigatório |
| 2 | Pré Autenticar\* | Alguns Web Services necessitam de Pré-Autenticação, nesses casos o valor deve ser "True".  **Obs.: A partir da 12.1.19, os WebServices do RM precisam de Pré Autenticação.** | YellowOPCIONAL |
| 3 | Senha | Senha que será usada na requisição ao Web Service. | YellowOPCIONAL |
| 4 | Usuário | Usuário que será usado na requisição ao Web Service. | YellowOPCIONAL |
| 5 | Wsdl | Descritor do serviço de Web Service. | GreenObrigatório |

OBS

Quando o Pré Autenticar é marcado como verdadeiro o cabeçalho **WWW-authenticate** é enviado às requisições sub-sequentes.  
Quando o Pré Autenticar é marcado como falso, uma requisição é feita ao Método do Web Service sem se atentar inicialmente à autenticação do usuário. Se o Web Service permitir acesso anônimo, então o Método do Web Service é executado. Se o acesso anônimo não foi permitido, é enviado como resposta à maquina cliente o código de retorno HTTP 401 . Em resposta, a class **WebClientProtocol** retorna as credenciais ao Servidor Web. Se a máquina cliente está autenticada e subsequentemente autorizada a acessar o Web Service, o Método do Web Service é executado; se não à máquina cliente é negado o acesso.

Importante

É importante frisar que, caso o contrato WSDL possua qualquer serviço que possua hífen em seu nome ( - ), este será substituído por travessão/underline ( \_ ) em tempo de execução. Faça as validações, tenha atenção e se possível, evite nomes de serviços com hífen, para evitar inconsistências.

Vamos Configurar o Web Service:

**1)** Clique com o botão direito na atividade.

**2)** Defina o descritor do Web Service (**WSDL**) que será utilizado e clique em **OK**.

Será apresentado o **XML** do descritor à sua esquerda, e será apresentado os métodos disponíveis à sua direita.

**3)**Escolha o método que será utilizado.

**4)** Após escolher o método à ser utilizado na Fórmula Visual, as propriedades Method e Wsdl já estarão preenchidas, você deverá preencher então o usuário e senha (caso houver necessidade) e o Pré Autenticar (também se houver necessidade)

**5)** Após o preenchimento do Grupo **Diversos**, deve-se preencher o Grupo **Parâmetros**.

A quantidade de parâmetros do Grupo **Parâmetros** é variável, no caso demonstrado, são dois, mas pode ser qualquer valor maior ou igual a 0. (x >= 0)

| N° | Nome do Parâmetro | Descrição do Parâmetro | Obrigatoriedade |
| --- | --- | --- | --- |
| 1 | CityName | Nome da Cidade à qual será retornado à informação de Clima. | GreenObrigatório |
| 2 | CountryName | Nome do Páis à qual será retornado à informação de Clima. | GreenObrigatório |

**6)** Após o preenchimento do Grupo **Parâmetros**deve-se preencher o Grupo **Retorno**

**7)**Clique no **Ícone Amarelo** ao lado da Propriedade **Retorno**, ou no **botão [...]** que aparece ao lado da mesma propriedade, a tela abaixo irá aparecer.

**8)** Clique na Aba **Associar a um novo membro** e defina uma nova **Propriedade** com o nome que desejar.

**9)** Após criar a nova propriedade vinculada ao Retorno, verifique se o nome dela aparece na árvore de Membros.

**10)** Caso a Propriedade (**rmsWebServiceActivity1\_Retorno1** ou outro nome definido pelo usuário) tenha sido criada, ela será vinculada à Propriedade **Retorno** da Atividade.

Como foi dito antes, esse retorno pode ser utilizado por várias atividades, um exemplo fácil é vinculá-lo a uma atividade de Gerar Exceção.

Após acrescentar a atividade de Gerar Exceção, temos que configurá-la, preenchendo a Propriedade **Mensagem de Erro**.

Devemos vincular a Propriedade (**rmsWebServiceActivity1\_Retorno1** ou outro nome definido pelo usuário) à Propriedade **Mensagem de Erro**da atividade Gerar Exceção.

Depois de preenchido a Propriedade **Mensagem de Erro,** verificar se o valor vinculado está correto.

Após isso, salvar e executar a fórmula, que uma exceção será gerada com o valor de retorno do Método do Web Service escolhido.

Informação

Ao utilizar essa atividade com HTTPS é necessário que o certificado ofereça uma conexão segura.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.17 ou Superior

false

**Processo:** Atividade "Executar Web Service" da Fórmula Visual

falsefalse

**Status:** **Finalizado**

false

**Data:**

false

**Autores:**

false
