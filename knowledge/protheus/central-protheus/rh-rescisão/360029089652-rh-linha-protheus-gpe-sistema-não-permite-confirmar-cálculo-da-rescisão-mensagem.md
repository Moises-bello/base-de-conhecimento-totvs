---
article_id: 360029089652
category: RH - Rescisão
content_hash: c1aa68a7d8dbc368e0bf165e651c99d166a711396b82ad9515451ba75bcc0978
fetched_at: '2026-06-28T22:43:50.924222+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Sistema não permite confirmar cálculo da rescisão
  - Mensagem "Existem campos obrigatórios não preenchidos"
type: support-article
updated_at: '2025-07-15T18:24:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029089652-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-permite-confirmar-c%C3%A1lculo-da-rescis%C3%A3o-Mensagem-Existem-campos-obrigat%C3%B3rios-n%C3%A3o-preenchidos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33487592424343) Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Ao tentar confirmar o cálculo de uma rescisão, sistema apresenta a mensagem "Não é possível completar a ação. Existem campos obrigatórios não preenchidos"  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030651551)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Versão 12  
  
**Solução**Esse erro ocorre por conta de divergência na estrutura da tabela SRG, onde a coluna X3\_RESERV para algum campo esta diferente do padrão, fazendo com que não seja possível gravar a rescisão.  
Abaixo exemplo do padrão do sistema de como deve estar parametrizado a coluna **X3\_RESERV** para cada campo da tabela SRG:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| x3\_ordem | x3\_campo | x3\_tipo | x3\_titulo | x3\_reserv |
| 1 | RG\_FILIAL | C | Filial | €€ |
| 2 | RG\_MAT | C | Matricula | ƒ€ |
| 3 | RG\_NOME | C | Nome | ƒ€ |
| 4 | RG\_EFETIVA | C | Resc.Efetiv. | †€ |
| 5 | RG\_SABDOM | C | Pg Sab/Dom? | †À |
| 6 | RG\_TIPORES | C | Tipo Resc. | “€ |
| 7 | RG\_DESCTPR | C | Desc.Tp.Resc | „€ |
| 8 | RG\_DTAVISO | D | Data Aviso | € |
| 9 | RG\_DAVISO | N | Aviso Previo | –€ |
| 10 | RG\_DAVCUM | N | Aviso Cump. | „€ |
| 11 | RG\_DAVIND | N | Aviso Inde. | „€ |
| 12 | RG\_DATADEM | D | Dt. Demissao | ƒ€ |
| 13 | RG\_DATAHOM | D | Dt. Homologa | “€ |
| 14 | RG\_DTGERAR | D | Data Geracao | ‘€ |
| 15 | RG\_MEDATU | C | Mes p/Media | †À |
| 16 | RG\_DFERVEN | N | Dias Fer.Ven | € |
| 17 | RG\_DFERPRO | N | Dias Fer.Pro | € |
| 18 | RG\_DFERAVI | N | Dias Fer Avi | –À |
| 19 | RG\_NORMAL | N | Hrs.Normais | ƒ€ |
| 20 | RG\_DESCANS | N | Hrs. D.S.R. | ƒ€ |
| 21 | RG\_SALMES | N | Salario Mes | ’€ |
| 22 | RG\_SALDIA | N | Salario Dia | ’€ |
| 23 | RG\_SALHORA | N | Salario Hora | ’€ |
| 24 | RG\_PROCES | C | Cod.Processo | †€ |
| 25 | RG\_COMPRAV | C | Comp.N.Empr. | –À |
| 26 | RG\_JTCUMPR | C | Jor.Trabalho | ‡€ |
| 27 | RG\_RHEXP | C | Contr.Exp.RH | „€ |
| 28 | RG\_IDCMPL | C | ID.Comp. | „€ |
| 29 | RG\_RESCDIS | C | Tp. Resc. | „€ |
| 30 | RG\_RRA | C | Control.RRA | „€ |
| 31 | RG\_TPAVISO | C | Tipo Aviso | ”€ |
| 32 | RG\_NPROC | C | Nº Processo | „€ |
| 33 | RG\_OBITO | C | Atest. óbito | ž€ |
| 34 | RG\_PERIODO | C | Periodo | ‡€ |
| 35 | RG\_SUCES | C | CNPJ Emp.Suc | „€ |
| 36 | RG\_OBS | C | Observação | „€ |
| 37 | RG\_ROTEIR | C | Roteiro Calc | „€ |
| 38 | RG\_SEMANA | C | Nr. Semana | –À |
| 39 | RG\_TPDIR | C | Tp Resc Dire | „€ |
| 40 | RG\_DTPROAV | D | Dt Projetada | Ä€ |
| 41 | RG\_INDAV | C | Ind.Cum.Av.P | „€ |
| 42 | RG\_PDRESC | C | Vb.Res.Comp. | „€ |
| 43 | RG\_NPROCS | C | P.C.Social | „€ |

**Saiba mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
