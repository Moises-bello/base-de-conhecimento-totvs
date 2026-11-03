---
article_id: 40440616532119
category: Ativo Fixo - EFD Contribuições - Registros F120/F130
content_hash: e181cb0a4da1a5fefb07c72af8b25a22ffad4d6ab0fb41d2745f5671b2ea020c
fetched_at: '2026-06-28T22:41:36.234362+00:00'
product: protheus
section_id: 31045161075991
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAATF - Preenchimento
  do campo CL2_VLEXCL nos registros F120 e F130 sem gerar duplicidade.
type: support-article
updated_at: '2026-05-15T18:32:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40440616532119-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAATF-Preenchimento-do-campo-CL2-VLEXCL-nos-registros-F120-e-F130-sem-gerar-duplicidade
---

O campo CL2\_VLEXCL armazena o valor de exclusão do ICMS e IPI na base de cálculo de PIS/COFINS para ativos adquiridos a partir de 01/05/2023. O cálculo automático depende do vínculo do bem com a nota fiscal de entrada, configuração correta dos campos Cred. ICMS e Credita IPI como "N" na TES, e parâmetros específicos (MV\_ATFEIPI, MV\_BSCREPC, MV\_AGVLATF). Para evitar duplicidade, deve-se seguir os passos indicados e, se necessário, usar pontos de entrada AF120EXC ou AF130EXC para customização.

**Dúvida**  
Como é realizado o preenchimento do campo Vl. Exclu.  CL2\_VLEXCL para os registros F120 e F130 do EFD Contribuições e quais são os requisitos para o cálculo automático, e que não ocorra duplicidade?

**Ambiente**   
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAATF - Versão a partir da 12.1.2410

**Solução**   
O campo Vl. Exclu. (CL2\_VLEXCL) é utilizado para armazenar o valor de exclusão do ICMS e IPI da base de cálculo de PIS/COFINS sobre os ativos (registros F120 e F130), o valor incide em ativos adquiridos a partir de 01/05/2023 campo Dt.Aquisicao (N1\_AQUISIC).

O sistema utiliza os dados da Nota Fiscal de Entrada (SD1) e da TES (SF4) para compor o valor. Para que o cálculo ocorra, é recomendável que o bem esteja vinculado ao documento de entrada. Caso não haja vínculo, o sistema não calculará o valor automaticamente, sendo necessário o uso de Pontos de Entrada ou o reprocessamento da entrada do bem via Compras (MATA103).

Não podem ser usados os campos Cred. ICMS (F4\_CREDICM) e Credita IPI (F4\_CREDIPI) como N, caso ele já tenha deduzido o ICMS da aquisição. Se estiver como S, ele demonstra que já foi deduzido, se estiver como N, irá deduzir, e caso tenha retirado da entrada, ele ficará duplicado.

**Passos para gerar o valor corretamente e não ficar duplicado:**

1. No Cadastro de TES (MATA080), valide se os campos Cred. ICMS (F4\_CREDICM) e Credita IPI (F4\_CREDIPI) estão configurados como N (Não), pois, se houver crédito na nota, o valor de exclusão não será gerado.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40440569511959)
2. Para incluir o IPI no cálculo da exclusão, configure o parâmetro MV\_ATFEIPI como .T. (Verdadeiro). Caso contrário, apenas o ICMS será considerado.
3. Verifique o campo Desmem. IT. ATF. (F4\_BENSATF) na TES:

* Se igual a 1 (Sim): O ativo foi desmembrado. O sistema utilizará a fórmula proporcional: CL2\_VLEXCL = (D1\_VALICM + D1\_VALIPI) / D1\_QUANT \* N4\_TXDEPR (para F120).
* Se igual a 2 (Não): Será gerado apenas um ativo, utilizando o valor total do imposto na fórmula.

6. Para o registro F130, valide se o parâmetro MV\_BSCREPC está igual a 2 e o campo Base PIS/COF (N1\_CBCPIS) igual a 1 (Normal).
7. Caso o parâmetro MV\_AGVLATF esteja como .F., o sistema entenderá que o valor de aquisição já é líquido (via Base Imp. 6 - D1\_BASIMP6 e Base Imp. 5 - D1\_BASIMP5), dispensando o preenchimento do Vl. Exclu. (CL2\_VLEXCL).
8. Se houver necessidade de customização dos valores calculados, utilize os pontos de entrada AF120EXC (para registro F120) ou AF130EXC (para registro F130).  
   [AF120EXC - Exclusão do valor na base de cálculo do SPED PIS/COFINS no registro F120](https://tdn.totvs.com/pages/releaseview.action?pageId=152802056)

**Saiba Mais**  
[Documentação de Referência - Campo CL2\_VLEXCL](https://tdn.totvs.com/pages/releaseview.action?pageId=859054135)  
[EFD Contribuições - F120 e F130 - Ativo Fixo](https://tdn.totvs.com/pages/viewpage.action?pageId=859054070)  
[EFD CONTRIBUIÇÕES - F120 - MP 1159/2023 - Exclusão de ICMS da base de calc. do PIS/COFINS quando ICMS não é creditado](https://tdn.totvs.com/pages/viewpage.action?pageId=841694477)  
[Exclusão do ICMS da Base de Cálculo do PIS e da COFINS](https://tdn.totvs.com/pages/viewpage.action?pageId=790637042)  
[Lei 14.592 / 2023](https://www.planalto.gov.br/CCIVIL_03/////_Ato2023-2026/2023/Lei/L14592.htm)  
[Frete - Base de cálculo IPI](https://tdn.totvs.com/pages/viewpage.action?pageId=823819152)  
[Exclusão do IPI da Base de Cálculo de PIS/COFINS - DEPRECIAÇÃO](https://tdn.totvs.com/pages/viewpage.action?pageId=821187917)
