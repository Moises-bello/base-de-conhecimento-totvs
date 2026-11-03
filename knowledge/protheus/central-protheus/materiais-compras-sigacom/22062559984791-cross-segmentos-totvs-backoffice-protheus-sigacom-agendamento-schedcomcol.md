---
article_id: 22062559984791
category: Materiais - Compras (SIGACOM)
content_hash: 9ebfa3fba5b7ae1953cb25dd5b676a7f6b8ead76df18df0324bc40711bb92f42
fetched_at: '2026-06-28T22:41:13.090779+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Agendamento SCHEDCOMCOL
type: support-article
updated_at: '2025-01-30T16:59:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22062559984791-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Agendamento-SCHEDCOMCOL
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22062488097431)** Tempo aproximado para leitura:**00h05 min**

**Dúvida**Como realizar a configuração do agendamento da rotina SCHEDCOMCOL dentro do novo SCHEDULE POUI?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - A partir da Versão 12  
  
**Solução**

O agendamento SCHEDCOMCOL é responsável por realizar leitura e integração dos XMLs importados na tabela CKOCOL (tabela onde é armazenado os XMLs lidos pelos agendamentos COLAUTOREAD e SCHEDIMPTRA) para o monitor do Importador XML.

Para realizar a configuração do agendamento das rotinas que serão utilizadas no Importador XML/ TOTVS Colaboração e a integração com TOTVS Transmite seguir o passo a passo abaixo:

![SCHEDCOMCOL (online-video-cutter.com) (1).gif](https://centraldeatendimento.totvs.com/hc/article_attachments/22062559978519)

**Passo 1:** Entrar no módulo do configurador

* Acesse o sistema no módulo do configurador.
* Dentro do ambiente configurador, localize e clique em "Schedule" (ou agendamento).
* Em seguida, clique novamente em "Schedule" para abrir a tela de criação e configuração de agendamentos.

**Passo 2:** Criar um novo agendamento

* No menu de agendamentos, clique em "Novo" para iniciar a criação de um novo agendamento.  
  Digite "SCHEDCOMCOL" no campo de nome do agendamento e clique em "Avançar".

**Passo 3:** Configurar a primeira execução

* Especifique o dia e horário de início para a execução do agendamento.  
  Deixe a periodicidade como "diária" e clique em "Avançar".
* Selecionar Frequência = "SIM", selecionar Minuto e colocar o tempo de 5.

**Passo 4:** Selecionar todas as empresas e todas as filiais que irão receber as notas.

* Selecione todas as empresas e todas as filiais para qual o agendamento será aplicado.  
  Escolha o módulo de compras.

Selecione o usuário que executará o agendamento ou mantenha como "administrador".

**Passo 5:** Adicionar descrição

* Na caixa de descrição, insira: **"Ler os XML's da CKO e importar para o monitor (SDS e SDT)"**.

**Passo 6:** Concluir o agendamento

* Clique em "Avançar" e, em seguida, em "Concluir" para finalizar a configuração do agendamento.

***Saiba Mais:***

* [Importador XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994-MP-SIGACOM-Importador-XML#:~:text=No%20Importador%20de%20XML%20%C3%A9%20necess%C3%A1rio%20criar%20agendamentos,op%C3%A7%C3%B5es%20do%20menu%20Ambiente%20-%3E%20Schedule%20-%3E%20Schedule%3A)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Qual o Consumo de Licenças das rotinas responsáveis pela importação e gravação do XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17736765600407-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Qual-o-Consumo-de-Licen%C3%A7as-das-rotinas-respons%C3%A1veis-pela-importa%C3%A7%C3%A3o-e-grava%C3%A7%C3%A3o-do-XML)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM)
