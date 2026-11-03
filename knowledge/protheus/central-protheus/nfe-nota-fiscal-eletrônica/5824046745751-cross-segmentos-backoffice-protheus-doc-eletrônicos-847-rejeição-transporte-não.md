---
article_id: 5824046745751
category: NFe - Nota Fiscal Eletrônica
content_hash: 8aee87d9da84bc37958dc2cdf31f0fa2656d8f4887d9b6a1ebf06c40371ce908
fetched_at: '2026-06-28T22:40:05.381196+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 847 Rejeição: Transporte
  não é próprio por conta do Remetente e CNPJ Base ou CPF do Transportador igual ao
  CNPJ Base ou CPF do Remetente'
type: support-article
updated_at: '2025-06-25T11:49:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5824046745751-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-847-Rejei%C3%A7%C3%A3o-Transporte-n%C3%A3o-%C3%A9-pr%C3%B3prio-por-conta-do-Remetente-e-CNPJ-Base-ou-CPF-do-Transportador-igual-ao-CNPJ-Base-ou-CPF-do-Remetente
---

**Dúvida**Como solucionar a 847 Rejeição: Transporte não é próprio por conta do Remetente e CNPJ Base ou CPF do Transportador igual ao CNPJ Base ou CPF do Remetente  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Se for NF-e de saída (tpNF=1) e Modalidade do Frete <> 3 ***(id: X02, campo: modFrete), o CNPJ Base (id: X04, campo: CNPJ)*** ou **CPF (id: X05, campo: CPF)** do transportador deve ser DIFERENTE do CNPJ Base **(id: C02, campo: CNPJ)** ou CPF do Remetente **(id: C03, campo: CPF)**

1. Verifique se a modalidade do frete correta no campo é opção ***3=****Transporte Próprio por conta do Remetente;** **e altere no campo C5\_TPFRETE Tipo Frete.***

![Tipo_frete.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11928684074007)

2. Após isso, exclua a nota e gere novamente.

*3.* Se caso opção de modalidade do frete for diferente de 3 no campo ***C5\_TPFRETE Tipo Frete***

**0=**Contratação do Frete por ***conta do Remetente (CIF);***

**1=**Contratação do Frete por ***conta do Destinatário (FOB);***

**2=**Contratação do Frete por ***conta de Terceiros;***

**4=**Transporte ***Próprio por conta do Destinatário;***

***9=Sem Ocorrência de*** Transporte;

4. Acessar Cadastro de Contribuinte da UF ***(Chave: UF Retirada , IE Retirada)*****Cadastro Centralizado de Contribuinte (CCC)**[Clique Aqui](https://dfe-portal.svrs.rs.gov.br/Nfe/Ccc) e verificar o CNPJ correto da transportadora e alterar no cadastro da transportadora no campo ***CNPJ A4\_CGC.***

![ccc.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11928739118871)

5. Após isso, exclua a nota e gere novamente.

***Observação 1:*** Regra de validação não se aplica quando ***CNPJ/CPF*** do transportador não for informado.

1. Se não houver um  ***CNPJ/CPF*** transportador, retire o conteúdo do  ***CNPJ/CPF no campo*** ***A4\_CGC vinculado no campo C5\_TRANSP***

***![transp_cnpj.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11928741047831)***

2. Após isso, exclua a nota e gere novamente.

***Observação 2:*** Regra de validação não se aplica quando CNPJ Base ou CPF do emitente for igual ao CNPJ Base ou CPF do destinatário e CFOP é de operação com combustíveis ***(indComb= 2)***, conforme Tabela  
CFOP.

1. Configurar a Nota com ***combustível conforme abaixo:***

Para habilitar a opção de complemento de combustível nos Livros Fiscais, você deverá:  
  
1. Incluir um grupo de produto (**Combustíveis**);

![GRUPO_DE_PRODUTO.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33040459558295)

2. Alterar o cadastro do produto e vincular o grupo no campo **B1\_GRUPO;**

**![GRUPO_DE_PRODUTO.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33040459558295)**

3. Informar o grupo no parâmetro **MV\_COMBUS;**

**![MV_COMBUST.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33040459559959)**

4. Após gerar a nota, acessar: **Livros Fiscais > Atualizações > Movimentos > NF-e Manual de Entrada / Saída > Complementos;**

**![COMP._COMBUSTIVEL.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33040447432599)**

**Na versão 4.00 da NF-e será necessário informar os quatro campos abaixo:  
  
· CD6\_CODANP**

**· CD6\_DESANP**

**. CD6\_UFCONS**

**. CDD\_IFCOMP**

Existe a possibilidade do preenchimento automático dos campos da CD6 para isso usar o ponto de entrada MATUCOMP.

Existe a possibilidade do campo CDD\_IFCOMP ser preenchido automaticamente. Para isso é necessário ativar o parâmetro MV\_ATUCOMP e usar o ponto de entrada MATUCOMP, abaixo documentação:   
  
<https://tdn.totvs.com/pages/releaseview.action?pageId=642645988>

* **Saiba mais:**

[Nota Técnica 2016.002 - v 1.61 (publicada em 10/09/2018)](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=zfWxcJtOf98=)

Ao clicar no link acima será aberto um PDF com NT.

**Página 51**

**0=**Contratação do Frete por conta do Remetente (CIF);

**1=**Contratação do Frete por conta do Destinatário (FOB);

**2=**Contratação do Frete por conta de Terceiros;

**3=**Transporte Próprio por conta do Remetente;

**4=**Transporte Próprio por conta do Destinatário;

**9=**Sem Ocorrência de Transporte.

* **Saiba mais:**

Referente ao ***redespacho,*** temos um parecer da consultoria no link abaixo:

*[Clique Aqui](https://tdn.totvs.com/display/public/ConSeg/REDESPACHO)*

Conforme a ***NT 2021.004\_V\_1.33*** a regra de validação será para ***implementação futura.***
