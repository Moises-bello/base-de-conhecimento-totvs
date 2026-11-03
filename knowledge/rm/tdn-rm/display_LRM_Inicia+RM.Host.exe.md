---
content_hash: 949f29a2756f9c22c6bf4bb8927a1dbcfb8321712e0e4883fa67eaa79fadf478
fetched_at: '2026-06-29T00:11:39.060793+00:00'
page_id: '787858176'
product: rm
source: tdn-rm
title: Inicia RM.Host.exe
type: documentation
url: https://tdn.totvs.com/display/LRM/Inicia+RM.Host.exe
version: 33
---

## O que é?

Essa atividade executa o Host do RM, realizando um teste de conexão com os alias cadastrados no arquivo `alias.dat`. A atividade também pode receber um Recurso de Alias, se necessário.

## Para que serve?

A atividade serve para iniciar o serviço do RM Host, verificando a conectividade com os aliases configurados e garantindo que o ambiente esteja corretamente preparado para rodar os serviços. Permite passar configurações, argumentos de processo e definir qual base será utilizada através do parâmetro "Alias".

## Exemplo de Uso

Cria alias RMParâmetros da atividade

**Inicia RM.Host.exe** é considerada uma **atividade fixa** dentro do TOTVS Automação de testes. Atividades fixas não são passíveis de serem cadastradas, podemos apenas usa-las dentro de um projeto de teste, isso facilita a utilização dessa atividade pois não hà um versionamento ligado ao projeto de teste e a criação dessa atividade é sobre demanda.

**Pré-requisito:** Para realizar a passagem de parâmetros para uma atividade 'Inicia RM.Host.exe' é necessário já ter inserido esta atividade a um Projeto de Teste.

Schema JSONjsRDarkMetadados JSON - Cria alias RMtrueJSON de exemplojsRDarkExemplo de JSON a ser passado por parâmetrotrueRecursos

Para acessar os recursos dessa atividade acesse a documentação a seguir: [Recursos - Inicia RM.host.exe](https://tdn.totvs.com/display/LRM/Recursos+-+Inicia+RM.host.exe)

Exemplo prático

Imagine que você faz parte da equipe de Fiscal e precisa realizar um teste para o **cadastro de uma nova moeda no sistema**.

Para garantir que o processo foi realizado corretamente, é necessário ter um alias para que seja passado para o Inicia RM.Host.exe via parâmetro ou via recurso e verificar se o registro da nova moeda foi inserido na base restaurada após o teste automatizado, isso garantirá que a base foi restaurada, o alias foi criado, o host inicializado e os recursos foram compartilhados com sucesso. 

Criação da atividade

---

# Saiba mais

Certifique-se de que o arquivo de configuração do **RM.Host** esteja no diretório correto do ambiente, para evitar falhas na inicialização do Host.

A verificação de **Alias** é automática, mas você pode fornecer um Alias específico como parâmetro se desejar controlar manualmente qual banco de dados será usado pelo Host.

Caso o **Timeout** seja atingido e o Host ainda não esteja pronto, a atividade será interrompida com erro. Ajuste o valor de timeout conforme a complexidade da inicialização.

# FAQ

**P: O que acontece se o arquivo de configuração do RM.Host não for encontrado?**  
**R:** A atividade será marcada como erro e interrompida se o arquivo de configuração do RM.Host não for localizado no diretório especificado.

**P: Posso iniciar o Host do RM sem um recurso de Alias?**  
**R:** Sim, mas você deve fornecer o Alias como parâmetro diretamente na atividade. Caso contrário, a atividade falhará se não houver um recurso de Alias disponível no projeto.
