---
article_id: 28272502990999
category: Escrita Fiscal - Configurador de Tributos
content_hash: 84c2ae522c2f3f5ac4452c22b9d615ecb2e8fe729dab8aa7e87ed8f82fe1f145
fetched_at: '2026-06-28T22:39:18.471238+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 – Como utilizar
  uma alíquota de ISS por Município com Configurador de Tributos.
type: support-article
updated_at: '2025-11-17T21:23:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28272502990999-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-utilizar-uma-al%C3%ADquota-de-ISS-por-Munic%C3%ADpio-com-Configurador-de-Tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28272516826263) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como utilizar uma alíquota de ISS diferente para cada Município utilizando o Configurador de Tributos (FISA170)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

Para definir uma alíquota de ISS para cada Município é necessário realizar o vínculo com o Código de Serviço ISS no cadastro do Produto e a Regra de Código de Prestação de Serviço no Configurador de Tributos.

* Configure o Parâmetro: **MV\_ISSXMUN = .T.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28272502949271)

* Configure o **Produto**, campo **Exe. Serviço (B1\_MEPLES) = 2 - LES**
* Caminho: Regras Fiscais > Cadastros > Regra de Código de Prestação de Serviço:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28272502952087)

* Informe o Código de Serviço que está vinculado no cadastro do Produto no campo B1\_CODISS:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28272516831383)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28272502955287)

* Em Tributos, informe o tributo ISS e a alíquota padrão a ser utilizada:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28272516838039) 

* Em alíquota Especifica por Município, informe o Estado, o Código do Município e a alíquota a ser utilizada:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28272516839447)

* Na Regra de Alíquota, no campo Valor Origem = 06 – Fórmula Manual e ajuste o campo Tipo de Alíquota = Percentual:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28272502963223)

* Após acesse a aba Detalhamento da Fórmula de Cálculo.

Em Tipo de Regra a ser consultada = 06 – Índices de Cálculo e no campo Consulta de Regra = I:ALQ\_SERVICO:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28272502964631)

**Procedimento ao Incluir a NF:**

* Ao acessar o Pedido de Venda, deverá informar os cadastros de Cliente e Produto normalmente. Porém, para que o sistema considere a alíquota por Município pelo Código de Serviço Cadastrado na FISA170 é necessário informar a UF e o Código do Município nos campos UF PREST. (C5\_ESTPRES) e MUN PREST (C5\_MUNPRES):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28272516851095)

 

Desta forma, o sistema irá considera a alíquota informada na Regra de Código de Prestação de Serviço.

Obs.: Com relação ao Código de Serviço utilizado para esta operação, o mesmo deverá constar não só no Produto (campo B1\_CODISS) e na Regra de Código de Prestação de Serviço, mas também na aba Código de Serviço do Perfil Tributário de Operação.

Abaixo encontram-se as demais documentações para auxiliar na configuração dos cadastros:

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FISA170 - Como deduzir o valor do imposto no tipo NF que gerou no Contas a Receber, onde o seu imposto gerou um tipo ISS no Contas a Pagar pelo configurador de tributos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/24300803419543-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-Como-deduzir-o-valor-do-imposto-no-tipo-NF-que-gerou-no-contas-a-receber-onde-o-seu-imposto-gerou-um-tipo-ISS-no-contas-a-pagar-pelo-configurador-de-tributos)

[Configurador de Tributos - Regras Financeiras](https://tdn.totvs.com/display/public/PROT/Configurador+de+Tributos+-+Regras+Financeiras#01-01)

[CFGTRIB - Código de Serviço ISS por Perfil de Operação](https://tdn.totvs.com/pages/releaseview.action?pageId=883676152)

[CFGTRIB - Cálculos no Configurador de Tributos](https://tdn.totvs.com/pages/viewpage.action?pageId=676039354)
