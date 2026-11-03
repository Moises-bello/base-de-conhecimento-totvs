---
article_id: 4410945050007
category: Manutenção de Ativos (SIGAMNT)
content_hash: 330fbc6191c2bd4fcf0f749db618e0e1684b79d5df4cbbb56baf36dc97a399c4
fetched_at: '2026-06-28T22:42:32.921985+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Como funciona o processo de horas realizadas
  no SIGAMNT
type: support-article
updated_at: '2021-11-12T14:09:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410945050007-Manufatura-Linha-Protheus-MNT-Como-funciona-o-processo-de-horas-realizadas-no-SIGAMNT
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:03:15 min****Dúvida**Qual é o conceito e como funcionam as **Horas Realizadas** no **SIGAMNT - Manutenção de Ativos**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Versão 12  
  
**Solução**No módulo de **Manutenção de Ativos** e **Gestão de Frotas**, o conceito de **horas realizadas** está relacionado aos apontamentos na tabela **STL** **- Insumos da O.S.** para o funcionário em questão.  
Se existe algum bloqueio ou restrição por motivo de férias, atestado, afastamento para o funcionário, é validado no momento do apontamento da **O.S**., não permitindo que seja realizado qualquer apontamento para o funcionário durante o período afastado.  
  
Assim, a fórmula das **Horas Realizadas** poderia ser expressada da seguinte forma:

```
Hr = Σ (HrOS)
```

### Onde: **Hr -** Horas realizadas;

**Σ - HrOS -** Soma das horas apontadas como realizadas na **STL** para o tipo de insumo **Mão de Obra**.  
  
**Exemplo**:  
1. Acessar o módulo de **Manutenção de Ativos**  
  
2. Ir em **Atualizações - Cadastros Básicos - Calendário**  - **MATA780**  
  
3. Incluir um calendário com o **Código** **ADM**, possuindo os seguintes intervalos:  
- De **Segunda-feira** até **Sexta-feira**;  
- Das **08h** até **12h** e de **14h** até **18h**.  
  
4. Incluir um **Funcionário da manutenção - MNTA020**  
  
5. Incluir **bloqueio - MNTA160** para o **funcionário**  
  
6. Incluir **O.S. - Ordem de serviço** na rotina **O.S. Corretiva - MNTA420** com as seguintes características:

* **Ordem Serviço - TJ\_ORDEM**: 000001;
* **Data Original - TJ\_DTORIGI**: 05/04/2021;
* **Horário do Sistema**: 08:00;
* **Bem - TJ\_CODBEM**: CAM001;
* **Calendário da Mão de Obra**: **ADM**;

7. No **Retorno de O.S. - MNTA400**, aplicar o funcionário como **Insumo** de **mão de obra** conforme exemplo abaixo:

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **INSUMOS REALIZADOS** | | | | | | |
| **Tipo Insumo****- TL\_TIPOREG** | **Código Insumo - TL\_CODIGO** | **Usa calendário - TL\_USACALE** | **Quantidade - TL\_QUANTID** | **Unidade** | **Data/Hora Início -****TL\_DTINIC/TL\_HOINIC** | **Data/Hora Fim - TL\_DTFIM/TL\_HOFIM** |
| Mão de Obra | MECANICO | Sim | 4 | H | 05/04/2021 - 08:00 | 05/04/2021 - 12:00 |
| Mão de Obra | MECANICO | Sim | 2 | H | 05/04/2021 - 14:00 | 05/04/2021 - 16:00 |

Verificar que as **datas e horas** de início e fim **obedecem** os**intervalos de calendário**.  
  
8. Incluir **O.S. Corretiva** com as seguintes características:

* **Ordem Serviço - TJ\_ORDEM**: 000002;
* **Data Original - TJ\_DTORIGI**: 05/04/2021;
* **Horário do Sistema**: 08:00;
* **Bem - TJ\_CODBEM**: CAM002;
* **Calendário da Mão de Obra**: ADM;

9. Acessar o **Retorno de O.S. Modelo 2 - MNTA435** e apontar um insumo conforme exemplo abaixo:

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **INSUMOS REALIZADOS** | | | | | | |
| **Tipo Insumo****- TL\_TIPOREG** | **Código Insumo - TL\_CODIGO** | **Usa calendário - TL\_USACALE** | **Quantidade - TL\_QUANTID** | **Unidade** | **Data/Hora Início -****TL\_DTINIC/TL\_HOINIC** | **Data/Hora Fim - TL\_DTFIM/TL\_HOFIM** |
| Mão de Obra | MECANICO 001 | Sim | 4 | H | 05/04/2021 - 16:30 | 05/04/2021 - 17:00 |
| Mão de Obra | MECANICO 001 | Sim | 2 | H | 05/04/2021 - 17:00 | 05/04/2021 - 18:00 |

10. Acessar a consulta de **Disponibilidade - MNTC905**:

* Dar duplo clique no **funcionário** em questão.
* Verificar que os **apontamentos realizados** anteriormente foram contabilizados como **Horas Realizadas.**
* Observar que para o dia 05/04/2021 ele realizou 6 horas na **O.S.** 000001 e 1 hora e 30 minutos na **O.S.** 000002, conforme apontamentos na tabela de insumos **STL**, totalizando 7 horas e 30 minutos como **Horas Realizadas**.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **CONSULTA DE DISPONIBILIDADE** | | | | | | | |
| **Data** | **Horas Disponíveis** | **Bloqueios** | **Disponibilidade** | **Horas realizadas** | **Diferença** | **Percentual (%)** | **Horas Extras** |
| 05/04/2021 | 08:00 | 02:00 | 00:00 | 06:00 | 00:00 | 75,00% | 00:00 |
