---
content_hash: c85f1ee718d993436c0c777276a2074d92562729e7acae112d5918d3f3ad89f4
fetched_at: '2026-06-29T00:05:49.387021+00:00'
page_id: '1040976898'
product: rm
source: tdn-rm
title: 7 - Registrar Boleto Híbrido em lote
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1040976898
version: 5
---

O registro o boleto híbrido pode ocorrer através do processo **Registrar Boleto Híbrido em lote** ou na visão de Boletos ou através do processo **Registrar Boleto Híbrido**. É necessário que o boleto já esteja cadastrado no sistema, podendo ser visualizado através do menu **Contas a Pagar/Receber | Boleto Híbrido | Registrar Boleto Híbrido em lote .**

Será exibida a tela de filtros para localizar os boletos que deseja registrar. Após selecionar os boletos desejados, clique em **Avançar**.

### Informações Atualizadas Automaticamente

Após a confirmação do registro pelo banco, os seguintes campos serão preenchidos automaticamente no boleto:

* **Nosso Número**
* **Linha Digitável**
* **Código de Barras**
* **QR Code Pix**

Essas informações são **geradas pelo banco no momento do registro**.

### Origem das Informações de Juros, Multa e Desconto

Os campos abaixo são preenchidos conforme a seguinte regra:

1️⃣ O sistema primeiro verifica os dados configurados no **Convênio Bancário**  
2️⃣ Caso não estejam configurados no convênio, serão utilizados os valores definidos **no próprio boleto**

Campos considerados:

* Desconto
* Multa
* Juros
* Modalidade

### Criação da Transação do Boleto

Ao realizar o registro do boleto híbrido, o sistema **cria automaticamente uma transação associada ao boleto**.

Essa transação garante o controle e atualização correta das informações relacionadas ao registro.

### Status de Registro do Boleto

Após o envio para registro, o boleto poderá apresentar os seguintes status:

**Pagamento Solicitado**  
✔ O registro foi realizado com sucesso e o boleto foi atualizado.

**Falha no Pagamento**  
⚠ Ocorreu algum problema no processo de registro do boleto.

Nessa situação, recomenda-se verificar os logs gravados na tabela FLOG.

Consulta para ajudar a localizar o LOG da transação com falha no pagamento

SELECT \*   
             FROM FLOG  
                         WHERE NOMEIDORIGEM = 'FINTEGRACAOCARTAO'  
                                                                        AND FUNCIONALIDADE LIKE 'BoletoHibrido%'  
                                                                        AND IDORIGEM = 'XXXXXX' -- COLOCAR IDTRANSACAO

### Regras Importantes

Caso o boleto esteja com o status:

**Remessa Registrado Boleto Híbrido**

❗ Não será possível realizar um novo registro.

Para registrar novamente o boleto, será necessário:

1. **Cancelar o registro atual**
2. Após o cancelamento, realizar **um novo registro**
