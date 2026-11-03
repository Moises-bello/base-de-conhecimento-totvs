---
article_id: 14154698706839
category: TAF - REINF
content_hash: 0f1c2edc3c83816263fb2acd31e9a95d75648aa6cd4c7fe61274652a221ffbfc
fetched_at: '2026-06-28T22:41:33.739138+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Como integrar o evento
  R-4020  (Emissão) manualmente no TAF.
type: support-article
updated_at: '2023-10-11T14:36:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14154698706839-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-integrar-o-evento-R-4020-Emiss%C3%A3o-manualmente-no-TAF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18192725302935) Tempo aproximado para leitura: **00:04:00 min****Dúvida**Como gerar o evento R4020 manualmente no TAF.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais - a partir da versão 12  
  
**Solução:**

Para gerar  o evento **R4020** (Pagamentos/créditos a beneficiário pessoa jurídica)

na emissão acesse  a rotina **TAFA062** no caminho abaixo:

**Atualizações -> Movimentos REINF -> documento de entrada TAFA062 -> Incluir.**

O  imposto calculado na nota fiscal deve ser somente o  IR na emissão (ID TAF = 000012 - IR Emissão)

**IMPORTANTE:**

Os campos abaixo são obrigatórios para  levar a nota no  painel reinf.

Capa do documento:

**Dt Emissão (C20\_DTDOC)**: O mês/ano selecionado para apuração deve corresponder ao mês/ano da data de emissão do Documento Fiscal

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/14152799662103)

**Tp. Oper. (C20\_INDOPE)**: Para que o Documento Fiscal seja considerado, seu Tipo de Operação deverá corresponder a uma Aquisição (Entrada);

![tipo.png](https://centraldeatendimento.totvs.com/hc/article_attachments/14152881549719)

Produtos/Serviços

**Natureza de Rendimento (C30\_CNATRE)**: Para que o item do documento seja considerado, a Natureza de Rendimento deverá possuir conteúdo válido que corresponda a um código da tabela V3O - Naturezas de Rendimento.

![nat.png](https://centraldeatendimento.totvs.com/hc/article_attachments/14153063821207)

Tributos do Item

**C.Tributo (C35\_CODTRI):** Apenas documentos que possuam Tributos do Item cujo código de Tributo corresponda ao código 12-IR emissão

![ir.png](https://centraldeatendimento.totvs.com/hc/article_attachments/14153124073239)

Participantes

**Tipo Pessoa (C1H\_PPES ):** Para Beneficiários residentes no Brasil **(C1H\_CODPAI=000001)** Faturas/Documentos Fiscais/Pagamentos cujo Participante seja Pessoa Jurídica serão consideradas;

![TIPO_P.png](https://centraldeatendimento.totvs.com/hc/article_attachments/14153257113239)

**Tipo Pessoa EX  (C1H\_PEEXE ):** Para participantes residentes no exterior **(C1H\_CODPAI <> 000001),** também serão considerados os Participantes que estejam com a opção = "3 - Outros" no campo Tipo Pessoa. Neste cenário é necessário preencher o campo Tipo Pessoa Exterior **(C1H\_PEEXE)** como 1 - Pessoa Jurídica

![EX.png](https://centraldeatendimento.totvs.com/hc/article_attachments/14153335062167)

**CNPJ (C1H\_CNPJ):** Para beneficiários residentes no Brasil **(C1H\_CODPAI=000001)** apenas Faturas/Documentos Fiscais/Pagamentos cujo Participante possua CNPJ preenchido serão consideradas.

![TESTE.png](https://centraldeatendimento.totvs.com/hc/article_attachments/14153798046615)

**IMPORTANTE:** As notas para o  evento R4020  serão demonstradas  somente na rotina PAINEL REINF, quando  o parâmetro **MV\_TAFVLRE**  indicar o layout  **2\_01\_02**
