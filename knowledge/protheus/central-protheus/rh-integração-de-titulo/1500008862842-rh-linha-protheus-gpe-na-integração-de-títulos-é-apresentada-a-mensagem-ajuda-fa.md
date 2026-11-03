---
article_id: 1500008862842
category: RH - Integração de Titulo
content_hash: 462c0f2243cdc023e9f93c2078de4705a382623edd97927bffcc574437e26e9e
fetched_at: '2026-06-28T22:43:36.380216+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: 'RH - Linha Protheus - GPE - Na integração de títulos é apresentada a mensagem:
  AJUDA FA050CODRET Código de retenção não informado'
type: support-article
updated_at: '2025-07-23T12:14:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008862842-RH-Linha-Protheus-GPE-Na-integra%C3%A7%C3%A3o-de-t%C3%ADtulos-%C3%A9-apresentada-a-mensagem-AJUDA-FA050CODRET-C%C3%B3digo-de-reten%C3%A7%C3%A3o-n%C3%A3o-informado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33657719639447)**Tempo aproximado para leitura:00:02:00 min

**Ocorrência**Na integração de títulos é apresentada a mensagem: AJUDA FA050CODRET Código de retenção não informado  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) -  GPE Gestão de Pessoal – Todas as versões  
  
**Causa**Esse incidente é ocasionado pois no processo de **Integração do Título - GPEM670** o mesmo esta sendo inserido com o campo **Gera DIRF - E2\_DIRF** igual a 1 - Sim, desta forma o preenchimento do campo **Cd. Retenção - E2\_CODRET** se torna obrigatório.  
  
**Solução**Exemplo de erro apresentado: ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500013346102)  
  
Para solucionar essa ocorrência será necessário verificar se o **Inicializador Padrão** do campo **DIRF - E2\_DIRF** foi modificado para 1, no Padrão o mesmo possui conteúdo igual a 2.   
Desta forma sempre que um título é inserido na rotina **Contas a Pagar - FINA050**, automaticamente o mesmo é preenchido com conteúdo 2, sendo necessário o usuário modificar o mesmo para 1 caso o título entre no critério de envio para DIRF.  
  
Acessar: **Configurador** -> **Base de Dados** -> **Dicionário** -> **Arquivos** -> Tabela SE2 -> Campo E2\_DIRF / Aba **Opções**, modifique o campo **Inic. Padrão** para **"2"**(dois entre aspas duplas):  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500013644281)

**Saiba Mais**[Artigos sobre Integração de Título](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
