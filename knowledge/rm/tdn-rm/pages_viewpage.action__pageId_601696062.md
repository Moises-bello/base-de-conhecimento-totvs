---
content_hash: 7c079728d9034823706f9a00f61c90ea6269e678374dcf9174081c29d44b8681
fetched_at: '2026-06-29T00:10:57.967791+00:00'
page_id: '601696062'
product: rm
source: tdn-rm
title: Alterações S-1200
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=601696062
version: 3
---

false

**A partir das Versões:**

* 12.1.29.282
* 12.1.31.197
* 12.1.32.135
* e Superiores.

# Objetivo:

---

Apresentar as alterações realizadas no evento S-1200 para o leiaute do eSocial Versão S-1.0.

---

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupos {**ideEvento**}: Campo {**nrRecibo**}  Alterado tamanho | De: 40 | Para: 23 |
| Grupos {**ideEvento**}: Campo      **{evtRemun}**           Alterado Chave |  | Para: {indApuracao} , {perApur} e {indguia} |
| Grupos{**ideEvento**}: Campo     **{IndGuia}**          Incluído campo |  | Indicativo do tipo de guia. **Valores válidos:** **1** - Documento de Arrecadação do eSocial - DAE |
| Grupo {**ideEvento**}: Campo     **{tpAmb}**         Incluído Valores | DE: 1 - Produção;        2 - Produção restrita. | Identificação do ambiente. Valores válidos: 1 - Produção 2 - Produção restrita 7 - Validação (uso interno) 8 - Teste (uso interno) 9 - Desenvolvimento (uso interno) |
| Grupo {**ideEvento**}: Campo     **{procEmi}**      Incluído Valores , Alterado        descrição e excluído campo | 1- Aplicativo do empregador;  2 - Aplicativo governamental - Empregador Doméstico;  3 - Aplicativo governamental - Web Geral;  4 - Aplicativo governamental - Simplificado Pessoa Jurídica;  5 - Aplicativo governamental - Segurado Especial. | 1 - Aplicativo do empregador 2 - Aplicativo governamental - Simplificado Pessoa Física 3 - Aplicativo governamental - Web Geral 4 - Aplicativo governamental - Simplificado Pessoa Jurídica 22 - Aplicativo governamental para dispositivos móveis - Empregador Doméstico 81 - Aplicativo governamental para envio de eventos pelo Judiciário 91 - Aplicativo governamental - Integração com a Junta Comercial |
| Grupo {**ideEmpregador**}:    Campo**{nrInsc}**      Alterado Tamanho | De: 15 | Para: 8,11 ou 14 |
| Grupo {**ideTrabalhador**}:     Campo**{nisTrab}**         Campo Excluído |  | Campo Excluído |
| Grupo {**sucessaoVinc**}:     Campo**{tpinsc}**   Alterado o Nome do Campo | DE: tpInscAnt | Para:{tpinsc} |
| Grupo {**sucessaoVinc**}:     Campo**{nrinsc}**   Alterado o Nome do Campo | DE:cnpjEmpregAnt | Para:{nrinsc} |
| Grupo {**procJudTrab**}:     Campo**{tpTrib}**  Alterado a Validação | De: 1 - IRRF;        2 - Contribuições sociais do        trabalhador;        3 - FGTS;       4 - Contribuição sindical | Para:1 - IRRF         2 - Contribuições sociais do trabalhador |
| Grupo {**procJudTrab**}:     Campo**{codSusp}**     Alterado a Validação | De: Preenchimento obrigatório se {tpTrib} = [1, 2]. A informação prestada deve estar de acordo com o que foi informado em S1070. | Para :A informação prestada deve estar de acordo com o que foi informado em S-1070. |
| Grupo {**infointerm**}:     Campo**{dia}**     Alterado o nome do Campo | DE: qtdDiasInterm | Para: {dia} |
| Grupo {**remunPerApur**}:     Campo**{matricula}**     Alterado a Validação | DE: Informação obrigatória para trabalhadores das categorias "empregados" e "agentes públicos". Deve corresponder à matrícula informada pelo empregador no evento S-2200 do respectivo vínculo trabalhista. | Para:Deve corresponder à matrícula informada pelo empregador no evento S-2190, S-2200 ou S-2300 do respectivo contrato. Não preencher no caso de Trabalhador Sem Vínculo de Emprego/Estatutário - TSVE sem informação de matrícula no evento S-2300. |
| Grupo {**remunPerApur**}:     Campo**{codRubr}**     Alterado a Validação | DE:O código informado deve existir na tabela S-1010 - Tabela de Rubricas, vigente no período indicado em: a) {perApur} se vinculado a {remunPerApur};  b) {perRef} se vinculado a {remunPerAnt}. Não pode ser utilizada rubrica: a) cujo {codIncCP} em S-1010 seja igual a [23, 24, 61]; b) cujo {codIncIRRF} em S-1010 seja igual a [31, 32, 33, 34, 35, 51, 52, 53, 54, 55, 81, 82, 83]; c) cujo {codIncCp} em S-1010 seja igual a [25, 26, 51] se {codCateg} pertencer a um dos grupos 'contribuinte individual' ou 'bolsistas' da Tabela 01 (Categoria de Trabalhadores). | Para: Não pode ser utilizada rubrica: a) cujo codIncCP em S-1010 seja igual a [25, 26, 51] se codCateg pertencer ao grupo "Contribuinte Individual" ou "Bolsista" da Tabela 01; b) cuja natRubr em S-1010 seja igual a [1801, 9209, 9210, 9220], desde que perApur >= [2021-05] (se indApuracao = [1]) ou perApur >= [2021] (se indApuracao = [2]). |
| Grupo {**remunPerApur**}:     Campo**{qtdRubr}**     Alterado a Validação | DE: Informar a quantidade de referência para apuração (em horas, cotas, meses, percentual, etc.). | Para: Deve ser maior que 0 (zero). Informação obrigatória se codRubr tiver natRubr em S-1010 igual a [9207, 9211]. |
| Grupo {**remunPerApur**}:    Campo**{vrUnit}**    Campo Excluído |  | Excluído |
| Grupo {**remunPerApur**}:    Campo**{indApurIR}**    Campo Incluído |  | Para :Indicativo de tipo de apuração de IR. Valores válidos: 0 - Normal (apuração sob a folha de pagamento declarada no eSocial) 1 - Situação especial de apuração de IR Validação: Informação obrigatória e exclusiva se perApur >= [2021-05] (se indApuracao = [1]) ou se perApur >= [2021] (se indApuracao = [2]). |
| Grupo {**remunPerApur**}:    Campo**{InfoTrabInterm}**    Campo Excluído |  | Campo Excluído |
| Grupo {i**nfoSaudeColet**}:   Grupo Excluído |  | Grupo Excluído |
| Grupo **{ideADC}**:     Campo:  **{compAcConv}**    Campo Excluído |  | Campo Excluído |
| Grupo **{ideADC}**:     Campo:  **{dtEfAcConv}**  Campo Excluído |  | Campo Excluído |
| Grupo **{InfoperAnt}**:     Campo:  **{Matricula}**  Alterado Validação | DE: Informação obrigatória para trabalhadores das categorias "empregados" e "agentes públicos", desde que {remunSuc} = [N]. Deve corresponder à matrícula informada pelo empregador no evento S-2200 do respectivo vínculo trabalhista. Não informar se {remunSuc} = [S]. | Para: Deve corresponder à matrícula informada pelo empregador no evento S-2190, S-2200 ou S-2300 do respectivo contrato. Não preencher no caso de TSVE sem informação de matrícula no evento S-2300 ou se [remunSuc](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-nt-01-2021-html/index.html/#1200_dmDev_infoPerAnt_ideADC_remunSuc) = [S]. |
| Grupo **{remunPerAnt}**:     Campo:  **{codConv/infoTrabInterm}**  Excluído |  | Campo Excluído |
| Grupo **{InfoComplCont}**:  Alterada Obrigatoriedade do Grupo | DE: O ((se {codCateg} <> [101,102, 103, 104, 105, 106, 107, 108, 111, 301, 302, 303, 306, 307, 309]) E (se para o trabalhador não houver evento S-2300 ativo)); N (nos demais casos). | Para: O ((se codCateg = [2XX, 304, 305, 4XX, 7XX, 902]) E (se para o trabalhador não houver evento S-2300 ativo) E (se não for informado remunPerApur/matricula ou remunPerAnt/matricula)); OC ((se codCateg = [901, 903, 904]) E (se para o trabalhador não houver evento S-2300 ativo) E (se não for informado remunPerApur/matricula ou remunPerAnt/matricula)); N (nos demais casos) |
| Grupo **{InfoComplCont}**:     Campo:  **{natAtividade}**  Alterado Validação | DE:  Natureza da atividade, conforme opções abaixo: 1 - Trabalho Urbano; 2 - Trabalho Rural. Validação: O campo deve ser preenchido apenas se atendida uma das condições a seguir apresentadas: a) a classificação tributária for igual a [06, 07, 08]; b) a classificação tributária for igual a [21,22] e existir remuneração para o trabalhador vinculada a um tipo de CAEPF informado em S-1005 como produtor rural ou segurado especial. Valores Válidos: 1, 2. | Para  Valores válidos: 1 - Trabalho urbano 2 - Trabalho rural Validação: O campo deve ser preenchido apenas se atendida uma das condições a seguir apresentadas: a) classTrib em S-1000 = [06, 07]; b) classTrib em S-1000 = [21, 22] e existir remuneração para o trabalhador vinculada a um tipo de CAEPF informado em S-1005 como produtor rural ou segurado especial. |
| Grupo **{InfoComplCont}**:     Campo:  **{qtDiasTrab}**  Alterado Validação | DE :  Informação prestada exclusivamente pelo Segurado Especial em caso de contratação de Contribuinte Individual, indicando a quantidade de dias trabalhados pelo mesmo. Validação: Só pode ser preenchido se {classTrib} = [22] e exista remuneração exclusivamente na categoria [701]. Neste caso, preencher com um número entre 1 e 31. | Para  Informação prestada exclusivamente pelo segurado especial em caso de contratação de contribuinte individual, indicando a quantidade de dias trabalhados pelo mesmo. Validação: Preenchimento obrigatório e exclusivo se classTrib em S-1000 = [22], natAtividade = [2] e indApuracao = [1]. Neste caso, preencher com um número entre 1 e 31, de acordo com o calendário anual. |
