---
content_hash: 7aa96bf351a09a6402d847327d644088673f757fcf0d88c00bcb515d9a136370
fetched_at: '2026-06-29T00:10:09.501762+00:00'
page_id: '452719685'
product: rm
source: tdn-rm
title: Faltas por Suspensão/Justificada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719685
version: 20
---

Neste módulo podemos consultar as ocorrências de faltas dos funcionários de acordo com o filtro selecionado. Podemos também informar se a falta é por suspensão ou justificada.

Quando a falta for Justificada o sistema irá habilitar o campo "Justificativa" para que o usuário defina a falta justificada.

Quando a falta for por suspensão o sistema irá habilitar o campo "Motivo" para informarmos o motivo da suspensão do funcionário no dia.

Regras e Parametrização

* Se o usuário editar um falta que já tenha uma justificativa, selecionar a flag "Suspensão" em seguida desmarcá-la , o campo justificativa será demonstrada vazia, ou seja, a justificativa informada será excluída.

* Para que as alterações sejam mantidas após o cálculo, ao editar um registro de suspensão via anexos, no sindicato do funcionário deve estar configurado para utilizar banco de horas ou deve ser marcado o parâmetro “Utiliza Justificativas de exceção” em Configurações | Parametrizador| Parâmetros Iniciais |  Parâmetros do Cálculo . Maiores detalhes:

* Caso não utilize a opção acima:
  + Deverá editar o registro da Suspensão em Movimento | Faltas por Suspensão/Justificativa ou
  + Cadastrar ou editar a suspensão em Cadastros | Suspensão. Maiores detalhes : [Como cadastrar uma Suspensão](https://tdn.totvs.com/pages/viewpage.action?pageId=452720016)

* Não podemos marcar falta por suspensão para os funcionários com horário do tipo flexível que possuir banco de horas por período.
* Para manter a flag da suspensão marcada, no processo de Recálculo em Movimento | Calcular, o parâmetro "Atualiza informações das ocorrências(Atitudes, justificativas) ", deverá ser desmarcado.

**Data -** Este campo é preenchido pelo sistema e informa a data da falta do funcionário.

**Suspensão -** Marcando este parâmetro o sistema irá considerar esta falta como uma Falta por Suspensão, e irá habilitar o campo "Motivo" para informarmos o motivo da suspensão do funcionário.

**Ocorrência -** Este campo é preenchido pelo sistema e informa a ocorrência do funcionário, neste caso todas as ocorrências serão "Falta".

**Início -** Este campo é preenchido pelo sistema e não pode ser alterado. Nele é informada a hora de início da falta do funcionário.

**Fim -** Este campo é preenchido pelo sistema e não pode ser alterado. Nele é informado a hora do final da falta do funcionário.

**Justificativa -** Este campo será habilitado se o campo "Suspensão" estiver desmarcado. É utilizado para informarmos a falta justificada do funcionário.

**Motivo -** Este campo só poderá ser editado se o campo "Suspensão" estiver marcado. É utilizado para informarmos o motivo da suspensão do funcionário. Este campo será impresso no relatório do Espelho do cartão de ponto do funcionário se marcarmos a opção "Imprime falta por suspensão".

|  |  |
| --- | --- |
|  | Como Fazer |

---

Faltas por Suspensão - Processos
