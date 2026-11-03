---
content_hash: 2787a328d1848924a4b3587f81493f2b5ba9a477434705bcb9d280c2699ca3ab
fetched_at: '2026-06-29T00:08:28.866765+00:00'
page_id: '271863270'
product: rm
source: tdn-rm
title: Utilizando o SaveRecord com valor nulo para data
type: documentation
url: https://tdn.totvs.com/display/LRM/Utilizando+o+SaveRecord+com+valor+nulo+para+data
version: 15
---

# Índice

---

.\*ndice:

# Objetivo

---

       O objetivo deste documento é mostrar como utilizar o SaveRecord com valor nulo para data.

**Observação:** Será necessário seguir os passos deste documento e adicionar a tag no atributo com valor nulo para data apenas se for passado um Schema no XML a ser utilizado. Se o XML **não** possuir Schema **não** será necessário alterar o atributo.

Mais informações para [Parâmetros de Contexto](https://tdn.totvs.com/display/LRM/TBC+-+Web+Service+DataServer#TBCWebServiceDataServer-Formatodospar%C3%A2metrosnaTagdecontexto)

# Como fazer - Valor nulo para Data

---

Quando existe a necessidade de atualizar um registro com o valor nulo para a data deve-se adicionar o atributo:

xml

       Para maiores detalhes sobre o uso do atributo, favor verificar em [www.w3.org](http://www.w3.org/). Também existem alguns detalhes na documentação da Microsoft, como o conteúdo disponível [neste link](https://msdn.microsoft.com/pt-br/library/ybce7f69%28v=vs.85%29.aspx?f=255&MSPPError=-2147217396). 

       **Exemplo:**

       Observe que no exemplo abaixo a tag DATAULTIMOACESSOVALIDO contém o atributo informado acima e ao efetuar o SaveRecord esse campo será atualizado para o valor nulo.

xml




GlbUsuarioData



...

convidado
Usuario Convidado
...
]]]]>

CODCOLIGADA=1
]]>

# Exemplo

---

       A imagem abaixo ilustra o exemplo acima, executado no SoapUI utilizando o atributo:  xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance".

       O arquivo abaixo pode ser baixado e utilizado como teste da aplicação do atributo. Lembre-se de utilizar uma base de teste.

       Arquivo para download:

Atenção

Para executar o exemplo deste documento utilize uma base de teste, pois ao efetuar um SaveRecord um novo registro será criado na sua base, evitando assim inconsistências no seu ambiente.

falsefalse

**Produto:** Framework

false

**Versão:** 11.82.XX e 12.01.XX

false

**Processo:** Utilizando o Saverecord com valor nulo para data

falsefalse

**Status:** Finalizado

false

**Data:** 03/03/2017

false

**Autores:**

**Douglas Maxwell de Oliveira**
