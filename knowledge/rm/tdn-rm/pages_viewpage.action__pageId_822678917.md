---
content_hash: 85d5c829880f04294812df4a1914da75dd5f31af5ac26705c2935dcdb711c9ab
fetched_at: '2026-06-29T00:11:46.050439+00:00'
page_id: '822678917'
product: rm
source: tdn-rm
title: DPS/infDPS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=822678917
version: 10
---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nome | Pai | Obrigatório | Origem | Descrição |
| **infDPS** | **DPS** | **Sim** | **Grupo** | **Grupo de informações da declaração de prestação de serviços.** |
| id | DPS/infDPS | Sim | ID gerado para a nota | O ID é composto por: "DPS"  + Código de classificação do município + 1 ou 2 (pessoa jurídica sendo 1 e pessoa física sendo 2) + série da nota + número do movimento da nota |
| tpAmb | DPS/infDPS | Sim | Tipo do ambiente da nota | Preenchido com 1 ou 2, sendo 1 = Produção e 2 = Homologação |
| dhEmi | DPS/infDPS | Sim | Data de emissão da nota | Data e hora de emissão da nota  A data é obtida do campo "Data de Emissão" e o horário do campo "Horário de Emissão"  TMOV.DATAEMISSAO + TMOV.HORARIOEMISSAO Campos no movimento   O horário de emissão pode ser habilitado pelo parâmetro "Edição do Horário de Emissão" nos parâmetros de data do tipo de movimento. Devendo ser selecionada uma opção diferente de "Não Utiliza". Parâmetro |
| verAplic | DPS/infDPS | Sim | Versão da aplicação do sistema. Ex.: 12.1.2402 | Versão da aplicação do sistema. Ex.: 12.1.2402 |
| serie | DPS/infDPS | Sim | Série informada na movimentação da nota | Série informada na movimentação da nota |
| nDPS | DPS/infDPS | Sim | Número do movimento da nota | Número do movimento da nota |
| dCompet | DPS/infDPS | Sim | Data de competência da nota | Data de competência da nota |
| tpEmit | DPS/infDPS | Sim | Tipo do Emitente da nota | Gerado fixo como "prestador" |
| cLocEmi | DPS/infDPS | Sim | Município da Filial da nota | Município da Filial da nota |
