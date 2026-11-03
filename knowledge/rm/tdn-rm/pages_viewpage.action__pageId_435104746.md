---
content_hash: e9a9db8124bb1df08131f7aef22db7869202cc7d0f76a8b98749225ec9e1e7ee
fetched_at: '2026-06-29T00:09:46.013898+00:00'
page_id: '435104746'
product: rm
source: tdn-rm
title: Empreendimento - Integração - Avanço da Obra
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435104746
version: 9
---

Neste cadastro é realizado as medições da obra do Empreendimento associado, nos quais podem ser utilizadas para os processos de  Andamento da Obra (POC) e Minha Casa Minha Vida.   
 O cadastro possui os seguintes campos:

* **Descrição:** Pode ser inserido uma descrição do Avanço da Obra;
* **Tipo de Medição:** Através desse campo que é definido qual como será realizada a medição do Avanço da Obra. Possui as seguintes opções:

* + **Manual:** Nessa opção deverá ser inserido manualmente as datas e percentuais das medições.
  + **TOTVS Obras e Projetos:** As medições serão buscadas do Cronograma do TOTVS Obras e Projetos informado no cadastro de Avanço de Obra.
    - Ao selecionar essa opção, os campos de integração com o cronograma do TOTVS Obras e Projetos serão exibidos;
  + **Fórmula:** As medições serão inseridas conforme o resultado da execução da fórmula informada no cadastro de Avanço de Obra.
    - Ao selecionar essa opção, o campo da Fórmula que será executada, será exibido. Assim como o botão que executa a fórmula e o parâmetro que permite que a medição total da obra exceda 100%.

* **Módulo**: Através desse campo é definido para qual funcionalidade o cadastro será utilizado. Possui as seguintes opções:
* **Apuração de Resultado Contábil pelo (POC):** Selecionando essa opção, as medições cadastradas servirão de insumo para o processo de Apuração de Resultado Contábil;
* **Minha Casa Minha Vida:** Selecionando essa opção, as medições cadastradas servirão de insumo para o processo Minha Casa Minha Vida;
* **Empreendimento:** Esse campo determina para qual o Empreendimento será associada as medições cadastradas;

**Incluir automaticamente diferença de avanço 100% em avanços de obra MCMV**

Para utilizar o parâmetro "Incluir automaticamente diferença de avanço 100% em avanços de obra MCMV" acesse o parametrizador em  Contrato >> Plano de Financiamento >>  Etapa 7 (MCMV) do TOTVS Incoporação.   
Com este parâmetro marcado, o cadastro de avanço de obra MCMV passa a incluir automaticamente ao salvar o avanço, um novo avanço de obra com o percentual da diferença de 100% caso este percentual total de 100% não seja alcançado.

* O novo avanço de diferença será incluído para o próximo mês/competência depois do maior avanço já informado.
* Caso não exista nenhum avanço informado será utilizada a data corrente para criação do avanço automático de 100%

**Figura 1: Parâmetro Incluir automaticamente diferença de avanço 100% em avanços de obra MCMV.**

**Exemplo:**

* Cadastro de avanço automático, com primeiro período 0% e segundo período 100%;
* Maior período informado 11/02/2019;
* Novo período automático 12/02/2019.

Este cenário apresentado com período de percentual 0%, representa o modelo de terreno averbado, ou seja, independente de medições.

* Com o parâmetro habilitado, os avanços de obra do tipo MCMV obrigatoriamente terão que totalizar 100%.
* Caso o percentual total seja diferente de 100% será exibida a seguinte mensagem para o usuário.

Mais informações: [Minha Casa Minha Vida](http://tdn.totvs.com/display/LRM/Minha+Casa+Minha+Vida)
