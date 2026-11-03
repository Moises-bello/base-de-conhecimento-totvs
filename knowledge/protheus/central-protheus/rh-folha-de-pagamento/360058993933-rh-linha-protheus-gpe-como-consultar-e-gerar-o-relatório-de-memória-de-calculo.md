---
article_id: 360058993933
category: RH - Folha de Pagamento
content_hash: 1ca86cbc2902363e822eed1f6d15164c49a46daf0d340956351b85c9886a95fe
fetched_at: '2026-06-28T22:44:13.356952+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como consultar e gerar o relatório de memória de
  calculo
type: support-article
updated_at: '2025-04-24T21:51:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058993933-RH-Linha-Protheus-GPE-Como-consultar-e-gerar-o-relat%C3%B3rio-de-mem%C3%B3ria-de-calculo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31604617363351) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**Como consultar e gerar o relatório de memória de calculo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.23.  
  
**Solução**

Incluídas opções de Consulta em tela e Impressão de Relatório para os *logs* gerados durante os cálculos. Realizada implementação da funcionalidade de geração de Memória de Cálculo para o cálculo de médias, adicionais, benefícios e pensão. O relatório de memória de cálculo, pode ser acessado nas seguintes rotinas:

* Consulta de Cálculo por Funcionário (GPEA090)
* Cálculo de Férias (GPEM030)
* Cálculo de rescisão (GPEM040)
* Cálculo de dissídio retroativo  
    
  ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11762551359767)

Para imprimir o relatório da memória de cálculo siga os passos abaixo:

1. Necessário habilitar o mnemônico **P\_LMEMCALC** e realizar o cálculo. Para habilitar o mnemônico acesse **Atualizações > Definições de Cálculo > Mnemônicos (GPEA300)**, e pesquise pelo mnemônico. Altere o Mnemônico **P\_LMEMCALC** para **.T.** para que possa ser recriadas as fórmulas com o *Log* Ativado.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31649707668375)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31649736139415)

**Observação:** Ao salvar a alteração, o processo pode demorar um pouco pelo fato do sistema recriar as fórmulas.

A cada fórmula executada, será gravado o *Log* com as informações de cálculo. (*\**Limitado, por hora, às formulas para cálculo de médias). Segue abaixo, Fórmulas / Funções disponíveis para geração de Log:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31649707671191)

**2.** Após habilitar o mnemônico realize novamente o calculo desejado. 

**3.** Na rotina que deseja imprimir o relatório, selecione o funcionário clique em **Outras Ações > Relatório memória de cálculo.**

Configure os parâmetros para selecionar o cálculo que deseja imprimir:

* Processo
  + Selecione o Processo de cálculo que deseja imprimir
* Roteiro
  + Selecione o Roteiro de cálculo que deseja imprimir
* Período
  + Através da Lupa (F3), selecione o Período, Nr. Pagamento, Data e Hora de Geração do cálculo que deseja imprimir.
  + Os registros listados são filtrados pelo Processo e Roteiro informados nas perguntas anteriores.
  + Os registros estão ordenados por Data e Hora de Geração em ordem decrescente, do mais novo ao mais antigo.
* Filial
  + Pergunta do tipo *range*. Informe a(s) filial(ais) que deseja imprimir ou mantenha em branco para imprimir todas as filiais do cálculo selecionado.
* Matrícula
  + Pergunta do tipo *range*. Informe a(s) matricula(s) que deseja imprimir ou mantenha em branco para imprimir todas as matrículas do cálculo selecionado

![](https://tdn.totvs.com/download/attachments/330831446/image2019-8-12_9-52-19.png?version=1&modificationDate=1565614339550&api=v2)

O relatório será impresso conforme abaixo:

![](https://tdn.totvs.com/download/attachments/330831446/image2019-8-12_9-52-55.png?version=1&modificationDate=1565614375620&api=v2)

![](https://tdn.totvs.com/download/attachments/330831446/image2019-8-12_9-53-24.png?version=1&modificationDate=1565614404687&api=v2)

**4.** Para consultar a memória de calculo em tela. Selecione o funcionário desejado no *browse* da rotina desejada, clique em Outras Ações > Consultar Memória de Cálculo e será apresentada uma tela listando os *logs* gravados para o funcionário selecionado, conforme exemplo abaixo emitido na rotina de rescisão:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31649707675543)

**Saiba Mais**  
Para adquirir maior conhecimento acesse os *links* abaixo  
[Documento Técnico Memória de Cálculo](https://tdn.totvs.com/pages/releaseview.action?pageId=330831446)   
[Melhorias Memória de Cálculo](https://tdn.totvs.com/pages/viewpage.action?pageId=791840585)  
[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
