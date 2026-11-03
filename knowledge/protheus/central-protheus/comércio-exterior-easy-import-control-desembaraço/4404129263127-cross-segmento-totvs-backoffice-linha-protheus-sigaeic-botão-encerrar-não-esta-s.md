---
article_id: 4404129263127
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 605dabf79a6c86014ee2932453ed25768309f59057bc6e1b4ba89bfacfbdbd48
fetched_at: '2026-06-28T22:39:49.987997+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Botão encerrar
  não esta sendo exibido no menu da rotina de Desembaraço.
type: support-article
updated_at: '2025-11-18T18:47:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404129263127-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Bot%C3%A3o-encerrar-n%C3%A3o-esta-sendo-exibido-no-menu-da-rotina-de-Desembara%C3%A7o
---

**Dúvida**No menu da rotina de desembaraço  no SIGAEIC não está disponível a opção de escolher uma data de encerramento.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**

1. Acessar o módulo do configurador (SIGACFG) e habilitar o conteúdo do parâmetro **MV\_EIC0007** para T que estará disponível esta opção na rotina de Desembaraço (EICDI500), habilitando a nova funcionalidade do botão de encerramento do processo e o tratamento de eliminação de resíduo no módulo de Compras (SIGACOM), por motivos de extravio de mercadoria.

![MV_EIC0007.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4405252928151/MV_EIC0007.PNG)

2. Acesse o módulo “17- *Easy Import Control* (SIGAEIC)” e selecione as opções: Atualizações \ Desembaraço \ Manutenção (EICDI500).

3. Posicione sobre o desembaraço desejado.

4. Selecione Outras Ações\Encerrar.

5. Selecione o botão Sim.

![PERGUNTA_ENCERRAMENTO.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4405252927383/PERGUNTA_ENCERRAMENTO.PNG)

6. Selecione a data de encerramento e clique no botão Confirmar.

![INFORME_DATA_DE_ENCERRAMENTO.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4405252926999/INFORME_DATA_DE_ENCERRAMENTO.PNG)

7. Será exibida uma mensagem de aviso.

![AVISO_DECLARA__O_DE_IMPORTA__O.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4405252926103/AVISO_DECLARA__O_DE_IMPORTA__O.PNG)

8. Caso tente clicar no botão de encerramento o sistema exibirá uma mensagem de que o pedido já foi encerrado.

![pedido_encerrado.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4405252925847/pedido_encerrado.PNG)
