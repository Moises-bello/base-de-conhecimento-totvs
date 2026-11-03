---
article_id: 35777677870743
category: Materiais - Compras (SIGACOM)
content_hash: 7460ad4c8b7e96070763a256ad7ced4ce8c63b4dcc2530c45f0eb85c10cb7585
fetched_at: '2026-06-28T22:41:21.891532+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - Quais tabelas
  e campos são preenchidos ao Migrar Cotações?
type: support-article
updated_at: '2025-10-21T14:08:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35777677870743-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-Quais-tabelas-e-campos-s%C3%A3o-preenchidos-ao-Migrar-Cota%C3%A7%C3%B5es
---

![relogio_tempo_leitura_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35777681793687) Tempo aproximado para leitura: 00:02:00 min  
  
**Dúvida**  
Quais tabelas são geradas e campos são preenchidos ao Migrar Cotações do Processo Legado de Cotação para o Novo Fluxo de Compras?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - A partir da Versão 12.  
  
**Solução**  
Ao executar a rotina de **Migrar Cotações** do processo legado para o **Novo Fluxo de Compras (NFC)**, o sistema executa os procedimentos abaixo:

* **Atualiza** campos na tabela de cotações **SC8** (registro da cotação original), sinalizando a migração

  **C8\_ORIGEM** — é preenchido com  PGCA020. Esse campo é atualizado para indicar que a cotação originou-se do processo legado / migração.

  **C8\_SITUAC** — é preenchido com 1. É atualizado para refletir a situação/legenda da cotação.

  **C8\_QTDISP** -- é preenchido com a quantidade da cotação que consta no campo C8\_QUANT
* **Cria um registro** de cabeçalho na tabela **DHU** (Cabeçalho da Cotação do Novo Fluxo)

  **DHU\_AGPCOT** — preenchido com o texto: "COTAÇÃO MIGRADA AUTOMATICAMENTE" (marca a migração).

  **DHU\_LEGACY** — preenchido com "2" . Serve para indicar que a cotação é legada e foi migrada. (convenção: 1 = Não / 2 = Sim).
* DHU\_CODCOM e DHU\_COMPRA  — permanecem em branco
* **Cria registro (os)** dos itens da cotação na tabela **DHV** (Saldo dos itens da cotação) com base nas informações da SC8. 1 registro por item da cotação.

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Novo Fluxo de Compras - NFC (PGCA010)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19838751317655-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Novo-Fluxo-de-Compras-NFC-PGCA010)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
