---
article_id: 35862760092055
category: SIGAEST - RELATORIOS
content_hash: 04ad999600d6dacf44d59cdb11fb9f3e2a2b1b99269ce889799225ffa1f80a47
fetched_at: '2026-06-28T22:39:06.110187+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR282 - Concorrencia
  - Ja esta sendo usado por outro usuario
type: support-article
updated_at: '2025-10-24T18:49:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35862760092055-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR282-Concorrencia-Ja-esta-sendo-usado-por-outro-usuario
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35862720605335) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Ao tentar gerar o relatorio MATR282 é informado que esta sendo usado por outro usuario.

Concorrencia - A filial X da empresa corrente já esta sendo utilizada na impressão do relatorio.

![Screenshot_5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35863116740759)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Solicite ao outro usuario que feche o relatorio que talvez esteja em aberto, avaliando através do dbmonitor, só pode existir 1 relatorio por empresa utilizavel:

![Screenshot_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35863116745239)

Caso não exista mais de 1 usuario, avalie se o arquivo com nome do relatorio consta na pasta spool do ambiente, então efetue a alteração do nome para matr282\_old, e após teste novamente.

![Screenshot_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35863105598871)

Se mesmo assim, constar ainda uso da sessão do relatorio em aberto, apague o arquivo gerado na pasta spool, reinicie o serviços (appserver) e realize um novo teste.

**Saiba mais:**

[*SIGAEST - MATR282 - Como incluir o relatório MATR282 no menu*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000317301-SIGAEST-MATR282-Como-incluir-o-relat%C3%B3rio-MATR282-no-menu)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Tratamento correto de desbalanceamento de tabelas de Lote e Endereço em todos os cenários*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402491211159)

[*Clique aqui e veja mais artigos sobre Relatórios do Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012224673-SIGAEST-RELATORIOS)
