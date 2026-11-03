---
content_hash: 3e78c79302462e1f88514716bca2c65c9d687dc518692f9e0d3eeff5a76e863c
fetched_at: '2026-06-29T00:11:13.049042+00:00'
page_id: '656071707'
product: rm
source: tdn-rm
title: Editando Empreendimentos
type: documentation
url: https://tdn.totvs.com/display/LRM/Editando+Empreendimentos
version: 5
---

#FF9000Introdução

Para que o Portal de Imóveis trabalhe com os empreendimentos estes devem estar cadastrados no TCGI, pois no portal podemos somente fazer edição de alguns dados para complementar as informações no empreendimento no Portal de Imóveis. Para editar os dados de empreendimentos devemos acessar Backend > Empreendimentos.

Ao acessar a opção vemos todos os empreendimentos cadastrados e na coluna “Situação” identificamos se este empreendimento está:

* **Ativo** – Empreendimento habilitado para ser vendido e trabalhado pelos corretores.  Nesta situação empreendimentos contam licenças. Importante. A partir da **versão 12.1.2205**, a ativação dos empreendimentos só poderá ser feita uma vez por domínio. Para maiores detalhes, consulte a documentação de [sincronia (clique aqui)](https://tdn.totvs.com/pages/viewpage.action?pageId=656060905).
* **Inativo** – Empreendimento não está habilitado para venda. Não conta para o número de licenças
* **Oculto** – Empreendimentos neste estado somente aparecem para grupos de usuários que visualizam empreendimentos ocultos. Esta situação serve para testarem os empreendimentos parametrizados sem que todos os corretores acessem o empreendimento. Empreendimentos nesta situação contam para o numero de licenças
* **Visualiza** – Empreendimentos nesta situação podem ser visualizados na tela de venda de empreendimentos mas não podem ser vendidos. Permite abrir o mapa de disponibilidade mas não permite reservas nem simular propostas. Para que empreendimentos nesta situação possam ser visualizados, no grupo do usuário deve-se estar marcado ver empreendimentos marcados como visualizar.
#FF9000Aba Empreendimentos

Nesta aba são cadastradas informações complementares dos empreendimentos que aparecerão no botão de informações na tela principal (Frontend) de visão dos empreendimentos a venda. Dados como informações do imóvel, características, área de lazer e demais informações que servem para informar aos usuários detalhes sobre a venda.

Além disto nesta mesma aba também são cadastrados parâmetros que determinam o comportamento do processo de simulação de propostas para as unidades deste empreendimento. Segue a descrição destes:

* **Situação:** Ativo ou não. Ativo o empreendimento contabiliza a licença. Idem o campo situação da grid inicial do cadastro de empreendimentos.
* **Estágio da obra:**Estágios possíveis da obra. Este cadastro pode ser feito através do menu backend> globais > estágios da obra.
* **Permite parcelas após entrega:**Se habilitado permitirá que uma proposta tenha parcelas a vencer após a data de entrega do empreendimento.
* **TMA:**Taxa Mínima de Atratividade ou Taxa de Desconto que será aplicada no cálculo do VPL.
* **Percentual de VPL para aprovação:** Por padrão é 100%, indicando que não existe nenhum desconto na comparação do VPL da proposta com a tabela de preços deste empreendimento, ou seja, o VPL da proposta tem que ser igual ou superior o VPL da tabela. Se desejar que todas as propostas feitas, por qualquer usuário do Portal de Imóveis, possa ser aprovada com 2% de desconto sobre o VPL da tabela, então neste campo indicamos 98% que significa que aceita-se uma proposta que seja 98% do VPL da tabela.
* **Tipo de cálculo de VPL**: Existem duas possibilidades, a primeira e a recomendada para 99% dos casos é o tipo BRUTO, que indica que o cálculo do VPL será realizado com o valor declarado na tabela de preço. O tipo LIQUIDO, elimina do calculo do VPL o valor da comissão para depois fazer o VPL (sugerimos não usar este tipo LIQUIDO pois este parâmetro será eliminado do sistema em versões futuras)
* **Unidades por linha no bloco:**Este parâmetro deve ser preenchido somente se o Portal de Imóveis não conseguir dividir corretamente e de forma automática as unidades por andar. Sendo assim aqui deve-se colocar quantas unidades por andar existem ou quantas unidades por andar deseja demonstrar.
* **Blocos lado a lado:** Idem ao parâmetro acima, só deve ser preenchido se o Portal de Imóveis não conseguiu dividir os blocos corretamente na tela. Normalmente preenchido quando um empreendimento possui vários blocos e a quebra das unidades por andar está comprometida na tela, então pode-se quebrar que deseja ver 3 blocos lado a lado na tela, determinando esta quebra de visão da tela.
* **Dias de vencimento parcelas:**Pode-se determinar os dias que deseja que as parcelas negociadas nas propostas tenham de vencimento, exemplo: 5,10,15.
* **Período de retenção da reserva:**Quantas horas as reservas feitas neste empreendimento duram. Se não preenchido usa o parâmetro global  (backend>parâmetros).
* **Período de retenção da reserva (em proposta):**Quantas horas as propostas feitas neste empreendimento duram. Se não preenchido usa o parâmetro global  (backend>parâmetros).
* **Percentual de comissão:**quando aplicado este percentual terá prioridade sobre os demais percentuais de comissão cadastrados. O Portal de Imóveis trata a seguinte hierarquia para o calculo de comissão:

- Comissão do empreendimento
- Comissão do usuário
- Comissão da imobiliária
- Comissão do grupo de usuário

* **Comissão adicional marcado como existente por padrão:**Se afirmativo defini que toda venda tem um valor livre e adicionar a acrescentar no valor da comissão.
* **Comissão adicional paga pelo cliente ou empresa:**Determina quem paga esta comissão adicional.
* **Comissão adicional paga por RPA ou NF:**Tipo de pagamento da comissão adicional.
* **Comissão mostrar painel na proposta:**Mostra ou não abaixo da simulação de propostas um painel para o corretor escolher as opções de comissão (quem paga e tipo de pagamento). Se a incorporadora possui um processo padrão de comissão, este painel pode ser omitido e o Portal de Imóveis seguirá as configurações definidas no empreendimento e se não parametrizado seguirá os parâmetros globais.
* **Comissão paga pelo cliente ou empresa:**Quem paga a comissão.
* **Comissão paga por RPA ou NF:**Tipo de pagamento da comissão (informativo).
* **Visão de vagas de garagem:**Deseja a descrição, a quantidade ou nenhuma informação nos campos relacionados a vaga de garagem.
* **URL Youtube:**Url de video no youtube sobre o empreendimento.
* **Ocultar data de entrega:**Não mostra a data de entrega no quadro do empreendimento.
* **Ocultar coluna de data no plano de pagamento:**Elimina a coluna data na impressão do plano de pagamento.
* **Cálculo de desconto da comissão:**Forma de desconto da comissão quando paga pelo cliente, decrescente (retira tudo valor possível na ordem decrescente dos componentes), proporcional (realiza regra de proporcionalidade para descontar o valor da comissão dos componentes que participam do calculo), parcelas iguais (divide igualmente o valor da comissão entre os componentes de onde se desconta a comissão).
* **Permite reservas:**Se marcado este empreendimento permite reservas.
* **Permite propostas:**Se marcado este empreendimento permite propostas.
* **Ordem de disposição do mapa de disponibilidade:**Opção valida somente quando se possui uma imagem de disponibilidade do empreendimento. Neste podemos definir o que aparecerá primeiro a imagem ou o mapa construído pelo portal.
* **Gerente do empreendimento:** Define o usuário que será responsável por aprovar as propostas reprovadas do empreendimento e qual será sua comissão no processo de vendas. Sempre que houver um usuário selecionado neste campo ele será a pessoa que receberá mensagens quando o corretor solicitar a aprovação de uma proposta deste empreendimento. Além disto ao salvar a proposta este gerente do empreendimento será inserido automaticamente no cadastro de comissão com seu percentual associado.
* **Avisar a obrigatoriedade de parcelas mensais simulação:** Quando marcado, exibirá mensagem quando o plano de pagamento proposto não possuir parcelas consecutivas mensalmente. Mensagem apenas informativa. Não impedirá de realizar a proposta.
* **Mostrar preço inicial das unidades na página de empreendimentos:**No frontend no menu empreendimentos, demonstrará ao lado de cada imagem do empreendimento o preço inicial das unidades deste.
#FF9000Aba Imagens

Cadastra as imagens que compõem a apresentação do empreendimento. As imagens são separadas por tipos e estas são visualizadas a partir do botão de informações do empreendimento na página de empreendimentos (frontend)

+ **Chamada:** imagem que aparecerá na demonstração do empreendimento na página de empreendimentos a venda.
+ **Fachada:** Imagens que será demonstrada a partir do botão de informações do empreendimento.
+ **Faixa:**banner com a logomarca do empreendimento será demonstrada a partir do botão de informações do empreendimento.
+ **Lazer:**imagens da área de lazer do empreendimento.
+ **Perspectiva:**imagens com visão geral do empreendimento como áreas privativas**,**comuns e áreas decoradas.
+ **Plantas:**imagens das plantas das unidades.
+ **Obra:**imagens do estágio da obra.

Sugerimos os seguintes tamanhos por tipos de imagens: faixa – 716px x 158px, logo – altura 250px e largura livre, demais – 1000px x 1000px.

#FF9000Aba Minutas

Nesta aba podemos anexar as minutas de contratos que serão utilizadas para impressão pelo Portal de Imóveis dos contratos de compra de unidades imobiliárias. Após criado o documento WORD com as TAG’s que representam os campos do Portal de Imóveis, devemos cadastrar esta minuta no empreendimento desejado. Um empreendimento pode ter tantas minutas quanto necessário for. Estas podem ser associadas a modalidade, desta forma ao se imprimir o contrato de uma proposta ele irá identificar qual a modalidade da proposta e buscar somente as minutas associadas aquela modalidade para a escolha do modelo para impressão. 

***Regras para criação de minutas.***

Todas as minutas devem ser feitas no WORD 2013 ou superior e o arquivo deve obrigatoriamente ser salvo na extensão DOCX . Para imprimir corretamente o documento deverá ser construído no estilo SEM ESPAÇAMENTO. 

Para documentos que já estejam prontos, siga os passos abaixo para deixar o documento no estilo “Sem Espaçamento”:

1. Abra o documento WORD
2. Selecione todo o conteúdo com CTRL + T
3. Clique no estilo SEM ESPAÇAMENTO (vide imagem abaixo)
4. Salve o documento como DOCX
#FF9000Aba Documentos da Proposta

Para definirmos quais documentos serão solicitados durante o processo de confecção da proposta, devemos primeiro em backend > globais > Documentos da proposta. Neste cadastro serão definidos os tipos de documentos possíveis de serem atribuídos aos empreendimentos. Após o cadastro dos documentos, na edição dos empreendimentos definimos quais documentos serão solicitados durante o processo de confecção da proposta de venda do empreendimento. Podemos ter diferentes documentos por empreendimento.

#FF9000Aba Imagens de Disponibilidade

Neste menu conseguimos inserir uma imagem (planta baixa de um loteamento por exemplo) para posicionarmos as unidades e ter uma visão humanizada da disponibilidade.

Após inserir a imagem e salvar, clique no botão “Posicionar Unidades” para arrastar cada unidade para sua devida posição.

#FF9000Aba Anexos Informativos

Através deste menu podemos carregar qualquer documento para ser disponibilizado na página de informações do empreendimento. 

Adicione um documento, dê um título para ele e carregue o arquivo de dados que ele será disponibilizado no ícone de informações do empreendimento.

#FF9000Aba Modelo Proposta

Da mesma forma que podemos criar os modelos de minutas de contratos, também podemos criar modelos de propostas. O processo é idêntico ao descrito acima sobre minutas de contratos

Mais Informações

---

* [Portal de Imóveis - Backend - Empreendimentos](https://tdn.totvs.com/pages/viewpage.action?pageId=563947962)
