---
content_hash: f0113aeea8bbd312e8f8c832eb393f6f96a2470237b6b30b0816b3beaaba0c6e
fetched_at: '2026-06-29T00:09:35.420784+00:00'
page_id: '425459348'
product: rm
source: tdn-rm
title: Linha RM x Protheus SigaMNT - Cadastro de Moeda
type: documentation
url: https://tdn.totvs.com/display/LRM/Linha+RM+x+Protheus+SigaMNT+-+Cadastro+de+Moeda
version: 3
---

**Linha** **RM x Protheus SigaMNT - Cadastro de Moeda**

---

As inclusões, alterações e exclusões de Moeda são feitos através do Linha RM, que identifica o evento em sua entidade e envia uma mensagem ao Protheus SigaMNT. Através da sincronia de dados, o Protheus pode utlizar as moedas enviadas em seus processos de Manutenção de Ativos.   
    
 Os dados sincronizados pela mensagem única são:

* Descrição
* Símbolo

**Observações:**

  Serão integrados somente os dados dos registros do tipo Moeda, desconsiderando registros do tipo Indices.

1. O Protheus, por default, aceita no máximo 5 tipos de Moedas.
2. O campo "Código da Moeda" é gerado pelo Adapter Protheus, uma vez que não existe o campo código no RM.

---

Para mais detalhes sobre o cadastro , acesse o Boletim Técnico.

**Recursos Adicionais**

TDN - Boletim Técnico : [Moedas](http://tdn.totvs.com/download/attachments/76251248/CONNECTOR_BT_CADASTRAR+MOEDA_BR_CON000158.pdf?version=1&modificationDate=1380044694000)
