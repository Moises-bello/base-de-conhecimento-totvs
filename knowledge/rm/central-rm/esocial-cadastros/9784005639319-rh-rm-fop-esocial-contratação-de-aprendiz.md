---
article_id: 9784005639319
category: eSocial - Cadastros
content_hash: 4ce81acde869d02bea57f818c59623eb9723451c1c3ac8cb4175db59fdf24302
fetched_at: '2026-06-28T22:47:14.484424+00:00'
product: rm
section_id: 1500000834341
source: central-rm
title: RH - RM - FOP - eSocial - Contratação de aprendiz
type: support-article
updated_at: '2026-01-09T12:00:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9784005639319-RH-RM-FOP-eSocial-Contrata%C3%A7%C3%A3o-de-aprendiz
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18245601758871) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como é realizada a contratação de aprendiz (categoria eSocial **103**) e quais eventos enviar ao eSocial?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**  
A contratação de aprendizes pode ocorrer na forma direta ou indireta, nos termos dos arts. 429 a 431 da CLT.

**- Contratação direta**

É aquela realizada entre o estabelecimento obrigado ao cumprimento da cota e o aprendiz, como típica relação de emprego com contrato especial de aprendizagem. Nessa modalidade de contratação, a entidade de formação profissional integra a relação jurídica apenas como parte responsável por proporcionar a formação teórica prevista no programa de aprendizagem, de forma que o **estabelecimento cumpridor da cota é** quem mantém a condição de **empregador do aprendiz**. Nesses casos, portanto, a própria **empresa contratante** é quem deverá **enviar o evento de admissão** do aprendiz (indicando, como local de trabalho, o CNPJ completo do estabelecimento da empresa e onde exercer suas atividades), além das demais informações sobre a relação empregatícia, como alterações contratuais, afastamentos, remunerações, desligamento etc. 

**- Contratação indireta**

Na contração indireta a **entidade de formação profissional** assume a condição de **empregador do aprendiz**. São autorizadas a atuarem nesse tipo de contratação as entidades sem fins lucrativos e as entidades de prática desportiva que formalizarem contrato ou convênio nesse sentido com o estabelecimento que deve cumprir a cota. Nesses casos, a **entidade** que assume a condição de empregadora é quem **deve enviar o evento de admissão** do aprendiz (indicando, em campo próprio, o CNPJ do estabelecimento cumpridor da cota para o qual a contratação do aprendiz foi efetivada), além das demais informações sobre a relação empregatícia, como alterações contratuais, afastamentos, remunerações, desligamento etc. A única obrigação da **empresa cumpridora da cota** de aprendizagem com relação ao eSocial, nos casos de contratação indireta, será informar, no evento **S-1005** (Tabela de Estabelecimentos, Obras ou Unidades de Órgãos Públicos), que a contratação de aprendizes daquele estabelecimento a ser cadastrado se dá por intermédio de entidade educativa sem fins lucrativos ou de prática desportiva, indicando o CNPJ da respectiva entidade.

Abaixo segue os eventos que devem ser enviados para cada tipo de contratação:

* **Contratação Direta**  
  **Empresa contratante (cumpridora de cota):**

  - Enviar o**S-2200** com a indicação da categoria **103 - Empregado - Aprendiz**, preenchendo os campos "**indAprend**" (Indicativo da modalidade de contratação) e "**cnpjEntQual**" (CNPJ da entidade qualificadora).

  - Todos os eventos relativos à relação de emprego do aprendiz deverão ser prestados pela empresa (Ex.: alterações contratuais, afastamentos, remunerações, desligamento).
* **Contratação Indireta**  
  **Empresa cumpridora de cota:**  
  - Enviar o **S-1005**  preenchendo o grupo "**infoEntEduc**" (Identificação da(s) entidade(s) educativa(s) ou de prática desportiva)  
    
  **Entidade educativa sem fins lucrativos ou de prática desportiva**:

  - Enviar o**S-2200** com a indicação da categoria **103 - Empregado - Aprendiz**, preenchendo os campos "**indAprend**" (Indicativo da modalidade de contratação), "**tpInsc**" (Tipo de inscrição da entidade) e "**nrInsc**" (número de inscrição da entidade).

  - Todos os eventos relativos à relação de emprego do aprendiz deverão ser prestados pela empresa (Ex.: alterações contratuais, afastamentos, remunerações, desligamento).

**Saiba mais**  
Para saber como e onde preencher as informações do aprendiz para correta geração do S-1005 e do S-2200, acesse:

* [Contratação de Aprendiz - Leiaute S-1.2](https://tdn.totvs.com/pages/viewpage.action?pageId=795092070)
