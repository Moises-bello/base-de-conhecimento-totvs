---
content_hash: 615d50e9827f2c0e87648cd34742f2dde4e5ea42aa1f6bbcf9c9e292747c81f4
fetched_at: '2026-06-29T00:11:02.528884+00:00'
page_id: '61931808'
product: rm
source: tdn-rm
title: Propriedade Sumário - RM Reports
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=61931808
version: 19
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | RM Reports                         **Versão:** 11.80 |
| **Processo** | **:** | Propriedades de campos |
| **Subprocesso** | **:** | Sumário |
| **Data da publicação** | **:** | 29/05/2013 |

Objetivo: A propriedade "Sumário" permite que o campo exiba um sumário (somatório, média, máximo, mínimo, etc) conforme a necessidade.

Este componente deverá ser utilizado no grupo “Rodapé do Detalhe”. Como exemplo, imagine o relatório na seguinte estrutura.

* **Cabeçalho do Detalhe:** PFUNC.CODSECAO e PSECAO.DESCRICAO
* **Detalhe:** PFUNC.CHAPA, PFUNC.NOME e PFUNC.SALARIO
* **Rodapé do Detalhe:** PFUNC.SALARIO

1. No grupo **Rodapé do Detalhe** replique o campo PFUNC.SALARIO para que possam ser utilizadas funções diferentes do sumário, como por exemplo:  Soma, Média, Max, Min, Contar, dentre outras disponíveis, conforme a necessidade.

        2. Para isso selecione o campo PFUNC.SALARIO e clique sobre a smart tag do componente. Nas propriedades listadas clique nas reticências da opção “Sumário”.

     3. Continuando o processo será escolhida a opção “Soma” do Sumário. Em seguida, marque a opção “Ignorar Valores nulos” e em "Resumo Processado", escolha a opção“Grupo”.

      Obs.: A opção "grupo" foi escolhida devido a quebra do grupo.

  4.  Mais adiante, realize este mesmo procedimento, copiando o campo PFUNC.SALARIO, porém alterando as opções no sumário (conforme a necessidade: média, máximo, mínimo, contar).

    Abaixo, temos o resultado do relatório gerado com a inclusão de sumários diferentes.

O arquivo do relatório utilizado "" e o resultado em formato "" seguem anexos.

---

Para maiores informações:

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
