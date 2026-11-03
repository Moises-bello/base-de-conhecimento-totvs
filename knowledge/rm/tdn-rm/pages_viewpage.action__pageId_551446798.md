---
content_hash: 8b76a0b5fdda53a910eae506c5ac5b0b33343cb3d238bb428d9e3db908cc21b5
fetched_at: '2026-06-29T00:10:43.993446+00:00'
page_id: '551446798'
product: rm
source: tdn-rm
title: NF-e de Ajuste - Estorno de Crédito - Art. 6° e 7 da Resolução SEFAZ MG 5.029/2017
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=551446798
version: 4
---

# Estorno de Crédito

O Imposto sobre Circulação de Mercadorias e Serviços de Transporte e Comunicação – ICMS é um imposto não cumulativo. Significa dizer que o contribuinte poderá compensar o imposto cobrado em operações anteriores, na forma de créditos, com o imposto devido por suas próprias operações. Este documento visa dar orientações conforme disposto na resolução SEFAZ MG 5.029/2017 sobre as parametrizações necessárias para realizar o Estorno de Crédito.

# Cadastros

O Cadastro da CFOP  *5.949*deverá ser realizado da seguinte forma:

Na aba Outros Dados na opção **Tipo de Operação** marcar a opção ***Natureza de Ajuste**.*

*Obs: A CFOP deve ser associada ao movimento e replicada para o item.*

# Movimento

Observação, é recomendado a criação de um tipo de movimento especifico para essa situação:

* No quadro “Destinatário/Remetente”, o nome do próprio contribuinte, o endereço e os números de inscrição estadual e no Cadastro Nacional de Pessoa Jurídica (CNPJ);

Acessar os parâmetros do tipo de movimento em : Ambiente | Parâmetros | Gestão de Estoque , Compras e Faturamentro | Parametrizar o movimento desejado

***Etapa Mov - Emitente/Destinatário 1/2***

***Emitente*** = Empresa

***Destinatário*** = Empresa

* No quadro “Dados Adicionais”, no campo “Informações Complementares” a observação: “Estorno de crédito - Estoque - Crédito Presumido, nos termos do art. XX do regime especial e-PTA n. 45.xxx-xx - art. 6º da Resolução nº 5029/2017”, se o crédito presumido for concedido através de e-PTA, ou “Estorno de crédito - Estoque - Crédito Presumido - art. 6º da Resolução nº 5029/2017”, nos demais casos;

***Etapa Mov - Campos Livres 1/2***

***Preencher Fórmula em:**Informações Adicionais do Contribuinte*

***Fórmula de Preenchimento Histórico:*** *Vincular uma fórmula que contenha o texto indicado acima conforme sua regra de negócio.*

* No quadro “Dados do Produto”, o valor integral por extenso do estorno de crédito e o respectivo valor numérico no campo “Valor Total Bruto do Produto”, que será totalizado no campo “Valor Total da Nota”;

No item de movimento:

*Em Cabeçalho informar o valor e quantidade do item:*

*Em Integrações Fiscais informar o valor por extenso do item:*

# NF-e

Na NF-e será gerado as seguintes tags:

Geração da DANFE:

# Escrituração

No processo de escrituração do movimento que possui o tributo ICMS:

| Lançamento: |
| --- |

**SPED:**

|  |
| --- |
