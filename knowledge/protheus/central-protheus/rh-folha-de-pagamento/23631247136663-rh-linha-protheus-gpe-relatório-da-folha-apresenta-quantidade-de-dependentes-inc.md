---
article_id: 23631247136663
category: RH - Folha de Pagamento
content_hash: 4091432720741221491b33619b1ab6f55121787469864ba1f8f0fab5a78f2e86
fetched_at: '2026-06-28T22:44:16.282308+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Relatório da Folha apresenta quantidade de Dependentes
  incorreto no cabeçalho
type: support-article
updated_at: '2025-04-23T17:30:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23631247136663-RH-Linha-Protheus-GPE-Relat%C3%B3rio-da-Folha-apresenta-quantidade-de-Dependentes-incorreto-no-cabe%C3%A7alho
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23631240035479) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**  
Na impressão do relatório da Folha de Pagamento, a quantidade de dependentes para o imposto de renda fica incorreto, mas no cálculo é considerado corretamente.  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de pessoal - Todas as versões  
  
**Causa**A impressão dessa informação não é direta do campo **RA\_DEPIR** que fica no **cadastro do funcionário** aba **benefícios.** Antes da impressão é feita uma consulta na **SR9 - Histórico Dados Funcionários.**Caso exista alteração na quantidade de dependentes com data posterior a competência de cálculo, este (s) não será (ão) considerado (s).  
  
**Exemplo**  
A folha de abril está sendo calculada no início de maio, mas foi necessária inclusão de novo dependente de IR. A data de inclusão ficou posterior à competência de cálculo, por isso no relatório da folha de abril não foi demonstrado o dependente incluído em maio.  
  
Dados de alteração em **Atualizações > Funcionários > Histórico Dados Funcionários**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23631247115543)

Impressão do Relatório da Folha de Pagamento em **Relatórios > Periódicos > Folha de Pagamento**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23631240040983)  
  
**Solução**Para que a impressão fique correta, é necessário ajustar a data de alteração do campo **RA\_DEPIR** pela rotina **Atualizações > Funcionários > Histórico Dados Funcionários.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23631240045591)**

Desta forma, a impressão do relatório apresentará a quantidade correta de dependentes de IR.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23631240047255)  
  
Saiba Mais**

[RH - Linha Protheus - GPE - O que verificar quando o relatório GPER040 - Folha de Pagamento é gerado em branco](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12784134072855-RH-Linha-Protheus-GPE-O-que-verificar-quando-o-relat%C3%B3rio-GPER040-Folha-de-Pagamento-%C3%A9-gerado-em-branco?source=search)

[RH - Linha Protheus - GPE - Impressão do relatório da folha com valor de salário incorreto no cabeçalho para funcionários com contrato intermitente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034690013-RH-Linha-Protheus-GPE-Impress%C3%A3o-do-relat%C3%B3rio-da-folha-com-valor-de-sal%C3%A1rio-incorreto-no-cabe%C3%A7alho-para-funcion%C3%A1rios-com-contrato-intermitente?source=search)

[RH - Linha Protheus - GPE - Como aglutinar verbas repetidas no recibo de pagamento (GPER030) e nos relatórios da folha (GPER040 e GPER106)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019870372-RH-Linha-Protheus-GPE-Como-aglutinar-verbas-repetidas-no-recibo-de-pagamento-GPER030-e-nos-relat%C3%B3rios-da-folha-GPER040-e-GPER106?source=search)

[RH - Linha Protheus - GPE - Como gerar o relatório da folha de pagamento não personalizável GPER040](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008542382-RH-Linha-Protheus-GPE-Como-gerar-o-relat%C3%B3rio-da-folha-de-pagamento-n%C3%A3o-personaliz%C3%A1vel-GPER040?source=search)

[RH - Linha Protheus - GPE - Relatório de Folha GPER040 por Centro de Custo e Funcionários com tipo de Contrato Diferente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051615953-RH-Linha-Protheus-GPE-Relat%C3%B3rio-de-Folha-GPER040-por-Centro-de-Custo-e-Funcion%C3%A1rios-com-tipo-de-Contrato-Diferente?source=search)

[RH - Linha Protheus - GPE - Parâmetros utilizados para impressão dos relatórios de Folha](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053937794-RH-Linha-Protheus-GPE-Par%C3%A2metros-utilizados-para-impress%C3%A3o-dos-relat%C3%B3rios-de-Folha?source=search)
