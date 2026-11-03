---
content_hash: 5d2a4d49807428ffe2683f229e0a2821d28ba700e36b3e7185b20ea844b39b29
fetched_at: '2026-06-29T00:10:21.839042+00:00'
page_id: '493647927'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Importador de Baixas (de Lançamentos Financeiros  -
  TIN)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=493647927
version: 69
---

Importador de Baixa - TOTVS Construção Gestão de Imóveis

**Configurações e Funcionalidades.**

Importador de BaixaParâmetros do Importador de Baixa |

# [Parâmetro → Utilitários → Importador de Baixa](https://tdn.totvs.com/display/LRM/Aditivo+Global+-+Importador+de+Baixa)

**O que é o Importador de Baixas?** É uma ferramenta que automatiza a quitação de parcelas em lote no TCGI, lendo arquivos de bancos ou planilhas. Ela substitui o trabalho manual e garante que o financeiro do contrato seja atualizado com precisão.

**Configuração de Tolerância:** Para que o sistema aceite pagamentos com pequenas diferenças (juros, multas ou centavos) sem travar a baixa, você deve definir as **Regras de Tolerância**. Sem isso, qualquer divergência exigirá ajuste manual.

OBS: Quando for realizada a implantação das baixas para qualquer cliente favor não utilizar nenhuma formula para evitar valores divergentes.

* **Mensagem de Erro:** Caso o sistema identifique a divergência, mas os parâmetros de ajuste não estejam definidos, será exibido o alerta:

  > *"ID Imp [X] Item Imp [Y] tem divergência a ser ajustada e o parâmetro para lançar valores de divergência a menor e a maior não estão configurados. Favor ajustar em Utilitários => Importador de Baixa"*
* **Como Resolver:** Para que o sistema processe a baixa automaticamente mesmo com diferenças, acesse **Utilitários | Importador de Baixa | Parâmetros** e defina:

  1. O valor limite para aceitação de divergência.
  2. Os eventos financeiros que receberão a diferença (ex: Evento de Juros para valores a maior).

Em cenários onde o sistema localiza **mais de um lançamento financeiro** compatível com os dados da baixa importada (mesmo contrato/vencimento), a regra de desempate aplicada é:

* **Critério de Proximidade:** O sistema comparará o valor contido no arquivo de importação com o valor de cada lançamento encontrado no banco de dados.
* **Ação Automática:** A baixa será vinculada ao lançamento cujo valor líquido seja o **mais próximo** ao valor informado no arquivo, minimizando assim a geração de resíduos ou necessidade de ajustes manuais.

---

## Modelo De Parametrização - Baixa Parcial

Normalmente utilizamos essas parametrizações para realizar baixas parciais. O sistema interpreta como “baixa com diferença de valores”, pois podem existir várias baixas com valores distintos até que o total da parcela seja completamente quitado e os valores fiquem conciliados corretamente.

## Modelo De Parametrização - Baixa Integral

Para baixas integrais, utilizamos esse modelo para que, caso exista alguma diferença de valor, o sistema gere automaticamente um desconto e realize o arredondamento necessário, garantindo que o lançamento seja baixado sem impedimentos.

## 

Importador de Baixa |

# [Importação de Baixa](https://tdn.totvs.com/display/LRM/Aditivo+Global+-+Importador+de+Baixa)

Criada a funcionalidade de importação de baixas de lançamentos financeiros para contratos de Vendas, Aluguéis e Securitização. Podendo ainda realizar baixas de Parceiros e comparar os valores que compõe as parcelas de componente a componente.

As opções disponíveis para realizar as baixas e localizar os lançamentos financeiros correspondentes são as seguintes:

* Código do Empreendimento
* Código da Unidade
* Código da Subunidade
* **CPF ou CNPJ**
* **Data de Vencimento**
* **Data da Baixa**
* **Valor da Parcela**
* **Valor Baixado**
* Número do contrato de venda
* Número do contrato de aluguel
* Número da venda
* Número do documento
* Nosso número
* Referência do lançamento financeiro no RM
* Coligada do lançamento financeiro RM
* Valor original
* Valor dos juros de contrato
* Valor da correção monetária
* Valor do seguro
* Outros valores (taxas administrativas, etc.)
* Valor do desconto
* Valor da multa
* Valor dos juros de mora

**\*Os campos que estão em negritos são obrigatórios o seu preenchimento no arquivo e devem ser combinados com outros campos para que o sistema possa encontrar a parcela a ser baixada.**

**\*\*Caso seja usado o campo de código de empreendimento na chave, os campos de unidade e subunidades ficam sendo obrigatórios o seu preenchimento.**

**1º  Liberar o Perfil do Usuário para utilização do Importador de Baixas**

TCGI - Gestão de Imvóveis

Utilitários | Importador de Baixas

O cadastro de importador é utilizado para visualizar, alterar ou excluir os itens de baixas que foram importados pelo processo de Importador de Baixas através de arquivo CSV.

Podendo ainda cadastrar manualmente o lançamento a ser baixado

**IDENTIFICADOR** = Preenchido automaticamente

**ID ITEM** = Preenchido automaticamente

**CNPJ/CPF** = Campo obrigatório para preenchimento

**DATA DE VENCIMENTO** = Campo obrigatório para preenchimento

**DATA DA BAIXA** = Campo obrigatório para preenchimento

**VALOR BAIXADO** = Campo obrigatório para preenchimento

**VR. PARCELA . IMP** = Campo obrigatório para preenchimento (Valor Líquido, contém valores de multa, juros de atraso e valores do TIN)

Esta tela é preenchida conforme arquivo com extensão CSV

.

CONTRATO DE VENDA = Não é um campo obrigatório , pois tem contrato de Venda/Aluguel que este mesmo fica em branco, mas no caso acima que tem o código , pode ser incluído no Arquivo CSV de importação.

Processo para importar arquivo de baixas CSV

Selecionar – Importação de Baixas

Processos | Importação do Arquivo de Baixa

Ao habilitar as opções Validar itens do arquivo e Baixar itens validados,é possível informar a Conta Caixa e o Meio de Pagamento que serão utilizados na baixa.

O layout deve ser gravado, para que  tenha a opção de escolher o layout ao entrar no importador. Isso irá possibilitar que o usuário tenha mais de um layout para importar baixas com objetivos diferentes.

Exemplo de configuração do Perfil no RM para Arquivo CSV Simples .

À direita o arquivo CSV com suas colunas na ordem :

* Emprendimento (**Formatar o campo para texto**)
* Bloco (**Formatar o campo para texto**)
* Unidade (**Formatar o campo para texto**)
* CPF (**Formatar o campo para texto**)
* Vencimento (**Formatar o campo para Data Abreviada**)
* Valor Parcela (**Formatar o campo para número**)
* Data Baixa (**Formatar o campo para Data Abreviada**)
* Data Movimento (**Formatar o campo para Data Abreviada**)
* Valor Pago (**Formatar o campo para número**)

Nesta mesma ordem o RM tem que estar configurado , como mostra a imagem á esquerda que informa Empreendimento = 1 por ser o primeiro no arquivo CSV e assim sucessivamente. Não pode haver buraco na numeração, tem que ser sequencial.

Arquivo selecionado e em seguida : Avançar

Neste passo é mostrada uma pré visualização antes que seja executado o arquivo!! Em seguida : Executar

Processo executado

Importado arquivo

Dados importados conforme Layout ( Arquivo CSV )

Na imagem acima mostra os dados no Arquivo CSV e como ficam no RM após sua importação , cada campo com sua definição da posição do Layout pré definido do Perfil .

Exemplo de Importação do Arquivo Completo:

Alguns Campos de exemplo que são informados no Completo que são importados:

* **Número Contrato**
* **Ref . Lançamento**

Lembrando que não pode ser Importado ao mesmo tempo ( Venda / Securitização e Aluguel ) Só podendo ser feita a importação de Venda em separado para ai sim , efetuar a importação de Securitização e sucessivamente Aluguel.

Arquivo de Importação configurado ( Complicado )

Avançar

Pré visualização do Arquivo antes de executar

Processo executado

Importado para o RM o Arquivo

Nesta Importação complete é informado mais campos e Inclusive a Ref do Lançamento já é informado no mesmo.

Lembrando que , se tentar importar Arquivo Completo com Perfil Simples e vice versa ocorrerá erro como é mostrado a baixo :

Selecionado o Perfil SIMPLES e o arquivo COMPLETO ..

Pré – Visualização do Arquivo

Validando Itens após Importação |

# [Validando Itens após importação.](https://tdn.totvs.com/display/LRM/Aditivo+Global+-+Importador+de+Baixa)

**Fluxograma do Processo**

Tipos de Status da Validação

* 0 - Em Aberto
* 1 - Cadastro Inconsistente
* 2 - Cadastro Validado
* 3 - Preparado para Baixar
* 4 - Lançamento de Baixa Não encontrado, não foi encontrado o lançamento financeiro com base no filtro importado.
* 5 - Lançamento Associado, foi encontrado o lançamento a ser baixado
* 6 - Lançamento Baixado
* 7 - Lançamento já Baixado
* 8 - Lançamento com Divergência de Valores, os valores não importados não bate com o valor líquido.
* 9 -  Diversos Lançamentos, se encontrou diversos lançamentos com a mesmo filtro, então o cliente tem que associar manualmente.
* 10 - Lançamento Cancelado, o lançamento encontra-se cancelado.
* 11 - Preparado para Baixar dentro do limite de divergência.
* 12 - Lançamento com Divergência de Valores com baixa parcial
* 13 - Preparado para Baixar dentro com juros e multa de atraso definido no valor baixado maior que o valor parcela
* 14 - Preparado para Baixar dentro do limite de divergência com juros e multa de atraso
* 15 - Preparado para Baixar com o desconto financeiro definido
* 16 - Preparado para Baixar Limite Divergência com o desconto financeiro definido
* 17 -  Preparado para Baixar dentro com juros e multa de atraso definido no valor baixado maior que o valor parcela

**Validando Itens Importados**

Os campos validados :

* **Empreendimento**
* **Contrato**
* **CPF/CNPJ**
* **Nosso Número**
* **Número do Documento**
* **Lançamento**

***Liberar Perfil do Usuário em Incorporação para que possa validar Itens de Baixa.***

# IMPORTAÇÃO COM OS DADOS CORRETOS

Arquivo CSV Importado e Validado pelo TOTVS Incorporação.

Comparativo dos campos do Arquivo CSV com o TOTVS Incorporação

## Empreendimento -  Bloco - Unidade

## CPF/ CNPJ

Selecionar Compradores

## Vencimento – ValorParcela – ValoPago – DataBaixa – Nro Doc - Idlan

Selecionar Lançamento Financeiro

Editar em seguida o Lançamento desejado

Vencimento – Número Documento e IdLan

## Valor da Parcela (Valor Líquido)

Validações feitas – Importando arquivo novamente.

Validando itens de baixa .

Todos itens são verificados e estando todos de acordo ao processar , Lan. Associado TIN é preenchido.

Lançamento foi associado ao registro !

Ao clicar sobre o Lançamento Associado é aberto o Lançamento .

Podendo realizar todos processos referente ao Lançamento.

# SOLUCIONANDO ERRO DE VALIDADOR!

Exemplos de erros ao validar os itens de baixas importados e solução para que possa ser validado o mesmo sem que possa se gerar um atraso para o Cliente.

Exemplo de erro de CPF inexistente.

Validador de Itens de Baixas Importados

Status encontra-se em : Aguardando Validação

Ao validar consta a mensagem : CPF/CNPJ não encontrado

Status passa para : Cadastro Inconsistente

Em Observação é informado o erro para que o Cliente possa efetuar as devidas correções necessárias para que possa validar o arquivo de baixa.

Enquanto não for validado, o Lanç. Associado TIN não fica preenchido.

Neste exemplo, o arquivo foi importado e o **Empreendimento** que foi informado não é o que consta no **Contrato do Cliente** , mas o empreendimento **existe na base de dados**.

Contrato do Cliente encontra-se:

Empreendimento =**2045**

Código do Bloco = 1

Código da Unidade = 000004

Arquivo a ser importado com Código do Empreendimento incorreto = 2046 ( Vendo que no Cliente é 2045 )

Validando item de Baixa

**Ocorre erro** , se o Empreendimento **não existisse na base de dados**  , o erro estaria informando ao Cliente o código errado do Empreendimento , Bloco e Unidade como **mostra abaixo** :

Empreendimento incorreto ( **Não existe na base de dados** )

O Log do Importador já avisa ao Cliente que ocorre um erro no Cadastro do **Empreendimento , Bloco e Unidade**.

Mas no nosso exemplo , o código do Empreendimento existe e o Log avisa erro de**Lançamento de Baixa não encontrado** , a possível solução para o caso é : **Excluindo campos NÃO OBRIGATÓRIOS e fazer a validação até o mesmo ser validado**.

Neste caso ,será excluído ( **Empreendimento , Bloco e Unidade** ) se persistir o erro , continuar exclusão até que o mesmo possa ser validado.

Editando o arquivo depois de importado e excluindo manualmente o Empreendimento 2046.

Refazendo o processo para validar

Validação realizada com sucesso !!

Validando Valores após Importação |

# [Validando Valores após importar arquivo.](https://tdn.totvs.com/display/LRM/Aditivo+Global+-+Importador+de+Baixa)

VALIDANDO VALORES DO IMPORTADOR

Exemplo do Validador do Importador com Valor limite de divergência.

Ref do Lançamento = 20887

Data de Baixa = 25/05/2026 >> coloquei a data maior do que o vencimento para propositalmente gerar o juros e detalhar os valores.

**Neste exemplo temos o seguinte Cenário:**

**Valor Original do Título                    = R$ 10.000,00**

**Juros                                              = R$ 207,9000**

**Multa                                              = R$ 207,9000**

**CM Antes Entrega                                = R$ 0,00**

**Taxa Juros Antes Entrega                       = R$ 0,00**

**Valor Líquido                                     = R$ 10.415,8000**

---

**Valores dos Campos a esquerda =** Estes campos pegam os valores do Arquivo CSV

**Valores dos Campos a direita =**Estes campos comparam os Valores importados com os Campos RM e mostram Diferenças de valores se existirem.

Após feita a validação dos Valores o Campo ( **Campo Central** ) Informa o Valor Original da base de Dados RM e se tive algum valor Divergente entre o **( Esquerdo** com o **Direito** ) nos campos a Direita, são informados os valores da diferença.

# VALOR TOLERÂNCIA DIFERENÇA DE BAIXA

Este campo serve para o cliente configurar uma determinada Tolerância nos valores para que possam ser baixados mesmo com divergência nos valores , desde que estejam dentro da Tolerância configurada neste Campo.

Ou podemos deixar pré-configurado na parametrização

Ambiente | Parâmetros | Gestão de imóveis  | Utilitários

# Exemplo do Validador dentro da Tolerância.

# 

Baixa dia **23/02/2026** ( Baixa neste dia , os valores da Parcela e Baixa ficam dentro da Tolerância )

# Exemplo do Validador fora da Tolerância.

Alterando o campo de Data Baixa para 25/05/2026

Informado para o Cliente : Lançamento com Divergência de Valores.

Valor de Juros e Multa ( Alterados )

Valor ficando R$ 415,8000 acima do Valor da Parcela ( **Ultrapassou R$ 405,8000** ) o valor da Tolerância )

Baixa após Validação do Arquivo |

# [Baixa de Lançamentos - Importador](https://tdn.totvs.com/pages/viewpage.action?pageId=497469694)

## EXEMPLO 01 – BAIXA TOTAL

### **Z1. Conferência dos Valores**

No cadastro do item importado, valide as seguintes informações na tela:

* **Campo: Vr. Parcela Imp.**  
  → R$ 11.111,110
* **Campo: Vr Parcela TIN**  
  → R$ 11.111,100
* **Campo: Valor Baixado**  
  → R$ 11.111,110

📌 **Regra para Baixa Total:**  
Quando o campo **Valor Baixado** estiver **igual ao campo Vr. Parcela (valor da parcela importada)**, o sistema efetuará a **baixa total do lançamento**.

No exemplo apresentado:

* O valor importado corresponde ao valor da parcela.
* Não há diferença de parcela (**Vr. Dif. Parcela = R$ 0,0000**).
* O lançamento será baixado integralmente.

---

### **2. Executar a Baixa**

Após a conferência:

1. Selecionar a **Conta Caixa** correspondente.
2. Clicar em **Executar**.

---

### **3. Resultado Esperado**

Após a execução:

* O campo **Status Atual** ficará como: **Lançamento Baixado**.
* O título será considerado **baixado totalmente**.
* Não haverá geração de diferença, desconto ou juros.

---

**Para que a baixa total ocorra corretamente:**

* Perfil deve estar habilitado para baixa de itens importados.
* Valor Baixado = Valor da Parcela Importada.
* Não pode haver diferença de valores.
* Conta Caixa deve estar informada antes da execução.

## EXEMPLO 02 – BAIXA PARCIAL

### **1. Conferência dos Valores na Tela**

No cadastro do item importado, observar os seguintes campos:

* **Valor Baixado:**  
  → **R$ 11.111,1100**
* **Vr. Parcela Imp.:**  
  → **R$ 6.111,1100**
* **Vr Parcela TIN:**  
  → **R$ 6.111,1100**
* **Vr. Dif. Parcela:**  
  → **R$ 0,0000**

---

### Contexto do Lançamento

Este título **já possuía uma baixa anterior de R$ 5.000,00**.

O valor total do lançamento é:

> **R$ 11.111,1100**

Como já havia sido baixado:

> **R$ 5.000,00**

Restou para baixa:

> **R$ 6.111,1100**

O arquivo importado trouxe exatamente o valor restante, por isso o sistema realizou uma **baixa parcial complementar**, quitando o saldo pendente.

---

### **2. Regra Aplicada pelo Sistema**

Mesmo o campo **Valor Baixado** demonstrando o valor total do título (R$ 11.111,1100), o sistema considera:

* O valor já baixado anteriormente.
* O saldo em aberto.
* O valor importado correspondente ao saldo restante.

Como o valor importado corresponde exatamente ao saldo pendente (**R$ 6.111,1100**), não houve diferença.

---

### **3. Executar a Baixa**

Após validação:

1. Selecionar a **Conta Caixa**.
2. Clicar em **Executar**.

---

### **4. Resultado Apresentado**

Após o processamento:

* O lançamento ficou com status de **Baixado Parcialmente** (considerando o histórico de movimentações).
* O saldo do título foi zerado.
* Não houve geração de juros, multa ou desconto.
* **Vr. Dif. Parcela = R$ 0,0000**.

**Para que a baixa parcial complementar ocorra corretamente:**

* O título pode já possuir baixas anteriores.
* O valor importado deve corresponder exatamente ao saldo pendente.
* Não pode haver diferença de valores.
* Conta Caixa deve estar informada.
* Perfil deve estar habilitado para baixa de itens importados.

Utilzando Aditivo para Divergência de Valores.

# [Aditivo Global - Importador de Baixa](https://tdn.totvs.com/display/LRM/Aditivo+Global+-+Importador+de+Baixa)

Registros com  status **“Divergência de Valores”** na visão de auditoria, tem opção de corrigir o valor no Arquivo CSV , corrigir o valor de Tolerância e ou Rodar o processo para gerar um aditivo de alteração global de valores de parcelas com o valor da divergência. O Aditivo utilizará a mesma parametrização dos componentes para ajuste automático na baixa, (componentes a maior e a menor).Mudando o Status para **Pronto para Baixa.**

Habilitar perfil do usuário para utilizar Aditivo Global ( **05.01.04.08** ) Importador – Ajustar Valores Divergentes Via Aditivo Global

Exemplo da utilização do Aditivo Global em Importador fora da Tolerância – Divergência de Valores

Contrato encontra-se sem nenhum Aditivo cadastrado.

Arquivo importado e com Status : Lançamento com Divergência de Valores

Neste exemplo , Tolerância no máximo de R$ 1,00 Real

O valor de Diferença = R$ 2.64 , fora do limite de Tolerância , fazendo o **Status** ficar igual =**Lançamento com Divergência de Valores**

Tentando efetuar a baixa do Título.

Sistema não deixa efeutar Baixa de Títulos com divergências de valores.

Processos | Ajustar Valores Divergentes dos Itens Via Aditivo Global

Executar Processo

Processo executado com sucesso

Status alterado para : Preparado para Baixar

Verificando se no Contrato do Cliente foi criado o Aditivo com esta Diferença.

Aditivo incluído no Contrato do Cliente

Baixando o Arquivo

Processos | Baixar os Itens do Importador

Status = Lançamento Baixado
