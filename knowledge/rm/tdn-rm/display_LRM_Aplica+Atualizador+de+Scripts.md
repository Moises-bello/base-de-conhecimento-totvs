---
content_hash: 086308d1d10f6a674c0592478eadcbe41ce1d327886f229695f19a14c4e72637
fetched_at: '2026-06-29T00:11:50.261085+00:00'
page_id: '839942702'
product: rm
source: tdn-rm
title: Aplica Atualizador de Scripts
type: documentation
url: https://tdn.totvs.com/display/LRM/Aplica+Atualizador+de+Scripts
version: 6
---

## O que é?

Esta atividade é responsável por verificar se existem scripts pendentes de atualização em uma base de dados específica. Caso scripts pendentes sejam identificados, a base será automaticamente atualizada.

## Para que serve?

Serve para garantir que as bases de dados estejam sempre atualizadas com os scripts mais recentes, evitando falhas ou inconsistências no sistema que possam ocorrer devido a scripts pendentes.

## Exemplo de Uso

Cria alias RMParâmetros da atividade

**Aplica Atualizador Scripts** é considerada uma **Atividade Fixa** dentro do TOTVS Automação de Testes. Atividades fixas não são passíveis de serem cadastradas, podemos apenas usa-las dentro de um projeto de teste, isso facilita a utilização dessa atividade pois não hà um versionamento ligado ao projeto de teste e a criação dessa atividade é sobre demanda.

**Pré-requisitos:**

Para que esta atividade funcione corretamente, os seguintes pré-requisitos devem ser atendidos:

* **Alias Configurado**:  
  Um **Alias** deve ser configurado previamente, seja através do parâmetro "Alias" no JSON ou utilizando um **Recurso de Alias** criado pela atividade "[Cria Alias RM](https://tdn.totvs.com/display/LRM/Cria+Alias+RM?draft=true#CriaaliasRM--729033878)".
* **Acesso ao Banco de Dados**:  
  As credenciais de login (usuário e senha) devem ter permissão para acessar o banco de dados que será atualizado.
* **Ambiente de Execução Disponível**:  
  O host onde a base de dados está localizada deve estar acessível na rede e rodando na **porta** correta especificada (padrão: 8051).
* **Conectividade de Rede**:  
  O DNS ou IP do host onde está a base de dados deve ser resolvido corretamente, permitindo a comunicação entre o servidor da aplicação e o banco de dados.
* **Permissões de Atualização**:  
  O usuário fornecido para o banco de dados deve ter permissões suficientes para aplicar atualizações de scripts na base.
* **Scripts Pendentes**:  
  A atividade assume que existem scripts pendentes de serem aplicados na base de dados. A ausência de scripts pode resultar em uma execução sem alterações.

Schema JSONjsRDarkMetadados JSON - Cria alias RMtrue

O parâmetro "Alias" pode ser substituídos por um "Recurso de Alias", é oferecido pela atividade "Cria Alias RM".

Validações

Validações:

* **Verificar se o servidor está ativo**:

  + Confirma que o servidor está a funcionar corretamente na **porta indicada**.
* **Verificar o acesso com utilizador e senha**:

  + Garante que as **credenciais** (nome de utilizador e senha) fornecidas estão **corretas** e permitem acesso ao sistema.
* **Verificar se os Scripts de atualização da base de dados funcionaram**:

  + Confirma que os S**c**ripts foram executados sem erros, garantindo que as alterações na base de dados foram aplicadas corretamente.
JSON de exemplojsRDarkExemplo de JSON a ser passado por parâmetrotrueRecursos

Para acessar os recursos dessa atividade acesse a documentação a seguir: [Recursos - Aplica atualizador de Scripts](https://tdn.totvs.com/display/LRM/Recursos+-+Aplica+atualizador+de+Scripts)

Exemplo prático

Imagine que um analista do sistema RM precise verificar, de forma periódica, se existem **Scripts Pendentes** para atualização numa base de dados específica, como a "CorporeRM". Para automatizar essa tarefa e garantir que a base esteja sempre Atualizada e Consistente, é utilizada uma atividade de Validação e Atualização, que garante que a base esteja sempre atualizada.

A atividade verifica automaticamente se há **Scripts Pendentes** numa determinada base de dados e, caso existam, Executa a Atualização.

---

# Saiba mais

Se a atividade verificar que não existem scripts pendentes na base de dados, ela finalizará sem fazer alterações. Isso garante que a base não será alterada desnecessariamente.

Se houver falhas durante a atualização dos scripts, como erros de sintaxe ou conflitos, a atividade registrará esses erros nos logs de execução. É importante revisar esses logs para identificar a causa e corrigir eventuais problemas.

# FAQ

**P: O que acontece se o Alias não for informado?**

R: Se o parâmetro "Alias" não for fornecido, a atividade tentará utilizar um **Recurso de Alias**, que deve ser previamente configurado por outra atividade, como a "Cria Alias RM". Caso nem o parâmetro nem o recurso estejam disponíveis, a atividade não conseguirá identificar a base de dados correta e falhará.

**P: O que acontece se o host ou a porta estiverem incorretos?**

R**:** Se o endereço DNS do host ou a porta forem informados incorretamente, a atividade não conseguirá se conectar à base de dados e falhará. Certifique-se de que as informações de "HostDns" e "HostPort" estão corretas.
