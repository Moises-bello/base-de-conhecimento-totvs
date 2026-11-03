---
content_hash: a750a87d5c011cf791ee9766a7b0edd3b61654c279e450fd73213b8c8759526a
fetched_at: '2026-06-29T00:10:27.903991+00:00'
page_id: '517116366'
product: rm
source: tdn-rm
title: Utilizando a Atividade "Integração"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=517116366
version: 8
---

## **ÍNDICE**

1. **Visão Geral**
2. **Exemplo de utilização**

**01. VISÃO GERAL**

      A atividade "Integração" tem por função, enviar mensagens através da [mensageria única](https://tdn.totvs.com/x/H-5bGQ) (disponível no menu "Integração").

      Basicamente é necessário informar alguns parâmetros, obter os dados necessários e qual o objeto de negócio (DataServer) responsável por retornar as informações do registro. A partir destas informações a atividade se responsabiliza pela leitura, transformação e envio dos dados ao sistema de destino, oferecendo como retorno o Log de integração.

**02. EXEMPLO DE UTILIZAÇÃO**

      Descrição dos campos da atividade "Transformar Arquivo em Cadeia de Bytes":

**Atividade:**

* **Nome:**Nome da atividade
* **Descrição:** Descrição da atividade
* **Habilitado:** Define se a atividade estará em uso ou não.

**Geral:**

* **DataSet:** DataSet que será salvo pela atividade (representa um cache de dados na memória).
* **Retorno:** Retorno da mensageria padrão (o dataSet selecionado é transformado em XML)
* **Síncrono:** Retorno da mensageria padrão (executar de forma simultânea)
* **Tipo de Destino:** Operação a ser realizada (ex: MSGPadrão ou ESB)
* **TransactionID:** Código de transação

**RM.NET:**

* **Dados do Usuário: Dados do usuário (OwerData) de parâmetro da execução da atividade.**
