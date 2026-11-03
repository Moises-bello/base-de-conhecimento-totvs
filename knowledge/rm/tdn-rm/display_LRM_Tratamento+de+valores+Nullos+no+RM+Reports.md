---
content_hash: 021333c2c4a7d79f4f4a618f3fc8727ef9b8c97f7758816d9ea1c704a30fe0cc
fetched_at: '2026-06-29T00:05:55.956691+00:00'
page_id: '147817841'
product: rm
source: tdn-rm
title: Tratamento de valores Nullos no RM Reports
type: documentation
url: https://tdn.totvs.com/display/LRM/Tratamento+de+valores+Nullos+no+RM+Reports
version: 7
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                     **Versão:**11.82 |
| **Processo** | **:** | RM Reports |
| **Subprocesso** | **:** | Como realizar tratamento de Nullos no RM Reports |
| **Data da publicação** | **:** | 17/07/2014 |

**Nota:** Não há uma opção direta para realizar o tratamento de valores nullos no RM Reports, entretanto já existe chamado aberto para essa melhoria, assim como na versão antiga do RM Gerador (Delphi). Porém, há uma forma de uso do componente "Expressão".

No momento da criação do contexto da expressão você poderá buscar o campo da base diretamente.

Na impressão o Reports faz um tratamento automático para os valores nullos dependendo do tipo do campo.

Exemplo; Para campos do tipo inteiro (int) que tiverem o valor igual a null o reports imprime o valor 0 (zero).

Para campos do tipo texto (string) o sistema traz o campo em branco. Sendo assim o contexto da expressão irá sofrer uma variação conforme o tipo de campo.

Segue abaixo os exemplos:

|  |  |  |
| --- | --- | --- |
| **CAMPO DA BASE** | **TIPO DO CAMPO** | **EXPRESSÃO** |
| PFUNC.JORNADA | RMDVALOR2 | If ( Base.PFUNC.JORNADA = 0, 'ZERADO', Base.PFUNC.JORNADA ) |
| PFUNC.OBSFERIAS | STRING | If ( Base.PFUNC.OBSFERIAS **=** '', 'SEM VALOR', Base.PFUNC.OBSFERIAS ) |
| PFUNC.NRODEPSALFAM | SMALLLINT | If ( Base.PFUNC.NRODEPSALFAM **=** 0, 'DEPENDENT', Base.PFUNC.NRODEPSALFAM ) |
| PFUNC.DATAADMISSAO | DATETIME | If ( Base.PFUNC.DATAADMISSAO <**=** '01/01/1753', 'SEM VALOR', Base.PFUNC.DATAADMISSAO ) |

Estrutura do relatório:

RMDVALOR2:

STRING:

SMALLLINT:

        Veja abaixo o resultado da impressão do relatório:

Relatório em anexo: "[Tratamento para valores Null - Valores Null.TotvsReport](http://tdn.totvs.com/download/attachments/147817841/Tratamento+para+valores+Null+-+Valores+Null.TotvsReport?version=1&modificationDate=1405598253731)"

|  |  |
| --- | --- |
|  | **Para maiores informações:**  Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)    **COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****    **Canais de Atendimento:**  **Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha). |
