---
article_id: 360060017093
category: RH – DIRF
content_hash: 9c56900c719785312b31bbb6a33b22f3dbbdd2a580430fcf4b7a9666f2fc3927
fetched_at: '2026-06-28T22:44:06.910174+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Como liberar/bloquear o acesso em Manutenção Arquivo
  DIRF somente para determinados códigos de retenção
type: support-article
updated_at: '2025-08-20T19:05:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060017093-RH-Linha-Protheus-GPE-Como-liberar-bloquear-o-acesso-em-Manuten%C3%A7%C3%A3o-Arquivo-DIRF-somente-para-determinados-c%C3%B3digos-de-reten%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34326005541655)** Tempo aproximado para leitura: **00:01:00 min**  
**Dúvida**Como liberar/bloquear o acesso em Manutenção Arquivo DIRF somente para determinados códigos de retenção?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**1. Acesse a rotina Controle de Acesso Usuários (GPEA270) pelo caminho **>Atualizações >Cadastros >Controle de Acesso Usuários** e clique em Incluir;

2. No campo **Grupo Usuário** ou **ID Usuário** escolha o grupo ou usuário que irá fazer o ajuste, no exemplo abaixo será feita restrição por Usuário:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098570654)

3. No campo Arquivo selecione a tabela SRL-DIRF/Informe de Rendimento:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100808773)

4. Nos campos Filtro Brows e Filtro Relat insira o filtro para restringir o acesso aos códigos de retenção tanto na visualização das rotinas quanto nos relatórios, no exemplo abaixo o usuário só pode visualizar os tipos de rendimentos diferentes de 0561 e 0588:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11133413612055)

5. Clique em Adicionar e depois em OK:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11133314588183)

6. Clique em Salvar:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11133275797655)  
  
Agora o usuário em questão tem acesso para visualizar na rotina Manutenção Arquivo apenas códigos de retenção diferentes de 0561 e 0588.

**Saiba mais**

[Página centralizadora Protheus - DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF)
