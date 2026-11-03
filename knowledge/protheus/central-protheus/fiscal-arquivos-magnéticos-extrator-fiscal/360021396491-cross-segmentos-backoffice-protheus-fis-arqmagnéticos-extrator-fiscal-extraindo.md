---
article_id: 360021396491
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: 33870c9e5614c5a2fecd637483d525fd3951544555af51ae6d13d1df3abc3f35
fetched_at: '2026-06-28T22:42:07.770112+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Extrator Fiscal
  - Extraindo T007 para Todas Filiais Selecionadas '
type: support-article
updated_at: '2022-08-18T17:25:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021396491-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Extrator-Fiscal-Extraindo-T007-para-Todas-Filiais-Selecionadas
---

**Ocorrência**Ao executar o extrator fiscal selecionando somente o ***Layout* T007** e selecionando mais de uma filial, o mesmo esta extraindo o **T007** para todas as filiais selecionadas, porém a **SB1** é compartilhada.  
  
**Ambiente**Microsiga Protheus - Livros Fiscais – A partir da versão 12.1.17.   
  
**Causa**Ambiente não possui o parâmetro **MV\_TAFCMPT**configurado.   
  
**Solução**Para sanar este problema, será necessário criar o parâmetro **MV\_TAFCMPT**, com as especificações a seguir e informar o nome das tabelas de cadastro do TAF e o tipo de compartilhamento da tabela de origem do Protheus.   
  
**Filial**: ( vazio - compartilhado )  
**Nome de Var.**: MV\_TAFCMPT   
**Tipo**: 1-Carácter  
**Conteúdo**: Exemplo - C1HEEE|C1JEEC|C1LEEC|C1PEEE|C1OECC **Descrição**: Informe o modo de compartilhamento das tabelas do TAF ( separados por pipe **"|"**) Alias Tabela TAF + Compartilhamento Empresa + Compartilhamento Un.Negócio + Compartilhamento Filial. Por exemplo:   
  
A tabela que representa o cadastro de clientes no Protheus é a **SA1** e o modo de compartilhamento desta tabela no dicionário de dados é **CEE**. Já a tabela que representa o cadastro de clientes no TAF é a **C1H**, desta forma a tabela **C1H** seria representada no parâmetro **MV\_TAFCMPT**desta forma **C1HCEE** **(**C1H=Alias, C=Compartilhamento Empresa, E=Compartilhamento Un. Negócio, E=Compartilhamento Filial**)**.

Saiba mais: [Extraindo T007 para todas filiais selecionadas ( SB1 Compartilhada )](http://tdn.totvs.com/pages/releaseview.action?pageId=439705174)

**Observação:**Para que seja possível a utilização desta funcionalidade, é necessário que o programa **EXTFISXTAF.PRW**esteja com data igual ou superior à 07/12/2018, disponível no patch <https://suporte.totvs.com/portal/p/10098/download?e=725848>.
