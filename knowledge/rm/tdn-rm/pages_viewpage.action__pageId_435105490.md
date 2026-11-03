---
content_hash: 322e51da99809a49b995385899dd2701280d117954ee8b1a8cd250e5d8421de6
fetched_at: '2026-06-29T00:09:50.624086+00:00'
page_id: '435105490'
product: rm
source: tdn-rm
title: Relatórios - Seguros a Vencer
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105490
version: 8
---

Este relatório é um objeto gerencial que mostra os seguros a vencer num período informado pelo usuário. Para utilizar este relatório é necessário importar o objeto gerencial 'TCGIRELALG0073 - Seguros a Vencer.TotvsReportt' através do menu de **Gestão / RM Reports / Processo de Importar Estrutura de Relatório.**

Este relatório está disponível na pasta de Objetos Gerenciais, presente no diretório de instalação do RM.

Após a importação do relatório, basta então acessar **Gestão / RM Reports,**selecionando o relatório importado. Após isso, ir em Processos/ Gerar relatório, utilizando os filtros disponíveis em sua estrutura.

Atualmente os filtros disponíveis são:

Data Inicial e Data Final para a Data Final de Vigência do Seguro.

Ou seja, caso o usuário informe a Data Inicial 01/01/2018 e Data Final 01/01/2019, o relatório mostrará todos os seguros em que a Data Final de Vigência esteja neste período.

As informações de Seguro mostradas no relatório serão:

Nº apólice,

Código do Seguro,

Nº SUSEP,

Fim de Vigência,

Corretora,

Seguradora,

Descrição,

Coligada.  
Outras informações que poderão ser mostradas são:  
**Informações de Imóveis:** Caso o seguro possua imóveis vinculados os mesmos serão mostrados no relatório.  
**Informações de Contrato de Locação:** Caso o seguro possua contratos de locação vinculados os mesmos serão mostrados no relatório.

**Atenção**: Apenas serão considerados os seguros com Status igual a "**Efetivado**" ou "**Endosso**". Os seguros que estiverem com status diferente destes não serão exibidos, mesmo que a data de vencimento esteja dentro do período informado.  
   
Voltar
