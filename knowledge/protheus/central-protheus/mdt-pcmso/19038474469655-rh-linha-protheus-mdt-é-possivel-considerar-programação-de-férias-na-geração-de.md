---
article_id: 19038474469655
category: MDT - PCMSO
content_hash: 859f3de191fce59942c99b976e87ef836c55a7688f21a7440c6c7da78b723c28
fetched_at: '2026-06-28T22:44:28.238173+00:00'
product: protheus
section_id: 360010945214
source: central-protheus
title: RH - Linha Protheus - MDT - É possivel considerar programação de férias na
  geração de programação de exames
type: support-article
updated_at: '2025-09-03T12:50:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19038474469655-RH-Linha-Protheus-MDT-%C3%89-possivel-considerar-programa%C3%A7%C3%A3o-de-f%C3%A9rias-na-gera%C3%A7%C3%A3o-de-programa%C3%A7%C3%A3o-de-exames
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19038422141719) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**É possível considerar programação de férias na geração de programação de exames?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**No módulo MDT (35), a rotina **Gerar Programação (MDTA190)** tem como funcionalidade gerar programação de exames para os funcionários.  
  
[Como gerar uma Programação de Exames rotina MDTA190](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059737173)  
  
Para que na geração de exames sejam considerados ou desconsiderados a programação de férias, é necessário que seja feita a configuração do parâmetro **MV\_MDTFERI** no configurador do Protheus.  
  
No configurador (SIGACFG), acesse a rotina de parâmetros através do caminho **Ambiente > Cadastros > Parâmetros,** busque o parâmetro **MV\_MDTFERI.****Valor do parâmetro =** **S:** Considera programação de férias na programação de exames.  
**Valor do parâmetro =** **N**: Não considera  programação de férias na programação de exames.  
  
![FeriasProgramacao.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/19038459569431)  
  
**Saiba mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)
