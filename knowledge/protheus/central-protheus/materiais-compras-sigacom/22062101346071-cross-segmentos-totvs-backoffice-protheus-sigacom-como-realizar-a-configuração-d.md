---
article_id: 22062101346071
category: Materiais - Compras (SIGACOM)
content_hash: d08fc8037ab554c594ffe144995836552c9da7bf3ed527207f938f7becba2d05
fetched_at: '2026-06-28T22:41:16.006611+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como realizar a configuração
  do agendamento da rotina COLAUTOREAD dentro do novo SCHEDULE POUI?
type: support-article
updated_at: '2024-04-22T11:34:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22062101346071-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-realizar-a-configura%C3%A7%C3%A3o-do-agendamento-da-rotina-COLAUTOREAD-dentro-do-novo-SCHEDULE-POUI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22062101342231) Tempo aproximado para leitura: **00h05 min****Dúvida**Como realizar a configuração do agendamento da rotina COLAUTOREAD dentro do novo SCHEDULE POUI?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - A partir da Versão 12  
  
**Solução**Para realizar a configuração do agendamento do COLAUTOREAD  no novo Schedule POUI que serão utilizadas no Importador XML/ TOTVS Colaboração seguir o passo a passo abaixo:

![COLAUTOREAD (online-video-cutter.com).gif](https://centraldeatendimento.totvs.com/hc/article_attachments/22062267991959)

**Passo 1:** Entrar no módulo do configurador

* Acesse o sistema no módulo do configurador.
* Dentro do ambiente configurador, localize e clique em "Schedule" (ou agendamento).
* Em seguida, clique novamente em "Schedule" para abrir a tela de criação e configuração de agendamentos.

**Passo 2:** Criar um novo agendamento

* No menu de agendamentos, clique em "Novo" para iniciar a criação de um novo agendamento.  
  Digite "COLAUTOREAD" no campo de nome do agendamento e clique em "Avançar".

**Passo 3:** Configurar a primeira execução

* Especifique o dia e horário de início para a execução do agendamento.  
  Deixe a periodicidade como "diária" e clique em "Avançar".
* Selecionar Frequência = "SIM", selecionar em "Minuto" e colocar o tempo de 30.

**Passo 4:** Selecionar apenas 1(uma) - empresa, 1(uma) - filial e módulo

* Selecione apenas uma empresa e uma filial para a qual o agendamento será aplicado.  
  Escolha o módulo de compras.

Selecione o usuário que executará o agendamento ou mantenha como "administrador".

**Passo 5:** Adicionar descrição

* Na caixa de descrição, insira: **"Para importar XML's através da pasta IN (MV\_NGINN) e gravar informações na tabela CKO"**.

**Passo 6:** Concluir o agendamento

* Clique em "Avançar" e, em seguida, em "Concluir" para finalizar a configuração do agendamento.

**IMPORTANTE.:** Para melhorar o desempenho, foram criadas as rotinas SCHEIMPTRA e SCHEDUPTRA, destinadas à integração do Importador XML com o TOTVS Transmite. Portanto, se você não estiver utilizando o Importador XML padrão ou qualquer integração, é recomendado manter a rotina **COLAUTOREAD** desativada.

Ative-as apenas se estiver utilizando a pasta INN para importar os XMLs. Essa abordagem otimizará o desempenho do sistema, ativando apenas as funcionalidades necessárias para o seu fluxo de trabalho específico.

***Saiba Mais:***

* [Importador XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994-MP-SIGACOM-Importador-XML#:~:text=No%20Importador%20de%20XML%20%C3%A9%20necess%C3%A1rio%20criar%20agendamentos,op%C3%A7%C3%B5es%20do%20menu%20Ambiente%20-%3E%20Schedule%20-%3E%20Schedule%3A)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Qual o Consumo de Licenças das rotinas responsáveis pela importação e gravação do XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17736765600407-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Qual-o-Consumo-de-Licen%C3%A7as-das-rotinas-respons%C3%A1veis-pela-importa%C3%A7%C3%A3o-e-grava%C3%A7%C3%A3o-do-XML)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
