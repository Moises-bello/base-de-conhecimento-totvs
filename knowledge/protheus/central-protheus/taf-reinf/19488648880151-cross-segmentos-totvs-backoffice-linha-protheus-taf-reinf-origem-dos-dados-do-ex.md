---
article_id: 19488648880151
category: TAF - REINF
content_hash: 77cba495ac462fef7b0f85998e40fe9ccd78e22acfaf614070578dbee69beacb
fetched_at: '2026-06-28T22:41:34.923031+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - TAF - REINF - Origem dos
  Dados do Extrator Fiscal até o Painel Reinf
type: support-article
updated_at: '2023-12-01T18:44:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19488648880151-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-TAF-REINF-Origem-dos-Dados-do-Extrator-Fiscal-at%C3%A9-o-Painel-Reinf
---

**![time.png](https://totvssuporte.zendesk.com/guide-media/01GVK0XPESEK73YY0FKEGBFP3Z) Tempo aproximado para leitura: 00:05:00min**

**Dúvida**Origem dos dados para geração dos eventos do bloco 40, do extrator fiscal até o painel reinf.  
  
**Ambiente**

Cross Segmentos - TOTVS Backoffice Linha Protheus - TOTVS Automação Fiscal- Todas as versões  
  
**Solução**

Origem dos dados do **Extrator Fiscal** até a rotina do **Painel Reinf**:

Registro **T013** >> **TAFA062E**(Docs de Entrada) >> **NFS** (Painel Reinf)

Registro **T154** >> **TAFA448**(Fatura/Recibo) >> **FAT** (Painel Reinf)

Registro **T158** >> **TAFA535**(Pagamentos) >> **PGT**(Painel Reinf)

Impostos: IR (Emissão, contabilização ou pagamento) e PCC (Pagamento).

**IR - Emissão (T013 e/ou T154):**

O IR na emissão será integrado ao TAF por meio do código 12 de tributo, que será destacado na nota fiscal (NFS) e no título (FAT).

Se a nota fiscal e o título vinculado a nota fiscal for integrado ao TAF, o painel reinf irá buscar o valor do IR do **título**.

Se a nota fiscal não gerar livro fiscal, não será gerado os dados da nota pelo extrator, somente do título, o painel reinf irá buscar o valor do IR do **título**.

Se a nota fiscal for integrada e não houver titulo ou não ter sido integrado o titulo, o painel reinf irá buscar o valor do IR da **nota fiscal.**

**IR - Contabilização (T013 e/ou T154)**

As regras para o IR na contabilização são as mesmas do IR emissão, o código também é o 12 e a precedência dos dados no painel reinf também.

Entretanto, para que o IR seja apurado pela contabilização, é necessário a configuração do parâmetro **MV\_TAFDT40=1** em conjunto com os campos LEM\_DTCONT e/ou C20\_DTCONT preenchidos. Mais informações: Cross Segmentos - Backoffice Protheus -TAF - REINF - Como considerar o IR na data de contabilização na apuração do Reinf?

**IR - Pagamento (T158):**

Para o IR ser gerado no pagamento, o código a ser considerado é o 28 de tributo. Esse código vem exclusivamente pelo registro T158 do extrator fiscal, onde trata-se de baixa do título principal no financeiro.

O painel reinf só irá levar o valor do IR no pagamento de registros do tipo PGT.

**Pis e Cofins - Pagamento(T158)**

O pis e Cofins pode ser gerado com diferentes códigos de tributo, de acordo com a escrituração efetuada:

PCC nas colunas próprias: Códigos de tributo 10 - Pis, 11 - Cofins e 18 - CSLL

PCC de forma agregada: Códigos de tributo 29 - CSRF ou 30 - COSIRF

O PCC sempre será gerado no pagamento, ou seja, na baixa do título principal.

Detalhamento dos valores no painel reinf:

No caso do evento R-4020, quando o **IR for na emissão**, será exibido as notas fiscais (NFS) ou faturas (FAT) com o tributo 12-IR Emissão:

![](https://tdn.totvs.com.br/download/attachments/344474121/image2023-8-24_10-19-40.png?version=1&modificationDate=1692883180893&api=v2)

Quando o IR for na baixa, será exibido a entidade **pagamento** (PGT) que tiver o tributo 28-IR no pagamento:

![](https://tdn.totvs.com.br/download/attachments/344474121/image2023-8-24_10-18-44.png?version=1&modificationDate=1692883124907&api=v2)

Quando possuir o imposto **IR na Emissão** (NFS ou FAT) e o PIS, COFINS, CSLL, CSRF ou COSIRF no **pagamento**, sendo o mesmo número de documento por participante, mesmo que sejam de entidades diferentes, será contabilizado como 1 documento. O valor bruto será considerado apenas uma vez.

![](https://tdn.totvs.com.br/download/attachments/344474121/image2023-9-16_12-31-5.png?version=1&modificationDate=1694878265930&api=v2)

![](https://tdn.totvs.com.br/download/attachments/344474121/image2023-9-16_12-35-44.png?version=1&modificationDate=1694878544663&api=v2)

Mesmo que as datas do fato gerador sejam diferentes, mas por ser o mesmo número de documento da fatura e pagamento, será contabilizado como 1 documento:

![](https://tdn.totvs.com.br/download/attachments/344474121/image2023-9-16_12-40-11.png?version=1&modificationDate=1694878811803&api=v2)

**Atenção**: Quando um movimento possuir mais de uma natureza de rendimento cadastrada, será considerado apenas como 1 documento, porém a exibição é detalhada por natureza de rendimento:

![](https://tdn.totvs.com.br/download/attachments/344474121/image2023-8-24_10-34-1.png?version=1&modificationDate=1692884041927&api=v2)

Para mais informações: https://tdn.totvs.com.br/display/public/TAF/EFD-Reinf
