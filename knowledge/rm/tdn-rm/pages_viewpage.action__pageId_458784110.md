---
content_hash: bdcfead9d7d1b37c585525e85042720d113f5e4ed7aaa97314a5b9e3725d8f78
fetched_at: '2026-06-29T00:10:14.410353+00:00'
page_id: '458784110'
product: rm
source: tdn-rm
title: FISCAL01-8077 - DT Nota Técnica 2018.005
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=458784110
version: 20
---

# Nota Técnica 2018.005

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Nota Fiscal Eletrônica (NF-e) |
| **Situação/Requisito:** | Implementar Nota Técnica (NT) 2018.005 |
| **Solução/Implementação:** | Para atender as necessidades da NT 2018.005 foram realizadas as implementações abaixo.  **Gatilho para emissão da NF-e através da NT 2018.005:**  Foi criado o campo **Habilita NT 2018.05** nos dados fiscais do cadastro da Filial para informar se as notas emitidas pela mesma deverão seguir o padrão definido na NT 2018.005. Anexo Dados Fiscais do cadastro da filial:  **Grupo ZD:**  A partir daNT 2018.005 cada xml de cada nota deverá conter os dados do responsável técnico do sistema no qual o xml foi gerado. Para atender esta demanda foi criado um serviço no servidor mashup da TOTVS (<http://mashups.totvs.com.br>) para que os dados sejam fornecidos/atualizados nas bases dos clientes. Para atualizar o usuário deverá executar em sua base o processo "Atualizar Responsável técnico" disponível na tela de emissão da NF-e.  No XML da NF-e foi implementado o grupo ZD com os dados do responsável técnico. Exemplo 01111111000191 Responsável Técnico email@totvs.com.br 31922223333 01 12ugRZOFrqQoHkWXWouMhetxfFs= ]]>  ATENÇÃO Os dados do Responsável técnico são de responsabilidade da TOTVS e o usuário do sistema não tem a opção de alterá-los. Se for necessário atualizar, basta executar o processo **Atualizar Responsável Técnico** na tela de envio da NF-e/NFC-e.  Se algum dado for alterado na base sem que seja pelo processo **Atualizar Responsável Técnico** as NF-e não serão enviadas apresentando a mensagem: "Falha ao inserir o grupo ZD: Os dados de responsável técnico não estão consistentes. Dica: execute o processo de atualização dos dados do responsável técnico"    **Grupo K:**  No xml da NF-e foi implementada a tag *xMotivoIsencao* no grupo "med" que será gerada através do campo "Motivo de Isenção ANVISA" no cadastro do produto.    XML:    **Grupo F e G:**  De acordo com a Nota Técnica 2018.005, passa a ser necessário o envio de mais dados referente ao Local de Coleta/Entrega. Existe um grupo específico para as informações de retirada (F) e um grupo específico para as informações de entrega (G). O grupo de informações de retirada será enviado se o endereço de coleta estiver preenchido no movimento e o grupo de informações de entrega será enviado se o endereço de entrega estiver preenchido no movimento. Sendo assim, podem ocorrer situações em que somente os dados de coleta ou os dados de entrega estarão preenchidos.  Quando o parâmetro "Utilizar Endereço de Coleta e Entrega como Destinatário" estiver marcado, serão habilitados os dados de coleta e entrega no movimento, conforme abaixo:      **Mensagem de Interesse da SEFAZ**    Foi implementado no Processo de Consulta da NF-e o retorno das tags cMsg e xMsg (Mensagem de Interesse da SEFAZ) do Grupo infProt para que os mesmo sejam apresentados em uma Aba do Cadastro de Notas Fiscais Eletrônicas.      **Grupo ICMS60**  Foi implementado a tag vICMSSubstituto que será o valor do ICMS.      **Grupo ICMSSN500:**  Foi implementado a tag *vICMSSubstituto* que será o valor do ICMS.      **Grupo ICMSST - Repasse de** **Combustível**  Foram implementadas as tags *ICMSSTSubstituto*, *vBCFCPSTRet*, *pFCPSTRet* e *pFCPSTRet* que serão preenchidas conforme o grupo *ICMS60*. |
