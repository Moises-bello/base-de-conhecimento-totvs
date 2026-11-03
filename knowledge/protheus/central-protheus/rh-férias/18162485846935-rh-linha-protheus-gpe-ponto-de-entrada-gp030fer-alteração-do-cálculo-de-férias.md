---
article_id: 18162485846935
category: RH - Férias
content_hash: d9b02ef6baae8a5d4b150cbb6b397fdd022f4a3c0db32d264278037d0f42a677
fetched_at: '2026-06-28T22:43:59.382353+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Ponto de Entrada GP030FER - Alteração do cálculo
  de férias
type: support-article
updated_at: '2025-09-02T17:11:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18162485846935-RH-Linha-Protheus-GPE-Ponto-de-Entrada-GP030FER-Altera%C3%A7%C3%A3o-do-c%C3%A1lculo-de-f%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18162484465943) Tempo aproximado para leitura: **00:01:30 min****Dúvida**Funcionalidade do PE GP030FER - Alteração do cálculo de férias  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução**Ponto-de-Entrada: **GP030FER****- Alteração do Cálculo de Férias**Versões: A partir da Versão   
Microsiga\_Protheus12.1.7  
Compatível Países: Todos  
Sistemas Operacionais: Todos  
Compatível às Bases de Dados: Todos

**Descrição**

O Ponto de Entrada GP030FER permite alterar os valores de férias calculados após a gravação dos dados nas tabelas SRH e SRR.  
  
**Programa Fonte**  
GPEM030.PRW  
GPEM060.PRW  
  
**Sintaxe**GP030FER()  
Parâmetros: Nenhum  
  
**Retorno:** Nil  
  
**Observações**Ao entrar no ponto de entrada a rotina estará posicionada no funcionário (SRA) calculado. Deve ser posicionado na SRH e SRR do funcionário para que as alterações possam ser efetuadas.

**Exemplos**

#Include '[Protheus.ch](http://protheus.ch/)'

User Function GP030FER()

If SRH->(DbSeek(SRA→RA\_FILIAL + SRA→RA\_MAT))

         RecLock("SRH",.F.)  
         SRH→RH\_USERCPO := "Teste"  
         MsUnLock()

EndIf

Return( Nil )

**Saiba Mais**[RH - Linha Protheus - GPE - Pontos de Entrada da rotina de Cálculo de Férias - GPEM030](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053133974-RH-Linha-Protheus-GPE-Pontos-de-Entrada-da-rotina-de-C%C3%A1lculo-de-F%C3%A9rias-GPEM030)

[RH - Linha Protheus - GPE - Pontos de Entrada disponíveis na rotina GPEM060 - Férias Coletivas/Programadas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002601062-RH-Linha-Protheus-GPE-Pontos-de-Entrada-dispon%C3%ADveis-na-rotina-GPEM060-F%C3%A9rias-Coletivas-Programadas)

[GP030FER - Alteração do cálculo de férias](https://tdn.totvs.com/pages/viewpage.action?pageId=675561859)
