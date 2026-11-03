---
content_hash: f78ffa0406567f30f5e3af8d85290fd8d961d2810b627f48d7c9c7807e694cc4
fetched_at: '2026-06-29T00:10:58.209087+00:00'
page_id: '604509965'
product: rm
source: tdn-rm
title: Alterações S-2206
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=604509965
version: 10
---

false

**A partir das Versões:**

* 12.1.29.282
* 12.1.31.197
* 12.1.32.135
* e Superiores.

# Objetivo:

---

Apresentar as alterações realizadas no evento S-2206 para o leiaute do eSocial Versão S-1.0.

---

| **GRUPO/CAMPO/ITEM** | **DE** | **PARA** |
| --- | --- | --- |
| Grupos {evtAltContratual}  Alterada descrição | Evento Alteração Contratual | Evento Alteração de Contrato de Trabalho/Relação Estatutária |
| Grupos {ideEvento}: Campos{nrRecibo}   Alterado Tamanho | Tamanho :40 | Tamanho:23 |
| Grupos {ideEvento}: Campos{tpAmb}   Incluídos valores [7, 8, 9] |  | Identificação do ambiente. Valores válidos: 1 - Produção 2 - Produção restrita 7 - Validação (uso interno) 8 - Teste (uso interno) 9 - Desenvolvimento (uso interno) |
| Grupos {ideEvento}: Campos{procEmi}   Incluídos valores [22, 81, 91], Alterada a descrição do valor [2],  Excluído valor [5]   Tamanho do campo foi alterado de 1 para 2 |  | Processo de emissão do evento. Valores válidos: 1 - Aplicativo do empregador 2 - Aplicativo governamental - Simplificado Pessoa Física 3 - Aplicativo governamental - Web Geral 4 - Aplicativo governamental - Simplificado Pessoa Jurídica 22 - Aplicativo governamental para dispositivos móveis - Empregador Doméstico 81 - Aplicativo governamental para envio de eventos pelo Judiciário 91 - Aplicativo governamental - Integração com a Junta Comercial |
| Grupos {ideEmpregador}: Campos{procEmi}   Alterados tamanho e descrição, e excluída validação | Tamanho:15  Informar o número de inscrição do contribuinte de acordo com o tipo de inscrição indicado no campo {tpInsc}. Se for um CNPJ deve ser informada apenas a Raiz/Base de oito posições, exceto se natureza jurídica de administração pública direta federal ([101-5], [104-0], [107-4], [116-3], situação em que o campo deve ser preenchido com o CNPJ completo (14 posições). Validação: Se {tpInsc} for igual a [1], deve ser um número de CNPJ válido. Se {tpInsc} for igual a [2], deve ser um CPF válido. | Tamanho: 8, 11 ou 14 Informar o número de inscrição do contribuinte de acordo com o tipo de inscrição indicado no campo ideEmpregador/tpInsc e conforme informado em S-1000. |
| Grupos {ideVinculo}: Campos{nisTrab} |  | Campo excluido |
| Grupos {altContratual}: Campos{dtAlteracao} | Deve ser uma data válida | Não pode ser posterior a 180 (cento e oitenta) dias da data atual. |
| Grupos {vinculo}: Campos{tpRegPrev}   Alterada a descrição | Tipo de regime previdenciário conforme opções abaixo: 1 - Regime Geral da Previdência Social - RGPS; 2 - Regime Próprio de Previdência Social - RPPS; 3 - Regime de Previdência Social no Exterior. | Tipo de regime previdenciário (ou Sistema de Proteção Social dos Militares) 1 - Regime Geral de Previdência Social - RGPS 2 - Regime Próprio de Previdência Social - RPPS ou Sistema de Proteção Social dos Militares 3 - Regime de Previdência Social no exterior |
| Grupos {infoRegimeTrab}:   Alterados grupo pai e nível | Hierarquia: Subgrupo de altContratual ARA: Subgrupo de vinculo.  Nível:4 | Hierarquia: Subgrupo de vinculo.    Nível:5 |
| Grupos {infoCeletista}:  Alterado Nivel | Nível: 5 | Nivel:6 |
| Grupos {trabTemp}:   Criado o grupo {trabTemporario} e respectivo campo. |  | Excluído o grupo {trabTemp} e respectivo campo justProrr |
| Grupos {trabTemporario}: Campos{tpRegPrev} |  | Renomeado de trabTemp para trabTemporario |
| Grupos {aprend}:  Alterado nível | Nível:6 | Nível:7 |
| Grupos {aprend}: Campos{nrInsc}   Alterados tamanho, descrição e validação | Tamanho:15   Descrição :Informar o número de inscrição do empregador para o qual a contratação de aprendiz foi efetivada, de acordo com o tipo de inscrição indicado no campo {tpInsc}.  Validação  Se {tpInsc} for igual a [1], deve ser um número de CNPJ válido. Se {tpInsc} for igual a [2], deve ser um CPF válido. | Tamanho:11 ou 14    Descrição:Informar o número de inscrição do estabelecimento para o qual a contratação de aprendiz foi efetivada, de acordo com o tipo de inscrição indicado no campo aprend/tpInsc  Validação: Deve ser um identificador válido e: a) Se aprend/tpInsc = [1], deve ser informado com 14 (catorze) algarismos. Se o empregador for pessoa jurídica, a raiz do CNPJ informado deve ser diferente de ideEmpregador/nrInsc. b) Se aprend/tpInsc = [2], deve ser diferente do CPF do empregado. Se o empregador for pessoa física, também deve ser diferente do CPF do empregador. |
| Grupos {infoContrato}: Campos {codCargo}  Campo excluído |  | Campo excluido |
| Grupos {infoContrato}: Campos {nmCargo}   Nome do cargo |  | Campo novo para tratar Gatilho |
| Grupos {infoContrato}: Campos {CBOCargo}  Criado o campo {CBOCargo} – Classificação Brasileira de Ocupações - CBO relativa ao cargo |  | Campo novo tratar Gatilho |
| Grupos {infoContrato}: Campos {codfuncao} |  | Campo {codFuncao} – excluído |
| Campo {remuneraçao}   Alterados nível, ocorrência e condição. | Nível: 5   Ocorrência : 1-1   Condição: O | Nivel:6  Ocorrência:0-1  Condição: O (se tpRegTrab em S-2200 = [1]); N (nos demais casos) |
| Campo {duracao}   Alterados nível, ocorrência e condição. | Nível :5   Ocorrência: 1-1   Condição: O | Nivel:6  Ocorrência: 0-1  Condição : O (se tpRegTrab em S-2200 = [1]); N (nos demais casos) |
| Grupos {localTrabalho}:   Alterado nível | Nível: 5 | Nível:6 |
| Grupos {localTrabGeral}:   Alterados nível e condição. | Nível : 6   Condição: O (se categoria do trabalhador for diferente de [104, 106]); N (se categoria do trabalhador for igual a [104, 106]). | Nivel:7  Condição: O (se codCateg for diferente de [104]); N (nos demais casos) |
| Grupos {localTrabGeral}:   Excluido Grupo |  | Campos excluídos: tpLograd, dscLograd, nrLograd, complemento, bairro, cep, codMunic e uf |
| Grupos {horContratual}:   Alterados nível e descrição no registro do evento. | Nível: 5   Descrição : Informações do Horário Contratual do Trabalhador. O preenchimento é obrigatório se {tpRegJor} = [1]. | Nível:6  Descrição:Informações do horário contratual do trabalhador |
| Grupos {horContratual}: campo {dscTpJorn }    Excluido campo |  | Campo excluido |
| Grupos {horContratual}: campo {TpJornada }    Incluídos valores [4, 5, 6, 7] e excluído valor [1] | Preencher com uma das opções: 1 - Jornada com horário diário e folga fixos; 2 - Jornada 12 x 36 (12 horas de trabalho seguidas de 36 horas ininterruptas de descanso); 3 - Jornada com horário diário fixo e folga variável; 9 - Demais tipos de jornada | Valores válidos: 2 - Jornada 12 x 36 (12 horas de trabalho seguidas de 36 horas ininterruptas de descanso) 3 - Jornada com horário diário fixo e folga variável 4 - Jornada com horário diário fixo e folga fixa (no domingo) 5 - Jornada com horário diário fixo e folga fixa (exceto no domingo) 6 - Jornada com horário diário fixo e folga fixa (em outro dia da semana), com folga adicional periódica no domingo 7 - Turno ininterrupto de revezamento 9 - Demais tipos de jornada |
| Grupos {horContratual}: campo {horNoturno}    Criado o campo {horNoturno} – Indica se a jornada semanal possui horário noturno (no todo ou em parte) |  | Gera Gatilho |
| Grupos {horContratual}: campo {dscjorn}    Criado o campo {dscJorn} – Descrição da jornada semanal contratual |  | Gera Gatilho |
| Grupos {horario}:  Excluído o grupo {horario} e respectivos campos. |  | Campos excluídos: dia e codHorContrat |
| Grupos {filiacaoSindical}: campo {cnpjSindTrab}    Excluído o grupo {filiacaoSindical} e respectivo campo. |  | Campo excluido |
| Grupos {alvaraJudicial} | Nível :5 | Nivel:6 |
| Grupos {observaçãol} | Nível :5 | Nivel:6 |
| Grupos {treiCap}: campo {codTreiCap}    Criado o campo {codTreiCap} – código do treinamento, capacitação, exercício simulado ou outra anotação |  | Validação: Deve ser um código válido e existente na  Tabela 28. |
