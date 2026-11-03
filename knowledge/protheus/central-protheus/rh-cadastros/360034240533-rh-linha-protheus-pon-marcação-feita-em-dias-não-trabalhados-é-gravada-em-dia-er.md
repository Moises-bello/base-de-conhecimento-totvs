---
article_id: 360034240533
category: RH - Cadastros
content_hash: f55df0d32b6fdd3a33831e16140bf6045e2ebb1e0fc2b42e63673a3a3fbcb5b9
fetched_at: '2026-06-28T22:44:53.037131+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Marcação feita em dias Não Trabalhados é gravada
  em dia errado
type: support-article
updated_at: '2026-02-04T19:08:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034240533-RH-Linha-Protheus-PON-Marca%C3%A7%C3%A3o-feita-em-dias-N%C3%A3o-Trabalhados-%C3%A9-gravada-em-dia-errado
---

**Dúvida**  
Marcação feita em dias Não Trabalhados é gravada em dia errado.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Acesse a **Tabela de Horário Padrão, veja detalhes sobre como cadastrar a**[**Tabela de Horário Padrão**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047920293-RH-Linha-Protheus-PON-Tabela-de-Hor%C3%A1rio-Padr%C3%A3o) verifique se a tabela está preenchida com os horários mesmo para os dias **Não Trabalhados** **(Compensado, DSR e Não Trabalhado).**  
  
É necessário **informar um horário** assim como nos dias Trabalhados, para quando houver trabalhado extraordinário nestes dias, o sistema grave as marcações no dia correto e gere os apontamentos.  
Além disso, é necessário se atentar ao conteúdo dos campos de [**Limite Inferior/Superior**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002754861-RH-Linha-Protheus-PON-Funcionalidades-dos-campos-de-Limite-inferior-e-Limite-superior-na-Tabela-de-Hor%C3%A1rio-Padr%C3%A3o)**,** os **valores informados** nestes campos **somados com a carga horária** prevista para o dia **não pode ultrapassar o valor de 23:59**, caso contrário, também poderá ocorrer problemas na gravação das marcações.  
  
Por fim, **mesmo nestes dias**, é necessário que o campo **1ª S. Interv. esteja como Sim, quando houver intervalo definido.**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044243233)  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
