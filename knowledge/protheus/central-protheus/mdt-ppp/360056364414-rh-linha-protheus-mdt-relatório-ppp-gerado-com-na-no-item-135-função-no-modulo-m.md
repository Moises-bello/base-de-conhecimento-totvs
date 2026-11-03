---
article_id: 360056364414
category: MDT - PPP
content_hash: 9f9ac4b5a5918341294f4c31bc2848ce922c56f8ad9dd92c8caf8e884f3a2238
fetched_at: '2026-06-28T22:44:22.340415+00:00'
product: protheus
section_id: 360010945654
source: central-protheus
title: RH - Linha Protheus - MDT - Relatório PPP gerado com NA no item 13.5 Função
  no modulo medicina e segurança do trabalho (SIGAMDT)
type: support-article
updated_at: '2025-07-31T14:18:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056364414-RH-Linha-Protheus-MDT-Relat%C3%B3rio-PPP-gerado-com-NA-no-item-13-5-Fun%C3%A7%C3%A3o-no-modulo-medicina-e-seguran%C3%A7a-do-trabalho-SIGAMDT
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20008128153879)** Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Relatório PPP (Perfil Profissiográfico Previdenciário) gerado com **NA** no item **13.5 Função** no modulo medicina e segurança do trabalho (SIGAMDT)  
  
![ppp_funcao_NA.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097969393)  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho  - Todas as versões  
  
**Causa**  
Quando o relatório de PPP é gerado com a descrição **NA** no item **13.5 Função,** ou invés da descrição da função do trabalhador, é devido o cadastro de função não estar definido com a opção Imprime PPP igual a SIM.  
  
**Solução**  
Esta documentação refere-se exclusivamente a versão do PPP impresso no Módulo de Medicina e Segurança do Trabalho, rotina MDTR700, não tendo nenhuma relação com o PPP Eletrônico maiores informações consulte: **[RH - Linha Protheus - MDT - Qual diferença entre o PPP impresso no Módulo Medicina MDTR700 e o PPP da Previdência Social consultado através do APP Meu INSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14223826251287)**  
  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o cadastro de funções no modulo SIGAMDT através do caminho atualizações > cadastros gerais > funções (GPEA030);  
  
2. Localize a função que não foi gerada no relatório, acesse como alterar e deixe o campo **Impr. no PPP** (RJ\_PPPIMP) com **SIM**;  
  
![cadastro_funcao_ppp.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097969373)  
  
3. Após esse processo gere o relatório PPP no modulo SIGAMDT através do caminho: atualizações > relatórios > PPP > perfil profissiogr (MDTR700).  
  
![ppp_funcao_completa.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095672794)  
  
**Saiba Mais**  
[Como gerar o PPP (Perfil Profissiográfico Previdenciário) no modulo Medicina (sigamdt), e de onde vem as informações apresentadas no relatório](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050700933)  
[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
