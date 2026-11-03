---
content_hash: 55cd78c069469f645e382bfaa2bb2178f8bf37abf06f95e8855026455957eadc
fetched_at: '2026-06-29T00:09:21.718892+00:00'
page_id: '422545884'
product: rm
source: tdn-rm
title: Imprimir DANFE.NET (RM Reports)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545884
version: 22
---

ATENÇÃO

* O processo de impressão da DANFE só será realizado com os relatórios Totvs, NUCREL00037 - DANFE - 2.00 - Paisagem ou NUCREL00037 - DANFE - 2.00 - Retrato, NUCREL00080 - DANFE - 4.00 - Retrato ou NUCREL00081 - DANFE - 4.00 - Paisagem e NUCREL00074 - DANFE NFC-e - Via Consumidor.
* O relatório utiliza recurso do RM Reports e pode ser editado de acordo com a permissão do usuário, mas possui um padrão estabelecido pela Secretaria da Fazenda (SEFAZ). Antes de realizar alterações, recomendamos a consulta aos portais oficiais da NF-e.

Informamos que os dados pessoais contidos nesta entidade foram colhidos para emissão de documentos fiscais e geração de rotinas legais e são retidos por determinação legal de normas fiscais e de transparência. Os mesmos não poderão ser eliminados em virtude de obrigação legal de retenção. O cumprimento de obrigação legal é hipótese legítima do tratamento dos seus dados conforme a Lei Geral de Proteção de Dados Pessoais (Lei n° 13.709/2018).

Para mais informações sobre a LGPD e as soluções oferecidas pela TOTVS consulte nossa página neste link ([https://tdn.totvs.com/pages/releaseview.action?pageId=514427789](https://tdn.totvs.com/pages/releaseview.action?pageId=514427789 "Follow link")).

nonenonenonenone

## **01. DANFE**

O DANFE - Documento Auxiliar da Nota Fiscal Eletrônica é o espelho da NF-e em papel comum, salvos os casos de [contingências](http://tdn.totvs.com/pages/viewpage.action?pageId=422545886)[, e tem os seguintes objetivos:](http://wikihelp.totvs.com.br:1210Modalidades de Emissão da NF-e e NFC-e)

1. Acompanhar o trânsito das mercadorias;
2. Colher a firma do destinatário/tomador para a comprovação de entrega das mercadorias ou prestação de serviços;
3. Prover a necessidade de representações impressa adicionais previstas expressamente na legislação;
4. Auxiliar na escrituração da NF-e pelo destinatário.

DANFE deve ser impresso, quando em modalidade normal, em qualquer tipo de papel, exceto papel jornal. A impressão deve ser em uma única via salvo se houver disposição expressa em outro sentido.  
O DANFE só poderá ser emitido para os registros de NF-e que estiverem com o status Autorizada.  
Quando emitido em ambiente de homologação o DANFE deverá conter no quadro Informações Complementares ou em seu corpo como marca d´água a frase "SEM VALOR FISCAL" .  
Quando emitido em contingência deverá conter esta informação em destaque, conforme legislação vigente.  
Para emitir selecione a NF-e autorizada, clique no botão de processos e escolha a opção Imprimir DANFE.Net e escolha uma das opções: Visualização de Impressão, Imprimir ou Salvar em PDF.  
O relatório do DANFE dever ter sido previamente importado para o RM.

## **02. Regras específicas de campos:**

* Retirada/Entrega: para o preenchimento dos campos de retirada/entrega, é necessário que ao menos o CNPJ / CPF esteja preenchido no movimento em Transporte / Coleta e Entrega.
* Caso somente os dados de coleta estiverem preenchidos, o sistema só gerará o grupo de retirada. De forma equivalente com os dados de entrega.
* Produto perigoso: o produto será considerado perigoso ao marcar o campo "Produto Perigoso" em Detalhes / Características no cadastro de produto. Desta forma, o item que contém este produto será impresso destacado (sublinhado e em negrito) na DANFE.
* Fatura: Para preenchimento dos quadros de fatura, o movimento precisa utilizar meios de pagamento.
* Informações complementares: para preenchimento do quadro de informações complementares, o sistema limitará o número de linhas em 9 (retrato) e 6 (paisagem), sendo que cada linha poderá conter no máximo 52 letras (retrato) e 84 letras (paisagem), caso a linha supere esta quantidade de letras, o sistema quebrará a linha automaticamente. No caso destes limites não serem suficientes para comportar a informação, o sistema continuará no quadro "Continuação - Informações complementares" a ser exibido na segunda página.
* Reservado ao Fisco: as informações retornadas pela SEFAZ através da TAG xMsg do grupo protNFe serão impressas no quadro "Reservado ao Fisco".
