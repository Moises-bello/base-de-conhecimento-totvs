---
article_id: 360019123951
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: 4d73b87fca611a988f98c389956d0abdbeac61a749b682e28c3b38c1a0dd67cf
fetched_at: '2026-06-28T22:39:36.812753+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS -  Cálculo CPRB (Contribuição
  Previdenciária Sobre a Receita Bruta)
type: support-article
updated_at: '2023-12-26T13:32:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019123951-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-C%C3%A1lculo-CPRB-Contribui%C3%A7%C3%A3o-Previdenci%C3%A1ria-Sobre-a-Receita-Bruta
---

**Dúvida**Como realizar cálculo CPRB (Contribuição Previdenciária sobre a Receita Bruta)?  
  
**Ambiente**Protheus - Livros Fiscais - A partir da versão 11.80  
  
  
**Solução**Para realizar calculo de **CPRB,** realize os seguintes passos:

Configure o parâmetro MV\_CPRBNF = **.T.**

 Configure a TES, campo Calc. CPRB (F4\_CALCCPB) = **Sim**

 Acesse o complemento do produto (tabela SB5) (MATA180)

Caminho: Faturamento> Atualizações> Cadastros> Complemento de Produto> Aba Outros

Verif Ind (B5\_VERIND)= **2**-**Não**    
INSS Patron (B5\_INSPAT)= **1-Sim**  
Cod. Ativ. (B5\_CODATIV) = Informe o seu código de atividade – (Código de atividade tabela CG1)

O cadastro deste código deve conter a data inicial preenchida e **data final não deve ser informada**.

![Screenshot_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014821732)

Após configuração, no momento do lançamento da nota fiscal de saída, em planilha financeira será demonstrado o calcular a CPRB no momento da digitação do Documento Fiscal.

![Screenshot_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014856651)

<https://tdn.totvs.com/display/public/PROT/EFDCON+-+CPRB+via+Documentos+Fiscais>
