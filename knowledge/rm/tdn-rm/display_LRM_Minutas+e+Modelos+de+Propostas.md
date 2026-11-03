---
content_hash: aa18860f4e1cdc2c5abf3c6c000e09bc4bac8cfb1f12847998b395f6ad0baff9
fetched_at: '2026-06-29T00:11:33.194683+00:00'
page_id: '752940616'
product: rm
source: tdn-rm
title: Minutas e Modelos de Propostas
type: documentation
url: https://tdn.totvs.com/display/LRM/Minutas+e+Modelos+de+Propostas
version: 13
---

Baixe aqui o modelo de minuta do contrato para ser importado:  
250

#FF9000Minutas

**Associação de um relatório RM Report nas visualizações de Minutas e Modelos de Proposta.**

---

Com o objetivo de aprimorar a integração entre o Portal de Imóveis e o RM, a partir da versão 12.1.33, disponibilizamos uma nova opção que permite associar um relatório RM Reports na aba "minutas" do empreendimento.

Além disso, a partir da versão 12.1.34, os usuários também terão acesso ao relatório RM Reports na aba "modelos de proposta". As parametrizações para ambas as opções seguem o mesmo padrão.

Para que o relatório do RM seja selecionável na visualização, ele deve atender às seguintes condições:

* Ser um relatório da coligada global;
* Ser um relatório do tipo genérico ou do tipo "Portal de Imóveis".

Uma vez que os relatórios do RM estejam parametrizados dessa forma, eles poderão ser selecionados através da opção "Selecionar RM Report" no botão "..." que está presente ao lado do botão "Enviar Nova Minuta" no painel de ações.

É importante destacar que não será possível selecionar um RM Report se já houver um documento de minuta ou modelo associado. Em outras palavras, se já foi feito o upload de um documento definido como minuta ou modelo, não será possível substituí-lo por um relatório RM Report. Entretanto, é possível excluir a minuta ou modelo existente e adicionar um novo, o que permitirá a seleção e salvamento do relatório RM Report normalmente.

Para facilitar a busca e seleção do RM Reports, foi criado um filtro que permite filtrar por tipo de relatório, como mostrado na imagem abaixo:

**Imprimindo relatório em propostas e contratos:**

No Backend, é possível realizar a impressão dos relatórios RM Reports que estão configurados especificamente para cada empreendimento.

Quando o usuário selecionar a opção **"Contrato > Imprimir"** ou **"Proposta > Imprimir"** no Portal de Imóveis, o sistema exibirá automaticamente o relatório (Report) correspondente ao empreendimento selecionado, funcionando de maneira semelhante à geração da minuta.

Além da visualização e impressão direta, o sistema também permite que o relatório seja salvo em formato Word. Para isso, basta acessar a opção **"Contrato > Salvar em Word"**, possibilitando a edição e armazenamento do documento de forma prática.

**Exibição de tags referentes aos dados do proponente nas minutas e modelos de propostas.**

---

Para facilitar a criação das minutas e modelos de propostas, foram adicionadas tags nos exemplos que se referem aos dados financeiros do proponente.   
É importante observar que as TAGs listadas abaixo estão em "case sensitive". Pode acontecer do usuário incluir uma TAG em maiúscula que não retorne resultados. Nesse caso, é *necessário verificar na lista abaixo* se essa TAG deve ser utilizada em maiúscula ou minúscula, pois cada uma possui sua tratativa específica no sistema.

Para visualizar essas tags e outras que podem ser utilizadas na criação de minutas ou modelos, basta clicar no botão "Mostrar Tags" na tela correspondente.

Segue abaixo a lista completa de tags disponíveis:

Tag para Comissões 2.0

**Estas são as tags que serão utilizadas para listar os dados de Comissões 2.0.**Elas foram definidas para estruturar e padronizar a forma como as informações de comissão serão consultadas e exibidas em modelos de propostas do Poral de Imóveis.  
  
${proposta.comissaoV2.v2.comissoes}

**valor\_total\_comissao\_formatado:** ${proposta.comissaoV2.v2.comissao.valor\_total\_comissao\_formatado}  
**valor\_total:** ${proposta.comissaoV2.v2.comissao.valor\_total}  
**valor\_total\_comissao\_extenso:** ${proposta.comissaoV2.v2.comissao.valor\_total\_comissao\_extenso}

${/proposta.comissaoV2.v2.comissoes}

---

**Empresa – Paga Comisao**

${proposta.comissaoV2.v2.comissoesEmpresa}

**valor\_total\_comissao\_formatado:** ${proposta.comissaoV2.v2.comissaoE.valor\_total\_comissao\_formatado}  
**valor\_total:** ${proposta.comissaoV2.v2.comissaoE.valor\_total}  
**valor\_total\_comissao\_extenso:** ${proposta.comissaoV2.v2.comissaoE.valor\_total\_comissao\_extenso}

${/proposta.comissaoV2.v2.comissoesEmpresa}

---

**Cliente – Paga Na Mesa**

${proposta.comissaoV2.v2.comissoesCliente}

**valor\_total\_comissao\_formatado:** ${proposta.comissaoV2.v2.comissaoC.valor\_total\_comissao\_formatado}  
**valor\_total:** ${proposta.comissaoV2.v2.comissaoC.valor\_total}  
**valor\_total\_comissao\_extenso:** ${proposta.comissaoV2.v2.comissaoC.valor\_total\_comissao\_extenso}

${/proposta.comissaoV2.v2.comissoesCliente}

Tag de parcela

Foram criadas novas tags para serem adicionadas na parametrização da minuta. Essas novas tags têm como função demonstrar o valor da parcela e/ou o valor total sem correção monetária. Isso permitirá uma maior personalização da minuta e atenderá às necessidades específicas de cada empreendimento.   
É importante lembrar que as tags devem ser inseridas na ordem correta para que a minuta seja gerada corretamente.

O Parâmetro Usar valor da parcela PRICE nos relatórios deve estar parametrizado para ”SIM”

As tag’s são:

* qr\_valor\_real
* qr\_subtotal\_real
* qr\_total\_real

É importante ressaltar que há uma diferença entre os valores das tags "proposta.valor\_contrato" e "proposta.valor\_contrato\_real", especialmente quando a proposta contém PRICE/FORMULA, seja com ou sem correção monetária.

Em uma modalidade com componentes cujo modelo de cálculo seja padrão, as tags receberão o mesmo valor. No entanto, se houver componentes com PRICE/FORMULA, a tag "proposta.valor\_contrato" receberá o valor com a soma das parcelas PRICE/FORMULA calculadas.

Por outro lado, a tag "proposta.valor\_contrato\_real" exibirá sempre o valor sem correção monetária, ou seja, o valor original da venda. Portanto, é importante selecionar a tag correta para cada caso específico, garantindo que as informações da minuta ou modelo de proposta estejam precisas e completas.

   
**Exemplo:**  
   
***Proposta sem PRICE/FORMULA com valor total = 100.000***  
***Proposta com PRICE/FORMULA a 1% em 10 x = 105.582,08***  
 

Caso o parâmetro "usar valor das parcelas PRICE" esteja definido como "NÃO" no Portal de Imóveis, então ambas as tags "proposta.valor\_contrato" e "proposta.valor\_contrato\_real" receberão o mesmo valor.

No entanto, se o parâmetro estiver definido como "SIM", as tags mostrarão informações diferentes. A tag "proposta.valor\_contrato" exibirá a soma das parcelas PRICE/FORMULA calculadas, enquanto a tag "proposta.valor\_contrato\_real" exibirá o valor original da venda, sem correção monetária.

É importante lembrar que a escolha correta da tag é fundamental para garantir a precisão das informações apresentadas nas minutas e modelos de proposta. Por isso, é recomendado verificar os parâmetros do Portal de Imóveis e utilizar as tags de forma adequada em cada caso.
