---
article_id: 360050903073
category: Inspeção de Processos (SIGAQIP)
content_hash: d2f5bb12bd502feac07b67e8c32f8cdeeb46df6f4cc8ca123ec5d2980c4627f1
fetched_at: '2026-06-28T22:42:25.947346+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Validações no campo Data Medição da
  rotina QIPA215
type: support-article
updated_at: '2021-10-01T13:16:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050903073-Manufatura-Linha-Protheus-SIGAQIP-Valida%C3%A7%C3%B5es-no-campo-Data-Medi%C3%A7%C3%A3o-da-rotina-QIPA215
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min**  
**Dúvida**Quais as validações realizadas no campo **Data Medição** da rotina **QIPA215 - Resultados** para que seja possível alterar a data sugerida pelo Sistema?  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Solução**A alteração no campo **QPR\_DTMEDI - Data Medição** está relacionada com o conteúdo do parâmetro **MV\_QVLDTHR - Validação a ser efetuada da Data e Hora**.  
Este parâmetro aceita as opções:

* **1 - Validação completa** - será consistido além das datas, as horas e minutos;
* **2 - Data Medição >= Data OP**;
* **3 - Data Medição >= Database >= Data OP**.

**Onde**:

* **Data Medição**: tabela **QPR - Medições**, campo **QPR\_DTMEDI**;
* **Data OP**: tabela **SC2 - Ordem de Produção**, campo **C2\_EMISSAO - Dt Emissão**;
* **Database**: data base do **Protheus**.
