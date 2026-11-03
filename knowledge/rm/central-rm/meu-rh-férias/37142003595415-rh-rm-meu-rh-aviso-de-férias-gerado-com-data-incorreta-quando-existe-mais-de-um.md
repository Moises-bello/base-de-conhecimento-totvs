---
article_id: 37142003595415
category: Meu RH - Férias
content_hash: 16393f1fe0a1e41af4b258f3b1aea229235be6b7695699f35a3bbea0a7fd448d
fetched_at: '2026-06-28T22:47:31.624431+00:00'
product: rm
section_id: 1500000835241
source: central-rm
title: RH – RM – Meu RH – Aviso de Férias gerado com data incorreta quando existe
  mais de um período de férias marcado
type: support-article
updated_at: '2025-12-19T14:51:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37142003595415-RH-RM-Meu-RH-Aviso-de-F%C3%A9rias-gerado-com-data-incorreta-quando-existe-mais-de-um-per%C3%ADodo-de-f%C3%A9rias-marcado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37142019240215) Tempo aproximado para leitura: **00:03:25 min**  
  
**Ocorrência**  
Quando um colaborador possui mais de um período de férias cadastrados no Meu RH, ao gerar e baixar os avisos, todos os documentos são emitidos com a mesma data do primeiro período de férias, mesmo que os demais períodos estejam registrados corretamente no sistema.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37143819547159)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37143585574935)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir do release 12.1.2406  
  
**Causa**  
O relatório padrão "Aviso de Férias" do RM Reports, foi desenvolvido a partir da utilização da tabela **PFUNC** como fonte de dados, dessa forma consegue atender apenas a impressão do aviso de férias do período de gozo mais próximo, tendo em vista que o mesmo fica gravado na tabela. Os demais períodos de gozo marcados, só passam a alimentar a tabela conforme o primeiro altera seu status para finalizada.  
  
**Solução**  
O RM está em constante evolução e vem adotando o Smart View como padrão para o sistema de relatórios. Nesse cenário, nosso time de desenvolvimento está criando novos relatórios alinhados a essa tecnologia, e já está disponível o relatório padrão **"FOPTRP0001 – Aviso de Férias"**, que permite a geração correta do aviso mesmo quando há mais de um período de gozo marcado.  
  
Para utilizar esse novo relatório do Smart View, realize os seguintes passos:  
  
1. Parametrize o Smart View no RM conforme os passos desta documentação: [Instalação e Configuração do Smart View](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13311540250007-Cross-Segmentos-Backoffice-RM-BI-Instala%C3%A7%C3%A3o-e-Configura%C3%A7%C3%A3o-do-Smart-View)  
  
2. Realize o download do relatório **FOPTRP0001 – Aviso de Férias** através do [TOTVS Compartilhamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7781155867543-RH-RM-FOP-Importa%C3%A7%C3%A3o-de-relat%C3%B3rios-e-layouts-atrav%C3%A9s-do-Totvs-Compartilhamento)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37142003586071)  
  
3. Acesse Folha de pagamento > Configurações > Parametrizador > *Edite o quiosque do funcionário* > Férias. Marque a flag **Relatorios do Smart View"** e vincule o relatório "**FOPTRP0001"** em **Aviso de Férias.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37142019240983)

Após realizar essa parametrização, será possível gerar corretamente o aviso de férias quando houver mais de um período de gozo marcado, exibindo as datas correspondentes a cada um deles.

**Meu RH:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37142019241623)

**Download dos avisos:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37142003587479)

**Saiba mais:**

[**RH - RM - Meu RH - Como Gerar o Demonstrativo de Pagamento com relatório via SmartView**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36814407779991-RH-RM-Meu-RH-Como-Gerar-o-Demonstrativo-de-Pagamento-com-relat%C3%B3rio-via-SmartView)

[**Documentos de Referência Smart View**](https://tdn.totvs.com.br/pages/viewpage.action?pageId=632492810)
