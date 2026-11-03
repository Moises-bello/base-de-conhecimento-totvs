---
article_id: 1500001834761
category: Escrita Fiscal - Error.log
content_hash: 47d560f9568bc3b8309f7760453292787e3a5c90b9e1fc84c9ac4b459ee513b7
fetched_at: '2026-06-28T22:39:32.867755+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Solucionar mensagem
  CPF Rural / Valor inválido (CPF Rural) ao preenche o campo A2_CPFRUR
type: support-article
updated_at: '2021-07-08T13:21:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001834761-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Solucionar-mensagem-CPF-Rural-Valor-inv%C3%A1lido-CPF-Rural-ao-preenche-o-campo-A2-CPFRUR
---

**Dúvida**

Como Solucionar mensagem CPF Rural / Valor inválido (CPF Rural) ao preenche o campo A2\_CPFRUR no cadastro de Fornecedores?

**Ambiente**

Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Conferir configuração e se necessario criar o parâmetro MV\_TAFESLB := SP|MG|RJ ; **<https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=573530961>**

**Habilitar o preenchimento do campo A2\_CPFRUR**

Para habilitar preenchimento do campo "A2\_CPFRUR" precisa atender as seguintes condições:

 lRural    :=    (M->A2\_TIPO $ "F") .AND. (M->A2\_INDRUR $ "1,2,3") .AND. (M->A2\_EST $ "SP|MG") 

**Obs.: Preencher na seguinte ordem:**

1 - Estado / A2\_EST = SP ou MG

2 - Tipo / A2\_TIPO = F

3 - Na Pasta "Outros" Ind. Prod. Rur / A2\_INDRUR = 1,2 ou 3

4 - CPF Rural / A2\_CPFRUR = Números do CPF

5 - Completar dados cadastrais, CNPJ ou CPF na pasta "Cadastrais"

No cadastro de Fornecedores os campos listados abaixo devem atender as seguintes opções:

1 - Estado = SP ou MG

2 - Tipo = Físico

3 - Ind. Prod. Rur. = 1,2 ou 3:

**Exemplo Preenchimento:**

![A2_CPFRUR.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360040859654/A2_CPFRUR.jpg)

**Exemplo parâmetro;**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001764722/mceclip0.png)
