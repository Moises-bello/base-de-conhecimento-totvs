---
content_hash: 43f7105c3ef2658207d1f361155eb56ac29ed44473a2021cfdecbddb70983a8f
fetched_at: '2026-06-29T00:10:51.365065+00:00'
page_id: '566491377'
product: rm
source: tdn-rm
title: 9782487 FISCAL01-13907 DT NFS-e Curitiba - Emissão de NFS sem os dados do endereço
  do tomador do serviço
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=566491377
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | NFS-e Municipal |
| Ticket: | 9782487 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-13907 |

## **02. SITUAÇÃO/REQUISITO**

A prefeitura de Curitiba permite a emissão de NFS sem os dados do endereço do tomador do serviço, porém quando tal emissão é realizada, o TSS retorna a seguinte mensagem:

"Não foi possível enviar o(s) movimento(s) da Coligada 20, Filial 15, Tipo Movimento 2.1.40.  
TOTVS Service SOA TSS : [SchemaX]TSS<SchemaValTSS><Ids><Id><Codigo>789278761</Codigo><Msg>Element 'bairro': This element is not expected. Expected is ( numend ).  
</Msg></Id></Ids></SchemaValTSS>"

## **03. SOLUÇÃO**

Ajuste nas tags de endereço quando o usuário não informar o logradouro, numero, bairro, cidade e uf o sistema  
possa preencher os dados como SEM ENDEREÇO, SN e SU na geração do XML para envio ao TSS.

Grupo Tomador:

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| logradouro | tomador | E | 1-1 | Logradouro do tomador. | FCFO.RUA | A prefeitura de Curitiba permite a emissão de NFS sem os dados do endereço do tomador do serviço. Caso a tag logradouro não for informado nesta situação, o mesmo será exibido como SEM ENDERECO |
| numend | tomador | E | 1-1 | Número do endereço do tomador. | FCFO.NUMERO | A prefeitura de Curitiba permite a emissão de NFS sem os dados do endereço do tomador do serviço. Caso a tag numend não for informado nesta situação, o mesmo será exibido como SN |
| bairro | tomador | E | 1-1 | Bairro do tomador. | FCFO.BAIRRO | A prefeitura de Curitiba permite a emissão de NFS sem os dados do endereço do tomador do serviço. Caso a tag bairro não for informado nesta situação, o mesmo será exibido como SEM ENDERECO |
| cidade | tomador | E | 1-1 | Município do tomador. | GMUNICIPIO.NOMEMUNICIPIO | A prefeitura de Curitiba permite a emissão de NFS sem os dados do endereço do tomador do serviço. Caso a tag cidade não for informado nesta situação, o mesmo será exibido como SEM ENDERECO |
| uf | tomador | E | 1-1 | Unidade federativa do tomador. | FCFO.CODETD | A prefeitura de Curitiba permite a emissão de NFS sem os dados do endereço do tomador do serviço. Caso a tag uf não for informado nesta situação, o mesmo será exibido como SU |
