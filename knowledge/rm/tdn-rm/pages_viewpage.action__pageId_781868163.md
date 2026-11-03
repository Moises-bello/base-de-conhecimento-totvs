---
content_hash: 5858e937d8bfc77544c59626d28c7c33963e0f146ec0a163d150b4995f4ed5d4
fetched_at: '2026-06-29T00:11:38.189953+00:00'
page_id: '781868163'
product: rm
source: tdn-rm
title: Catálogo de Erros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=781868163
version: 1
---

Para facilitar e padronizar a informação para o usuário, os erros que podem ocorrer durante a integração da mensagem única, deverão ser tratados conforme catálogo abaixo.

Os códigos utilizam a seguinte máscara na sua composição:

```
XY999
```

Onde:

X - corresponde à área responsável pela geração do erro/aviso/informação. As letras possíveis na posição são:

* A - área de negócio (adapter).
* F - framework, mas não relacionado ao EAI.
* I - integração (EAI).

Y - corresponde à natureza da mensagem. As opções são:

* I - informação.
* W - aviso ou alerta.
* E - erro.

999 - código numérico sequencial.

| Código | Operação | Descrição | Retorno para mensagem |
| --- | --- | --- | --- |
| **AW001** | Exclusão | Registro   não encontrado | Retornará   código de warning informando que não encontrou o registro |
| **AW002** | Alteração/Exclusão | Não   existência de de/para | Retornará   código de warning informando que não encontrou o de/para |
| **AW003** | Inclusão/Alteração | Máscara incorreta | \*\* Aplicado somente nos casos padronizados ou em que   houve um acordo na fase de desenho da integração.  Retornará código de warning informando que a máscara   está incorreta. |
| **AE001** | Exclusão | Registro relacionado em movimentações | Retornará código de erro informando que o registro não poderá ser   excluído, pois está sendo utilizado em tabelas de movimentações. |
| **AE002** | Alteração | FK não encontrada; Encontrou o de/para, mas não   encontrou o registro na base | Retornar código de erro informando que não ser   alterado o registro, pois faltam cadastros relacionados. |
| **AE003** | Inclusão/Alteração | Exception (Erro de programação) | Retornar Erro + Log padrão de cada produto |
| **AE004** | Inclusão/Alteração | Empresa não configurada para integração | Retornará código de erro informando que a empresa enviada na Tag CompanyId (BusinessContent) não está habilitada para integração |
| **FI001** | HealthCheck - License | Sucesso ao checar a disponibilidade de um servidor de licenças. | Retornará uma mensagem padrão de sucesso ao checar a disponibilidade de um servidor de licenças.  Status = License Server Ativo |
| **FI002** | HealthCheck - License/Get | Sucesso ao consumir a licença de teste. | Retornará uma mensagem padrão de sucesso ao consumir a licença de teste.  Status = Licença Consumida |
| **FI003** | HealthCheck - Database | Sucesso ao checar a disponibilidade de um banco de dados. | Retornará uma mensagem padrão de sucesso ao checar a disponibilidade de um banco de dados.  Status = Banco de Dados Ativo |
| **FW001** | HealthCheck - License | Versão do License Server incompatível. | Retornará um alerta sobre a versão do ERP não ser compatível com a atual versão do License Server.  ReturnCode = -99  Status = License Server Ativo |
| **FW002** | HealthCheck - License | License Server offline | Retornará um alerta sobre a indisponibilidade do License Server.  ReturnCode = -10008  Status = License Server Inativo |
| **FW003** | HealthCheck - License/Get | Aplicação não conseguiu consumir licença de teste. | Retornará uma alerta sobre a impossibilidade de se consumir a licença de teste.  ReturnCode = {ErrorCode proveninente do License Server}  Status = Licença Não Consumida |
| **FW004** | HealthCheck - Database | Banco de dados offline | Retornará um alerta sobre a indisponibilidade do banco de dados.  Status = Banco de Dados Inativo |
| **FW005** | Todas | Usuário não tem permissão para utilizar o recurso e/ou executar uma determinada operação no sistema | Retornará o código de erro e a mensagem informando que o usuário não tem permissão. No mensagem detalhada, será informado o código de permissão necessário, caso exista. |
| **FE001** | Todas | Mensagem padrão no formato incorreto | Tratado pelo EAI (Framework) |
| **FE002** | Todas | Incompatibilidade de versões da mensagem única | Tratado pelo EAI (Framework) |
| **FE003** | Todas | Timeout | Tratado pelo EAI (Framework) |
| **FE004** | Todas | Mensagem já existe no repositório com o UUID informado | Tratado pelo EAI (Framework) |
| **FE005** | Todas | Não autorizado | Tratado pelo EAI (Framework) |
| **FE006** | Todas | Exceção não tratada | Tratado pelo EAI (Framework) |
| **FE007** | Todas | Stack Trace |  |
| **FE008** | HealthCheck - License | Erro desconhecido ao tentar consumir a licença de teste | Erro na tentativa de consumir a licença de teste. Objeto retornado pelo License Server não contem mensagem ou ErrorCode, que defina a exceção. |
| **FE009** | Todas | Erro ao recuperar informações para conexão com o banco de dados. | Erro ao recuperar informações necessárias para realizar a conexão com o banco de dados. |
| **FE010** | Envio/Recebimento | Ambiente EAI não está devidamente configurado. | Retornar dicas do que pode estar faltando em relação à configuração do EAI. |
| **FE011** | Todas | Registro não encontrado | Indica que o registro não foi encontrado na base de dados. |
| **FE012** | Put / Post | Propriedades Chave [Prop1, Prop2, ...] com valores diferentes. | Indica que as propriedades chave [Prop1, Prop2, ...] foram submetidas à API com valores diferentes. |
| **FE013** | Put | Propriedade definida na rota do método PUT com valores diferentes das Propriedades Chave [Prop1, Prop2, ...] | Inidica que a propriedade definida na rota do método PUT foi submetida à API com valores diferentes das propriedades chave [Prop1, Prop2, ...] |
| **FE014** | Todas | Método não implementado | Indica que um método HTTP não foi implementado. |
| **FE015** | Exclusão | Registro não pode ser excluído | Retornará código de erro informando que o registro não poderá ser   excluído, por motivo de regra de negócio. |
| **FE016** | Todas | Quando a requisição não possuir os dados "Essenciais" da requisição ou o mesmo estiver errado | Retornará o código de erro informando que é necessário preencher o corretamente os dados da requisição |
| **FE017** | Api de Parâmetros do Sistema - Get | Erro ao recuperar o valor de um parâmetro do sistema. | Retornará o código de erro informando que o valor de pelo menos um dos parâmetros não pôde ser recuperado. |
| **FE018** | Post / Put | Quando o corpo da mensagem não respeitar uma regra de negócio da API. | Retornará o código de erro informando que é necessário preencher o corretamente o corpo da requisição |
| **FE019** | Todos | Quando por algum motivo de regra de negócio a requisição não pode ser executada | Retornará o código de erro e o motivo que a requisição não pode ser executada. |
| **FE020** | Api de Parâmetros do Sistema - Get | Servidor de parâmetros não encontrado. | Retornará o código de erro e a mensagem informando a obrigatoriedade de se informar o servidor de parâmetros. |
| **IE001** | Pesquisa | Identificador da requisição inválido | Erro na validação do identificador da requisição. |
| **IE002** | Inclusão/Alteração | Campos da estrutura JSON inválida | Erro na validação dos campos da estrutura json enviada para persistência. |
| **IE003** | Pesquisa | Entidade não encontrada | Erro ao buscar entidade no repositório. |
| **IE004** | Inclusão/Alteração | Estrutura JSON inválida | Erro na validação da estrutura json enviada para persistência |
| **IE005** | Todas | Aplicativo de origem (sourceApplication) desconhecido. | Retornar o nome do aplicativo de origem fornecido na mensagem. |
| **IE006** | Todas | Aplicativo de origem (sourceApplication) não foi informado. |  |
| **IE007** | Todas | Aplicativo de origem é o próprio aplicativo de recebimento. | Retornar o nome do aplicativo interno. |
| **IE008** | Todas | Transação e versão não está habilitada para recebimento. | Retornar o nome da transação e a versão. |
| **IE009** | Todas | Falha na comunicação entre sistemas. | Mensagem de erro retornada pelo canal de comunicação. |
