---
content_hash: 022f4517f939ab62d666157417517bf426669feecd1775eb6068042646ea9c95
fetched_at: '2026-06-29T00:06:01.349662+00:00'
page_id: '198937749'
product: rm
source: tdn-rm
title: Integração TOTVS Educacional x TOTVS Gestão de Estoque, Compras e Faturamento.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=198937749
version: 1
---

**1. Introdução**

*Este manual contempla todos os passos necessário para permitir a integração entre os sistemas TOTVS Educacional e TOTVS Gestão de Estoque, Compras e Faturamento com relação à Geração de Movimentos.*

**2. Desenvolvimento/Procedimento**

**(TOTVS Gestão de Estoque e Faturamento)**

**Criação do Tipo de movimento**

Só serão listados tipos de movimentos que obedecem às seguintes condições abaixo:

* Ser um tipo de movimento de venda (2.2)
* Ser um tipo de movimento de tipo Pedido (2.1)
* Não estar parametrizado para gera lançamentos,

*Deve estar parametrizado para gerar nota fiscal eletrônica.*

**Ambiente>>Parâmetros>>TOTVS Gestão de Estoque e Faturamento**

Cadastrar um novo Tipo de Movimento seguindo as configurações básicas mostradas abaixo:

Selecionar em nosso caso a opção: e em seguida Avançar

Para inclusão de um novo Tipo de Movimento, basta clicar em Incluir Novo, como mostra o print acima.

Código do Tipo de Movimento iniciado em 2.2 que é do tipo de vendas, como já informado no inicio da apostila.

Informar a Máscara do Número, Dados de Emitente / Destinatário e as fórmulas do Valor Bruto, Subtotal e Valor Líquido, devem ser preenchidos

Informar a Séria do Tipo de Movimento na qual foi criado, se é principal ou não.

Neste exemplo, o código de Série informado: CCE

Depois de criado o novo Tipo de Movimento, deve-se selecioná-lo em seguida e dar um duplo clique para que possa configurar o novo Tipo de Movimento.

Avançar

Numeração: **MOSTRA**

Informar a Classificação e os campos de **Máscara do Número** e séries já são informados, conforme mostrado nas telas de criação do tipo de movimento.

, no caso de **Estadual**, é obrigatório o uso de **9 dígitos** e

No caso de **Municipal**, é indiferente o número de caracteres. (Nosso caso é NF Municipal)

, o uso é Numérico no caso de **NF Estadual**. No caso de **NF Municipal** que é o nosso exemplo, indiferente, pode ser usado letras, pois este campo é Alfanumérico.

Saída: Emitente Empresa

Destino: Cliente

Avançar

**Observação sobre as opções:**

**Edita:** Obriga o usuário a preencher as informações necessários do parâmetro.

**Mostra:** Não Obriga o preenchimento das informações do campo na qual estiver parametrizado desta forma.

**Não Edita:** Não obriga, mas não mostra.

 Edição do Local de Saída: **NÃO EDITA**

Avançar

Avançar

Neste Tópico tem que estar em Edição da Data de Saída Edita e em nome da Data de saída , Data de Saída

Avançar

 Avançar

Avançar

Avançar

Avançar

Avançar

Avançar

Avançar

O Campo Fórmulas, é povoado no ato da criação do Novo Tipo de Movimento ou por este parametrizador **‘Mov – Valores Financeiros’** como mostra a tela acima.

Avançar

Avançar

Avançar

Avançar

Se o campo: Editar Transportadora 1 estiver informada no movimento, o sistema consiste, mas no caso de Municipal (Não consiste).

Avançar

Avançar

Avançar

Avançar

Avançar

Avançar

Avançar

Tipo dos itens: tem que ser do tipo, **SERVIÇO**, **não** pode ser usada as opções, **Ambos** ou **Produtos**.

Avançar

Avançar

Avançar

Avançar

Avançar

Avançar

Avançar

Avançar

Avançar

Avançar

Avançar

Avançar

Avançar

Avançar

Avançar

Avançar

Avançar

Avançar

Avançar

Avançar

Avançar

Avançar

Avançar

**Não utilizar Evento**  
Avançar

Avançar

Avançar

: Para gerar o financeiro, este parâmetro deve estar habilitado, mas neste caso, não deve ficar habilitado este parâmetro, pois não é gerado financeiro.

Avançar

Como no exemplo do ‘Fin – Faturamento 1/6’ não encontra-se habilitado o campo: Fatura o Movimento, nenhum destes campos ficam habilitados para edição, mas ao habilitar o parâmetro, Fatura Movimento, todos estes parâmetros que pertencem ao ‘Fin – Faturamento 2/4’ ficam habilitados para as devidas parametrizações.

Avançar

Avançar

Avançar

Passar pelos campos 5/6 e 6/6 sem nenhuma alteração também e em seguida:

Avançar

Este campo Natureza, deve estar marcado em Edição como: **Não Edita**

Avançar

Avançar

Tipo de Documento Escrituração: Caso a NF seja **Estadual**, o código do Modelo  do Tipo de Documento , deve ser **55** , caso contrário, deve ser outro código.

Conforme mostrado abaixo pelo print do Tipo 01 – NF que encontra-se inserido em Tipo de Documento Escrituração

Avançar

Avançar

NF – Municipal, tem que estar integrado, pois no nosso exemplo, a NF usada é a Municipal e não a Estadual.

Avançar

Tributação (ISS) Imposto sobre serviços

O campo **Fórmula da base de cálculo** é obrigatória a existência de uma formula neste campo.

Avançar

Em tributação do item, encontra-se vinculado o ISS, neste caso não é usado nenhuma Tributação para o Movimento.

Avançar

Avançar

Avançar

Avançar

Avançar

Avançar

Avançar

É visualizada na tela um LOG com todas as alterações feitas no Tipo de Movimento e em seguida >>Avançar.

Concluir

Em seguida, o assistente volta para o Wizard do cadastro do Tipo de movimento , selecionar a opção : Avançar e em seguida > Última Etapa.

Gerado um log com todas as alterações. Avançar

Concluir

Sim

**(TOTVS Educacional)**

Gerar Lançamento

Anexo > Parcela>>Editar a Parcela a ser gerada

Serviço vinculado: **MENSALIDADE**

Editar o tipo de serviço no TOTVS Educacional.

Verifique se o Produto criado no TOTVS Gestão de Estoque e Faturamento está vinculado ao serviço do TOTVS Educacional. Esta informação é obrigatória para geração de movimentos.

Editar o tipo de serviço do TOTVS Gestão de Estoque e Faturamento, basta clicar sobre a descrição do Serviço. Verifique as configurações do Serviço como mostrado abaixo:

Tipo: SERVIÇO e ULTIMO NÍVEL

Na Aba ‘Informações por Filial’ verifique se a filial à ser utilizada para geração de movimento está informada.

Em Anexo>>Tributos por Município, verifique se o Estado e Município estão informados de acordo com tributos. Verifique também o Código do Serviço no Município. Todos os tributos devem ser informados.

Em Anexo>>Dados Fiscais por UF, verifique se o estado está informado

Salve o registro de serviço, caso tudo esteja corretamente configurado.

Após todas as conferências, entre novamente na parcela do contrato do aluno e gere o Lançamento Financeiro.

Lançamento gerado com sucesso

Editar o lançamento clicando sobre sua Referência: **14780**

Em Anexo>>Boletos é possível verificar a referência de boleto gerado

Para gerar o movimento à partir do TOTVS Educacional, siga os passos abaixo:

Escolha o Tipo de Movimento criado anteriormente, escolha qual será a data, presente no Lançamento Financeiro, que será inserida como emissão do movimento.

Informe a data inicial e final da emissão do lançamento para que o sistema filtre os registros. Escolha o filtro apropriado para trazer os registros.

Em nosso caso, utilizei um filtro simples trazendo somente a referência do boleto gerada para nosso aluno.

Após configurações, Clique em avançar e execute o processo

Após execução, o movimento será gerado corretamente como pode ser visto no TOTVS Gestão de Estoque e Faturamento

Obrigado.
