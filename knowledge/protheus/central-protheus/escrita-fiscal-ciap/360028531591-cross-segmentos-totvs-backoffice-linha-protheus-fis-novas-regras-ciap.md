---
article_id: 360028531591
category: Escrita Fiscal - CIAP
content_hash: 5a25dbc913fb2159674d7cbba8e77b1604e078ff0ca6c976c11ecca213ef0140
fetched_at: '2026-06-28T22:39:33.938807+00:00'
product: protheus
section_id: 1500001538561
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Novas regras CIAP
type: support-article
updated_at: '2022-09-08T16:42:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028531591-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Novas-regras-CIAP
---

**Dúvida**Como configurar as novas regras CIAP - Coeficiente?

**Ambiente**A partir Versão 12.1.17  
  
**Solução**

Esta implementação tem objetivo de disponibilizar uma nova forma de configuração para compor o coeficiente de apropriação do CIAP, por meio do CFOP e CST de ICMS.

## Cadastro de Operandos de Coeficiente do CIAP

Para esta configuração foi disponibilizado novo cadastro, para que sejam efetuadas as configurações por CFOP e CST, a FISA220 (Configuração Coeficiente CIAP). Trata-se de uma nova forma de composição do coeficiente, totalmente independente da configuração atual, como por exemplo os parâmetros MV\_CFOPEXC, MV\_CIAPTOT, MV\_CIAPVER etc.

Esta implementação não altera de nenhuma forma a configuração “legado”.

Para acessar acessar este cadastro, primeiramente deverá ser adicionado no menu do módulo SIGAFIS, em ***Atualizações/Cadastros*** adicionar a rotina **FISA220**, com descrição ***“Conf. Coeficiente CIAP”***, utilizando as tabelas **F1F** e **F1G**.

Este novo cadastro terá duas seções, seção de cabeçalho para definirmos o **Operando**, e a seção de **CFOP** e **CST**para definirmos quais os CFOPs e CSTs de ICMS que compõem este operando.

Teremos os seguintes operandos disponíveis:

* + **01=Saídas Tributadas**
  + **02=Dev. Saídas Tributadas**
  + **03=Saídas Não Tributadas**
  + **04=Dev. Saídas Não Tributadas**
  + **05=Exportações**
  + **06=Dev. Exportações**
  + **07=Equiparadas a Exportação**
  + **08=Dev. Equiparadas a Exportação**

Na seção de CFOP e CST de ICMS, basicamente definiremos quais CFOPs e CSTs de ICMS que compõem o operando em questão, bem como o valor de origem, que poderá ser:

* + **01=Valor Contábil**
  + **02=Valor da Mercadoria**
  + **03=Isentas**
  + **04=Outras**
  + **05=Base ICMS**
  + **06=Outras + Isentas**
  + **07=Base ICMS + Outras**
  + **08=Base ICMS + Isentas**
  + **09=Base ICMS + Outras + Isentas**

Desta forma a rotina permite definirmos também o valor de origem, conforme a combinação de CFOP e CST de ICMS.

Como exemplo, digamos que o CFOP 5101 deve ser considerado como Saídas Tributadas quando nas vendas com os CST 00 e 20, utilizando a Base de Cálculo de ICMS como valor de origem e, o mesmo CFOP 5101 deve ser considerado como Saída Não Tributada nas vendas com CSTs 30 e 40 e com valor de origem das colunas ISENTAS + OUTRAS, para isso devemos realizar o seguinte cadastro:

| Operando: 01 = Saídas Tributadas | | |
| --- | --- | --- |
| CFOP | CST | Valor de Origem |
| 5101 | 00 | 05 = Base de ICMS |
| 5101 | 20 | 05 = Base de ICMS |

| Operando: 03 = Saídas Não Tributadas | | |
| --- | --- | --- |
| CFOP | CST | Valor de Origem |
| 5101 | 30 | 06 = Isentas + Outras |
| 5101 | 40 | 06 = Isentas + Outras |

Desta maneira, ao processar apropriação dos bens através da rotina **MATA906**, as notas fiscais que enquadrarem nas configurações serão consideradas para composição do coeficiente de apropriação.

A rotina possui uma carga inicial de configurações de operandos, CFOPs e CSTs, que serve como sugestão de configuração, será disparada sempre que acessar o cadastro e o mesmo estiver vazio. Para processar a carga inicial basta confirmar a solicitação de processamento que será exibida ao acessar o cadastro.

Para habilitar esta nova configuração no MATA906, será preciso alterar dois parâmetros, **MV\_CFGCOEF** e **MV\_MTDCOEF**.

O parâmetro **MV\_CFGCOEF** indica se se o coeficiente será obtido através das regras e configurações do legado, ou pelas regras do novo cadastro, a opção **.F.** neste parâmetro indica configuração legado, já a opção .**T.** indica que deverá considerar as novas regras.

O parâmetro **MV\_MTDCOEF** indica o método de cálculo para obter o coeficiente, a opção **1** indica que as devoluções de vendas serão obtidas automaticamente pelo sistema, sem a necessidade de configurar os **Operandos de Devoluções**, já a opção **2** indica que as devoluções de vendas serão obtidas por meio dos **Operandos de Devoluções**, ou seja, as devoluções neste método não serão tratadas automaticamente, precisam ser previamente configuradas.

Isso se deve por conta de alguns Estados não considerarem qualquer devolução para estornar os valores das vendas, por este motivo possuímos este método. Em ambos os casos a fórmula de cálculo do coeficiente será:

**A = Saídas Tributadas**

**B = Saídas Não Tributadas**

**C = Exportações**

**D = Equiparadas a Exportação**

**Coeficiente = ( A + C + D ) / (A + B + C+ D)**

## Relatório de Conferência

Para conferir quais as notas enquadradas conforme as configurações, foi elaborado relatório de conferência, o **FISR220**. 

Para acessar acessar este relatório, primeiramente deverá ser adicionado no menu do módulo SIGAFIS, em ***Relatórios/Listagem*** adicionar a rotina **FISR220**, com descrição **“Conf. Coeficiente CIAP”**, utilizando as tabelas **F1F** e **F1G**.

Para processar este relatório será necessário informar a data de referência, pode ser a mesma data informada ao processar a apropriação do CIAP no MATA906.

Neste relatório teremos três seções, a primeira com detalhamento das saídas, a segunda com o detalhamento das devoluções, sejam elas automáticas ou configuráveis. Nestas duas seções teremos as seguintes colunas:

* + **Nota Fiscal**
  + **Série da Nota Fiscal**
  + **CFOP**
  + **Código do Participante**
  + **Loja do Participante**
  + **Data da nota**
  + **Item do documento Fiscal**
  + **CST de ICMS**
  + **Valor Contábil**
  + **Valor da Mercadoria**
  + **Base de Cálculo do ICMS**
  + **Valor da Coluna Isento**
  + **Valor da Coluna Outras**
  + **Valor de Origem**

Importante ressaltar que a coluna de **Valor de Origem** é dinâmica, conforme indicado no cadastro do coeficiente, para a combinação do CFOP e CST. O valor de origem considerado será exibido no cabeçalho do relatório.

A quebra de página será considerando por Operando e Valor de Origem.

A terceira seção é um resumo com os totalizadores, e terá as seguintes colunas:

* + **Saídas Tributadas**
  + **Devolução das Saídas Tributadas**
  + **Saídas Não Tributadas**
  + **Devolução das Saídas Não Tributadas**
  + **Exportações**
  + **Devolução das Exportações**
  + **Saídas Equiparadas a Exportação**
  + **Devolução das Saídas Equiparadas a Exportação**
  + **Total Tributado**
  + **Total Não Tributado**
  + **Total das Saídas**

Nesta seção cada coluna está identificada com uma letra, para auxiliar no entendimento dos cálculos do resumo.

## Estorno CIAP

Ao processar a Apropriação do CIAP no **MATA906**, os parâmetros MV\_CFGCOEF e MV\_MTDCOEF serão verificados, se o MV\_CFGCOEF estiver com conteúdo .F., então a configuração do legado será processada, caso o parâmetro esteja com conteúdo .T., as regras do legado serão desconsideradas e as regras do novo cadastros serão processadas.

Relembrando que sobre as devoluções, se o parâmetro MV\_MTDCOEF estiver com conteúdo 1 as devoluções serão processadas sem a necessidade de configurar os Operandos de Devoluções, mas se estiver com conteúdo 2 então os Operandos de Devoluções precisam ser configurados.

Importante lembrar que estas novas regras se aplicam também no coeficiente de apropriação no bloco G do SPED Fiscal.

Importante

O compartilhamento das tabelas é compartilhado, porém se houver necessidade poderá ser alterado para exclusivo, conforme necessidade de configuração específica para filial ou grupo de empresa.

As tabelas envolvidas são a **F1F e F1G**
