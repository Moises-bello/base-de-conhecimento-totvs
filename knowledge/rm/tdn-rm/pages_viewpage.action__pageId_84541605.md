---
content_hash: 87643cb615bd30838d433fb0f6f631b728225b11385af1791f7a1a0b12c83f0c
fetched_at: '2026-06-29T00:11:50.738580+00:00'
page_id: '84541605'
product: rm
source: tdn-rm
title: Apuração IRRF Importação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=84541605
version: 4
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                       **Versão:**11.52 |
| **Processo** | **:** | Apuração de Tributos |
| **Subprocesso** | **:** | Geração de Guia Automática para o tributo IRRF Importação |
| **Data da publicação** | **:** | 17/09/2013 |

***Definição do Processo***

O objetivo deste documento é oferecer orientações sobre a implementação realizada no TOTVS Gestão Fiscal para a apuração do tributo IRRF importação.

***Regras Gerais***

O sistema de Gestão Fiscal foi alterado para tratar a apuração do tributo IRRF Importação. Esse tipo de tributo deve ser utilizado em lançamentos fiscais para a retenção de imposto de renda cujo beneficiário seja do exterior.

***Parametrização Necessária:***

**1.****Cadastro do Tributo**

Foi criado o Tipo de Tributo "IRRF Importação". Esse tipo de tributo deve ser utilizado em lançamentos fiscais para a retenção de imposto de renda cujo beneficiário seja do exterior. Este tributo deve ser criado com a periodicidade diária e devem ser inseridos períodos de apuração correspondentes a esta periodicidade.

**Cadastro do Cliente/Fornecedor**

Foi criado um campo para informação do Número de Identificação Fiscal - NIF e outro campo para informar o motivo para o não preenchimento do NIF com as seguintes opções:

                a) Beneficiário dispensado do NIF

                b) País não exige NIF               

Esses campos serão apresentados somente se o Estado informado no cadastro do Cliente/Fornecedor for estrangeiro

**Cadastro do Cliente/Fornecedor | Tributo do Lançamento Fiscal | Tributo do Movimento**

Foram criados campos para informação do "Tipo de Rendimento" e "Forma de Tributação" que serão utilizados como *defaults* nos Lançamentos Fiscais e Movimentos, com as seguintes listas:

                a) Tipo de Rendimento:

                               100 - Rendas de propriedade imobiliária

                               110 - Rendas do transporte internacional

                               120 - Lucros e dividendos distribuídos

                               130 - Juros

                               140 - Royalti

 150 - Ganhos de capital

                               160 - Rendas do trabalho sem vínculo empregatício

                               170 - Rendas do trabalho com vínculo empregatício

                               180 - Remuneração de administradores

                               190 - Rendas de artistas e esportistas

                               200 - Pensões

                               210 - Pagamentos Governamentais

                               220 - Rendas de professores e pesquisadores

                               230 - Rendas de estudantes e aprendizes

                               300 - Outras rendas

b) Forma de Tributação:

                               10 - Retenção do IRRF - alíquota padrão

                               11 - Retenção do IRRF - alíquota da tabela progressiva

                               12 - Retenção do IRRF - alíquota diferenciada (países com tributação favorecida)

                               13 - Retenção do IRRF - alíquota limitada conforme cláusula em convênio

                               30 - Retenção do IRRF - outras hipóteses

                               40 - Não retenção do IRRF - isenção estabelecida em convênio

                               41 - Não retenção do IRRF - isenção prevista em lei interna

                               42 - Não retenção do IRRF - alíquota zero prevista em lei interna

                               43 - Não retenção do IRRF - pagamento antecipado do imposto

                               44 - Não retenção do IRRF - medida judicial

                               50 - Não retenção do IRRF - outras hipóteses

***Como fazer geração da rotina***

Criar um período de apuração do tributo IRRF  Importação, ao encerrar o período o sistema não irá calcular o Saldo *Credor/Devedor* do tributo, isto porque o tributo é pago ao se registrar cada nota fiscal de importação. O saldo devedor será atualizado a cada geração de guia, equivalente a soma das guias *DARF's* geradas.

No menu Processos realizar a Geração automática das Guias.

A seleção dos Lançamentos Fiscais para geração das guias será feita à partir do campo "Data do Desembaraço", localizado na pasta Exterior do Lançamento Fiscal. Serão selecionados lançamentos fiscais de entrada que possuem o tributo informado na pasta Outros Tributos

Para maiores informações:

 [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)

**COMUNIDADE **[R@Fiscal](https://totvs.byyou.com/?space=rfiscal)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
