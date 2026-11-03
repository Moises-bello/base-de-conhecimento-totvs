---
content_hash: 2ae35514155c7ab394dcb21cc31434827addf0782668d140a271acd8940a2bd7
fetched_at: '2026-06-29T00:11:38.824981+00:00'
page_id: '785419528'
product: rm
source: tdn-rm
title: Alterações do Layout 2023 - Versão 2.1.2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=785419528
version: 13
---

#f5f5f5#363636

Foi publicado o [ATO DECLARATÓRIO EXECUTIVO COFIS Nº 23, DE 10 DE MARÇO DE 2023](http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=129523), que aprova a versão 2.1.2 dos leiautes dos arquivos que compõem a Escrituração Fiscal Digital de Retenções e Outras Informações Fiscais - EFD-Reinf (Eventos R-4000). Essa versão será exigida para os eventos ocorridos a partir da competência de Setembro de 2023.

Com os Eventos R-4000, a Receita Federal inicia uma nova Fase na obrigação: a inclusão de outros tributos federais como PIS, COFINS, CSLL e o IRRF. Essa fase, portanto, completa a Evolução da EFD-REINF e mantém a mesma escritura de eventos.

Devem ser declarados nos eventos R-4000 todas Retenções na fonte (IR, CSLL, COFINS, PIS/PASEP) que são incidentes sobre os pagamentos diversos efetuados às pessoas físicas e jurídicas.

#f5f5f5#363636Alterações

Antes de avaliar as alterações da versão 2.1.2, sugerimos que sejam consultadas as alterações da versão 2.1.1 no link

**Registros:**

01lefttrue01\_1Visão Geral dos Registros

**Tipos de Registros:**

**[R-2030](https://tdn.totvs.com/pages/viewpage.action?pageId=715830674)** - Recursos recebidos por associação desportiva  
**[R-4010](https://tdn.totvs.com/pages/viewpage.action?pageId=733184530)** - Pagamentos/créditos a beneficiário pessoa física  
**[R-4020](https://tdn.totvs.com/pages/viewpage.action?pageId=733190896)** - Pagamentos/créditos a beneficiário pessoa jurídica

R-2030R-2030

**R-2030 - Recursos recebidos por associação desportiva**

O Evento R-2030 passa a gerar os seguintes campos:**recEmprExt** e **nmEmprExt.** Para mais informações, acesse:

R-4010R-4010

**R-4010 - Pagamentos/créditos a beneficiário pessoa física**

* O Evento R-4010 não será gerado para os Lançamentos Financeiros que estiverem configurados para gerar no e-Social. Para mais informações, acesse:
* Ao incluir Movimento ou Lançamento Financeiro, utilizando uma Natureza de Rendimento com campo "**Rendimento Isento/Não Tributável**" configurado, ao gerar a EFD-REINF apenas o valor bruto será gerado e os valores referentes a retenção não serão gerados mesmo que esteja preenchido no tributo.
R-4020R-4020

**R-4020 - Pagamentos/créditos a beneficiários não identificados**

* O Evento R-4020 passou a permitir a geração de um Evento com origens Financeira e Fiscal simultaneamente. Exemplo: IR configurado com origem Fiscal e as Retenções configuradas com Origem Financeiro.
* O campo **isenImun** passa a não ser mais gerado.

Para mais informações, acesse:

**Movimento:**

O Movimento passou a preencher os Defaults da Natureza de Rendimento conforme condições a seguir:

Para as retenções de**PISRF, COFINSRF, COSIRF, CSLLRF e CSRF**, o Campo Natureza de Rendimento no Tributo do Item do Movimento passa a ser o preenchido conforme abaixo:

* Se preenchido no Cadastro do Produto (Anexo – Dados Fiscais do Produto – Campo Código de Natureza de Rendimento), considera este;
* Senão, se preenchido no Cadastro do Cliente\ Fornecedor (Tributos, demais tributos na pasta Tributos Default do Fornecedor), considera este;
* Senão, considera o preenchido no tipo de Movimento.

Para mais informações, acesse:

#f5f5f5#363636TSS (TOTVS Service SOA)

Para a versão 2.1.2 da EFD-REINF, o TSS também liberou várias atualizações. Antes de iniciar os testes, faça a atualização do TSS conforme link abaixo:

* [Atualização do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-MP-TSS-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS)
#f5f5f5#363636Relatórios


#f5f5f5#363636Outras Informações

As alterações foram disponibilizadas nos patches

* 12.1.2302.207
* 12.1.2306.151
* 12.1.2310
