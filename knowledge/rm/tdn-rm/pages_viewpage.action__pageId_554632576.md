---
content_hash: edea1cc056e25be752ba597530ac431a98317238483e95110a719d7b5a68bdd6
fetched_at: '2026-06-29T00:10:46.180060+00:00'
page_id: '554632576'
product: rm
source: tdn-rm
title: Cliente Smart eSocial e solução RH em ambiente local
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=554632576
version: 13
---

Importante

* Realizando o passo a passo não será possível o retorno ao serviço Smart.
1true1Passo 1Passo 1 - Atualizar recibos na fila e status pendentes

**Atualizar recibos na fila de eventos e status pendentes**

Para realizar a alteração do Smart eSocial para o Middleware é imprescindível realizar a atualização dos status pendentes e recibos na fila de eventos do RM, pois após sua alteração não será mais possível o resgaste dessas informações. 

1) Acesse o menu RH | Folha de Pagamento | eSocial | Atualizar Status Integração TAF

Este processo consulta o status atual do evento no TAF e atualiza a informação na [Fila de Eventos](https://tdn.totvs.com/display/LRM/Fila+de+Eventos).

**Observações:**

* A Quebra de Seção e Seleção de Funcionários na tela principal e nos parâmetros específicos da coligada, apenas serão habilitados caso seja marcado algum evento que relacione funcionários ou [Eventos Periódicos](https://tdn.totvs.com/pages/viewpage.action?pageId=452718520).
* O Período de Apuração será obrigatório caso selecione algum dos [Eventos Periódicos](https://tdn.totvs.com/pages/viewpage.action?pageId=452718520).
* Para a atualização do status de uma grande quantidade de registros, não é recomendável utilizar a Fila de Eventos, deverá utilizar o processo "Atualizar Status Integração TAF" que encontra-se disponível no menu  "eSocial".

2) Acesse o menu RH | Folha de Pagamento | eSocial | Outros Processos | Atualizar Recibo Entrega eSocial

Esse processo irá preencher o campo "Recibo" dos eventos que já estão na fila de eventos com Status "10-Aceito RET" ou "11-Excluído RET" e estão com o campo em branco.

Mais informações em: 

2Passo 2Passo 2 - instalar o TAF (serviço do middleware) e TSS

**Instalar o TAF (serviço do middleware) e TSS**

1) Verificar a aderência a migração ao serviço middleware e realizar o cancelamento da contratação do Smart eSocial, devendo acionar o suporte do Cloud e o CST para direcionarem a solicitação.

2) Instalar o TAF (serviço do middleware) e TSS local.

[https://tdn.totvs.com/pages/releaseview.action?pageId=520111521](https://www.google.com/url?q=https://tdn.totvs.com/pages/releaseview.action?pageId%3D520111521&sa=D&source=hangouts&ust=1593721254214000&usg=AFQjCNG5Lzl4Znka7ggqRtCDCSg_DxDTAw)

**Atenção:** Após o cancelamento da contratação do Smart eSocial, é fornecido um DUMP do Banco de Dados do cliente, ficará a cargo do mesmo definir se irá restaurar esse banco de dados para utilização do Middleware ou criar uma nova base de dados do TAF.

3Passo 3 Passo 3 - Execução do script para desativar o Smart eSocial no RM

**Execução do script para desativar o Smart eSocial no RM**

Para a desativação do Smart eSocial é necessário a limpeza do ambiente, que será executada através de um script especifico no sistema RM.Script.Executor.exe, sendo necessário solicitar esse script ao suporte de folha de pagamento.

Importante

* Para verificar a aderência a migração ao serviço middleware e realizar o cancelamento da contratação do Smart eSocial, devendo acionar o suporte do Cloud e o CST para direcionarem a solicitação.

* Antes de executar o script, certifique-se que o "Passo 1" foi executado com sucesso, pois após a execução do script não é possível mais resgatar as informações, e lembrando que, a ativação do serviço do middleware não é executada com eventos cujo os status sejam "3-Enviado TAF" ou "4-Aceito TAF".
4Passo 4Passo 4 - Realize o processo de Ativação do Middleware

**Realize o processo de Ativação do Middleware**

1) Para realizar a ativação siga o passo a passo
