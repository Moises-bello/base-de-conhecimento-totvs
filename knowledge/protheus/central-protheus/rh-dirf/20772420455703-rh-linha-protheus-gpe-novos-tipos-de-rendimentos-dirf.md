---
article_id: 20772420455703
category: RH – DIRF
content_hash: a9e2b5abcb23b4370dcbac776b0c5862004547f47295a705f209c5bf76d1edf9
fetched_at: '2026-06-28T22:44:07.072078+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: 'RH - Linha Protheus - GPE - Novos Tipos de Rendimentos DIRF '
type: support-article
updated_at: '2024-02-07T18:18:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20772420455703-RH-Linha-Protheus-GPE-Novos-Tipos-de-Rendimentos-DIRF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20772451218583) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Quais são os Novos Tipos de Rendimentos para a DIRF?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus - Gestão de Pessoal - À partir do release 12.1.33  
  
**Solução**Conforme novo Leiaute da DIRF 2024, será utilizada uma nova coluna para a Dedução Simplificada e para isso os valores deverão estar vinculados à novos Tipos de Rendimento na tabela genérica 36.

Para atender a essa necessidade será gravado na tabela genérica 36 - Tipos de Rendimentos os tipos:

* B4 Dedução modelo simplificado Folha
* B5 Dedução modelo simplificado Folha 13º
* B6 Tributação com exigibilidade suspensa - Dedução - Desconto Simplificado Mensal

Eles deverão ser vinculados aos identificadores abaixo através do campo "**DIRF**" (RV\_DIRF) no cadastro da verba:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20772451222423)

**Importante:**   
O Tipo de Rendimento B6 deve ser associado à verba (sem identificador de cálculo) utilizada pelo cliente.

Esta implementação de dicionário está disponível na Expedição Contínua do RH à partir do dia 22/01/2024.  
Para acessar o pacote RH Expedição Contínua [Clique Aqui](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/RH_EXPEDICAO_CONTINUA) .

O cliente deve aplicar os fontes e dicionário da expedição em seu ambiente para criação dos novos tipos de rendimento, mas também é possível incluir manualmente conforme instrução abaixo:

1. No Configurador, acesse a rotina Tabelas pelo caminho >Ambiente >Cadastros >Tabelas;  
2. Pesquise pela Tabela 36 e clique em Editar:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21190615475095)  
  
3. Clique em Itens, vá até o último registro da tabela e com a seta para baixo inclua uma nova linha para cada novo tipo de rendimento B4, B5 e B6 conforme exemplo abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21190560664727)

4. Salve a alteração no botão Confirmar:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21190615508759)

Detalhes do ajuste:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21190615523991)

Saiba mais:  
[DIRF - Novos Tipos de Rendimentos](https://tdn.totvs.com/pages/releaseview.action?pageId=819056237)

[RH - DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF)
