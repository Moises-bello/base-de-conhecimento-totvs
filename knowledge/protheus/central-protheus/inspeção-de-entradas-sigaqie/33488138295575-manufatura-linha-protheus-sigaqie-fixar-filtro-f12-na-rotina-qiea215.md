---
article_id: 33488138295575
category: Inspeção de Entradas (SIGAQIE)
content_hash: 111bb65bc04159a55676e045ef608f33dd8664ea3a3a7e5281b3743e6b5ce7ef
fetched_at: '2026-06-28T22:42:26.966402+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Fixar filtro F12 na rotina QIEA215
type: support-article
updated_at: '2025-07-15T20:54:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33488138295575-Manufatura-Linha-Protheus-SIGAQIE-Fixar-filtro-F12-na-rotina-QIEA215
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33488138280087) Tempo aproximado para leitura: **00:00:52 min**  
  
**Dúvida**  
Na rotina **QIEA215 - Resultados**, ao utilizar o filtro via tecla **F12**, como **fixar o filtro em tela** após sair da rotina e acessá-la novamente?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Todas as versões  
  
**Solução**  
Para fixar o filtro **F12** na rotina **QIEA215 - Resultados,** o parâmetro **MV\_QFILENT - Indica se o filtro das entradas inspecionadas e/ou a inspecionar será realizado antes da exibição do browse** deve ter o **conteúdo igual .T. - True**, e o campo do perguntes do filtro F12 **Desliga o Filtro** deve ter o conteúdo igual a **Não**. Deste modo, ao entrar na rotina **QIEA215** é aplicado o filtro conforme selecionado no F12.
