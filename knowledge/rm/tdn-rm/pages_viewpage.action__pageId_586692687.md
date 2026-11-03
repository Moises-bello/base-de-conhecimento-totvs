---
content_hash: 8f9991e084f5a4168453a74cbc2394806e366edacdca9a4decbb55f4e7dd3dc9
fetched_at: '2026-06-29T00:10:53.808461+00:00'
page_id: '586692687'
product: rm
source: tdn-rm
title: Alterações S-3000
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=586692687
version: 6
---

false

**A partir das Versões:**

* 12.1.29.282
* 12.1.31.197
* 12.1.32.135
* e Superiores.

# Objetivo:

---

Apresentar as alterações realizadas no evento S-3000 para o leiaute do eSocial Versão S-1.0.

---

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupos {**ideTrabalhador**}: alterada condição. | O (Se **tpEvento** (tipo do evento) corresponder a um dos eventos não periódicos (S-2190 a S-2400) ou um dos eventos periódicos (S-1200, S-1202 ou S-1210); N (Nos demais casos). | O (se **tpEvento**  (tipo do evento) corresponder a um dos eventos não periódicos (S-2190 a S-2420) ou um dos eventos periódicos (S-1200 a S-1210); N (nos demais casos). |
| Grupos {**ideFolhaPagto**} (Identificação do período de apuração a que se refere o evento que será excluído) - Alteração de condição | O (se **tpEvento** (tipo do evento) corresponder a um dos eventos periódicos (S-1200 a S-1280 e S-1300)); N (nos demais casos). | O (se **tpEvento** (tipo do evento) corresponder a um dos eventos periódicos (S-1200 a S-1280)); N (nos demais casos). |
| Grupos {**infoExclusao**}: Campo {**nrRecEvt**} alterada validação. | Tamanho  40.   O recibo deve ser relativo ao mesmo tipo de evento indicado em {tpEvento} e o respectivo evento não deve constar como excluído ou retificado. Além disso, no        caso de exclusão de eventos em que existe a identificação do trabalhador, o evento que está sendo excluído deve referir-se ao mesmo trabalhador identificado por {cpfTrab} e {nisTrab}. | Tamanho  23.  O recibo deve ser relativo ao mesmo tipo de evento indicado em tpEvento e o respectivo evento não deve constar como excluído ou retificado. Além disso, no caso de exclusão de eventos em que existe a identificação do trabalhador, o evento que está sendo excluído deve referir-se ao mesmo trabalhador identificado por cpfTrab. |
| Grupos {**ideFolhaPagto**}: Campo {**indApuracao** } Alterada ocorrência e incluída validação. | Ocorrência  1-1. | Ocorrência  0-1. (Preenchimento obrigatório e exclusivo se tpEvento =[S-1200, S-1202, S-1207, S-1280]) |
| Grupos {**ideFolhaPagto**}: Campo {**tpEvento**} Alterada ocorrência e incluída validação. | Podem ser excluídos apenas os eventos relacionados abaixo:                          a) Não periódicos (S-2190, S-2200, S-2205, S-2206, S-2210, S-2220, S-2221, S-2230 , S-2240, S-2245, S-2250, S-2260, S-2298, S-2299, S-2300, S-2306 e S-2399);                          b) Periódicos (S-1200, S-1202, S-1207, S-1210, S-1250, S-1260, S-1270, S-1280 e S-1300). | Podem ser excluídos apenas os eventos relacionados abaixo:               a) Não periódicos (S-2190, S-2200, S-2205, S-2206, S-2210, S-2220, S-2230 , S-2240, S-2298, S-2299, S-2300, S-2306 e S-2399);               b) Periódicos (S-1200, S-1202, S-1207, S-1210, S-1260, S-1270 e S-1280). |
| Grupos {**IdeTrabalhador**}: Campo {**nisTrab** } Excluído | Campo excluído. | Campo excluído. |

Foram realizados ajustes em alguns processos e na visão.

Acesse **RH | Folha de Pagamento | eSocial | Eventos****periódicos | Processos | Gerar Evento de Exclusão (S-3000)** ou ****RH | Folha de Pagamento | eSocial | Fila de Eventos****| Processos | Gerar Evento de Exclusão (S-3000)****

Será apresentado mensagem de ressalva ao tentar gerar o evento de exclusão dos eventos que foram retirados no grupo **ideFolhaPagto.**

Em **RH | Folha de Pagamento | eSocial | Fila de Eventos**

Ao clicar em Incluir ou Editar o evento S-3000 - Exclusão de Evento não será apresentado o campo NIS

No menu **RH | Folha de Pagamento | eSocial | Fila de Eventos Complementar | Fila de Eventos Complementar**

Ao clicar em Editar o evento S-3000 - Exclusão de Evento não será apresentado o campo NIS
