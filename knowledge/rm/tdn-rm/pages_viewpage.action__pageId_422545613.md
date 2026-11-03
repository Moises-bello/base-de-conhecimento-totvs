---
content_hash: c25b4d5107f09744c4059ed099ef4ad54fa78c2743a409707e5dad67ad53b7bd
fetched_at: '2026-06-29T00:09:19.566749+00:00'
page_id: '422545613'
product: rm
source: tdn-rm
title: DAPI (Pasta Identificação)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545613
version: 10
---

A edição de alguns campos desta pasta irá depender do ramo de atividade da Filial que irá gerar o arquivo, campo informado no Cadastro de Filial, nos Dados Fiscais / Outros Dados e do Período de Referência informado na geração da DAPI.  
 Informe os seguintes campos:

**Arquivo Texto**: Informe neste campo, o nome do arquivo onde será gerada a DAPI, o sistema já traz como default a denominação DAPI.TXT.

**Filial**: Informe a filial que terá suas informações geradas na DAPI.

**Referência**: Informe o período a que se refere a DAPI.  
 ***Observação***: Este período já deverá estar cadastrado em Obrigações Principais | Períodos de Apuração.

**Data Limite Pagamento**: Informe a data limite para pagamento do ICMS sem multa (data vencimento).

**Regime Recolhimento**: Informe o regime de recolhimento sujeitos entrega da DAPI. As Opções são:

|  |  |
| --- | --- |
| **Código** | **Regime** |
| 01 | Débito/ Crédito |
| 03 | Isenta ou Imune |
| 29 | Microprodutor Rural (Pessoa Jurídica) |
| 30 | Produtor Rural de Pequeno Porte (Pessoa Jurídica) |
| 40 | Microempresa |
| 41 | Microempresa Inscrição Coletiva |
| 42 a 51 | Empresa de Pequeno Porte - de Faixa 1 a Faixa 10 |

**CAE / Desmembramento**: Informe o código de Atividade Econômica que o contribuinte esta enquadrado no período de referência da DAPI, complementando, se necessário, o Desmembramento do CAE especificado;   
 ***Observação***: Caso não seja necessário complementar o CAE com o código do Desmembramento deixar o campo em branco.

**Destino**: Drive onde será gerado o arquivo.

**Modelo DAPI**: Informe o Modelo DAPI a ser gerado. As opções são:

|  |  |
| --- | --- |
| DAPI 1 | Débito e Crédito, Isento ou Imune, Microprodutor Rural nos termos do Inciso II, art. 9º do Anexo VIII do   RICMS/96 ou Produtor Rural pequeno porte. |
| DAPI2 | Microempresa ou Microempresa Inscrição Coletiva. |
| DAP 3 | Empresa de Pequeno Porte |

**Distribuidor, Atacadista ou Depósito com Regime Especial ST**: Marcando essa opção o sistema estará gerando o Campo 76. Se não marcar o sistema estará gerando o Campo 85 com as mesmas informações.

**DAPI Consolidada**: Habilitando esse campo o sistema gera uma única DAPI selecionando os Lançamentos Fiscais e de Outros Débitos e Créditos das Filiais que possuem mesma Inscrição Estadual e UF da Filial selecionada na tela da rotina.

* **Observações Gerais**

**Campo 76 - Base de Cálculo ST:**Base Tributada ST das operações de saídas internas, se os campos Base Tributada ST e Valor ST forem maior que zero. Estará recebendo também a Base Tributada ST de todas as operações de entrada com Valor ST maior que zero, o Tipo ICMS igual a "ST Retido na Compra", o campo Contribuinte Credenciado, localizado na Tela de Subst. Tributária, está habilitado e o campo Distribuidor, Atacadista ou Depósito com Regime Especial ST nessa tela encontra-se habilitado.

**Campo 77 - Valor Retido:**Valor ST das operações utilizadas para o cálculo do campo 76.

**Campo 85 - Base de Cálculo ST:**Base Tributada ST de todas as operações de entrada com Valor ST maior que zero, o Tipo ICMS igual a "ST Retido na Compra", o campo Contribuinte Credenciado, localizado na Tela de Subst. Tributária, está habilitado e o campo Distribuidor, Atacadista ou Depósito com Regime Especial ST nessa tela encontra-se desabilitado.

**Campo 86 - Valor Retido:**Valor ST das operações utilizadas para o cálculo do campo 85.
