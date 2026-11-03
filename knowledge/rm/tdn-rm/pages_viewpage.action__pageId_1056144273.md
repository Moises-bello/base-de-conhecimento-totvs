---
content_hash: d4721d143accb05172767b1961735f7b33a2d088ad1f15c4c99d54412000cd24
fetched_at: '2026-06-29T00:05:52.043027+00:00'
page_id: '1056144273'
product: rm
source: tdn-rm
title: Grupo de informações relativas à exportação/importação de serviço prestado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1056144273
version: 3
---

### Voltar para [Layout único de integração da NFS-e com o TSS](https://tdn.totvs.com/pages/viewpage.action?pageId=560652116)

| **Nome** | **Pai** | **Tipo Elemento** | **Ocorrência** | **Campo no RM** | **Descrição** | **Observações** |
| --- | --- | --- | --- | --- | --- | --- |
| **comExt** | **[servico](https://tdn.totvs.com/pages/viewpage.action?pageId=560653807)** | **G** | **0-1** |  | **Grupo de informações relativas à exportação/importação de serviço prestado** | Será gerado sempre que o cliente for do exterior e a natureza de operação (CFOP) for iniciada por 7. |
| mdPrestacao | comExt | E | 0-1 | TMOVFISCAL.MODOPRESTACAO | Modo de Prestação:  0 - Desconhecido (tipo não informado na nota de origem); 1 - Transfronteiriço; 2 - Consumo no Brasil; 3 - Movimento Temporário de Pessoas Físicas; 4 - Consumo no Exterior; |  |
| vincPrest | comExt | E | 0-1 | TMOVFISCAL.VINCPREST | Vínculo entre as partes no negócio:  0 - Sem vínculo com o tomador/ Prestador 1 - Controlada; 2 - Controladora; 3 - Coligada; 4 - Matriz; 5 - Filial ou sucursal; 6 - Outro vínculo; |  |
| tpMoeda | comExt | E | 0-1 | Este campo gera automaticamente o valor fixo **790,**referente a moeda Real | Identifica a moeda da transação comercial. |  |
| vServMoeda | comExt | E | 0-1 | TMOV.VALORLIQUIDO | Valor do serviço prestado expresso em moeda estrangeira especificada em tpMoeda. |  |
| mecAFComexP | comExt | E | 0-1 | TMOVFISCAL.MEXAFCOMEXP | Campo disponível na nota do prestador.  Mecanismo de apoio/fomento ao Comércio Exterior utilizado pelo prestador do serviço:  00 - Desconhecido (tipo não informado na nota de origem); 01 - Nenhum; 02 - ACC - Adiantamento sobre Contrato de Câmbio – Redução a Zero do IR e do IOF; 03 - ACE – Adiantamento sobre Cambiais Entregues - Redução a Zero do IR e do IOF; 04 - BNDES-Exim Pós-Embarque – Serviços;  05 - BNDES-Exim Pré-Embarque - Serviços; 06 - FGE - Fundo de Garantia à Exportação; 07 - PROEX - EQUALIZAÇÃO 08 - PROEX - Financiamento; | valor default: 00 - Desconhecido (tipo não informado na nota de origem). |
| mecAFComexT | comExt | E | 0-1 | Este campo gera automaticamente o valor fixo **01 -**Nenhum; | Se refere ao mecanismo de apoio/fomento ao Comércio Exterior utilizado pelo tomador do serviço |  |
| movTempBens | comExt | E | 0-1 | TMOVFISCAL.MOVTEMPBENS | Vínculo da Operação à Movimentação Temporária de Bens:  0 - Desconhecido (tipo não informado na nota de origem); 1 - Não; 2 - Vinculada - Declaração de Importação; 3 - Vinculada - Declaração de Exportação; | valor default:  0 - Desconhecido (tipo não informado na nota de origem); |
| nDI | comExt | E | 0-1 | TMOVFISCAL.DECLARACAOIMPORTACAO | **Este campo será gerado sob demanda.**  Número da Declaração de Importação (DI/DSI/DA/DRI-E) averbado. |  |
| nRE | comExt | E | 0-1 | TMOVFISCAL.DECLARACAOEXPORTACAO | Número do Registro de Exportação (RE) averbado. |  |
| mdic | comExt | E | 0-1 | TMOVFISCAL.MDIC | Indicador se a NFS-e deverá ser disponibilizada ao MDIC.  0 - Não enviar para o MDIC; 1 - Enviar para o MDIC; | valor default:  0 - Não enviar para o MDIC; |
