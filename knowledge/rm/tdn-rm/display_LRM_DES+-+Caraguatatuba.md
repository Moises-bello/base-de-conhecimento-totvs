---
content_hash: 90769fcc97f7836edc9852203351c41ec2fe546e61cec89ea4be8eaf9bfca400
fetched_at: '2026-06-29T00:11:53.974900+00:00'
page_id: '852891234'
product: rm
source: tdn-rm
title: DES - Caraguatatuba
type: documentation
url: https://tdn.totvs.com/display/LRM/DES+-+Caraguatatuba
version: 13
---

# Conteúdo

## 2Conteúdo

# 1. Introdução

 A DES é uma rotina municipal cujo objetivo é informar a prefeitura o registro dos serviços prestado e contratados pelas pessoas jurídicas para que possam gerenciar de forma eficaz, o recolhimento do Imposto sobre Serviços de Qualquer Natureza – ISSQN. Neste documento iremos demonstrar o processo para a extração das informações no Gestão Fiscal para a geração do arquivo e importação no portal da prefeitura de Caraguatatuba no link  <https://caraguatatuba.meumunicipio.online/ISS/contribuinte/login.php> 

Neste processo o foco é a geração das informações dos serviços tomados e acobertados por documentos fiscais e sujeitos à incidência do ISSQN.

Glossário de termos técnicos e siglas:

* **DES** - Declaração Eletrônica de Serviços.
* **ISSQN** - Imposto sobre Serviços de Qualquer Natureza.
* **NFS-e** - Nota Fiscal de Serviço Eletrônica.

# 2. Regras Gerais

 O DECRETO Nº 1.584, DE 26 DE JANEIRO DE 2022  Institui o novo Sistema Eletrônico de Gestão do ISSQN, estabelece obrigações acessórias relativas ao ISSQN – Imposto Sobre Serviços de Qualquer Natureza e dá outras providências.

Em substituição aos livros fiscais previstos na legislação vigente,todo prestador que emita nota fiscal de prestação de serviços e todo tomador de serviços ficam obrigados a escriturar eletronicamente, por meio do programa SIG ISS, os fatos geradores do ISSQN, por meio do preenchimento dos seguintes livros  
fiscais:  
I – Livro de Registro de Prestação de Serviços; e  
II – Livro de Registro de Serviços Tomados de Pessoas Físicas e Jurídicas.

Neste processo de extração dos dados para a geração das informações a prefeitura iremos gerar eletronicamente as informações para atender ao  Livro de Registro de Serviços Tomados de Pessoas Físicas e Jurídicas.

# 3. Geração do arquivo

A geração da DES deve ser executada a partir de Obrigações Acessórias | Gerador de Saídas. Sendo necessário obter o layout mais recente do arquivo "FISLAY0032 - DES-Caraguatatuba-SP.TotvsGen" pelo TOTVS Compartilhamento.

O arquivo é gravado no diretório selecionado na tela de geração.

Para a geração do arquivo, devem ser informados:

* Filial;
* Período: Data inicial e final dos lançamentos a serem considerados. Lembrando que se trata de uma rotina mensal;
* Classificações que serão utilizadas para codificação do Município e para o País;
* Gerar Centralizada: Ao marcar este parâmetro, o sistema irá considerar lançamentos de entrada das filiais que possuem a mesma Inscrição Municipal e o mesmo município da filial selecionada. Desmarcado, será gerado apenas informações da filial informada.

As guias de recolhimento do ISSQN deverão ser geradas e obtidas pelos contribuintes e responsáveis tributários por meio do software da DES.

# 4. Seleção de Lançamentos

A seleção dos Lançamentos Fiscais de Entrada serão feitos conforme os parâmetros informados no TOTVS Gestão Fiscal (Processo 03.02 - "Apuração de Tributos" → 03.02.03 - "ISS" → "Apur. por Filial" **→** Datas Apuração do ISS). As opções são:

* Data de Emissão;
* Data de Entrada/Saída;
* Data de Pagamento/Vencimento.

Utilizando a opção "Data de Pagamento/Vencimento", o sistema se comportará da seguinte forma:

* Se existir integração com sistema de Gestão Financeira, serão selecionados os Lançamentos Fiscais cujo Lançamento Financeiro associado esteja baixado no período informado na tela da rotina (Data de Baixa);
* Se não existir integração com sistema de Gestão Financeira, serão selecionados os Lançamentos Fiscais cuja Data de Vencimento (aba "Dados Financeiros") esteja no período informado na tela da rotina.

Essa parametrização deve ser feita para operação de Entrada.

***Importante!*** Se a Filial estiver parametrizada para utilizar município por item, as informações de Alíquota, Tipo de Recolhimento, Base de Cálculo e Valor do Imposto serão preenchidos conforme os dados informados na aba "Outros Tributos" dos Itens do Lançamento Fiscal. Se a Filial for parametrizada para não usar o município por item, esses campos serão preenchidos conforme os dados informados na aba "Outros Tributos" do Lançamento Fiscal.

# 5. Registros

**Observação:** A geração do arquivo da DES pelo Módulo Fiscal da linha RM não inclui o registro 40 (Exclusivo para Instituição Financeira)

A geração dos demais Registros da DES será realizada conforme as regras seguintes:

registrosregistro-10Registro 102

### Registro Unico

|  |  |  |
| --- | --- | --- |
| **Posição** | **Campo** | **Origem dos Dados** |
| 01 | CNPJ do Prestador | Preencher com os dados do Cliente/Fornecedor associado ao Lançamento Fiscal |
| 02 | Numero Inicial da Nota | Número do Documento Inicial informado no Lançamento Fiscal. |
| 03 | Série da Nota | Série informada no Lançamento Fiscal. |
| 04 | Subsérie da Nota | Sub série informada no Lançamento Fiscal. |
| 05 | Dia da Emissão | Data de emissão informada no Lançamento Fiscal buscando somente o dia. |
| 06 | Código do Serviço | Verificar em tributos do município do produto o código do serviço senão buscar no lançamento. |
| 07 | Situação da Nota | Regras **Se** Tipo de Recolhimento **igual** **à** isento, **então** gerar com letra  I isento  **Senão, Se** Nota de Entrada cujo município do prestação for **diferente** do município da Filial, **então** gerar letra  N - Retido Fora  **Senão, Se** Nota de Entrada cujo município do prestação for **igual** do município da Filial **e** Município do prestador **diferente** do município da Filial **e** Tipo de Recolhimento **igual** Retido ou Retido deduzido , **então** gerar letra R - Retido no tomador **Senão, Se** Município do prestador **igual** ao município da Filial, **então** gerar letra T -Tributada no Prestador |
| 08 | Valor do Serviço | Busca do valor contábil do lançamento. |
| 09 | IM  Tomador | Busca no cadastro de filial a IM da filial do contexto. |
| 10 | Tipo de Nota | Fixo EL |
| 11 | Aliq. Simples Nacional | Fixo 000 |
|  |  |  |
|  |  |  |
|  |  |  |
