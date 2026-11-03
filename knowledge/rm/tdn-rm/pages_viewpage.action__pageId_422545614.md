---
content_hash: c7b5becc0bbb2c7c2aabd9103e970c3dd9f9980ba7a967c66339d2faa9b9b819
fetched_at: '2026-06-29T00:09:19.571345+00:00'
page_id: '422545614'
product: rm
source: tdn-rm
title: Implementações para a NF-e 3.10
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545614
version: 3
---

Para adequar o processo da NF-e no RM ao layout 3.10 da NF-e foi necessária a criação de novos campos na base dados. Eles estão descritos abaixo.

**Operação Presencial** - Indicador de presença do comprador no estabelecimento no momento da operação.  
 **Localização do campo**: Aba integração Fiscal no Movimento.  
 **Tag no XML**: indPres  
 **Campo na base de dados**: TMOVFISCAL.OPERACAOPRESENCIAL e DLAF.OPERACAOPRESENCIAL  
 **Valores permitidos**:  0 - Não se aplica,   
                                   1 - Operação presencial,   
                                   2 - Operação não presencial pela internet,   
                                   3 - Operação não presencial tele atendimento,   
                                   4 - NFC em operação com entrega em domicílio,   
                                   9 - Operação não presencial outros.  
    
**Número RECOPI** - Registro de Controle das Operações com Papel Imune Nacional. A informação do número do RECOPI será obrigatória na operação com papel imune e a NF-e poderá ser autorizada em até 5 (cinco) dias após a data contida no identificador gerado no RECOPI.  
 **Localização do campo**: Aba Fiscal do item do movimento.  
 **Tag no XML**: nRECOPI  
 **Campo na base de dados**: TITMMOVFISCAL.NUMERORECOPI, DITEM.NUMERORECOPI  
 **Valores permitidos**: Sequência numérica de tamanho 20 dígitos.

**Motivo da Desoneração do ICMS**   
 **Localização do campo**: Nos tributos (ICMS) do Item. Pode ser colocado como default no Cadastro da Regra de ICMS associada ao CFOP utilizado na inclusão do item.  
 **Tag no XML**:  motDesICMS  
 **Campo na base de dados**: TTRBMOV.MOTDESICMS, DLAF.MOTDESICMS.  
 **Valores permitidos**:  Ver manual de Integração da NF-e.

**Identificação do destinatário no caso de comprador estrangeiro**  
 **Localização do campo:** Aba de identificação do cadastro de CliFor.  
 **Tag no XML:** idEstrangeiro  
 **Campo na base de dados:** FCFO.DOCUMENTOESTRANGEIRO  
 **Valores permitidos:** Sequência numérica com tamanho de 5 (cinco) a 20 (vinte) dígitos.

**Indicador da IE do Destinatário**  
 **Localização do campo:** Aba Dados Fiscais | Outros dados no cadastro de CliFor  
                                            Anexo Dados Fiscais |Tributos no cadastro de Filial.  
 **Tag no xml: indEDest**  
 **Campo na base de dados:** FCFO.CONTRIBUINTE, DFILIAL.CONTRIBUINTE  
 **Valores permitidos:** 1 - Contribuinte ICMS  
                                      2 - Contribuinte isento de Inscrição no Cadastro de Contribuintes do ICMS  
                                      9 - Não Contribuinte, que pode ou não possuir Inscrição Estadual no Cadastro de Contribuintes do ICMS.  
                                      Para maiores informações a respeito dos valores permitidos consultar o manual de Integração da NF-e.

Para a correta emissão da NF-e deverá ser feita uma análise do manual de integração para que sejam elencadas quais informações devem ser enviadas e como devem ser preenchidas. Estas informações são de inteira responsabilidade do contribuinte.

Legislação

* [Manuais da NF-e/NFC-e](http://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=33ol5hhSYZk=)
* [Notas Técnicas da NF-e/NFC-e](http://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=tW+YMyk/50s=)
