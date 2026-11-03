---
content_hash: d7c2ea4de6096688689216eb558d2a88eca0c8d39c5cf6a858c12ab94c41a990
fetched_at: '2026-06-29T00:05:48.716976+00:00'
page_id: '1028924670'
product: rm
source: tdn-rm
title: Grupo de informações de operações relacionadas a bens imóveis, exceto obras
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1028924670
version: 9
---

| Nome | Pai | Obrigatório | Origem | Descrição |
| --- | --- | --- | --- | --- |
| imovel | [impostoibscbs](https://tdn.totvs.com/pages/viewpage.action?pageId=1025223880) | Não | Grupo de informações de operações relacionadas a bens imóveis, exceto obras | Grupo gerado conforme as informações incluídas no Movimento - Pasta Integrações - Sub Pasta Dest.Serviço - Imovél |
| inscImobFisc | imovel | Sim | aba **“Dest. Serviço”** Grupo Imóvel -   Campo **→** TMOVFISCALSERV/INSCRICAOIMOBILIARIA | Inscrição Imobiliária Fiscal do Imóvel destinado ao serviço. |
| cCIB | imovel | Sim | aba **“Dest. Serviço”** Grupo Imóvel -  Campo **→** TMOVFISCALSERV/CIB | Cadastro Imobiliário Brasileiro do Imóvel destinado ao serviço. |
| logradouro | imovel | Não | aba **“Dest. Serviço”** Grupo Imóvel -  Campo **→** TMOVFISCALSERV/ENDIMOVELLOGRADOURO | Código alfanumérico do Endereçamento Postal no exterior do Imóvel destinado ao serviço.  se não informado o grupo não será gerado. |
| numend | imovel | Não | aba **“Dest. Serviço”** Grupo Imóvel -  Campo **→** TMOVFISCALSERV/ENDIMOVELNUMERO | Número no logradouro do endereço do Imóvel destinado ao serviço.  se não informado o grupo não será gerado. |
| complend | imovel | Não | aba **“Dest. Serviço”** Grupo Imóvel -  Campo **→** TMOVFISCALSERV/ENDIMOVELCOMPLEMENTO | Complemento do endereço do Imóvel destinado ao serviço.  se não informado o grupo não será gerado. |
| bairro | imovel | Sim | aba **“Dest. Serviço”** Grupo Imóvel -  Campo **→** TMOVFISCALSERV/ENDIMOVELBAIRRO | Bairro do endereço do Imóvel destinado ao serviço. |
| cep | imovel | Não | aba **“Dest. Serviço”** Grupo Imóvel -  Campo **→** TMOVFISCALSERV/CEPENDIMOVEL | Código numérico do Endereçamento Postal (CEP)    do endereço do Imóvel destinado ao serviço.  se não informado o grupo não será gerado. |
| codmunibge | imovel | Não | aba **“Dest. Serviço”** Grupo Imóvel -  Campo **→** DVIEWMUNICIPIOS/CODIFICACAO | Código do município do Imóvel destinado ao serviço |
| cidade | imovel | Não | aba **“Dest. Serviço”** Grupo Imóvel -  Campo **→** DVIEWMUNICIPIOS/NOMEMUNICIPIO | Nome da cidade no exterior do Imóvel destinado ao serviço.  Obrigatório para imóvel do exterior |
| estado | imovel | Não | aba **“Dest. Serviço”** Grupo Imóvel -  Campo **→** TMOVFISCALSERV/ENDIMOVELCODETD | Nome do estado do Imóvel destinado ao serviço. |
| codpais | imovel | Não | aba **“Dest. Serviço”**  Campo **→** DPAIS/CODPAIS | Código do país do endereço do imóvel.   (Tabela de Países ISO) |
