---
article_id: 6015434319511
category: Comércio Exterior - Easy Export Control - Embarque
content_hash: 095f0f5954e98872cc629ea4828d57c897c4c4e63037c5122926cd5da885e635
fetched_at: '2026-06-28T22:36:56.589682+00:00'
product: protheus
section_id: 1500001549322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Os Dados Informados
  nas Despesas Internacionais estão Incompletos
type: support-article
updated_at: '2022-05-11T16:48:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6015434319511-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Os-Dados-Informados-nas-Despesas-Internacionais-est%C3%A3o-Incompletos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**

Ao tentar gravar um processo na rotina do embarque de exportação **(EECAE100)** esta sendo exibida a seguinte mensagem : "**Atenção - Os dados informados na Despesas Internacionais estão incompletos. A despesa do tipo Frete Inl. este sem preenchimento do campo empresa"**. Como faço para conseguir gravar o processo sem que esta mensagem seja exibida?

![Picture1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6015504432151/Picture1.png)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões.  
  
**Solução**

Esta mensagem esta sendo exibida pois a efetuar a inclusão da despesa internacional não foi informada a empresa. Para que mensagem não seja mais exibida podemos seguir por 2 caminhos.

Para dar continuidade a inclusão da despesa internacional :

1. Acesse a rotina da Manuteção do Embarque de Exportação **(EECAE100)**.
2. Selecione o processo que se encontra com a mensagem e clique no botão alterar.
3. Clique no menu Outras Ações e selecione a opção a Despesas Internacionais.
4. Selecione a despesa Fret Intl.
5. Acesse o campo Empresa **(EXL\_EMFR)** e informe a empresa desejada para inclusão da despesa.
6. Clique no botão Salvar.
7. Salve o embarque novamente e a mensagem não será mais exibida.

Para remover a depesa do processo:

1. Acesse a rotina da Manuteção do Embarque de Exportação **(EECAE100)**.
2. Selecione o processo que se encontra com a mensagem e clique no botão alterar.
3. Botão outras ações e selecione a opção a Despesas Internacionais.
4. Selecione a despesa Fret Intl.
5. Menu Outras Ações selecione a opção Limpar.
6. Será feita um pergunta **"Atenção - Deseja limpar os dados da Despesa?"**.
7. Clique no botão **Sim**.
8. Salve o embarque novamente e a mensagem não será mais exibida.
