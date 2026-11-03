---
content_hash: cd4227f5f37e0fa752ae6a48eefdd701d0d9c1457f93d5a4817a62942d48031a
fetched_at: '2026-06-29T00:11:44.884302+00:00'
page_id: '817630765'
product: rm
source: tdn-rm
title: Nota Técnica V. S-1.2 01/2023 - Itens 3.3 e 3.4
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=817630765
version: 43
---

false

**A partir das Versões:**

* [DT - eSocial - Nota Técnica S-1.2 Nº 01/2023 - Itens 3.1 e 3.2](https://tdn.totvs.com/pages/viewpage.action?pageId=817630807)
* [DT - eSocial - Nota Técnica S-1.2 Nº 01/2023 - Itens 3.3 e 3.4](https://tdn.totvs.com/pages/viewpage.action?pageId=837872896)

# Objetivo:

---

Adequamos o produto TOTVS Folha de Pagamento para atender ao leiaute S-1.2, conforme as alterações descritas na [Nota Técnica 01/2023](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-s-1-2-01-2023.pdf)[,](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-s-1-1-01-2023.pdf)  do eSocial, publicada em 07/12/2023, referentes aos itens 3.3 e 3.4

11AtualizadorAtualizador

Após a liberação da versão será necessário executar os script's de adequação das tabelas e campos do sistema através do sistema **RM.Atualizador.exe.**

true3 Alterações Eventos Alterações com entrada em produção 04/01/2024 

1) **Tabela 3 - Natureza das Rubricas da Folha de Pagamento**

Descontinuidade do código [] em virtude da criação do código [1012] relativo a DSR e feriado.

| DE | PARA |
| --- | --- |
| 1002 - Descanso Semanal Remunerado - DSR | Incluído término de validade para o código [1002]. Validade: 01/01/2014 a 30/04/2024 |

Ao cadastrar um evento e informar no campo Natureza da Rubrica(eSocial) o código 1002  o sistema apresenta a mensagem abaixo:

2) **Tabela 18 - Motivos de Afastamento**

| DE | PARA |
| --- | --- |
| **26 -** Participação de empregado no Conselho Nacional de Previdência Social - CNPS - Art. 3º da Lei 8.213/1991 | Excluído |
| **28 -** Representante sindical - Afastamento pelo tempo que se fizer necessário, quando, na qualidade de representante de entidade sindical, estiver participando de reunião oficial de organismo internacional do qual o Brasil seja membro | Excluído |

Caso o funcionário já tenha cadastrado na base o código excluído o sistema irá apresentar a mensagem abaixo:

3) **S-1000 - Informações do Empregador/Contribuinte/Órgão Público.**

| TAG | DE | PARA |
| --- | --- | --- |
| dtTrans11096 | Validação: Não preencher se classTrib = [21, 22] | Não preencher se classTrib = [21, 22]. Se informada, deve ser maior que [2005-11-21] e menor ou igual à data atual |

4) **S-1200 - Remuneração de Trabalhador vinculado ao Regime Geral de Previd. Social**

| TAG | DE | PARA |
| --- | --- | --- |
| tpAcConv | Validação: Se classTrib em S-1000 = [04, 22], não pode ser informado [E, H]. | Validação: Se classTrib em S-1000 = [04, 22], não pode ser informado [E, H, I]. |
| ideAdv | Identificação dos advogados - OC | O (se vlrDespAdvogados > 0); N (nos demais casos) |
| dia | Validação: Deve ser um número entre 0 e 31, de acordo com o calendário anual | Deve ser um número entre 0 e 31, de acordo com o calendário anual. |

Agora passa a apresentar uma mensagem de aviso no log do XML

**Exemplo:**

Ao gerar o evento o sistema irá apresentar uma mensagem de aviso no log do XML caso a tag (dia) não atenda a validação.

**Avisos evento S1200 / ID: ID1218673870000002024040817540400000:**

**Aviso: validação do campo 'dia': O dia deve ser um número entre 0 e 31, de acordo com o calendário anual.**

5) **S-2299 - Desligamento**

| TAG | DE | PARA |
| --- | --- | --- |
| tpAcConv | Validação: Se classTrib em S-1000 = [04, 22], não pode ser informado [E, H]. | Validação: Se classTrib em S-1000 = [04, 22], não pode ser informado [E, H, I]. |
| dia | Validação: Deve ser um número entre 0 e 31, de acordo com o calendário anual | Deve ser um número entre 0 e 31, de acordo com o calendário anual.   Agora passar a apresentar uma mensagem de aviso no log do XML |

6) **S-2200 - Cadastramento Inicial do Vinculo e admissão/Ingresso de trabalhador**

| TAG | DE | PARA |
| --- | --- | --- |
| tpContr | Não tinha validação | Validação: Se codCateg = [103] e dtAdm >= [2024-04-22], deve ser informado [2]. |
| racaCor | Validação: Se dtAlteracao for igual ou posterior a [2023-07-01], retornar alerta caso seja informado o valor [6]. | Validação: Se dtAdm, dtExercicio, sucessaoVinc/dtTransf ou transfDom/dtTransf (maior data entre elas) for igual ou posterior a [2024-04-22], não pode ser informado o valor [6]. |
| tpProv | Validação:Os valores [3, 5, 6, 7, 8, 9] só são permitidos se a natureza jurídica do declarante for Administração Pública (grupo [1]).Se codCateg = [302], deve ser preenchido com [2, 5, 8, 10]. | Validação:Os valores [3, 5, 6, 8, 9] só são permitidos se a natureza jurídica do declarante for Administração Pública (grupo [1]).Se codCateg = [302], deve ser preenchido com [2, 5, 8,10] |

7) **S-2190 - Registro Preliminar de Trabalhador**

| TAG | DE | PARA |
| --- | --- | --- |
| tpContr | Não tinha validação | Validação: Se codCateg = [103] e dtAdm >= [2024-04-22], deve ser informado [2]. |

8) **S-2206 - Trabalhador Sem Vínculo de Emprego/Estatutário -Alteração Contratual**

Exigir que o contrato de aprendiz seja por prazo determinado, definido em dias.

| TAG | DE | PARA |
| --- | --- | --- |
| tpContr | Não tinha validação | Validação: Se codCateg = [103] e dtAdm >= [2024-04-22], deve ser informado [2]. |

9) **S-2240 - Condições Ambientais do Trabalho-Agentes Nocivos**

Não permitir o preenchimento do campo se {codAgNoc} = [09.01.001].

| TAG | DE | PARA |
| --- | --- | --- |
| dscAgNoc | Descrição do agente nocivo. Validação: Preenchimento obrigatório se codAgNoc = [01.01.001, 01.02.001, 01.03.001, 01.04.001, 01.05.001, 01.06.001, 01.07.001, 01.08.001, 01.09.001, 01.10.001, 01.12.001, 01.13.001, 01.14.001, 01.15.001, 01.16.001, 01.17.001, 01.18.001, 05.01.001]. | Descrição do agente nocivo. Validação: Preenchimento obrigatório se codAgNoc = [01.01.001, 01.02.001, 01.03.001, 01.04.001, 01.05.001, 01.06.001, 01.07.001, 01.08.001, 01.09.001, 01.10.001, 01.12.001, 01.13.001, 01.14.001, 01.15.001, 01.16.001, 01.17.001, 01.18.001, 05.01.001]. Não informar se codAgNoc = [09.01.001] e dtIniCondicao >= [2024-04-22]. |

 10) **S-2205 - Alteração de Dados Cadastrais do Trabalhador**

| TAG | DE | PARA |
| --- | --- | --- |
| racaCor | Validação: Se dtAlteracao for igual ou posterior a [2023- 07-01], retornar alerta caso seja informado o valor [6]. | Se dtAdm, dtExercicio, sucessaoVinc/dtTransf ou transfDom/dtTransf (maior data entre elas) for igual ou posterior a [2024-04-22], não pode ser informado o valor [6]. |

11) **S-2300-Trabalhador Sem Vínculo de Emprego/Estatutário -Início Tabela de Resumo dos Registro**

| TAG | DE | PARA |
| --- | --- | --- |
| racaCor | Validação: Se dtInicio for igual ou posterior a [2023- 07-01], retornar alerta caso seja informado o valor [6]. | Se dtAdm, dtExercicio, sucessaoVinc/dtTransf ou transfDom/dtTransf (maior data entre elas) for igual ou posterior a [2024-04-22], não pode ser informado o valor [6]. |

12)  **S-2400 - Cadastro de Beneficiário - Entes Públicos - Início**

| TAG | DE | PARA |
| --- | --- | --- |
| racaCor | Validação: Se dtInicio for igual ou posterior a [2023- 07-01], retornar alerta caso seja informado o valor [6]. | Se dtAdm, dtExercicio, sucessaoVinc/dtTransf ou transfDom/dtTransf (maior data entre elas) for igual ou posterior a [2024-04-22], não pode ser informado o valor [6]. |

13)  **S-2405 - Cadastro de Beneficiário - Entes Públicos - Início**

| TAG | DE | PARA |
| --- | --- | --- |
| racaCor | Validação: Se dtInicio for igual ou posterior a [2023- 07-01], retornar alerta caso seja informado o valor [6]. | Se dtAdm, dtExercicio, sucessaoVinc/dtTransf ou transfDom/dtTransf (maior data entre elas) for igual ou posterior a [2024-04-22], não pode ser informado o valor [6]. |

14) **S-2500 - Processo Trabalhista**

| TAG | DE | PARA |
| --- | --- | --- |
| ideResp | OC | O (se infoContr/tpContr = [8]); N (nos demais casos) |

 Não houve necessidade de criação de um novo leiaute para tratar a Nota Técnica
