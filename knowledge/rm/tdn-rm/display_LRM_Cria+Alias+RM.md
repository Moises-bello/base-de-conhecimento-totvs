---
content_hash: 26f9c010e4e89a51cfacf3821dafb09af505aec14aa11bfcc0875f4e123dd300
fetched_at: '2026-06-29T00:11:39.056563+00:00'
page_id: '787858095'
product: rm
source: tdn-rm
title: Cria Alias RM
type: documentation
url: https://tdn.totvs.com/display/LRM/Cria+Alias+RM
version: 24
---

## O que é?

É uma atividade que facilita a criação de um Alias dentro do ambiente RM, facilitando o compartilhamento de informações da conexão entre as atividades ao longo do projeto através do recurso de Alias que são apelidos personalizados para a conexão.

## Para que serve?

Essa atividade é útil para criar um Alias que atua como um identificador de conexão para diversos bancos de dados, simplificando o gerenciamento de múltiplos ambientes e conexões dentro de um projeto.

## Exemplo de Uso

Cria alias RMParâmetros da atividade

## Parâmetros de Atividade

**Cria alias RM:** É considerada uma **atividade fixa** dentro do TOTVS Automação de Testes. Atividades fixas não são passíveis de serem cadastradas, podemos apenas usá-las dentro de um projeto de teste, isso facilita a utilização dessa atividade pois não hà um versionamento ligado ao projeto de teste e a utilização dessa atividade é sobre demanda.

**Pré-requisito**: Para realizar a passagem de parâmetros para uma atividade 'Cria alias RM' é necessário já ter inserido esta atividade em um Projeto de Teste.

Schema JSONjsRDarkMetadados JSON - Cria alias RMtrueJSON de exemplojsRDarkExemplo de JSON a ser passado por parâmetrotrueRecursos

Para acessar os recursos dessa atividade acesse a documentação a seguir: [Recursos - Cria Alias RM](https://tdn.totvs.com/display/LRM/Recursos+-+Cria+alias+RM) 

Exemplo prático

## Exemplo Prático

Imagine que você faz parte da equipe de Fiscal e precisa realizar um teste para o **cadastro de uma nova moeda no sistema**. Para garantir que o processo foi realizado corretamente, é necessário ter uma base restaurada ou restaurar no projeto de teste, **criar um alias RM** e verificar se o registro da nova moeda foi inserido na base restaurada após o teste automatizado, isso garantirá que a base, o alias foram criados e os recursos foram compartilhados com sucesso. 

Criação da atividade

---

# Saiba mais

A atividade pode aceitar um recurso de conexão de banco de dados existente, caso contrário, será gerado um nome aleatório para o Alias. Ela valida a criação do Alias, garantindo que, caso ocorra algum erro (como a falta de diretórios do ambiente ou parâmetros inválidos), a atividade será marcada como falha.

Você pode utilizar esta atividade em conjunto com recursos de conexão a banco, como aqueles fornecidos por atividades de restauração de banco de dados, para evitar repetição de parâmetros.

É importante garantir que os parâmetros obrigatórios sejam sempre fornecidos corretamente. Caso contrário, a atividade não será executada com sucesso.

Ao criar o Alias, monitore o status da atividade. Se houver erros, como a não existência de diretórios ou problemas de conexão, a atividade será marcada como erro e o fluxo será interrompido.

# FAQ

**P: O que acontece se o Alias não puder ser criado?**  
**R:** Caso o Alias não possa ser criado, por exemplo, por falta de diretórios ou problemas de conexão, a atividade será marcada como erro e o fluxo de execução será interrompido.

**P: Posso usar recursos de conexão de banco de dados ao invés de definir todos os parâmetros manualmente?**  
**R:** Sim, você pode usar um recurso de conexão de banco ao invés de definir manualmente os parâmetros de banco de dados. Isso é geralmente recomendado para maior facilidade de manutenção e flexibilidade.
