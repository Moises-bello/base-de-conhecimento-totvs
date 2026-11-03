---
article_id: 23170014421911
category: eSocial - Tabelas/Não Periódicos
content_hash: 668d6de101854611a90ec911ca21d7a8f9d25caeb8b17172919706b9c6fe5fee
fetched_at: '2026-06-28T22:47:10.168888+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: RH - RM - FOP - eSocial - Erro código 1898 - Matricula do trabalhador no empregador
  anterior inválida
type: support-article
updated_at: '2026-06-01T17:30:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23170014421911-RH-RM-FOP-eSocial-Erro-c%C3%B3digo-1898-Matricula-do-trabalhador-no-empregador-anterior-inv%C3%A1lida
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23170029827991) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao transmitir o evento S-2200 de uma transferência para o governo e retornado a inconsistência: **O evento ID"xxxx" foi rejeitado pelo RET.  Erro código 1898: Matricula do trabalhador no empregador anterior inválida.**  
  
**Ambiente**  
TOTVS RH - TOTVS RH ( Linha RM ) - eSocial - Todas as versões.  
  
**Causa**  
Esse incidente ocorre quando a matricula anterior (do primeiro vinculo, que está demitido) esta divergente do que foi enviado na primeira admissão.  
  
**Solução**  
Revise as matriculas de admissão do S-2200 atual e do S-2200 antigo, as matriculas dos vínculos deveram estar de acordo. Esse campo  'matricAnt' - Matricula anterior foi alterado na NT 01/2023 do leiaute S-1.2, passando a seguir a regra abaixo de geração de acordo com o leiaute.

![image (1).png](https://centraldeatendimento.totvs.com/hc/article_attachments/23170014413079)

Se caso o S-2200 estiver com a data de transferência 22/04/2024, que e igual a data mencionada na validação do campo, este evento não e uma carga inicial(cadINI=N), ou seja, é obrigado a gerar a tag.

No entanto as informações estando corretas será necessário entrar em contato com o suporte do governo.

[Contato com o Governo para dúvidas sobre os eventos do eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004050432-RH-RM-FOP-eSocial-Contato-com-o-Governo-para-d%C3%BAvidas-sobre-os-eventos-do-eSocial?source=search)
