---
article_id: 6444603160599
category: Integrações Outros BackOffice
content_hash: 928a883f6ac0f9a726a7827df6d7d1fb428b1db44c64d217b571a26780f06caa
fetched_at: '2026-06-28T22:46:42.147215+00:00'
product: rm
section_id: 4410716084503
source: central-rm
title: 'RH - RM - FOP - Integração RM Labore x BackOffice Protheus: Mensagem não configurada
  ou configurada incorretamente para processamento pelo EAI'
type: support-article
updated_at: '2025-02-10T12:26:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6444603160599-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Labore-x-BackOffice-Protheus-Mensagem-n%C3%A3o-configurada-ou-configurada-incorretamente-para-processamento-pelo-EAI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29874127880855) Tempo aproximado para leitura: **00:03:27 min****Ocorrência**Quando está ativa a integração entre **RM x BackOffice Protheus**, ao tentar realizar alguma rotina para ser integrada pode gerar o erro que será referente ao ***adapter*** utilizado.  
Mensagem XXXXXXX não configurada ou configurada incorretamente para processamento pelo EAI  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Essa incidência acontece pois não há o cadastro do *adapter* que foi utilizado pela rotina, tanto no ambiente **RM** quanto no ambiente **Protheus**, também pode acontecer de já existir esse cadastro mas de forma incorreta.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

1. É altamente recomendável, caso desejar criar automaticamente as versões tanto no **RM** quanto no **Protheus**, executar o **Configurador de Integração** através do sistema **RM** em **EAI 2.0 | Configurador**, essa rotina irá trazer os padrões para comunicação.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6444044251799)

2. Caso realizar o cadastro manualmente, deverá acessar **SIGACFG>AMBIENTE>SCHEDULE>ADAPTER EAI** no **Protheus** e incluir o *adapter* que foi retornado no erro, caso já exista o cadastro deverá verificar se está configurado conforme o [Manual de Integrações.](https://tdn.totvs.com/display/public/INT/Manual_Doc_Integracao_RMLabore_BackOfficeProtheus)  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6443840741527)

3. Para cadastro manual no RM, acesse **Integrações | EAI 2.0 | Rotas.** Caso já exista o cadastro deverá verificar se está configurado corretamente conforme o [Manual de Integrações.](https://tdn.totvs.com/display/public/INT/Manual_Doc_Integracao_RMLabore_BackOfficeProtheus)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6443871823255)

Para a versão do **EAI 1.0** será utilizado o caminho **Integrações | Mensagem Única | Integrações | Anexos | Mapeamento de Entidades**.

**Importante**

Pode acontecer do sistema **RM** não ter as mesmas versões de adapter indicadas conforme tabela de *adapter*, mas no sistema Protheus deve seguir rigorosamente o cadastro sempre que possível.
