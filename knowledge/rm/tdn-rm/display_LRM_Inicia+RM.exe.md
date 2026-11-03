---
content_hash: 7d81a5365b8cba101810392f84abdb3acb38dc52e163acdf5a6897d9b8f6657c
fetched_at: '2026-06-29T00:11:39.067388+00:00'
page_id: '787858202'
product: rm
source: tdn-rm
title: Inicia RM.exe
type: documentation
url: https://tdn.totvs.com/display/LRM/Inicia+RM.exe
version: 9
---

## O que é?

Esta atividade é responsável por executar o **Arquivo RM.exe**, selecionar um **Alias** previamente configurado e realizar o **login** no aplicativo **RM**. O Alias pode ser definido através de **parâmetros JSON** ou pela utilização de um **Recurso de Alias**.

## Para que serve?

Serve para automatizar o processo de inicialização do sistema **RM**, permitindo a configuração de credenciais, seleção de Alias e outros parâmetros necessários para o funcionamento do aplicativo. Esta atividade é útil para automatizar tarefas administrativas e operacionais, garantindo que o sistema RM esteja configurado e autenticado corretamente antes de outras operações.

## Exemplo de Uso

Cria alias RMParâmetros da atividade

**Inicia RM.exe** é considerada uma **atividade fixa** dentro do TOTVS Automação de Testes. Atividades fixas não são passíveis de serem cadastradas, podemos apenas usa-las dentro de um projeto de teste, isso facilita a utilização dessa atividade pois não hà um versionamento ligado ao projeto de teste e a criação dessa atividade é sobre demanda.

**Pré-requisito:** Para realizar a passagem de parâmetros para uma atividade 'Inicia RM.exe' é necessário já ter inserido esta atividade a um Projeto de Teste.

Schema JSON

Aqui está um exemplo de configuração JSON para inicializar a atividade:

jsRDarkMetadados JSON - Cria alias RMtrue

O parâmetro "Alias" pode ser substituídos por um **Recurso de Alias**, é oferecido pela Atividade Cria Alias RM.

JSON de exemplojsRDarkExemplo de JSON a ser passado por parâmetrotrueValidações

A atividade realiza um conjunto de validações antes e durante a execução do sistema **RM.exe** para garantir o funcionamento correto e evitar falhas inesperadas. Abaixo está a descrição detalhada de cada uma dessas validações:

#### 1. **Validação do Caminho do RM.exe**

Antes de iniciar o processo, a atividade verifica se o caminho para o arquivo **RM.exe** está corretamente configurado no sistema. Caso o arquivo não seja encontrado no diretório especificado, a execução será interrompida e uma exceção será lançada.

* **Motivo**: Garantir que o aplicativo **RM** esteja instalado e acessível no sistema antes de tentar iniciar a sua execução.
* **Exceção Lançada**: `"Arquivo RM.exe não encontrado no caminho especificado"`.

#### 2. **Reset da Key no Registro do Windows (Regedit)**

A atividade tenta **resetar uma chave específica no Registro do Windows** necessária para a inicialização correta do RM. Se não for possível realizar essa operação, a execução será interrompida.

* **Motivo**: Certas chaves no Registro podem interferir na execução do RM se estiverem corrompidas ou configuradas incorretamente.
* **Exceção Lançada**: `"Falha ao resetar a chave do Registro no Regedit"`.

#### 3. **Verificação do Parâmetro Alias**

Antes de continuar com o login no sistema RM, a atividade verifica se um **Alias** foi corretamente informado nos parâmetros de entrada ou através de um **Recurso de Alias**.

* **Motivo**: O **Alias** é essencial para identificar o ambiente correto em que o sistema RM será executado.
* **Exceção Lançada**: `"Alias não especificado nos parâmetros ou recurso de Alias ausente"`.

#### 4. **Leitura do Registro do Windows e Timeout**

Durante o processo de inicialização, a atividade realiza a leitura de registros específicos do Windows que são necessários para que o RM funcione corretamente. Caso a leitura falhe ou o aplicativo demore mais do que o tempo definido no parâmetro **Timeout** para iniciar, uma exceção será lançada.

* **Motivo**: Garantir que o RM tenha tempo suficiente para iniciar corretamente, evitando problemas de configuração ou desempenho que possam resultar em falhas críticas.
* **Exceção Lançada**:

  `"Falha ao ler o registro do Windows durante a inicialização"`

  `"Tempo de inicialização excedido (Timeout)"`
Recursos

Para acessar os recursos dessa atividade acesse a documentação a seguir: [Recurso RM.exe](https://tdn.totvs.com.br/display/LRM/Recursos+-+RM.exe)

Exemplo prático

Imagine um **Analista responsável pelo sistema RM**, utilizado para a gestão de processos no setor **imobiliário**. Às vezes, é necessário **reiniciar manualmente** o sistema após uma manutenção ou quando a aplicação deixa de responder. Para simplificar e agilizar esse processo, foi desenvolvida uma **atividade automatizada** que inicializa o **RM.exe de forma imediata**, garantindo que o sistema esteja totalmente operacional antes de outras tarefas críticas dependerem dele.

Criação da atividade

---

# Saiba mais

A atividade exigirá que um **Alias** seja configurado, seja através dos parâmetros JSON ou através de um **Recurso de Alias**. Se nenhum alias for encontrado, a execução será interrompida com uma exceção.

Erros no Registro do Windows geralmente estão relacionados a permissões insuficientes ou chaves corrompidas. Tente executar a aplicação com privilégios de administrador. Em casos recorrentes, crie um script automatizado para resetar as chaves necessárias antes da execução do RM.

# FAQ

**P: O que fazer se o arquivo RM.exe não for encontrado?**R: Certifique-se de que o caminho do RM.exe está corretamente configurado no seu sistema e que o aplicativo está devidamente instalado. Verifique também se o utilizador possui as permissões necessárias para acessar a pasta onde o executável está localizado.

**P: Posso iniciar o RM sem um recurso de Alias?**  
R**:** Não, não é possível iniciar o sistema **RM** sem especificar um **Alias**. O **Alias** é um parâmetro **obrigatório** que identifica qual ambiente o RM deve utilizar (por exemplo, Produção, Homologação, ou Testes). Ele é essencial para que o sistema consiga carregar as configurações corretas e acessar os dados associados a esse ambiente específico.
