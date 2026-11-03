---
article_id: 9783033300119
category: eSocial - Gerar XML/ Integração Evento
content_hash: 9409d5c560607147a4704d8f3326603e131c1ac56e2e8c6178f9e71586018517
fetched_at: '2026-06-28T22:47:12.119538+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro 303 na integração com o Governo: Não foi localizado
  o contrato de trabalho do trabalhador'
type: support-article
updated_at: '2025-07-02T17:51:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9783033300119-RH-RM-FOP-eSocial-Erro-303-na-integra%C3%A7%C3%A3o-com-o-Governo-N%C3%A3o-foi-localizado-o-contrato-de-trabalho-do-trabalhador
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24266708921879) Tempo aproximado para leitura: **00:02:00 min**  
**Ocorrência**Ao transmitir o evento S-2306 para o governo é retornado a inconsistência **Erro código** **303: Não foi localizado o contrato de trabalho do trabalhador CPF: xxxxxxxxxxx e Categoria: Contribuinte individual - empresários, sócios e membro de conselho de administração ou fiscal. Ação: Utilize o evento S-2300 - Trabalhador Sem Vínculo de Emprego/Estatutário - Início, para cadastramento do contrato de trabalho conforme tabela 1 (Categorias de Trabalhadores).**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9778034393879)**

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões

**Causa**  
Essa mensagem de erro ocorre na validação do registro **S-2306** (**Trabalhador Sem Vínculo de Emprego/Estatutário - Alteração Contratual**) que contém informações divergentes com o cadastro do funcionário no S-2300, como matrícula, código de categoria ou CPF ou quando a data de alteração é superior à data de início do funcionário encaminhado no S-2300.

**Solução**Para correção da ocorrência favor realizar as validações abaixo:

**• Matrícula** eSocial **divergente**  
1. Para conferir a matricula do funcionário acesse **Administração de Pessoal** | **Funcionários**;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9786273351959)

2.  Localize o funcionário e no campo **Matrícula eSocial** realize a alteração conforme consta no eSocial;

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9786371455383)

3. Após ajuste,  gere o XML e envie ao eSocial.

**• Categoria** eSocial **divergente**1. Para consultar a categoria do funcionário acesse **Administração de Pessoal** | **Funcionários** e localize o funcionário;

2. No histórico do funcionário em **Anexos** | **Históricos** | **Histórico da Categoria eSocial** deverá constar a categoria de acordo com o informado no cadastro do funcionário;

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9786734865431)

3. Após ajuste, na fila de eventos gere o XML e envie ao eSocial.

• Data de alteração anterior a **data de admissão**  
Para conferir a data de admissão acesse **Administração de Pessoal** | **Funcionários** é selecione o funcionário;

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9786931162263)

• *Tag* **codCateg** não gerada no XML  
Verifique se no evento S-2306 a *tag* **codCateg** esta sendo informada. Caso a *tag* não esteja sendo informada no XML:

 ![](https://totvssuporte.zendesk.com/attachments/token/If9fEqeCYqtCGNY1jd4LsSq2S/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/dHJnBFJsQXKGjiBW1WeAS2Ceo/?name=image.png)
