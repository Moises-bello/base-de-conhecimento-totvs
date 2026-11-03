---
content_hash: 71a4a577e79f88f2b03554d6e2ec5f3354ce5d7cca7635d8c8d40921afadf020
fetched_at: '2026-06-29T00:10:57.630435+00:00'
page_id: '599032982'
product: rm
source: tdn-rm
title: Alterações S-2220 - Monitoramento da Saúde do Trabalhador
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=599032982
version: 4
---

false

**A partir das Versões:**

* 12.1.28.281
* 12.1.29.239
* 12.1.31.142

* e Superiores.

# Objetivo:

---

Apresentar as alterações realizadas no evento S-2190 para o leiaute do eSocial Versão S-1.0.

---

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupos {respMonit}: alterada condição  e ocorrência. | O  1-1 | OC  0-1 |
| Grupos {ideEvento}: Campo {nrRecibo} tamanho alterado | 040 | 23 |
| Grupos {ideVinculo}: Campo {nisTrab} excluído. |  |  |
| Grupos {ideVinculo}: Campo {matricula} alterado condição. | Matrícula atribuída ao trabalhador pela empresa ou, no caso de servidor público, a matrícula constante no Sistema de Administração de Recursos Humanos do órgão. Validação: A matrícula deve corresponder à informada pelo empregador no evento S-2200 do respectivo vínculo trabalhista. Se o trabalhador não está sujeito a esse evento (S-2200), a matrícula não deve ser informada, porém, o trabalhador deve ter sido registrado como TSVE - Trabalhador Sem Vínculo de Emprego/Estatutário, através do evento S-2300. | Matrícula atribuída ao trabalhador pela empresa ou, no caso de servidor público, a matrícula constante no Sistema de Administração de Recursos Humanos do órgão. Validação: Deve corresponder à matrícula informada pelo empregador no evento S-2190, S-2200 ou S-2300 do respectivo contrato. Não preencher no caso de Trabalhador Sem Vínculo de Emprego/Estatutário - TSVE sem informação de matrícula no evento S-2300. |
| Grupos {ideVinculo}: Campo {codCateg} alterado condição. | Preencher com o código da categoria do trabalhador, conforme Tabela 01. Validação: Só informar se o trabalhador tiver sido registrado como TSVE - Trabalhador Sem Vínculo de Emprego/Estatutário, através do evento S-2300. Não informar nos demais casos. Se informado, deve existir na Tabela de Categorias de Trabalhadores (Tabela 01). 18 | Preencher com o código da categoria do trabalhador. Informar somente no caso de TSVE sem informação de matrícula no evento S-2300. Validação: Informação obrigatória e exclusiva se não houver preenchimento de matricula. Se informado, deve ser um código válido e existente na Tabela 01. |

Mais informações em:
