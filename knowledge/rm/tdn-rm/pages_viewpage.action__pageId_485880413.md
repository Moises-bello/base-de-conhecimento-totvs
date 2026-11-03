---
content_hash: 0f3df10e1a90debf0ae55bc79b270daccfb2872652a23bcb74b7391707cb08d4
fetched_at: '2026-06-29T00:10:20.141783+00:00'
page_id: '485880413'
product: rm
source: tdn-rm
title: Endereço de Prestação do Serviço
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=485880413
version: 11
---

Conforme as regras de cada prefeitura pode ser necessário informar o endereço completo do local de prestação do serviço. Neste caso devem ser criados os campos complementares abaixo no movimento e parametrizados no tipo de movimento.

**Campos Complementares:**

| Nome da Coluna | Descrição | Tipo |
| --- | --- | --- |
| TIPOENDPREST | Tipo do Endereço | Texto |
| ENDPREST | Endereço | Texto |
| NUMPREST | Número | Texto |
| COMPLPREST | Complemento | Texto |
| BAIRPREST | Bairro | Texto |
| CEPPREST | Cep | Texto |

O **tamanho** do campo deverá ser preenchido conforme layout da prefeitura vigente.

Quando integrado com educacional , durante a geração de movimento o sistema verifica se o município do cliente é diferente do município da Filial, se sim, o Educacional cópia automaticamente as informações do endereço da Filial para os respectivos campos complementares parametrizados.

**Observações:**

* Os campos complementares criados no movimento devem seguir exatamente a nomenclatura citada acima (nome, nome da coluna e  tipo).
* No Município de Rio claro o campo prestacao.logradouro será preenchido com o resultado da concatenação entre os campos TIPOENDPREST e ENDPREST.
* O campo "Tipo do Endereço" TIPOENDPREST precisa ser preenchido com um dos seguintes valores abaixo. Caso não seja informado um dos valores abaixo o sistema irá gerar no xml somente a tag logradouro concatenando o TIPOENDPREST + ENDPREST.

|  |
| --- |
| AVENIDA |
| RUA |
| RODOVIA |
| RUELA |
| RIO |
| SITIO |
| SUP QUADRA |
| TRAVESSA |
| VALE |
| VIA |
| VIELA |
| VILA |
| VARGEM |
| ALAMEDA |
| PRAÇA |
| BECO |
| VIA ELEVADA |
| PARQUE |
| LARGO |
| VIELA PARTICULAR |
| PATIO |
| VIELA SANITÁRIA |
| LADEIRA |
| JARDIM |
| ESTRADA |
| PONTE |
| RUA PARTICULAR |
| PRAIA |

Após criação dos campos complementares é necessário que o mesmo seja ativado nos parâmetros do tipo de movimento:
