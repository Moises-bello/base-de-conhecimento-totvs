---
content_hash: 97643cf5865fde29b35eb3e386da1ad968517f68b7653a6962dfa01e40f1555b
fetched_at: '2026-06-29T00:10:57.912707+00:00'
page_id: '600519452'
product: rm
source: tdn-rm
title: FISCAL01-14945 DT Gerar o Evento R-2055 pelo Backoffice RM - Reinf
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-14945+DT+Gerar+o+Evento+R-2055+pelo+Backoffice+RM+-+Reinf
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Eventos Periodicos |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14945 |

## **02. SITUAÇÃO/REQUISITO**

Conforme documentação anexada no épico deverá ser criado no processo de geração de Eventos da Reinf o Evento do tipo R-2055;

Criar a versão 1.5.01 (Conferir a máscara no manual) nos parâmetros da EFD-Reinf para correta geração do grupo verProc dos Eventos.

## **03. SOLUÇÃO**

Na geração da Reinf foi incluído o registro R2055 referente a produção rural. O registro é gerado ao agrupar todos as notas que possuem o mesmo tipo de Cliente/Forncedor.

Este registro so será gerado a partir da versão 1.5.01 da Reinf, nos parametros do Fiscal.

**Como gerar:**

Para gerar o registro é necessário uma nota de Entrada que possua o tributo Funrural e que os valores de contribuições do Gilrat e Senar estejam preenchidos.

O que ocorre na geração do R2055, desde que a nota obedeça os requisitos anteriores:

1. Agrupa todos os lançamentos em dois grupos:
   * Caso o Tipo de Cliente/Forncedor (igual Cliente/Fornecedor) agrupa pelo CodColCfo e EmitenteCfo (ou seja, lançamento preenchido no campo Cliente Fornecedor)
   * Caso o Tipo de Cliente/Fornecedor (igual a Empresa) agrupa pelo CodColCfo e CodCfoOrigemDestino (ou seja, lançamento preechido no campo Cliente FOrnecedor Origem/ Destino)
2. Para cada agrupamento gera as informações nos seguintes subgrupos:
   * ideEvento = Informações de identificação do evento (Exatamente igual aos outros registros R2010, R2020  etc)
   * ideContri = Informações de identificação do contribuinte (Informações da Filial Matriz)
   * ideEstabAdquir = Identificação do estabelecimento adquirente da produção (Informações da Filial Matriz)
   * ideProdutor = Identificação do produtor rural, do qual foi efetuada aquisição de produção pelo contribuinte declarante (Informações do Cliente/Fornecedor agrupado no Passo 1) (Obs: o campo 21 deste registro indOpcCP, será gerado sob demanda)
   * detAquis = Detalhamento da aquisição de produção rural (Informação dos Lançamentos e Cliente/Fornecedor)
     + O campo indAquis  deste registro será gerado da seguinte forma, repesitado as seguintes regras gerais:
       - O Participante (Cliente/Fornecedor) deve estar parametrizado como Produtor Rural (no cadastro do Cliente/Forncedor)
       - O Cliente/Forncedor pode ser Pessoa Física ou Juridica, variando de acordo com o Indicativo de Aquisição a ser gerado
       - Para cada Indicativo da aquisição, vale as regras especificas:
         * Para Pessoa Fisica
           + 1 - Aquisição de produção de produtor rural pessoa física ou segurado  
             especial em geral : o Participante NÃO DEVE estar parametrizado como Executadora de PAA (no cadastro do Cliente/Fornecedor), o Produto NÃO DEVE estar parametrizado como Isento de Tributação do Funrural e Natureza NÃO DEVE ser de Exportação (iniciada com 3.)
           + 2 - Aquisição de produção de produtor rural pessoa física ou segurado especial em geral por entidade do PAA: o Participante DEVE estar parametrizado como Executadora de PAA (no cadastro do Cliente/Fornecedor), o Produto DEVE estar parametrizado como Isento de Tributação do Funrural
           + 4 - Aquisição de produção de produtor rural pessoa física ou segurado especial em geral - Produção isenta (Lei 13.606/2018) :  o Participante NÃO DEVE estar parametrizado como Executadora de PAA (no cadastro do Cliente/Fornecedor), o Produto DEVE estar parametrizado como Isento de Tributação do Funrural
           + 5 - Aquisição de produção de produtor rural pessoa física ou segurado especial em geral por entidade do PAA - Produção isenta (Lei 13.606/2018) : Participante DEVE estar parametrizado como Executadora de PAA (no cadastro do Cliente/Fornecedor), o Produto NÃO DEVE estar parametrizado como Isento de Tributação do Funrural
           + 7 - Aquisição de produção de produtor rural pessoa física ou segurado especial para fins de exportação : o Participante NÃO DEVE estar parametrizado como Executadora de PAA (no cadastro do Cliente/Fornecedor) e a Natureza de Operação DEVE ser de Exportação (iniciada com 3)
         * Para Pessoa Juridica
           + 3 - Aquisição de produção de produtor rural pessoa jurídica por entidade do PAA : Participante DEVE estar parametrizado como Executadora de PAA (no cadastro do Cliente/Fornecedor), o Produto NÃO DEVE estar parametrizado como Isento de Tributação do Funrural
           + 6 - Aquisição de produção de produtor rural pessoa jurídica por entidade do  
             PAA - Produção isenta (Lei 13.606/2018) : Participante DEVE estar parametrizado como Executadora de PAA (no cadastro do Cliente/Fornecedor), o Produto DEVE estar parametrizado como Isento de Tributação do Funrural
     + O campo vlrBruto é gerado com a soma do valor da mercadoria dos itens daquele Indicativo de Aquisição
     + O campo vlrCPDescPR  Não será gerado, valor fixo zero
     + O campo vlrRatDescPR Não será gerado, valor fixo zero
     + O campo vlrSenarDesc Não será gerado, valor fixo zero
   * O subgrupo infoProcJud será gerado em outra issue
3. A Filial do Contexto deve estar parametrizada coma versão do TSS 1.5.00, só assim o registro 2055 será gerado.
