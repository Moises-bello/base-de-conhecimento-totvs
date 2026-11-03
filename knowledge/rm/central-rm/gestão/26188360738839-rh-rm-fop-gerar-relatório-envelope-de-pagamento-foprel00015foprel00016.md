---
article_id: 26188360738839
category: Gestão
content_hash: a8a8c83421360b4ae1420b4d5a2577f07ccc8e1b4eab59309665eda7bcd178ee
fetched_at: '2026-06-28T22:46:48.252939+00:00'
product: rm
section_id: 1500000861162
source: central-rm
title: RH - RM - FOP Gerar relatório envelope de pagamento FOPREL00015/FOPREL00016
type: support-article
updated_at: '2025-01-07T17:59:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26188360738839-RH-RM-FOP-Gerar-relat%C3%B3rio-envelope-de-pagamento-FOPREL00015-FOPREL00016
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26188404450711) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como gerar um relatório de envelope de pagamento que apresenta valores incorretos no somatório e traz eventos zerados?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
Para gerar o relatório corretamente, é necessário aplicar os filtros abaixo para garantir que os proventos/descontos estejam corretos e que eventos zerados não sejam exibidos.  
  
1. Acesse o modulo **Gestão** | **RM Reports** selecione o relatório envelope de pagamento e gere o relatório.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26188360709399)  
  
2. Preencha os filtros de acordo com as orientações abaixo. Expanda o filtro clicando em "+", à esquerda, depois clique nos três pontinhos para editar o filtro. Em seguida, clique em 'Adicionar' e depois em 'Salvar', conforme os filtros abaixo.  
  
**Ficha Financeira - Períodos**  
**Ano de competência = [ANO COMPETÊNCIA]**  
**Mês de competência = [MÊS COMPETENCIA]**  
**Numero de período = [PERIODO]  
  
![](https://totvssuporte.zendesk.com/attachments/token/pKN1qThf7XuDVsEfd6YhKXpKm/?name=image.png)  
  
Ficha Financeira   
Valor >= 0.0001  
  
![](https://totvssuporte.zendesk.com/attachments/token/2dpKm5njX1rc6AOrCJpwzYGEC/?name=image.png)  
  
Proventos/Desconto = P  
   
![](https://totvssuporte.zendesk.com/attachments/token/zDkzJ4AcRJ9mr9iF5RJ0hlbL2/?name=image.png)  
  
Ficha Financeira   
Valor >= 0.0001  
   
![](https://totvssuporte.zendesk.com/attachments/token/CBT7mC6KzHpT1qOm3lZ1lVbQZ/?name=image.png)  
  
Proventos/Desconto = D**  
   
![](https://totvssuporte.zendesk.com/attachments/token/1lWZXYYnZqeCj3BxVoAHWD3iF/?name=image.png)  
  
03. Ao realizar a aplicação dos filtros, é necessário clicar no primeiro filtro para preencher os dados de ano de competência, mês de competência e período.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26188360714391)  
  
04. Exemplo geração do relatório.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26188360717591)  
  
**Saiba mais**[Importação de relatórios e layouts através do Totvs Compartilhamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7781155867543-RH-RM-FOP-Importa%C3%A7%C3%A3o-de-relat%C3%B3rios-e-layouts-atrav%C3%A9s-do-Totvs-Compartilhamento)  
[Como gerar relatório no RM reports](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019726432-RH-RM-FOP-RM-Reports-Gera%C3%A7%C3%A3o-de-relat%C3%B3rios)
