---
article_id: 18981445665687
category: MDT - PCMSO
content_hash: dd892ff30d7656b45b9f9d3e07bb634d40377440554d9add1b4aea2f632a5001
fetched_at: '2026-06-28T22:44:28.244644+00:00'
product: protheus
section_id: 360010945214
source: central-protheus
title: RH - Linha Protheus - MDT - É possível desconsiderar funcionários afastados
  na Programação de Exames
type: support-article
updated_at: '2025-09-03T12:50:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18981445665687-RH-Linha-Protheus-MDT-%C3%89-poss%C3%ADvel-desconsiderar-funcion%C3%A1rios-afastados-na-Programa%C3%A7%C3%A3o-de-Exames
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18981435642775) Tempo aproximado para leitura: **00:02:00min** **Dúvida**É possível desconsiderar funcionários afastados na Programação de Exames?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**No módulo MDT (35), a rotina **Gerar Programação (MDTA190)** tem como funcionalidade gerar programação de exames para os funcionários.  
  
[Como gerar uma Programação de Exames rotina MDTA190](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059737173)  
  
Para que na geração de exames sejam considerados ou desconsiderados funcionários afastados, é necessário que seja feita a configuração do parâmetro **MV\_NGMDTVA** no configurador do Protheus.  
  
No configurador (SIGACFG), acesse a rotina de parâmetros através do caminho **Ambiente > Cadastros > Parâmetros,** busque o parâmetro **MV\_NGMDTVA.****Valor do parâmetro =** **1** : Considera afastados na programação de exames.  
**Valor do parâmetro =** **2** : Desconsidera afastados na programação de exames.  
  
![Afastado.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18981483132951) **Saiba mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)
