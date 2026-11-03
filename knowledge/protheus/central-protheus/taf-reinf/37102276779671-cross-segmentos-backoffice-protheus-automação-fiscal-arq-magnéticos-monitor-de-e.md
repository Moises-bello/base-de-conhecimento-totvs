---
article_id: 37102276779671
category: TAF - REINF
content_hash: 01a88eed2f58415039c689764cb244aef51694f099f099c8845c8f5ecc33760e
fetched_at: '2026-06-28T22:41:33.332618+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Automação Fiscal - Arq. Magnéticos
  - Monitor de Eventos - Foi detectada uma divergência no tamanho dos campos (T7A_CHVELE
  e C20_CHVELE)
type: support-article
updated_at: '2025-12-17T21:30:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37102276779671-Cross-Segmentos-Backoffice-Protheus-Automa%C3%A7%C3%A3o-Fiscal-Arq-Magn%C3%A9ticos-Monitor-de-Eventos-Foi-detectada-uma-diverg%C3%AAncia-no-tamanho-dos-campos-T7A-CHVELE-e-C20-CHVELE
---

**Ocorrência**  
Mensagem de alerta ''Foi detectada uma divergência no tamanho dos campos (T7A\_CHVELE e C20\_CHVELE)'' ao abrir a rotina TAFA635 (Monitor de Eventos).

![PRINT 1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37102286941975)  
  
**Ambiente**  
Microsiga Protheus – TAF – versão 12.1.2410 e inferior.

**Causa**  
Erro ocorre devido a diferença de campos da tabela T7A e da tabela C20, onde por padrão os campos são criados como T7A\_CHVELE com tamanho 44, e C20\_CHVELE com tamanho 60.  
  
**Solução**  
Acesse o SIGACFG e vá no seguinte caminho Base de Dados>Dicionário>Base de dados.

![PRINT 2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37102276752919)

Posteriormente, vá até a lupa e pesquisa a tabela T7A.

![PRINT 3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37102276756631)

Após isso, clique para editar a tabela (ícone do lápis).

![PRINT 4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37102286951447)

Clique para editar novamente com o campo selecionado, e altere o tamanho para 60.

![PRINT 5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37102286953623)

Posteriormente, clique para Sair (ícone da porta), e salve a alteração (ícone do disquete).

![PRINT 6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37102286955031)

Avance as telas e valide que o campo foi alterado.

![PRINT 8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37102276762519)

Validando a mensagem que foi alterado com sucesso, basta finalizar o processo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37102286956823)

Posteriormente, saia do Configurador e acesso o TAF onde o erro inicial não deverá persistir.

**Procedimento não deve ser realizado a parti da release 2510.**

**IMPORTANTE: É NECESSÁRIO QUE O PROCESSO EXECUTADO SEJA FEITO COM AMBIENTE DE MANEIRA EXCLUSIVA (SEM NENHUM USUÁRIO LOGADO NO AMBIENTE).**

Documentação complementar:

https://tdn.totvs.com/display/public/TAF/Monitor+de+Eventos+-+TAF+-+P12
