---
article_id: 4410278789527
category: PMS - Dúvidas Gerais
content_hash: d6e211538c52d049bab47c60d7a8c309f4018586360287e2669b312f27a8e002
fetched_at: '2026-06-28T22:37:17.710183+00:00'
product: protheus
section_id: 1500001539681
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Preenchimento dos campos
  "DT.INIC.RLZ Data Inicial Realizado" e "DT.FIN.RLZ Data Final Realizado" na estrutura
  do projeto
type: support-article
updated_at: '2024-02-23T15:17:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410278789527-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Preenchimento-dos-campos-DT-INIC-RLZ-Data-Inicial-Realizado-e-DT-FIN-RLZ-Data-Final-Realizado-na-estrutura-do-projeto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21567742076823) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Qual o processo para preencher o campo "DT.INIC.RLZ Data Inicial Realizado" e "DT.FIN.RLZ Data Final Realizado" na estrutura do projeto?   
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAPMS - Todas as versões.  
  
**Solução**Qual o processo para preencher o campo DT.INIC.RLZ "AFC\_DTATUI" Data Inicial Realizada:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410263812247)

Os campos **Dt.Inic.Rlz.** ou **Dt.Fin.Rlz.** estão presentes na seguinte estrutura do seu projeto:

**Projeto:**  
AF8\_DTATUI -   
AF8\_DTATUF -

**Tarefa:**  
AF9\_DTATUI -   
AF9\_DTATUF -

**EDT:**  
AFC\_DTATUI -   
AFC\_DTATUF -

**1º Passo:** Com um projeto já criado você pode realizar o apontamento pela rotina **PMS410 "Projetos(modelo 2)**" > Outras Ações > Alt. Estrutura:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410259862295)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410269126807)

**2º Passo:** O apontamento da **Dt.Inic.Rlz.** ou **Dt.Fin.Rlz.** deve ser realizado em cima da **tarefa** ou **EDT**, o projeto somente recebe a informação que foi apontada na sua estrutura conforme sua regra.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410260054167)

**3º Passo:**Ao acessar a rotina de **"Progresso físico do Projeto"**será necessário fazer a inclusão do seu apontamento:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410260144407)

**4º Passo:** Ao realizar o apontamento inclua as principais informações como "Data Referencia" e Qtd Executada e a hora que iniciou e concluiu:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410260248343)

**5º Passo:** Ao sair da tela do **"Progresso físico do Projeto"** é possível visualizar o campo preenchido com as suas informações:

**![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410260319639)**

* **Observação:**

O apontamento pode ser realizado também pela rotina "Gerenciamento de Execução" PMSA310:

SIGAPMS > Atualizações > Projetos > Gerenciamento de Execução

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410277201303)

Ao clicar em atualizar segue o mesmo padrão utilizado anteriormente na rotina **PMS410 "Projetos(modelo 2)":**

**![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410277256343)**

Ao confirmar será aberta a mesma tela para incluir o seu apontamento, alterar ou excluir:

**![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410277308567)**

**Vídeo da simulação:**

![Apontando-AFC_DTATUI-com-projeto-ja-criado.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4410277765015)
