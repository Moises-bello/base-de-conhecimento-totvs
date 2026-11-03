---
article_id: 360006564072
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: cd8407bf92e6d589d8f89ad4c6fd63553eae6fe72fe0516fec6d47949dc420b7
fetched_at: '2026-06-28T22:40:47.490929+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBS001 - ECF - Parâmetros
  de Integração do módulo contábil para o módulo do TAF
type: support-article
updated_at: '2023-10-31T18:34:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006564072-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-Par%C3%A2metros-de-Integra%C3%A7%C3%A3o-do-m%C3%B3dulo-cont%C3%A1bil-para-o-m%C3%B3dulo-do-TAF
---

**Ocorrência**Ao efetuar a integração do CTB para o TAF, é apresentada a mensagem: "Erro na transferência de dados...". Caso a TAFST2  não seja populada.  
  
**Ambiente**

Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – 12.1.17.

**Causa**Configuração incorreta dos parâmetros de integração.

**Solução**

Ajustar os parâmetros de integração conforme abaixo:

* MV\_TAFTALI = "Deve ser informado no nome do TOPALIAS do seu ambiente dentro do appserver.ini"
* MV\_TAFTDB = "Deve ser informado nome do banco do seu ambiente Exemplo MSSQL ou MSSQL7 informado no seu TOPBASE dentro do appserver.ini"
* MV\_TAFPORT - Indica o número da porta do serviço do TopConnect
* MV\_TAFVER - Release corrente do TAF
* MV\_TAFWIZ =.T. (A letra 'T' deve ser maiúscula)
* MV\_TAFINT = .T. (A letra 'T' deve ser maiúscula)
* MV\_TAFQPRC - Alterado rotinas de processamento para utilizar a Clausula de Limitação de Registros somente quando o parâmetro MV\_TAFQPRC estiver configurado com um número maior que 0, consequentemente para inibição da Cláusula deve-se preencher o parâmetro com 0.
* Deve ser configurado 0 ou 9999999 , se estiver configurado com 1 o sistema só irá integrar um registro na TAFST1 , se estive com 0 o sistema irá inibir a clausula de limitação
* <http://tdn.totvs.com/pages/releaseview.action?pageId=185752114>
* <http://tdn.totvs.com/display/TAF/Complemento+de+Empresa+-+TAFA050+-+TAF+-+P12>
* Verificar o cadastro do complemento de empresa
* [MV\_VAUTCON](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006985071-MP-SIGATAF-Como-realizar-a-atualiza%C3%A7%C3%A3o-das-Tabelas-Autocontidas-no-TAF-)  = para atualizar a autocontida deixe o parâmetro  EM BRANCO. Acessar sistema para carregar as **Autocontidas " Taf atualizações/ Wizard Configuração"** , ao concluir o processo o sistema irá preencher o parâmetro automaticamente

Exemplo :

* Através da APSDU obter as informações abaixo

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085926493)

* Parâmetros foram preenchidos com base nos dados anterior

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084734554)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085926993)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084734694)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084734774)

* Campo Filial TAF: Faz um consulta ao cadastro de filiais ( SM0 ) do sistema. Neste campo deverá ser preenchido a filial correspondente do TAF de destino das informações integradas dos ERP's.

  Campo Cod. Filial: Neste campo será informado o código da filial de origem dos dados de integração. O conteúdo deste campo deve ser idêntico ao conteúdo do campo TAFFIL das tabelas de integração ( TAFST1 e TAFST2 ).
* [Complemento de Empresa - TAFA050 - TAF - P12](http://tdn.totvs.com/display/TAF/Complemento+de+Empresa+-+TAFA050+-+TAF+-+P12#samples-4)
* [Associe\_as\_obrigacoes\_fiscais\_a\_um\_Complemento\_de\_Empresa](http://tdn.totvs.com/display/public/PROT/ECF0017_Associe_as_obrigacoes_fiscais_a_um_Complemento_de_Empresa)

![COMPLEMENTO.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360007711211)![COMPLEMENTO__2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360007711291)
