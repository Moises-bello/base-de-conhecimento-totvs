---
content_hash: 4352b4acccbcfdcbc81fff3378e0e6ccb5cb57de365c80beb0a2a006f29f964e
fetched_at: '2026-06-29T00:10:09.355774+00:00'
page_id: '452719640'
product: rm
source: tdn-rm
title: Gerenciador de Log de Cálculo e Gerenciador de Logs Complementares
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719640
version: 8
---

O módulo **Gerenciador de Log de Cálculo** é uma parte do sistema que permite ao usuário verificar informações de cálculos da Folha de Pagamento que já foram executados. As informações são recuperadas a partir dos logs que são gerados para os funcionários. Inicialmente, ao entrar na tela, é apresentado, ao usuário do sistema, um grid com todos os logs de funcionários, gerados anteriormente pela execução de cálculos. Um clique duplo sobre uma linha permite a visualização de mais informações sobre o log escolhido. Juntamente com os detalhes dos logs dos funcionários, é possível verificar, também, dados sobre o cálculo que gerou o log escolhido (aba "Log do Processo"). Essa tela, com detalhes a respeito dos logs, conta também com um botão que permite mostrar as informações exibidas, na aba corrente, no programa **Bloco de Notas**.

Existem também  o **Gerenciador de Log de Cálculo Complementares,** que foram criados para melhorar a performance da leitura dos logs. Quando há muitos registros no **Gerenciador de Log** os mesmos podem ser movidos para a tabela de log complementares, assim diminuindo o tempo de leitura

**Mover para Logs Complementares**: É possível que as tabelas responsáveis por armazenarem os logs de cálculo acumulem muitos dados. Para minimizar o problema de armazenar muitos dados nas tabelas de log principais foi criado um processo para esse módulo que possibilita transferir parte dos logs existentes para as tabelas complementares. Essas tabelas são cópias das tabelas de cálculo originais que foram criadas para que exista a possibilidade de diminuir a carga de dados armazenadas somente nas tabelas originais. Os logs movidos ainda podem ser acessados através do módulo de **Logs Complementares**. Uma vez que os logs tenham sido movidos para as tabelas complementares eles podem, inclusive, ser removidos, permanentemente, do sistema. Esse processo é exclusivo da opção **Gerenciador de Log de Cálculo**

**Quantidade de meses a manter o log de cálculo:** É possível informar o número de meses ao invés da Data Base para a contagem a ser considera a partir da competência anterior. Para que sejam movidos todos os logs de antes do final do último dia do mês anterior deverá ser informado no campo 0 (zero).

**Data Base para Movimentação:** Deverá ser informada a Data Base para Movimentação dos logs de cálculo, sendo transferidos a partir da data base informada para a tabela de Logs Complementares.

**Transfere logs de funcionários demitidos:**É possível transferir os Logs de funcionários demitidos para as tabelas de Logs Complementares.

Um recurso que pode ser usado nos dois tipos de log (comum e complementar) é o **Gerenciador de Log**

Este recurso permite exportar  os Logs para arquivos **.txt**

Antes de exportar o relatório é possível escolher o tipo de log que se vai exportar, se ele vai ser gerado no formato **wordPad** (neste caso o txt não é gerado) e agora com a nova alteração os logs serão salvos no caminho informado pela tag [<fileserverpath>](https://tdn.totvs.com/display/LRM/Configuracao+das+Tags+FileServerPath+e+LogPath)

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Gerenciador de Logs Complementares
