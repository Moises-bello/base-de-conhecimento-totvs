---
content_hash: 7403db5edba0a17b7b0e657adbbe0f9877f4ab9e59c3cb1490b3093b85e19c5f
fetched_at: '2026-06-29T00:09:45.863030+00:00'
page_id: '435097908'
product: rm
source: tdn-rm
title: Como gerar  o processo "Atualizar recibo entrega eSocial"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435097908
version: 19
---

## **Objetivo:**

---

O objetivo deste documento é demonstrar o processo de atualização do recibo entrega eSocial.

---

Esse processo irá preencher o campo "Recibo" dos  eventos que já estão na fila de eventos com Status 10-Aceito RET ou 11-Excluído RET e estão com o campo em branco.

Para habilitar este menu devemos dar permissão para o usuário através Serviços Globais | Segurança | Perfil | eSocial | Processos - Atualizar Recibo Entrega eSocial.

Para executar o processo deverá ir no menu Outros Processos-Atualizar Recibo Entrega esocial

O usuário poderá selecionar o tipo de arquivos, status do evento ,ID(identificador) a ser filtrado ou selecionar os eventos a serem atualizados.

O parâmetro Sobscrever Recibo quando marcado deve atualizar tantos os recibos existentes como os NULL.

**Exemplo I:**

Na fila temos o evento  S-1030 com status 10-Aceito Ret e não foi informado o número do recibo.

No TAF aba Monitoramento-Eventos de Tabela é visualizado o número Recibo para a função FUN1.

Em outros processos | Atualizar recibo de entrega eSocial selecionado o evento S-1030.

Verificando o status na fila de eventos.

**Exemplo II**: Evento enviado para TAF e até governo atualizando status na fila

Evento S1030 com código 1600 enviado e integrado no TAF

Na Fila atualizar status integração TAF

**Importante:**

O número do recibo será gravado na fila de eventos sempre que for atualizado o status do evento para 10-Aceito Ret .
