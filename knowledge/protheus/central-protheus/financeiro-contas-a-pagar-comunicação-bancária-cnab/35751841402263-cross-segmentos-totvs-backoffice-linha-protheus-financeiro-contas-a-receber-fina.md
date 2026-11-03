---
article_id: 35751841402263
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 6eec32d37014a0edb946c386ab403eea45dd08e5d52865052490561715a34948
fetched_at: '2026-06-28T22:37:55.128411+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Financeiro - Contas
  a Receber - FINA200 - HELP: ARQUIVO NÃO ENCONTRADO'
type: support-article
updated_at: '2025-10-20T14:54:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35751841402263-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Financeiro-Contas-a-Receber-FINA200-HELP-ARQUIVO-N%C3%83O-ENCONTRADO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35751827370647) Tempo aproximado para leitura: **00:10 min**  
  
**Ocorrência**  
No módulo Financeiro, ao tentar realizar a baixa do arquivo de retorno via FINA200 - Retorno de cobranças, ocorre a mensagem de erro **"HELP: ARQUIVO NÃO ENCONTRADO".**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35751827371031)  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Causa**  
Esse incidente ocorre porque o ambiente **não está configurado para utilizar o WebAgent**, o que **impede a validação de arquivos locais na máquina do usuário**.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. **Acesse a página inicial do Protheus e clique abaixo do ambiente na engrenagem ⚙️**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35751827371415)

2. Marque a opção de **"Habilita/Desabilita o Agente Local"**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35751841379479)

3. Efetue o download do **WebAgent** e instale-o na máquina local.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35751841379863)

4. Após os passos acima, efetue novamente a baixa do arquivo de retorno e será efetuada a baixa via CNAB.  
  
**Saiba mais**  
[**TOTVS | WebAgent**](https://tdn.totvs.com/display/tec/2.+WebApp+-+WebAgent)  
[**Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Principais configurações e dúvidas para uso do CNAB**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7778595184407-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Principais-configura%C3%A7%C3%B5es-e-d%C3%BAvidas-para-uso-do-CNAB)
