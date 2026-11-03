---
article_id: 360026219274
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 2bdfd89b12ea78dcd1100436d287a5cb0612d40e4eef395a707ab0e11b476a34
fetched_at: '2026-06-28T22:39:30.682438+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Como Habilitar Utilização
  do Campo A2_CPFRUR
type: support-article
updated_at: '2021-10-04T19:51:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026219274-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-Habilitar-Utiliza%C3%A7%C3%A3o-do-Campo-A2-CPFRUR
---

**Dúvida**

Como habilitar utilização do campo A2\_CPFRUR no cadastro de Fornecedores dos estados de SP e MG?

**Ambiente**

Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Para habilitar preenchimento do campo "A2\_CPFRUR" precisa atender as seguintes condições:

 lRural    :=    (M->A2\_TIPO $ "F") .AND. (M->A2\_INDRUR $ "1,2,3") .AND. (M->A2\_EST $ "SP|MG") 

**Obs.: Preencher na seguinte ordem:**

1 - Estado / A2\_EST = SP ou MG

2 - Tipo / A2\_TIPO = F

3 - Na Pasta "Outros" Ind. Prod. Rur / A2\_INDRUR = 1,2 ou 3

4 - CPF Rural / A2\_CPFRUR = Números do CPF

5 - Completar dados cadastrais, CNPJ ou CPF na pasta "Cadastrais"

Ao informar o CPF Rural para um Fornecedor que tenha CNPJ, a máscara do campo CNPJ/CPF (A2\_CGC) irá se manter para que seja possível informar o CNPJ.

No cadastro de Fornecedores os campos listados abaixo devem atender as seguintes opções:

1 - Estado = SP ou MG

2 - Tipo = Físico

3 - Ind. Prod. Rur. = 1,2 ou 3:

**Exemplo:**

![A2_CPFRUR.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360040859654/A2_CPFRUR.jpg)
