---
article_id: 20469849558679
category: Gestão organizacional
content_hash: e2fcbbab2996f43cc19d983e6691f0249753e8e8d9a817fd1bbf7b025fb889fb
fetched_at: '2026-06-28T22:47:22.274282+00:00'
product: rm
section_id: 1500000861422
source: central-rm
title: 'RH - RM - RHU - Processos Trabalhistas: Funcionário com vínculo de emprego
  formalizado em período anterior ao eSocial'
type: support-article
updated_at: '2025-12-16T18:04:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20469849558679-RH-RM-RHU-Processos-Trabalhistas-Funcion%C3%A1rio-com-v%C3%ADnculo-de-emprego-formalizado-em-per%C3%ADodo-anterior-ao-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20469849519383) Tempo aproximado para leitura: **00:03:00 min****Dúvida**

Ao realizar o cadastro do Processo Trabalhista de um Funcionário que possui vínculo formalizado anterior ao eSocial é solicitado o preenchimento da Matrícula, o que fazer?   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - **12.1.34.263**, **12.1.2205.211**, **12.1.2209.155**e superiores.  
  
**Solução**

Quando trata-se de um funcionário com vínculo anterior a obrigatoriedade do eSocial, neste caso, significa que não existem outros eventos para este funcionário. Dessa forma, ao cadastrarem o Contrato de Trabalho, deve informar a opção 'Não' para o campo 'Possui informação no evento S-2190, S-2200 ou S-2300 no declarante?'.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20469838239639)

Ainda assim, deverá criar uma Matrícula para ele que não pertença a nenhum outro funcionário e informar no campo 'Matrícula'.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20469838250135)  
  
A partir do Leiaute S-1.2 também foi incluído o tipo de Contrato de Trabalho: **7** - Trabalhador com vínculo de emprego formalizado em período anterior ao eSocial. Neste caso, deve informar esta opção para os trabalhadores com vínculos anteriores ao eSocial.   
  
Além destes itens, segue trecho orientativo com outras informações estabelecidas pelo Governo e disponibilizadas no [MANUAL DE ORIENTAÇÃO DO ESOCIAL(MOS)](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-1-consolidada-ate-a-no-s-1-1-05-2023.pdf/) sobre o correto preenchimento do Processo Trabalhista quando o funcionário não possui vínculo no eSocial.  
  
***9. Trabalhador com vínculo de emprego formalizado em período anterior ao eSocial***

*d) o grupo [infoCompl] deve ser informado, observando o disposto no item 1.6.2, alínea “b” deste  
evento e ainda:  
d.1) devem ser informadas as datas de admissão e de desligamento originais, salvo o disposto na  
alínea “g” deste item;  
d.2) as evoluções salariais ocorridas durante o período do vínculo não precisam ser informadas neste  
evento; e  
d.3) as demais condições contratuais (CBO, duração do contrato, natureza da atividade etc) previstas  
no grupo [infoCompl] devem ser prestadas considerando a informação mais atual;  
e) as informações cadastrais do trabalhador devem refletir a condição vigente a época do trânsito em  
julgado ou da celebração do acordo. Por exemplo, estado civil. A informação relativa aos dependentes  
não precisa ser prestada neste evento;  
f) as alterações de categoria e de natureza da atividade ocorridas ao longo do contrato de trabalho  
devem ser informadas no grupo [mudCategAtiv], conforme orientações constantes no item 5 deste  
evento, observando que o campo {dtMudCategAtiv} deve ser preenchido com data posterior à data  
de admissão e  
g) se a decisão ou acordo reconhecer alteração de data de admissão, o campo {dtAdmOrig} deve ser  
preenchido com a data original e o campo {dtAdm} com a data de admissão reconhecida.  
9.2. Caso o declarante, em alguma das hipóteses exigidas (pagamento de remuneração posterior ao  
desligamento, por exemplo), tenha enviado o evento S-2200 referente ao vínculo extinto antes do  
início da obrigatoriedade do envio dos eventos não periódicos do eSocial, o declarante deve observar  
as seguintes peculiaridades:  
a) o campo {indContr} deve ser preenchido com [S];  
b) deve ser informada a mesma matricula já utilizada no evento S-2200;  
c) o grupo [infoCompl] não deve ser preenchido; e  
d) eventuais alterações contratuais ocorridas no período contratual devem ser informadas por meio  
do envio dos correspondentes eventos S-2206.*

**Saiba mais**Para maiores informações sobre os cadastros, acesse os links abaixo:

     - [RH - RM - RHU - eSocial: Processos Trabalhistas - Perguntas e respostas do evento webinar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18727698331543)  
     - [RH - RM - RHU - eSocial: S-2500 - Mapeamento dos campos para geração do evento S-2500](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18256276341783)  
     - [RH - RM - RHU - eSocial: S-2501 - Mapeamento dos campos para geração do evento S-2501](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18863423016855)  
     - [RH - RM - RHU - Dúvidas frequentes: geração dos eventos de Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17623656599575)
