---
content_hash: 6a7d97989c9872e6b045bbe7821f131ecbb89583fa1dd65747c26ba17017dc3d
fetched_at: '2026-06-29T00:10:56.848845+00:00'
page_id: '593253092'
product: rm
source: tdn-rm
title: Alterações S-2190
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=593253092
version: 4
---

false

**A partir das Versões:**

* 12.1.29.282
* 12.1.31.197
* 12.1.32.135
* e Superiores.

# Objetivo:

---

Apresentar as alterações realizadas no evento S-2190 para o leiaute do eSocial Versão S-1.0.

---

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupos {ideEvento}: Campo {indRetif} adicionado. |  | Informe [1] para arquivo original ou [2] para arquivo de retificação. Valores válidos: 1 - Original 2 - Retificação |
| Grupos {ideEvento}: Campo {nrRecibo} adicionado. |  | Preencher com o número do recibo do arquivo a ser retificado. Validação: O preenchimento é obrigatório se indRetif = [2]. Deve ser um recibo de entrega válido, correspondente ao arquivo que está sendo retificado. |
| Grupos {infoRegPrelim}: Campo {matricula} adicionado. |  | Matrícula atribuída ao trabalhador pela empresa. Validação: O valor informado não pode conter a expressão 'eSocial' nas 7 (sete) primeiras posições. Regra de validação: REGRA\_CARACTERE\_ESPECIAL |
| Grupos {infoRegPrelim}: Campo {codCateg} adicionado. |  | Preencher com o código da categoria do trabalhador. Validação: Deve ser um código de categoria sujeito ao Registro de Eventos Trabalhistas - RET de trabalhador não vinculado ao Regime Próprio de Previdência Social - RPPS, ou seja, "Empregado" ([1XX]), algumas categorias de "Agente Público" ([301, 302, 303, 304, 306, 307, 309, 310, 312]), "Avulso" ([2XX]), "Cessão" ([4XX]), algumas categorias de "Contribuinte Individual" ([721, 722, 723, 731, 734, 738, 761, 771]) ou de "Bolsista" ([901, 902]). |
| Grupos {infoRegPrelim}: Campo {natAtividade } adicionado. |  | Natureza da atividade. Valores válidos: 1 - Trabalho urbano 2 - Trabalho rural Validação: Preenchimento obrigatório se codCateg for relativo a "Empregado", "Agente Público", "Avulso" ou igual a [401, 731, 734, 738]. Não deve ser preenchido se codCateg = [721, 722, 771, 901]. Se codCateg = [104], deve ser preenchido com [1]. Se codCateg = [102], deve ser preenchido com [2]. |
| Grupos {infoRegCTPS} adiconado. |  | OC (se codCateg for relativo a "Empregado" ou "Agente Público"); N (nos demais casos) |
| Grupos {infoRegCTPS}: Campo {CBOCargo} adicionado. |  | Informar a Classificação Brasileira de Ocupações - CBO relativa ao cargo. Validação: Deve ser um código válido e existente na tabela de CBO, com 6 (seis) posições. |
| Grupos {infoRegCTPS}: Campo {vrSalFx} adicionado. |  | Salário base do trabalhador, correspondente à parte fixa da remuneração. Validação: Se undSalFixo for igual a [7], preencher com 0 (zero). |
| Grupos {infoRegCTPS}: Campo {undSalFixo} adicionado. |  | Unidade de pagamento da parte fixa da remuneração. Valores válidos: 1 - Por hora 2 - Por dia 3 - Por semana 4 - Por quinzena 5 - Por mês 6 - Por tarefa 7 - Não aplicável - Salário exclusivamente variável |
| Grupos {infoRegCTPS}: Campo {tpContr} adicionado. |  | Tipo de contrato de trabalho. Valores válidos: 1 - Prazo indeterminado 2 - Prazo determinado, definido em dias 3 - Prazo determinado, vinculado à ocorrência de um fato |
| Grupos {infoRegCTPS}: Campo {dtTerm} adicionado. |  | Data do término do contrato por prazo determinado. Validação: O preenchimento é obrigatório se tpContr = [2]. Não informar se tpContr = [1]. Deve ser igual ou posterior à data de admissão. |

Foram criados alguns campos no cadastro de registro preliminar.

Acesse **RH | Folha de Pagamento | Administração de pessoal | Registro preliminar**

Campos incluídos na tela

**Observação:** Campo **natureza da atividade** tem validação de preenchimento no caso de **código da categoria eSocial** 102,104.
