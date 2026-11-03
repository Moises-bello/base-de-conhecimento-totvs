---
content_hash: 7eec3b47a5f6eab9c7efac2dff74a05a028a9f6615709e9502f38ee45e3b6a73
fetched_at: '2026-06-29T00:10:51.321766+00:00'
page_id: '566470804'
product: rm
source: tdn-rm
title: Portal de Imóveis - Backend - Globais - Metas de Comissão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=566470804
version: 17
---

# **Introdução**

---

Visando providenciar um cálculo de comissão de acordo com os descontos dados pelo corretor no momento da venda, foi criado o cadastro de metas de comissão, possibilitando atribuir valores percentuais nas retiradas de acordo com os percentuais de desconto aplicados nas vendas.

# **Procedimentos para utilização**

---

Para acessar o menu de metas de comissão é preciso primeiramente conceder permissão no grupo de usuários que irá acessar o cadastro como mostra a figura abaixo:

Após salvar a permissão, o cadastro de metas de comissão poderá ser encontrado em *Backend / Globais / Metas de Comissão*

# **Cadastrando metas com regra de utilização de desconto: PROPOSTA**

---

Esta regra utiliza na faixa de desconto (um %) para retirada de comissionamento, possui como referência o **desconto nominal da proposta de venda.**

Acesse o Cadastro do Empreendimento > edite o empreendimento que está sendo parametrizado > Acesse a Guia: Comissão.

Ao acessar este menu, deverá ser parametrizado o Percentual % Limitador que será utilizado no cálculo para retirada de comissionamento.   
Neste Exemplo: A regra de utilização de desconto será realizado na Proposta.  
Selecionando o Empreendimento que será vinculado a meta de comissão (ao final do cadastro Clique em salvar).

### **Exemplo prático**

Neste exemplo observe que o campo: Percentual de Comissão (foi informado o percentual da comissão de10%):  
Marque a opção: Permite descontar comissão do corretor. Salve estas alterações;

Em seguida Foi realizada a inclusão de uma proposta com o valor de R$ 141.000,00  
Observe que nesta proposta as opções de Comissão (C) encontram-se marcada, ou seja, as somas dos cálculos dos componentes irão ser somados para que o sistema possa realizar o cálculo.  
Ao clicar no botão desconto, será apresentada a tela onde será informado o % de desconto sobre o valor.  
Após clicar em aplicar, basta salvar a proposta.

Ao acessar a visão da tela de Propostas, observe que será gerado a Comissão (1). Observe que a comissão apresenta este numeral 1, o que indica que existe uma comissão para esta proposta gerada.

Observe como é apresentado o resultado da comissão no sistema e o entendimento deste cálculo:

Valor da Proposta: Valor que será utilizado para o cálculo da comissão.  
  
Veja em nosso Exemplo como ficou:

Valor da Proposta: R$ 141.000,00  
Valor do Percentual do Limitador 5 % - Valor do percentual de desconto Especial da Proposta 6 % =  1%  
Este resultado de 1% - 10% (comissão do empreendimento) = 9% que será o desconto para geração da comissão pago pela empresa.  
  
R$ 141.000,00 – 9% = R$ 12.690,00

# **Cadastrando metas com regra de utilização de desconto: VALOR DO VPL (\* Valor Presente Líquido)**

---

Para realizar esta parametrização realiza-se as configurações abaixo:

Acesse os Parâmetros > Globais > Metas de Comissões

Ao acessar este menu, deverá ser parametrizado o Percentual % Limitador que será utilizado no cálculo para retirada de comissionamento.

### **Exemplo prático**

Utilizaremos a regra de utilização de desconto será realizado no valor do VPL.  
  
Acesse o Cadastro do Empreendimento > edite o empreendimento que está sendo parametrizado > Acesse a Guia: Comissão.  
No campo: Percentual de Comissão (informe o percentual da comissão) exemplo: 5%  
Marque a opção: Permite descontar comissão do corretor. Em seguida salve estas alterações;

Foi realizada a inclusão de uma proposta com o valor de R$ 14.970,00  
Observe que nesta proposta as opções de Comissão (C) encontram-se marcada, ou seja, as somas dos cálculos dos componentes irão ser somados para que o sistema possa realizar o cálculo.  
Ao clicar no botão desconto, será apresentada a tela onde será informado o % de desconto sobre o valor.  
Após clicar em aplicar, basta salvar a proposta.

Ao acessar a visão da tela de Propostas, observe que será gerado a Comissão (1). Observe que a comissão apresenta este numeral 1, o que indica que existe uma comissão para esta proposta gerada.

Observe como foi apresentado o resultado da comissão no sistema e o entendimento deste cálculo:

Valor da Proposta: Valor que será utilizado para o cálculo da comissão.  
  
Veja em nosso Exemplo como ficou:

Valor da Proposta: R$ 14.970,00

Cálculo:

Valor do percentual do VPL é de  0,20 %, ou seja, total do VPL 100% subtraído pelo valor do VPL da proposta o que resulta em: 99,80%

Neste momento o sistema irá validar 2 situações:

**1-** Se o resultado da subtração do % do VPL (informado na proposta) for **menor** que o % do Limitador (então o sistema utilizará o % informado no campo comissão do empreendimento para o cálculo):

Exemplo:   
Valor do desconto Especial: 0,20% (VPL) - 2,00% (Valor do Limitador) = -1,80  
Neste caso será utilizado para cálculo o valor do % informado no campo comissão do empreendimento = 5%  
Logo o resultado será:

Valor da Proposta = R$ 14.970,00 – 5% = R$ 748,50

**2-** Se subtrair o valor do % do VPL **(informado na proposta)** pelo % do Limitador e o resultado for = (igual)  ou maior (>) que o % de desconto informado na comissão do empreendimento **(então não haverá desconto de comissão):**

Veja na imagem:

Informado um valor de desconto de 7 %

**3-** Ao visualizar o menu Comissão desta proposta salva, é observado que o sistema não apresentará valor gerado para esta comissão:

Observe no exemplo abaixo por que isto ocorreu:

Valor do desconto Especial: 7% (VPL) - 2% (Valor do Limitador) = 5%  
Este resultado de 5% será subtraído pelo valor do % informado no campo comissão do empreendimento = 5%  
Logo o resultado será: (5% - 5%) = 0%

Ou seja, o sistema não irá calcular o valor do % de comissão para esta proposta

#### ***\* VPL =Valor Presente Líquido (indicador financeiro que demonstra valor presente de fluxos como: entradas, saídas, investimentos, calculos de comissões, etc.***

Importante:

O portal utiliza uma ordem (hierárquica para verificação destes  %)

- % de Comissão do empreendimento (utilizado neste nosso exemplo);

- % de comissão parametrizado no cadastro do usuário que está acessando o portal;

- % de comissão parametrizado no cadastro da Imobiliária

- % de comissão do Grupo do usuário

# **Metas de comissão por Bloco**

---

A partir da versão 12.1.2205 será possível definir metas de comissões específicas para blocos do empreendimento. Desta forma podemos ter no mesmo empreendimento, diversas metas de comissão, com características pertinentes a cada bloco.

Na imagem acima, temos, na mesma meta de comissão a divisão entre dois empreendimentos e blocos distintos.

É importante ressaltar que não será possível termos metas de comissão diferentes para os mesmos blocos.

Caso o intuito da meta de comissão seja um cadastro global, ou seja, para o empreendimento e todos os seus blocos sem distinção, basta marcar o Empreendimento em questão. Ao marcar o empreendimento, todos os blocos serão marcados automaticamente.

Veja o vídeo abaixo:
