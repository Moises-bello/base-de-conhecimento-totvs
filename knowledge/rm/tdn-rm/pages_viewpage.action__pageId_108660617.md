---
content_hash: 3f77471b2f330f03c1abcaa6728cf29ac6e962542b8d31adf3fce3b18e6aff76
fetched_at: '2026-06-29T00:05:54.787145+00:00'
page_id: '108660617'
product: rm
source: tdn-rm
title: Passagem de parâmetros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=108660617
version: 17
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Inteligência de Negócios                         **Versão:** 11.52 |
| **Processo** | **:** | Planilhas .NET |
| **Subprocesso** | **:** | Passagem de parâmetros |
| **Data da publicação** | **:** | 07/01/2014 |

        Planilha.NET é uma das opções evolutivas para a Planilha Delphi. Com possibilidade de uso de vários recursos que o Excel oferece as Planilhas.Net dispõem de inúmeras formas de trabalhar/manusear as informações administrativas da sua instituição.

        Neste tópico iremos exemplificar as formas de passagem de parâmetros para esta ferramenta.

**PARÂMETROS DA PRÓPRIA CONSULTA SQL**

        Neste exemplo, na estrutura da Planilha.Net, utilizaremos o parâmetro da própria consulta SQL como parâmetro.

        Utilizaremos a consulta SQL abaixo que retornará dados de um funcionário. Desta consulta utilizaremos duas passagens de parâmetros; SECAO e SITUACAO.

ATENÇÃO

         O parâmetro **:**$CODCOLIGADA  desta consulta, não será considerado no exemplo por se tratar de uma variável dinâmica. Para informações acesse: <http://tdn.totvs.com/x/RoLFAw>

        Elaborada a consulta SQL acessamos a planilha.Net através das opções de menu: “**Gestão | Ferramentas de Análise | Planilha Net**”.

        Criada uma planilha faça a associação da consulta SQL a planilha recentemente criada. Durante associação da consulta SQL o sistema solicitará o preenchimento dos valores dos parâmetros para consulta.

        Quando finalizada a associação, teremos nas configurações “Ações do Documento”, grupo “Parâmetros”, os parâmetros informados na inclusão da consulta SQL.

        Para alterações dos valores dos filtros, clique duas vezes sobre o valor do parâmetro, na coluna “Valor”. Feita alteração dos valores tecle Enter para registrar a alteração e recalcular a planilha.

---

**PARÂMETROS DA PRÓPRIA CONSULTA SQL EM MAIS DE UMA PLANILHA**

        Quando utilizado no mesmo arquivo de Excel mais de uma planilha com consultas SQL diferentes. Quando necessário modificar o valor de um dos parâmetros, primeiramente, atente-se a consulta SQL selecionada e a qual Plan está associada. Feita a identificação e seleção correta do parâmetro clique duas vezes sobre seu valor e digite o novo. Para confirmar as alterações e recalcular a planilha tecle Enter.

       No exemplo abaixo demonstramos as configurações “Ações do Documento” de um arquivo que possui duas planilhas e em cada planilha uma consulta SQL diferente.

| Plan1 | Plan2 |
| --- | --- |
|  |  |

---

**PARÂMETROS UTILIZANDO CÉLULAS DA PLANILHA.**

        Este método é o mais prático e usual para passagem de parâmetros para a consulta SQL associada a planilha.Net. Para uso deste método iremos criamos uma consulta SQL com três parâmetros: CHAPA, DTINI e DTFIM.

        Criada a consulta SQL, durante associação a planilha, é possível informar qual(is) a(s) célula(s) da planilha passará(ão) o(s) valor(es) do(s) parâmetro(s) para consulta SQL.

        Caso não queira informar as células que passarão o valor ao parâmetro, informe diretamente nos filtros os valores para que a associação seja concluída. Em seguida em “Ações do Documento”, altere no grupo “Parâmetros”, o valor do filtro incluindo o comando que indicará qual a célula receberá para ser utilizado como parâmetro.

       O comando deve ser constituído pelo **nome da guia da planilha****!** + **nome da célula** separado pelo ponto de exclamação. Exemplo: **PLAN1!A1**.

Feita as configurações teremos no grupo “Parâmetros” a seguinte visualização:

        Feita as configurações basta alterar o valor da célula utilizada como parâmetro e teclar Enter para que a consulta SQL receba o novo valor e recalcule a planilha. No exemplo abaixo o resultado da planilha após atribuição dos valores de parâmetro diretamente na planilha.

---

**PARÂMETROS UTILIZANDO CÉLULAS EM VÁRIAS PLANILHAS.**

        Quando utilizamos mais de uma planilha no arquivo de Excel com mais de uma planilha associada com mais de uma consulta SQL, devemos nos atentar para definição de qual célula é responsável por repassar o valor de parâmetro para consulta SQL.

        Nas configurações, “Ações do Documento”, verificamos no grupo “Parâmetros”, qual célula da planilha o parâmetro está localizado. Abaixo exemplo destas opções, a primeira consulta está associada a **plan1** e a segunda associada a **plan2**.

| Plan1 | Plan2 |
| --- | --- |
|  |  |

        Para alterar os valores dos parâmetros digite diretamente nas células seus novos valores e tecle Enter, para recalculo da planilha. Abaixo o resultado de exemplo com células recebendo valores de parâmetros.

| Plan1 | Plan2 |
| --- | --- |
|  |  |

Para maiores informações:

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
