---
article_id: 34879226447511
category: SIGAACD - Automação e Coleta de Dados
content_hash: cf8e6a14f2a4bb4b96e489edf12984fd762b034f78c47a659d3c156fc9148065
fetched_at: '2026-06-28T22:39:13.816716+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Significado do campo
  CB7_TIPEXP na Ordem de Separação.
type: support-article
updated_at: '2026-05-07T19:18:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34879226447511-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Significado-do-campo-CB7-TIPEXP-na-Ordem-de-Separa%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34879256775191) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Qual o significado do campo CB7\_TIPEXP, demostrando com detalhes em base dos parâmetros da consulta F12 da rotina ordem de separação(ACDA100).   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.

**Solução**  
Segue os significado do campo CB7\_TIPEXP ao selecionar um pergunte, na rotina Ordem de Separação ao não finalizar a Ordem de Separação, é necessário avaliar esses parâmetros.

1. Ao acessar a rotina Ordem de Separação(ACDA100) seleciona o F12 ira apresentar essa tela:

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/34879226439319)

   2. Ao clicar em OK apresenta os parâmetros voltado ao campo CB7\_TIPEXP.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/34879256776471)

   3. Segue o significado de cada campo citado acima.

   **Observação** Todos os parâmetros da consulta F12 da rotina:

   (00-Separacao,01-Separacao/Embalagem,02-Embalagem,03-Gera Nota,04-Imp.Nota,05-Imp.Volume,06-embarque,07-Aglutina Pedido,08-Aglutina Local,09-Pre-Separacao')

   **CB7\_TIPEXP** = 00\* (Separação Simples)

   **CB7\_TIPEXP** = 01\* (Separação com Embalagem Simultânea)

   **CB7\_TIPEXP** = 02\* (Embalagem)

   **CB7\_TIPEXP** = 03\* (Gera Nota)

   **CB7\_TIPEXP** = 04\* (Imprime Nota)

   **CB7\_TIPEXP** = 05\* (Imprime Etiquetas Oficiais de Volume)

   **CB7\_TIPEXP** = 06\* (Embarque)

   **CB7\_TIPEXP** = 11\* (Aglutina pedido)

   **CB7\_TIPEXP** = 08\* (Aglutina armazém)

   **CB7\_TIPEXP** = 09\* (Pré-Separação)

   **CB7\_TIPEXP** = 10\* (confere lote)

   Visualização do campo CB7\_TIPEXP na rotina Ordem de Separação:

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/34879293415319)

   Quando seleciona uma dessas opções na rotina Ordem de Separação e não finaliza a Ordem é porque algum parâmetro desse estão selecionados, e deve ser liberado no emulador na opção Cadastro - Atualização - Expedição (ACDV166).

   **Saiba Mais:**

   [Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
