---
article_id: 360060011053
category: RH - Funcionários
content_hash: 34d952f52f0a1802d79a1c3d7750745958a58e2f13a25f941c06964243316578
fetched_at: '2026-06-28T22:43:27.372377+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Ao tentar informar conteúdo no campo Cat. E-social
  - RA_CATEFD, ocorre mensagem que não existe a tabela
type: support-article
updated_at: '2025-09-15T18:09:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060011053-RH-Linha-Protheus-GPE-Ao-tentar-informar-conte%C3%BAdo-no-campo-Cat-E-social-RA-CATEFD-ocorre-mensagem-que-n%C3%A3o-existe-a-tabela
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27256528891159) Tempo aproximado para leitura: **00:01:30 min****Ocorrência**No módulo Gestão de Pessoal, ao tentar informar conteúdo no campo Cat. E-social - RA\_CATEFD, ocorre mensagem que não existe a tabela.

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Esse incidente ocorre, pois não foi feita a carga na tabela de Categorias do E-social - Tabela S049  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100807133)  
Para solucionar essa ocorrência, realize os seguintes passos:  
  
**1.** Acesse primeiramente o menu **Atualizações > Definições de Cálculo > Definição de Tabelas (GPEA310)** apenas para realizar a carga das tabelas. Assim que a tela for carregada, você já pode sair da rotina.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27256528892823)  
  
**2.** Em seguida, acesse **Atualizações > Definições de Cálculo > Manutenção de Tabelas (GPEA320)** apenas para realizar a carga dos dados. Após a tela ser carregada, pode sair da rotina.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27256515931671)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27256528897047)  
  
**3.** Após esse processo os dados serão carregados e, ao acessar novamente o cadastro do funcionário **Atualizações > Funcionários > Funcionários (GPEA010),** conseguirá amarrar o código no campo RA\_CATEFD com os dados da tabela S049.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27256528902935)

**Saiba mais:**

[RH - Linha Protheus - GPE - Como realizar o cadastro/admissão de funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404568864151-RH-Linha-Protheus-GPE-Como-realizar-o-cadastro-admiss%C3%A3o-de-funcion%C3%A1rio)  
[RH - Linha Protheus - GPE - Quais os parâmetros utilizados para o cadastro de funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9138402927639-RH-Linha-Protheus-GPE-Quais-os-par%C3%A2metros-utilizados-para-o-cadastro-de-funcion%C3%A1rios)  
[RH - Linha Protheus - GPE - Como realizar a cópia do cadastro do funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412275775895-RH-Linha-Protheus-GPE-Como-realizar-a-c%C3%B3pia-do-cadastro-do-funcion%C3%A1rio)
