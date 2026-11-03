---
content_hash: 4c1ad0393b7c01f9e2610187f50bfb06a685de20760fcd1744af7df63386e015
fetched_at: '2026-06-29T00:08:07.866817+00:00'
page_id: '237393863'
product: rm
source: tdn-rm
title: REG0002_Alterar_Data_De_Fechamento_De_Estoque
type: documentation
url: https://tdn.totvs.com/display/LRM/REG0002_Alterar_Data_De_Fechamento_De_Estoque
version: 2
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Versões:** | 11.82 e superiores |
| **Ocorrência:** | Alteração da Data de Fechamento de Estoque |
| **Ambiente:** | Regeração de Saldos e Custos e Alteração da Data de Fechamento de Estoque |
| **Passo a passo:** | Ao alterar a data de fechamento de estoque o sistema apresenta uma mensagem informando que é necessário regerar saldos e custos.        Porém mesmo após regerar saldos e custos o sistema impede que a data seja alterada e a mensagem continua informando que é necessário regerar.   O motivo pelo qual a mensagem continua sendo apresentada é porque alguns produtos ainda continuam sem serem regerados.    Estes produtos podem ser verificados pela consulta abaixo, lembrando de trocar o código da coligada (X) em questão: SQL SELECT DISTINCT CODIGOPRD FROM TPRD(NOLOCK) WHERE CODCOLIGADA= X AND (0=1 OR RECALCSALDO1=1 OR RECALCSALDO2=1 OR RECALCSALDO3=1 OR RECALCSALDO4=1 OR RECALCSALDO5=1 OR RECALCSALDO6=1 OR RECALCSALDO7=1 OR RECALCSALDO8=1 OR RECALCSALDO9=1 OR RECALCSALDO10=1)  ORACLE SELECT DISTINCT CODIGOPRD FROM TPRD WHERE CODCOLIGADA= X AND (0=1 OR RECALCSALDO1=1 OR RECALCSALDO2=1 OR RECALCSALDO3=1 OR RECALCSALDO4=1 OR RECALCSALDO5=1 OR RECALCSALDO6=1 OR RECALCSALDO7=1 OR RECALCSALDO8=1 OR RECALCSALDO9=1 OR RECALCSALDO10=1)       **Possíveis Causas**   * Durante o processo de regeração algum erro foi apresentado e assim o produto não foi regerado (Verificar o Log). * O produto não é de último nível. * O produto é do tipo Serviço e não consiste saldo de serviço. * O produto está inativo.    **Possíveis Soluções**   * Identificar quais produtos não estão sendo regerados e realizar o procedimento um a um. * Produto não é de último nível: Mesmo que o cliente não controle níveis de máscara a opção deverá estar marcada. * Verificar o log de regeração e acertar as mensagens apresentadas para que o produto seja regerado. * Se o produto for do Tipo Serviço, o parâmetro “Consistir Saldo de Serviços” deverá ser habilitado (Ambiente - Parâmetros - Gestão de Estoque - Definições de Estoque - Etapa Gestão de Estoque). * Ativar o produto se estiver inativo. |
| **Observações:** | Para mais informações:    [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
