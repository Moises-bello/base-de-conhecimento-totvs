---
article_id: 14155918383383
category: TAF - REINF
content_hash: 79496a4d60f4f40aff6c7cc0a519b56cd032fc98fa425771531802766c3378aa
fetched_at: '2026-06-28T22:41:33.744775+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Como integrar o evento
  R-4020  (FATURA) manualmente no TAF.
type: support-article
updated_at: '2024-12-20T16:04:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14155918383383-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-integrar-o-evento-R-4020-FATURA-manualmente-no-TAF
---

Tempo aproximado para leitura: 00:03:00 min**Dúvida**Como gerar uma fatura manualmente no TAF para o evento R4020 ?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais - a partir da versão 12.  
  
**Solução:**

Para incluir a fatura acesse o caminho abaixo:

**Atualizações -> Movimentos REINF -> Fatura/ReciboTAFA448** **-> Incluir.**

O  imposto calculado na nota fiscal deve ser somente o  IR na emissão (ID TAF = 000012 - IR Emissão)

Todos os campo abaixo devem ser preenchidos:

**Capa da Fatura**

**Natureza (LEM\_NATTIT):** Apenas serão consideradas Faturas com Natureza = 0 - A Pagar

![nazt.png](https://centraldeatendimento.totvs.com/hc/article_attachments/14155820016151)

**Dt Emissão (LEM\_DTEMIS):** O mês/ano selecionado para apuração deve corresponder ao mês/ano da data de emissão da fatura.

![dtr.png](https://centraldeatendimento.totvs.com/hc/article_attachments/14155820792471)

Caso o IR seja pela Contabilização, deve ser preenchido o campo **DT Contábil(LEM\_DTCONT) em conjunto com a Configuração do parâmetro MV\_TAFDT40:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20435060107415)

**Natureza de Rendimento**

**Natureza de Rendimento (V3S\_IDNATR):** Para que o item do documento seja considerado, a Natureza de Rendimento deverá possuir conteúdo válido que corresponda a um código da tabela V3O - Naturezas de Rendimento.

![nat_ret.png](https://centraldeatendimento.totvs.com/hc/article_attachments/14155821958167)

**Tributos do Item**

**C.Tributo (V47\_CODTRI):** Apenas documentos que possuam Tributos do Item cujo código de Tributo corresponda ao código 12-IR emissão.

![dte.png](https://centraldeatendimento.totvs.com/hc/article_attachments/14155826188951)

**Participantes**

**Tipo Pessoa (C1H\_PPES ):** Para Beneficiários residentes no Brasil **(C1H\_CODPAI=000001)** Faturas/Documentos Fiscais/Pagamentos cujo Participante seja Pessoa Jurídica serão consideradas;

![TIPO_P.png](https://centraldeatendimento.totvs.com/hc/article_attachments/14155861883671)

**Tipo Pessoa EX  (C1H\_PEEXE ):** Para participantes residentes no exterior **(C1H\_CODPAI <> 000001),** também serão considerados os Participantes que estejam com a opção = "3 - Outros" no campo Tipo Pessoa. Neste cenário é necessário preencher o campo Tipo Pessoa Exterior **(C1H\_PEEXE)** como 1 - Pessoa Jurídica

![EX.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18192759448727)

**CNPJ (C1H\_CNPJ):** Para beneficiários residentes no Brasil **(C1H\_CODPAI=000001)** apenas Faturas/Documentos Fiscais/Pagamentos cujo Participante possua CNPJ preenchido serão consideradas.

![TESTE.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18192759458071)

**IMPORTANTE:** As faturas  para o  evento R4020  serão demonstradas  somente na rotina PAINEL REINF, quando  o parâmetro **MV\_TAFVLRE**  indicar o layout  **2\_01\_02**
