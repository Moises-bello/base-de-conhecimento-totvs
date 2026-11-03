---
article_id: 5866827935639
category: CIPA
content_hash: d6b7f88cfdbec68323d5ad2246740b06fddb5540efaa5c5ea04efd3bfc5906ac
fetched_at: '2026-06-28T22:47:37.666742+00:00'
product: rm
section_id: 1500001076482
source: central-rm
title: RH - RM - SMT - Representantes Empregado e Representantes Empregador na CIPA
type: support-article
updated_at: '2025-12-16T17:14:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5866827935639-RH-RM-SMT-Representantes-Empregado-e-Representantes-Empregador-na-CIPA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16035563482775) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Quais a diferenças entre os representantes dos empregados e os representantes do empregador na CIPA - Comissão Interna de Prevenção de Acidentes ?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Segurança e Saúde Ocupacional – Todas as versões  
  
**Solução**

A CIPA é formada por representantes do empregador e dos empregados. **O representante do empregador (titulares e suplentes) é designado pela empresa, e o representante dos empregados (titulares e suplentes) serão eleitos através de voto secreto.** E juntos irão representar na comissão da CIPA os interesses dos colaboradores em geral, com a finalidade de estabelecer diálogos e esclarecimentos direto com o empregador, promovendo a boa-fé e o respeito mútuo. Em relação a **estabilidade**, a **mesma se estende somente ao eleitos pelos empregados**, e irá se comportar da seguinte forma:

Após o **cadastro do Representante** é realizada uma integração com o sistema Folha de Pagamento (RM Labore), registrando a sua estabilidade. Para verificar a estabilidade acesse **Acompanhamento | Funcionários, Anexo Folha de Pagamento | Estabilidade.**

* Se o Representante foi cadastrado com o tipo 14 (Candidato Representante dos Funcionários) ele gera a estabilidade com as datas de início e fim da candidatura.
* Se o Representante foi cadastrado com o tipo 15 (Eleito Titular Representante dos Funcionários) ele gera a estabilidade com a data de início da candidatura e data fim do mandato, este acrescido de mais 1 ano.
* Se o Representante foi cadastrado com o tipo 16 (Eleito Suplente Representante dos Funcionários) ele gera a estabilidade com a data de início da candidatura e data fim do mandato, este acrescido de mais 1 ano. Quando incluir a Data de exoneração do Representante, ele finaliza a estabilidade com esta data.
* Se o Representante for excluído da Comissão, os registros da estabilidade também são excluídos. **Obs.:** **A estabilidade, não se estende para designados representantes pela empresa (empregador).**   
  Ao eleger um representante pelos empregados, este funcionário terá a flag **Membro CIPA** marcada em seu cadastro de Funcionário.  Quando o usuário utilizar o Gestão de Pessoas, e o funcionário for representante ou ex-representante da CIPA, será apresentada uma mensagem observando o seguinte critério:

* Até a competência que o funcionário tiver estabilidade será apresentada uma mensagem com a data fim e o motivo da estabilidade.

Para competências posteriores, apenas será apresentada uma mensagem informando que o funcionário já foi membro ou candidato nas eleições da CIPA.

**Atenção:**  
1.    Este campo ficará desabilitado para o usuário, caso a Coligada tenha o Gestão de Pessoas instalado, já que, os controles serão feitos por este sistema. O controle de estabilidade do funcionário, em caso de rescisão, também será feito pelo Gestão de Pessoas. Ou seja, se o funcionário é candidato ou Membro da CIPA ou ainda tem estabilidade após um ano do término da vigência da comissão em que ele foi eleito como representante dos funcionários, o RM Labore bloqueará sua demissão com uma mensagem de alerta.  
  
2.    O RM Labore também atualiza este campo durante a Liberação da Competência de acordo com os dados do Gestão de Pessoas. Se a comissão terminou na competência que está sendo liberada, o sistema desmarcará o campo "Membro da CIPA" (cadastro do funcionário) para a próxima competência. Se a base não tem o Gestão de Pessoas instalado, o controle para este campo deverá ser feito manualmente.

**Saiba Mais:**  
[Mandato membro da CIPA como representante do empregador](https://tdn.totvs.com/display/public/ConSeg/Mandato+membro+da+CIPA+como+representante+do+empregador)  
[Reforma Trabalhista - Comissão de Empregados - Direitos e Estabilidades](https://tdn.totvs.com/pages/releaseview.action?pageId=307834061)  
[CIPA - Perda de Estabilidade de Funcionário Cipeiro](https://tdn.totvs.com/pages/releaseview.action?pageId=590242699)  
[Representante de Empregado](https://tdn.totvs.com/display/LRM/Representante+de+Empregado)  
[NR-5 COMISSÃO INTERNA DE PREVENÇÃO DE ACIDENTES](http://www.guiatrabalhista.com.br/legislacao/nr/nr5.htm)  
[TOTVS RH - Linha RM - SMT - Representante CIPA (Comissão Interna de Prevenção de Acidentes)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019180312-TOTVS-RH-Linha-RM-SMT-Representante-CIPA-Comiss%C3%A3o-Interna-de-Preven%C3%A7%C3%A3o-de-Acidentes-)  
[Flag Membro CIPA](https://tdn.totvs.com.br/display/public/LRM/CIPA)
