---
article_id: 7630668843287
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: 0d1703e543c26a64c65eabf5c420f79673e77c31a124277bf29fae74ec88e43f
fetched_at: '2026-06-28T22:39:36.785068+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Como gerar os Registros M100,
  M105, M500 e M505 do EFD Contribuições.
type: support-article
updated_at: '2022-10-03T14:57:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7630668843287-Cross-Segmentos-Backoffice-Protheus-FIS-Como-gerar-os-Registros-M100-M105-M500-e-M505-do-EFD-Contribui%C3%A7%C3%B5es
---

**Dúvida**Como gerar os Registros M100, M105, M500 e M505 do EFD Contribuições?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões.  
  
**Solução**A geração do **Bloco M** é baseada nas informações já processadas e gravadas pela rotina de **Apuração da EFD Contribuições (FISA001)**, então **antes de gerar o arquivo texto**, é necessário **processar antes apuração**.

**Registro M100: Crédito de PIS/Pasep Relativo ao Período**  
**Registro M105: Detalhamento da Base de Calculo do Crédito Apurado no Período – PISPasep**  
**Registro M500: Crédito de Cofins Relativo Ao Período**  
**Registro M505: Detalhamento da Base de Calculo do Crédito Apurado no Período – Cofins**Importante:   
Após finalização do **processamento apuração**, para que os valores possam ser coerentes com as movimentações nos demais blocos, não poderá mais emitir nota, título, baixas, ajustes etc, caso seja necessário incluir alguma informação após finalização da apuração, será necessário fazer **reprocessamento da apuração**, e **depois gerar o arquivo**, para não ter diferenças de valores entre o bloco da apuração e os demais blocos.  
  
Os **Registros M100 e M500** tem objetivo de informar a **consolidação do crédito de PIS e do crédito de COFINS**, respectivamente, apurada no período.  
São gerados para os seguintes **CST: 50, 51, 52, 53, 54, 55, 56, 60, 61, 62, 63, 64 e 66**.   
As informações deste registro tem origem da **Tabela CL8**.

**Os Registros M105 e M505** tem **objetivo de detalhar a Base de Cálculo do Crédito Apurado no Período para PIS e COFINS**, respectivamente.Nestes registros são **detalhados a base de cálculo de cada tipo de crédito informado nos registros M100 e M500**, com base nas **operações com Código da Base de Cálculo do crédito** e **CST geradores de créditos nos documentos escriturados nos blocos A, C, D e F**.   
As informações deste registro tem origem da **Tabela CL9**.  
  
**Importante:**As **tabelas CL8 - Crédito PIS/COF Consolidado** e **CL9 - Crédito PIS/COF Detalhado** apenas serão gravadas **quando o período possuir crédito**. Caso contrário, estas tabelas não serão gravadas e, consequentemente, os registros referentes à apuração não serão gerados já que não possui crédito no período.   
Além disso, a não geração destes registros não ocasiona nenhum tipo de erro na validação ou na entrega do arquivo gerado. 

Os controles de créditos de PIS disponíveis para os próximos períodos são gravados na tabela **Controle de Crédito de PIS** **(CCY)**, e os créditos de COFINS gravados na tabela **Controle de Crédito de COFINS** **(CCW).**Geralmente, ao validar no **PVA** o **arquivo txt** do **EFD Contribuições** os erros do **Bloco M,** ocorrem porque o mesmo não encontra as informações corretas de **CST** e o **vínculo de crédito** ou quando **não condiz com o CST esperado** pelo validador.  
- Primeiramente é importante compreender que o **Bloco M busca as informações dos demais Blocos (A, C, D e F)**, então avalie o **Relatório de Conferência EFD (FISR101)** referente as Notas Fiscais do período, avalie as amarrações dos **campos dos códigos de credito do campo FT\_CODBCC** e a **CFOP** utilizada.O código é gravado no **campo FT\_CODBCC** esse campo é alimentado pela **TES** campo **F4\_CODBCC**. Se o código informado não for o correto para **CFOP** correta a ser utilizada a composição dos valores dos **registros M105 e M505** será gerado de forma incorreta.  
  
**Deve ser gerado um registro M100 (crédito PIS) e um registro M500 (crédito COFINS) especifico para cada tipo de crédito apurado (vinculados à receita tributada, vinculados à receita não tributada e vinculados à exportação), conforme a Tabela de tipos de créditos “Tabela 4.3.6”, bem como para créditos de operações próprias e créditos transferidos por eventos de sucessão.**  
Link: <http://sped.rfb.gov.br/arquivo/show/1632>

O **Campo 02 - COD\_CRED** dos **Registros M100 e M500** será gerado conforme a **Tabela 4.3.6.** da **Receita Federal**, tratado as operações dos **grupos 100**, **grupo 200** e **grupo 300.**

1. - O **CST 50** é exclusiva do **grupo 100**, **CST 51** é **excluída do grupo 200** e **CST 52** exclusiva do **grupo 300.**  
   - O **CST 53 a 56** pertencem aos **grupos 100, 200, 300**.  
     
   **GRUPO 100** – Crédito vinculado a Receita tributada no mercado interno.   
   Utiliza os **CSTs: 50|60|53|63|54|64|56|66**  
            
   **GRUPO 200** – Crédito vinculado a Receita não Tributada no mercado interno.   
   Utiliza os **CSTs: 51|61|53|63|55|65|56|66**  
     
   **GRUPO 300** – Crédito vinculado a receita de Exportação.   
   Utiliza os **CSTs: 52|62|54|64|55|65|56|66**  
     
     
   **Identificação do grupo**:   
   Verifica o código **CST** usado no **registro filho M105**, se for igual a **50, 53, 54 e 56**, é considerado o **grupo 100** da **tabela 4.3.6**, se for igual a **51, 53, 55 e 56**, será **grupo 200** da **tabela 4.3.6**, e se for igual a **52, 54, 55 e 56,** será **grupo 300** da **tabela 4.3.6.**  
   **Identificação do código do grupo**:   
   Se a nota tiver informações referentes **à pauta de PIS**, então é considerado **código 103, 203 ou 303** dependendo do grupo. Se a nota for de **importação**, será **código 108, 208 ou 308**, dependendo do grupo. Quando se tratar de **alíquotas básicas**, será o **código 101, 201 ou 301**, dependendo do grupo, e se tratar de **alíquotas diferenciadas**, será o **código 102, 202 ou 302,** dependendo do grupo.  
   **Tratamento específico para os códigos 106, 206 ou 306:**Para que seja considerado um destes códigos referente as **créditos presumido – Agroindustria** será necessário que o **campo FT\_TNATREC** esteja preenchido com o **código da Receita 4.3.9**, caso o contrário serão considerados os **códigos 107, 207 ou 307**.
