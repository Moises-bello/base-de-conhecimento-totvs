---
content_hash: 647ae43e1c47dab647abf9b9f7525ddadbfd0b44895fa30d214961eddc63c1c4
fetched_at: '2026-06-29T00:05:48.548645+00:00'
page_id: '1025223880'
product: rm
source: tdn-rm
title: Grupo detalhado para IBS e CBS
type: documentation
url: https://tdn.totvs.com/display/LRM/Grupo+detalhado+para+IBS+e+CBS
version: 30
---

### Voltar para [Layout único de integração da NFS-e com o TSS](https://tdn.totvs.com/pages/viewpage.action?pageId=560652116)

| Nome | Pai | Obrigatório | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- |
| **impostoibscbs** | **[rps](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143227)** | **Não** | **Tag raiz dos impostos IBS CBS** | **--** | **Grupo gerado apenas quando há IBS/CBS no item do movimento, cujas bases de cálculo sejam maiores que zero.** |
| codigo | impostoibscbs | Não | Código do imposto |  | Será preenchido com o valor fixo "IBSCBS" |
| finnfse | impostoibscbs | Não | Indicador da finalidade da emissão de NFS-e: 0 - NFS-e regular; |  |  |
| indfinal | impostoibscbs | Não | Indica operação de uso ou consumo pessoal (art. 57): 0 - Não; 1 - Sim | TMOVFISCAL.OPERACAOCONSUMIDORFINAL | Aba Fiscal do movimento, campo "Consumidor final" |
| cindop | impostoibscbs | Não | Código indicador da operação de fornecimento, conforme tabela "código indicador de operação" | TITMMOVFISCAL.CODINDOP | Aba Fiscal do item do movimento, campo "Código Indicador da Operação" |
| tpoper | impostoibscbs | Não | Tipo de Operação com Entes Governamentais ou outros serviços sobre bens imóveis: 1 – Fornecimento com pagamento posterior; 2 - Recebimento do pagamento com fornecimento já realizado;  3 – Fornecimento com pagamento já realizado;  4 – Recebimento do pagamento com fornecimento posterior;  5 – Fornecimento e recebimento do pagamento concomitantes | TMOVFISCAL.TPOPER | aba **“Integrações ” →****“Fiscal 2” (Versões até 2602)**    **aba “Integrações ” → “Fiscal” → "Documentos Fiscais Eletrônicos" (Versões 2606 ou superior)**  As informações são geradas somente se o campo estiver diferente de 0 - Não se Aplica. |
| tpentegov | impostoibscbs | Não | Tipo de ente governamental Para administração pública direta e suas autarquias e fundações:  1 - União;  2 - Estado;  3 - Distrito Federal;  4 - Município; | FCFO.ORGAOPUBLICO | Código identifica se o cliente/fornecedor é do tipo Ente Governamental.  Para ser considerado um Ente Governamental a campo Órgão Público deve esta selecionado com uma das opção.   * Federal. * Estadual * Municipal * Distrito Federal   Caso a seleção escolhida seja a "não se aplica" a tag não será evidenciada no xml |
| inddoacao | impostoibscbs | Não | Indica uma Operação de Doação | **Não será gerado no momento** |  |
| inddest | impostoibscbs | Não | A respeito do Destinatário dos serviços:  0 – o destinatário é o próprio tomador/adquirente identificado na NFS-e (tomador = adquirente = destinatário);  1 – o destinatário não é o próprio adquirente, podendo ser outra pessoa, física ou jurídica (ou equiparada), ou um estabelecimento diferente do indicado como tomador (tomador = adquirente ≠ destinatário) |  | É feita a comparação entre os dados do Tomador e o Destinatário (aba **“Dest. Serviço”**).  Se forem os mesmo, o campo é gerado com "0". Caso contrário, é gerado com "1" |
| **Tributo** | **impostoibscbs** | **Não** | **Tag raiz dos tributos dos impostos IBS CBS** |  |  |
| CST | Tributo | Não | Código de Situação Tributária do IBS e CBS | TTRBMOV.SITTRIBUTARIA | Código de situação tributária do tributo IBS/CBS do item de movimento. Caso tenhamos os tributos IBS e CBS e/ou tenhamos mais de um item na nota então será adotado o código do primeiro item/tributo IBS/CBS encontrado. |
| cClassTrib | Tributo | Não | Código de Classificação Tributária do IBS e CBS | TTRBMOV.CLASSTRIB | Código de classificação tributária do tributo IBS/CBS do item de movimento. Caso tenhamos os tributos IBS e CBS e/ou tenhamos mais de um item na nota então será adotado o código do primeiro item/tributo IBS/CBS encontrado. |
| pRedutor | Tributo | Não | Percentual redutor | TTRBMOV.PCTREDUTORGOV | O Percentual redutor e exclusivamente para ente governamental. Somente tem visibilidade quando o Tipo Operação for "Recebimento do pagamento com fornecimento já realizado / Fornecimento com pagamento já realizado" |
| **gIBSCBS** | **Tributo** | **Não** | **Tag raiz do grupo IBS CBS** |  |  |
| vBC | gIBSCBS | Não | Base de cálculo do IBS e CBS | TTRBMOV.BASEDECALCULO |  |
| **gIBSUF** | **gIBSCBS** | **Não** | **Tag raiz do grupo IBSUF** |  | Caso o parâmetro de agrupar itens da NFS-e esteja marcado no anexo no município e a nota possua mais de um item, os valores de todo tributo deste tipo nos itens serão somados |
| pIBSUF | gIBSUF | Não | Alíquota do IBS de competência das UF (em percentual) | TTRBMOV.ALIQUOTA |  |
| vIBSUF | gIBSUF | Sim | Valor do IBS Estadual | TTRBMOV.VALOR |  |
| **gDif** | **gIBSUF** | **Não** | **Grupo de Informações do Diferimento** |  | O grupo de Diferimento somente será gerado quando o **CST** informado possuir o indicador **IndDif = true** na tabela de CST **e** quando o **percentual de diferimento** for **maior que zero**. |
| pDif | gDif | Não | Percentual do diferimento | TTRBMOV.PCTDIFERIMENTO |  |
| vDif | gDif | Não | Valor do Diferimento | TTRBMOV.TRIBUTODIFERIDO |  |
| **gDevTrib** | **gIBSUF** | **Não** | **Grupo de Informações da devolução de tributos** |  |  |
| vDevTrib | gDevTrib | Não | Valor do tributo devolvido | **Não será gerado no momento** |  |
| **gRed** | **gIBSUF** | **Não** | **Grupo de informações da redução da alíquota** |  |  |
| pRedAliq | gRed | Não | Percentual da redução de alíquota do cClassTrib | TTRBMOV.PCTREDUCAOALIQUOTA |  |
| pAliqEfet | gRed | Não | Alíquota Efetiva do IBS de competência das UF que será aplicada a Base de Cálculo (em percentual) | TTRBMOV.ALIQUOTA |  |
| **gIBSMun** | **gIBSCBS** | **Não** | **Grupo de Informações do IBS para o município** |  | Caso o parâmetro de agrupar itens da NFS-e esteja marcado no anexo no município e a nota possua mais de um item, os valores de todo tributo deste tipo nos itens serão somados |
| pIBSMun | gIBSMun | Não | Alíquota do IBS de competência do Município (em percentual) | TTRBMOV.ALIQUOTA |  |
| vIBSMun | gIBSMun | Sim | Valor do IBS Municipal | TTRBMOV.VALOR |  |
| **gDif** | **gIBSMun** | **Não** | **Grupo de Informações do Diferimento** |  | O grupo de Diferimento somente será gerado quando o **CST** informado possuir o indicador **IndDif = true** na tabela de CST **e** quando o **percentual de diferimento** for **maior que zero**. |
| pDif | gDif | Não | Percentual do diferimento | TTRBMOV.PCTDIFERIMENTO |  |
| vDif | gDif | Não | Valor do Diferimento | TTRBMOV.TRIBUTODIFERIDO |  |
| **gDevTrib** | **gIBSMun** | **Não** | **Grupo de Informações da devolução de tributos** |  |  |
| vDevTrib | gDevTrib | Não | Valor do tributo devolvido | **Não será gerado no momento** |  |
| **gRed** | **gIBSMun** | **Não** | **Grupo de informações da redução da alíquota** |  |  |
| pRedAliq | gRed | Não | Percentual da redução de alíquota do cClassTrib | TTRBMOV.PCTREDUCAOALIQUOTA |  |
| pAliqEfet | gRed | Não | Alíquota Efetiva do IBS de competência do Município que será aplicada a Base de Cálculo (em percentual) | TTRBMOV.ALIQUOTA |  |
| vIBS | gIBSCBS | Não | Valor (total) do IBS | -- | Soma dos campos vIBSUF e vIBSMun |
| **gCBS** | **gIBSCBS** | **Não** | **Grupo de Informações da CBS** | -- | Caso o parâmetro de agrupar itens da NFS-e esteja marcado no anexo no município e a nota possua mais de um item, os valores de todo tributo deste tipo nos itens serão somados |
| pCBS | gCBS | Não | Alíquota da CBS (em percentual) | TTRBMOV.ALIQUOTA |  |
| vCBS | gCBS | Não | Valor da CBS | TTRBMOV.VALOR |  |
| **gDif** | **gCBS** | **Não** | **Grupo de Informações do Diferimento** |  | O grupo de Diferimento somente será gerado quando o **CST** informado possuir o indicador **IndDif = true** na tabela de CST **e** quando o **percentual de diferimento** for **maior que zero**. |
| pDif | gDif | Não | Percentual do diferimento | TTRBMOV.PCTDIFERIMENTO |  |
| vDif | gDif | Não | Valor do Diferimento | TTRBMOV.TRIBUTODIFERIDO |  |
| **gDevTrib** | **gCBS** | **Não** | **Grupo de Informações da devolução de tributos** |  |  |
| vDevTrib | gDevTrib | Não | Valor do tributo devolvido | **Não será gerado no momento** |  |
| **gRed** | **gCBS** | **Não** | **Grupo de informações da redução da alíquota** |  |  |
| pRedAliq | gRed | Não | Percentual da redução de alíquota do cClassTrib | TTRBMOV.PCTREDUCAOALIQUOTA |  |
| pAliqEfet | gRed | Não | Alíquota Efetiva da CBS que será aplicada a Base de Cálculo (em percentual) | TTRBMOV.ALIQUOTA |  |
| **gTribRegular** | **gIBSCBS** | **Não** | **Grupo de informações da Tributação Regular** |  | Este grupo será gerado se houver uma Regra Tributária Regular associada à Regra Tributária informada no Item do Movimento. |
| CSTReg | gTribRegular | Não | Código de Situação Tributária do IBS e CBS | DREGRATRIBUTARIA.SITUACAOTRIBUTARIA |  |
| cClassTribReg | gTribRegular | Não | Código de Classificação Tributária do IBS e CBS | DREGRATRIBUTARIA.CLASSTRIB |  |
| pAliqEfetRegIBSUF | gTribRegular | Não | Valor da alíquota do IBS da UF (em percentual) | TTRBMOV.ALIQUOTACHEIA |  |
| vTribRegIBSUF | gTribRegular | Não | Valor do Tributo do IBS da UF | TTRBMOV.BASEDECALCULO \*  TTRBMOV.ALIQUOTACHEIA |  |
| pAliqEfetRegIBSMun | gTribRegular | Não | Valor da alíquota do IBS do Município (em percentual) | TTRBMOV.ALIQUOTACHEIA |  |
| vTribRegIBSMun | gTribRegular | Não | Valor do Tributo do IBS do Município | TTRBMOV.BASEDECALCULO \*  TTRBMOV.ALIQUOTACHEIA |  |
| pAliqEfetRegCBS | gTribRegular | Não | Valor da alíquota da CBS (em percentual) | TTRBMOV.ALIQUOTACHEIA |  |
| vTribRegCBS | gTribRegular | Não | Valor do Tributo da CBS | TTRBMOV.BASEDECALCULO \*  TTRBMOV.ALIQUOTACHEIA |  |
| **gIBSCredPres** | **gIBSCBS** | **Não** | **Grupo de Informações do Crédito Presumido** **referente ao IBS** |  |  |
| cCredPres | gIBSCredPres | Não | Código de Classificação do Crédito Presumido | TTRBMOV.CODCREDPRESUMIDO | O campo é gerado no XML com **zero à esquerda** sempre que o código possuir apenas **1 caractere**.  **Exemplo:**   * Valor informado: `4` * Valor gerado no XML: `04` |
| pCredPres | gIBSCredPres | Não | Percentual do Crédito Presumido | TTRBMOV.PCCREDPRESUMIDO |  |
| vCredPres | gIBSCredPres | Não | Valor do Crédito Presumido | TTRBMOV.VALORCREDPRESUMIDO |  |
| vCredPresCondSus | gIBSCredPres | Não | Valor do Crédito Presumido em condição suspensiva. | **Não será gerado no momento** |  |
| **gCBSCredPres** | **gIBSCBS** | **Não** | **Grupo de Informações do Crédito Presumido** **referente a CBS** |  |  |
| cCredPres | gCBSCredPres | Não | Código de Classificação do Crédito Presumido | TTRBMOV.CODCREDPRESUMIDO |  |
| pCredPres | gCBSCredPres | Não | Percentual do Crédito Presumido | TTRBMOV.PCCREDPRESUMIDO |  |
| vCredPres | gCBSCredPres | Não | Valor do Crédito Presumido | TTRBMOV.VALORCREDPRESUMIDO |  |
| vCredPresCondSus | gCBSCredPres | Não | Valor do Crédito Presumido em condição suspensiva. | **Não será gerado no momento** |  |
| Dest | impostoibscbs | Não |  |  |  |
| Imovel | impostoibscbs | Não |  |  |  |
