---
content_hash: 7199b00d76f7d9b63f8b24b85de7b084fee4af1dc1a351e4a0608eb15718195c
fetched_at: '2026-06-29T00:11:46.475538+00:00'
page_id: '822687536'
product: rm
source: tdn-rm
title: serv/comExt
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=822687536
version: 30
---

Para a geração deste grupo, a **CFOP** deve obrigatoriamente iniciar com o dígito **7,** e o cliente/fornecedor deve ter o campo "**Nacionalidade***"* marcado com a opção "**Estrangeiro***"* ou o estado do endereço principal deve ter a opção Nacional desmarcada.

| Nome | Pai | Obrigatório | Origem | Descrição |
| --- | --- | --- | --- | --- |
| **comExt** | **/DPS/infDPS/serv/** | **Não** |  | **Grupo de informações sobre transações entre residentes ou domiciliados no Brasil com residentes ou domiciliados no exterior** |
| mdPrestacao | /DPS/infDPS/serv/comExt/ | Sim | TMOVFISCAL.MODOPRESTACAO | Modo de Prestação:  0 - Desconhecido (tipo não informado na nota de origem); 1 - Transfronteiriço; 2 - Consumo no Brasil; 3 - Movimento Temporário de Pessoas Físicas; 4 - Consumo no Exterior; |
| vincPrest | /DPS/infDPS/serv/comExt/ | Sim | TMOVFISCAL.VINCPREST | Vínculo entre as partes no negócio:  0 - Sem vínculo com o tomador/ Prestador 1 - Controlada; 2 - Controladora; 3 - Coligada; 4 - Matriz; 5 - Filial ou sucursal; 6 - Outro vínculo; |
| tpMoeda | /DPS/infDPS/serv/comExt/ | Sim | Este campo gera automaticamente o valor fixo **790,** referente a moeda Real | Identifica a moeda da transação comercial. |
| vServMoeda | /DPS/infDPS/serv/comExt/ | Sim | TMOV.VALORLIQUIDO | Valor do serviço prestado expresso em moeda estrangeira especificada em tpMoeda. |
| mecAFComexP | /DPS/infDPS/serv/comExt/ | Sim | TMOVFISCAL.MEXAFCOMEXP | Campo disponível na nota do prestador.  Mecanismo de apoio/fomento ao Comércio Exterior utilizado pelo prestador do serviço:  00 - Desconhecido (tipo não informado na nota de origem); 01 - Nenhum; 02 - ACC - Adiantamento sobre Contrato de Câmbio – Redução a Zero do IR e do IOF; 03 - ACE – Adiantamento sobre Cambiais Entregues - Redução a Zero do IR e do IOF; 04 - BNDES-Exim Pós-Embarque – Serviços;  05 - BNDES-Exim Pré-Embarque - Serviços; 06 - FGE - Fundo de Garantia à Exportação; 07 - PROEX - EQUALIZAÇÃO 08 - PROEX - Financiamento; |
| mecAFComexT | /DPS/infDPS/serv/comExt/ | Sim | Este campo gera automaticamente o valor fixo **01 -** Nenhum; | Se refere ao mecanismo de apoio/fomento ao Comércio Exterior utilizado pelo tomador do serviço |
| movTempBens |  | Sim | TMOVFISCAL.MOVTEMPBENS | Vínculo da Operação à Movimentação Temporária de Bens:  0 - Desconhecido (tipo não informado na nota de origem); 1 - Não; 2 - Vinculada - Declaração de Importação; 3 - Vinculada - Declaração de Exportação; |
| nDI |  | Não | TMOVFISCAL.DECLARACAOIMPORTACAO | **Este campo será gerado sob demanda.**  Número da Declaração de Importação (DI/DSI/DA/DRI-E) averbado. |
| nRE |  | Não | TMOVFISCAL.DECLARACAOEXPORTACAO | Número do Registro de Exportação (RE) averbado. |
| mdic |  | Sim | TMOVFISCAL.MDIC | Indicador se a NFS-e deverá ser disponibilizada ao MDIC.  0 - Não enviar para o MDIC; 1 - Enviar para o MDIC; |
