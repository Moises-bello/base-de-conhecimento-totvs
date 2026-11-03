---
content_hash: 94273aa709231a36a92bab0a78dc090ad3878fecc3841ffebc1acac255588ee8
fetched_at: '2026-06-29T00:11:21.135759+00:00'
page_id: '687766316'
product: rm
source: tdn-rm
title: 2.6.2 - Http
type: documentation
url: https://tdn.totvs.com/display/LRM/2.6.2+-+Http
version: 35
---

## O que é?

Automação de testes HTTP REST envolve o uso do protocolo HTTP para interagir com servidores ou APIs (Interfaces de Programação de Aplicações) de maneira automatizada. Nesse contexto, o TOTVS Automação de Testes atua como um cliente, enviando requisições para sistemas externos, como o RM, para realizar operações específicas. Essas operações podem incluir a consulta, criação, atualização ou exclusão de dados em sistemas externos, sem a necessidade de intervenção manual.

## Para que serve?

Serve para realizar operações automatizadas, como a inclusão de novas entidades (como moedas) no sistema RM via chamadas de API. Isso é especialmente útil para integração de sistemas, automação de tarefas repetitivas e manutenção de registros atualizados em bases de dados corporativos.

## Links Úteis

1. [O que é um Protocolo Http;](https://www.alura.com.br/artigos/http?srsltid=AfmBOoqRZxPiAF-dqmZabQEhU6Blna01c18E24WquLIPR20ItRPs5EB-)
2. [Documentação Postman.](https://www.postman.com/)

# Exemplo de Uso

Como cadastrarComo Cadastrar 1. Navegação para o cadastro 

1. Navegue no menu do TOTVS Automação de Testes e clique em: **Atividades →** **Serviços** →**Http**
2. Na tabela que será mostrada, clique no botão verde em destaque para criar **Atividade de Http.**

2. Link para Definir cabeçalho (Nome e nível de acesso)

[Clique aqui para obter as informações do cabeçalho](https://tdn.totvs.com/pages/viewpage.action?pageId=859591806)

3. Preenchimento dos CamposVersão

Especifica a versão da atividade em questão. O objetivo de versionar uma atividade é para quando necessitamos ter mais de uma atividade em versões diferentes. Isso irá nos auxiliar a ter um histórico de atualizações e assegurar que as mudanças feitas sejam rastreáveis e reversíveis, se necessário.

Se for necessário utilizar mais de uma versão do RM no seu ambiente, é recomendado que a versão da atividade seja compatível com o sistema RM em uso. Caso contrário, pode-se optar por uma versão padrão de sua preferência.

*Exemplo utilizando a versão do RM*

*Exemplo utilizando a versão padrão*

Descrição de Atividade 

Fornece uma descrição detalhada da atividade, explicando seu propósito e operações, facilitando a compreensão e manutenção futura.

Condição de Erro 

**Logar. o Erro:** Quando uma atividade HTTP encontra um erro durante a execução, essa opção registra o erro nos logs do sistema. Isso permite que os administradores ou desenvolvedores revisem os detalhes do erro mais tarde, incluindo a mensagem de erro, a causa e outros detalhes relevantes da requisição falhada.

* + - **Exemplo:** Se uma requisição HTTP falhar com um erro 404, o TOTVS Automação de Testes deverá registrar essas informações nos logs para análise posterior. A execução do processo não será finalizada

**Gerar Erro de Execução:** Esta opção interrompe a execução da atividade e retorna um erro, que pode fazer com que todo o fluxo de trabalho ou processo seja interrompido. Um erro de execução indica que a operação não pode continuar devido a uma falha crítica.

* + - **Exemplo:** Se uma requisição HTTP falhar com um erro 404, o TOTVS Automação de Testes deverá registrar essas informações nos logs para análise posterior e a execução do processo será finalizada.

**Gerar Alerta e Continuar:** Quando ocorre um erro, em vez de interromper a execução, esta opção gera um alerta (por exemplo, uma notificação ao administrador) mas permite que o processo continue. Isso é útil em situações onde o erro não é crítico e o processo pode prosseguir sem causar maiores problemas.

* + - **Exemplo:** Se uma requisição HTTP falhar com um erro 404,a ferramenta  deverá registrar um alerta sobre a execução da atividade e continuar processando outras operações relacionadas sem interrupção.

Requisições Interpretando os Ícones

## Adicionar Requisição

Clique neste ícone para adicionar uma requisição Http.

## Deletar todas as Requisições

Clique nesse ícone para deletar todas as requisições Http presentes na atividade.

Cada requisição possui este ícone, permitindo que você delete aquela requisição específica.

Preenchimento dos camposAutorização

**Autorização**: É responsável pela autenticação da sua requisição. Você pode escolher entre o tipo Basic ou optar por não utilizar autenticação.

Headers

**Headers**: São pares de chave-valor enviados com a requisição HTTP para fornecer informações adicionais sobre a requisição ou sobre o cliente que está enviando a requisição.

Body

 É a parte da requisição HTTP onde os dados são enviados para o servidor, especialmente em métodos como POST, PUT, ou PATCH. Esses dados podem estar nos seguintes formatos:

* **JSON**
* **XML**
* **Text/Plain**

Para utilizá-lo, selecione um dos tipos de media types listados acima e adicione o conteúdo ao corpo da requisição:

Queries 

São parâmetros de consulta que são adicionados ao final da URL na requisição HTTP. Eles permitem enviar informações adicionais para o servidor, sem modificar o conteúdo principal do body.

* Na Ferramenta, o campo *Chave e Valor* nas **Queries** é utilizado para adicionar parâmetros de consulta à URL da requisição HTTP. Esses parâmetros são usados para passar informações adicionais ao servidor, permitindo que você filtre, refine ou modifique os resultados retornados pela API.

Exemplo:

Cookies 

Cookies são pequenos pedaços de dados que o servidor armazena no navegador do cliente. Eles são enviados em cada requisição subsequente ao mesmo servidor e são utilizados para manter sessões, lembrar preferências do usuário, ou rastrear informações de autenticação.

Na Ferramenta, o campo *Chave e Valor* nos **Cookies** é utilizado para configurar dados que serão enviados junto com a requisição HTTP ao servidor. Os cookies são pequenas informações armazenadas pelo navegador ou cliente que podem ser enviadas automaticamente com cada requisição subsequente ao mesmo servidor, permitindo que o servidor mantenha o estado entre requisições.

Teste a Requisição

É  uma funcionalidade no TOTVS Automação de Testes que permite executar uma simulação da requisição HTTP que você configurou para verificar se está funcionando corretamente antes de integrá-la a um fluxo de trabalho maior.

Para que a atividade seja realizada é obrigatório que adicione o seu servidor.

O Agent deve estar em execução no servidor para que possa funcionar.

Após todos os campos obrigatórios preenchidos clique no botão em destaque para executar o teste de requisição.

Variáveis de ambiente

As Variáveis de Ambiente são utilizadas para configurar e personalizar o comportamento da Atividade. Elas permitem definir valores específicos ou dinâmicos que podem ser usados durante a execução dos testes, assegurando que o teste execute conforme o ambiente em que o mesmo é executado. As Variáveis de Ambiente são cadastradas no cadastro de Ambiente onde informamos os valores fixos ou de forma dinâmica no cadastro de Script SQL.

Consulte quais campos permitem o uso das Variáveis de Ambiente nessa Atividade:

[HTTP - Variáveis de Ambiente](https://tdn.totvs.com/pages/viewpage.action?pageId=842289210)

Saiba mais sobre [Ambientes](https://tdn.totvs.com/display/LRM/4+-+Ambientes).

Exemplo prático

## Criação de chamadas Http para Cadastros RM.

Navegação pelo Swagger do RM.

1. Configure os requisitos para esse tipo de atividade. Clique [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=862597885) para mais informações.
2. Carregue o Host do RM como Administrador.
3. No nosso exemplo, vamos utilizar o cadastro de Moedas no sistema RM.
4. Para isso, deve-se consultar o swagger das **API´S** do Host. Isso pode ser feito inserindo a URL a seguir em seu navegador <http://localhost:8051/api/swagger/ui/index#!/> e se essa página carregar, seu Host está corretamente configurado para o uso.
5. Na página do swagger procure pelo item Currency. Clique sobre ele para que seja expandido.
6. Note que existem vários métodos disponíveis. Iremos utilizar o POST, método que fará a inclusão da moeda.
7. Selecione o método POST para que ele seja expandido. Role a tela até chegar na área PARAMETERS no campo em branco de nome RECORD. Vá ao campo imediatamente a direita que tem o nome BODY e clique sobre o schema para que ele seja transferido para o campo RECORD.
8. Preencha todos os campos do cadastro ou somente os obrigatórios conforme imagem abaixo e clique no botão TRY IT OUT.

   js
9. Se tudo correr bem você receberá a resposta abaixo da imagem a seguir.
Configuração no TOTVS Automação de Testes

1. Na tela Método - URL informe o Verbo, a URL (conseguida na tela do swagger no navegador), Timeout, o status esperado no teste e uma descrição para a chamada como na imagem a seguir.
2. Os itens: **Autorização, Headers, Body, Queries e Cookies** só devem ser preenchidos se sua chamada exigir. No caso do nosso exemplo a única exigida é a Autorização na qual devem ser informados os dados do usuário para acesso ao RM.
3. Na guia BODY, escolha o Media Type application/json cole o o json criado na página do swagger.
4. Navegue até a aba **TESTE A REQUISIÇÃO**. Selecione um servidor para execução. Lembrando que neste servidor o Agent do TOTVS Automação de Testes deve estar em execução como Administrador. Clique [aqui](https://tdn.totvs.com/display/LRM/10+-+TestFlow+Agent) para mais informações sobre o agent.
5. Clique no botão play e aguarde o resultado. Devem ser mostrados os dados que foram incluídos. Este é sinal de que sua requisição está correta e pronta para ser inserida em um Projeto ou Agendamento.

---

# Saiba mais

Entender como manipular headers HTTP é essencial, especialmente quando se trata de autenticação.

A atividade HTTP na ferramenta, fornece logs detalhados de cada requisição realizada. Aprender a monitorar esses logs, interpretar mensagens de erro e revisar respostas de APIs é crucial para manter a integridade e o desempenho dos seus processos automatizados.

Antes de implementar uma atividade HTTP em um processo de produção, é fundamental testá-la. O TOTVS Automação de Testes oferece opções para testar requisições diretamente na interface, permitindo verificar se os dados enviados e recebidos estão corretos e se o comportamento esperado foi alcançado. Testar suas atividades ajuda a evitar problemas quando o processo estiver em execução.

# FAQ

**P:** **Posso usar variáveis de ambiente na Atividade?**

R: Sim, você pode usar variáveis dinâmicas no TOTVS Automação de Testes para preencher automaticamente partes da URL, Headers, Body, e outros campos com dados gerados ou capturados por outras atividades no fluxo.

**P: Quais são os erros comuns e como resolvê-los?**

* **Erro 400 (Bad Request):** Verifique se todos os campos obrigatórios estão preenchidos corretamente no Body da requisição.
* **Erro 401 (Unauthorized):** Confirme se as credenciais de autenticação são válidas e foram incluídas corretamente nos Headers.
* **Erro 404 (Not Found):** Certifique-se de que a URL da API está correta e o recurso existe.
* **Erro 500 (Internal Server Error):** Problema diretamente relacionado ao servidor da Api
