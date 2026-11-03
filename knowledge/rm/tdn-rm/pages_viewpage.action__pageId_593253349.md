---
content_hash: bbf839f7ca2cd4a7cab6b49d4d4391a79eb3fd0455621f10214679ae3c1cf044
fetched_at: '2026-06-29T00:10:56.865216+00:00'
page_id: '593253349'
product: rm
source: tdn-rm
title: Alterações S-2299
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=593253349
version: 19
---

false

**A partir das Versões:**

* 12.1.29.282
* 12.1.31.197
* 12.1.32.135
* e Superiores.

# Objetivo:

---

Apresentar as alterações realizadas no evento S-2299  para o leiaute do eSocial Versão S-1.0.

---

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupos {ideEvento }Campo: indGuia  Inclusão de campo |  | Novo Campo E | N | 0-1 | 1 Descrição:Indicativo do tipo de guia.  Valores válidos:  1 - Documento de Arrecadação do eSocial - DAE |
| Grupos {ideEvento}: Campo {procEmi }   Incluido e excluidos valores  Alterado descrição  Alterado tamanho | Tamanho :1-1  Processo de emissão do evento:  1- Aplicativo do empregador;  2 - Aplicativo governamental - Empregador Doméstico;  3 - Aplicativo governamental - Web Geral;  4 - Aplicativo governamental - Simplificado Pessoa Jurídica;  5 - Aplicativo governamental - Segurado Especial.  Valores Válidos: 1, 2, 3, 4, 5. | Tamanho :1-2  Processo de emissão do evento. Valores válidos: 1 - Aplicativo do empregador 2 - Aplicativo governamental - Simplificado Pessoa Física 3 - Aplicativo governamental - Web Geral 4 - Aplicativo governamental - Simplificado Pessoa Jurídica 22 - Aplicativo governamental para dispositivos móveis - Empregador Doméstico 81 - Aplicativo governamental para envio de eventos pelo Judiciário 91 - Aplicativo governamental - Integração com a Junta Comercial |
| Grupos {ideEmpregador }: Campo {nrInsc }  alterados tamanho e descrição, e excluída validação | Tamanho De [15]  Validação Excluída Descriçao DE: Informar o número de inscrição do contribuinte de acordo com o tipo de inscrição indicado no campo {tpInsc}. Se for um CNPJ deve ser informada apenas a Raiz/Base de oito posições, exceto se natureza jurídica de administração pública direta federal ([101-5], [104-0], [107-4], [116-3], situação em que o campo deve ser preenchido com o CNPJ completo (14 posições). | Tamanho [8,11 ou 14].  Informar o número de inscrição do contribuinte de acordo com o tipo de inscrição indicado no campo ideEmpregador/tpInsc e conforme informado em S-1000. |
| Grupos {ideVinculo}: Campo {nisTrab} |  | Excluido |
| Grupos {infoDeslig}: Campo {mtvDeslig}   Alteração na validação | Deve ser um código existente na tabela. Os códigos [19,20,21,22,23,24,25] só podem ser utilizados para desligamento de trabalhador pertencente à categoria de agente público (301 a 309). O código [34] só pode ser utilizado para desligamento de trabalhador doméstico (código de categoria [104]). | Deve ser um código válido e existente na Tabela 19, bem como compatível com o código de categoria do trabalhador, conforme Tabela 19. |
| Grupos {infoDeslig}: Campo {dtDeslig}   Alteração na validação | Deve ser uma data igual ou posterior a data de admissão do trabalhador (no caso de sucessão ou de mudança de CPF, igual ou posterior à data da transferência ou à data de alteração do CPF, respectivamente) e não superior à data atual (data do envio do evento) acrescida de 10 dias corridos. | Deve ser uma data igual ou anterior à data atual acrescida de 10 (dez) dias. No caso de empregado reintegrado, também deve ser uma data igual ou posterior a dtEfetRetorno do evento S-2298. |
| Grupos {infoDeslig}: Campo {dtAvPrev}  Novo campo |  | Descrição: Data de concessão do aviso prévio. .  Validação Se informada, deve ser igual ou posterior à data de admissão e igual ou anterior a dtDeslig. |
| Grupos {infoDeslig}: Campo {pensAlim}  Alterada Validação | Indicativo de pensão alimentícia para fins de retenção de FGTS:  0 - Não existe pensão alimentícia;  1 - Percentual de pensão alimentícia;  2 - Valor de pensão alimentícia;  3 - Percentual e valor de pensão alimentícia.  Valores Válidos: 0, 1, 2, 3. | Indicativo de pensão alimentícia para fins de retenção de FGTS.  Valores válidos:  0 - Não existe pensão alimentícia  1 - Percentual de pensão alimentícia  2 - Valor de pensão alimentícia  3 - Percentual e valor de pensão alimentícia  Validação: Preenchimento obrigatório e exclusivo se o vínculo for celetista (tpRegTrab em S-2200 = [1]). |
| Grupos {infoDeslig}: Campo {vrAlim}  Alterada Validação | Valor da pensão alimentícia.  Validação: Informação obrigatória se {pensAlim} = [2,3]. Não pode ser preenchido nos demais casos. | Valor da pensão alimentícia.  Validação: Deve ser maior que 0 (zero). Informação obrigatória e exclusiva se pensAlim = [2, 3]. |
| Grupos {infoDeslig}: Campo {nrCertObito}  Campo Excluido |  | Excluido |
| Grupos {infoDeslig}: Campo {indCumprParc}  Campo Excluido |  | Excluido |
| Grupos {infoDeslig}: Campo {qtdDiasInterm}  Campo Excluido |  | Excluido |
| Grupos {infoInterm}: Campo { dia}  Novo Grupo |  | Descrição: Informações relativas ao trabalho intermitente.|Tamanho: 0-31 | Chave: Dia  Condição: O (se o código de categoria no RET for igual a [111] no mês/ano de dtDeslig; N (nos demais casos)Dia do mês efetivamente trabalhado pelo empregado com contrato de trabalho intermitente. Validação: Deve ser um número entre 1 e 31, de acordo com o calendário anual. |
| Grupos {sucessaoVinc }: Campo {tpInscSuc}  Alteração no nome do campo | [tpInscSuc] | [tpInsc] |
| Grupos {sucessaoVinc }: Campo {cnpjSucessora}  Alteração no nome do campo. Tamanho | Alteração nome campo [cnpjSucessora].  Tamanho de: 14   Validação:  Deve ser um número de inscrição válido diferente da inscrição do declarante, considerando as particularidades aplicadas à informação de CNPJ de órgão público em S-1000. Se {tpInscSuc} = [1], deve possuir 14 (catorze) algarismos e ser diferente do CNPJ base do empregador e dos estabelecimentos informados através do evento S-1005. Se {tpInscSuc} = [2], deve possuir 11 (onze) algarismos | Alteração nome campo[nrInsc]  Tamanho de:11 ou 14  Validação:  Deve ser um número de inscrição válido e diferente da inscrição do declarante, considerando as particularidades aplicadas à informação de CNPJ de órgão público em S-1000. Se sucessaoVinc/tpInsc = [1], deve possuir 14 (catorze) algarismos e ser diferente do CNPJ base do empregador (exceto se ideEmpregador/nrInsc tiver 14 (catorze) algarismos) e dos estabelecimentos informados através do evento S-1005. Se sucessaoVinc/tpInsc = [2], deve possuir 11 (onze) algarismos |
| Grupos {ideEstabLot }: Campo {tpInsc } | Preencher com o código correspondente ao tipo de inscrição do estabelecimento, de acordo com as opções da Tabela 05.  Validação:  Se {classTrib} igual a [21], deve ser igual a [3,4], exceto se empregador doméstico. Se {classTrib} igual a [22], caso não seja empregador doméstico, deve ser igual a [3, 4] e, se for igual a [3], o CAEPF deve constar na tabela S-1005 como sendo de segurado especial. Se empregador doméstico (trabalhador com {codCateg} = [104]), deve ser igual a [2]. Nos demais casos ({classTrib} <> [21,22]), deve ser igual a [1,4]. Valores Válidos: 1, 2, 3, 4 | Preencher com o código correspondente ao tipo de inscrição do estabelecimento, de acordo com as opções da Tabela 05. Valores válidos: 1 - CNPJ  3 - CAEPF  4 - CNO  Validação:  Se classTrib em S-1000 = [21], deve ser igual a [3, 4]. Se classTrib em S-1000 = [22], deve ser igual a [3, 4] e, se for igual a [3] e não se tratar de empregado doméstico, o CAEPF deve constar na Tabela S-1005 como sendo de segurado especial. Nos demais casos (classTrib em S-1000 diferente de [21, 22]), deve ser igual a [1, 4]. |
| Grupos {ideEstabLot }: Campo {nrInsc }  Alterações tamanho,descrição,validação | Tamanho:[15]   Descrição:  Informar o número de inscrição do contribuinte de acordo com o tipo de inscrição indicado no campo {tpInsc}  Validação: De: A inscrição informada deve ser compatível com {tpInsc}. Se {tpInsc} igual a [1, 3, 4] deve constar na tabela S-1005. Para: A inscrição informada deve ser compatível com ideEstabLot/tpInsc | Tamanho :[12 ou 14]  Descrição: Informar o número de inscrição do estabelecimento do contribuinte de acordo com o tipo de inscrição indicado no campo ideEstabLot/tpInsc    Validação: A inscrição informada deve ser compatível com ideEstabLot/tpInsc |
| Grupos {detVerbas }: Campo {qtdRubr}  Alterações Tamanho,descrição ,validação | Tamanho:[6]   Alteração na Descrição  De: Informar a quantidade de referência para apuração (em horas, cotas, meses, percentual, etc.). Exs.: Quantidade de horas extras trabalhadas relacionada com uma rubrica de hora extra, quantidade de dias trabalhados relacionada com uma rubrica de salário. etc. | Tamanho: [1-12]   Descrição  Informar a quantidade de referência para apuração (em horas, cotas, meses, etc.). Ex.: Quantidade de horas extras trabalhadas relacionada com uma rubrica de hora extra, quantidade de dias trabalhados relacionada com uma rubrica de salário, etc. Preenchimento obrigatório quando se tratar de rubrica relativa a faltas ou Descanso Semanal Remunerado - DSR sobre faltas (nesse caso, informar a quantidade de dias).  Nova Validação: Deve ser maior que 0 (zero). Informação obrigatória se codRubr tiver natRubr em S-1010 igual a [9207, 9211]. |
| Grupos {detVerbas }: Campo {fatorRubr} | Informar o fator, percentual, etc, da rubrica, quando necessário. Ex: Adicional de Horas Extras 50%, relacionado a uma rubrica de horas extras: Fator = 50. | Informar o fator, percentual, etc. da rubrica, quando necessário. Ex.: Adicional de horas extras 50%, relacionado a uma rubrica de horas extras: Fator = 50.  Validação: Deve ser maior que 0 (zero). |
| Grupos {detVerbas }: Campo {vrUnit} |  | Excluido |
| Grupos {detVerbas }: Campo {indApurIR}  Novo Campo |  | Indicativo de tipo de apuração de IR. Valores válidos: 0 - Normal (apuração sob a folha de pagamento declarada no eSocial) 1 - Situação especial de apuração de IR Validação: Informação obrigatória e exclusiva se mês/ano de dtDeslig >= [2021-05]. |
| Grupo infoSaudeColet: excluido   SubGrupo excluido |  | Grupo excluído. Subgrupo excluído: detOper  Campos excluídos: [cnpjOper,regANS,vrPgTit ] Subgrupo excluído: detPlano  Campos excluídos: [tpDep,cpfDep,nmDep,dtNascto,vlrPgDep] |
| Grupo infoAgNocivo | Descrição Alterada Registro preenchido exclusivamente em relação a remuneração de trabalhador amparado pelo RGPS - Regime Geral de Previdência Social. | Chave Removida. [grauExp ]  Descrição Alterada Grupo referente ao detalhamento do grau de exposição do trabalhador aos agentes nocivos que ensejam a cobrança da contribuição adicional para financiamento dos benefícios de aposentadoria especial. |
| Grupos {ideADC}: Campo {compAcConv} |  | Excluido |
| Grupos {ideADC}: Campo {dtEfAcConv} |  | Excluido |
| Grupos {infoTrabInterm}: Campo { codConv} |  | Grupo excluído. Campo excluído: codConv |
| Grupos procJudTrab }: Campo { tpTrib } | 1 - IRRF; 2 - Contribuições sociais do trabalhador; 3 - FGTS; 4 - Contribuição sindical. | Excluídos valores [3, 4]. 1 - IRRF 2 - Contribuições sociais do trabalhador |
| Grupos procJudTrab }: Campo { nrProcJud  }  Alterada descrição e Validação | Descrição Alterada  De: Informar um número de processo judicial cadastrado através do evento S-1070, cujo {indMatProc} seja igual a: - [1] se {tpTrib} = [1, 2]; - [1, 7] se {tpTrib} = [3]; - [8] se {tpTrib} = [4].  Validação Alterada De: O processo deve existir na tabela de processos | Informar um número de processo judicial cadastrado através do evento S-1070, cujo indMatProc seja igual a [1].  Deve ser um número de processo judicial válido e existente na Tabela de Processos (S-1070), com indMatProc = [1]. |
| Grupos {procJudTrab}: Campo { codSusp }  Alterado Ocorrência e Validação | Ocorrência:[0-1]   Validação:  Preenchimento obrigatório se {tpTrib} = [1, 2]. A informação prestada deve estar de acordo com o que foi informado em S-1070. | Ocorrência:[1-1]   Validação:  A informação prestada deve estar de acordo com o que foi informado em S-1070 |
