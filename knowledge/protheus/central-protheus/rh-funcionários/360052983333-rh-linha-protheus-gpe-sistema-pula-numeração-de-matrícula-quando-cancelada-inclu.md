---
article_id: 360052983333
category: RH - Funcionários
content_hash: c95c5d2e08eaf8b5b885bcddccf1a39030e9665fd96b996b7ed93861f702d34c
fetched_at: '2026-06-28T22:43:27.286498+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE -  Sistema pula numeração de matrícula quando cancelada
  inclusão de funcionário
type: support-article
updated_at: '2025-08-18T19:36:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052983333-RH-Linha-Protheus-GPE-Sistema-pula-numera%C3%A7%C3%A3o-de-matr%C3%ADcula-quando-cancelada-inclus%C3%A3o-de-funcion%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31673155130391)** Tempo aproximado para leitura: **00:02:00 min**

**Ocorrência**No módulo Gestão de Pessoal, quando há configuração para numeração automática, Sistema pula numeração de matrícula quando **cancelada inclusão de funcionário e solicitada nova inclusão em seguida.**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**Esse incidente ocorre, pois existe **validação** **incorreta** na SRA, no campo **Inici. Padrão do RA\_MAT.**

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Através do ambiente **Configurador** acesse a rotina **Base de Dados > Dicionário > Base de Dados;**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084167454)  
  
2. Clique em expandir e selecione a opção **Dicionário de Dados;**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084167574)  
  
3. Clique no **ícone da lupa** e busque pela tabela **SRA**;

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085356173)

4. Clique no ícone **editar**, expanda as opções da tabela e selecione a opção **campos**;

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085356373)

5. Posicione o **cursor em cima** do campo **RA\_MAT** e clique no **ícone editar;**6. Na caixa de diálogo aberta, selecione a aba **Opções, limpe o conteúdo do campo Inic. Padrão e clique em Salvar;**

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085357133)

7. Para **gravar as alterações**, primeiramente **clique em salvar** na caixa de diálogo e posteriormente no ícone de Atualização da base de dados;

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084169334)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085357653)

8. Clique em **avançar** na tela seguinte;

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084169454)

9. E finalize a gravação do processo.

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084169774)

**Importante**  
Após ajustes, saia do Sistema e acesse-o novamente.

**Para saber mais**[RH - Linha Protheus - GPE - Configuração para Matrícula automática de funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028979231)

[RH - Linha Protheus - GPE - Inclusão de funcionário com matrícula incorreta](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051186933-MP-GPE-Inclus%C3%A3o-de-funcion%C3%A1rio-com-matr%C3%ADcula-incorreta-?source=search)
