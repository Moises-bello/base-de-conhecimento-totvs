---
article_id: 360041812553
category: Manutenção de Ativos (SIGAMNT)
content_hash: 9de90ac45c766825e4bca827523a7758edbe5c0ed4acb9715b77da74f07d1bd3
fetched_at: '2026-06-28T22:42:34.369031+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Processo de Tolerância na Manutenção
type: support-article
updated_at: '2021-09-21T20:51:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041812553-Manufatura-Linha-Protheus-MNT-Processo-de-Toler%C3%A2ncia-na-Manuten%C3%A7%C3%A3o
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:03:30 min**  
**Dúvida**Como funciona o processo de tolerância na manutenção?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**O controle de tolerância de uma manutenção pode ser por **Tempo - TF\_TOLERA** e/ou por **Contador -  TF\_TOLECON**. Estes campos permitem definir um período de antecedência no qual o Sistema passa a indicar a proximidade da data de início da manutenção, que pode ser por meio de envio de *Workflow* na rotina **MNTW020 - Alerta de O.S. Preventiva a Vencer**, relatórios de **Manutenção a Vencer - MNTR011** e **Equipamentos Sujeitos à Manutenção - MNTR030**, legenda da **Manutenção - MNTA120** e geração de **O.S. automática**. Este processo possibilita um melhor planejamento para a execução da manutenção, antecipando a geração da ordem de serviço preventiva do bem, permitindo ao planejador da manutenção, programar todos os recursos necessários com antecedência para a execução da manutenção:

* *Workflows* na rotina **MNTW020 - Alerta de O.S Preventiva a Vencer**;
* Relatórios nos programas **MNTR011 - Manutenção a Vencer** e **MNTR030 - Equipamentos Sujeitos à Manutenção**;
* E indicativos visuais como legendas.

**Exemplo 1:**  Aplicação do controle por **Tempo**:  
Nesta simulação será consideração que a data atual é:**03/03/2021**

| Bem |
| --- |
| VEICULO-001 |

| Dt. última manutenção - TF\_DTULTMA | Incremento da manut. - TF\_TEENMAN | Unid. manut. - TF\_UNENMAN | Dt. prevista para prox. manut. | Tolerância - TF\_TOLERA |
| --- | --- | --- | --- | --- |
| 08/02/2021 | 1 | Mês | 08/03/2021 | 5 Dias |

A legenda da **Manutenção - MNTA120** ficará na cor **amarela**, indicando que está próxima a vencer, permanecendo do dia **03/03/2021** até **08/03/2021**. Após esse período, a legenda ficará **vermelha**, indicando que a manutenção está vencida.  
  
Caso esteja parametrizado para a geração de **O.S. -** **Ordem de Serviço** automática, neste dia será gerado a **O.S.** no dia**03/03/2021** com data prevista inicio **08/03/2021**, permitindo assim o planejador tomar ações necessárias para sua execução.   
  
**Exemplo 2:** Aplicação do controle por **Contador**:  
Nesta simulação será considerado que a data atual é: **03/03/2021**

| Bem | Dt. último acompanhamento - T9\_DTULTAC | Contador acumulado - T9\_CONTACU | Varição dia - T9\_VARDIA |
| --- | --- | --- | --- |
| VEICULO-002 | 02/03/2021 | 59.000 | 250 |

| Contador última manut. - TF\_CONMANU | Incremento de contador - TF\_INENMAN | Contador da prox. manut. | Dt. prevista para prox. manut. | Tolerância - TF\_TOLECON |
| --- | --- | --- | --- | --- |
| 50.000 | 10.000 | 60.000 | 06/03/2021 | 1.000 |

A legenda da **Manutenção - MNTA120**, ficará na cor **amarela**, indicando que está próxima a vencer, permanecendo do dia **03/03/2021** até **06/03/2021**. Após esse período, a legenda ficará **vermelha**, indicando que a manutenção está vencida.  
  
Caso esteja parametrizado para a geração de **O.S. automática**, neste dia será gerado a **O.S.** no dia **03/03/2021** com data prevista inicio **06/03/2021**, permitindo assim o planejador tomar ações necessárias para sua execução.   
  
**Importante**Após o Sistema calcular a **Data da próxima manutenção** será classificado como **Atrasada**, **A Vencer** ou **Em Dia** sendo que:

* **Atrasada**:  Ocorre quando a data da próxima manutenção é menor que a data atual.
* **A Vencer**: Ocorre quando a data da próxima manutenção é igual ou maior que a data atual e menor que a data atual somando a tolerância.
* **Em Dia**: Ocorre quando a data da próxima manutenção é igual ou maior que a data atual e maior que a data atual somando a tolerância.

**Saiba mais**Para informações complementares, acesse os artigos:  
[Parametrização para gerar O.S de forma automática](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025947072)  
[Cálculo da próxima manutenção quando controlado por 1 ou 2 contadores](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057396894)
