---
content_hash: 131a837da0890953edd9ebbc20383a6deac41784cb0977959b4697cd9bbf56c6
fetched_at: '2026-06-29T00:09:27.353778+00:00'
page_id: '423938506'
product: rm
source: tdn-rm
title: Relatório Razão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938506
version: 24
---

Pré-Requisitos

O relatório "Livro razão" é obrigatório pela legislação comercial e tem a finalidade de demonstrar a movimentação analítica das contas escrituradas nos diários e constantes do balanço. Para a impressão deste relatório, selecione o item "Relatórios" no Menu principal da nova MDI e em seguida a opção Razão.

Atualmente é possível a emissão de cinco Tipos de razão:

* ;
* Razão Analítico; (oficial para legislação)
* Razão Gerencial / Contábil;
* Razão Contábil / Gerencial;
* ;
* [Razão Contábil / Centro de Custo;](https://tdn.totvs.com/x/h-QUIg)
* .

Para ordenação de impressão de Campos idêntica ao relatório Delphi, as Preferências de impressão existentes devem ser deletadas. Para exclusão clique na imagem de engrenagem das Preferências | Abrir/Excluir, após selecione a preferência, e clique em Excluir.

Performance do relatório

A opção **"****Contas sem movimentação e sem Saldo"** marcada faz com que todas as contas contábeis sejam retornadas no processamento do relatório, o que pode ser um ofensor na performance dependendo da quantidade de contas existentes na base de dados. Caso não seja necessário, recomendados que essa opção não seja marcada juntamente com as outras disponíveis.   
Para uma melhor avaliação dessas contas em específico, sugerimos que essa opção seja sempre utilizada de forma isolada.  
  
Sugerimos também para o **ganho de performance** a geração do arquivo em formato PDF direcionando onde o mesmo será salvo (neste caso, não deve ser marcado a opção de visualizar impressão).

Exportação Excel/CSV

Quando estiver gerando o Razão analítico ou o Razão Sintético, se optar pela exportação em Excel ou CSV algumas parametrizações que refletem na exibição do relatório ou na totalização das informações serão ignoradas, independente de como tiverem sido parametrizadas na tela.

Como o intuito da exportação em planilha é possibilitar o trabalho nos dados de forma "crua", ao optar por esse tipo de exportação alguns parâmetros serão desconsiderados. Portanto, não será realizada totalização no relatório e nem a quebra. Os parâmetros abaixo serão desconsiderados internamente durante a geração do arquivo:

Exportação com Smart View

Novo Tipo de Saída adicionado.

Configurar Recurso Smart View

Segue documentação: 

Parâmetros Contemplados

**1 -** Intervalo de Datas e se as informações serão buscadas do histórico:

**2 -** Filtro de Coligada\Filial\Departamento:

**3 -** Tipo de Razão FIXO como **Razão Contábil Analítico**:

**4 -** Opções de Imprimir\Filtrar:

**5 -** Ordenação dos Lançamentos:

**6 -** Filtro de Lotes:

**7 -** Filtros de Conta Contábil \ Centro de Custo \ Histórico \ Participante:

**8 -** Tipo de Valor (Moeda):

**9 -** Imprimir Valores e Milhares e Não imprimir os centavos:

---

Após selecionado o tipo Smart View, deverá preencher o Lookup para informar o Recurso do Smart View

**Validação** com relação ao Tipo do Razão informado.

Após gerar, é necessário clicar em **"Enviar"** na tela do Smart View pois o usuário pode ter parametrizado outros filtros no relatório.

**Exibição do Relatório:**
