---
article_id: 360053374314
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: e8ea5c5dabcb780e5bbae3f39af551e652b052109628072d52f42f9dd820bec7
fetched_at: '2026-06-28T22:39:36.932614+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Dedução apenas do
  ICMS tributado da base de cálculo do PIS e COFINS
type: support-article
updated_at: '2021-09-14T02:58:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053374314-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Dedu%C3%A7%C3%A3o-apenas-do-ICMS-tributado-da-base-de-c%C3%A1lculo-do-PIS-e-COFINS
---

**Dúvida**  
Dedução do ICMS Tributado da Base de Cálculo do PIS e COFINS   
  
**Ambiente**  
Protheus – Financeiro – A partir da versão 12  
  
**Solução**

-Para **Notas Fiscais de Entrada**, será necessária a alteração do campo do **Cadastro de Fornecedores Ded. PIS/COF = (1 = Legado)** e o parâmetro **MV\_DICMISE** conter os **CST's de ICMS** que não devem ser deduzidos da **Base de Cálculo do PIS e COFINS**.

-Para**Notas Fiscais de Saída**, será necessário apenas o preenchimento do parâmetro **MV\_DICMISE**com os **CST's de ICMS** que não devem ser deduzidos da **Base de Cálculo do PIS e COFINS**.

**-Obs.:** Em ambos os casos, ainda se faz necessário respeitar a configuração para **dedução do ICMS da Base de Cálculo de PIS e COFINS** de acordo com a documentação a seguir:   
  
<https://tdn.totvs.com/pages/releaseview.action?pageId=272158405>

-Uma segunda alternativa para as **Notas Fiscais de Entrada**, é apenas configurar o campo do **Cadastro de Fornecedores Ded. PIS/COF = (3 = ICMS)** e o parâmetro **MV\_DICMISE** conter os **CST's de ICMS** que não devem ser deduzidos da **Base de Cálculo do PIS e COFINS**.

Obs.: Uma forma alternativa de ter acesso a essa implementação ao invés da execução do **compatibilizador UPDDISTR** com o **pacote diferencial (SDFBRA.txt)**, além da aplicação do **patch de atualização**, é necessária apenas a criação do parâmetro **MV\_DICMISE** via **configurador**:

| Campo | Preenchimento |
| --- | --- |
| Nome da Var. | MV\_DICMISE |
| Tipo | 1 - Caractere |
| Ex.: Cont. Por | 40|50|90 |
| Descrição | CST's de ICMS que não devem ser deduzidos da Base |
| Cont. Descrç | de Cálculo de PIS e COFINS. |

Abaixo links contendo atualizações liberadas na ISSUE: **DSERFIS1-17190**  
  
12.1.27:<https://r.totvs.io/p/955552> ; 12.1.25:<https://r.totvs.io/p/955551> ; 12.1.23:<https://r.totvs.io/p/955550> ; 12.1.17:<https://r.totvs.io/p/955549> ; 11.80:<https://r.totvs.io/p/955548> ;  
  
Os fontes acima são referente a data da implementação do cenário acima, caso esteja com o ambiente atualizado, poderá desconsiderar a aplicação do pacote.
