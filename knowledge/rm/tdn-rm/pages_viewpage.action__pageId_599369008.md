---
content_hash: 1aa9c2e0255208da2c0f118069e54b14eb23a19b6d85babebda9f1132f07dda5
fetched_at: '2026-06-29T00:10:57.704023+00:00'
page_id: '599369008'
product: rm
source: tdn-rm
title: Alterações S-2306
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=599369008
version: 5
---

false

**A partir das Versões:**

* 12.1.29.282
* 12.1.31.197
* 12.1.32.135
* e Superiores.

# Objetivo:

---

Apresentar as alterações realizadas no evento S-2306 para o leiaute do eSocial Versão S-1.0.

---

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupos {evtTSVAltContr}: incluído regra: REGRA\_ENVIO\_PROC\_FECHAMENTO,  REGRA\_MESMO\_PROCEMI,  REGRA\_RETIFICA\_MESMO\_VINCULO,  REGRA\_TSV\_ATIVO\_NA\_DTEVENTO.  Excluído regra:  REGRA\_EXISTE\_EVENTO\_TSV\_INICIO,  REGRA\_VALIDA\_TRABALHADOR\_BASE\_CNIS |  |  |
| Grupos {ideTrabSemVinculo}: Campo {matricula} adicionado. |  | Matrícula atribuída ao trabalhador pela empresa. Validação: Deve corresponder à matrícula informada pelo empregador no evento S-2300 do respectivo contrato. Não preencher no caso de TSVE sem informação de matrícula no evento S-2300. |
| Grupos {ideTrabSemVinculo}: Campo {codCateg} alterada ocorrência, condição e validação. | 1-1  Preencher com o código da categoria do trabalhador, conforme Tabela 1. Validação: Deve existir na Tabela de Categorias de Trabalhadores (tabela 1). | 0-1  Preencher com o código da categoria do trabalhador. Informar somente no caso de TSVE sem informação de matrícula no evento S-2300. Validação: Informação obrigatória e exclusiva se não houver preenchimento de matricula. Se informado, deve ser um código válido e existente na Tabela 01. |
| Grupos {infoTSVAlteracao}: Campo {dtAlteracao} incluída validação. | Preencher com a data da alteração das informações. | Preencher com a data da alteração das informações. Validação: Não pode ser posterior a 180 (cento e oitenta) dias da data atual. |
| Grupos {infoTSVAlteracao}: Campo {natAtividade} condição alterada. | Natureza da atividade, conforme opções abaixo: 1 - Trabalho Urbano; 2 - Trabalho Rural. Validação: Preenchimento obrigatório para as categorias de avulso, cooperado e dirigente sindical. Não deve ser preenchido para as categorias Diretor não empregado, servidor público indicado a conselho, membro de conselho tutelar e estagiário. Valores Válidos: 1, 2. | Natureza da atividade. Valores válidos: 1 - Trabalho urbano 2 - Trabalho rural Validação: Preenchimento obrigatório se o código de categoria no Registro de Eventos Trabalhistas - RET for igual a [201, 202, 401, 731, 734, 738]. Não deve ser preenchido se o código de categoria no RET for igual a [721, 722, 771, 901]. |
| Grupos {cargoFuncao}:  condição alterada. | OC (Se {codCateg} = [901, 903, 904, 905]); O (Nas demais situações) | OC (se o código de categoria no RET for igual a [901, 903, 904]); O (nos demais casos) |
| Grupos {cargoFuncao}: Campos {codFuncao},{codCargo} excluído. |  |  |
| Grupos {cargoFuncao}: Campo {nmCargo} adicionado. |  | Informar o nome do cargo. Validação: Preenchimento obrigatório se o código de categoria no RET for diferente de [410]. |
| Grupos {cargoFuncao}: Campo {nmFuncao} adicionado. |  | Informar o nome da função de confiança. Validação: Preenchimento obrigatório se o código de categoria no RET for igual a [410] e não houver informação de nmCargo. |
| Grupos {cargoFuncao}: Campo {CBOCargo} adicionado. |  | Ocorrência: 0 - 1  Tamanho: 6  Informar a Classificação Brasileira de  Ocupações CBO relativa ao cargo.  Validação:  Informação obrigatória e exclusiva  se nmCargo for preenchido.  Se informado, deve ser um código  válido e existente na tabela de CBO,  com 6 (seis) posições. |
| Grupos {cargoFuncao}: Campo {CBOFuncao} adicionado. |  | Ocorrencia: 0 - 1  Tamanho: 6  Informar a CBO relativa à função de confiança/cargo  em comissão. Validação: Informação obrigatória  e exclusiva se nmFuncao for preenchido.  Se informado, deve ser um código válido  e existente na tabela de CBO,  com 6 (seis) posições. |
| Grupos {renumeracao}:  condição alterada. | O (se categoria igual a diretor não empregado, servidor público indicado a conselho ou membro de Conselho Tutelar) OC (nas demais situações). | O (se codCateg = [721, 722, 771]); OC (nos demais casos) |
| Grupos {infoDirigenteSindical}: Campo {tpInsc} adicionado. |  | Preencher com o código correspondente ao tipo de inscrição, conforme Tabela 05. Valores válidos: 1 - CNPJ 2 - CPF Validação: O preenchimento é obrigatório e exclusivo se infoDirigenteSindical/categOrig corresponder a "Empregado", "Agente Público", "Avulso" ou for igual a [721]. |
| Grupos {infoDirigenteSindical}: Campo {tpRegPrev} adicionado. |  | Tipo de regime previdenciário (ou Sistema de Proteção Social dos Militares). Valores válidos: 1 - Regime Geral de Previdência Social - RGPS 2 - Regime Próprio de Previdência Social - RPPS ou Sistema de Proteção Social dos Militares 3 - Regime de Previdência Social no exterior Validação: Se infoDirigenteSindical/categOrig for relativa a "Empregado", não pode ser preenchido com [2]. |
| Grupos {infoTrabCedido}:  condição alterada. | O (se categoria do trabalhador = trabalhador cedido) N (nas demais situações) | O (se codCateg = [410]); N (nos demais casos) |
| Grupos {infoTrabCedido}: Campo {tpRegPrev} alterada descrição e validação. | Tipo de regime previdenciário conforme opções abaixo: 1 - Regime Geral da Previdência Social - RGPS; 2 - Regime Próprio de Previdência Social - RPPS; 3 - Regime de Previdência Social no Exterior. Validação: Se {categOrig} for relativa a Empregado, não pode ser preenchido  com [2]. Valores Válidos: 1, 2, 3. | Tipo de regime trabalhista. Valores válidos: 1 - CLT - Consolidação das Leis de Trabalho e legislações trabalhistas específicas 2 - Estatutário/legislações específicas (servidor temporário, militar, agente político, etc.)  Validação: O preenchimento é obrigatório e exclusivo se infoDirigenteSindical/categOrig corresponder a "Empregado" ou "Agente Público". |
| Grupos {infoEstagiario}: alterada condição | O (se categoria igual a estagiário) N (nas demais situações) | O (se o código de categoria no RET for igual a [901]); N (nos demais casos) |
| Grupos {infoEstagiario}: Campo {areaAtuacao} alterado tamanho. | 50 | 1-100 |
| Grupos {infoEstagiario}: Campo {vlrBolsa} excluído. |  |  |
| Grupos {instEnsino}: Campo {nmRazao} incluída validação e alterada ocorrência. | Informar a razão social.  1-1 | Informar a razão social. Validação: Preenchimento obrigatório e exclusivo se o campo cnpjInstEnsino não estiver preenchido.  0-1 |
| Grupos {instEnsino}: Campo {dscLograd} incluída validação. | Descrição do logradouro. | Descrição do logradouro.  Validação: Preenchimento obrigatório e exclusivo se o campo cnpjInstEnsino não estiver preenchido. |
| Grupos {instEnsino}: Campo {nrLograd} alterada descrição e incluída validação. | Número do logradouro. Se não houver número a ser informado, preencher com "S/N". | Número do logradouro. Se não houver número a ser informado, preencher com "S/N". Validação: Preenchimento obrigatório e exclusivo se o campo cnpjInstEnsino não estiver preenchido. |
| Grupos {instEnsino}: Campo {bairro} incluída validação. | Nome do bairro/distrito | Nome do bairro/distrito. Validação: Preenchimento obrigatório e exclusivo se o campo cnpjInstEnsino não estiver preenchido. |
| Grupos {instEnsino}: Campo {cep} alterada validação. | Código de Endereçamento Postal - CEP. Validação: Deve ser preenchido apenas com números. Deve ser um CEP válido. | Código de Endereçamento Postal - CEP. Validação: Não informar se o campo cnpjInstEnsino estiver preenchido. Se informado, deve ser preenchido apenas com números, com 8 (oito) posições. |
| Grupos {instEnsino}: Campo {codMunic} alterada validação. | Preencher com o código do município, conforme tabela do IBGE. Validação: Se informado, deve ser um código existente na tabela do IBGE. | Preencher com o código do município, conforme tabela do IBGE. Validação: Não informar se o campo cnpjInstEnsino estiver preenchido. Se informado, deve ser um código válido e existente na tabela do IBGE. |
| Grupos {instEnsino}: Campo {uf} alterada validação. | Preencher com a sigla da Unidade da Federação. Validação: Deve ser uma UF válida. | Preencher com a sigla da Unidade da Federação - UF. Valores válidos: AC, AL, AP, AM, BA, CE, DF, ES, GO, MA, MT, MS, MG, PA, PB, PR, PE, PI, RJ, RN, RS, RO, RR, SC, SP, SE, TO Validação: Não informar se o campo cnpjInstEnsino estiver preenchido |
| Grupos {ageIntegracao}: Campos {nmRazao}, {dscLograd}, {nrLograd}, {bairro},{cep},{codMunic},{uf} excluídos. |  |  |
| Grupos {supervisorEstagio}: Campo {nmSuperv} excluído. |  |  |

Criação de um campo no cadastro do funcionário.

Acesse**RH | Folha de Pagamento | Administração de Pessoal | Funcionários**

Criado o campo tipo de regime previdenciário (ou sistema de proteção social dos militares).  Para atender ao preenchimento da tag<tpRegPrev> do grupo <infoDiregenteSindical> que se refere a informações relativas ao dirigente sindical.
