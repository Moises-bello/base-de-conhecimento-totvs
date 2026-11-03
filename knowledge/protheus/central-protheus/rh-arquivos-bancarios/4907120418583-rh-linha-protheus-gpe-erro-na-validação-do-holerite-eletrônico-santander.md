---
article_id: 4907120418583
category: RH - Arquivos Bancarios
content_hash: aa293d8e9a552a5e9eb56db431cd0f8c7c2d9f9333e1b97927f2660584463783
fetched_at: '2026-06-28T22:43:38.293119+00:00'
product: protheus
section_id: 360004833673
source: central-protheus
title: RH - Linha Protheus - GPE - Erro na validação do Holerite Eletrônico Santander
type: support-article
updated_at: '2025-09-19T22:05:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4907120418583-RH-Linha-Protheus-GPE-Erro-na-valida%C3%A7%C3%A3o-do-Holerite-Eletr%C3%B4nico-Santander
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32324030656919) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Erro na validação do Holerite Eletrônico Santander**.**

**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal– A partir da versão 12.

**Solução**Ao validar o arquivo no banco pagador, é apresentada a mensagem de erro no *layout*:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4903927596567)

**Observação:** Importante que o banco (Gerente de Contas do banco pagador), informe o erro no arquivo, de modo que seja tratado via rotina ou se haverá necessidade de ajustar o arquivo RDMAKE.  
  
No exemplo abaixo , foi identificado o erro no número de convênio , agência e conta do banco pagador:![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5125292688151)  
  
Essas informações, o sistema busca do próprio grupo de perguntas da rotina de geração do Holerite eletrônico Santander.   
Acesse: Miscelânea -> Líquido -> Holerite Eletrônico Santander![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4907170486807)

O arquivo apresentará os dados conforme configurado nas perguntas acima:![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5125013744151)

**Saiba Mais:**

[RH - Linha Protheus - GPE - Geração de Holerite Eletrônico Santander](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035943494)
