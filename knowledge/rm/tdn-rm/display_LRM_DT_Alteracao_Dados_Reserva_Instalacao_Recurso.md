---
content_hash: d140e1d3472e4623bf191033e75caece90fd16dbc89c76f0b2793223355a498c
fetched_at: '2026-06-29T00:08:27.302334+00:00'
page_id: '271406485'
product: rm
source: tdn-rm
title: DT_Alteracao_Dados_Reserva_Instalacao_Recurso
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Alteracao_Dados_Reserva_Instalacao_Recurso
version: 4
---

# Edição da reserva de recurso e instalação

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | RM | | |
| ****Segmento Executor:**** | Educacional | | |
| **Módulo:** | TOTVS Educacional | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Reserva de recurso e instalação | Reserva de recurso e instalação | | | |
| **Requisito (ISSUE):** | EDUEDU001-707 | | |
| **País:** | (x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

### Objetivo

Ajustar uma reserva de um recurso ou de uma instalação sem que seja necessário executar o processo de cancelamento de reserva e em seguida seja executado o processo de criação da reserva.

### Definição da Regra de Negócio

# Editar a reserva de recurso e Instalação

No sistema, acessar: **Módulo Educacional | Atividades acadêmicas | Infra-estrutura | Reserva de recurso e instalação**

Selecionar uma atividade agendada e ir anexo **Reserva de recurso ou Reserva de instalação** e editar a reserva  criada através do processo.

Ao editar uma reserva de recurso o usuário poderá alterar o recurso, data/hora  inicio e data/hora fim. Já na reserva de instalação é possível alterar a sala, data/hora  inicio e data/hora fim.

**Importante**

Uma reserva poderá ser editada se a data da reserva for maior ou igual a data atual. Em caso de choque de horário deve-se verificar a permissão especial para superalocar salas ou recursos. Se o usuário possuir esta permissão, é emitido uma mensagem exibindo o choque e solicitando a confirmação da alteração.

 A edição irá obedecer todas as parametrizações relacionadas à atividade agendada que a reserva está associada de:

* Dias de antecedência;
* Se o dia informado é maior que o dia atual;
* Se Permite exportação para agenda global;
* Se permite reserva para instalação ou todos.

Para reservas de instalação que possuam reserva de recurso:

Se houver alteração de sala e o recurso for exclusivo da sala é emitido mensagem avisando que o recurso será eliminado. Caso o usuário opte por realizar a alteração a reserva do recurso é eliminada.

 Se houver alteração de sala e o recurso associado não for exclusivo a data de início e fim da reserva de sala quando alteradas na reserva de instalação devem ser replicadas para a reserva de recurso. Neste cenário é verificado o choque de horário de recurso. 

Caso seja necessário excluir a reserva de recurso associada deve-se utilizar o processo de cancelar reserva de recurso.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Reserva de recurso | [Alteração] | Atividades acadêmicas -> Infra-estrutura - > Reserva de recurso e instalação ->Reserva de recurso | - |
| Reserva de instalação | [Alteração] | Atividades acadêmicas -> Infra-estrutura - > Reserva de recurso e instalação -> Reserva de instalação | - |
