---
content_hash: a9fa61a7de02fae85dcc1c87a77eab8e27bcba6af8ad58f85879bf03a27dfbe3
fetched_at: '2026-06-28T21:35:16.956250+00:00'
page_id: '1019341119'
product: fluig
source: tdn-fluig
title: Migração de processo para produção usando formulário 2.0
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1019341119
version: 7
---

1

# Objetivo

---

Este documento detalha os passos para migrar um processo, incluindo seu formulário, do ambiente de desenvolvimento para o ambiente de produção.

Dica

Os códigos utilizados nesta documentação são para auxiliar no entendimento. Fique a vontade para utilizar códigos que fazem sentido com o dia a dia da sua empresa.

# Preparação do processo e formulário no desenvolvimento

---

**Processo criado**

* Um processo de exemplo foi criado: **Migrando para Produção** (código: **migrando-para-producao**).

**Formulário criado**

* O formulário associado foi criado: **Formulário de Migrando para Produção** (código: 3).

# Exportação do processo em desenvolvimento

---

**Exportar processo do ambiente de desenvolvimento**

* Obtenha o conteúdo (XML) do processo de desenvolvimento com o **ID do processo seja o mesmo** (migrando-para-producao) utilizando a API: **[GET /process-management/swagger-ui/#/Processes/exportProcess](https://api.fluig.com/latest/process-management/swagger-ui/#/Processes/exportProcess)**

**Exemplo de retorno**

* A execução da API retornou o seguinte corpo, que contém o body (o XML do do processo).

Importante

Recomendamos abrir a URL de exportação direto no navegador para então copiar o conteúdo ou fazer download, como no exemplo abaixo:

**Importar o processo para produção**

* Importe o novo processo para o ambiente de produção usando a API abaixo e populando os campos body, processId e release com os dados obtidos na etapa anterior. O body deve ser o XML copiado do retorno da API de exportação. [POST /process-management/swagger-ui/#/Processes/importNewProcess](https://api.fluig.com/latest/process-management/swagger-ui/#/Processes/importNewProcess)

Importante

É preciso alterar o campo **<formIdV2>** com o valor **0** para desvincular o formulário, ficando desta forma: **<formIdV2>0</formIdV2>**

**Resultado da criação**

* A execução bem-sucedida da API deve retorno o novo processo criado (no exemplo, o processo foi criado com o código: **migrando-para-producao**).

# Exportação do formulário em desenvolvimento

---

### Obtenção do conteúdo do formulário de desenvolvimento

**API para conteúdo do formulário**

* Obtenha o conteúdo (JSON) do formulário de desenvolvimento (código 3) utilizando a API: **[GET /form-management/Forms/getFormByCode](https://api.fluig.com/latest/form-management/swagger-ui/#/Forms/getFormByCode)**

**Exemplo de retorno**

* A execução da API retornou o seguinte corpo, que contém o content (o JSON do layout do formulário), como no exemplo abaixo:

# Criação do formulário em produção

---

**API para criação**

* Crie o novo formulário no ambiente de produção usando a API indicada no link e populando os campos **name**, **content**, **category** e **processId** com os dados obtidos no retorno da API de consulta. **[POST /form-management/Forms/createFormInDraftWithInitialVersion](https://api.fluig.com/latest/form-management/swagger-ui/#/Forms/createFormInDraftWithInitialVersion)**

**Exemplo do corpo da requisição**

**Resultado da criação**

* A execução bem-sucedida da API deve retornar o novo ID do formulário criado (no exemplo, o formulário foi criado com o código **4**).

# Finalização e publicação do processo e formulário em produção

---

**Edite o novo processo no ambiente de produção na web e publique**

* Com o Formulário (**código** **4**) e o Processo (**migrando-para-producao**) criados no ambiente de Produção, basta que você **edite o processo** e, em seguida, **publique-o**.
