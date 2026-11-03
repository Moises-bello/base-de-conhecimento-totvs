---
content_hash: e9d14d0708be7b9b925e214d38e7c101b76dd03d58e9b560b0b572fe89a71911
fetched_at: '2026-06-29T00:10:57.098459+00:00'
page_id: '594163257'
product: rm
source: tdn-rm
title: Alterações S-2205
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=594163257
version: 8
---

false

**A partir das Versões:**

* 12.1.29.282
* 12.1.31.197
* 12.1.32.135
* e Superiores.

# Objetivo:

---

Apresentar as alterações realizadas no evento S-2205 para o leiaute do eSocial Versão S-1.0.

---

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupos {alteracao }: Campo {dtAlteracao} incluída validação. | Preencher com a data da alteração das informações. | Preencher com a data da alteração das informações. Validação: Não pode ser posterior a 180 (cento e oitenta) dias da data atual. |
| Grupos {nascimento}: Campo {dtNascto},{codMunic}, {uf}, {paisNascto}, {nmMae }, {nmPai} excluído. |  |  |
| Grupos {documentos}: Campo |  |  |
| Grupos {CTPS}: Campo {nrCtps},{serieCtps }, {ufCtps}, excluído. |  |  |
| Grupos {RIC}: Campo {nrRic},{orgaoEmissor }, {dtExped}, excluído. |  |  |
| Grupos {RG}: Campo {nrRg},{orgaoEmissor }, {dtExped}, excluído. |  |  |
| Grupos {OC}: Campo {nrOc},{orgaoEmissor }, {dtExped},{dtValid} excluído. |  |  |
| Grupos {CNH}: Campo {nrRegCnh},{dtExped}, {ufCnh},{dtValid}, {dtPriHab}, {categoriaCnh} excluído. |  |  |
| Grupos {RNE}: Campo {nrRne},{orgaoEmissor }, {dtExped} excluído. |  |  |
| Grupos {trabEstrangeiro}: Campo {dtChegada},{classTrabEstrang}, {casadoBr}, {filhosBr} excluído. |  |  |
| Grupos {aposentadoria}: Campo {trabAposent} excluído. |  |  |
| Grupos {alteracao}: Campo {nisTrab} excluído. |  |  |
| Grupos {trabImig}: Grupo adicionado |  | OC (se paisNac for diferente de [105]); N (nos demais casos) |
| Grupos {trabImig}: Campo {tmpResid}, adicionado. |  | Tempo de residência do trabalhador imigrante. Valores válidos: 1 - Prazo indeterminado 2 - Prazo determinado Validação: Preenchimento obrigatório quando houver trabalhador com (dtAdm ou dtExercicio ou dtInicio) no Registro de Eventos Trabalhistas - RET >= [2021-05-10]. |
| Grupos {trabImig}: Campo {condIng}, adicionado. |  | Condição de ingresso do trabalhador imigrante. Valores válidos: 1 - Refugiado 2 - Solicitante de refúgio 3 - Permanência no Brasil em razão de reunião familiar 4 - Beneficiado pelo acordo entre países do Mercosul 5 - Dependente de agente diplomático e/ou consular de países que mantêm acordo de reciprocidade para o exercício de atividade remunerada no Brasil 6 - Beneficiado pelo Tratado de Amizade, Cooperação e Consulta entre a República Federativa do Brasil e a República Portuguesa 7 - Outra condição Validação: Se tmpResid = [1], não pode ser informado [2, 5]. Se tmpResid = [2], não pode ser informado [1]. |
| Grupos {nascimento }: Campo {paisNac} excluído. |  |  |
| Grupos {dadosTrabalhador}: Campo {paisNac} adicionado. |  | Preencher com o código do país de nacionalidade do trabalhador. Validação: Deve ser um código válido e existente na Tabela 06. |
| Grupos {dependente}: Campo {sexoDep} adicionado. |  | Sexo do dependente. Valores válidos: M - Masculino F - Feminino Validação: Preenchimento obrigatório e exclusivo quando houver trabalhador cadastrado no evento S2200, ativo em dtAlteracao e com {tpRegPrev} = [2] no RET. |
| Grupos {contato}: Campo {foneAlternat},{emailAlternat} excluído. |  |  |
