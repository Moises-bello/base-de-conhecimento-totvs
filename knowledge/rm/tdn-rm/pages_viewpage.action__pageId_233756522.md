---
content_hash: e85c2010df9337219ac7737141d2f6edd49e0e98b76678958dd97a0d2b369864
fetched_at: '2026-06-29T00:06:28.643830+00:00'
page_id: '233756522'
product: rm
source: tdn-rm
title: BD0008_Recomendações_Sobre_Nível_de_Isolamento_BR
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=233756522
version: 2
---

|  |  |
| --- | --- |
| **Produto:** | Banco de Dados |
| **Versões:** | Todas |
| **Ocorrência:** | Recomendações sobre o Nível de Isolamento |
| **Ambiente:** | SQL Server |
| **Passo a passo:** | As transações realizadas no banco de dados possuem um nível de isolamento, que determina o grau em que a transação será isolada das demais transações. Os níveis de isolamento controlam, por exemplo, se serão feitos bloqueios quando os dados são lidos, que tipo de bloqueio é necessário, e por quanto tempo estes bloqueios serão mantidos.  Para melhor aproveitamento do sistema RM, recomendamos a utilização do nível de isolamento READ COMMITTED (default), usando controle de versões de linha, ou seja, com o parâmetro da base de dados READ\_COMMITTED\_SNAPSHOT ativado.  Esta alteração traz os seguintes benefícios:   * As operações de leitura terão um resultado consistente no banco de dados. * Os comandos SELECT não bloquearão dados durante uma operação de leitura (os leitores não bloqueiam os gravadores e vice-versa). * Os comandos SELECT podem acessar o último valor confirmado da linha, enquanto outras transações estão atualizando a linha sem serem bloqueadas. * O número de deadlocks é reduzido. * O número de bloqueios exigido por uma transação é reduzido, o que diminui a sobrecarga do sistema requerida pelo gerenciamento de bloqueios. * Ocorrem menos escalações de bloqueio.   Com o nível de isolamento READ COMMITTED usando controle de versão de linha (READ\_COMMITTED\_SNAPSHOT como ON), o SQL Server terá o mesmo comportamento que o Oracle, para bloqueios de leitura. A configuração deste parâmetro não causa perda de integridade no banco de dados e pode ser revertido se necessário.  Abaixo a sintaxe do comando para ativar o nível de isolamento READ COMMITTED com controle de versionamento de linha. Esta configuração está disponível a partir do SQL Server 2005. **É importante observar que durante a execução do comando, não pode haver nenhuma outra conexão com a base de dados.**  ALTER DATABASE <**nome da base**> SET READ\_COMMITTED\_SNAPSHOT ON GO |
| **Observações:** | Para mais informações:  **COMUNIDADE** [R@Tecnologia](http://fluig.totvs.com/portal/p/10097/post/rtecnologia-community/1639774)   **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 8 – (Tecnologia), 2 – (Banco de Dados) |
