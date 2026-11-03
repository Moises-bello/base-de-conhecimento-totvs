---
article_id: 360017527792
category: Materiais - Compras (SIGACOM)
content_hash: 6059038051c9be52d90bd266ccb8f2cc0f93bf2a2085f00aaa1dfea203c81be6
fetched_at: '2026-06-28T22:41:07.513742+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Códigos de erro no
  REPROCESSAR do Importador XML
type: support-article
updated_at: '2025-03-06T11:08:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017527792-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-C%C3%B3digos-de-erro-no-REPROCESSAR-do-Importador-XML
---

**Ocorrência**No momento de realizar a importação de uma nota é apresentado código de erro no REPROCESSAR no Importador XML.

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - A partir da Versão 12  
  
  
**Solução**

|  |  |  |  |
| --- | --- | --- | --- |
| **C****ód****igo** | **Situação** | **Solução** | **Observação** |
| COM001 | Erro de sintaxe no arquivo XML | Entre em contato com o emissor do documento e comunique a ocorrência. |  |
| COM002 | Este XML pertence a outra empresa/filial e não poderá ser processado na empresa/filial corrente | Importe na filial correta. |  |
| COM003 | Documento complemento de preço icms/ipi não é tratado pelo Importador XML | Gere o documento complemento de preço icms/ipi manualmente através da rotina documento de entrada. |  |
| COM004 | Tipo NF-e de ajustes não será tratado pelo Importador XML | Gere o documento de ajustes de forma manual através da rotina documento de entrada. |  |
| COM005 | ID de NF-e já registrado na NF do fornecedor. | Exclua o documento registrado na ocorrência. |  |
| COM006 | ID de NF-e já registrado na NF do Do Cliente. | Exclua o documento registrado na ocorrência. |  |
| COM007 | Fornecedor/Cliente inexistente na base | Gere cadastro para este fornecedor/cliente. |  |
| COM008 | O Cliente Emitente não está cadastrado | Inclua o Emitente do XML como um cliente. |  |
| COM009 | Não foi possível incluir o destinatário. | Inclua o destinatário do XML como um cliente. |  |
| COM010 | Não foi possível incluir o local de entrega. | Inclua o local de entrega (Tabela DUL). |  |
| COM011 | Não foi possível atualizar o local de entrega. | Atualize o local de entrega (Tabela DUL). |  |
| COM012 | Fornecedor sem cadastro de Produto X Fornecedor. | Inclua o fornecedor com o produto no cadastro de produto x fornecedor. |  |
| COM013 | Nota fiscal possui itens com valor zerado. | Verifique a nota recebida do fornecedor. |  |
| COM015 | Erro no TMSAE80INC | Verifique as informações da Nf-e (Detalhe no retorno da função TMSAE80INC). |  |
| COM016 | DS\_PLIQUI - O tamanho do campo não suporta o valor fornecido. | Aumente o tamanho do campo DS\_PLIQUI. |  |
| COM017 | DS\_PBRUTO - O tamanho do campo não suporta o valor fornecido. | Aumente o tamanho do campo DS\_PBRUTO. |  |
| COM019 | ID de CT-e já registrado na NF. | Exclua o documento registrado na ocorrência. |  |
| COM020 | Documento de entrada inexistente na base. | NF Origem não encontrada ao importar o CT-e. |  |
| COM021 | TES não informada no parâmetro MV\_XMLTECT ou inexistente no cadastro correspondente. | Cadastre a TES e informe no parâmetro. |  |
| COM022 | Condição de pagamento não informada no parâmetro MV\_XMLCPCT ou inexistente no cadastro correspondente. | Cadastre a condição de pagamento e informe no parâmetro. |  |
| COM023 | Produto frete não informado no parâmetro MV\_XMLPFCT ou inexistente no cadastro correspondente. | Cadastre o produto e informe no parâmetro. |  |
| COM024 | Erro na execauto (CT-e) | Corrija a inconsistência apontada no log. | Rotinas do Importador a partir do dia 22/11/19 e com o campo CKO\_MSGERR será gravado o detalhe do erro. |
| COM025 | Documento já processado. | Exclua o documento registrado na ocorrência. |  |
| COM026 | O tamanho de um dos campos de volume não suporta o valor fornecido. | Aumente o tamanho do campo correspondente. |  |
| COM027 | Cliente sem cadastro de Produto X Cliente. | Inclua o cliente com o produto no cadastro de produto x cliente. |  |
| COM028 | CNPJ fornecedor/cliente duplicado. | Utilize o P.E A116IFOR (CT-e) ou A140IFOR (NF-e) para definir qual Cliente/Fornecedor utilizar. |  |
| COM029 | Quantidade nos Pedidos (P.E A140IVPED) é maior que a quantidade do XML | Utilize o pedido correto no P.E. |  |
| COM030 | Fornecedor/Cliente bloqueado na base | Faça o desbloqueio do cadastro para este fornecedor/cliente. |  |
| COM031 | TES bloqueado. | Verifique a configuração do cadastro de TES. |  |
| COM032 | Retorno do ponto de entrada A116ICOMP inconsistente. | Verifique na documentação do P.E. |  |
| COM033 | Inscrição Estadual do Fornecedor/Cliente não identificada. | Verifique o cadastro do Fornecedor/Cliente e informe a inscrição estadual. |  |
| COM034 | Tag \_DTEMISNFSE não encontrada. | Verificar com quem originou o XML. |  |
| COM035 | Tag \_NNFSE não encontrada. | Verificar com quem originou o XML. |  |
| COM036 | CT-e cancelado | Verificar CT-e e realizar as devidas modificações. |  |
| COM037 | CT-e rejeitado | Verificar CT-e e realizar as devidas modificações. |  |
| COM038 | Tag \_UFTOM não encontrada ou com conteúdo em branco. | Verificar com quem originou o XML. |  |
| COM039 | Valor total da prestação de serviço e valor a receber estão zerados. | Deve-se incluir o CT-e manualmente pelo MATA103 com uma TES parametrizada para permitir quantidade e valor zerado. |  |
| COM040 | NF-e cancelada |  |  |
| COM041 | NF-e rejeitada |  |  |
| COM042 | Existe mais de uma Empresa/Filial para este XML. | Selecione a Empresa/Filial deste XML através da rotina Reprocessar no Monitor do TOTVS Colaboração. |  |
| COM043 | Aliquota de imposto maior que 100% | Verificar com quem originou o XML. |  |
| COM044 | Documento de entrada existente no monitor | Processe o recebimento do documento de entrada NFE (F1/D1) para importar o CTE corretamente |  |
| COM045 | CTEOS cancelado | Verificar CTEOS e realizar as devidas modificações. | A partir de 13/12/19. |
| COM046 | CTEOS rejeitado | Verificar CTEOS e realizar as devidas modificações. | A partir de 13/12/19. |
| COM047 | Documento CT-e complemento de imposto não é tratado pelo Importador XML | Gere o documento complemento manualmente através da rotina documento de entrada. |  |
| COM048 | Inconsistência na importação do CT-e | Verifique no SIGAGFE (GFEA118) |  |
| COM049 | Tag \_NFEPROC não encontrada no XML da NF-e | Verifique o XML | A partir de 24/07/20 |
| COM050 | Não foi possível converter para 1ª unidade de medida, pois o produto não possui fator de conversão. | Preencha o fator de conversão | XML recebido em segunda unidade medida |
| COM051 | Código de município inexistente | Verificar existência na tabela CC2 (Municípios) |  |
| COM052 | XML não pertence ao grupo de empresas | Verificar se XML esta correto. | A partir de 24/02/21 |
| COM053 | Não há cadastro de conversão da unidade **"Unidade de Medida"** para o produto **"Produto"**. O cadastro é obrigatório quando MV\_CSDXML = .T." | Verificar no cadastro de produto x fornecedor (**A5\_UNID**) esta preenchido e o cadastro do Fator de Conversão de Unidade de Medida (**ESTA0001**) | Mais detalhes na documentação sobre o consolidador XML: [Consolidador XML](https://tdn.totvs.com/display/public/PROT/IX11+-+Consolidador+XML+-+SEFAZ+AM#cabecalho-Fator%20de%20Convers%C3%A3o) |
| COM055 | NFe importada e cancelada | Verifique se o arquivo importado, gerou pré-nota ou documento de entrada. O documento deve ser avaliado e tomada as devidas providencias de acordo com o processo interno. |  |
| COM056 | CTe/CTeOS Importada e cancelada | Verifique se o arquivo importado, gerou pré-nota ou documento de entrada. O documento deve ser avaliado e tomada as devidas providencias de acordo com o processo interno. |  |
| COM057 | NFSe importada e cancelada | Verifique se o arquivo importado, gerou pré-nota ou documento de entrada. O documento deve ser avaliado e tomada as devidas providencias de acordo com o processo interno. |  |
| COM058 | NFSe rejeitada | Verifique se o arquivo importado, gerou pré-nota ou documento de entrada. O documento deve ser avaliado e tomada as devidas providencias de acordo com o processo interno. |  |
| COM059 | Layout de XML de NFe estão fora dos padrões para importação | Verificar com quem originou o XML. |  |

***Saiba Mais :***

[IX06 - Erros (Códigos)](https://tdn.totvs.com/x/q8b1H)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML)

[TOTVS Colaboração - Guia de Referencia (SIGACOM)](https://tdn.totvs.com/pages/releaseview.action?pageId=271661626)

[Importador XML - Guia de Referencia (SIGACOM)](https://tdn.totvs.com/pages/viewpage.action?pageId=485858148)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
