---
article_id: 360053590733
category: RH - Férias
content_hash: a5b74e357dfb04ccf92ee1f7821f335678d5390180cc7100127874af968b9917
fetched_at: '2026-06-28T22:43:59.189804+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Relatório Conciliação de Férias em planilha (GPER135)
type: support-article
updated_at: '2025-04-30T11:22:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053590733-RH-Linha-Protheus-GPE-Relat%C3%B3rio-Concilia%C3%A7%C3%A3o-de-F%C3%A9rias-em-planilha-GPER135
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31766683741079) Tempo aproximado para leitura: **00:03:00 min**  
**Dúvida**Relatório Conciliação de Férias em **planilha** (GPER135).  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**A finalidade do relatório é apresentar o valor líquido das Férias proporcionais para o mês correspondente, quando as férias são calculadas em meses partidos. Dessa forma, a partir de uma data de referência, o relatório poderá demonstrar o líquido proporcional em três colunas distintas: **Valor Mês Ant.**, **Valor Mês** e **Valor Mês Seg**.  
  
**Exemplo:** 30 dias de Férias durante o período de 20/03/25 a 18/04/25.  
Se a Data de Referência do relatório for 31/03/25, o sistema irá demonstrar os valores de Férias correspondentes ao período de 20/03 à 31/03 na coluna **VALOR MES,** e os valores de Férias correspondentes ao período de 01/04 à 18/04 serão demonstrados na coluna **VALOR MES SEG.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31766683741975)**

Por outro lado, se a Data de Referência do relatório for 30/04/25, o sistema irá demonstrar os valores de Férias correspondentes ao período de 20/03 à 31/03 na coluna **VALOR MES ANT,** e os valores de Férias correspondentes ao período de 01/04 à 18/04 serão demonstrados na coluna **VALOR MES**.  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31766683742359)**

**Importante:**Para realizar a conferência dos valores do relatório, é preciso ter atenção aos seguinte detalhes:  
**1 -** O relatório irá pesquisar os lançamentos existentes no **Movimento Mensal e nos Acumulados** (tabelas SRC e SRD, respectivamente). Ou seja, antes de gerar o relatório será necessário **efetuar o cálculo da Folha de Pagamento** quando a Data de Referência estiver dentro do mesmo mês aberto para o cálculo da Folha, para que os valores de Férias sejam gerados no movimento mensal.  
**2 -** Os valores exibidos são apurados com base no Líquido do Recibo de Férias do Funcionário, porém, dependendo da configuração do parâmetro **MV\_DINSSFM**, o INSS de Férias poderá ser recalculado na Folha de Pagamento. Por esse motivo, após calcular a Folha de Pagamento, o INSS de Férias pode exibir um valor diferente daquele que foi calculado inicialmente nas Férias. Essa situação acontece, principalmente, o quando o parâmetro **MV\_DINSSFM**está definido com valor **N.****3 -** A Data de Referência deve estar dentro no mês de início ou término das Férias. Então, para o exemplo citado no início desse documento, a Data de Referência será válida somente se estiver entre os meses 01 e 02 de XX.  
  
Para que o relatório seja gerado em formato **planilha**, selecione o tipo conforme imagem abaixo:   
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087864173)  
  
  
Em **Outras Ações >** **Parâmetros,** preencha o grupo de perguntas de acordo com a necessidade e *help* de campo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31766723583895)

**Saiba Mais:**  
[RH - Linha Protheus - GPE - Quais relatórios de férias são gerados em planilha](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053346713-RH-Linha-Protheus-GPE-Quais-relat%C3%B3rios-de-f%C3%A9rias-s%C3%A3o-gerados-em-planilha)
