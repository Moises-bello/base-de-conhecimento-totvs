---
content_hash: 37a0b524996d69fc5f5605e29f2dbc1dcbe779ff577da2966832fff8a7b081a9
fetched_at: '2026-06-29T00:10:10.559564+00:00'
page_id: '452719875'
product: rm
source: tdn-rm
title: CIPA
type: documentation
url: https://tdn.totvs.com/display/LRM/CIPA
version: 3
---

A Comissão Interna de Prevenção de Acidentes (CIPA) é para tratar da prevenção de acidentes do trabalho, das condições do ambiente do trabalho e de todos os aspectos que afetam a saúde e segurança do trabalhador. A CIPA é regulamentada pela Consolidação das Leis do Trabalho (CLT).  
   
**Dados da CIPA:**  
Membro da CIPA é para registrar se o funcionário é ou não membro da CIPA. Esta informação serve para alertar o usuário caso queira demitir um funcionário que tenha estabilidade e para utilizá-lo deverá:  
   
Criar fórmula:  
**SE TABFUNC('MEMBROCIPA','V') = 1**   
**ENTAO 1**  
**SENAO 0**  
**FIMSE**  
Informar o código da fórmula criada em Cadastros | Sindicatos campo "Fórmula de Estabilidade". Após a confirmação da demissão o sistema emitirá a mensagem: "Este funcionário possuem estabilidade garantida segundo a fórmula cadastrada no sindicato XXX ", onde XXX será o código do sindicato.  
   
**Observação:**  
Quando o usuário utilizar o Gestão de Pessoas, e o funcionário for representante ou ex-representante da CIPA, será apresentada uma mensagem observando o seguinte critério:

* Até a competência que o funcionário tiver estabilidade será apresentada uma mensagem com a data fim e o motivo da estabilidade.
* Para competências posteriores, apenas será apresentada uma mensagem informando que o funcionário já foi membro ou candidato nas eleições da CIPA.

 **Atenção:**  
1.    Este campo ficará desabilitado para o usuário, caso a Coligada tenha o Gestão de Pessoas instalado, já que, os controles serão feitos por este sistema. O controle de estabilidade do funcionário, em caso de rescisão, também será feito pelo Gestão de Pessoas. Ou seja, se o funcionário é candidato ou Membro da CIPA ou ainda tem estabilidade após um ano do término da vigência da comissão em que ele foi eleito como representante dos funcionários, o RM Labore bloqueará sua demissão com uma mensagem de alerta.  
2.    O RM Labore também atualiza este campo durante a Liberação da Competência de acordo com os dados do Gestão de Pessoas. Se a comissão terminou na competência que está sendo liberada, o sistema desmarcará o campo "Membro da CIPA" (cadastro do funcionário) para a próxima competência. Se a base não tem o Gestão de Pessoas instalado, o controle para este campo deverá ser feito manualmente.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Funcionários
