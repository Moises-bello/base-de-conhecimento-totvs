---
article_id: 38301661775511
category: Contabilidade Gerencial - Apuração, Estorno e Encerramento Contábil
content_hash: 24a1446aede3c3b73592a9d822b2772e75cc6ac5021bce437dd5286e5163fbda
fetched_at: '2026-06-28T22:41:05.113742+00:00'
product: protheus
section_id: 1500001548342
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBA960 - Fechamento
  Contábil apresenta a mensagem "Não foram encontrados os campos MSUIDT nas tabelas".
type: support-article
updated_at: '2026-04-27T20:23:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38301661775511-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA960-Fechamento-Cont%C3%A1bil-apresenta-a-mensagem-N%C3%A3o-foram-encontrados-os-campos-MSUIDT-nas-tabelas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38301661762199) Tempo aproximado para leitura: 00:10 min

**Dúvida**  
Ao tentar acessar a rotina **CTBA960 (Fechamento Contábil)**, o sistema apresenta a mensagem impeditiva informando que os campos **MSUIDT** não foram encontrados no dicionário de dados para diversas tabelas. Como proceder?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contabilidade Gerencial - 12.1.2210

**Solução**  
Este incidente ocorre devido à ausência dos campos de identificação unica (UUID) necessários para o funcionamento do **Fechamento Contábil**. Para a correção, é necessário realizar a geração do arquivo diferencial (SDF) através do Wizard e a posterior atualização do dicionário de dados via **UPDDISTR**.

Acesse o **Wizard de Implantação do Conciliador Backoffice** (**WIZARDUUID**): [CTBA940 - Conciliador Contábil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6451317698583-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA940-Conciliador-Cont%C3%A1bil?source=search)

1. Prossiga até a **Segunda Opção** do Wizard para realizar a geração do arquivo **SDF** contendo as definições dos campos de ID;

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38304178508823)
2. Após a geração do arquivo, execute o compatibilizador **UPDDISTR** para que os campos sejam efetivamente criados no Dicionário de Dados (SX3);  
     
   **Observação:** Caso a execução automática pelo Wizard não crie os campos, realize a execução do **UPDDISTR** de forma manual/direta apontando para o arquivo gerado.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38304178510743)
3. Acesse o Wizard novamente e confirme se o status dos campos de ID é apresentado como **"OK"** (em vez de "Incluir");

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38304180352535)
4. Com o status **"OK"**, siga com as demais etapas do Wizard para realizar a população dos campos de ID na base de dados.

Após a criação dos campos o acesso à rotina CTBA960 (Fechamento contábil), será liberada para uso.

**Saiba Mais:**  
[CTBA940 - Conciliador Contábil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6451317698583-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA940-Conciliador-Cont%C3%A1bil?source=search)

[CTBA960 - Fechamento Contábil.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34334419010839-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA960-Fechamento-Cont%C3%A1bil)
