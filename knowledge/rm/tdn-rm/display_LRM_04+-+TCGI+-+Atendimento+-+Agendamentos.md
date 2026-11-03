---
content_hash: 0bcb9ed20e44a46d07fc936b40ff9e3ed2cff59bbd9d1cd97982120b68b83ccb
fetched_at: '2026-06-29T00:09:49.495395+00:00'
page_id: '435105305'
product: rm
source: tdn-rm
title: 04 - TCGI - Atendimento - Agendamentos
type: documentation
url: https://tdn.totvs.com/display/LRM/04+-+TCGI+-+Atendimento+-+Agendamentos
version: 7
---

**Agendamento de Atendimento**

---

Nessa tela aparecerão todos os agendamentos do TOTVS Incorporação, referentes à todas solicitações cadastradas.  
Os campos existentes são os mesmos da tela de anexo de agendamento da solicitação.  
   
**Aba Identificação**   
   
**Agendamento**  
Código identificador do agendamento. Campo auto incremental.  
   
**Status do Agendamento**  
Informa a situação atual do agendamento, são eles: Em aberto, Concluído, Cancelado e Improdutivo.  
   
**Data Inicial**  
Marca a data em que foi iniciado o serviço agendado.  
   
**Hora inicial**  
Marca a hora em que foi iniciado o serviço agendado.  
   
**Data Final**  
Mostra a data de término do Serviço agendado.  
   
**Hora Final**  
Mostra a data de término do Serviço agendado.  
   
**Número do Atendimento**  
Mostra a solicitação que foi vinculada ao agendamento.  
   
**Responsável pelo Atendimento**  
Usuário do sistema que realizou ou irá realizar o atendimento/inspeção.  
   
**Tipo de Responsável**  
Mostra se o responsável é um inspetor ou atendente.  
   
**Descrição**  
Mostra o detalhamento do incidente e observações do agendamento.  
*Observação:* Nesse campo podem ser usados os Mnemônicos.

Importante

Foi liberado a opção de edição dos campos '**Status do Agendamento**' e '**Descrição**' para que seja feita a atualização do agendamento. Vale ressaltar que atendimentos com o status **Concluído** ou **Cancelado** não poderão sofrer edição.

   
   
   
**Publicação dos agendamentos na Agenda**  
   
O RM permite que as visões de dados sejam publicadas na sua própria agenda, transformadas em compromissos.  
A partir da tela de Agendamento é possível exportar os dados para a agenda, informando a data do compromisso e uma breve descrição.

* Para exportar os dados acesse o menu Exportar -> Publicar na Agenda.
* Como data de Compromisso escolha a opção **Período de Agendamento**.
* Na próxima tela dê um nome para a fonte de dados e escolha qual campo será a descrição do Compromisso.  Sugestão: **Campo Descrição**.
* Execute o processo e abra a agenda. Todos os compromissos gerados pelo agendamento aparecerão.

A agenda mostrará todos os compromissos referentes a todos os usuários do Sistema da coligada.  
**Filtro por Perfil**  
Para uma melhor visualização, se necessário, pode-se criar um filtro por perfil. Neste filtro utilizamos as variáveis de contexto para que apareçam somente os compromissos do usuário logado por exemplo, ou que apareçam apenas compromissos em aberto.   
No anexo do cadastro de perfil pode ser incluído este filtro.Basta utilizar a tabela XAGENDAMENTOGARANTIA, escolher a coligada e criar a sentença para o filtro.   
   
*Exemplo de filtro (Compromissos não cancelados do usuário corrente):*  
*Código do Usuário = $CODUSUARIO E Status do Agendamento <> 2 (Diferente de Cancelado).*

|  |  |
| --- | --- |
|  | Informações Complementares |

---

|  |  |
| --- | --- |
|  | Como Fazer |

---

|  |  |
| --- | --- |
|  | Veja Também |

---

Para saber como exportar um compromisso para a Agenda do RM, veja em:  
  
  
   
   
Para saber mais sobre como criar filtros por perfil utilizando variáveis de contexto, veja o link abaixo:
