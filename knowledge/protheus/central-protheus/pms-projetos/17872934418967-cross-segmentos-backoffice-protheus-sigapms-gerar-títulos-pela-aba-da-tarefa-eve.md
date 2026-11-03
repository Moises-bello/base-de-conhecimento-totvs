---
article_id: 17872934418967
category: PMS - Projetos
content_hash: 756a4381089091ade5ac3720fb3ba62a7b46aa2e2f2a55b447b0a962ab831755
fetched_at: '2026-06-28T22:37:15.195176+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Gerar títulos pela aba da
  tarefa "Eventos"
type: support-article
updated_at: '2024-03-21T14:04:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17872934418967-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Gerar-t%C3%ADtulos-pela-aba-da-tarefa-Eventos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17872948003735) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como gerar títulos pela aba da tarefa "Eventos"?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAPMS - Todas as versões  
  
**Solução**Pode surgir a necessidade, de apontar em algum evento executado do projeto, uma certa receita (Lucro) no contas a receber (FINA740).

Para que seja realizado o título no financeiro, deve ser atingido o percentual de execução do evento configurado.

1 - Vá na aba "Eventos" ao alterar uma tarefa na rotina (PMSA410), cadastre com os campos a seguir e salve:

* AFP\_USO = 0002 (Receitas do projeto)
* AFP\_DESCRI = "Receitas do Projeto"
* AFP\_DTPREV = DATABASE (Data prevista para início do evento)
* AFP\_PERC = 100,00 (Percentual físico do projeto para que o evento seja executado)
* AFP\_CLIENT = 'Cliente para qual será gerado a cobrança'
* AFP\_LOJA = 'Loja do Cliente para qual será gerado a cobrança'
* AFP\_VALOR = 123,45 (Valor do título)
* AFP\_GERPRV = 1 - Data Prevista
* AFP\_GERTIT = 1 - Sim
* AFP\_COND = 'Condição de pagamento' (Como será organizado as parcelas após apontamento físico do projeto)
* AFP\_NUM = 'Numeração do título que será gerado'
* AFP\_PREFIX = "PMS" (Prefixo do título que será gerado)
* AFP\_NATUREZ = 'Natureza financeira do título que será gerado'
* Salvar

**OBSERVAÇÃO 1:** Será gerado um título do tipo "PR = Previsão":

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17872843703319)

**OBSERVAÇÃO 2:** Os títulos pelo evento são incluídos ou excluídos, a baixa destes deve ser realizado no financeiro (qualquer rotina que gere títulos, não baixam os títulos que geram, tem de ir pelo módulo Financeiro)

2 - Entrar na rotina (PMSA410 - Projetos(modelo 2)

* Posicionar no projeto que o evento foi criado na tarefa
* Outras Ações > Alt. Estrutura > Posiciona na tarefa com evento > Outras Ações > Progresso físico do projeto > Confirmações > Incluir (no rodapé)
* Aparecerá a janela do passo 3

3 - Preencher o controle de execução (janela)

* AFF\_DATA = DATABASE
* AFF\_PERC = Deve ser igual ou superior ao campo AFP\_PERC do passo 1.
* Confirmar

**OBSERVAÇÃO 3:** Nesse instante, é excluído o título de tipo "PR" e são incluídos parcelas de acordo com a regra da condição de pagamento (AFP\_COND) do tipo "NF", com o total (AFP\_VALOR) dividido entre as parcelas criadas:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17872916149271)
