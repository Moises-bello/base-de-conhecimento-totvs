---
content_hash: 604b7e9f98e89e8dc0458f222ceed193740c64a4ea002242c5ace29895184277
fetched_at: '2026-06-29T00:10:21.986303+00:00'
page_id: '496012109'
product: rm
source: tdn-rm
title: eSocial
type: documentation
url: https://tdn.totvs.com/display/LRM/eSocial
version: 22
---

---

**Objetivo**

O anexo **eSocial** existente no cadastro do Cliente/Fornecedor foi implementado pelo produto TOTVS Folha de Pagamento e tem como objetivo parametrizar informações a serem levadas para o eSocial.

---

**IMPORTANTE**

1. Para o preenchimento do grupo **S-1005 - Informações de Estabelecimentos/Obras**, é necessário que o campo "Tipo da Lotação", existente no menu eSocial | Lotação Tributária, seja igual a "01-Classificação da atividade econômica exercida pela Pessoa Jurídica para fins de atribuição de código FPAS, inclusive obras de construção civil própria".

2. Caso oCliente/Fornecedor seja **obra própria**, as informações consideradas para o eSocial serão as preenchidas no menu Cliente/Fornecedor | Anexo CEI do Cliente/Fornecedor | Anexo eSocial. Veja detalhes no link [Anexo eSocial](https://tdn.totvs.com/display/LRM/Anexo+eSocial).

---

**Tomador de Serviços Folha**

Este parâmetro indica que o Cliente/Fornecedor será considerado na carga inicial do eSocial. Além disso, qualquer alteração em suas informações relevantes ativará os gatilhos correspondentes.

**Obra Própria**

Ao marcar este parâmetro, será gerado um gatilho de "inclusão" do evento "S-1005-abela de Estabelecimentos, Obras ou Unidades de Órgãos Públicos" para tomadores de serviço do tipo "Obra Própria". Além disso, os campos **CNAE, RAT, FAP e Registro de Ponto** serão habilitados e deverão ser preenchidos.

Caso o parâmetro esteja desmarcado, os campos **CNAE**, **RAT**, **FAP** e **Registro de Ponto** serão habilitados e deverão ser preenchidos.

**FAP**

Ao marcar os parâmetros **"Tomador de serviço folha"** e **"Obra Própria"**, os campos do FAP serão habilitados. Quando preenchidos, o XML do evento S-1005 considerará essas informações para o preenchimento da tag referente ao processo FAP.

**ATENÇÃO:**

* + Quando um tomador possuir múltiplos CEIs, será gerado um gatilho para o tomador e outro para cada**CEI**. O XML do evento S-1005 considerará as informações do FAP registradas no respectivo CEI.
  + Caso não deseje que o sistema busque os dados do processo do FAP no Cliente/Fornecedor, marque o parâmetro **"Considera Dados da Filial"**. Com essa opção ativada, os dados serão obtidos a partir da filial informada nesse parâmetro.

Maiores informações acesse o link [DT-S1005:Tratar a geração do grupo <procAdmJudFap> para obra própria (CNO/CEI)](https://tdn.totvs.com/pages/viewpage.action?pageId=929925143)

**Considera dados da Filial**

Ao selecionar este parâmetro, as informações da filial indicada serão consideradas no processamento.

Caso o parâmetro esteja desmarcado, os campos **CNAE**, **RAT**, **FAP** e **Registro de Ponto** serão habilitados e deverão ser preenchidos.

**Código da Categoria eSocial**

Preencha com o código correspondente à categoria do trabalhador, conforme a **Tabela 01 - Categorias de Trabalhadores** do eSocial. Este campo deve ser informado principalmente para autônomos que serão enviados ao eSocial.

**CPF**

O CPF é utilizado nos eventos periódicos do eSocial nas seguintes situações:

* Quando o Cliente/Fornecedor for do tipo **Pessoa Física**, produtor rural, localizado no estado de São Paulo, e o campo CPF/CNPJ estiver preenchido com um CNPJ. Eventos considerados: **S-1250 / S-1260**. Veja detalhes em [Link](https://tdn.totvs.com/pages/releaseview.action?pageId=458773344).
* Quando o Cliente/Fornecedor for do tipo **Pessoa Jurídica**, com porte de empresa **MEI**, e o campo CPF/CNPJ estiver preenchido com um CNPJ. Evento considerado: **S-1200**.

**Indicativo da Opção pelo Produtor Rural para Tributação da Contribuição Previdenciária**

Define a forma de tributação da contribuição previdenciária utilizada pelo produtor rural. Essa informação é aplicada no evento "S-1250 - Aquisição de Produção Rural"e será habilitada somente se o ramo de atividade estiver definido como **produtor rural**.

**Indicador de Desconto da Contribuição Previdenciária do Declarante**

Este campo deve ser preenchido exclusivamente para **autônomos que possuam outros vínculos empregatícios**. Ao gerar o XML do evento S-1200 a tag <**indMV>** será preenchida conforme o indicador do desconto do segurado:

1. O declarante aplica a **alíquota integral** de desconto do segurado sobre a remuneração informada (o percentual será calculado considerando a remuneração total do trabalhador).
2. O declarante aplica a **alíquota sobre a diferença** entre o limite máximo do salário de contribuição e a remuneração recebida em outra(s) empresa(s), informada pelo trabalhador.
3. O declarante **não realiza desconto** do segurado, pois o trabalhador já atingiu o limite máximo do salário de contribuição em outra(s) empresa(s).

**Prefixo Período**

Este campo é utilizado para separar osperíodos de autônomos com múltiplos vínculos cadastrados que possuem lançamentos no mesmo período de pagamento. O campo aceita até 10 caracteres e deve ser preenchido conforme o código do cliente/fornecedor.

### Exemplo de uso:

* + Autônomo 1 (CPF 111.111.111-11, código 00001): Lançamento cadastrado para o dia 10/01/2019.
  + Autônomo 2 (CPF 111.111.111-11, código 99999): Lançamento cadastrado para o dia 15/01/2019.

Nesse caso, o campo **Prefixo Período** pode ser preenchido com o código do cliente/fornecedor.

### Como funciona a geração dos eventos:

Após preencher o campo **Prefixo Período**, serão gerados dois arquivos XML para o envio ao governo, com a tag `<ideDmDev>` formatada da seguinte forma:

* + Autônomo com código 00001 (Categoria 701):  
    `<ideDmDev>100001</ideDmDev>`

    (Padrão + 00001 - Código do Cliente/Fornecedor)
  + Autônomo com código 99999 (Categoria 712):  
    `<ideDmDev>199999</ideDmDev>`

    (Padrão + 99999 - Código do Cliente/Fornecedor)

### Observações:

1. 1. A tag`<ideDmDev>` será formada pela união do período (padrão "1") com a informação cadastrada no campo **Prefixo Período**.

      * Caso o campo **Prefixo Período** não seja preenchido, será informado apenas o número do período na tag `<ideDmDev>`.
   2. O campo pode ser preenchido com números ou letras.
