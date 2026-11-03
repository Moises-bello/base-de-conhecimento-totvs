---
content_hash: 3ba098ee97f5f73999130cc8548593fbe8d4839362c03229e6095022ebe9a4bb
fetched_at: '2026-06-29T00:10:11.099797+00:00'
page_id: '452719939'
product: rm
source: tdn-rm
title: Preencher Matrícula eSocial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719939
version: 5
---

Neste módulo é possível fazer o preenchimento de forma automática e em massa do campo Matrícula eSocial do Cadastro do Funcionário.   
O processo irá preencher o campo em branco dos Cadastros Funcionários com vínculo empregatício, inclusive os demitidos, exceto os funcionários com Saída por transferência (tipo 5 ou 6).  
   
Para que o processo seja executado com sucesso é necessário que antes o usuário configure a Máscara para Matrícula do Trabalhador em Configurações | Parâmetros | Parametrizador | eSocial | Configurações Gerais.  
   
Para executar o processo de Preenchimento de Matrícula do eSocial, basta acessar eSocial | Processos | Preencher Matrícula eSocial, selecionar a coligada do contexto e clicar em executar.  
   
É possível também executar o processo para Multi-Coligadas.

**Gerar matricula para funcionário sem vinculo com admissão a partir de:**Este campo será apresentado a partir do leiaute S-1.0  e a data preenchida padrão será a data de alteração para o leiaute S-1.0 na base de dados. Poderá ser preenchida com uma data igual ou superior a data padrão. Para funcionários sem vinculo que foram transferidos será considerado a data de transferência.

**Observação**

* Quando a parametrização não estiver configurada no parametrizador, o processo irá retornar para o usuário a coligada que não tem a configuração e não será preenchido o campo Matrícula eSocial do Cadastro do Funcionário.
* O campo Matrícula eSocial será preenchido de acordo com a Máscara para Matrícula do Trabalhador configurada no parametrizador para cada coligada e em sequencial de cada coligada.
* Caso o funcionário já tenha matrícula eSocial cadastrada não será gerada uma nova matrícula.
