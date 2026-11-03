---
content_hash: 4fe8370b3f7b9e5a0427f21840aab61db9cf9cf3a7215150639533de18c6bcc3
fetched_at: '2026-06-29T00:10:53.783911+00:00'
page_id: '585316051'
product: rm
source: tdn-rm
title: Alterações S-1005
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=585316051
version: 41
---

false

**A partir das Versões:**

* 12.1.29.282
* 12.1.31.197
* 12.1.32.135
* e Superiores.

# Objetivo:

---

Apresentar as alterações realizadas no evento S-1005 para o leiaute do eSocial Versão S-1.0.

---

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupos {aliqGiLrat}:Campo {dadosEstab}   alterada ocorrência e condição | ocorrência [1-1] | ocorrência [0-1] |
| Grupos {aliqGiLrat}: Campo {aliqRat}  alteradas ocorrência, descrição e validação | ocorrência [1-1]   Preencher com a alíquota definida na legislação vigente para a atividade (CNAE) preponderante. A divergência só é permitida se existir o registro complementar com informações sobre o processo administrativo/judicial que permite a aplicação de alíquotas diferentes. | ocorrência [0-1]  Informar a alíquota RAT, quando divergente da legislação vigente para a atividade (CNAE) preponderante. A divergência só é permitida se existir o grupo com informações sobre o processo administrativo/judicial que permite a aplicação de alíquota diferente.  Validação Adicionada : Se informada, deve ser diferente da alíquota definida na legislação vigente para a atividade (CNAE) preponderante. (Validação completa em observações RM) |
| Grupos {aliqGiLrat}: Campo {fap}  alterada validação | Tamanho [5]  Validação: Preenchimento obrigatório por Pessoa Jurídica. Não pode ser preenchido por Pessoa Física. O FAP informado deve corresponder àquele definido pelo Órgão Governamental Competente para o estabelecimento, exceto se {ideEstab/tpInsc} = [4]. A divergência só é permitida se houver processo informado em {procAdmJudFap}. Deve ser um número maior ou igual a 0,5000 e menor ou igual a 2,0000. | Tamanho [1-5]  Validação: Preenchimento obrigatório e exclusivo por Pessoa Jurídica e ideEstab/tpInsc = [4], ou se ideEstab/tpInsc = [1] e o fator informado for diferente do definido pelo órgão governamental competente para o estabelecimento (neste caso, deverá haver informações de processo em procAdmJudFap). Se informado, deve ser um número maior ou igual a 0,5000 e menor ou igual a 2,0000 e, se ideEstab/tpInsc = [1], deve ser diferente do valor definido pelo órgão governamental competente. |
| Grupos {aliqGiLrat}: Campo {aliqratAjust} | Alíquota do RAT após ajuste pelo FAP. Validação: Deve corresponder ao resultado da multiplicação dos campos {aliqRat} e {fap}. Preenchimento obrigatório pela Pessoa Jurídica. | Excluido |
| Grupo {infoCaepf} | O (se {tpInsc} = [3]); N (nos demais casos). | O (se ideEstab/tpInsc = [3]); N (nos demais casos). |
| Grupo { infoObra}  Adicionada na Condição | Registro preenchido exclusivamente por empresa construtora, relacionando os estabelecimentos inscritos no CNO, para indicar a substituição ou não da contribuição patronal incidente sobre a remuneração dos trabalhadores de obra de construção civil. | O (se indConstr em S-1000 = [1] e ideEstab/tpInsc = [4]);   N (nos demais casos) |
| Grupo {infoTrab}: Campo regPt | Opção de registro de ponto (jornada) adotada pelo estabelecimento. Indicar o sistema de controle de ponto preponderante, conforme opções: 0 - Não utiliza;  1 - Manual;  2 - Mecânico;  3 - Eletrônico (portaria MTE 1.510/2009);  4 - Não eletrônico alternativo (art. 1° da Portaria MTE 373/2011);  5 - Eletrônico alternativo (art. 2° da Portaria MTE 373/2011);  6 - Eletrônico - outros. O preenchimento deste campo é facultativo. Valores Válidos: 0, 1, 2, 3, 4, 5, 6. 38 | Excluido |
| Grupo { infoApr}: Campo Apr | Indicativo de contratação de aprendiz:  0 - Dispensado de acordo com a lei;  1 - Dispensado, mesmo que parcialmente, em virtude de processo judicial;  2 - Obrigado.  Valores Válidos: 0, 1, 2. | Excluido |
| Grupo {infoApr}: Campo nrProcJud  Alteração Validação | Preencher com o número do processo judicial.  Validação:  O preenchimento é obrigatório se {contApr} for igual a [1]. Deve ser um número de processo judicial válido. | Preencher com o número do processo judicial.  Validação: Se informado, deve ser um número de processo judicial válido. |
| Grupo {infoApr}:  Campo contEntEd | Informar se o estabelecimento realiza a contratação de aprendiz por intermédio de entidade educativa sem fins lucrativos que tenha por objetivo a assistência ao adolescente e à educação profissional (art. 430, inciso II, CLT) ou por entidade de prática desportiva filiada ao Sistema Nacional do Desporto ou a Sistema de Desporto de Estado, do Distrito Federal ou de Município (art. 430, inciso III, CLT): S - Sim; N - Não. Validação: O preenchimento é facultativo se {contApr} for igual a [1, 2]. Não informar se {contApr} for igual a [0]. Valores Válidos: S, N. 42 infoEntEduc infoApr G - 0-99 - - Identificação da(s) entidade(s) educativa(s) ou de prática desportiva | Excluido |
| Grupo {infoEntEduc}:     alterada condição | F (Se {contEntEd} for igual a [S]. N (nas demais situações). | OC |
| Grupo {infoEntEduc}: Campo nrInsc  alterado tamanho e validação | Tamanho[15]  Informar o número de inscrição da entidade educativa ou de prática desportiva. Validação: Deve ser um número de CNPJ válido. | Tamanho[14]  Complemento na validação:  Validação: Deve ser um número de CNPJ válido, com 14 (catorze) algarismos. Se o empregador for pessoa jurídica, a raiz do CNPJ informado deve ser diferente de ideEmpregador/nrInsc. |
| Grupo { ideEmpregador}: Campo nrInsc  alterado tamanho e descrição, e excluída validação | Tamanho [15]  Informar o número de inscrição do contribuinte de acordo com o tipo de inscrição indicado no campo {tpInsc}. Se for um CNPJ deve ser informada apenas a Raiz/Base de oito posições, exceto se natureza jurídica de administração pública direta federal ([101-5], [104-0], [107-4], [116-3], situação em que o campo deve ser preenchido com o CNPJ completo (14 posições). Validação: Se {tpInsc} for igual a [1], deve ser um número de CNPJ válido. Se {tpInsc} for igual a [2], deve ser um CPF válido | Tamanho [14]  Validação Excluída .  Informar o número de inscrição do contribuinte de acordo com o tipo de inscrição indicado no campo ideEmpregador/tpInsc e conforme informado em S-1000. |
| Grupo {procAdmJudFap}: Campo tpProc  alterada descrição do valor [4] | Preencher com o código correspondente ao tipo de processo:  1 - Administrativo;  2 - Judicial;  4 - Processo FAP.  Valores Válidos: 1, 2, 4. | Validação  complemento na descrição do valor[4].  Valores válidos:   1 - Administrativo   2 - Judicial   4 - Processo FAP de exercício anterior a 2019 |
| Grupo {procAdmJudFap}: Campo nrProc  alterada validação | Informar um número de processo cadastrado através do evento S-1070, cujo {indMatProc} seja igual a [1].  Validação: Deve ser um número de processo administrativo ou judicial válido e existente na Tabela de Processos (S-1070). | Complemento na Validação.  Validação: Deve ser um número de processo administrativo ou judicial válido e existente na Tabela de Processos (S1070), com indMatProc = [1]. |
| Grupo {infoPCD}  alterada descrição no registro do evento | Informações sobre a contratação de pessoa com deficiência (PCD). Essa informação deve ser prestada apenas no estabelecimento "Matriz".   Preenchimento obrigatório somente no caso de dispensa, ainda que parcial, de contratação de PCD em virtude de processo judicial.  Preenchimento facultativo nos demais casos. | Informações sobre a contratação de pessoa com deficiência (PCD). Essa informação deve ser prestada apenas no estabelecimento "Matriz".   Preenchimento obrigatório somente no caso de dispensa, ainda que parcial, de contratação de PCD em virtude de processo judicial |
| Grupo {infoPCD}: Campo contPCD |  | Excluido |
| Grupo {infoPCD}: Campo nrProcJud  alterada ocorrência e validação | Ocorrência [0-1]  Informação obrigatória se {contPCD} = [1].  Deve ser um número de processo judicial válido. | Ocorrência [1]. Deve ser um número de processo judicial válido. |
| Grupo {ideEstab}: Campo nrInsc  alterado tamanho, descrição e validação | Tamanho [15] | Tamanho [12 ou 14]. |
| Grupo {ideEvento}:Campo tpAmb  incluídos valores [7, 8, 9] | Identificação do ambiente:  1 - Produção;  2 - Produção restrita.  Valores Válidos: 1, 2. | Identificação do ambiente. Valores válidos: 1 - Produção 2 - Produção restrita 7 - Validação (uso interno) 8 - Teste (uso interno) 9 - Desenvolvimento (uso interno) |
| Grupo {ideEvento}: Campo procEmi  incluídos valores [22, 81, 91], alterada a descrição do valor [2], Excluído valor [5] e o tamanho do campo foi alterado de 1 para 2 | Processo de emissão do evento:  1- Aplicativo do empregador;  2 - Aplicativo governamental - Empregador Doméstico;  3 - Aplicativo governamental - Web Geral;  4 - Aplicativo governamental - Simplificado Pessoa Jurídica;  5 - Aplicativo governamental - Segurado Especial.  Valores Válidos: 1, 2, 3, 4, 5. 7 | Processo de emissão do evento. Valores válidos: 1 - Aplicativo do empregador 2 - Aplicativo governamental - Simplificado Pessoa Física 3 - Aplicativo governamental - Web Geral 4 - Aplicativo governamental - Simplificado Pessoa Jurídica 22 - Aplicativo governamental para dispositivos móveis - Empregador Doméstico 81 - Aplicativo governamental para envio de eventos pelo Judiciário 91 - Aplicativo governamental - Integração com a Junta Comercial  Solicitação enviada ao proprietário. |
