---
content_hash: 9b7c18346937dcd30858232d0af33bab5f9099d6fa47d84211ec5ea5fcaff9a9
fetched_at: '2026-06-29T00:09:27.921245+00:00'
page_id: '423938572'
product: rm
source: tdn-rm
title: Roteiro de Associação de Escrituração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938572
version: 2
---

Se para a Escrituração Resumida existir um Livro Auxiliar, será necessária a Associação de Escrituração.

Para facilitar a compreensão da "Associação da Escrituração", foram denominadas nesse documento:

**"Livro Diário com Escrituração Resumida (com escrituração auxiliar)",** aqui denominado de Escrituração *Pai*.

**"Livro Diário Auxiliar ao Diário com Escrituração Resumida"**, aqui denominado de Escrituração *Filha*.

Para associar a "Escrituração Pai" à "Escrituração Filha", é necessário:

Abrir o Cadastro: Rotinas Legais | SPED Contábil | Escrituração Contábil.

Cadastrar uma "Escrituração Pai" e uma "Escrituração Filha", com os mesmos dados, diferenciando apenas o campo "Forma de Escrituração".

1- Editar a "Escrituração Pai" e acionar em Anexos a opção "Livros Auxiliares ao Diário". Informar a "Escrituração Filha" que irá complementar o livro resumido, associando-a à "Escrituração Pai". Salvar a associação.

2- Da mesma forma, é preciso que se faça também a associação na "Escrituração Filha" e, para isto, editar a "Escrituração Filha" e acionar em Anexos a opção "Livros Auxiliares ao Diário". Informar a "Escrituração Pai" à qual servirá como complemento. Salvar a associação.

**Observação** Para a forma de escrituração "Livro Diário (completo, sem escrituração auxiliar)" não deve ser preenchido livro auxiliar.

**Atenção**  
A geração do SPED Contábil para escriturações que exigem livros auxiliares deverá seguir a seguinte ordem: Primeiro deve-se gerar a "Escrituração Filha". Em seguida gerar a "Escrituração Pai" e informar o caminho em que a escrituração filha foi gerada para que o sistema possa identificar o seu código Hash para informá-lo no arquivo da escrituração pai.

Os dois arquivos correspondentes à "Escrituração Pai" e à "Escrituração Filha" devem ser validados no PVA.
