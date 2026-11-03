---
article_id: 360016141732
category: Financeiro - Contas a Pagar
content_hash: 80698524cbd41e90224d65708b25ae3e75c3601bae3f568a282308f3a8a458b1
fetched_at: '2026-06-28T22:38:07.043473+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN   - FINA870 - Como gerar
  Aglutinação de títulos de INSS
type: support-article
updated_at: '2026-01-28T16:43:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016141732-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA870-Como-gerar-Aglutina%C3%A7%C3%A3o-de-t%C3%ADtulos-de-INSS
---

**Dúvida**  
Como gerar Aglutinação de Títulos de INSS?  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Financeiro -  FINA870 - A partir da versão 11.80  
  
**Solução**  
Para realizar a aglutinação de títulos de INSS, é necessário efetuar as seguintes configurações e validações:

**1. Cadastro de Fornecedor**  
Aba impostos ajustar os campos **Calcula INSS** definido como **Sim** e o campo **Porc. INSS** preenchido com a porcentagem correspondente à retenção aplicável, conforme a necessidade.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37995303116439)

**2. Cadastro de Fornecedor**

Aba cadastrais, campo CNPJ cadastrado

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37995303117847)

Selecione a aba, fiscais, o campo **Calcula INSS** = Sim.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37995303118743)

**3. Inclusão do Título – Contas a Pagar (FINA050)**  
Inclua um título com retenção de INSS, observando as configurações acima.

* Na aba **Outros**, aplique o código de retenção de INSS por meio do campo **Ret. INSS (E2\_RETINS)**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37995298836887)

**4. Emissão de GPS (FINA870)**  
Após a inclusão do título, acesse a rotina **Emissão de GPS (FINA870) e** preencha as informações dos parâmetros. Os títulos relacionados à retenção de INSS serão automaticamente aglutinados em um único título, com o prefixo **AGI**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37995298837527)

**Importante**

Caso o Código de Retenção não esteja cadastrado, acesse o Configurador, na rotina Ambiente. Em seguida, selecione Cadastro, escolha a Tabela correspondente, clique em Editar, acesse Itens, selecione a última linha disponível e grave o registro.

**Saiba mais**

[Emissão de GPS (FINA870 - SIGAFIN)](https://tdn.totvs.com/pages/releaseview.action?pageId=528467281)
