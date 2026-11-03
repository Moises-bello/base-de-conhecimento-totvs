---
article_id: 360046633454
category: eSocial - Middleware
content_hash: c24b1ca57e66aa914dc8992b29c02bcb07452b30fc8ad3447faa6a01e12604d0
fetched_at: '2026-06-28T22:47:05.637803+00:00'
product: rm
section_id: 1500000834541
source: central-rm
title: RH - RM - FOP - eSocial - Geração da tag ideDmDev com prefixo para múltiplos
  vínculos na mesma coligada
type: support-article
updated_at: '2024-08-06T20:27:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046633454-RH-RM-FOP-eSocial-Gera%C3%A7%C3%A3o-da-tag-ideDmDev-com-prefixo-para-m%C3%BAltiplos-v%C3%ADnculos-na-mesma-coligada
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23948931424407)** Tempo aproximado para leitura: **00:01:00 min****Dúvida**  
Como gerar no S-1200 a tag **ideDmDev** com prefixo para múltiplos vínculos na mesma coligada?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial  - A partir dos *Patches*12.1.26.206, 12.1.27.155 e 12.1.28.000  
  
**Solução**  
Para geração do prefixo será necessário observar onde o vínculo está cadastrado (TOTVS Folha de Pagamento ou TOTVS Gestão Financeira). Veja abaixo onde preencher o prefixo de acordo com o cadastro:

• **TOTVS Folha de Pagamento**

1. Acesse o módulo **Folha de Pagamento** e o menu **Administração de Pessoal | Funcionários**;  
2. Edite o funcionário desejado e acesse na lateral a opção **Informações para o Cálculo | Parâmetros**;  
3. Preencha o campo **Prefixo Período (eSocial)**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25443860051863)

• **TOTVS Gestão Financeira**

1. Acesse o módulo **Gestão Financeira** e o menu **Cadastros | Clientes Fornecedores**;  
2. Edite o cliente/fornecedor desejado e acesse **Anexos | eSocial**;  
3. Preencher o campo **Prefixo Período**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25456706966295)

**Importante**  
O prefixo poderá ser preenchido com números e/ou letras. O valor preenchido neste campo será concatenado na *tag* **ideDmDev**, impedindo assim que ocorra duplicidade de períodos.  
  
**Saiba mais**  
Para mais informações acesse:  
      • [Como gerar no S-1200 a tag <ideDmDev> com prefixo para múltiplos vínculos na mesma coligada?](https://tdn.totvs.com/pages/releaseview.action?pageId=544732520)
