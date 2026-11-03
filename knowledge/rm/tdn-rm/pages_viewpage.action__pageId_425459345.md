---
content_hash: f70d8f79f91fba4b24ac104c61118e83b43867d7ca401e9ac269ff16205c3308
fetched_at: '2026-06-29T00:09:35.414555+00:00'
page_id: '425459345'
product: rm
source: tdn-rm
title: Tratamento Específico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459345
version: 3
---

**Tratamento Específico**

---

Nas integrações, os aplicativos enviam mensagens cujo conteúdo pode estar relacionado a outro registro. Embora informações referentes ao registro sejam enviadas, outros dados necessários podem não ter sido, gerando a necessidade de um tratamento específico para obter estes dados.   
  Por exemplo, na integração TOTVS Obras e Projetos x BackOffice EMS, em uma mensagem referente a um documento de Nota Fiscal de Compra , o código do produto é enviado, mas o ID do produto não, sendo o mesmo necessário para gravação na base de dados.   
  Um tratamento específico é então criado para descobrir, via consulta SQL, qual o ID correspondente a um determinado código de produto.  
    
 ***Observações***

* O tratamento específico é disparado nos pacotes de integração somente durante o Agente de Recebimento.
* Um pacote de integração pode possuir um ou vários tratamentos específicos, cadastrados automaticamente pela execução do wizard de configuração. Mas também é possível cadastrar manualmente novos tratamentos específicos. Para isso basta acessar a visão de Tratamentos Específicos e incluir um novo.

A visão é composta pelos campos:

* **Descrição Tratamento:** É necessário informar uma descrição sucinta da finalidade do tratamento específico.
* **Data Server:** Informe o Data Server correspondente. Em caso de dúvidas consulte o suporte da Linha RM.
* **Tabela Tratamento:** Informe o nome da tabela do banco de dados.
* **Campo Tratamento:** Informe o nome do campo da tabela do banco de dados.
* **Tratar Somente Nulo:**  Permite que o tratamento específico também seja aplicado caso o valor do campo esteja nulo na mensagem de origem.
* **Código da Sentença:** Selecione a sentença SQL para obter o valor desejado para o Campo Tratamento. Pode ser uma sentença pré-cadastrada ou incluir uma nova.
* **Descrição Exceção:** Campo opcional, nele deve ser informado uma mensagem a ser exibida caso o tratamento específico não seja executado com sucesso.
