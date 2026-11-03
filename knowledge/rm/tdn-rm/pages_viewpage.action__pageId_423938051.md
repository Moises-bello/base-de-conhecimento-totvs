---
content_hash: 73ddd23d5a4ad44bb3f7051555379c69d6735f5816f0a4a7173cc2ebf0226ae4
fetched_at: '2026-06-29T00:09:25.186335+00:00'
page_id: '423938051'
product: rm
source: tdn-rm
title: Manifesto Eletrônico Documentos Fiscais (MDF-e)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938051
version: 6
---

O objetivo é orientar sobre os trâmites do MDF-e, onde esse manifesto é um documento fiscal eletrônico, de existência apenas digital, cuja validade jurídica é garantida pela assinatura digital do emitente e Autorização de uso de MDF-e pela administração tributária da unidade federada do contribuinte, sendo um documento fiscal que deverá ser emitido por empresas prestadoras de serviço de transporte para prestações com mais de um conhecimento de transporte ou pelas demais empresas nas operações, cujo transporte seja realizado em veículos próprios, arrendados, ou mediante contratação de transportador autônomo de cargas, com mais de uma nota fiscal.  
O MDF-e será emitido com base no Manual de Integração MDF-e – Contribuinte e conterá no mínimo:

* Identificação dos documentos fiscais relacionados à carga transportada
* Identificado por um número de chave de acesso
* Ser elaborado no padrão XML
* Possuir série de 1 a 999 e numeração sequencial de 1 a 999.999.999
* Ser assinado digitalmente pelo emitente (certificação digital)

O MDF-e substitui o documento fiscal Manifesto de Carga, modelo 25. A representação gráfica do MDF-e é o DAMDFE, que possui layout estabelecido no [Manual de Orientação do Contribuinte](http://www.scarpinicontabilidade.com.br/download.php?uCode=qQkM5A9L0jro5bQ8Hcvme) e obrigatoriedade de acompanhar a carga durante o transporte. No decorrer do percurso ou se houver qualquer alteração nas informações do MDF-e como o veículo ou a carga ou o motorista, entre outros, o mesmo deverá ser encerrado e ser refeito um novo documento MDF-e a partir do início com a sua nova configuração.   
O MDF-e será gerado para os modais: Rodoviário, Ferroviário, Aquaviário e Aéreo. Como a informação do modal estará vinculada à parametrização do tipo de movimento, se uma empresa gerar MDF-e de modais diferentes, será necessário criar um tipo de movimento para cada modal.   
Como o MDF-e substitui o livro fiscal Manifesto de Carga, o movimento de saída vinculado a ele terá um emitente e destinatário, não terá integração fiscal e nem financeira. A integração contábil ficará a cargo de cada empresa. Na visão do movimento do MDF-e, além dos grupos normais de parametrização do movimento, serão solicitadas informações específicas para geração do MDF-e, que estarão identificadas em grupos específicos.  
 ***Atenção*:**

* Para viabilização do processo se faz necessário utilizar o TSS ou Client Neogrid para o envio do XML à SEFAZ.
* Movimentos específicos de saída para o envio da MDF-e.
* A receita somente validará o envio oficialmente caso o modo de operação esteja configurado como "PRODUÇÃO".
* Após a Impressão DAMDFE em contingência fica sendo obrigatório a autorização em até 24 horas após a impressão, o mesmo vale para o caso da solicitação do cancelamento do MDF-e, nesse segundo caso contado do momento em que foi concedida a autorização do MDF-e, desde que não tenha iniciado o transporte, observadas as demais normas da legislação pertinente.
* O cancelamento da MDF-e automaticamente fará o cancelamento do movimento relacionado.
* Em nenhum momento os movimentos que já foram enviados à SEFAZ ou que estão em contingência poderão ser excluídos ou cancelados, sendo assim, deverá ser enviado um evento de cancelamento de MDF-e.
* Só será permitido o cancelamento de um MDF-e através de evento caso seu status esteja como Enviado.
* Um MDF-e já encerrado não poderá ser cancelado em nenhuma hipótese.
* Os movimentos em contingência poderão ser enviados no modo normal.

Deve-se ser verificada a parametrização do sistema em relação ao MDF-e, observando qual será a sua integração, se via TSS ou se via Client Neogrid, onde essa parametrização será realizada nos parâmetros por filiais através do seguinte caminho:

**Ambiente | Parâmetros | TOTVS Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Parâmetros por Filial**

Após a criar um movimento parametrizado, o usuário deverá entrar no seguinte caminho para efetuar o envio do MDF-e:

**Vendas | Documentos Eletrônicos | Manifesto Eletrônico Documentos Fiscais (MDF-e)**

A Consulta da MDF-e não poderá ser realizada com o status pendente.  
Após o MDF-e ser enviado demora um período para que haja a validação por parte da SEFAZ (Sem período fixo).  
No final do percurso ou se houver qualquer alteração nas informações do MDF-e como o veículo, a carga, o motorista, etc, o mesmo deverá ser encerrado.  
Na emissão do MDF-e, quando associado uma NF-e (CODMODDOC = 55) que foi emitida em contingência o sistema busca na TNFEESTADUAL.DADOSNFECONTINGENCIA o valor para gerar no XML a tag <SegCodBarra>.   
Agora se tem uma NF-e que precisa ser associada ao MDF-e que não foi emitida pelo sistema, ou seja será informada manualmente, é habilitado no movimento o campo Segundo Código de Barras da NF-e na aba CTRC | CTRC Saída para informar o segundo código de barras. Assim esse será gerado no XML na tag <SegCodBarra>.

---

Informações Adicionais

* # [MDF-e Layout 3.0](http://tdn.totvs.com/display/LRM/MDF-e+Layout+3.0)
