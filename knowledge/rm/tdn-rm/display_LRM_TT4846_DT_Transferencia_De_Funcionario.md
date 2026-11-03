---
content_hash: 59df264f513d4d14c6cd1de7e79caaf8e767c1736200f68ce6b6dba0a815aca6
fetched_at: '2026-06-29T00:06:10.524509+00:00'
page_id: '203764052'
product: rm
source: tdn-rm
title: TT4846_DT_Transferencia_De_Funcionario
type: documentation
url: https://tdn.totvs.com/display/LRM/TT4846_DT_Transferencia_De_Funcionario
version: 3
---

# TRANSFERÊNCIA DE FUNCIONÁRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Transferência de Funcionário* |
| **Situação/Requisito:** | *A transferência de funcionários pode demorar horas em alguns casos, mesmo apenas para um funcionário.* |
| **Solução/Implementação:** | *A demora se devia à quantidade de informações do Chronus que precisavam ser copiadas e recalculadas para garantir a integridade da informação. Em casos de funcionários com um grande volume de batidas, o processo era muito demorado.*  *O processo foi então alterado para copiar apenas as informações a partir da data de rescisão, mantendo o histórico antigo associado à chapa antiga do funcionário. Salvo algumas exceções que ainda são necessárias de serem copiadas em sua totalidade, como o Saldo de Banco de Horas.*  *Devido à limitações do sistema, caso seja marcado o parâmetro "Alterar chapa do funcionário demitido", o processo continuará funcionando como antes, copiando todos os dados do funcionário.* |
| **Chamados relacionados:** | TT4846 |
| **Versões/Release:** | *11.82.41* |
