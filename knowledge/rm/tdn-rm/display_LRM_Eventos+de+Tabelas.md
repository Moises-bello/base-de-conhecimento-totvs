---
content_hash: f5c1aba9ff9a8c711394d438ad79b495a28825f350a25fceeb304128e34266ea
fetched_at: '2026-06-29T00:10:07.693683+00:00'
page_id: '452719415'
product: rm
source: tdn-rm
title: Eventos de Tabelas
type: documentation
url: https://tdn.totvs.com/display/LRM/Eventos+de+Tabelas
version: 1
---

**Eventos de Tabelas**

---

Estes eventos complementam os Eventos Iniciais, sendo responsáveis por uma série de informações que validam os Eventos Não Periódicos e Eventos Periódicos, e buscam otimização na geração dos arquivos e no armazenamento das informações no Ambiente Nacional do eSocial, por serem utilizadas em mais de um evento do sistema ou por se repetirem em diversas partes do leiaute. Sua transmissão é obrigatória e deverá ser feita logo após o envio do evento de Informações do  Empregador/Contribuinte/órgão público (S-1000) e antes dos eventos de cadastramento inicial (S-2100 e S-2300), e dos Eventos Periódicos e Eventos Não Periódicos.  
Todos os eventos de tabela do eSocial possuem um atributo de vigência ou "Período de validade das informações". Esse atributo será utilizado para "guardar um histórico" das informações transmitidas, vinculado ao respectivo "período de validade". Neste sentido, todos os eventos de tabela possuem 3 grupos de informações: a) Inclusão: Utilizada para inserir um novo item na tabela(Histórico) ou modificar um atributo de um item já existente, com uma nova vigência;  
Exemplo: Realizado a transmissão de uma rubrica ao governo na competência 11-2017, porém na competência 12-2017 foi feito uma alteração na mesma, sendo assim, será gerado um gatilho de alteração possuindo o grupo Inclusão, pois se trata de um novo registro para o histórico, sendo que será valido apenas a partir da competência 12-2017.  
b) Alteração: Utilizada para alterar os atributos de um item que estavam incorretos para um determinado período que se quer alterar;  
Exemplo: Realizado a transmissão de uma rubrica ao governo na competência 11-2017 e logo em seguida(mesma competência) foi feito uma alteração na mesma, sendo assim, será gerado um gatilho de alteração possuindo o grupo Alteração, pois se trata de um ajuste referente a um período de validade já enviado.  
c) Exclusão: Utilizada para excluir uma determinada ocorrência de uma tabela.  
S-1000 - Informações do Empregador S-1005 - Tabela de Estabelecimento/Obras S-1010 - Tabela de Rubricas S-1020 - Tabela de Lotações Tributárias S-1030 - Tabela de Cargos S-1050 - Tabela de Horários/Turnos de Trabalho S-1060 - Tabela de Ambientes de Trabalho S-1070 - Tabela de Processos Administrativos/Judiciais

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Gerar XML HelpWiki GDP RH - Folha de Pagamento
