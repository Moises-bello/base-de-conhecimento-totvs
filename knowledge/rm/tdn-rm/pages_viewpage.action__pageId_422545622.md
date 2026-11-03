---
content_hash: 4a108925c51c3396fa2da402b9db443eec03257b717eeb4527931797ec6c4320
fetched_at: '2026-06-29T00:09:19.601870+00:00'
page_id: '422545622'
product: rm
source: tdn-rm
title: GIA (SP)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545622
version: 3
---

A GIA é uma declaração eletrônica que consta as operações de entradas e saídas das empresas. É por meio dela que a SEFAZ tem ciência dos créditos e débitos do ICMS.  Nela consta o ICMS a credito, a débito e as operações sujeitas a ST e também as operações estaduais e interestaduais. É obrigatório transmitir a GIA empresas que são tributadas pelo ICMS, tanto lucro real como lucro presumido.   
 O arquivo GIA07XX.TXT gerado pelo Sistema de Gestão Fiscal deve ser importado posteriormente no programa distribuído pela Secretaria de Estado da Fazenda - SP a fim de efetuar alterações e enviar definitivamente este ao Órgão de Competência.  
 Além da importação de arquivos pré-formatados, deverão ser incluídas neste Sistema da Secretaria da Fazenda, informações de Cadastro - UFESP, Contribuinte, Responsável e Provedor para que possam ser emitidos os protocolos, demonstrativos, transmissões e também sejam feitas as conversões para UFESP quando necessário.

**Observações Lançamentos referentes a CTRC**

**Saídas:**  
 O CTRC de SP somente deve ser emitido se o início do serviço for em SP, ou seja, UF de coleta será preenchido com SP. Neste caso, UF da operação é o de entrega e o sistema já preenche o Estado do Lançamento Fiscal de saída com UF de entrega.   
 A regra geral é que o ICMS é devido no Estado de início da operação, ou seja, UF de coleta.  
 Saindo de SP e chegando também em SP, o Estado da operação será SP e o CFOP 5.###. Saindo de SP e chegando em outra UF, o Estado da operação será o de entrega e o CFOP 6.###. Exemplo:  
 1) Cliente: SP  
     Transportadora: SP  
     Coleta: SP  
     Entrega: MG  
 No exemplo acima, se o contribuinte possui uma filial em SP e precisa gerar a GIA SP, poderá emitir o CTRC com CFOP 6.### e a UF da operação será MG. Assim a GIA SP não estará rejeitando o registro.

2) Cliente: SP  
     Transportadora: SP  
     Coleta: MG  
     Entrega: SP

No exemplo acima, o contribuinte não poderá emitir o CTRC de SP, pois o início da operação foi em MG. Com isso, a operação não deverá ir para os livros e para a GIA da filial de SP.   
 Se o contribuinte é inscrito e possui filial em MG, deverá emitir o CTRC autorizado por MG e registrá-lo na filial daquele Estado. A operação deverá ir para o DAPI MG e não para a GIA SP.   
 Se o contribuinte não é inscrito em MG, deverá recolher o imposto para aquele Estado através de guia de recolhimento e o CTRC não deverá ser emitido. Neste caso a guia de recolhimento será enviada juntamente com a mercadoria.  
O Lançamento Fiscal de saída (CTRC), somente poderá ser registrado na filial de SP se o serviço iniciar em SP. Como o sistema já preenche o UF da operação com o UF de entrega, se a entrega não for em SP, o CFOP deverá ser 6.### e o UF será o de entrega. Caso contrário, o CFOP deverá ser 5.### e o UF será SP.

**Quadro 14 – Operações Interestaduais**

O quadro 14 será considerado para todas as operações interestaduais.  
Quanto ao preenchimento do Estado:  
 Nas operações de transporte, devemos considerar o Estado da Coleta/Remetente. se o Estado de Coleta for São Paulo, o registro será gerado com o Estado da Entrega/Destinatário.
