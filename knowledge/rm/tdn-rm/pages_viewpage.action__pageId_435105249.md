---
content_hash: 48049e28c17c5e7adbb0802d8ef11d2c077cb53e667837d7f4892760397bec78
fetched_at: '2026-06-29T00:09:49.187037+00:00'
page_id: '435105249'
product: rm
source: tdn-rm
title: Portal do Cliente - PDC - Situação Financeira
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105249
version: 35
---

### **Descrição**

---

Traz mais usabilidade e segurança com uma nova Plataforma para Boletos de Cobrança.  
Com a nova plataforma, a estrutura de páginas do portal foi alterada para apenas uma visualização deixando a usabilidade e acesso do cliente simplificado.

**Procedimentos para Utilização**

---

O cabeçalho passa a ter a opção de alterar a Data Base e consequentemente o processo de recalculo de correção Monetária, juros Contratual, multa ou descontos.   
O processo de cálculo da Data Base possui as seguintes consistências:

* Poderá alterar para data futura desde que o sistema tenha índice de reajuste cadastrado para a data informada.
* Não poderá informar uma data base anterior à data atual.

As informações dos contratos serão exibidas da seguinte forma:

* Cabeçalho de cada registro da árvore de contrato:
  + Nº da Subunidade;
  + Unidade;
  + Empreendimento;
  + Nº do Contrato;
  + Cod. Contrato;
  + Valor Total Financiado;
  + Valor Total Pago;
  + Saldo Devedor do Contrato;

**Valores de parcelas de MCMV não são demonstrados no PDC, pois são valores pagos pela caixa.**

Os contratos serão exibidos somente de vendas efetivadas, com contrato gerado e com lançamentos financeiros gerados e desbloqueados.   
Ao expandir um contrato, será exibido detalhes das parcelas do contrato, da seguinte forma:

* Data de Vencimento;
* Comprador (este campo apenas será exibido se houver mais de um comprador);
* Descrição do Tipo de Componente;
* Nº da Parcela;
* Nº do documento?;
* VR Parcela;
* VR Juros;
* VR Multa;
* VR Desconto;
* VR Atual (liquido);

Será permitido selecionar mais de um lançamento financeiro, mesmo que vendas diferentes. No rodapé da página serão exibidos os totalizadores dos campos:

* VR Parcela;
* VR Juros;
* VR Multa;
* VR Desconto;

Além dos campos totalizadores serão exibidos o total de parcelas selecionadas e também o total valor líquido das parcelas selecionadas .

**Parâmetros:**  
Para as funcionalidades do Portal do Cliente, existe os seguintes parâmetros para o Totvs Incorporação e para o Totvs Gestão Financeira:

* Parâmetros do Financeiro estarão disponíveis no caminho *Contas a Receber>>Integração Bancária*:

* + **Convênio padrão para Registro Online:** A geração de um novo boleto com registro online precisa de um convênio bancário padrão que deverá ser estabelecido nos parâmetros financeiros. O usuário só poderá escolher entre convênios que tenham a opção de Registro online marcado. Não permitir desmarcar a configuração de registro online do convenio que esteja sendo utilizado na parametrização; Não permitir desativar o convenio ou a conta financeira configurada no registro online do convenio que esteja sendo utilizado na parametrização;

* Parâmetros do Incorporação estão disponíveis nos seguintes caminhos:

*[Imobiliária >> Portal do Cliente >> Relatórios](https://tdn.totvs.com/pages/viewpage.action?pageId=435105047)*

* **Exibir Valores Sumarizados do Contrato:** Permite exibir ou não os campos de "Valor Total Financiado Atualizado", "Saldo Devedor" e "Valor Total Pago" da visão de Situação Financeira

**Boletos:**

1. **Permite antecipação de pagamento:**Este parâmetro permite a incorporadora indicar se o Portal TIN deve ou não disponibilizar parcelas financeiras com vencimento futuro para antecipação do pagamento. Para o correto funcionamento do recurso de Antecipação de Pagamento, o recurso de reajuste online do financeiro deve estar ativado para cálculo de valores contratuais(Juros e CM), caso contrário não haverá atualização dos valores contratuais.
   1. **Pode antecipar, mesmo com parcela atrasada:** Marque esta opção para permitir que o cliente possa antecipar o pagamento das parcelas vincenda (a vencer), mesmo que ele tenha parcelas vencidas, em aberto.
2. **Permite Gerar Novo Boleto para Parcelas Vencidas e do Mês:** nem todas as empresas permitem que sejam gerados novos títulos para parcelas já vencidas sendo necessário a parametrização para que cada cliente estabeleça seus próprios critérios

Para usar o recurso de Antecipação de Pagamento, alguns parâmetros são necessários estar devidamente configurados. Caso contrário não haverá atualização dos valores contratuais. Os parâmetros são:

* + - Parâmetros TOTVS Incorporação  
      *Imobiliária >> Contrato*  
      - Permitir reajustar parcelas enviadas a banco no modelo PRICE (habilitado)   
      - Não ALTERAR parcelas enviadas ao banco, no modelo de cálculo PADRÃO (desabilitado)  
      *Contrato >> Plano Financiamento*  
      - Tipo de deságio do Modelo de cálculo Pré-Fixado (Price e Sac). (Informado “Valor presente meses”)
    - Parâmetros TOTVS Gestão Financeira  
      Financeiro >> Contas a Receber:  
      - Permitir alterar lançamentos a receber remetidos ao banco (habilitado)  
      *Financeiro >> Integração imobiliária:*- Permitir reajustar lançamentos registrados ou remetidos ao banco na baixa manual e Rec. Via cheque (habilitado)  
      - Reajusta os valores de integração dos lançamentos até a data de reajuste" (habilitado)

* 1. **Opções de pagamento para as parcelas:**Este parâmetro define se novos boletos ou a antecipação de boleto será feita pelo processo de registro online ou pelo processo de gerar boletos não registrados. Abaixo temos uma explicação de cada item:
     + **Registro Online**: A geração do boleto é feita pela entidade bancária.
     + **Pix TPD:** O Pix para pagamento desse boleto é gerado diretamente na entidade bancária cadastrada para o cliente, sem a intermediação de nenhuma outra entidade bancária.
     + **Registro Online / Pix TPD**: São geradas as duas opções de pagamento acima, cabendo ao cliente escolher a que melhor lhe atende.
  2. **Relatório para impressão de boletos não registrados:** Neste parâmetro deve ser selecionado o relatório do RM Report's, que será a base para a geração de boletos. É importante lembrar que este relatório precisa ter como parâmetros os campos: COLIGADA, IDLAN, DATAEMISSAO, DATAVENCIMENTO, VALORPARCELA, NOSSONUMERO, IPTE, CODIGOBARRAS.
  3. **Exibir todo o Plano de Financiamento:** Na visão da situação financeira de contrato o PDC irá exibir para o comprador logado toda a visão do plano de financiamento. **Observação:** Caso deseje modificar a versão do comprador no PDC, deverá ser criado um filtro de perfil ou de usuário que será executado para a visão da situação financeira, sendo que o filtro de usuário tem prioridade sobre o filtro de perfil. Para a criação do filtro deverá ser utilizada a tabela XVENDAPARCELA (que existe somente na versão revitalizada do TIN) ou a tabela XPARCELAPAGAMENTO (para bases não revitalizadas).

O uso da opção de Registro Online  no Portal só poderá ser utilizada se o convênio padrão do Gestão Financeira estiver cadastrado.

**Processo de Impressão de Boleto**  
Na nova plataforma estará disponível para o usuário na opção  "Imprimir Boleto", que estará visível apenas quando usuário clicar em abrir qualquer contrato. Após selecionar qualquer lançamento e clicar no botão de impressão de boleto os seguintes processos serão realizados pelo Portal:

* **Reimprimir Boleto:** apenas reimprime o boleto usando o relatório padrão configurado no convênio do Gestão Financeira;
  + O usuário deve selecionar as parcelas com vencimento menor ou igual a data atual para gerar a 2º via.
  + A 2º via será gerada via Serviço Financeiro, utilizando relatório padrão parametrizado no convenio do Gestão Financeira.
* **Gerar Novo Boleto:** gera um boleto do tipo "Não Registrado", ou seja, que não terá comunicação com o banco.
  + Caso os parâmetros "Permite Antecipação de Pagamento" ou "Permite gerar novo boleto para parcelas vencidas"  estiverem marcados, e o tipo do boleto configurado para Não Registrado o portal irá gerar um boleto baseado no relatório configurado nos parâmetros do Incorporação.
  + O usuário deve selecionar as parcelas  desejadas onde o sistema pode apresentar todas as parcelas futuras do plano, conforme parâmetro "Permite Antecipação de Pagamento", ou apenas as parcelas em aberto até a data atual do sistema.
  + Caso o usuário selecione parcelas vencidas o sistema poderá gerar um novo boleto com todos os valores atualizados  (CM + juros do Contrato + Multa+ Juros de Mora) desde que o parâmetro "Permite gerar novo boleto para parcelas vencidas" esteja marcado.
* **Gerar Boleto Agrupado:** gera um boleto único para todas as parcelas selecionadas, somando o valor total das mesmas.
  + Caso o parâmetro **"Permite Antecipação de Pagamento"** estiver habilitado, associado a geração de boletos do tipo "Registo Online" o portal agrupará todas as parcelas selecionadas em um único boleto para a mesma data de vencimento.
  + Caso o parâmetro **"Permite Gerar Novo Boleto para Parcelas Vencidas e do Mês"** estiver habilitado, associado a geração de boletos do tipo "Registo Online" o portal agrupará todas as parcelas selecionadas em um único boleto para a mesma data de vencimento.
  + O(s) novo(s) boleto(s) será (ão) gerado (s) via Serviço Financeiro e conforme convênio padrão parametrizado no financeiro. Conforme o banco associado ao convenio o sistema poderá apresentar o boleto já gerado e pronto para a impressão ou abrir a tela do banco de geração do boleto, pois isso dependerá dos recursos de integração disponibilizados por cada banco.

A impressão de boletos pela nova plataforma e totalmente automática não tendo a influencia do usuário na escolha do processo, ou seja, o sistema avalia a parcela e os parâmetros configurados e demonstra para o usuário um modal com os boletos que serão gerados pelo sistema.  
Quando usuário clicar em gerar boleto será sugerido para o usuário o download dos boletos.

Parâmetro - Permite Antecipação de Parcelas em Atraso.

**VERSÃO 12.1.34 em diante.**

Criado o parâmetro - Permite antecipação de parcelas em Atraso.

Independente do parâmetro acima estar marcado, o cliente tem a opção de antecipar parcelas futuras e da seguinte forma:

* Qualquer parcela
* Da primeira parcela para última ( Só pode antecipar a próxima parcela que irá vencer em diante. )
* Da última parcela para primeira ( Só poderia antecipar da última parcela para primeira.)

Caso o parâmetro de ordem não estiver sendo obedecido no portal, uma mensagem ao tentar gerar o boleto aparece (Obs.: A mensagem muda a descrição da ordem conforme o que for escolhido no parâmetro dentro do RM).

Não exibir Juros , Multa e Desconto

### 📌 Melhoria – Novo parâmetro para ocultar campos de Juros, Multa e Desconto no PDC e APP Meu Imóvel

**Versão:** 12.1.2506 ou superior

#### O que mudou?

Foi disponibilizado um novo parâmetro no módulo **Gestão de Imóveis** que permite **ocultar os campos de Juros de Mora, Multa e Desconto** nas telas do **Portal do Cliente (PDC)** e do **APP Meu Imóvel**.

#### Benefícios

* Maior controle sobre as informações exibidas aos clientes finais.
* Simplificação da interface do PDC e do APP Meu Imóvel, quando a empresa não negocia juros, multa ou desconto diretamente.
* Adequação a diferentes políticas comerciais e de relacionamento com clientes.

#### Como configurar?

1. Acesse: **Parâmetros > Gestão de Imóveis > Portal do Cliente**.
2. Marque a opção: **Não exibir juros de mora, multa e desconto**.
3. Salve a configuração.

#### Resultado

* Ao ativar este parâmetro, os campos de **Juros de Mora, Multa e Desconto** deixam de ser exibidos automaticamente nas telas do **Portal do Cliente (PDC)** e do **APP Meu Imóvel**.

#### Observações

* Esta configuração afeta **somente a exibição** dos campos, não alterando o cálculo financeiro do sistema.
* Disponível a partir da versão **12.1.2506**.
TELA NOVA SITUAÇÃO FINACEIRA

***Observação : A tela de Situação Financeira abaixo esta liberada na versão 12.1.2502 em Diante.***

Exemplo de marcação da Primeira para a última:

Neste exemplo , marcado o Portal do Cliente - Incorporação

Situação Financeira

A mensagem:

Calcular valor líquido

### **Alteração no Cálculo dos Valores Líquidos na Tela de Situação Financeira**

Ao acessar a tela de **Situação Financeira**, os valores líquidos dos lançamentos não serão mais calculados automaticamente para todas as parcelas. Inicialmente, esses campos aparecerão sem valor.

Para visualizar os **valores líquidos**, o usuário deverá **selecionar as parcelas desejadas** (ou todas, se preferir) e, em seguida, clicar no botão **"Calcular"**. O sistema realizará o cálculo apenas para as parcelas selecionadas, exibindo os respectivos valores líquidos.

Esse mesmo procedimento se aplica ao processo de **Geração de Cobrança**: os valores líquidos só serão calculados para as parcelas selecionadas após acionar o botão **"Calcular"**.

Imagem Situação Financeira Portal do Cliente ( Versão 12.1.2410 e anteriores )

|  |  |
| --- | --- |
|  | Informações Complementares |

* [Portal do Cliente - PDC - Situação Financeira x Protheus](http://tdn.totvs.com/pages/viewpage.action?pageId=453294101)

---

Se houver mais de um boleto a ser gerado fique atento aos pop'p que serão abertos, pois alguns navegadores bloqueiam a geração de varias abas, sendo assim é necessário autorizar a exibição para imprimir todos boletos.

0Possíveis cenários de Antecipação ou reimpressão de boletos |

De acordo com os parâmetros abaixo, podemos ter vários cenários para reimpressão (2ª via) e antecipação.

Os parâmetros estão no Totvs Incorporação:

* Permite antecipação de Pagamento.
* Permite gerar novo boleto parcela vencida e do mês.

**Primeiro cenário:**

* Permite antecipação de Pagamento. (Desmarcado)
* Permite gerar novo boleto parcela vencida e do mês. (Desmarcado)

Com esse cenário, é possível gerar o boleto até o mês atual. Hoje só busca o boleto do vencimento selecionado e não permite gerar mais de um boleto para essa configuração, mas permite gerar mais de um boleto para registro on-line. Boletos remetidos não serão reimpressos nessa configuração. Apenas boletos não emitidos ou não registrados podem ser reimpressos.

**Segundo cenário:**

* Permite antecipação de Pagamento. (Marcado)
* Permite gerar novo boleto parcela vencida e do mês. (Desmarcado)

O cliente só pode emitir 2ª via de parcela até a data atual da competência. A vencer pode gerar boleto na data solicitada caso não exista na base. Se antecipação, verifica se existe boleto na data solicitada. Se não existir, gera boleto e chama o relatório (não registrado) ou o registro online do boleto. Se já existir boleto na data, emitir a segunda via.

Observação: Não permite gerar mais de um boleto para essa configuração, mas permite gerar  mais um boleto para registro on-line.

Quando o status do boleto é não registrado somente é permitido gerar um boleto. A seguinte mensagem será mostrada:

**Terceiro cenário:**

* Permite antecipação de Pagamento. (Desmarcado)
* Permite gerar novo boleto parcela vencida e do mês. (Marcado)

Se a parcela estiver vencida, verifica se existe boleto na data solicitada. Se não existir, gera boleto e chama o relatório (não registrado) ou o registro online do boleto. Se já existir boleto na data, emitir a segunda via. Se não for parcela vencida, emitir a segunda via do boleto (relatório) para o boleto existente no Financeiro. Se existir mais de um boleto no Financeiro, buscar o do vencimento.

**Quarto cenário:**

* Permite antecipação de Pagamento. (Marcado)
* Permite gerar novo boleto parcela vencida e do mês. (Marcado)

Verifica se existe boleto na data solicitada. Se não existir, gera boleto e chama o relatório (não registrado) ou o registro online do boleto. Se já existir boleto na data, emitir a segunda via do boleto (relatório) para o boleto existente no Financeiro. Se existir mais de um boleto no Financeiro, buscar o do vencimento.

**Quinto Cenário:**

* Novos boletos serão gerados do tipo: Registro Online

Para este cenário é necessário importar um certificado digital e configurar o convênio da conta caixa, conforme exemplo abaixo:

E também nos parâmetros financeiros, associar o convênio utilizado.

Observação: Somente utilizando registro online, será possível realizar o agrupamento de boletos pelo PDC.

No PDC temos os seguintes grupos de parcelas:

* **Reimprimir**: São parcelas que já possuem boletos registrados e sua impressão pode não conter a atualização de Juros e Multa.
* **Sem boleto Emitido**: São parcelas que não possuem boletos registrados.
* **Parcelas Agrupadas**: São parcelas futuras em antecipação, elas serão agrupadas em um único boleto.
* **Novos**: Pode conter lançamentos vencidos com data de vencimento atualizada junto com os cálculos de Juros e/ou multa, ou lançamentos futuros para antecipação.

Abaixo segue uma tabela entre a combinação de parâmetros e seus efeitos no sistema:

| ( ) Exibir todo o plano de financiamento ( ) Permite antecipação de pagamento ( ) Permite gerar novo boleto parcela vencida e do mês | Filtra parcelas vencidas até o mês atual. Exibe os grupos de "Reimprimir" e "Sem Boleto Emitido". |
| --- | --- |
| (X) Exibir todo o plano de financiamento () Permite antecipação de pagamento () Permite gerar novo boleto parcela vencida e do mês | Filtra todas parcelas. (Permite o filtro por perfil.) Exibe os grupos de "Reimprimir" e "Sem Boleto Emitido", para parcelas vencidas até o mês atual. Exibe o grupo "Agrupadas" para todas as parcelas futuras a vencer. Gera um boleto unico para as parcelas selecionadas. (Registro on-line) |
| () Exibir todo o plano de financiamento (X) Permite antecipação de pagamento        ( ) Registro on-line        (X) Não registrado () Permite gerar novo boleto parcela vencida e do mês | Filtra todas parcelas. Exibe os grupos de "Reimprimir" e "Sem Boleto Emitido", para parcelas vencidas até o mês atual. Exibe o grupo "Novos" para todas as parcelas a vencer. Um único boleto por parcela selecionada, se não existir boleto para o lançamento. |
| () Exibir todo o plano de financiamento (X) Permite antecipação de pagamento        (X) Registro on-line        ( ) Não registrado () Permite gerar novo boleto parcela vencida e do mês | Filtra todas parcelas. Exibe os grupos de "Reimprimir" e "Sem Boleto Emitido", para parcelas vencidas até o mês atual. Exibe o grupo "Agrupadas" para todas as parcelas a vencer. Gera um boleto unico para as parcelas selecionadas. (Registro on-line) |
| () Exibir todo o plano de financiamento () Permite antecipação de pagamento (X) Permite gerar novo boleto parcela vencida e do mês         ( ) Registro on-line        (X) Não registrado | Filtra parcelas vencidas até o mês atual. Exibe o grupo "Novos" para todas as parcelas a vencidas até o mês atual. Um único boleto por parcela selecionada, se não existir boleto para o lançamento. |
| () Exibir todo o plano de financiamento () Permite antecipação de pagamento (X) Permite gerar novo boleto parcela vencida e do mês         (X) Registro on-line        ( ) Não registrado | Filtra parcelas vencidas até o mês atual. Exibe o grupo "Agrupadas" para todas as parcelas a vencidas até o mês atual. Gera um boleto unico para as parcelas selecionadas. (Registro on-line) |
| () Exibir todo o plano de financiamento (X) Permite antecipação de pagamento (X) Permite gerar novo boleto parcela vencida e do mês         ( ) Registro on-line        (X) Não registrado | Filtra todas parcelas. Exibe o grupo "Novos" para todas as parcelas a vencer e vencidas até o mês atual. Um único boleto por parcela selecionada, se não existir boleto para o lançamento. |
| () Exibir todo o plano de financiamento (X) Permite antecipação de pagamento (X) Permite gerar novo boleto parcela vencida e do mês         (X) Registro on-line        ( ) Não registrado | Filtra todas parcelas. Exibe o grupo "Agrupadas" para todas as parcelas a vencer e vencidas até o mês atual. Gera um boleto unico para as parcelas selecionadas. (Registro on-line) |

Observação

Quando utilizamos o **Registro Online**, os **dados bancários** podem ser anexados ao empreendimento. Caso estiver associado, todo o processo relacionado aos **boletos**, serão consultados primeiramente nos dados bancários do empreendimento. Caso não exista convênio parametrizado nos dados bancários do Empreendimento, será utilizado o convênio do lançamento.

Quando utilizamos somente a opção de **Registro Online**, somente o botão de "Gerar Cobrança" será apresentado. Para a geração dos boletos, basta pressionar este botão, depois de selecionar os lançamentos.

1PIX

 Melhoria que será liberada a partir da versão 12.1.32.  
  
Será possível realizar a geração do PIX diretamente na visão de situação Financeira.  
  
Para que o processo seja realizado com sucesso, algumas parametrizações são necessárias:

1. Acessar o Totvs Gestão Financeira e parametrizar o TPD(**Totvs Pagamento Digital**)

   Importante:

   Para realizar essa parametrização é necessário acionar a equipe do Totvs Gestão Financeira para que todas as devidas orientações seja passadas.
2. Acessar os parâmetros do TCGI, Parâmetros>>Gestão de Imóveis>>Portal do Cliente>>Relatórios - '**Opções de Pagamento para as parcelas:**' 

   Importante:
   * Para que seja possível habilitar o **PIX** ou **Registro Online** é preciso trabalhar com o(s) parâmetro(s) **Permite antecipação de pagamento** ou **Permite gerar novo boleto parcela vencida e do mês**.
   * Quando utilizamos somente a opção de **PIX TPD**, somente o botão de "Gerar Cobrança" será apresentado. Para a geração do QR Code, basta pressionar este botão, depois de selecionar os lançamentos.

Ao realizar a parametrização será disponibilizado no portal do cliente em situação financeira as opções para realizar o Registo online(Boleto) ou PIX. Para a execução do processo é necessário selecionar a parcela que deseja selecionar a opção Boleto(Para registro Online) ou PIX e clicar em **Gerar Cobrança**.

Será apresentado um pop up informando os valores das parcelas selecionadas e ao clicar em baixar será realizar o processo de **Registro Online** ou **PIX.**

Para o PIX será apresentado o QR Code permitindo a captura via câmera ou uma opção para copiar o código.

**No aplicativo Meu Imóvel:**

Assim como no portal, ao realizar o pagamento de uma parcela, será exibido a geração de cobrança. De acordo com a parametrização citada acima, ambas as opções (pagamento por boleto ou pix) ou opções individuais estarão disponíveis.

No momento do pagamento, para parametrização com pagamento apenas com pix, somente a opção pix será mostrada. O mesmo ocorre para o boleto. Em caso de ambas, ambas as opções serão mostradas:

* Ambos (ao clicar na opção "Copiar código QR Pix" ou "Copiar código de barras", o código será copiado para área de transferência):

* Somente Pix (ao clicar na opção "Copiar código QR Pix", o código será copiado para área de transferência):

* Somente código de barras (ao clicar na opção "Copiar código de barras", o código será copiado para área de transferência):
