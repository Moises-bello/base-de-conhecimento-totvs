---
content_hash: 9f53f7ae4ad2b762815bc50379883ea79fc8a5fa8fa0305b58d79c43439e87e5
fetched_at: '2026-06-29T00:09:33.288657+00:00'
page_id: '425458955'
product: rm
source: tdn-rm
title: Informações Estratégicas - Sumário de Atendimentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458955
version: 1
---

**Informações Estratégicas - Sumário de Atendimentos**

---

São apresentadas informações relativas aos mais recentes acessos e somatórios de atendimentos associados ao cliente. Para este recurso não é utilizado o conceito de grupo de clientes (os calculos são realizados para um único cliente que no caso é o cliente do atendimento que se está acessando) e também não é permitido o uso de consultas personalizadas.  
Os dados apresentados são: Total de atendimentos pendentes, concluídos, abertos no último mês, abertos no último ano, total geral, total de atendimentos que estão agendados, data de último acesso e média de acesso mensal (considerando a abertura do atendimento mais antigo e o mais recente). Segue abaixo a consulta SQL como os dados são recuperados:  
         SELECT REGISTROS, TOTAL, DATA          FROM (                 SELECT 'Pendente' REGISTROS, COUNT TOTAL, NULL DATA                 FROM HATENDIMENTOEXT (NOLOCK)                 WHERE     CODCFO     = :CODCFO                       AND FECHAMENTO IS NULL                       AND CODSTATUS  IN ('A', 'R', 'G', 'T', 'D', 'E')                 UNION                 SELECT 'Concluídos' REGISTROS, COUNT TOTAL, NULL DATA                 FROM HATENDIMENTOEXT (NOLOCK)                 WHERE     CODCFO         = :CODCFO                       AND NOT FECHAMENTO IS NULL                       AND CODSTATUS      IN ('U','O','F')                 UNION                 SELECT 'Abertos no Último Mês' REGISTROS, COUNT TOTAL, NULL DATA                 FROM HATENDIMENTOEXT (NOLOCK)                 WHERE     CODCFO          = :CODCFO                       AND MONTH(ABERTURA) = MONTH(DATEADD(MONTH,11,GETDATE()))                       AND (YEAR(ABERTURA) = YEAR(GETDATE()) OR ((MONTH(GETDATE())=1) AND (YEAR(ABERTURA) = YEAR(GETDATE())-1)))                 UNION                 SELECT 'Abertos no Último Ano' REGISTROS, COUNT TOTAL, NULL DATA                 FROM HATENDIMENTOEXT (NOLOCK)                 WHERE     CODCFO         = :CODCFO                       AND YEAR(ABERTURA) = YEAR(GETDATE())-1                 UNION                 SELECT 'Total' REGISTROS, COUNT TOTAL, NULL DATA                 FROM HATENDIMENTOEXT (NOLOCK)                 WHERE     CODCFO    = :CODCFO                 UNION                 SELECT 'Agendadas' REGISTROS, COUNT TOTAL, NULL DATA                 FROM HATENDIMENTOEXT (NOLOCK)                 WHERE     CODCFO     = :CODCFO                       AND FECHAMENTO IS NULL                       AND CODSTATUS  IN ('E')                 UNION                 SELECT 'Data último acesso' REGISTROS, NULL TOTAL, MAX(ABERTURA) DATA                 FROM HATENDIMENTOEXT (NOLOCK)                      WHERE (CODCFO IN (:CODCFO))                 UNION                 SELECT 'Média de acessos' REGISTROS, COUNT(CODATENDIMENTO)/(DATEDIFF(MONTH, MIN(abertura), MAX(abertura))+1) TOTAL, NULL DATA                 FROM HATENDIMENTOEXT (NOLOCK)                 WHERE CODCFO  IN (:CODCFO)               ) XXX
