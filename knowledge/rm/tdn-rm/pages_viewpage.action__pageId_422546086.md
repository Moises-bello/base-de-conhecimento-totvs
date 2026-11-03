---
content_hash: 950e4498bea98f56773db889563e08434d13715fbc71031cb42a0eccb9d9e856
fetched_at: '2026-06-29T00:09:23.255129+00:00'
page_id: '422546086'
product: rm
source: tdn-rm
title: Registro de Faturamento (Inclusão de RF)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546086
version: 4
---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **XML**: Inclusão de RF (Registro de Faturamento)   **Padrão de Nomeclatura dos arquivo RF**:  FAT + INC + Código Coligada + Código Filial + Id. Laf. Agrup + Data + Hora   **Formato**: XML   **Observação**: Para montagem do RF serão considerados Lançamentos Fiscais de Saída. | | | | |
| **Campo** | **Descrição** | **Origem dos Dados** | **Obrigatório** | **Observação** |
| Número RVS Empresa | Informar o número RVS da empresa que foi inserido na Inclusão do RVS e que se deseja faturar | **DLAF.CODCOLIGADA  + DLAF.CODFILIAL + DLAF.IDLAFAGRUP** | Obrigatório |  |
| ID Fatura Empresa | Informar o número identificador do faturamento da empresa que fará o mapeamento com o registro de fatura | **DLAF.CODCOLIGADA  + DLAF.CODFILIAL + DLAF.IDLAFAGRUP** | Obrigatório |  |
| Número Fatura | Informar o número da nota fiscal ou documento equivalente | **DLAF.DOCINI** | Obrigatório |  |
| Data Fatura | Informar a data do faturamento da operação.   Formato da data AAAA-MM-DD. | **DLAF.DATAEMISSAO** | Obrigatório |  |
| Id Item Fatura Empresa | Identificador unívoco do faturamento dentro do registro (o identificador pode repetir-se em registros distintos). Gerado pelo usuário sem quaisquer restrições de formato a não ser aquelas declaradas nos arquivos XSD. No caso de retificação, o faturamento será identificado através dele. | **DITEM.NUMITEM** | (TAG NÃO OBRIGATÓRIA) | [11ª Edição do Manual do Módulo de Aquisição/Venda da Rotina Federal SISCOSERV.](http://tdn.totvs.com/pages/viewpage.action?pageId=403737188) |
| Número Operação Empresa | Informar o número de mapeamento da operação realizada na inclusão, retificação ou aditivo do registro | **DLAF.CODCOLIGADA + DLAF.IDLAF + DITEM.IDPRD** | Obrigatório | [11ª Edição do Manual do Módulo de Aquisição/Venda da Rotina Federal SISCOSERV.](http://tdn.totvs.com/pages/viewpage.action?pageId=403737188) |
| Valor Faturado | Informar o valor parcial ou total da fatura da operação. Formato do campo: 1000.00, o ponto é o separador para os centavos | **DITEM.VALORMERC + DITEM.VALORDESPESA             +**   **DITEM.VALORSEGURO + DITEM.VLRFRETE – DITEM.DESCONTOITEM** | Obrigatório |  |
| Valor Mantido Exterior | Informar o valor da fatura da operação mantido no Exterior. Formato do Campo: 1000.00, o ponto é o separador para os centavos       Este campo se refere a valores que porventura, tenhamos mantido em instituições financeiras no exterior. Esta informação depende se a empresa possui conta bancaria no exterior, recebe o valor dos serviços prestados mediante a este banco e mantém este valor na instituição estrangeira. | Gerar com o mesmo valor gerado na tag **ValorFaturado** | Não Obrigatório |  |
| Vinculação Número RE | Se a operação de venda estiver vinculada a movimentação de bens informar os REs associados à movimentação temporária de bens. O campo contém 12 dígitos e deve ser informado com máscara | **DITEM.NUMERORE** | Não Obrigatório | Excluído do grupo "Faturamento" mas continua nos arquivos de Venda e Aquisição conforme determinações legais impostas pela [11ª Edição do Manual do Módulo de Aquisição/Venda da Rotina Federal SISCOSERV](http://tdn.totvs.com/pages/viewpage.action?pageId=403737188) |
| Vinculação Número DI | Se a operação de venda estiver vinculada a movimentação de bens informar as DI's associadas a movimentação temporária de bens. O campo contém 9 dígitos e um Dígito verificador e deve ser informado com máscara conforme exemplo: 11/1111111-3 | **Não preenchido** | Não Obrigatório | Excluído do grupo "Faturamento" mas continua nos arquivos de Venda e Aquisição conforme determinações legais impostas pela [11ª Edição do Manual do Módulo de Aquisição/Venda da Rotina Federal SISCOSERV](http://tdn.totvs.com/pages/viewpage.action?pageId=403737188). |
