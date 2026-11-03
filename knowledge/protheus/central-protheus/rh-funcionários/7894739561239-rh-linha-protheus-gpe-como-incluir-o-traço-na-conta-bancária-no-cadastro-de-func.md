---
article_id: 7894739561239
category: RH - Funcionários
content_hash: 11bdd7b83a9a3ac89a49d090aa15188dc0776e7b543bf816f4c685dc72c09501
fetched_at: '2026-06-28T22:43:27.607693+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Como incluir o traço (-) na conta bancária no cadastro
  de funcionário
type: support-article
updated_at: '2025-04-17T17:21:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7894739561239-RH-Linha-Protheus-GPE-Como-incluir-o-tra%C3%A7o-na-conta-banc%C3%A1ria-no-cadastro-de-funcion%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31489611194519) Tempo aproximado para leitura: **00:01:00 min****Dúvida**  
Como incluir o traço (-) na conta bancária no cadastro de funcionário?   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.33  
  
**Solução**  
Para incluir o traço (-) no campo **Cta. Dep. Sal**, realize os seguintes passos:

**1.** No módulo configurador, acesse **Base de dados > Dicionário > Base de dados.  
2.** Busque a tabela SRA e acesse as configurações de campos:   
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7893749760791)  
  
  
**3.** Busque o campo **RA\_CTDEPSA** (Cta. Dep. Sal) e altere o formato para **@!** e clique em Salvar:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7893822558999)

**4.** Aperte em **Confirmar** e depois **Atualizar Base de Dados:**![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7894049781783)

**IMPORTANTE:** Esse ultimo passo deve ser com acesso exclusivo ao sistema:![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7894063996695)

**5.** Após isso, será possível incluir o traço (-) na conta do funcionário:   
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7894382051479)

**Saber Mais:**

[RH - Linha Protheus - GPE - Cadastro funcionário Safrista](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051860553-RH-Linha-Protheus-GPE-Cadastro-funcion%C3%A1rio-Safrista?source=search)

[RH - Linha Protheus - GPE - Onde alterar os dados cadastrais do funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016407931-RH-Linha-Protheus-GPE-Onde-alterar-os-dados-cadastrais-do-funcion%C3%A1rio?source=search)

[RH - Linha Protheus - GPE - Ao alterar uma função no cadastro de funcionário apresenta a mensagem "Não foi possível recuperar o código do cargo"](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403611535255-RH-Linha-Protheus-GPE-Ao-alterar-uma-fun%C3%A7%C3%A3o-no-cadastro-de-funcion%C3%A1rio-apresenta-a-mensagem-N%C3%A3o-foi-poss%C3%ADvel-recuperar-o-c%C3%B3digo-do-cargo-?source=search)

[RH - Linha Protheus - GPE - Criação de Filtro para consulta na SRA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052771373-RH-Linha-Protheus-GPE-Cria%C3%A7%C3%A3o-de-Filtro-para-consulta-na-SRA?source=search)
