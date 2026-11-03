---
content_hash: 692bc52ac0540d945f96fa3d2f60e30951c3aa8d80bf5fc001821b6d0d1b2608
fetched_at: '2026-06-29T00:10:57.104858+00:00'
page_id: '594179630'
product: rm
source: tdn-rm
title: Alterações S-2210 - Comunicação de Acidente de Trabalho
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=594179630
version: 9
---

false

**A partir das Versões:**

* 12.1.28.281
* 12.1.29.239
* 12.1.31.142

* e Superiores.

# Objetivo:

---

Apresentar as alterações realizadas no evento S-2210 para o leiaute do eSocial Versão S-1.0.

---

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {ideEmpregador} Campo {nrInsc} | Tamanho: 15  Informar o número de inscrição do contribuinte de acordo com o tipo de inscrição indicado no campo {tpInsc}. Se for um CNPJ deve ser informada apenas a Raiz/Base de oito posições, exceto se natureza jurídica de administração pública direta federal ([101-5], [104-0], [107-4], [116-3], situação em que o campo deve ser preenchido com o CNPJ completo (14 posições). Validação: Se {tpInsc} for igual a [1], deve ser um número de CNPJ válido. Se {tpInsc} for igual a [2], deve ser um CPF válido. | Tamanho: 14  Informar o número de inscrição do contribuinte de acordo com o tipo de inscrição indicado no campo {tpInsc}. Validação: Se {tpInsc} for igual a [1], deve ser um número de CNPJ válido. Neste caso, deve ser informada apenas a raiz/base (8 posições), exceto se natureza jurídica do declarante for igual a ([1015, 1040, 1074, 1104, 1139, 1163, 1198, 1252, 1287, 1317, 1341]), situação em que o campo deve ser preenchido com o CNPJ completo (14 posições). Se {tpInsc} for igual a [2], deve ser um CPF válido. |
| Grupos {ideLocalAcid}: Alterada condição | O (se {ideEmpregador/tpInsc} = [1], {tpLocal} = [1, 3]  e {codAmb} não for preenchido); OC (nos demais casos). | O (se ideEmpregador/tpInsc = [1] e tpLocal = [1, 3]); OC (nos demais casos) |
| Grupos {ideVinculo}: Campo {nisTrab} excluído. |  |  |
| Grupos {ideVinculo}: Campo {matricula} Alterada condição. | Matrícula atribuída ao trabalhador pela empresa ou, no caso de servidor público, a matrícula constante no Sistema de Administração de Recursos Humanos do órgão. Validação: Deve corresponder à matrícula informada pelo empregador no evento S-2200 do respectivo vínculo trabalhista. Se o trabalhador não está sujeito a esse evento (S-2200), a matrícula não deve ser informada, porém, o trabalhador deve ter sido registrado como TSVE - Trabalhador Sem Vínculo de Emprego/Estatutário, através do evento S-2300. | Matrícula atribuída ao trabalhador pela empresa ou, no caso de servidor público, a matrícula constante no Sistema de Administração de Recursos Humanos do órgão. Validação: Deve corresponder à matrícula informada pelo empregador no evento S-2190, S-2200 ou S-2300 do respectivo contrato. Não preencher no caso de Trabalhador Sem Vínculo de Emprego/Estatutário - TSVE sem informação de matrícula no evento S-2300. |
| Grupos {ideVinculo}: Campo {codCateg} Alterada condição. | Preencher com o código da categoria do trabalhador, conforme Tabela 01. Validação: Só informar se o trabalhador tiver sido registrado como TSVE - Trabalhador Sem Vínculo de Emprego/Estatutário, através do evento S-2300. Não informar nos demais casos. Se informado, deve existir na Tabela de Categorias de Trabalhadores (Tabela 01). | Preencher com o código da categoria do trabalhador. Informar somente no caso de TSVE sem informação de matrícula no evento S-2300. Validação: Informação obrigatória e exclusiva se não houver preenchimento de matricula. Se informado, deve ser um código válido e existente na Tabela 01. |
| Grupos {cat}: Campo {tpAcid} Alterada condição. | Tamanho: 4  Tipo de Acidente de Trabalho, conforme Tabela 24. Preencher com números e pontos. Validação: Dever ser um código da Tabela 24 - Codificação de Acidente de Trabalho. | Tamanho: 1  Tipo de acidente de trabalho. Valores válidos: 1 - Típico 2 - Doença 3 - Trajeto |
| Grupos {cat}: Campo {hrAcid} Alterada condição. | Hora do Acidente, no formato HHMM. Validação: Preenchimento obrigatório se {tpAcid} <> [2.0.01, 2.0.02, 2.0.03, 2.0.04, 2.0.05, 2.0.06, 4.0.01, 4.0.02]. Se informada, deve estar no intervalo entre [0000] e [2359], criticando inclusive a segunda parte do número, que indica os minutos, que deve ser menor ou igual a 59. Se {tpCat} = [2,3] deve ser informado valor igual ao preenchido no evento de CAT anterior, quando informado em {nrRecCatOrig}. | Hora do acidente, no formato HHMM. Validação: Preenchimento obrigatório e exclusivo se tpAcid = [1]. Se informada, deve estar no intervalo entre [0000] e [2359], criticando inclusive a segunda parte do número, que indica os minutos, que deve ser menor ou igual a 59. Se tpCat = [2, 3], deve ser informado valor igual ao preenchido no evento de CAT anterior, quando informado em nrRecCatOrig. |
| Grupos {cat}: Campo {hrsTrabAntesAcid} Alterada condição. | Horas trabalhadas antes da ocorrência do acidente, no formato HHMM. Validação: Deve estar no intervalo entre [0000] e [9959], criticando inclusive a segunda parte do número, que indica os minutos, que deve ser menor ou igual a 59. | Horas trabalhadas antes da ocorrência do acidente, no formato HHMM. Validação: Preenchimento obrigatório e exclusivo se tpAcid = [1]. Se informada, deve estar no intervalo entre [0000] e [9959], criticando inclusive a segunda parte do número, que indica os minutos, que deve ser menor ou igual a 59. |
| Grupos {localAcidente}: Campo {codAmb} excluído. |  |  |
| Grupos {localAcidente}: Campo {cep} Alterada condição. | Código de Endereçamento Postal - CEP. Validação: Preenchimento obrigatório se {tpLocal} = [1, 3, 5]. Não preencher se {tpLocal} = [2]. Se preenchido, deve ser um CEP válido e informado apenas com números. | Código de Endereçamento Postal - CEP. Validação: Preenchimento obrigatório se tpLocal = [1, 3, 5]. Não preencher se tpLocal = [2]. Se preenchido, deve ser informado apenas com números, com 8 (oito) posições |
| Grupo {ideLocalAcid} Campo {nrInsc} | Tamanho: 15 | Tamanho: 14 |
| Grupos {ideLocalAcid}: Campo {codCNES} excluído. |  |  |
| Grupos {emitente}: Campo {ufOC} Alterada ocorrência. |  | Passa a ser obrigatório. |
| Grupos {catOrigem}: Campo {nrRecCatOrig} Alterada condição. | Informar o número do recibo da última CAT referente ao mesmo acidente/doença relacionada ao trabalho, nos casos: a) de CAT de reabertura; b) de óbito, quando houver CAT anterior. Validação: Deve corresponder ao número do recibo do arquivo relativo à CAT informada anteriormente, pertencente ao mesmo trabalhador. O sistema não efetuará a conferência da informação se {dtAcid} for anterior à data de transferência no evento de admissão. Obs.: Quando {dtAcid} for anterior à data de obrigatoriedade do empregador ao envio deste evento, a CAT de reabertura e/ou de óbito não devem ser informadas ao eSocial, mantendo-se o procedimento realizado na emissão da CAT original. | Informar o número do recibo da última CAT referente ao mesmo acidente/doença relacionada ao trabalho, nos casos: a) de CAT de reabertura; b) de óbito, quando houver CAT anterior. Validação: Deve corresponder ao número do recibo do arquivo relativo à última CAT informada anteriormente, pertencente ao mesmo contrato, desde que indCatObito da última CAT informada seja igual a [N]. O sistema não efetuará a conferência da informação se dtAcid for anterior a sucessaoVinc/dtTransf, transfDom/dtTransf ou dtAltCPF do evento S-2200. OBS.: Quando a data do acidente for anterior à data de obrigatoriedade do empregador ao envio deste evento, a CAT de reabertura e/ou de óbito não devem ser informadas ao eSocial, mantendo-se o procedimento realizado na emissão da CAT original. |

Mais informações em:
