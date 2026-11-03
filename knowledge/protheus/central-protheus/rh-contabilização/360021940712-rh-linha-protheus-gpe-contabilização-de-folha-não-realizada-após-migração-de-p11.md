---
article_id: 360021940712
category: RH - Contabilização
content_hash: 7394dabf943eeb51b5a79cb0354bf6187854cabf34c942491caad6930c38931e
fetched_at: '2026-06-28T22:43:45.937882+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Contabilização de Folha não realizada após migração
  de P11 para P12, mesmo com geração da tabela SRZ
type: support-article
updated_at: '2025-07-29T13:57:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021940712-RH-Linha-Protheus-GPE-Contabiliza%C3%A7%C3%A3o-de-Folha-n%C3%A3o-realizada-ap%C3%B3s-migra%C3%A7%C3%A3o-de-P11-para-P12-mesmo-com-gera%C3%A7%C3%A3o-da-tabela-SRZ
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33791336377495)** Tempo aproximado para leitura: **00:01:30 min**

**Ocorrência**Ao realizar processo de **Contabilização**, em casos de clientes que migraram da **versão 11 para 12 do Protheus**, o sistema não realiza a integração dos dados gerados na tabela de resumo **SRZ**, para as tabelas **CT2** e **CTK** do módulo **Contabilidade Gerencial**. O sistema fecha a tela de **Contabilização**, da rotina **GPEM110** sem carregar as tabelas ou demonstrar valores contabilizados.   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**Neste caso, o incidente ocorreu devido estruturas criadas a partir do arquivo SIGAMAT.EMP migrado da versão 11 incorretamente para a versão 12.  
  
**Solução**Para solucionar a ocorrência, é necessário:  
**1.** Validar se o tamanho do campo **SM0\_FIL** do arquivo **SIGAMAT.EMP** migrado do **P11**, está diferente dos campos de filial da **P12**;  
**2.** Solicitar para a equipe de **Framework**  o acompanhamento para validar o tamanho do campo **SM0\_FIL** do **SIGAMAT** migrado da **P11**, comparando com as estruturas **XX (XX8)** do ambiente **P12** criadas. Estando as estruturas incorretas, o sistema ao validar o tamanho dos campos das tabelas para **Contabilização**, retorna conteúdos divergentes, não finalizando o processo.

**Saiba Mais**  
[Artigos Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)
