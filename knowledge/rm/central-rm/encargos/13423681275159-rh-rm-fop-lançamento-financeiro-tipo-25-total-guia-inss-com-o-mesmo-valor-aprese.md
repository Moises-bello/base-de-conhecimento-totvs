---
article_id: 13423681275159
category: Encargos
content_hash: 94a499de196e65d5ff7434fa87be424b8b90d3fe32f6511756cbf26c578bffb1
fetched_at: '2026-06-28T22:46:52.353398+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Lançamento financeiro tipo 25 - Total Guia INSS com o mesmo
  valor apresentado na DCTFWeb
type: support-article
updated_at: '2024-10-31T16:03:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13423681275159-RH-RM-FOP-Lan%C3%A7amento-financeiro-tipo-25-Total-Guia-INSS-com-o-mesmo-valor-apresentado-na-DCTFWeb
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16079398768791) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como fazer lançamento financeiro tipo 25 - Total Guia INSS com o mesmo valor apresentado  na DCTFWeb.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir da versão 12.1.2209  
  
**Solução**Para realizar o lançamento financeiro, acessar **Encargos | Cadastros Financeiros | Parâmetros**, e parametrizar o lançamento com o tipo 25 - Total Guia INSS com o mesmo valor apresentado  na DCTFWeb.:

Parametrizar o lançamento conforme necessidade da organização.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16079358414231)  
  
Importante: Com o intuito de evitar divergências durante a conferência, o **Relatório de Conferência de INSS Patronal** sempre levará em consideração os autônomos registrados no TOTVS Gestão Financeira. Portanto, o parâmetro "Desconsiderar Autônomos TOTVS Gestão Financeira" não será aplicado no referido relatório. Essa abordagem visa garantir a consistência e a coerência dos registros, facilitando o processo de verificação e prevenindo possíveis discrepâncias.

Após criar o parâmetro financeiro, acesse:, **Configurações | Parametrizador | Encargos Sociais** e marque a flag **Habilita Histórico de INSS no cadastro de seção** e a flag **Discriminar Percentual de Terceiros**

*![](https://centraldeatendimento.totvs.com/hc/article_attachments/13422715654295)*

Após, acesse o cadastro da **seção centralizadora**  **| Anexos | Histórico de percentuais para INSS:**

*![](https://centraldeatendimento.totvs.com/hc/article_attachments/13422683063447)*

Após acessar o histórico de percentuais para INSS, será necessário realizar a parametrização dos valores. Realize a criação de um novo e parametrize conforme necessidade da empresa.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14562024136983)

Ao salvar será apresentado da seguinte forma:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14561514699543)

**Importante**  
Mesmo que a empresa seja filantrópica é necessário que seja criado um histórico de percentual de INSS com os valores zerados.

O sistema não preenche o histórico de percentual de INSS de forma automática, porque cada empresa possui um valor diferenciado para cada campo, sendo assim este preenchimento é realizado de forma manual.

Para geração do lançamento financeiro tipo 25 - Total Guia INSS com o mesmo valor apresentado na DCTFWeb o sistema irá buscar a parametrização que consta no histórico de percentual de INSS, desconsiderando qualquer informação parametrizada na aba dados p/INSS dentro do cadastro da seção.

Segue abaixo um exemplo de lançamento financeiro de INSS com as seguintes parametrizações no cadastro do histórico de percentuais de INSS.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14562065153559)

Envelope do funcionário:

*![](https://centraldeatendimento.totvs.com/hc/article_attachments/13422756585239)*

Geração do lançamento, para esse parâmetro financeiro não obedece os filtros informados no momento da geração da rotina, levando as informações para todas as chapas que possui INSS:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13424142769943)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13422831496983)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13422986336407)

A composição do valor é :

* 20% empresa: 8000\*20% =1.600
* 6,80% de terceiros: 8000\*6,80% = 544,00
* 5,80% de acidente de trabalho: 8000\*5,80% =464,00
* O valor do segurado: 877,22

Total: 3.485,22

**Saiba mais:  
[RH - RM - FOP - Histórico de Percentuais para INSS no cadastro de Seção](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8681885111063-RH-RM-FOP-Hist%C3%B3rico-de-Percentuais-para-INSS-no-cadastro-de-Se%C3%A7%C3%A3o)  
[RH - RM - FOP - Parametrização dos Lançamentos Financeiros](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414130953111-RH-RM-FOP-Parametriza%C3%A7%C3%A3o-dos-Lan%C3%A7amentos-Financeiros)****[DT - Lançamento Financeiro: "25-Total Guia INSS DCTFWeb" e "26-Total Guia INSS DCTFWeb 13º Salário"](https://tdn.totvs.com/pages/releaseview.action?pageId=727915586)**

**[Perguntas e Respostas DCTFWeb](https://tdn.totvs.com/display/LRM/Perguntas+DCTFWeb)**
