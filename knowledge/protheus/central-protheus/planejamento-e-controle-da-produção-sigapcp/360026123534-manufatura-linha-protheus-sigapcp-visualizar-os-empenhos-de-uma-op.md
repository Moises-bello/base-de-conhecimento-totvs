---
article_id: 360026123534
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 81ab53a90cbe09a3c511a9e135068c6e69d27cd91b964bdf824c04da7a2478c3
fetched_at: '2026-06-28T22:42:47.147707+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Visualizar os empenhos de uma OP
type: support-article
updated_at: '2021-10-15T18:27:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026123534-Manufatura-Linha-Protheus-SIGAPCP-Visualizar-os-empenhos-de-uma-OP
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:01:10 min****Dúvida**Como visualizar os empenhos de uma **OP - Ordem de produção**?  
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Consulte os empenhos gerados através das rotinas **MATA380** **- Empenho Simples**  ou **MATA381 - Empenho Múltiplo.** Também pode visualizá-los no momento da geração. Para isso o conteúdo do parâmetro **Mostra Tela Alt. de Empenhos** do **F12** do **MATA650 - Ordem de Produção** deve estar igual a **Sim**, neste caso será apresentada uma tela com os empenhos gerados ao sair da rotina **MATA650** quando for confirmada a geração das **ordens intermediárias** e **solicitações de compras**, conforme pergunta apresentada ao usuário ou ao confirmar a geração da **OP** por pedido de venda.  
  
**Importante**  
Se mesmo alterando o conteúdo do parâmetro **Mostra Tela Alt. de Empenhos** não estiver aparecendo a tela ao sair do **MATA650**, verifique se o produto em questão possui estrutura.   
  
Verifique também no módulo **SIGACFG - Configurador**, **Usuário > Senhas > Usuários**, altere o cadastro do usuário que não está apresentando a tela de empenho e na aba **Restrições de Acesso** > **Acessos >** marque a opção **37** **Alterar Empenhos de OPs**.
