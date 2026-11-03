---
article_id: 30084782592919
category: Avaliação e Pesquisa de Desempenho (SIGAAPD)
content_hash: 8b3e89dec3d20f8d3d467323c4a7b47e3e1c0d4ec58471139157c79cd4aae77b
fetched_at: '2026-06-28T22:42:53.875661+00:00'
product: protheus
section_id: 206956088
source: central-protheus
title: RH - Linha Protheus - APD - É possível importar o Cadastro de Participantes
  da tabela RD0, via MILE
type: support-article
updated_at: '2025-02-19T12:53:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30084782592919-RH-Linha-Protheus-APD-%C3%89-poss%C3%ADvel-importar-o-Cadastro-de-Participantes-da-tabela-RD0-via-MILE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30084782579479) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**É possível importar o Cadastro de Participantes da tabela RD0, via MILE  
  
**Ambiente**TOTVS RH (Linha Protheus) - Avaliação e Pesquisa de Desempenho - Todas as versões  
  
**Solução**A rotina em questão **não tem suporte ao *MILE***.  
  
As rotinas homologadas para serem aceleradas via *MILE*, para o módulo de Gestão de Pessoal são as rotinas/tabelas conforme documentadas abaixo:  
**[RH - Linha Protheus - GPE - Configuração de MILE em rotinas do GPE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059771073-RH-Linha-Protheus-GPE-Configura%C3%A7%C3%A3o-de-MILE-em-rotinas-do-GPE?source=search)**  
  
É possível verificar que, na documentação: [https://tdn.totvs.com/pages/releaseview.action?pageId=550315418,](https://tdn.totvs.com/pages/releaseview.action?pageId=550315418) é informado que as demais rotinas ou tabelas **não são homologadas para que funcionem via acelerador *MILE*** e, nesses casos, é possível realizar a abertura de uma Sugestão de Melhoria na Central Colaborativa.  
  
Demais rotinas/tabelas, são possíveis de preenchimento através de configuração de Execução Automática (*execAuto*) das rotinas, como a tabela SRA, sendo o *execAuto* da rotina GPEA010, por exemplo:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=6079003>  
  
Contudo, **para o caso específico do cadastro de participantes, não há um *execAuto* disponível** e não está homologado o uso desta rotina via *MILE*, como informado no *link* acima.  
  
Entretanto, para a rotina de Participantes, existe a funcionalidade de Relacionamento, de acordo com os **Funcionários (SRA)** e o arquivo de relacionamento **msrelrdz\*\*\***, como descrito abaixo:  
**[RH - Linha Protheus - PORTAL GCH - Arquivo MSRELRDZ.ini](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059317533-RH-Linha-Protheus-PORTAL-GCH-Arquivo-MSRELRDZ-ini?source=search)**  
**\*\*\*arquivo modelo anexo a este artigo**  
  
Como realizar este relacionamento:  
**[RH - Linha Protheus - MEU RH - Como relacionar os Participantes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050255013-RH-Linha-Protheus-MEU-RH-Como-relacionar-os-Participantes?source=search)**  
  
**Quanto ao uso do acelerador MILE para a tabela RD0 especificamente**, é possível prosseguir com uma solicitação de Melhoria através de nossa Central Colaborativa**, mas de fato, não está homologado para uso esta tabela nesta rotina.  
  
Saiba Mais  
[Como relacionar os Participantes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051031874)  
[Qual a diferença das opções "Relacionar, Atualizar e Ambos" do cadastro de Participantes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052360593)  
[Artigos Avaliação Pesquisa e Desempenho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206956088-RH-Avalia%C3%A7%C3%A3o-e-Pesquisa-de-Desempenho)**
