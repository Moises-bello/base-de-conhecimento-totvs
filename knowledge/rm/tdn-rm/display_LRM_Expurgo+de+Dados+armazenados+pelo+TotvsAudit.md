---
content_hash: 609b5f6571a21005cd629cf5e9f963ff5a71d25c85c7de2ea6b67d8b2fc43e3e
fetched_at: '2026-06-29T00:11:33.957457+00:00'
page_id: '763249034'
product: rm
source: tdn-rm
title: Expurgo de Dados armazenados pelo TotvsAudit
type: documentation
url: https://tdn.totvs.com/display/LRM/Expurgo+de+Dados+armazenados+pelo+TotvsAudit
version: 2
---

**Expurgo parcial**

É realizado quando desejamos excluir das tabelas de auditoria registros específicos.  
Vá em Processos, e Expurgo Parcial do Log de Auditoria.

Nesta etapa temos que selecionar o filtro de Limpeza/Expurgo, é possível expurgar usando as opções:

1. Usuário específico: Nesta opção é possível expurgar dados apenas de um determinado usuário;
2. Período: Nesta opção é possível expurgar dados apenas de período superior a um determinado período, exemplo: 30,60,90 dias.
3. Operação: Nesta opção é possível expurgar dados apenas de uma das operações que o log executa.

Além das opções acima é possível expurgar log de acessos de tabelas que contém dados protegidos (LGPD), a idade do log é configurável.

Nesta tela é apresentado as tabelas que desejamos que seja feito o expurgo.

Após o expurgo parcial, a tela abaixo indica o sucesso da operação.

**Expurgo Total**

Nesta opção será realizado o expurgo de todos os dados das tabelas de auditoria, esta é a forma mais rápida e pratica para quando a auditoria não é mais necessária.

Na execução desse processo o usuário é alertado quanto ao procedimento a ser feito.

Na tela abaixo demonstra o status da execução do expurgo total, nesse momento a Triggers são desabilitadas.

**Agendamento do Expurgo Parcial/Total**

A partir da versão **12.1.32** foi implementado o agendamento de Jobs para o expurgo, tanto parcial como total, com esta nova funcionalidade o usuário poderá agendar o melhor momento

para realizar o expurgo.

Mais informações sobre o agendamento de processos, clique em [Agendamento de Processos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005088792-RM-Frame-Como-agendar-a-execu%C3%A7%C3%A3o-de-um-processo-)

Podemos gerar os relatórios a partir dos dados coletados pela auditoria para isso vamos em Processos, Gerar Relatório com Base no Log de Auditoria  
  
Aqui teremos a tela de filtros  
  
Definimos os filtros necessário e onde o arquivo deve ser gerado.  
  
Selecionamos as tabelas que desejamos que o relatório seja gerado  
  
  
Abaixo modelo de relatório gerado

**Observação Importante !!!**

Por questões de performance e aumento significativo da base de dados, alguns tipos de dados não são auditados. São eles:

* Em bases Sql Server os tipos não auditáveis são: 'TEXT','NTEXT','IMAGE','TIMESTAMP'
* Em bases Oracle os tipos não auditáveis são: 'LONG','LONG RAW','CLOB','NCLOB','BLOB','BFILE','TIMESTAMP'

Mudança de comportamento colunas de segurança

Visando melhoria na rastreabilidade, a partir da versão 12.1.2406 as colunas de segurança RECCREATEDBY, RECCREATEDON, RECMODIFIEDBY e RECMODIFIEDON presentes nas tabelas do CorporeRM elegíveis a auditoria também serão auditadas por padrão.
