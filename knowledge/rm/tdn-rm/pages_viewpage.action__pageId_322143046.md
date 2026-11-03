---
content_hash: 68e863d675c6733044228ee93d0ca11f03a1fcb9178feb05035cc1560bb15b22
fetched_at: '2026-06-29T00:08:47.992404+00:00'
page_id: '322143046'
product: rm
source: tdn-rm
title: Atualizador RM - Scripts Opcionais / Intermediários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=322143046
version: 9
---

|  |  |
| --- | --- |
| **Produto:** | Banco de Dados |
| **Versões:** | 12.1.17 ou superiores |
| **Ocorrência:** | SQL Server e Oracle |
| **Ambiente:** | RM - Scripts Opcionais / Intermediários |
| **Passo a passo:** | **INTRODUÇÃO**  No intuito de padronizar o processo de liberação de Scripts de grandes melhorias e legislações como E-Social, DIRF, CAGED e etc, a Linha RM implementou em sua ferramenta RM Atualizador, o conceito de Scripts Opcionais onde poderemos disponibilizar Scripts "Intermediários" em uma Release que já se encontra no Mercado. Essa Ferramenta tem como objetivo otimizar a execução de scripts que atendem legislações, melhorias e implementações que serão liberadas entre as releases e que demandam grandes alterações estruturais na base de dados.  Assim, garantiremos mais facilidade na execução do processo e mais segurança para o cliente, já que em casos de erros, a base de dados será bloqueada para utilização até que a TOTVS realize a avaliação do LOG de Atualização conforme já ocorre na Atualização para as versões de Release.  **\*Obs.: Scripts com pequenas alterações estruturais e correções pontuais em registros, continuarão a ser disponibilizados através do RM Script Executor.**  Este documento objetiva orientar os procedimentos de execução dos Scripts Opcionais/Intermediários da base de dados dos produtos RM através do Atualizador.    **DESENVOLVIMENTO/PROCEDIMENTO**    **Executando Scripts Opcionais / Intermediários da Base de Dados:**   1. O processo para execução destes scripts, ocorre naturalmente da mesma forma quando atualizamos a base de dados, usando o arquivo "**RM.Atualizador.exe**" no diretório **"...\CorporeRM\RM.Net\"** 2. Na tela **"**Atualizações Disponíveis**",** clique no botão **"**Avançar**".**   **Vale ressaltar que o processo de execução de Scripts Opcionais / Intermediários é um processo crítico que poderá bloquear a base e deve ser feito sem que exista nenhuma **conexão** ativa no banco de dados!**  Neste ponto podemos perceber os scripts opcionais, estes devem ser marcados quando necessários. 3. **Note que os scripts obrigatórios não podem ser desmarcados. Os scripts opcionais possuem a cor VERDE no ícone:** 4. Somente em casos de erros, acione o Suporte da TOTVS. 5. Após a conversão, **em caso de erros,** enviar o log para análise. O log fica neste caminho: C:\totvs\CorporeRM\RM.Net\Atualizador\Log Como característica o nome inicia por "RM.Upgrade..."        **Obs.**: A execução de scripts através do Atualizador RM não inviabilizará a utilização do RM.Script.Executor, o RM.Script.Executor continuará a ser utilizado em casos mais simples em que não haja grande volume de alteração na base de dados. |
| **Observações:** | Para mais informações:  **COMUNIDADE** [R@Tecnologia](http://fluig.totvs.com/portal/p/10097/post/rtecnologia-community/1639774)   **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 8 – (Tecnologia), 2 – (Banco de Dados) |
