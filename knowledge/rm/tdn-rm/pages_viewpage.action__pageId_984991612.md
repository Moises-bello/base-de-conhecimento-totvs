---
content_hash: 8501adea1a1d6da82e9395c486fe3e66117c3a45299725de8cfe19c3d4bf7686
fetched_at: '2026-06-29T00:12:16.318208+00:00'
page_id: '984991612'
product: rm
source: tdn-rm
title: Nível de compatibilidade Sql Server para Linha RM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=984991612
version: 33
---

Este documento tem como objetivo fornecer orientações sobre Nível de Compatibilidade do SQL Server. Esta alteração deve ser feita pelo DBA responsável, mais detalhes sobre este procedimento consulte a [Documentação da Microsoft](https://learn.microsoft.com/pt-br/sql/relational-databases/databases/view-or-change-the-compatibility-level-of-a-database?view=sql-server-ver17).

### Importância de Manter o Nível de Compatibilidade do SQL Server Atual

O nível de compatibilidade do SQL Server define como o banco de dados interpreta comandos T-SQL, aplica otimizações e habilita recursos. Embora seja possível manter bancos configurados em níveis antigos, essa prática pode trazer riscos e limitar o funcionamento adequado dos sistemas, especialmente na linha RM.

**1. Segurança**  
Manter o nível de compatibilidade atualizado ajuda a garantir que o banco de dados utilize recursos modernos de segurança. Compatibilidades antigas podem manter comportamentos obsoletos que não seguem as práticas atuais, aumentando a superfície de risco do ambiente.

**2. Compatibilidade com Scripts da Linha RM**  
Os produtos da Linha RM trabalham com scripts SQL  desenvolvidos considerando as funcionalidades e comportamentos mais recentes do SQL Server. Se o banco estiver em um nível de compatibilidade defasado, comandos podem não ser interpretados corretamente, resultando em erros de execução ou atualização do sistemas.

**3. Desempenho e Estabilidade**

A utilização de níveis de compatibilidade mais recentes permite que o otimizador de consultas do SQL Server adote planos mais eficientes e inteligentes, resultando em melhor desempenho para os scripts da Linha RM.

**Observação:** Nos níveis 120 e 130, a alteração no cálculo de cardinalidade pode gerar degradação de performance em consultas com *joins* alinhados, conforme documentado pela própria Microsoft. Nesses casos, a recomendação é reescrever a consulta, aplicar o *hint* que força a cardinalidade anterior ou migrar para versões superiores. Mais detalhes: [Documentação Microsoft](https://learn.microsoft.com/en-us/troubleshoot/sql/database-engine/performance/upgrade-compatibility-level-degrades-performance)

### Versões Recomendadas

| SGBD | 32Bits | 64Bits | Nível de Compatibilidade Padrão | Versão/Patch | Info TOTVS | Observações | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SQL Server 2019 |  | X | 150 | RTM | Recomendado |  | GreenSupported |
| SQL Server 2022 |  | X | 160 | [CU5](https://www.microsoft.com/download/details.aspx?id=105013) | Recomendado | **Importante:** Aplicar [atualização cumulativa 5](https://learn.microsoft.com/pt-br/troubleshoot/sql/releases/sqlserver-2022/cumulativeupdate5) ou superior. | GreenSupported |
| SQL Server 2025 |  | X | 170 |  | Recomendado |  | GreenSupported |

### Versões Suportadas

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SQL Server 2014 |  | X | 120 | SP2 |  | Término do suporte padrão, em suporte estendido, mais informações [acesse aqui](https://docs.microsoft.com/pt-br/lifecycle/products/sql-server-2016). | YellowEOL |
| SQL Server 2016 |  | X | 130 | SP1 |  | Término do suporte padrão, em suporte estendido, mais informações [acesse aqui](https://docs.microsoft.com/pt-br/lifecycle/products/sql-server-2016). | YellowEOL |
| SQL Server 2017 |  | X | 140 | RTM |  | Término do suporte padrão, em suporte estendido, mais informações [acesse aqui](https://docs.microsoft.com/pt-br/lifecycle/products/sql-server-2017). | YellowEOL |

```

```

Documento de Portabilidade

Mais detalhes sobre portabilidade na [página de portabilidade da linha RM](https://tdn.totvs.com/x/XDVNDQ)

Previsão de bloqueio nível de compatibilidade

Atenção: A partir da release 12.1.2702, os níveis de compatibilidade 110 e 120 do SQL Server não serão mais suportados. Planeje sua migração.

[![Contador de visitas](https://megacontador.com.br/img-hL2YYgu6qeqACYD4-1.gif)](https://megacontador.com.br/ "Contador de Visitas do MegaContador")

]]>
