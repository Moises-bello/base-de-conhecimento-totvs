---
content_hash: f0fefd9adfae1ca23de0e23866a21fc509d827720fa289cd65c6e2e612e171ae
fetched_at: '2026-06-29T00:08:43.764065+00:00'
page_id: '306839706'
product: rm
source: tdn-rm
title: MATFATCMPCRM01-1358 DT CT-e versão 3.00
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=306839706
version: 112
---

# Conhecimento de Transporte Eletrônico 3.00

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Gestão de Estoque, compras e faturamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Parâmetros de CT-e por Filial* | *MovFilialCTeParamsForm* | | Tela de Edição do Movimento | MovMovimentoForm | |
| **Cadastros Iniciais:** | *N/A* |
| **Parâmetro(s):** | Parâmetros → Gestão de Estoque, Compras e Faturamento → Integração → Fiscal → Dados Fiscais → Parâmetros por Filial → Ambiente CT-e |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | *N/A* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MATFATCMPCRM01-1358 |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQLServer e Oracle* |
| **Tabelas Utilizadas:** | *TPARFILIAL* |
| **Sistema(s) Operacional(is):** | *Windows* |
| **Releases Disponíveis** | 12.1.16.181 12.1.17.194 12.1.18.124 |

## **Documentação Adicional**

Informações adicionais sobre o funcionamento do CT-e podem ser encontrados no Manual do CT-e que pode ser adquirido em <http://www.cte.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=bx74pJ8hXaM=>

Para informações sobre o **Evento de Prestação em Desacordo**, consultar [MATFATCMPCRM01-2050 DT PRESTAÇÃO DE SERVIÇO EM DESACORDO](http://tdn.totvs.com/pages/viewpage.action?pageId=351017018)

**Importante:**

**- Além da atualização da release é necessário executar o script EXECSQL.TOTVSGESTESTCOMPFAT disponível na Central de Downloads. Junto com o script também foi disponibilizado o relatório DACTE que deverá ser importado.**

**- Ao atualizar a release é necessário atualizar o parâmetro Versão do CT-e para que a emissão possa ser feita.**

**Parâmetros**

Com o objetivo de evitar erros durante o processo de implantação do CT-e, foram realizadas as seguintes melhorias nos parâmetros por filial:

1- Foram **removidos** os seguintes campos da tela de parâmetros de CT-e:

* Versão Modal Aéreo
* Versão Modal Aquaviário
* Versão Modal Ferroviário
* Versão Modal Rodoviário

Observação: Somente o modal Rodoviário está sendo atendido neste momento.

2- O componente utilizado no parâmetro **Versão do CT-e** foi substituído, esta informação era preenchida através de uma caixa de texto, a qual foi substituída por um componente de seleção, desta forma não será possível informar uma versão inexistente/descontinuada.

Observações:

1. A partir da versão 3.00, o sistema utilizará a mesma versão do CT-e para os modais já atendidos pelo sistema.

2. Para as informações já contidas na base, a tela exibirá o campo em branco e, apenas a opção **3.00** estará disponível.

**Cadastros**

Para que não ocorram erros no envio, deverão ser revisados alguns cadastros, de acordo com o seu papel no CT-e. Segue detalhamento abaixo:

1- Emitente do CT-e

No cadastro da filial emitente do CT-e, deverá ser informado o Registro ANTT (RNTRC) da filial, conforme a figura abaixo:

2- Tomador

O tomador do CT-e pode ser um cliente/fornecedor ou uma filial. Em ambos os casos, é necessário que o tipo de contribuinte ICMS esteja devidamente informado no cadastro do tomador.

Cadastro de Cliente/Fornecedor

Cadastro de Filial

Existem três tipos de contribuintes de ICMS:

* Contribuinte ICMS
* Contribuinte Isento de Inscrição no Cadastro de Contribuintes do ICMS
* Não Contribuinte, pode ou não possuir IE no Cadastro de Contribuintes do ICMS

Para o envio do CT-e é importante observar o seguinte:

* Quando o tipo de contribuinte ICMS for “Contribuinte ICMS”, é necessário que esteja devidamente informado no cadastro deste tomador o CNPJ e a Inscrição Estadual.
* Quando o tipo de contribuinte ICMS for “Contribuinte Isento de Inscrição no Cadastro de Contribuintes do ICMS”, é necessário que esteja devidamente informado no cadastro deste tomador o CNPJ e a Inscrição Estadual seja igual a “ISENTO”.
* Quando o tipo de contribuinte ICMS for “Não Contribuinte, pode ou não possuir IE no Cadastro de Contribuintes do ICMS”, é necessário que esteja devidamente informado no cadastro deste tomador um CPF e a Inscrição Estadual não pode estar preenchida.

**Movimento**

Na aba Remetente Destinatário:

* Foi incluída a opção Diversos no grupo remetente.
* Foi criado um novo campo "TMOVTRANSP.OBSGLOBALIZADO", o qual será habilitado ao selecionar a opção "Diversos" do grupo remetente ou destinatário.

Consistências:  
Caso seja informada a opção "diversos" em ambos os grupos "Remetente e Destinatário", o sistema deve exibir a seguinte mensagem de consistência:

Observação: Quando o Remetente for do tipo "Diversos", o tomador do CT-e deve ser o destinatário. Quando o Destinatário for do tipo "Diversos", o tomador do CT-e deve ser o remetente. Caso isso não seja observado, ao fazer o envio a SEFAZ retornará um erro.

Na aba Ct-e:

Foram removidos os seguintes grupos para CT-e na versão 3.00:

* Motorista
* Seguro de Carga
* Carga Perigosa

O Campo "**TCTEDOC.TIPODOCORIGINARIO**" foi ajustado e passa a permitir os seguintes valores:

* 07- ATRE  ,
* 08- DTA (Despacho de Transito Aduaneiro),
* 09- Conhecimento Aéreo Internacional,
* 10- Conhecimento - Carta de Porte Internacional,
* 11- Conhecimento Avulso,
* 12- TIF (Transporte Internacional Ferroviário)
* 13- Bill of Lading (Conhecimento de Embarque Marítimo)
* 99- Outros

Os campos "**TMOVTRANSP.CIOT**" e "**TMOVTRANSP.LOTACAO**" foram descontinuados e consequentemente não serão exibidos na tela do movimento.

**Evento - Carta de Correção**

A partir da implementação do leiaute 3.00 do CT-e, a relação de campos utilizados para o Evento de Carta de Correção sofreu pequenas alterações, sendo alguns destes campos excluídos ou incluídos.

Campo incluído:

Grupo: Informações do CT-e Globalizado / Campo: Observação.

Corresponde à área de texto localizada na aba CTRC | Remetente e Destinatário, quando o tipo de um deles é marcado como 'Diversos'.

Campos excluídos:

Todo o grupo "Local de Coleta";  
Todo o grupo "Local de Entrega";  
Todo o grupo "Veículos";  
Todo o grupo "Seguro de Carga";  
Todo o grupo "Produtos Perigosos (Classificação da ONU)";  
Todo o grupo "Motorista";

Campo 'Código Identificador da Operação de Transporte', dentro do grupo "Rodoviário - Informações do Modal";  
Campo 'Data prevista para a entrega',  dentro do grupo "Rodoviário - Informações do Modal";  
Campo "Forma de Pagamento", dentro do grupo "Identificação".

Obs.: O campo 'Chave de Acesso', do dentro do grupo "Nota Fiscal Eletrônica" não pode mais ser alterado.

divs
