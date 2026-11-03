---
article_id: 4421892365591
category: Financeiro - Contas a Pagar - Dirf
content_hash: 5c417a28f55a9239e2275df697fb3a7ea69ae9d687dd1e25b143587247ab9181
fetched_at: '2026-06-28T22:38:10.708570+00:00'
product: protheus
section_id: 1500001550482
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus- SIGAFIN - FINA401 - Relatório de
  conferência da DIRF fornecedores Internacionais
type: support-article
updated_at: '2022-02-07T18:04:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4421892365591-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA401-Relat%C3%B3rio-de-confer%C3%AAncia-da-DIRF-fornecedores-Internacionais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Ao gerar o relatório de conferencia da **DIRF** com títulos incluídos no financeiro para fornecedores internacionais, nome não é apresentado.

**Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) - TOTVS SIGAFIN - A partir da versão 12.1.27  
  
**Solução**Para fornecedores internacionais devem seguir as seguintes configurações para geração da DIRF:

Aba **Cadastrais**:

**Estado**: EX

**Município**: A seu Critério (Nova York)

**Tipo**: Outros

**País**: código do pais (disponível no site da receita federal)

<http://idg.receita.fazenda.gov.br/orientacao/tributaria/declaracoes-e-demonstrativos/dirf-declaracao-do-imposto-de-renda-retido-na-fonte>

![](https://tdn.totvs.com/download/attachments/267798349/dirf%201.jpg?version=1&modificationDate=1476802604000&api=v2)

Aba **Residente** **Exterior**:

**Nome** **Empresa**: Nome do Fornecedor no exterior

**Código** **NIF**: Receita quem disponibiliza

**Código** **do** **país**: código do pais (disponível no site da receita federal)

<http://idg.receita.fazenda.gov.br/orientacao/tributaria/declaracoes-e-demonstrativos/dirf-declaracao-do-imposto-de-renda-retido-na-fonte>

Rendimento: Código disponibilizado pela receita (Cliente sabe qual deve ser utilizado)

**Form** **Trib**.: Código disponibilizado pela receita (Cliente sabe qual deve ser utilizado)

**Benef**. **Rend**:  Código disponibilizado pela receita (Cliente sabe qual deve ser utilizado)

![](https://tdn.totvs.com/download/attachments/267798349/dirf2.png?version=1&modificationDate=1476802604000&api=v2)

Se no título a pagar de um fornecedor residente no exterior, não for utilizado um código de retenção (**E2\_CODRET**)  relacionado a pagamentos no exterior, deve-se preencher o campo **CNPJ**/**CPF** ( **A2\_CGC**) no **Cadastro de Fornecedores** da aba "**Cadastrais**", para que o mesmo seja enviado para a **DIRF** como rendimento tributável nacional:

![](https://tdn.totvs.com/download/attachments/267798349/image2018-11-12_10-43-50.png?version=1&modificationDate=1542030231147&api=v2)

**Saiba Mais**:  
<https://tdn.totvs.com/pages/viewpage.action?pageId=224126168>
