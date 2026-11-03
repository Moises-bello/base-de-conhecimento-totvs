---
content_hash: c85f59dcc57bb4258e40a38688fd7d1b45c7773c0c9999a62456d0dcd24c330a
fetched_at: '2026-06-29T00:11:46.066822+00:00'
page_id: '822679381'
product: rm
source: tdn-rm
title: infDPS/toma
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=822679381
version: 12
---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nome | Pai | Obrigatório | Origem | Descrição |
| **toma** | **DPS/infDPS/** | **Sim** | **Grupo** | **Grupo de informações relativas ao tomador do serviço.**    **Obs.**: O envio da NFS-e Nacional sem identificação do Tomador é permitido, conforme regras do documentos fiscal e da Prefeitura.  Como não é possível deixar de informar um  Cliente no movimento, é necessário criar um fictício conforme documentação.  [NFS-e com Tomador Não Identificado - Linha RM - TDN](https://tdn.totvs.com/pages/viewpage.action?pageId=439355177) |
| CNPJ | DPS/infDPS/toma | Sim\* | CNPJ do Cli/For |  |
| CPF | DPS/infDPS/toma | Sim\* | CPF do Cli/For |  |
| NIF | DPS/infDPS/toma | Sim\* | Número de identificação fiscal do Cli/For |  |
| cNaoNIF | DPS/infDPS/toma | Sim\* | Motivo sem NIF | 0 - Não informado na nota de origem 1 - Dispensado do NIF 2 - Não exigência do NIF |
| CAEPF | DPS/infDPS/toma | Não | Cadastro de Atividade Econômica da Pessoa Física do Cli/For |  |
| IM | DPS/infDPS/toma | Não | Inscrição Municipal do Cli/For |  |
| xNome | DPS/infDPS/toma | Sim | Nome do Cli/For |  |
| fone | DPS/infDPS/toma | Não | Telefone do Cli/For |  |
| email | DPS/infDPS/toma | Não | E-mail do Cli/For | Gerado com o Campo e-Mail do Cadastro do Cliente\Fornecedor - Identificação - FCFO.EMAIL |

Elemento de escolha

Para os campos marcados com asterisco ("Sim\*"), é obrigatório que pelo menos uma das informações sejam preenchidas. Por exemplo, caso o CNPJ seja informado, não necessariamente será informado o CPF do cli/for.
