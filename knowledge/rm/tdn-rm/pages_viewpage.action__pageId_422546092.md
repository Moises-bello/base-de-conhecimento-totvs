---
content_hash: 955f02183142a3bf9c90d849a55fcb25edcf9d7aa7572adee88e9e671d355020
fetched_at: '2026-06-29T00:09:23.301558+00:00'
page_id: '422546092'
product: rm
source: tdn-rm
title: Registro de Pagamento (Inclusão de RP)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546092
version: 6
---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **XML**: Inclusão de RP (Registro de Pagamento)  **Padrão de Nomeclatura dos arquivo RP**:  RP + INC + Código Coligada + Código Filial + Id. Laf. Agrup + Data + Hora  **Formato**: XML  **Observação**: Para montagem do RP serão considerados Lançamentos Fiscais de Entrada com integração com o Financeiro e Status do Lançamento Financeiro Baixado ou Baixado com Acordo. | | | | |
| **Campo** | **Descrição** | **Origem dos Dados** | **Obrigatório** | **Observação** |
| Número RAS Empresa | Informar o número RAS da empresa que foi inserido na Inclusão e que se deseja faturar | **DLAF.CODCOLIGADA  + DLAF.CODFILIAL + DLAF.IDLAFAGRUP** | Obrigatório |  |
| ID Pagamento Empresa | Informar o número identificador do Pagamento da empresa que fará o mapeamento com o registro de fatura | **FLAN.CODCOLIGADA + FLAN.IDLAN** | Obrigatório |  |
| Número Pagamento | Informar o número da nota fiscal ou documento equivalente | **DLAF. DOCINI** | Obrigatório |  |
| Data Pagamento | Informar a data do Pagamento da operação no formato AAAA-MM-DD | **FLAN.DATABAIXA** | Obrigatório | Formato AAAA-MM-DD |
| Id Item Pagamento Empresa | Identificador unívoco do pagamento dentro do registro (o identificador pode repetir-se em registros distintos). Gerado pelo usuário sem quaisquer restrições de formato a não ser aquelas declaradas nos arquivos XSD. No caso de retificação, o pagamento será identificado através dele. | **DITEM.NUMITEM** | Obrigatório | [11ª Edição do Manual do Módulo de Aquisição/Venda da Rotina Federal SISCOSERV](http://tdn.totvs.com/pages/viewpage.action?pageId=403737188)[.](http://www.mdic.gov.br/images/REPOSITORIO/scs/decin/Siscoserv/11aEdicaoManualModuloAquisi%C3%A7%C3%A3o_versao_final.pdf) |
| Número Operação Empresa | Informar o número de mapeamento da operação realizada na inclusão, retificação ou aditivo do registro | **DLAF.CODCOLIGADA + DLAF.IDLAF + DITEM.IDPRD** | Obrigatório |  |
| Valor Pago | Informar o valor do Pagamento da operação. Formato do campo: 1000.00, o ponto é o separador para os centavos | **FLAN.VALORBAIXADO** | Obrigatório |  |
| Valor Pago Rec Mantido Exterior | Informar o valor do Pagamento Oriundo de Recurso Mantido no Exterior. Formato do Campo: 1000.00, o ponto é o separador para os centavos | Gerar com o mesmo valor gerado na tag **ValorPago** | Não obrigatório | [11ª Edição do Manual do Módulo de Aquisição/Venda da Rotina Federal SISCOSERV](http://tdn.totvs.com/pages/viewpage.action?pageId=403737188). |
| Vinculação Número RE | Se a operação de venda estiver vinculada a movimentação de bens  informarem os REs associados. O campo contém 12 dígitos e deve ser informado com máscara 11/1111111111 | Não é gerado | Não obrigatório | Excluído do grupo "Faturamento" mas continua nos arquivos de Venda e Aquisição conforme determinações legais impostas pela [11ª Edição do Manual do Módulo de Aquisição/Venda da Rotina Federal SISCOSERV](http://tdn.totvs.com/pages/viewpage.action?pageId=403737188). |
| Vinculação Número DI | Se a operação de venda estiver vinculada a movimentação de bens  informarem as DI's.O campo contém 9 dígitos e um Dígito verificador e deve ser informado com máscara conforme exemplo: 11/1111111-3 | **DLAFEXTERIOR.NUMERODI** | Não obrigatório | Excluído do grupo "Faturamento" mas continua nos arquivos de Venda e Aquisição conforme determinações legais impostas pela [11ª Edição do Manual do Módulo de Aquisição/Venda da Rotina Federal SISCOSERV](http://tdn.totvs.com/pages/viewpage.action?pageId=403737188). |
