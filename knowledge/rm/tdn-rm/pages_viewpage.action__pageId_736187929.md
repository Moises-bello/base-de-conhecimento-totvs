---
content_hash: 8795b7faa210dd46f1ebe25827c2e0310f246af6989c40b8d1d52413943580fe
fetched_at: '2026-06-29T00:11:29.348111+00:00'
page_id: '736187929'
product: rm
source: tdn-rm
title: Casos de Teste.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=736187929
version: 38
---

# O que são?

É uma descrição detalhada de uma funcionalidade ou cenário específico que deve ser testado, com o objetivo de organizar e planejar seus Projetos de Teste automatizados antes mesmo de cria-los.

# Para que servem?

Servem como base principal para a validação de sistemas, pois descrevem o comportamento que o produto deve ter sob diversos fatores, como:

* + Definir critérios claros de sucesso e falha para cada funcionalidade testada.
  + Identificar e detalhar as condições prévias necessárias para a execução dos testes.
  + Fornecer uma estrutura clara de passos a serem seguidos durante os testes.
  + Estabelecer os resultados esperados para cada teste.

# Exemplo de Uso

Como cadastrarComo Cadastrar 1. Navegação para o cadastro

 1. Navegue no menu do TOTVS Automação de Testes e clique em **Casos de Teste.**

 2. Na tabela que será mostrada, clique no botão verde em destaque.

2. Preenchimento dos CamposInformações

a. **Nome**: Informe o nome do caso de teste. Adote um padrão nomenclatura que propicie uma rápida e fácil identificação de seu objetivo. O título do caso de teste deverá ser sucinto, simples e autoexplicativo com informações para que o Analista de Teste saiba a validação a qual o teste se propõe. **Exemplos:**

* + Fazer upload de arquivo
  + Realizar cadastro de usuário com perfil administrador

b**. Descrição**: Aqui você poderá detalhar mais seu caso de teste, fornecendo uma visão geral do teste que será realizado. **Exemplos:**

* + Verificar se realiza o upload do arquivo com as extensões permitidas
  + Verificar se o cadastro é efetivado após preencher as informações corretamente

c. **Criticidade:** Baixa, Média ou Alta de acordo com suas necessidades.

* + - * Baixa: Impacto mínimo, não afeta a funcionalidade principal do sistema.
      * Média: Impacto moderado, pode afetar a usabilidade ou segurança, mas não interrompe totalmente as operações.
      * Alta: Impacto significativo, pode causar perda de dados, comprometer a segurança ou interromper o serviço.

Permissões

Aqui você poderá determinar qual ou quais grupos terão acesso ao seu Caso de Teste e ainda se poderá alterá-lo ou não. (Saiba mais sobre o que são os [Grupos](https://tdn.totvs.com/display/LRM/6+-+Grupos) no **TOTVS Automação de Testes** ). Este campo será desabilitado ao associar um projeto de teste no registro. Após feita esta associação seu Caso de teste passará a ter as mesmas permissões do Projeto de Testes nele associado.

Projeto de Teste

Após concluir a criação do seu Caso de Teste e construir o respectivo Projeto de Testes, faça a associação entre eles. Você também pode associar um Projeto de Teste já existente. A associação é de 1 para 1 e, se necessário, pode ser desfeita posteriormente.

* + Se for associado um Projeto de Teste a um Caso de Teste:
    - * Se existirem permissões por grupo de usuário elas serão sobrepostas pelas permissões do Projeto de Teste.
      * Se não existirem permissões serão gravadas as do Caso de Teste.
  + Se for retirada a associação de Projeto de Teste de um Caso de Teste:
    - * Se já existiu alguma permissão por grupo de usuário elas serão restauradas.
      * Se não existirem o usuário será obrigado a informar um outro projeto ou novas permissões por grupo de usuário.

Pré-condições

São condições necessárias para que o caso de teste consiga ser executado, para evitar que não tenha alguma informação necessária.

Relate aqui tudo que é necessário para uma correta execução de seu Caso de Teste e posterior Projeto de Teste.

**Exemplos:**

* + - * O sistema deve estar conectado a um banco de dados de teste
      * Usuário cadastrado e autenticado no sistema
      * Usuário com perfil Administrador

Passos

Detalhe cada ação necessária para a execução bem-sucedida do seu **Caso de Teste** ou Projeto de Teste. Inclua todos os passos detalhadamente, excluindo ou reordenando-os conforme necessário.

**Exemplos:**

* + Acessar a tela Negociação > Boleta
  + Clique no botão “Entrar”
  + Insira o campo código e descrição do cadastro
  + Clique no botão salvar

Resultados

Descrever o comportamento esperado do sistema após executar os passos detalhados.

Para informar os resultados do Caso de Teste:

* Utilize verbos no presente (valida, apresenta, recupera, retorna).
* Evite frases como “O sistema deve retornar a mensagem”; prefira “O sistema retorna a mensagem” para deixar claro o resultado esperado.

**Exemplos**:

* + A ordem é enviada e executada com o preço informado.
  + O cadastro é salvo no banco de dados.

Ícones e Filtros da TabelaColuna Ações

### Edição

O botão de editar permite que os usuários autorizados modifiquem as configurações de um ambiente específico.

### Projeto de Teste

Se o caso de teste estiver vinculado a um projeto de teste, é possível visualizar o projeto utilizando este botão.

Seção Passos

## Passos:

### **Incluir:**

O botão de Incluir permite adicionar novos passos ao seu Caso de Teste. Ao clicar nele, você pode detalhar cada ação necessária para a execução do teste, garantindo que todos os procedimentos sejam seguidos corretamente.

### **Arrastar:**

O ícone de Arrastar permite que você reordene os passos do Caso de Teste, movendo-os para a posição desejada. Isso facilita a organização e a estruturação das etapas, garantindo que sejam executadas na sequência correta.

### **Remover:**

O botão Remover permite excluir passos previamente adicionados ao seu Caso de Teste. Utilizando este recurso, você pode manter a lista de passos atualizada e livre de informações desnecessárias ou incorretas.

Filtros da Tabela 

No menu inicial do Caso de Testes, temos as seguintes opções de filtros:

* **Nome do Caso de Teste**: Filtre pelos nomes específicos dos casos de teste para encontrar rapidamente um caso particular que você deseja visualizar ou editar.
* **Projeto de Teste**: Filtre pelos diferentes projetos de teste para organizar e visualizar os casos de teste associados a um projeto específico, facilitando a gestão de múltiplos projetos.
* **Versões dos Projetos de Teste**: Filtre pelas diversas versões dos projetos de teste, permitindo a visualização e comparação de casos de teste entre diferentes versões do mesmo projeto. Isso é útil para acompanhar mudanças e atualizações ao longo do tempo.
* **Grupos**: Filtre pelos grupos que associam ao seu caso de teste.

Exemplo prático

Imagine que você é o novo analista responsável pelo produto RM. É crucial garantir que o sistema permita que um usuário faça login com credenciais válidas ao acessar o produto pela primeira vez. Aplicando isso ao caso de teste, temos:

**Nome do caso de Teste:** Validação do Login com Credenciais Válidas.

**Descrição(Objetivo):** Garantir que o sistema permita que um usuário faça login com credenciais válidas

**Pré-condição:** Possuir usuário com credenciais Válidas.

**Passos:**

a. Inserir Usuário Válido no campo: "insira seu usuário ou E-mail".

b. Inserir Senha Válida no campo: "insira sua senha".

c. Clique em: "Entrar".

**Resultados esperados:** Após concluir o login, exibe uma mensagem de sucesso: "Você entrou como Exemplo". 

---

# Saiba mais

Utilize um padrão de nomenclatura que facilite a rápida e fácil identificação do objetivo do teste.

Os Casos de Teste não são versionados.

O registro de Caso de Teste só poderá ser salvo se todos os campos obrigatórios estiverem preenchidos. Para facilitar a visualização dos campos não preenchidos será acrescentado um sinal de exclamação na seção que contem algum campo obrigatório vazio. Ela só desaparecera após preencher os campos obrigatórios.

Se o caso de teste estiver associado a um projeto de teste, um botão para edição será exibido. Se o projeto de teste tiver várias versões, será necessário escolher qual versão editar.

# FAQ

**P: Como posso garantir que meu Caso de Teste seja eficaz?**  
R: Para garantir a eficácia do caso de teste, certifique-se de que ele cubra todos os cenários possíveis, incluindo casos de uso críticos, exceções e integrações com outros sistemas.

**P:****Por que devo usar um padrão de nomenclatura para o Nome do Caso de Teste?**

R: Um padrão de nomenclatura facilita a identificação rápida e clara do objetivo do caso de teste, tornando a organização e a busca mais eficientes.

**P: O que acontece com as Permissões quando um Projeto de Teste é associado?**  
R: Se um projeto de teste for associado, as permissões do projeto sobreporão as do caso de teste. Caso a associação seja desfeita, as permissões originais do caso de teste serão restauradas.

**P: Quais são os desafios comuns ao criar e manter Casos de Teste?**  
R: Alguns desafios comuns incluem manter os casos de teste atualizados conforme o software evolui, garantir cobertura completa de testes e ajustar casos de teste conforme novos requisitos são adicionados ou alterados.
