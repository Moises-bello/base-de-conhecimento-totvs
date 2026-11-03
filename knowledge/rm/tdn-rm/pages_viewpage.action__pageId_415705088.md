---
content_hash: db1de4a65ed693d2053f940d70f70e42995f82212206b52dfe6bed2b58696fc4
fetched_at: '2026-06-29T00:09:11.719595+00:00'
page_id: '415705088'
product: rm
source: tdn-rm
title: Como acertar a Base de IRRF Férias que foram enviadas em duplicidade no eSocial?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=415705088
version: 68
---

Para tratar a  situação relacionada a duplicidade na base de IRRF Férias, foi implementado o código de cálculo **381-IRRF Férias Envelope.**

Maiores informações: <http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.BaseIrrfFeriasEnvelope.aspx>

**O usuário deverá seguir os procedimentos abaixo****:**

Erros e AçõesUsuários que não aplicaram a saída de contorno:

**Para os clientes que não aplicaram a saída de contorno, é necessário executar os procedimentos abaixo:**

* + Executar um recálculo na base, o recálculo poderá ser apenas para um funcionário. Com isso o sistema irá criar o novo código de cálculo na tabela dinâmica (**381-Base de IRRF Férias Envelope).**
  + Cadastrar um evento com código de cálculo **381-Base de IRRF Férias Envelope.** Este deverá ser do tipo "Base de Cálculo", sem incidência e com o código da Natureza da Rubrica (eSocial) igual a 9939-Outros valores tributáveis. Essa é a rubrica indicada no sistema para os eventos do tipo base de calculo que são considerados como valores tributáveis para o eSocial.

Ao cadastrar o evento será gerado automaticamente o gatilho S-1010 -Tabela de Rubricas. O usuário deverá acessar o menu eSocial | Fila de Eventos e editar esse evento alterando o campo "Competência" preenchendo com a data de obrigatoriedade do eventos de tabela:

+ Executar o processo para Gerar o XML do novo evento (S-1010) e enviar até o governo .
+ Enviar os eventos periódicos S-1200 - Remuneração de trabalhador vinculado ao Regime Geral de Previd. Social  e  S-1210 - Pagamentos de Rendimentos do Trabalho.
+ Verificar os valores dos rendimentos tributáveis de férias no ambiente do governo.
+ **Importante:**

  - Caso o usuário não tenha criado um evento com o código de cálculo **381-IRRF Férias Envelope**, ao realizar o processo de lançamento das férias através do processo ou diretamente no cadastro de férias será apresentada a mensagem de erro abaixo impedindo o processo:

  Após a criação do evento, ao lançar as férias o evento de código de cálculo 381-Base de IRRF Férias será visualizado no envelope do funcionário, conforme tela a seguir:

  ****Atenção!****

  Para os funcionários que já estão com férias lançadas antes da criação do evento com código de cálculo **381-IRRF Férias Envelope** deverá inserir manualmente o evento na movimentação dos funcionários em seguida realizar recálculo. Seguir os processos normalmente gerando o XML para os eventos S-1200 - Remuneração de trabalhador vinculado ao Regime Geral de Previd. Social  e  S-1210 - Pagamentos de Rendimentos do Trabalho e enviar até o governo.
Usuários que aplicaram a saída de contorno:

**Para os clientes que entraram em contato com o atendimento alegando o incidente de "Duplicidade na base IRRF Férias" e que receberam orientação para retificar os eventos da folha (saída de contorno), favor executar os procedimentos abaixo:**

* + Executar um recálculo na base, o recálculo poderá ser apenas para um funcionário. Com isso o sistema irá criar o novo código de cálculo na tabela dinâmica (**381-IRRF Férias Envelope).**
  + Cadastrar um evento com código de cálculo **381-IRRF Férias Envelope.** Este deverá ser do tipo "Base de Cálculo", sem incidência e com o código da Natureza da Rubrica (eSocial) igual a 9939-Outros valores tributáveis. Essa é a rubrica indicada no sistema para os eventos do tipo base de calculo que são considerados como valores tributáveis para o eSocial.

Ao cadastrar o evento será gerado automaticamente o gatilho S-1010 -Tabela de Rubricas. O usuário deverá acessar o menu eSocial | Fila de Eventos e editar esse evento alterando o campo "Competência" preenchendo com a data de obrigatoriedade do eventos de tabela:

* + Executar o processo para Gerar o XML do novo evento (S-1010) e enviar o registro para o governo .
  + Acessar o menu eSocial | Fila de Eventos, e inserir manualmente as rubricas dos eventos de férias lançadas na envelope de pagamento que incidem em IRRF Férias e que foram retificados como saída de contorno anteriormente. Estes eventos devem ser incluídos com tipo de operação "Alteração".
  + Gere o XML para os eventos e envia até o governo.

**Importante:**

* Caso o usuário não tenha criado um evento com o código de cálculo **381-IRRF Férias Envelope**, ao realizar o processo de lançamento das férias através do processo ou diretamente no cadastro de férias será apresentada a mensagem de erro abaixo impedindo o processo:

Após a criação do evento, ao lançar as férias o evento de código de cálculo 381-Base de IRRF Férias será visualizado no envelope do funcionário, conforme tela a seguir:

****Atenção!****

Para os funcionários que já estão com férias lançadas antes da criação do evento com código de cálculo **381-IRRF Férias Envelope** deverá inserir manualmente o evento na movimentação dos funcionários em seguida realizar recálculo. Seguir os processos normalmente gerando o XML para os eventos S-1200 - Remuneração de trabalhador vinculado ao Regime Geral de Previd. Social  e  S-1210 - Pagamentos de Rendimentos do Trabalho e enviar até o governo.

falsefalse

**Produto:** Folha de Pagamento

false

**Rotina:** eSocial

false

**Versões:**

|  |
| --- |
| 12.1.22 |
| 12.1.21 |
| 12.1.20 |
| 12.1.19 |

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autor:**
