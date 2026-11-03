---
content_hash: a0cb4e7e2e4d2d1758336dc89719db88b1bed7ba6a520ebbb9523ba7123dbdb5
fetched_at: '2026-06-29T00:06:28.626414+00:00'
page_id: '233756338'
product: rm
source: tdn-rm
title: BD0003_Manutenção_Oracle_BR
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=233756338
version: 5
---

|  |  |
| --- | --- |
| **Produto:** | Banco de Dados |
| **Versões:** | Todas |
| **Ocorrência:** | Manutenção Servidor |
| **Ambiente:** | Oracle |
| **Passo a passo:** | **Manutenção:**   * Mantenha a base de dados e o servidor de banco de dados de acordo com as recomendações do documento de portabilidade da TOTVS. O documento de portabilidade pode ser obtido através do portal do cliente, onde existirá um documento por versão (XX.XX) – ([Portabilidade](http://tdn.totvs.com/display/public/LRM/GLB0015_PORTABILIDADE)[).  *Motivo: Diversos problemas podem ocorrer na conversão relacionada à insuficiência de recursos da instancia do banco de dados ou parâmetros do banco de dados fora do padrão homologado. O modelo padrão é a base vazia disponibilizada pela TOTVS, em caso de dúvidas a mesma pode ser verificada para comparação de parâmetros.*](http://tdn.totvs.com/pages/createpage.action?spaceKey=LRM&title=Portabilidade) * Não executar scripts DML ou DDL diretamente na base de dados sem o aval da TOTVS. Scripts executados diretamente na base de dados podem alterar a estrutura e gerar inconsistências na base, o que no momento da conversão pode ser evidenciado ocasionando a necessidade de validação da base de dados. O processo de validação pode ser moroso e gerará custos para o cliente, visto ser um processo de consultoria de especialistas em Banco de dados. * Efetuar a manutenção da base de dados, realizando a reindexação e ou reconstrução de índices e atualização de estatísticas além de monitorar o espaço para crescimentos dos arquivos de dados e arquivos de log do banco de dados. Verifique também a consistência física e lógica da base de dados. Estes procedimentos são de responsabilidade do DBA da empresa, caso não possua DBA a equipe de consultoria da TOTVS poderá ser acionada para esta avaliação.   **Recomendamos que o DBA avalie a periodicidade para execução destas procedures, caso não possua DBA, execute as mesmas na seguinte periodicidade:**  **Reindexação de Indices** – Semanalmente **Atualização de Estatisticas** - Diariamente        Documento de manutenção completo em: [Oracle - Parametrizações básicas da base de dados e servidor](http://tdn.totvs.com/pages/viewpage.action?pageId=61935083) |
| **Observações:** | Para mais informações:  **COMUNIDADE** [R@Tecnologia](http://fluig.totvs.com/portal/p/10097/post/rtecnologia-community/1639774)   **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 8 – (Tecnologia), 2 – (Banco de Dados) |
