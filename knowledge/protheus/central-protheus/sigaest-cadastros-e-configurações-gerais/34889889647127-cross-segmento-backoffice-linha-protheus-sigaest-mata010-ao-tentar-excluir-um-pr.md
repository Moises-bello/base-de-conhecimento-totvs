---
article_id: 34889889647127
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: fcbec334620f9376275a9f76d34ea823632501f3ea53458edd380694adb20afb
fetched_at: '2026-06-28T22:39:09.397596+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA010 - Ao tentar
  excluir um produto ocorre - Alias does not exist TNF
type: support-article
updated_at: '2025-09-12T12:55:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34889889647127-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-Ao-tentar-excluir-um-produto-ocorre-Alias-does-not-exist-TNF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34889904964631) Tempo aproximado para leitura: **00:02:00 min**

**Ocorrência**

Durante a criação de um produto, foi identificado que não há vínculo ou utilização do módulo **35 – Medicina e Segurança do Trabalho**, no qual a tabela **TNF** é alimentada pela rotina **Funcionário x EPI (MDTA695)**.  
Ao acessar a rotina, ocorre o seguinte erro:

```
TNF: TOP Error -19 - not found for table [TNF]. (From tISAMFile::CreateIndex)  
(PREVIOUS ERROR: Alias does not exist: TNF) on TABLECREATE(APLIB200.PRW)
```

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Causa**  
O problema ocorre devido a indices incorretos na tabela TNF

**Solução**

### **Valide se os índices da tabela TNF estão padronizados conforme a tabela SIX.**

* A quantidade e a ordem dos índices devem ser idênticas conforme imagens a seguir:

  ![TNFINDICE.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34890204512023)

  ![TNFINDICE2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34890189464215)

  ![TNFINDICE3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34890189464727)

### **Caso a tabela TNF não apresente os mesmos índices definidos na SIX:**

* Será necessário realizar manutenção para recriação dos índices.
* Para isso, envolva o time técnico responsável e proceda da seguinte forma:
  + **Se não houver dados na tabela TNF:** realizar o *drop* da tabela diretamente.
  + **Se houver dados:** efetuar previamente um ***backup***completo antes do *drop sempre.*

Após o *drop*:

* Acesse novamente a rotina **MDTA695** para que a tabela **TNF** seja recriada automaticamente.
* Valide se os índices foram recriados corretamente dentro da própria tabela, de acordo a quantidade de indices existentes na SIX

#### **Observação**

* Em anexo, encontra-se a tabela **SIX** filtrada pela **TNF**, para validação técnica pelo seu time de infraestrutura, caso necessário.
* Os índices foram coletados em **12/09/2025**. Ressalta-se que podem sofrer alterações em versões futuras; portanto, recomenda-se sempre validar as atualizações mais recentes do produto.

**Saiba mais:**

[*Clique aqui para mais informações sobre a MATA010*](https://tdn.totvs.com/display/public/PROT/Produtos+-+MATA010#ProdutosMATA010-PastaCadastrais)

[*Clique aqui e veja mais artigos sobre Cadastros e Configurações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Configuração de envio Messenger para ID de eventos do Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003963562-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Configura%C3%A7%C3%A3o-de-envio-Messenger-para-ID-de-eventos-do-Estoque)
