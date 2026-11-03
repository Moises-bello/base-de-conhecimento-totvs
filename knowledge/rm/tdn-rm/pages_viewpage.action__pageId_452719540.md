---
content_hash: ed3081469b73973fc2ab8c018c4bd33b1764539323e5376ebb9e7e4ae459ca36
fetched_at: '2026-06-29T00:10:08.576692+00:00'
page_id: '452719540'
product: rm
source: tdn-rm
title: Processos Jurídicos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719540
version: 2
---

**Processos Jurídicos**

---

O cadastro de Processos Jurídicos, é um centralizador de diversas informações, tais como fóruns, varas, reclamações, advogados, documentos, audiências, depósitos recursais, dentre outros.

Este tem como objetivo, controlar e acompanhar os processos trabalhistas movidos contra ou pela coligada corrente, bem como os custos, as empresas e todas as pessoas envolvidas com estes processos.

**Pasta Identificação:**

Nesta pasta serão cadastradas as principais informações relativas ao processo trabalhista.

Nesta tela do processo jurídico se registra dados de identificação, o número do processo é a informação mais importante.

Define-se em qual fórum está o processo juntamente com qual vara será responsável pelo acompanhamento. A data de abertura, data de reclamação, data de encerramento, representante e tipo de processo são dados indispensáveis neste cadastro.

O representante se refere a uma empresa, entidade terceirizada pela empresa reclamada.

A data de abertura do processo é literalmente a data em que se originou o protocolo, a data de reclamação define em que data o reclamante levantou o seu protesto contra a empresa e a data de encerramento, valor informado no final do processo, marca a data de conclusão de todo o processo.

O tipo de processo informado tem a função de agrupar os vários processos que a empresa possa vir a ter, processos de reclamatória, processos de abertura de falência, por exemplo.

Para que os processos possam ser selecionados no eSocial, deverá ser marcado o parâmetro "Processo da empresa contra órgão governamental envolvido no eSocial".

Deverá ser definido qual o indicativo da matéria do processo ou alvará judicial.

**Campos Complementares:**

Campos complementares são campos que criados dentro do aplicativo, depois de todas as tabelas principais do sistema já terem sido criadas. Eles têm como objetivo complementar informações de um cadastro, com os dados que você desejar e da maneira que desejar.

**Atenção:**

O número do processo jurídico é composto por 20 caracteres numéricos no formato "NNNNNNN-DD.AAAA.J.TR.OOOO". Esta formatação se dá com base na Resolução 65 de 16 de Dezembro 2008:

Fonte: [{\_}{+}](http://www.cnj.jus.br/images/stories/docs_cnj/resolucao/rescnj_65.pdf)<http://www.cnj.jus.br/images/stories/docs_cnj/resolucao/rescnj_65.pdf+_>

NNNNNNN - Número sequencial do Processo, por Unidade de Origem, a ser reiniciado a cada ano

DD - Dígito Verificador

AAAA - Ano do ajuizamento do Processo

J - Órgão ou Segmento do Poder Judiciário

TR - Tribunal do respectivo Segmento do Poder Judiciário

OOOO - Unidade de origem do Processo (Varas)

Exemplo:

Código de processo: 20802520125150049 Na formatação são acrescentados zeros à esquerda de modo a ficar 00020802520125150049. Quando aplicado na máscara seu formato seria 0002080-25.2012.5.15.0049

A Regra de Validação de um número de processo jurídico se dá no Dígito Verificador. O dígito verificador de um processo é calculado com base em um cálculo: 98 menos o resto de (NNNNNNNAAAAJTROOOO x 100 ÷ 97).

Este resultado confirma o número do DV, com dois dígitos. A forma de cálculo é conhecida como "Módulo 97, Base 10, ISO 7064".

**Observação:**

O sistema não realiza nenhuma consistência sobre o código do processo, cabendo ao usuário a responsabilidade pela entrada correta da informação. Qualquer caractere que seja informado de maneira equivocada, ao enviar ao governo, incidirá em um cálculo que poderá entender o dígito verificador diferente do correto.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Fases do Processo Audiências Intimações/Controle de Prazos Perícias Bens Penhorados Despesas por Processo Depósitos Recursais Documentos Reclamado Reclamante  
Suspensão de exigibilidade de tributos e FGTS devido processo judicial  
 

|  |  |
| --- | --- |
|  | Como Fazer |

---

Calcular Fórmulas Reajustar Valores de Depósitos Enviar Email

|  |  |
| --- | --- |
|  |  |
