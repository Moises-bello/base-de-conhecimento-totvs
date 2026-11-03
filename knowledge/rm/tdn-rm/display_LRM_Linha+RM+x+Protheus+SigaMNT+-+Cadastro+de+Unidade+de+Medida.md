---
content_hash: 660e1f78a2d74dd1a60d0485a0d69ff6c0e27ff0ffba0bac5e597d0ed16f96a8
fetched_at: '2026-06-29T00:09:35.449008+00:00'
page_id: '425459355'
product: rm
source: tdn-rm
title: Linha RM x Protheus SigaMNT - Cadastro de Unidade de Medida
type: documentation
url: https://tdn.totvs.com/display/LRM/Linha+RM+x+Protheus+SigaMNT+-+Cadastro+de+Unidade+de+Medida
version: 3
---

**Linha** **RM x Protheus SigaMNT - Cadastro de Unidade de Medida**

---

As inclusões, alterações e exclusões de Unidade de Medida são feitas através do Linha RM, que identifica o evento em sua entidade e envia uma mensagem ao Protheus SigaMNT. Através da sincronia de dados o Protheus pode utlizar as unidades de medida enviadas, em seus processos de Manutenção de Ativos.   
    
 Os dados sincronizados pela mensagem única são :

* Código
* Descrição

**Observação:**

1. Visto que a base Protheus possui carga de unidades de medida padrões, que obrigatoriamente constam na base de dados, deve-se efetuar manualmente o cadastramento da relação "DE-PARA" nas tabelas referentes no RM e Protheus para viabilizar a integração de registros que utilizem estas como parâmetro.
2. As unidades de medida referentes à Hora (H), Quilometragem (KM), Unidade (UN) e Litro (L) devem possuir o mesmo código tanto no RM quanto no PROTHEUS.
3. O campo Código da Unidade de Medida no PROTHEUS será gerado pelo Adapter, uma vez que este campo no RM tem tamanho de 5 caracteres, no PROTHEUS 2 caracteres e na mensagem única 6 caracteres.

---

Para mais detalhes sobre o cadastro , acese o Boletim Técnico.

**Recursos Adicionais**

TDN - Boletim Técnico : [Unidade de Medida](http://tdn.totvs.com/download/attachments/76251248/CONNECTOR_BT_CADASTRAR+UNIDADE+DE+MEDIDA_BR_CON000158.pdf?version=1&modificationDate=1380044705000)
