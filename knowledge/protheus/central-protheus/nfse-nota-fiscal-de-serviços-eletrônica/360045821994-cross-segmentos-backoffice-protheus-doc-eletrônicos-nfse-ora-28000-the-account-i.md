---
article_id: 360045821994
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: ad532f01358d6f94f5a4a5439127b9288ed355b783e33f0110be69e1ffd942ef
fetched_at: '2026-06-28T22:39:57.613109+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - ORA-28000:
  The account is locked'
type: support-article
updated_at: '2025-06-25T21:13:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045821994-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-ORA-28000-The-account-is-locked
---

**Ocorrência**Ao transmitir um RPS onde a base de dados da prefeitura é Oracle, é apresentado a seguinte mensagem de erro: ***ORA-28000: The account is locked*.**  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Causa**Esse incidente ocorre geralmente por dois motivos:

I. O usuário informou a senha incorreta na comunicação Web Services, onde consequentemente é bloqueado por ultrapassar o número máximo de vezes especificado pelo parâmetro de perfil do usuário FAILED\_LOGIN\_ATTEMPTS (10x padrão do Oracle);  
II. O administrador do banco de dados bloqueou a conta.  
  
**Solução**Nesse caso, por se tratar de um **erro interno no banco de dados da própria prefeitura**, deverá entrar em contato com os mesmos para que realizem as devidas validações e correções internamente.
