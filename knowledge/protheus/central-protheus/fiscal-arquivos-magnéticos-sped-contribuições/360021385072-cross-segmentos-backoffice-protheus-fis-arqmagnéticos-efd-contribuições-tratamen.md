---
article_id: 360021385072
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: e13063b9aed5fed01775663358d1659b07ed352dd8e4ced414dd581a51a621c8
fetched_at: '2026-06-28T22:42:05.325737+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - Tratamento Referente as Notas Fiscais Canceladas na Apuração da EFD Contribuições
type: support-article
updated_at: '2025-04-01T18:27:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021385072-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Tratamento-Referente-as-Notas-Fiscais-Canceladas-na-Apura%C3%A7%C3%A3o-da-EFD-Contribui%C3%A7%C3%B5es
---

**Dúvida**O sistema está considerando as notas fiscais canceladas na apuração da EFD Contribuições.  
  
**Ambiente**Microsiga Protheus – Livros Fiscais – A partir da versão 11.80.  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Verifique a data de cancelamento na nota fiscal (cancelamento no mesmo período de emissão da nota fiscal).  
  
Se a nota fiscal foi cancelada no mesmo período da data de emissão, a nota fiscal não será considerada na apuração. Se o sistema estiver considerando esta nota da apuração da EFD Contribuições, verifique o preenchimento dos campo abaixo:

a) Tabela SF3:  
**F3\_DTCANC** = Data de Cancelamento da nota (esta preenchida exemplo 04/01/2019)  
**F3\_OBSERV** = NF CANCELADA  
**F3\_CODRSEF** = 101 (101 = Cancelamento de NF-e )  
**F3\_CHVNFE** = Chave NF-e.  
  
b) Tabela SFT:  
**FT\_OBSERV** = NF CANCELADA  
**FT\_DTCANC** = Data de Cancelamento da nota (esta preenchida exemplo 04/01/2019)  
**FT\_CHVNFE** = Chave NF-e.  
  
Se as informações das notas fiscais que estão sendo consideradas no arquivo magnético do SPED estiverem com as informações diferentes do orientado acima, será necessário entrar em contato com Suporte da NF-e (SPED/TSS).

2. Verifique a data de cancelamento na nota fiscal (cancelamento em período posterior ao de emissão da nota fiscal).  
Se a nota fiscal foi cancelada em período **POSTERIOR** ao de emissão, então, o sistema realizará um ajuste no bloco M conforme orientado no Guia Prático do Sped Contribuições.  
  
Para os cancelamentos efetuados em período posterior ao da emissão do documento, então deverá ser realizado um estorno da contribuição, através de um ajuste de redução da contribuição. No parâmetro **MV\_SPDAJCA**definimos a quantidade de meses anteriores que a rotina irá considerar para poder efetuar o estorno da contribuição.

**Segue trecho do Guia Prático:**  
"Se o cancelamento se deu em período posterior ao de sua emissão, devendo assim ser considerado na redução da base de cálculo do período em que ocorreu o cancelamento, a empresa pode proceder á escrituração destes valores redutores da base de cálculo do mês do cancelamento, mediante a geração de registros de ajustes de débitos, em M220 (PIS) e M620 (Cofins), fazendo constar nestes registros de ajustes o montante da contribuição a ser reduzida, em decorrência do(s) cancelamentos em questão."

Abaixo um link referente parecer elaborado pela nossa consultoria de segmentos referente Cancelamento de NFS-e/Nota de Serviço em período subsequente:  
  
<https://tdn.totvs.com/pages/releaseview.action?pageId=269447768>
