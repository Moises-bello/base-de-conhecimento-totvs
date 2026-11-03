---
content_hash: 0047919539d31a1b2857d6a397b2d84588ba73e667dedd14d969c79f7899df7a
fetched_at: '2026-06-29T00:09:21.362327+00:00'
page_id: '422545869'
product: rm
source: tdn-rm
title: Declaração Mensal 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545869
version: 3
---

Na Declaração Mensal deverá conter todas as notas fiscais incluídas pela SEFAZ-AM no arquivo Notas Fiscais a declarar, selecionado na geração deste arquivo, demais Notas Fiscais Eletrônicas que tenham sido recebidas pelo contribuinte e também as notas que, por qualquer motivo, não constem no Arquivo de Notas a Declarar gerado pela SEFAZ-AM.   
Para a correta geração do arquivo serão selecionados os Lançamentos de Entrada Interestaduais que possuem natureza de operação do grupo 2.XXX  
 O reconhecimento das notas será através da tag <<reconheceNFe>> gerada no arquivo:

* Quando as Notas Fiscais constarem no TOTVS Gestão Fiscal e a apuração dos tributos já terem sido realizadas, será gerado o campo fixo com "S" Reconhecida;
* As Notas Fiscais existentes no arquivo xml disponibilizado pela SEFAZ-AM e que não constarem no aplicativo, serão reconhecidas com valor fixo "N" Não reconhecido.

Vale ressaltar que quando uma NF-e não for reconhecida pelo destinatário, será iniciada a ação fiscal cabível para esclarecimento do destino dos produtos nela consignados.  
 O arquivo de Declaração Mensal, uma vez transmitido e processado sem erros, servirá para que a SEFAZ-AM calcule o valor do ICMS devido pelo contribuinte em relação ao conjunto de Notas Fiscais declaradas e faça a inclusão do valor do débito no conta corrente, nos Códigos de Tributos correspondentes.   
 **Schema XML**: enviDeclaracaoMensalAuto\_v9.99.xsd
