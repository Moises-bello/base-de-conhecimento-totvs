---
article_id: 360028432491
category: Comércio Exterior - Easy Import Control - Financeiro
content_hash: 9ab500b43af48fd276c3c21b406d9b6281a6fc489b6bef6608db6c3247f0635a
fetched_at: '2026-06-28T22:39:44.381514+00:00'
product: protheus
section_id: 1500001549642
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Manutenção de
  Câmbio 3/4
type: support-article
updated_at: '2022-06-01T21:13:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028432491-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Manuten%C3%A7%C3%A3o-de-C%C3%A2mbio-3-4
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:****00:02:00 min****

**Dúvida**Como utilizar rotina de câmbio tipo 3 e 4?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**

**Procedimentos para Utilização**

Pré-Requisitos:

* Para criação da opção Cambio 3/4 no menu ou efetuar a sua inclusão via SIGACFG. Importante: mesmo se tratando do menu do módulo SIGAEIC, o módulo (<module>/ <owner>) a ser informado deve ser o 29 (SIGAEEC), pois trata-se de uma funcionalidade nativa do módulo Easy Export Control.
* Possuir os parâmetros MV\_EASYFIN = S

Sequencia 01 - Inclusão do Câmbio 3/4:

1. No Easy Import Control (SIGAEIC), acesse Atualizações/ Financeiro/ Câmbio 3/4.
2. Clique em Incluir.
3. Preencha o campo Processo e clique em Confirmar.
4. Preencha os campos obrigatórios, informando um evento (de despesa) que represente o câmbio da Invoice de Importação ou da operação de remessa que deseja-se registrar no Sistema. No campo Tipo Contrato é possível informar as opções: 3 = Recebimento ou 4 = Remessa.
5. Selecione a opção 4 - Remessa e clique em Confirmar para salvar o processo.
6. Será apresentado a mensagem "Confirma a Inclusão?", clique em Sim.
