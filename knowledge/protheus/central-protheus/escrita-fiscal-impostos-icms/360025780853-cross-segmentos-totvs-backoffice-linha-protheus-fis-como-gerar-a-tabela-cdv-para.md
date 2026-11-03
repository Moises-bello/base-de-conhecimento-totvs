---
article_id: 360025780853
category: Escrita Fiscal - Impostos - ICMS
content_hash: 485f6c58c8faef6a56f8c3e8449ab06f010bab251b8285af725c00105baf12ff
fetched_at: '2026-06-28T22:39:25.554815+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Como gerar a tabela
  CDV para alimentar a tag cBenef para o estado do RJ com os valores desonerados (RESOLUÇÃO
  SEFAZ 13 DE 14/02/2019 RJ) e para outros processos?
type: support-article
updated_at: '2021-07-20T14:12:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025780853-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-gerar-a-tabela-CDV-para-alimentar-a-tag-cBenef-para-o-estado-do-RJ-com-os-valores-desonerados-RESOLU%C3%87%C3%83O-SEFAZ-13-DE-14-02-2019-RJ-e-para-outros-processos
---

**Dúvida**

Como gerar a tabela CDV para alimentar a tag cBenef para o estado do RJ com os valores desonerados e para outros processos?  
  
**Ambiente**

Protheus - Livros Fiscais - A partir da versão 12.1.17  
  
**Solução**

Para gerar a tabela CDV realize os seguintes passos:

**1. Parâmetros:**

MV\_ESTADO = RJ  
MV\_GIAEFD = F

2. Importar os códigos de lançamento da tabela 5.2 do estado do RS pelo U\_IMPSPED ou cadastrar manualmente na rotina FISA156 - Códigos de Valores Declaratórios.

Para importar a tabela, siga os passos abaixo:

- Realizar o *download* da tabela 5.2 através do portal do SPED na receita federal (<http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal>):

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045667353/mceclip0.png)

- Após realizado o *download*, é necessário renomear a tabela para o nome **"TABELA52.TXT"**.

- Colocar a tabela dentro da pasta Protheus\_Data

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044294174/mceclip1.png)

- Executar o Protheus com a opção "U\_IMPSPED":

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045150333/mceclip2.png)

- Selecionar a pasta onde está o arquivo e clicar em "Abrir"

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045150513/mceclip3.png)

- Confirmar a execução para importação das tabelas:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044294434/mceclip5.png)

3. Criar a amarração na rotina FISA140 - Prod. x Cod.V.Decl.

Necessário informar:   
- Produto 

- CFOP da operação a ser aplicado aquele código

- Cod. Val. Decl (Tabela 5.2 da receita federal)

- CST 

- Código de Reflexo conforme a sua necessidade

Exemplo 1: para Valor Desonerado, configurar a TES:

Calcula ICMS = Sim

L. Fiscal ICMS = Isento

CFOP da operação a ser utilizado

Sit Trib ICM = da operação a ser utilizado

TES Aba: Outros  
Campo: F4\_MOTICMS  
Título: Mot.Desone

**Importante: Para Valor Desonerado o código de reflexo deverá ser conforme abaixo, por exemplo:**

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045671473/mceclip6.png)

Exemplo 2: Caso seja necessário gravar o valor do ICMS na Tag CBenef:

Criar a amarração na rotina FISA140 - Prod. x Cod.V.Decl.

Necessário informar:   
- Produto 

- CFOP da operação a ser aplicado aquele código

- Cod. Val. Decl (Tabela 5.2 da receita federal)

- CST 

- Código de Reflexo conforme a sua necessidade, por exemplo:

Base p/ calc. = Base ICMS

Alíquota = Alíquota de ICMS

Valor = valor do ICMS

Configurar a TES:

Calcula ICMS = Sim

L. Fiscal ICMS = Isento

CFOP da operação a ser utilizado

Sit Trib ICM = da operação a ser utilizado

**Facilitador**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045667833/mceclip2.png)

Dentro da rotina FISA140 está disponível um facilitador que permite importar os produtos. Após preencher o CFOP, CST e Código de reflexo, a rotina irá incluir automaticamente todos os produtos com as regras cadastradas. Exemplo:

Preencha as perguntas com os filtros desejados:

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045151493/mceclip7.png)

Na tela apresentada a seguir, preencha os campos apresentados para que o sistema faça a inclusão destes códigos para todos os produtos encontrados.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045667773/mceclip1.png)

**Importante: O código de reflexo utilizado deverá retornar algum valor para que as informações sejam gravadas na CDV. Se o campo Valor (CE0\_NFVALO) retornar zero as informações não serão gravadas.**

4. Para verificar se os valores serão gravados na CDV acessar na planilha do pedido de venda na aba Lançamento da apuração ->Val Declaratório.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045180293/mceclip0.png)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044808594/mceclip4.png)

**5.****Documentação completa:**

<http://tdn.totvs.com/pages/releaseview.action?pageId=469449117>

<http://tdn.totvs.com/display/public/PROT/FIS0069_DIFERIMENTO_ICMS>

**Dicionário - Todas as Release´s**:

 **Link: <https://suporte.totvs.com/portal/p/10098/download#detail/765125>**
