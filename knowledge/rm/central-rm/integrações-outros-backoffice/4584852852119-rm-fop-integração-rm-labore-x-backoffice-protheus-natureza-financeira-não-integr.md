---
article_id: 4584852852119
category: Integrações Outros BackOffice
content_hash: 81fad16ac4e72c94edede99e761a25022193d92ad0eec2bcf559e3e4bc0adbf1
fetched_at: '2026-06-28T22:46:42.162173+00:00'
product: rm
section_id: 4410716084503
source: central-rm
title: RM - FOP - Integração RM Labore x BackOffice Protheus - Natureza Financeira
  não integrado
type: support-article
updated_at: '2025-02-10T17:25:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4584852852119-RM-FOP-Integra%C3%A7%C3%A3o-RM-Labore-x-BackOffice-Protheus-Natureza-Financeira-n%C3%A3o-integrado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:38 min****Ocorrência**No módulo da Folha de Pagamento, ao tentar realizar a integração do Lançamento Financeiro ao Protheus utilizando Natureza Financeira retorna erros.  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Essa incidência acontece pois os não há o registro de DE/PARA no ambiente RM e também no ambiente Protheus.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Caso o retorno do erro seja apresentado **"Código Natureza Financeira "X" não integrado"**:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4584546299799/mceclip1.png)

Deverá informar diretamente no **RM** um novo DE/PARA para essa Natureza na tabela **TTBORCAMENTO**, no exemplo acima retornou o erro para o código 1.

Imaginemos as seguintes entidades para mapeamento.

No RM:

* Coligada - 1
* Filial - 1

No Protheus:

* Grupo de Empresa - 01
* Filial - 0101
* Desejo integrar o lançamento para que utilize a Natureza de código 001 do Protheus.

O DE/PARA será feito da seguinte maneira.

**Tabela RM:** TTBORCAMENTO

**Campos RM:** CODCOLNATFINANCEIRA|CODNATFINANCEIRA

**Valores RM:** Coligada do RM|Código do erro (seguindo o exemplo será 1|1)

**Aplicativo:** Integração ativa

**Valores externos:** Grupo de Empresa|Filial|Codigo da Natureza do Protheus (Seguindo o exemplo será 01|0101|001)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4584609294999/mceclip2.png)

O erro irá se alterar para a mensagem **retornada pelo Protheus** sendo **"Natureza não encontrada no de/para. -> 1|1.**

Caso seja exibido esse novo retorno, significa que o DE/PARA por parte do RM foi feito corretamente e ficou pendente o DE/PARA do Protheus. Se essa mensagem não for exibida e ainda sim retornar o erro anterior é possível ter que realizar o cadastro do DE/PARA como Coligada 0 pois existem ambientes que utilizam de forma global.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4584633934231/mceclip3.png)  
2. Para solucionar a nova mensagem de erro, devemos acessar o **Protheus** em **SIGACFG | Ambiente | Schedule | De/Para Mensagem Única** e adicionar o registro para:

* **Tabela** - SEDXXX (Onde XXX será o Grupo de empresas em meu caso **01**0)
* **Alias** - SED
* **Campo** - ED\_CODIGO
* **Valor externo** - Informar o valor do RM
* **Valor interno** - Informar o valor do Protheus

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4584689509143/mceclip4.png)

Após acrescentar também o DE/PARA do Protheus, ao executar novamente a integração não será apresentada a mensagem de erro referente à Natureza Financeira.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4584756233367/mceclip5.png)
