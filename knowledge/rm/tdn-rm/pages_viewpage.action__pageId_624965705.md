---
content_hash: b49d3dc09d763f7997295a04703b64f8985bd54d037c9acb7f84e79dfd07ce56
fetched_at: '2026-06-29T00:11:04.085985+00:00'
page_id: '624965705'
product: rm
source: tdn-rm
title: Geração do IDTSS para integração com o TSS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=624965705
version: 6
---

A comunicação com o TSS é feita através do campo IDTSS, disponível na tela da SPED (Estadual).

Observação

Pode ser necessário habilitar a visualização do campo no ícone Configurar Colunas.

0Regras

O IDTSS corresponde ao campo NFE\_ID / DOC\_ID das tabelas do TSS.

Regra para preenchimento do IDTSS no RM:

* Preenchido no PRIMEIRO envio do documento com a chave de acesso.
* Após preenchido, o campo não é mais alterado, por mais que a chave de acesso seja alterada.
Importante

* Isso se aplica para NF-e e NFC-e.
* Esse campo é para controle interno da integração do RM com o TSS. Essa informação não é enviada para a SEFAZ.
* Disponível a partir da versão 12.1.29 (Ambiente atualizado).

As notas criadas anteriores a criação deste campo não irão ocorrer problemas. Para o legado o sistema permanece com o comportamento anterior da geração do NFE\_ID (100000000 - (Coligada + Idmov).
