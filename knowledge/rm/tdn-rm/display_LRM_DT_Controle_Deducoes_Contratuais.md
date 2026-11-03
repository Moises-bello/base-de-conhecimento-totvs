---
content_hash: f1ac76379c39c79eb1d4becdc2872c485cd391565772de517353f8e800a43f82
fetched_at: '2026-06-29T00:06:06.219244+00:00'
page_id: '201729316'
product: rm
source: tdn-rm
title: DT_Controle_Deducoes_Contratuais
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Controle_Deducoes_Contratuais
version: 6
---

# CONTROLE DE DEDUÇÕES CONTRATUAIS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Requisito (ISSUE):** | PCREQ-5375 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Oracle/SQL |
| **Tabelas utilizadas:** | TMOV – Movimentos    TTMV – Tipos de Movimentos |
| **Sistema(s) operacional(is):** | Windows 7 SP1 ou superiores. |
| **Versões/Release:** | 12.1.7 |

## Descrição

 Permitir que o usuário utilize o Controle de Deduções Contratuais.

 

**Desenvolvimento/Procedimento**

 

 Uma dedução de contrato pode ser identificada de N formas através do “detalhamento de itens de retenção”, no entanto podem ser generalizadas em três categorias de deduções:

* Dedução de Adiantamento
* Dedução de Itens de Compra Direta (**compra** de material)
* Outras Deduções

 O faturamento de um contrato de prestação de serviços do segmento de Construção pode ter quatro tipos de reduções:

* **Retenção Técnica** consultar boletim técnico $/RM.Net/Docs\_Proj/Roadmap\_2013\_2014/Construcao\_e\_Projetos/Materiais/R\_MOV006/Documentacao/12.1.6/MOV\_BT\_ControleRetencoesContratuais\_BRA\_PCREQ-5372.docx
* **Despesas ou Débitos não fiscais** como: despesas com alimentação, transporte, combustível, dentre outras.  Que não são abatidos do valor do serviço, mas sim descontados no momento do pagamento. Seria um acordo gerencial entre as partes.
* **Deduções Fiscais**, que são aquelas previstas por lei, na qual podem ser abatidas da base de cálculo do ISS valores gastos com material aplicado na construção e com sub empreitada, cujo serviço já foi tributado quando da emissão da nota fiscal de faturamento.
* **Adiantamento:** Na gestão de Materiais já existe um processo de Controle de Adiantamento. Porém,  o controle atual de adiantamento não atende o TOP, por restringir apenas o vínculo entre NFs. Dessa forma o adiantamento será enviado como uma despesa do movimento. A utilização de controle de adiantamento através do TOP será incluída em RoadMap futuro.

 

**Despesas ou Débitos de contrato**

* As Despesas ou Débitos apurados pelo TOP seram enviados para o campo de **Desconto** do movimento.
* O controle e o demonstrativo dos valores lançados como Despesas do Contrato são feitos pelo TOP.

 A parametrização necessária para utilizar este processo é no módulo **Gestão de Estoque, Compras e Faturamento**, acessar o menu **Ambiente >> Parâmetros >> Gestão de Estoque, Compras e Faturamento** selecionar o tipo de movimento e na **Etapa Mov – Valores Financeiros 1/4** marcar o parâmetro **Desconto** e informar o **Tipo de Desconto(Percentual, Valor** ou **Ambos)**.

 

 **Informações Adicionais**

 

**Dedução de produtos faturados no contrato**

 Quanto ao processo de Dedução de produtos faturados no contrato, no qual pode-se relacionar um movimento (item) a um contrato do TOP, informo que o mesmo é uma recurso que facilita a apuração dos valores de redução por parte do TOP. Ele não interfere nos processos do BackOffice e dependendo da definição dos processos de cada cliente pode ser utilizado pra extrair informações gerenciais.

 

**Deduções Fiscais**

  O escopo dessa implementação não contempla as Deduções Fiscais previstas por lei.
