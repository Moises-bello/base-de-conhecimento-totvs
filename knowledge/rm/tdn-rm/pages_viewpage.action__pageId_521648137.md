---
content_hash: a0a70fe4ca378406135256ae44f787d5cb1176d9ed8109a5ddac5e00e50f7c54
fetched_at: '2026-06-29T00:10:31.674412+00:00'
page_id: '521648137'
product: rm
source: tdn-rm
title: RM - 04 Processo de Exclusão das Informações do Contribuinte (Produção Restrita)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=521648137
version: 3
---

Foi implementado o processo "Transmitir Exclusão das Informações do Contribuinte" em RM | Gestão Fiscal | Obrigações Acessórias | SPED | EFD-Reinf | Eventos Cadastrais.

Este processo ao ser executado envia um Evento R-1000 para a Receita que solicita a exclusão de todas operações do contribuinte no ambiente de **Produção Restrita**na Base de dados da Receita.

ATENÇÃO

Esse processo irá excluir todos os eventos da base RM.

Validações:

* O tipo do evento selecionado deve ser R-1000.
* O Ambiente do Evento R-1000 deve ser **Produção Restrita.**
* Para transmissão do Evento R-1000 é necessário que o mesmo esteja **Autorizado**.

Se a transmissão da exclusão for executada com sucesso então o status do Evento R-1000 passará a ser **Pendente Exclusão.**

Caso contrário o status do Evento continua como **Autorizado** e será persistido no histórico do evento o motivo da rejeição da Exclusão.

Processo de Consulta Evento foi evoluído para excluir os eventos filhos como R-1070, R-5011 e R-20xx após aceite deste evento.

**Observação:** Apenas o Evento R-1000 selecionado persistira com status **Não Transmitido** e somente com o histórico desta operação.

Imagem
