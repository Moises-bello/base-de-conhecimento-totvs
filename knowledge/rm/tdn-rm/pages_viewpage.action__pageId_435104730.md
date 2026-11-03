---
content_hash: bd6249e730f0d625045aa90550a67936cd9f38f575e2ade5c8ce1c6380599021
fetched_at: '2026-06-29T00:09:45.985757+00:00'
page_id: '435104730'
product: rm
source: tdn-rm
title: Novidades 12.1.6 - TOTVS Construção Gestão de Imóveis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435104730
version: 4
---

**Novidades da versão 12.1.6**    
**Data Base**  
Foi criado uma estrutura de tabelas de log nos principais cadastros do TOTVS Incorporação, dessa forma sendo possível a recuperação de informações no tempo através de uma Data Base.   
Em cada registro é exibido a Data de Referência, no qual é a data de alteração que gera impacto. Será exibido também o processo no qual gerou o registro de log juntamente com sua ação que pode ser de:

* Criado;
* Alterado;
* Excluído;

Além da Data de referência, processo e ação é exibido todos os campos do Empreendimento gravados no banco no momento de criação do registro de log.

Para maiores informações sobre as tabelas de log's criadas, seguem os links detalhando cada log:

* Log do empreendimento
* Log do Rateio por Centro de Custo
* Log do Rateio por Departamento
* Log da Venda
* Log do Item da Venda
* Log da Regra da Venda
* Log Parcela Pagamento
* Log Parcela Componente
* Log da Subunidade
* Log da Unidade
* Log do Componente
* Log do Valor de Integração por coligada
* Log do Comprador
* Log do Vendedor
* Log do Contrato
* Log do Tipo de Parcela
* Log da Vaga
* Log do Fiador
* Log da Comissão
* Log da Modalidade
* Log do Componente da Modalidade da Venda
* Log da Característica da Sub-Unidade  
    
  **Limpeza de Tabelas de Log**  
  Foi implementado o processo que executa limpeza das tabelas de log da Venda, Item da Venda, Regra Componentes, Parcela Pagamento e Parcela Componente. O usuário informa o período de tempo onde deverá existir informações do log.   
  Para maiores informações clique aqui.
